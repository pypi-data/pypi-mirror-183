import math
MAXSYMLEN=7

SYMBOLS= { }
LC=4711
from capasm.assembler import parseFunc,ERROR,clsParsedExpression, \
     clsInvalidOperand

def getSymbol(name):
   try:
      return SYMBOLS[name]
   except KeyError:
      return None

class clsExpression(object):

   EX_NUM=0
   EX_SYM=1
   EX_OP=2

   OP_PLUS=0
   OP_MINUS=1
   OP_DIV=2
   OP_MULT=3
   OP_OR=4
   OP_AND=5
   OP_NOT=6
   OP_MOD=7
   OP_RESIZE=8
   OP_CHS=9
   OP_NONE=10

   def __init__(self):
      super().__init__()

   def addError(self,errnum):
      self.__errors__.append(errnum)
#
#  generate Bytecode
#
#  number
#
   def genNumber(self,value):
      self.__bc__.append([clsExpression.EX_NUM,value])
      self.__lastNumber__=value
      self.__hasSymbols__=False
#
#  symbol
#
   def genSymbol(self,name):
      self.__bc__.append([clsExpression.EX_SYM,name])
#
#  opcode
#
   def genOp(self,op):
      self.__bc__.append([clsExpression.EX_OP,op])
#
#  returns the number of bytes value will occupy
#
   def byteLen(self,value):
      return (1+math.floor(math.log(abs(value))/(0.69314718055994530942*8)))
#
   def makeBytes(self,value,size=None):
      if size is None:
         nBytes=self.byteLen(value)
      else:
         nBytes=size
      b=bytearray(nBytes)
      k=nBytes-1
      for i in range(0,nBytes):
            b[k]= value & 0xFF
            k-=1
            value=value>>8
      return b

#
#  resize a value to a given size
#  positve integers are right padded with zeros
#  negative integers are right padded with 0xFF
#  returns None if size is too small
#
   def resize(self,value,size):
      print("resize ",value, size)
      nBytes=self.byteLen(value)
      if size< nBytes:
         return None
      nPad=size-nBytes
      rVal=value
      for i in range(0,nPad):
         rVal= rVal << 8
         if value < 0:
            rVal |= 0xFF
      print("npad ",nPad," ",rVal)
      return rVal
#
#  scan a character
#
   def getch(self):
      self.__getchCount__+=1
      if self.__getchCount__ == len (self.__exprString__):
         self.__GCH__= "\n"
      else:
         self.__GCH__= self.__exprString__[self.__getchCount__]
#
#  location counter symbol "$"
#
   def LOC(self):
      self.getch()
      self.genNumber(LC)
      return 
#
#  number, which can be ocal, decimal, bcd or hex. Hex numbers must always
#  begin with a digit
#
   def number(self):
      numString=""
      while True:
         numString+=self.__GCH__
         self.getch()
         if "01234567890abcdefABCDEFhHoO#".find(self.__GCH__)< 0:
            break
      value=parseFunc.parseNumber(numString)
      if value is None:
         self.addError(ERROR.E_ILLNUMBER)
         bValue=0
      else:
         bValue=value
      self.genNumber(bValue)
      return 
#
#  ASCII string, which can be either enclosed in " or '
#
   def asc(self):

      value=0
      term=self.__GCH__
      self.getch()
      while self.__GCH__ != term:
         value= value*256 + ord(self.__GCH__)
         self.getch()
         if self.__GCH__== "\n":
            self.addError(ERROR.E_ILLSTRING)
            break;
      self.getch()
      self.genNumber(value)
      return
#
#  symbol name which always begins with a letter
#  
   def symbol(self):
      symName=""
      self.__hasSymbols__=True
      while True:
         symName+=self.__GCH__
         self.getch()
         if " )\n".find(self.__GCH__)>=0:
            break
      if parseFunc.parseLabel(symName,MAXSYMLEN) is None:
         self.addError(ERROR.E_ILL_LABELOP)
         return 
      self.genSymbol(symName)
      return 
