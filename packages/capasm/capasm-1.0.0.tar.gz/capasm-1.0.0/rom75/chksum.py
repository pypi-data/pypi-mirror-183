#!/usr/bin/python3
# -*- coding: utf-8 -*
# 
# This Python3 utility calculates the checksum of HP-75 ROM files
#
# Usage:
#
# python3 checksum.py <rom file name> <addr1> <addr2>
#
# where <rom file name>  name of the rom binary file
#       <addr1>          start address as hex number
#       <addr2>          end address as hex number
#
# <addr1> and <addr2> are relative to the beginning of the file.
#
# Calculate the checksums of SYSROM:
#
# python3 checksum.py SYSROM.bin 0 1FFF
# python3 checksum.py SYSROM.bin 2000 3FFF
# python3 checksum.py SYSROM.bin 4000 5FFF
#
# Calculate the checksum of MELROM:
#
# python3 checksum.py MELROM.bin 0 1FFF
#
# The ROM checksum is valid if the program outputs 0. If not, adjust the value
# of the checksum byte accordingly.
#
# 
import sys,os

def main():
   romname= sys.argv[1]
   addrStart= int(sys.argv[2],16)
   addrEnd= int(sys.argv[3],16)
   f=open(romname,"rb")
   romBin=f.read()
   f.close()
   chkSum=1
   addr=addrStart
   while addr <= addrEnd:
      chkSum=chkSum+romBin[addr]
      if chkSum>255:
         chkSum+=1
         chkSum= chkSum &0XFF
      addr=addr+1
   chkSum-=1
   print(chkSum)
if __name__ == "__main__":
   main()

