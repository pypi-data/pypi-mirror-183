#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
#
# This module contains the regression test driver for the CAPASM software
# (c) 2020 Joachim Siebold
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#--------------------------------------------------------------------------
#
# 28.05.2020 jsi
# - start change log
#
import os
from pathlib import Path
from capasm.assembler import clsAssembler
from capasm.ncas import clsNcas
from capasm.captools import clsLifCreator,fileDiff, clsSymClassGenerator, \
     silentRemove, clsRomCreator,clsAsmSourceFileConverter, \
     clsSymbolFileConverter
from capasm.capcommon import capasmError

ASSEMBLER=clsAssembler()
LIFCREATOR=clsLifCreator()
GENERATOR=clsSymClassGenerator()
ROMCREATOR=clsRomCreator()
ASMCONVERTER=clsAsmSourceFileConverter()
SYMCONVERTER=clsSymbolFileConverter()
NCAS=clsNcas()

#
# Test case specifications ------------------------------------------------
#
# dictionary CAPASM_TEST  { testKey: testSpec ... }
# list       testSpec     [ testDescription, command1, command2, ...]
# list       command      [ method, expected return value, positional params, 
#                            keyword params, exceptMsg]
# list       posParams    [ list of positional parameters ]
# dict       keyParams    { dictionary of key parameters }
# string     exceptMsg    expected message to check certain capasmException
#
CAPASM_TESTS={
   "rom000":  \
         ["Assemble ROM000", 
         [ ASSEMBLER.assemble,False,["rom85/rom000.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "rom000.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["rom000.bin","rom85/rom000.bin"]],
         [silentRemove, False, ["rom000.bin","rom000.lst"]]
         ],
   "romsys1": \
         ["Assemble ROMSYS1", 
         [ ASSEMBLER.assemble,False,["rom85/romsys1.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "romsys1.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["romsys1.bin","rom85/romsys1.bin"]],
         [silentRemove,False, ["romsys1.bin","romsys1.lst"]]
         ],
   "romsys2": \
         ["Assemble ROMSYS2", 
         [ ASSEMBLER.assemble,False,["rom85/romsys2.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "romsys2.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["romsys2.bin","rom85/romsys2.bin"]],
         [silentRemove,False, ["romsys2.bin","romsys2.lst"]]
         ],
   "romsys3": \
         ["Assemble ROMSYS3", 
         [ ASSEMBLER.assemble,False,["rom85/romsys3.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "romsys3.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["romsys3.bin","rom85/romsys3.bin"]],
         [silentRemove,False, ["romsys3.bin","romsys3.lst"]]
         ],
   "rom050": \
         ["Assemble ROM050", 
         [ ASSEMBLER.assemble,False,["rom85/rom050.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "rom050.lst",  "referenceOpt":2}],
         [ROMCREATOR.create,False,["rom050.bin"],{"romSize":8}],
         [fileDiff.testBinFile,False,["rom050.rom","test/rom050.rom"]],
         [silentRemove,False, ["rom050.bin","rom050.lst"]]
         ],
   "rom320b": \
         ["Assemble ROM320B", 
         [ ASSEMBLER.assemble,False,["rom85/rom320b.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "85", \
             "listFileName": "rom320b.lst",  "referenceOpt":2}],
         [ROMCREATOR.create,False,["rom320b.bin"],{"romSize":8}],
         [fileDiff.testBinFile,False,["rom320b.rom","rom85/rom320b.rom"]],
         [silentRemove,False, ["rom320b.bin","rom320b.lst"]]
         ],
   "plotrom75": \
         ["Assemble HP-75 plotter rom", 
         [ ASSEMBLER.assemble,False,["rom75/plotrom.asm"],{ "symNamLen":7, \
             "globalSymbolFile": "75", \
             "listFileName": "plotrom.lst",  "referenceOpt":2}],
         [ROMCREATOR.create,False,["plotrom.bin"],{"romSize":8}],
         [fileDiff.testBinFile,False,["plotrom.rom","rom75/plotrom.bin"]],
         [silentRemove,False, ["plotrom.bin","plotrom.lst"]]
         ],
   "missing": \
         ["Assemble missing statements", 
         [ ASSEMBLER.assemble,False,["test/missing.asm"],{ \
             "globalSymbolFile": "85", "extendedChecks":True, \
             "listFileName": "missing.lst"}],
         [fileDiff.testBinFile,False,["missing.bin","test/missing.bin"]],
         [fileDiff.testAscFile,False,["missing.lst","test/missing.lst"]],
         [silentRemove,False, ["missing.bin","missing.lst"]]
         ],
   "ftoc":\
         ["Assemble HP-85 lex file ftoc.asm", 
         [ ASSEMBLER.assemble,False,["lex85/ftoc.asm"]],
         [LIFCREATOR.create,False,["ftoc.bin"],{"machine":"85",\
            "lifFileName":"FTOCB","lexOnly":True}],
         [LIFCREATOR.create,False,["ftoc.bin"],{"machine":"85",\
            "lifFileName":"FTOCB","lexOnly":False}],
         [fileDiff.testBinFile,False,["ftoc.bin","test/ftoc.bin"]],
         [fileDiff.testBinFile,False,["ftoc.dat","test/ftoc.dat"]],
         [fileDiff.testBinFile,False,["ftoc.lex","test/ftoc.lex"]],
         [silentRemove,False, ["ftoc.bin","ftoc.lex","ftoc.dat"]]
         ],
   "gcurs": \
         ["Assemble HP-85 lex file gcurs.asm", 
         [ ASSEMBLER.assemble,False,["lex85/gcurs.asm"],{ "symNamLen":6, \
            "listFileName": "gcurs.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["gcurs.bin","lex85/gcurs.bin"]],
         [silentRemove,False, ["gcurs.bin","gcurs.lst"]]
         ],
   "rp": \
         ["Assemble HP-85 lex file rp.asm", 
         [ ASSEMBLER.assemble,False,["lex85/rp.asm"],{ "symNamLen":6, \
            "listFileName": "rp.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["rp.bin","lex85/rp.bin"]],
         [silentRemove,False, ["rp.bin","rp.lst"]]
         ],
   "softky": \
         ["Assemble HP-85 lex file softky.asm", 
         [ ASSEMBLER.assemble,False,["lex85/softky.asm"],{ "symNamLen":6, \
            "listFileName": "softky.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["softky.bin","lex85/softky.bin"]],
         [silentRemove,False, ["softky.bin","softky.lst"]]
         ],
   "udlbin": \
         ["Assemble HP-85 lex file udlbin.asm", 
         [ ASSEMBLER.assemble,False,["lex85/udlbin.asm"],{ "symNamLen":6, \
            "listFileName": "udlbin.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["udlbin.bin","lex85/udlbin.bin"]],
         [silentRemove,False, ["udlbin.bin","udlbin.lst"]]
         ],
   "alpha": \
         ["Assemble HP-87 lex file alpha.asm", 
         [ ASSEMBLER.assemble,False,["lex87/alpha.asm"],{ "symNamLen":8, \
            "listFileName": "alpha.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["alpha.bin","lex87/alpha.bin"]],
         [silentRemove,False, ["alpha.bin","alpha.lst"]]
         ],
   "hglbin": \
         ["Assemble HP-87 lex file hglbin.asm", 
         [ ASSEMBLER.assemble,False,["lex87/hglbin.asm"],{ "symNamLen":8, \
           "listFileName": "hglbin.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["hglbin.bin","lex87/hglbin.bin"]],
         [silentRemove,False, ["hglbin.bin","hglbin.lst"]]
         ],
   "keys": \
         ["Assemble HP-87 lex file keys.asm", 
         [ ASSEMBLER.assemble,False,["lex87/keys.asm"],{ "symNamLen":8, \
           "listFileName": "keys.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["keys.bin","lex87/keys.bin"]],
         [silentRemove,False, ["keys.bin","keys.lst"]]
         ],
   "linput": \
         ["Assemble HP-87 lex file linput.asm", 
         [ ASSEMBLER.assemble,False,["lex87/linput.asm"],{ "symNamLen":8, \
           "listFileName": "linput.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["linput.bin","lex87/linput.bin"]],
         [silentRemove,False, ["linput.bin","linput.lst"]]
         ],
   "savg": \
         ["Assemble HP-87 lex file savg.asm", 
         [ ASSEMBLER.assemble,False,["lex87/savg.asm"],{ "symNamLen":8, \
           "listFileName": "savg.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["savg.bin","lex87/savg.bin"]],
         [silentRemove,False, ["savg.bin","savg.lst"]]
         ],
   "bad": \
         ["Assemble faulty statements", 
         [ ASSEMBLER.assemble,True,["test/bad.asm"],{ \
             "globalSymbolFile": "85", \
             "listFileName": "bad.lst", "extendedChecks":True}],
         [fileDiff.testAscFile,False,["bad.lst","test/bad.lst"]],
         [silentRemove,False, ["bad.lst"]]
         ],
   "bad2": \
         ["Assemble faulty statements part 2", 
         [ ASSEMBLER.assemble,True,["test/bad2.asm"],{ \
             "listFileName": "bad2.lst", "extendedChecks":True}],
         [fileDiff.testAscFile,False,["bad2.lst","test/bad2.lst"]],
         [silentRemove,False, ["bad2.lst"]]
         ],
   "bad3": \
         ["Assemble faulty statements part 3", 
         [ ASSEMBLER.assemble,True,["test/bad3.asm"],{ \
             "listFileName": "bad3.lst", "extendedChecks":True}],
         [fileDiff.testAscFile,False,["bad3.lst","test/bad3.lst"]],
         [silentRemove,False, ["bad3.lst"]]
         ],
   "bad4": \
         ["Assemble faulty statements part 4", 
         [ ASSEMBLER.assemble,True,["test/bad4.asm"],{ \
             "listFileName": "bad4.lst", "extendedChecks":True}],
         [fileDiff.testAscFile,False,["bad4.lst","test/bad4.lst"]],
         [silentRemove,False, ["bad4.lst"]]
         ],
   "jrel": \
         ["Assemble faulty jrel statements", 
         [ ASSEMBLER.assemble,True,["test/jrel.asm"],{ \
             "listFileName": "jrel.lst", "extendedChecks":True}],
         [fileDiff.testAscFile,False,["jrel.lst","test/jrel.lst"]],
         [silentRemove,False, ["jrel.lst"]]
         ],
   "phyconst":\
         ["HP-75 lex file pyhconst.asm", 
         [ ASSEMBLER.assemble,False,["lex75/phyconst.asm"],{"symNamLen":7, \
               "globalSymbolFile":"75"}],
         [LIFCREATOR.create,False,["phyconst.bin"],{ "machine":"75",\
                "lexOnly":True}],
         [LIFCREATOR.create,False,["phyconst.bin"],{ "machine":"75",\
                "lexOnly":False}],
         [fileDiff.testBinFile,False,["phyconst.bin","test/phyconst.bin"]],
         [fileDiff.testBinFile,False,["phyconst.lex","test/phyconst.lex"]],
         [fileDiff.testBinFile,False,["phyconst.dat","test/phyconst.dat"]],
         [silentRemove,False, ["phyconst.bin","phyconst.lex","phyconst.dat"]]
         ],
   "nonexistent":\
         ["Assemble non existing file",
         [ASSEMBLER.assemble,False,["nonexistend"],{},\
           "Error opening source file"],
         ],
   "writeonly1":\
         ["Assemble write only file",
         [ASSEMBLER.assemble,False,["writeonly"],{},\
           "Error opening source file"],
         ],
   "writeonly2":\
         ["Assemble to read only binary file",
         [ASSEMBLER.assemble,False,["rom85/rom000.asm"],{"binFileName":\
           "readonly"},"Error opening object file"],
         ],
   "writeonly3":\
         ["Assemble and write list to read only file",
         [ASSEMBLER.assemble,False,["rom85/rom000.asm"],{"listFileName":\
           "readonly"},"Error opening list file"],
         [silentRemove,False, ["rom000.bin"]]
         ],
   "glonopyextension":\
         ["Assemble with global symbol file that has no .py suffix",
         [ASSEMBLER.assemble,False,["test/missing.asm"],\
          {"globalSymbolFile":"nonexistent"},\
           "global symbol file does not have a .py suffix"],
         ],
   "glononexistent":\
         ["Assemble wth non existing global symbol file",
         [ASSEMBLER.assemble,False,["test/missing.asm"],\
          {"globalSymbolFile":"nonexistent.py"},\
           "cannot open or read global symbol file"],
         ],
   "gloinvalid":\
         ["Assemble wth invalid global symbol file",
         [ASSEMBLER.assemble,False,["test/missing.asm"],\
          {"globalSymbolFile":"test/illglo.py"},\
           "Invalid global symbol file"],
         ],
   "symbols":\
         ["Generate global symbol class file",
         [GENERATOR.generate,False,["symbols/globals85.txt","globals85.py"]],
         [fileDiff.testAscFile,False,["globals85.py","capasm/globals85.py"]],
         [silentRemove,False,["globals85.py"]],
         ],
   "illsym":\
         ["Faulty global symbol file",
         [GENERATOR.generate,True,["test/illsym.txt","illsym.py"]],
         [silentRemove,False,["illsym.py"]],
         ],
   "symnoex":\
         ["Non existing global symbol file",
         [GENERATOR.generate,False,["nonexisting.glo","illsym.py"], {}, \
         "cannot open input file"],
         ],
   "empty":\
         ["Assemble empty file",
         [ASSEMBLER.assemble,False,["empty"],{},\
           "Empty source file"],
         ],
   "cvglo":\
         ["Convert global data file",
         [SYMCONVERTER.convert,False,["test/GLOBAL8.DTA8x","temp.glo"]],
         [fileDiff.testAscFile,False,["temp.glo","test/GLOBAL8.glo"]],
         [silentRemove,False,["temp.glo"]],
         ],
   "cvglonoex":\
         ["Convert non existing global data file",
         [SYMCONVERTER.convert,False,["nonexisting","temp.glo"],{},\
          "cannot open/read input file"],
         ],
   "cvasmnoex":\
         ["Convert non existing tokenized assembler source file",
         [ASMCONVERTER.convert,False,["nonexisting","temp.glo"],{},\
          "cannot open/read input file"],
         ],
   "cvasm85":\
         ["Convert tokenized HP-85 asm file",
         [ASMCONVERTER.convert,False,["test/REDZER2.ASCII","temp.asm"]],
         [fileDiff.testAscFile,False,["temp.asm","test/redzers85.asm"]],
         [silentRemove,False,["temp.asm"]],
         ],
   "cvasm87":\
         ["Convert tokenized HP-87 asm file",
         [ASMCONVERTER.convert,False,["test/REDZERS.e014","temp.asm"]],
         [fileDiff.testAscFile,False,["temp.asm","test/redzers87.asm"]],
         [silentRemove,False,["temp.asm"]],
         ],
   "forthrom87":\
         ["Assembling forth for HP-87",
         [ASSEMBLER.assemble,False,["forth/GEFRT1"],{"listFileName":\
           "GEFRT1.lis", "referenceOpt":"2","useHex":True},],
         [ROMCREATOR.create,False,["GEFRT1.bin"],{"romSize":8}],
         [fileDiff.testBinFile,False,["GEFRT1.rom","forth/FORTHROM87"]],
         [silentRemove,False,["GEFRT1.bin","GEFRT1.rom","GEFRT1.lis"]],
         ],
#
# ncas tests
#
   "ncas SYSROM":\
        ["Assembling SYSROM for HP-75 with ncas",
         [ NCAS.assemble,False,["rom75/SYSROM.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "SYSROM.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["SYSROM.bin","rom75/SYSROM.bin"]],
         [silentRemove,False,["SYSROM.bin","SYSROM.lst"]],
        ],
#
   "ncas BASROM":\
        ["Assembling BASROM for HP-75 with ncas",
         [ NCAS.assemble,False,["rom75/BASROM.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "BASROM.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["BASROM.bin","rom75/BASROM.bin"]],
         [silentRemove,False,["BASROM.bin","BASROM.lst"]],
        ],

#
   "ncas MELROM":\
        ["Assembling MELROM for HP-75 with ncas",
         [ NCAS.assemble,False,["rom75/MELROM.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "MELROM.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["MELROM.bin","rom75/MELROM.bin"]],
         [silentRemove,False,["MELROM.bin","MELROM.lst"]],
        ],

#
   "ncas ALTROM":\
        ["Assembling ALTROM for HP-75 with ncas",
         [ NCAS.assemble,False,["rom75/ALTROM.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "ALTROM.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["ALTROM.bin","rom75/ALTROM.bin"]],
         [silentRemove,False,["ALTROM.bin","ALTROM.lst"]],
        ],

   "ncas riowio":\
        ["Assembling riowio for HP-75 with ncas",
         [ NCAS.assemble,False,["ncas/riowio.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "riowio.lst",  "referenceOpt":2}],
         [fileDiff.testBinFile,False,["riowio.bin","test/riowio.bin"]],
         [silentRemove,False,["riowio.bin","riowio.lis"]],
        ],

   "ncas conditions":\
        ["Assembling conditional assembly tests with ncas",
         [ NCAS.assemble,False,["test/cond.asm"],{ "globalSymbolFile": "75", \
             "listFileName": "cond.lst","referenceOpt":2, \
             "definedFlags":["TEST2"]}],
         [fileDiff.testBinFile,False,["cond.bin","test/cond.bin"]],
         [silentRemove,False,["cond.bin","cond.lis"]],
        ],

   "ncas expressions":\
        ["Assembling expressions with ncas",
         [ NCAS.assemble,True,["test/expression.asm"],{ \
             "globalSymbolFile": "75", "extendedChecks":True, \
             "listFileName": "expression.lst"}],
         [fileDiff.testAscFile,False,["expression.lst","test/expression.lst"]],
         [silentRemove,False,["expression.lst"]],
        ],
}
#
# execute a regression test command 
#
# Test conditions are:
# - the command returns the expected return value
# or
# - the command raises the expected capasmEror condition
#
# All other error conditions are not handeled! 
#
# Returns:
#   False: command passed
#   True:  command failed
#
def doTestCommand(command):

   ret=False
#
#  Method or function pointer
#
   method=command[0]
#
#  expected return value
#
   expectedRetval=command[1]
#
#  List of positional parameters
#
   if len(command)>2:
      posParams=command[2]
   else:
      posParams=[]
#
#  List of keyword parameters
#
   if len(command)>3:
      varParams=command[3]
   else:
      varParams={}
#
#  exception message we check against
#
   if len(command)>4:
      exceptionMessage=command[4]
   else:
      exceptionMessage=""
   try:
      r=method(*posParams, **varParams)
      ret|= not (r==expectedRetval)
   except capasmError as e:
      if e.msg!=exceptionMessage:
         print("Unexpected capasm exception message: ")
         if not exceptionMessage:
            print(e.msg)
         else:
            print(e.msg+"!="+exceptionMessage)
         ret|=True
#  except Exception as e:
#     print("Unexpected exception ")
   return ret
#
# run a complete test spec
#
def doTest(testSpec):
   ret=False
#
#  get test spec and run all commands
#
   print(testSpec[0])
   for command in testSpec[1:]:
       ret|= doTestCommand(command)
   return ret

#
# regression test main program
#
def main():
   os.environ["CAPASMREGRESSIONTEST"]="1"
   testCount=0
   failedCount=0
   testResults=[]
   Path("writeonly").touch(mode=0o222,exist_ok=True)
   Path("readonly").touch(mode=0o444,exist_ok=True)
   Path("empty").touch(mode=0o666,exist_ok=True)

   for t in CAPASM_TESTS:
      testSpec=CAPASM_TESTS[t]
      testDescription=testSpec[0]
      ret=doTest(testSpec)
      testCount+=1
      if ret:
         failedCount+=1
      testResults.append([testDescription,ret])
   print("")
   print("Results of regression tests:")
   for result in testResults:
      s="Passed"
      if result[1]:
         s="Failed!"
      print("{:50s} {:s}".format(result[0],s))
   print("{:d} of {:d} tests failed".format(failedCount,testCount))
   Path("writeonly").chmod(0o666)
   Path("readonly").chmod(0o666)
   silentRemove("writeonly","readonly","empty")

if __name__ == "__main__":
   main()