#
#  expression base
#   
   def base(self):
#
#     location counter symbol
#
      if self.__GCH__== "$":
         self.LOC()
#
#     number
#
      elif "01234567890".find(self.__GCH__) >=0:
         self.number()
#
#     quoted string
#
      elif self.__GCH__=='"' or self.__GCH__=="'":
         self.asc()
#
#     left paranthesis, begin of a new term
#
      elif self.__GCH__=="(":
         self.getch()
         self.term()
         if self.__GCH__ != ")":
            self.addError(ERROR.E_MISSINGRPAREN)
            return 
         self.getch()
#
#    returned from term, look for a size specifier
#
         if self.__GCH__==".":
            self.getch()
            if  "01234567890".find(self.__GCH__) >=0:
               self.number()
               self.genOp(clsExpression.OP_RESIZE)
               self.__size__=self.__lastNumber__
               if self.__size__ ==None:
                  self.addError(ERROR.E_INVALIDSIZESPEC)
                  return 
      else:
         self.symbol()
      return 
#
#  expression unary, operators are "-" or "~"
#
   def unary(self):
      if self.__GCH__== "-":
         self.getch()
         self.base()
         self.genOp(clsExpression.OP_CHS)
      elif self.__GCH__=="~":
         self.getch()
         self.base()
         self.genOp(clsExpression.OP_NOT)
      else:
         self.base()
      return 
#
#  expression bool, operators are "&" or "|"
#
   def bool(self):
      first=True
      operator=clsExpression.OP_NONE
      done=False
      while not done:
         self.unary()
         if first:
            first=False
         else:
            self.__size__=None
            if operator== clsExpression.OP_AND:
               self.genOp(operator)
               self.__size__=None
            elif operator== clsExpression.OP_OR:
               self.genOp(operator)
               self.__size__=None
         done=True
         if self.__GCH__=="&":
            operator= clsExpression.OP_AND
            done= False
            self.getch()
         if self.__GCH__=="|":
            operator= clsExpression.OP_OR
            done= False
            self.getch()

      return 
#
#  expression factor, operators are "*", "/", "%" (modulo)
#
   def factor(self):

      operator=clsExpression.OP_NONE
      first=True
      done=False
      while not done:
         self.bool()
         if first:
            first=False
         else:
            self.__size__=None
            if operator== clsExpression.OP_MULT:
               self.genOp(operator)
               self.__size__=None
            elif operator== clsExpression.OP_DIV:
               self.genOp(operator)
               self.__size__=None
            elif operator == clsExpression.OP_MOD:
               self.genOp(operator)
               self.__size__=None
         done=True
         if self.__GCH__=="*":
            operator=clsExpression.OP_MULT
            done= False
            self.getch()
         if self.__GCH__=="/":
            operator=clsExpression.OP_DIV
            done= False
            self.getch()
         if self.__GCH__=="%":
            operator=clsExpression.OP_MOD
            done= False
            self.getch()

      return 
#
#  expression term, operators are "+" and "-"
#
   def term(self):

      operator=clsExpression.OP_NONE
      first=True
      done=False
      while not done:
         self.factor()
         if first:
            first=False
         else:
            if operator== clsExpression.OP_PLUS:
               self.__size__=None
               self.genOp(operator)
            elif operator== clsExpression.OP_MINUS:
               self.__size__=None
               self.genOp(operator)
         done=True
         if self.__GCH__=="+":
            operator=clsExpression.OP_PLUS
            done= False
            self.getch()
         if self.__GCH__=="-":
            operator=clsExpression.OP_MINUS
            done= False
            self.getch()

      return 

#
#  parse expression string
#
   def parse(self,expr):
      self.__exprString__=expr
      self.__getchCount__=-1
      self.__GCH__=""
      self.__errors__= []
      self.__size__= None
      self.__bc__= []
      self.__lastNumber__=None
      self.getch()
      exp=self.term()
      if self.__GCH__ != "\n":
         self.addError(ERROR.E_ILLEXPRESSION)
      if len(self.__errors__)==0:
         parsedExpression=clsParsedExpression(self.__bc__,self.__size__, \
            self.__hasSymbols__)
      else:
         parsedExpression=clsInvalidOperand()
      return parsedExpression,self.__errors__
