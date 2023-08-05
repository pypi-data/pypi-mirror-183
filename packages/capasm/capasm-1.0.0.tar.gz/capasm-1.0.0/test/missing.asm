!
! This test file checks the commands not covered by
! the ROM tests
!
        HED "Test non covered parts of the assembler (part1)"
        NAM MISS1
        LST
PROM#   EQU 360
OFFSET  EQU 10
        VAL PROM#
        DEF RUNTIM,

        UNL
RUNTIM,
        LDBD R30,=TABLE
        STMI R36,X30,OFFSET

        LDBD R32,=TABLE
        LDBI R36,R32
        ADM  R40,=100,100D,50H,101B,100d,100O,50#,101b
        LDM  R40,=
        BYT  101B
        DEF  SUB10
        VAL  PROM#
        DEF  RUNTIM,
        BYT  10#,12#
! redefine global Address SAVR0 as EQU with the same value
SAVR0   EQU  103220
! redefine EQU FWROM with an other value
FWROM   EQU  100
! redefine ADDRESS STACK with same type or value
STACK   DAD  101300
        ORG 1000
TABLE
LOC1    DAD 0
LOC2    DAD 10
LOC3    DAD 20
        FIN
