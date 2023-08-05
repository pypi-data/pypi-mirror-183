REM Regression test for WINDOWS
@echo off
set CAPASMREGRESSIONTEST="1"
set PATH=c:"\Program Files (x86)\Vim\vim81";%PATH%
REM  ROM000
capasm rom85\rom000.asm -s 7 -l rom000.lst -g 85 -r 2 > nul
call :checkfile  1 "rom000.bin" "test\rom000.bin"
del /q  rom000.bin rom000.lst
REM  ROMSYS1
capasm rom85\romsys1.asm -s 7 -l romsys1.lst -g 85 -r 2 > nul
call :checkfile  2 "romsys1.bin" "test\romsys1.bin"
del /q  romsys1.bin romsys1.lst
REM  ROMSYS2
capasm rom85\romsys2.asm -s 7 -l romsys2.lst -g 85 -r 2 > nul
call :checkfile  3 "romsys2.bin" "test\romsys2.bin"
del /q  romsys2.bin romsys2.lst
REM  ROMSYS3
capasm rom85\romsys3.asm -s 7 -l romsys3.lst -g 85 -r 2 > nul
call :checkfile  4 "romsys3.bin" "test\romsys3.bin"
del /q  romsys3.bin romsys3.lst
REM  ROM050
capasm rom85\rom050.asm -s 7 -l rom050.lst -g 85 -r 2 > nul
caprom rom050.bin -s8 > nul
call :checkfile  5 "rom050.rom" "test\rom050.bin"
del /q  rom050.bin rom050.lst rom050.rom
REM ROM320B
capasm rom85\rom320b.asm -s 7 -l rom320b.lst -g 85 -r 2 > nul
caprom rom320b.bin -s8 > nul
call :checkfile 5b "rom320b.rom" "rom85\rom320b.rom"
del /q rom320b.bin rom320b.lst rom320b.rom
REM Plotrom
capasm rom75\plotrom.asm -s 7 -l plotrom.lst -r2  > nul
caprom plotrom.bin -s8 > nul
call :checkfile 5c "plotrom.rom" "rom75\plotrom.bin"
del /q plotrom.bin plotrom.lst plotrom.bin
REM  missing
capasm test\missing.asm -g 85 > nul
call :checkfile  6 "missing.bin" "test\missing.bin"
del /q  missing.bin
REM  bad
capasm test\bad.asm -l bad.lst -c -g 85 > nul
call :checkfile  7 "bad.lst" "test\bad.lst"
REM del /q  bad.bin bad.lst
REM phyconst
capasm lex75\phyconst.asm -s 7   > nul
caplif phyconst.bin -m 75 > nul
caplex phyconst.bin -m 75 > nul
call :checkfile  8a "phyconst.bin" "test\phyconst.bin"
call :checkfile  8b "phyconst.lex" "test\phyconst.lex"
call :checkfile  8c "phyconst.dat" "test\phyconst.dat"
del /q  phyconst.bin phyconst.lif phyconst.lex
REM ftoc
capasm lex85\ftoc.asm -s 7  > nul
caplif ftoc.bin -m 85 -f ftocb > nul
caplex ftoc.bin -m 85 -f ftocb > nul
call :checkfile  9a "ftoc.bin" "test\ftoc.bin"
call :checkfile  9b "ftoc.lex" "test\ftoc.lex"
call :checkfile  9c "ftoc.dat" "test\ftoc.dat"
del /q  ftoc.bin ftoc.lif ftoc.lex
REM gcurs
capasm lex85/gcurs.asm > nul
call :checkfile 10 "gcurs.bin" "lex85\gcurs.bin"
del /q gcurs.bin
REM rp
capasm lex85/rp.asm > nul
call :checkfile 11 "rp.bin" "lex85\rp.bin"
del /q rp.bin
REM softky
capasm lex85/softky.asm > nul
call :checkfile 12 "softky.bin" "lex85\softky.bin"
del /q softky.bin
REM udlbin
capasm lex85/udlbin.asm > nul
call :checkfile 13 "udlbin.bin" "lex85\udlbin.bin"
del /q udlbin.bin
REM alpha
capasm lex87/alpha.asm  -s8 > nul
call :checkfile 14 "alpha.bin" "lex87\alpha.bin"
del /q alpha.bin
REM hglbin
capasm lex87/hglbin.asm  -s8 > nul
call :checkfile 15 "hglbin.bin" "lex87\hglbin.bin"
del /q hglbin.bin
REM keys
capasm lex87/keys.asm -s8 > nul
call :checkfile 16 "keys.bin" "lex87\keys.bin"
del /q keys.bin
REM linput
capasm lex87/linput.asm  -s8 > nul
call :checkfile 17 "linput.bin" "lex87\linput.bin"
del /q linput.bin
REM savg
capasm lex87/savg.asm  -s8 > nul
call :checkfile 18 "savg.bin" "lex87\savg.bin"
del /q savg.bin
REM cvglo
capconv -t glo "test\GLOBAL8.DTA8x"  > nul
call :checkfile 19a "GLOBAL8.glo" "test\GLOBAL8.glo"
del /q GLOBAL8.glo
REM cvasm85
capconv -t asm "test\REDZER2.ASCII"  > nul
call :checkfile 19b "REDZER2.asm" "test\redzers85.asm"
del /q REDZER2.asm
REM cvasm87
capconv -t asm "test\REDZERS.e014"   > nul
call :checkfile 19c "REDZERS.asm" "test\redzers87.asm"
del /q REDZERS.asm
REM symbols
capglo "symbols\globals85.txt" > nul
call :checkfile  20 "globals85.py" "capasm\globals85.py"
del /q  globals85.py
REM forth
capasm "forth\GEFRT1"  -l GEFRT1.lst -r 2 -x > nul
caprom -s8 GEFRT1.bin > nul
call :checkfile 21 "GEFRT1.rom" "forth\FORTHROM87"
del /q GEFRT1.bin GEFRT1.rom
REM  SYSROM ncas
ncas rom75\SYSROM.asm -l SYSROM.lis -g 75 -r 2 > nul
call :checkfile 22 "SYSROM.bin" "rom75\SYSROM.bin"
del /q SYSROM.lis SYSROM.bin
REM  BASROM ncas
ncas rom75\BASROM.asm -l BASROM.lis -g 75 -r 2 > nul
call :checkfile 23 "BASROM.bin" "rom75\BASROM.bin"
del /q BASROM.lis BASROM.bin
REM  MELROM ncas
ncas rom75\MELROM.asm -l MELROM.lis -g 75 -r 2 > nul
call :checkfile 24 "MELROM.bin" "rom75\MELROM.bin"
del /q MELROM.lis MELROM.bin
REM  ALTROM ncas
ncas rom75\ALTROM.asm -l ALTROM.lis -g 75 -r 2 > nul
call :checkfile 25 "ALTROM.bin" "rom75\ALTROM.bin"
del /q ALTROM.lis ALTROM.bin
REM  riowio ncas
ncas ncas\riowio.asm -l riowio.lis > nul
call :checkfile 26 "riowio.bin" "test\riowio.bin"
del /q riowio.bin riowio.lis
REM  ncas conditions
ncas test\cond.asm -l cond.lis -d TEST2 > nul
call :checkfile 27 "cond.bin" "test\cond.bin"
del /q cond.bin cond.lis
REM  ncas expressions
ncas test\expression.asm -l expression.lst -c > nul
call :checkfile 28 "expression.lst" "test\expression.lst"
REM del /q expression.bin expression.lst
exit /b


:checkfile 
diff %2 %3
if errorlevel 1 (
   echo Test %1 failed
) else (
   echo Test %1 passed
)
exit /b
