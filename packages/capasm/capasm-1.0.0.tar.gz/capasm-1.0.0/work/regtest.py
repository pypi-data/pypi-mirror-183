#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This module contains the regression test driver for capasm
# (c) 2020 Joachim Siebold
#
#
import os
from pathlib import Path
from capasm.assembler import clsAssembler
from capasm.tools import clsLifFileCreator,binDiff

ROMTESTFILES=["rom000.asm","romsys1.asm","romsys2.asm","romsys3.asm", \
              "rom050.asm"]
LEX75TESTFILES=["fky75l.asm","hpilcmd.asm","phyconst.asm","riowio.asm"]
#
# Test binary file, the reference is in the "ref" directory below
#
def testBinFile(fileName):
   fp=Path(fileName)
   fn=fp.name
   rn=fp.parents[0] / "ref" / fn
   ret=binDiff.compare(fileName,str(rn))
   if ret is None:
      return True
   if ret[0]!=0:
      print(str(fileName)+": compare failed, "+str(ret[0])+" differences found")
#     print("First occurrence at {:o}".format(ret[3][0]))
   if ret[1]!=ret[2]:
      print(str(fileName)+": file length differs, "+str(ret[1])+" "+str(ret[2]))
   if ret[0]==0 and (ret[1]==ret[2]):
      return False
   else:
      return True

def main():
   os.environ["CAPASMREGRESSIONTEST"]="1"
   testDir=Path("test")
   a=clsAssembler()
   l=clsLifFileCreator()
   numTests=0
   numFailed=0
#
# Run ROM tests
#
   for romTestfile in ROMTESTFILES:
      srcFile=testDir / romTestfile
      lstFile=srcFile.with_suffix(".lst")
      binFile=srcFile.with_suffix(".bin")
      
      a.assemble(str(srcFile),labelSize=7,listFileName=str(lstFile), \
            referenceOpt=2)
      numTests+=1
      if testBinFile(binFile):
         numFailed+=1
      srcFile=None
      lstFile=None
      binFile=None
#
# Test statements not covered by rom tests
#
   srcFile=testDir / "missing.asm"
   lstFile=srcFile.with_suffix(".lst")
   binFile=srcFile.with_suffix(".bin")
   a.assemble(str(srcFile),labelSize=7,listFileName=str(lstFile),\
             referenceOpt=2,  extendedChecks=True)
   numTests+=1
   if testBinFile(binFile):
      numFailed+=1
#
#  Test error messages
#
   srcFile=testDir / "bad.asm"
   lstFile=srcFile.with_suffix(".lst")
   a.assemble(str(srcFile),labelSize=7,listFileName=str(lstFile),\
             referenceOpt=2,  extendedChecks=True)
#
#  Process HP-75 lex files
#
   lexDir=Path("lex75")
   for lexTestFile in LEX75TESTFILES:
      srcFile=lexDir / lexTestFile
      lstFile=srcFile.with_suffix(".lst")
      binFile=srcFile.with_suffix(".bin")
      lexFile=srcFile.with_suffix(".lex")
      a.assemble(str(srcFile),labelSize=7,machine="75")
      if binFile.is_file():
         l.create(str(binFile))

   
#
   print("{:d} of {:d} tests failed".format(numFailed,numTests))

if __name__ == "__main__":
   main()
