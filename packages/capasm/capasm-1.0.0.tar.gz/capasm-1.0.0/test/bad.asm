! This assembler program is intended to check how the assembler manages
! bad code and to increase the coverage
        HED hhh
LABEL1
LABEL2  EQU   60000
LABEL3  EQU   200000
        EQU   HELLO
LABEL1
SAVR10  EQU   65432
        LOC ABC
        LOC 10000
1234567
100 LABALZ   ! comment
110     ! comment
        LDB R36, =3D
        LDB R36, =LABEL2
440     NAM ZZZAAAA
        BSZ
        BSZ =HELLO
        BSZ  100
        LDM R47, =LABEL2
        GTO   1LABEL
        JNZ   2LABEL
        GSB   NOLABEL
        LDM R20,=100,100D
        LDM R20,
        LDM R20,=
        LDM R22,=100C,19C
        LDM R24,=1XD,1XC
        LDM R26,=1X0
        LDM R28,=100,200
        LDM R24,+R26
        LDMD R24,=LABEL1,LABEL2
        STMI R30,X20,LABEL1
        STMI
        GTO UNKNOWN
        DEF UNK
        JSB =LABEL2,R12
        NAM HUGO,123
        STMI X20,R33,
        STMI R20,R39,HELLO
        PUBD R24,R22
        JSB  R12,=LABEL2
        JSB  R12,=LABEL2,R14
        DEF LABEL3
LABAL4  ! no comment
        ABS 10000
12LBL   LDM R25,=1
1 12LBL   LDM R25,=1
! no comment
                                    ! no comment
        LDM R40, =0,0,0,0,0,0,0,0,0,0,120
        LDM R46, =0 , 1, 2
        LDM R46, =0 , XXX, 2
        LDM R48, = "Z"
        LDM R44, ="ABCDE"
        LDM R44, ="{}CDE"
        LDM R44, =1LABEL
        VAL LABEL2
        ARP R99
        JSB =XYZ
        ICB K45
        ORB R-1,R22
        DRB R-1
        DRB R-1,R20
        ADB R-1,R20
        ADB R-1
        ADB X20
        ADB R10,R20,R30
        ADBD R10,
        ADBD R10,=LABEL2,25
        ADBD R10,R20,R30
LBL
        ADM  R#,=10,20,30,40
        LDM  R#,=10,20,30,40
        ADM  R20,=102B,1GGH
        LDM  R20,R30,R40
        LDM  R20,X20
        LDM R20,=LABEL2,20
        LDMD R20,X22
        LDMD R20,R22,R24
        LDBI R20,=LABEL2,20
        LDBI R20,X16,=LABEL2
        LDBI R20,X16,=LABEL2,22,44
        JSB R10,=LBL
        JSB X10,=LBL
        JSB X10,=LBL,R20
        LDM R40,=LABEL2,LABEL3,LABEL2

        JNZ XYZ
        JNZ SETFER
        DEF LOCATION1
        ORG 100
        DEF LOCATION2
        LDM R45, = 2496D
        ASC
        ASC     ""
        ASC     "HULLU
        ASC     "}"
        ASC  5X,HULLU
        ASC  5HULLU
        ASC ,HULLU
        ASC 7,HULLU
        ASC 3,HULLU
        INC  "Illegal
LOCATION1 BYT 0,400,"Z"
LOCATION2 BYT 1,2,3,4Z
        ELS
        ASC "ELSE WITHOUT AIF"
        EIF
        AIF 1TEST
        LDM R10,R20
        AIF COND1
        LDM R20,R30
        EIF
        LDM R20,R30
        ELS
        LDM R20,R30
        SET COND2
        AIF COND2
        LDM R20,R30
        ELS
        LDM R20,R40
        EIF
        CLR COND3
        AIF COND3
        LDM R20,R50
        ELS
        LDM R20,R60
        EIF
        AIF COND3
        FIN