#
#  execute the byte code of an expression
#
   def execute(self,parsedExpression):

      stack=[]
      self.__errors__= []
      size=parsedExpression.size

      for c in parsedExpression.byteCode:
         typ=c[0]
         if typ== clsExpression.EX_NUM:
            stack.append(c[1])
         elif typ==clsExpression.EX_SYM:
            value= getSymbol(c[1])
            if value is None:
               self.addError(ERROR.E_LBLNOTFOUND)
               return None, self.__errors__
            stack.append(value)
         elif typ==clsExpression.EX_OP:
            op=c[1]
            print(stack, op)
            if op==clsExpression.OP_PLUS:
               stack[-2]+=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_MINUS:
               stack[-2]-=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_MULT:
               stack[-2]*=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_DIV:
               if stack[-1]==0:
                  self.addError(ERROR.E_DIVBYZERO)
                  return None, self.__errors__
               stack[-2]//=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_MOD:
               if stack[-1]==0:
                  self.addError(ERROR.E_DIVBYZERO)
                  return None, self.__errors__
               stack[-2]%=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_AND:
               stack[-2]&=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_OR:
               stack[-2]|=stack[-1]
               stack.pop()
            elif op==clsExpression.OP_CHS:
               stack[-1]|=-stack[-1]
            elif op==clsExpression.OP_NOT:
               stack[-1]|= ~ stack[-1]
            elif op==clsExpression.OP_RESIZE:
               value=self.resize(stack[-2],stack[-1])
               if value== None:
                  self.addError(ERROR.E_VALTOOLARGE)
                  return None, self.__errors__
               else:
                  stack[-2]=value
                  stack.pop()
 
      exp=stack [0]
      b=self.makeBytes(exp,size)
      return exp,b,self.__errors__

   def testExp(self,string):
      errors=[]
      print("\nEXPRESSION= ",string)
      parsedExpression,parseErrors=self.parse(string)
      if parsedExpression.typ==clsParsedExpression.OP_INVALID:
         print("Parse errors ",end="")
         for i in parseErrors:
            print(ERROR.messages[i])
         return
      errors.extend(parseErrors)
      value,b,execErrors=self.execute(parsedExpression)
      errors.extend(execErrors)
      print("VALUE= ",value," ",end="")
      for i in b:
          print("{:02x} ".format(i),end="")
      print("")
      for i in errors:
         print(ERROR.messages[i])

eObj=clsExpression()
print("Expected result: 1002")
SYMBOLS['HENRY']= 1000
eObj.testExp('(HENRY)+2')
# 1000
# +1000
# +7
# *3
# + 4711
# ^
# 4407873
# = 100 0011 0100 0010 0100 0001
# |                      11 1111
# = 100 0011 0100 0010 0111 1111
# = 4407935
# +
# = 4418667 (436C6B)
print("Expected result: 4418667")
eObj.testExp('(((HENRY)+(HENRY)+7)*3+$+"ABC"|77)')

# 184
#  33554432
# + 144115188075855872
# +  9
# + 74
# + 63
# + 34
# = 144115188109410484
print("Expected result: 144115188109410484")
eObj.testExp('(2D).4+(2).8D+1001B+4AH+77O+22C')

print("Expected result: 42fe = 17150")
SYMBOLS['TYNBAS']=ord("B")
eObj.testExp('TYNBAS')
eObj.testExp('(TYNBAS)*100H+11111110B')

print("Expected result -1")
eObj.testExp("(-1).8D")
print("Expected result 12610078956637388800")
# 175
eObj.testExp("(0aF#).8D")

#17150
SYMBOLS['AFFE']=ord("B")
eObj.testExp('((AFFE)*100H+11111110B).12')

