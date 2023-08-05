#!/bin/bash
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
#function capasm {
#   python3 start.py capasm $*
#}
function checkfile {
   ret=`diff $2 $3`
   if test $? -eq 0 ; then
      echo "Test $1 passed"
   else
      echo "Test $1 failed"
   fi
}
export CAPASMREGRESSIONTEST=1
# ROM000
capasm rom85/rom000.asm -s 7 -l rom000.lst -g 85 -r 2 > /dev/null
checkfile 1 "rom000.bin" "test/rom000.bin"
rm -f rom000.bin rom000.lst
# ROMSYS1
capasm rom85/romsys1.asm -s 7 -l romsys1.lst -g 85 -r 2 > /dev/null
checkfile 2 "romsys1.bin" "test/romsys1.bin"
rm -f romsys1.bin romsys1.lst
# ROMSYS2
capasm rom85/romsys2.asm -s 7 -l romsys2.lst -g 85 -r 2 > /dev/null
checkfile 3 "romsys2.bin" "test/romsys2.bin"
rm -f romsys2.bin romsys2.lst
# ROMSYS3
capasm rom85/romsys3.asm -s 7 -l romsys3.lst -g 85 -r 2 > /dev/null
checkfile 4 "romsys3.bin" "test/romsys3.bin"
rm -f romsys3.bin romsys3.lst
# ROM050
capasm rom85/rom050.asm -s 7 -l rom050.lst -g 85 -r 2 > /dev/null
caprom rom050.bin -s8 > /dev/null > /dev/null
checkfile 5 "rom050.rom" "test/rom050.rom"
rm -f rom050.bin rom050.lst rom050.rom
# ROM320B
capasm rom85/rom320b.asm -s 7 -l rom320b.lst -g 85 -r 2 > /dev/null
caprom rom320b.bin -s8 > /dev/null
checkfile 5b "rom320b.rom" "rom85/rom320b.rom"
rm -f rom320b.bin rom320b.lst rom320b.rom
# Plotrom
capasm rom75/plotrom.asm -s 7 -l plotrom.lst -r2  > /dev/null
caprom plotrom.bin -s8 > /dev/null
checkfile 5c "plotrom.rom" "rom75/plotrom.bin"
rm -f plotrom.bin plotrom.lst plotrom.rom
# missing
capasm test/missing.asm -g 85 -l missing.lst -c > /dev/null
checkfile 6 "missing.bin" "test/missing.bin"
checkfile 6b "missing.lst" "test/missing.lst"
#rm -f missing.bin missing.lst
# bad
capasm test/bad.asm -l bad.lst -g 85 -c  > /dev/null
checkfile 7 "bad.lst" "test/bad.lst"
rm -f bad.lst
# jrel
capasm test/jrel.asm -l jrel.lst -c  > /dev/null
checkfile 7a "jrel.lst" "test/jrel.lst"
rm -f  jrel.lst
#phyconst
capasm lex75/phyconst.asm -s 7 -g 75    > /dev/null
caplif phyconst.bin -m 75 > /dev/null
caplex phyconst.bin -m 75 > /dev/null
checkfile 8a "phyconst.bin" "test/phyconst.bin"
checkfile 8b "phyconst.lex" "test/phyconst.lex"
checkfile 8c "phyconst.dat" "test/phyconst.dat"
rm -f phyconst.bin phyconst.lif phyconst.lex phyconst.dat
#ftoc
capasm lex85/ftoc.asm -s 6   > /dev/null
caplif ftoc.bin -m 85 -f ftocb > /dev/null
caplex ftoc.bin -m 85 -f ftocb > /dev/null
checkfile 9a "ftoc.bin" "test/ftoc.bin"
checkfile 9b "ftoc.lex" "test/ftoc.lex"
checkfile 9c "ftoc.dat" "test/ftoc.dat"
rm -f ftoc.bin ftoc.lif ftoc.lex ftoc.dat
#gcurs
capasm lex85/gcurs.asm  > /dev/null
checkfile 10 "gcurs.bin" "lex85/gcurs.bin"
rm -f gcurs.bin
#rp
capasm lex85/rp.asm  > /dev/null
checkfile 11 "rp.bin" "lex85/rp.bin"
rm -f rp.bin
#softky
capasm lex85/softky.asm  > /dev/null
checkfile 12 "softky.bin" "lex85/softky.bin"
rm -f softky.bin
#udlbin
capasm lex85/udlbin.asm  > /dev/null
checkfile 13 "udlbin.bin" "lex85/udlbin.bin"
rm -f udlbin.bin
#alpha
capasm lex87/alpha.asm  -s8 > /dev/null
checkfile 14 "alpha.bin" "lex87/alpha.bin"
rm -f alpha.bin
#hglbin
capasm lex87/hglbin.asm  -s8 > /dev/null
checkfile 15 "hglbin.bin" "lex87/hglbin.bin"
rm -f hglbin.bin
#keys
capasm lex87/keys.asm  -s8 > /dev/null
checkfile 16 "keys.bin" "lex87/keys.bin"
rm -f keys.bin
#linput
capasm lex87/linput.asm  -s8 > /dev/null
checkfile 17 "linput.bin" "lex87/linput.bin"
rm -f linput.bin
#savg
capasm lex87/savg.asm  -s8 > /dev/null
checkfile 18 "savg.bin" "lex87/savg.bin"
rm -f savg.bin
#cvglo
capconv -t glo "test/GLOBAL8.DTA8x"  > /dev/null
checkfile 19a "GLOBAL8.glo" "test/GLOBAL8.glo"
rm -f GLOBAL8.glo
#cvasm85
capconv -t asm "test/REDZER2.ASCII"  > /dev/null
checkfile 19b "REDZER2.asm" "test/redzers85.asm"
rm -f REDZER2.asm
#cvasm87
capconv -t asm "test/REDZERS.e014"   > /dev/null
checkfile 19c "REDZERS.asm" "test/redzers87.asm"
rm -f REDZERS.asm
#symbols
capglo -s capasm "symbols/globals85.txt" > /dev/null
checkfile 20 "globals85.py" "capasm/globals85.py"
rm -f globals85.py
#forth
capasm forth/GEFRT1  -l GEFRT1.lst -r 2 -x > /dev/null
caprom -s8 GEFRT1.bin > /dev/null
checkfile 21 "GEFRT1.rom" "forth/FORTHROM87"
rm -rf GEFRT1.bin GEFRT1.rom GEFRT1.lst
# SYSROM ncas
ncas rom75/SYSROM.asm -l SYSROM.lis -g 75 -r 2 > /dev/null
checkfile 22 "SYSROM.bin" "rom75/SYSROM.bin"
rm -rf SYSROM.lis SYSROM.bin
# BASROM ncas
ncas rom75/BASROM.asm -l BASROM.lis -g 75 -r 2 > /dev/null
checkfile 23 "BASROM.bin" "rom75/BASROM.bin"
rm -rf BASROM.lis BASROM.bin
# MELROM ncas
ncas rom75/MELROM.asm -l MELROM.lis -g 75 -r 2 > /dev/null
checkfile 24 "MELROM.bin" "rom75/MELROM.bin"
rm -rf MELROM.lis MELROM.bin
# ALTROM ncas
ncas rom75/ALTROM.asm -l ALTROM.lis -g 75 -r 2 > /dev/null
checkfile 25 "ALTROM.bin" "rom75/ALTROM.bin"
rm -rf ALTROM.lis ALTROM.bin
# riowio ncas
ncas ncas/riowio.asm -l riowio.lis > /dev/null
checkfile 26 "riowio.bin" "test/riowio.bin"
rm -rf riowio.bin riowio.lis
# ncas conditions
ncas test/cond.asm -l cond.lis -d TEST2 > /dev/null
checkfile 27 "cond.bin" "test/cond.bin"
rm -rf cond.bin cond.lis
# ncas expressions
ncas test/expression.asm -l expression.lst -c > /dev/null
checkfile 28 "expression.lst" "test/expression.lst"
#rm -rf expression.bin expression.lst
exit
