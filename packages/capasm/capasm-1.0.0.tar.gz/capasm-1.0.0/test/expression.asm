       ORG  4711D
ROMEND EQU  5FFFH
HENRY  EQU  1000D
TYNBAS EQU  'B'
TEST1  EQU  (HENRY)+2 ; expected 03EAH
TEST2  EQU  (((HENRY)+(HENRY)+7)*3+$+"ABC"|77) ; expected 436C6BH
TEST3  EQU  2D+2+1001B+4AH+77O+22C ; expected  0B8H
TEST4  EQU  TYNBAS  ; expected 42H
TEST5  EQU  (TEST4)*100H+11111110B ; expected 42FEH
TEST6  EQU  (-1).4D ; expected -1
TEST7  EQU  (0aF#).8D ; expected 0AFH
S27-57  EQU  (-(57-27+1)*256D+27).2 ; expected 0E717H
TEST8 EQU  123456D
TEST9  EQU  -1
TEST10 EQU (TEST1)*'B'/0EFH ; expected result 114H
TEST11 EQU 33H
ADDR1  ADDR HENRY    ; this is implicitely sized to two bytes
ADDR2  ADDR (HENRY)+96D
       DATA 'ABC'
       DATA 4276803D
       DATA (TEST1).2
       DATA (TEST2).6
       DATA (TEST3).4
       DATA (TEST4).1
       DATA (TEST5).2
       DATA (TEST6).1
       DATA (TEST6).2
       DATA (TEST6).3
       DATA (TEST6).4
       DATA (TEST7).1
       DATA (S27-57).2
       DATA (S27-57).4
       DATA (TEST8).8D
       DATA HENRY,TEST6
       DATA TEST11
T1     EQU  (TEST1).2
T2     EQU  (TEST2).6
T3     EQU  (END)-5
T4     EQU  ((HENRY).6+(TEST6).8D).10D
START  LDM  R40,=T1,T2
       LDM  R40,=END,T2
       LDM  R40,=START,T2
       LDM  R40,=(END).2,T2
blank  EQU  ' '
       LDM  R2,=blank,0
       LDMD R40,=34q
       STMD R20,=START
       ADM  R40,=1,(2+4).1,(8D).5,'X'
       DATA (-64000D).2
*
RTC    EQU  22
OFFSET EQU  7
BUFFER BSS  10
       ldmd R45,=RTC      ; required size is 2 bytes
                          ; RTC is generated as a two byte value,
                          ; regardless of its size
constant equ 128D
minusone equ -1

       DATA 1,2,3,4,50, 'Jack IV',"Roo"
       DATA ((BUFFER)+27*2).2,(constant).7
       DATA ((THERE)-($)).1,minusone
       DATA 1,2,3,-27
       DATA ((THERE)-($)-1).1, 'This is a message'
THERE
       DATA "This is a string ending with null",0
       DATA 'This one ',"ends with CR",CR
       DATA 'FNAME',8D
       DATA `This ends with the high bit set` ;note accents
       DATA ^so does this^

workfilename equ 'workfile'
devicefi1ename equ 'devfile '
trans equ 'a'-'A'
lcdsiz equ (LCDMIN)-(LCDMAX)
filler equ 0102030405060708#

DEST   ldm  R45,=110B
       cmbd R73,=BUFFER
       LDB  R62,=TYNLEX
LBL    ADM  R#,=1,2,3
       LDMD R3,X20,OFFSET
       LDMD  R#,=BUFFER
       LDM  R4,=((DEST)-1).2
END    BSS  0
       BSS (ROMEND)-($)+1
       END
