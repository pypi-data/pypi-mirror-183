#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
def main():
   tdict= {0: "EQU", 1: "DAD", 2:"DAD"}
   with open("GLOBAL","rb") as f:
      gloBytes=f.read()

   k=len(gloBytes)
   i=0
   count=0

   while i < k:
      h=gloBytes[i]
      i+=1
      l=gloBytes[i]
      if (l==0):
          break
      i+=1
      d=bytearray(0)
      for j in range (0,l):
         d.append(gloBytes[i])
         i+=1
         if i % 256 == 0:
            i+=3
      typ=gloBytes[i]
      symName=""
      ci=l-3
      while d[ci]!=0:
         symName+=chr(d[ci])
         ci-=1
      symValue=d[-2]*256+d[-1]
      d=None
      count+=1
      print("{:8s} {:3s} {:o}".format(symName,tdict[typ],symValue))
      i+=1
if __name__ == '__main__':  # pragma: no cover
   main()

