0020 !        GLO GLOB2
0030 !  MY&IP1 - 1ST PART IPBI
0040 !       UN
0050 ! *****************************************************
0060 !  IPBIN AND KEYBOARD IS binaries are merged togethe
0070 !  command to the IPBIN program: KEYBOARD IS ..
0080 !  10/15/80: IMAGE REMOVED FROM KEYBOARD IS ENTER CAL
0090 ! 
0100 ! 
0110 ! 
0120 ! 
0130 ! 
0140 !       DATE !      :          09/06/7
0150 ! 
0160 ! *****************************************************
0170 !       STRUCTURE OF THE BINARY 
0180 !       1. HEADE
0190 !       3. PARSIN
0200 !       5. KEYBOARD !  EXECUTIO
0210 !       7. LOG EOL SVC EXECUTIO
0220 !       9. ON CCODE !  EXECUTIO
0230 !      11. CPRINT !    EXECUTIO
0240 !      13. STRING AND BUFFER UTILITIE
0250 !      15. R/W MEMORY LOCATION
0260 ! 
0270 ! 
0280 ! 
0290 !       2.  SPEND !4 HRS TESTING IN MA
0300 ! 
0310 ! 
0320 ! 
0330 !       A BINARY PROGRAM BECAUSE 'BSS' IS NO
0340 ! 
0350 !       OPERATION CALCULATIONS BY THE PROCESSOR - I
0360 !       OCCUR ( WHICH DO HAPPEN IN A BINARY PROGRAM 
0370 !       STATEMENTS COME WITH BCD MODE SET - FUNCTION
0380 ! 
0390 !       NO SPACE LEFT. !YOU MUST DO THIS WITH A 'JEN
0400 ! 
0410 !        HED HEADE
0420 !            !                 FOR USE WITH HP-85 SYSTEM 2
0430        ASC  6,IPBIN 
0440        BYT  142
0450        DEF  LENGTH           !            END OF BINARY ADDRESS
0460        BSZ  17               !  FILLER
0470 ! 
0480 ! 
0490 BASE   BSZ  2
0500        DEF  RUNTIM           !            RUNTIME EXECUTION LINK
0510        DEF  ASCII 
0520        DEF  PARSE            !             PARSE EXECUTIION  LINK
0530        DEF  DUMMY 
0540        DEF  INIT             !              INITIALIZATION    LINK
0550 RUNTIM BSZ  2                !                 DUMMY ENTRY
0560        DEF  CPRNT.
0570        DEF  CLINE.           !            2   CLINE
0580        DEF  CCURS.
0590        DEF  CCLR.            !             4   CCLEAR
0600        DEF  CWRT. 
0610        DEF  CDISP.           !            6   CDISP
0620        DEF  ONKBD.
0630        DEF  OFFK.            !             8   OFF KBD
0640        DEF  ONCOD.
0650        DEF  OFFC.            !             10  OFF CCODE
0660        DEF  CLPOS.
0670        DEF  CCPOS.           !            12  CCPOS   ( NUM. FUNCTION )
0680        DEF  CCHR$.
0690        DEF  KBD$.            !             14  KBD$    ( STR. FUNCTION )
0700        DEF  FIND. 
0710        DEF  KCNVP.           !            16  CONVERT KBD PAIRS
0720        DEF  KCNVI.
0730        DEF  KCNV.            !             18  CONVERT KBD
0740        DEF  SGCLR.
0750        DEF  KBDIS.           !            20 KEYBOARD IS
0755        DEF  SCRATB
0760 PARSE  BSZ  2                !                 DUMMY ENTRY
0770        DEF  STM_S            ! CPRINT
0780        DEF  STM_N            !             2   CLINE
0790        DEF  STM_N 
0800        DEF  STM              !               4   CCLEAR
0810        DEF  STM_S            !             6   CDISP
0820        DEF  STM_S 
0830        DEF  ONKBD            !  7
0840        DEF  STM              !               8   OFF KBD
0850        DEF  ONKBD 
0860        DEF  STM              !               10  OFF CCODE
0870        DEF  DUMMY            !             12  ----------
0880        DEF  DUMMY 
0890        DEF  DUMMY 
0900        DEF  DUMMY 
0910        DEF  DUMMY            !             14  ----------
0920        DEF  STM_S            !             16  CONVERT KBD PAIRS
0930        DEF  STM_S 
0940        DEF  STM              !               18  CONVERT KBD
0950        DEF  SGCLR 
0960        DEF  KBDIS 
0965        DEF  STM   
0970 ! 
0980 ! 
0990 SVC_R  DEF  EOLSVC
1000 KBD_R  DEF  KBDISR           !            ON KBD  KEYBOARD ISR
1010 !       RELOCATING TABLES OF LABEL
1020 JMPTBL DEF  CD_LP            !             ASCII  0 - NULL
1030        DEF  CD_CC            !             ASCII  2 -
1040        DEF  CD_CC 
1050        DEF  CD_CC 
1060        DEF  CD_CC 
1070        DEF  CD_CC            !             ASCII  4 -
1080        DEF  CD_CC            !             ASCII  6 -
1090        DEF  CD_BL 
1100        DEF  CD_BS            !             ASCII  8 - BACKSPACE
1110        DEF  CD_CC 
1120        DEF  CD_LF            !             ASCII 10 - LINE FEED
1130        DEF  CD_CC 
1140        DEF  CD_FF            !             ASCII 12 - FORM FEED
1150        DEF  CD_CR 
1160 ! 
1170 PRTTBL DEF  CP_LP            !             ASCII  0 - NULL
1180        DEF  CP_CC            !             ASCII  2 -
1190        DEF  CP_CC 
1200        DEF  CP_CC 
1210        DEF  CP_CC 
1220        DEF  CP_CC            !             ASCII  4 -
1230        DEF  CP_CC            !             ASCII  6 -
1240        DEF  CP_BL 
1250        DEF  CP_BS            !             ASCII  8 - BACKSPACE
1260        DEF  CP_CC 
1270        DEF  CP_LF            !             ASCII 10 - LINE FEED
1280        DEF  CP_CC 
1290        DEF  CP_FF            !             ASCII 12 - FORM FEED
1300        DEF  CP_CR 
1310 ! 
1320 ! 
1330        BYT  377,377
1340 !       ABSOLUTE ENTRY POIN
1350 INCHR  DAD  35244            !      3470   READ CHARACTER FROM CRT
1360 CHKSTS DAD  36335
1370 PADKBD DAD  34662            !      3106   RETURN ENTRY POINT FOR ONKBD ISR
1380 ALPHA. DAD  36105
1390 RETRHI DAD  35771            !      4215   DEMAND A RETRACE
1400 ! 
1410 TRA?   DAD  1523
1420 CLKHIT DAD  507              !         507   FOR EOLSVC TO GET A SHOT AT CLOCK INTERRUPTS
1430 CHREDT DAD  364
1440 XCBIT3 DAD  274              !         274   FOR EOLSVC TO GET A SHOT AT INPUT TERMINATION
1450 ! 
1460 !            !        +75357   ( START OF MODULE KH4 
1470 PRDVR1 DAD  75767
1480 IPHERE DAD  101042           !            LOCATION TO TELL THE WORLD I AM HERE
1490 !        HED KEYWORD TABLE
1500 ASCII  ASC  5,CPRINT
1510        VAL  T     
1520        ASC  4,CLINE
1530        VAL  E     
1540        ASC  6,CCURSOR
1550        VAL  R     
1560        ASC  5,CCLEAR
1570        VAL  R     
1580        ASC  5,CWRITE
1590        VAL  E     
1600        ASC  4,CDISP
1610        VAL  P     
1620        ASC  5,ON KBD
1630        VAL  D     
1640        ASC  6,OFF KBD
1650        VAL  D     
1660        ASC  7,ON CCODE
1670        VAL  E     
1680        ASC  8D,OFF CCODE
1690        VAL  E     
1700        ASC  4,CLPOS
1710        VAL  S     
1720        ASC  4,CCPOS
1730        VAL  S     
1740        ASC  4,CCHR$
1750        VAL  $     
1760        ASC  3,KBD$
1770        VAL  $     
1780        ASC  3,FIND
1790        VAL  D     
1800        ASC  "CONVERT KBD PAIRS "
1810 !       16  CONVERT KBD PAIR
1820        BYT  59D
1830        BYT  240              !                    ( BLANK     )
1840        ASC  "CONVERT KBD INDEX "
1850 !       17  CONVERT KBD INDE
1860        BYT  59D
1870        BYT  240              !                    ( BLANK     )
1880        ASC  10D,CONVERT KBD
1890        VAL  D     
1900        ASC  06D,SGCLEAR
1910        VAL  R     
1920        ASC  "KEYBOARD I"
1930        VAL  S     
1934        ASP  "SCRATCHBIN"
1940        BYT  377
1950 !        HED PARSIN
1960 !       PARSE CODE FOR SGCLEAR ( 4 NUMERIC PARAMETERS 
1970 SGCLR  LDB  R35,=4           !        DEMAND 4 PARAMETERS
1980        JMP  STM_X 
1990 ! 
2000 ! 
2010 STM    LDM  R56,=371,0
2020        PUMD R56,+R12         !         /    AND  DUMMY  TOKEN (   0 )
2030        PUBD R43,+R12
2040        JSB  =SCAN  
2050        RTN  
2060 ! 
2070 ! 
2080 STM_N  LDB  R35,=1
2090 STM_X  PUBD R43,+R6          !          SAVE STATEMENT TOKEN AWAY
2100        LDB  R14,=371
2110        JSB  =GETPAR          !           /    PUSH BINARY TOKEN ( 371 )
2120        POBD R53,-R6
2130        PUBD R53,+R12         !         PUSH DUMMY TOKEN  ( NON-ZERO )
2140        PUBD R53,+R12
2150        RTN  
2160 !       PARSE CODE FOR A STATEMENT WITH 1 STRING PARAMETE
2170 STM_S  PUBD R43,+R6          !          SAVE STATEMENT TOKEN AWAY
2180        JSB  =SCAN  
2190        JSB  =STRREF          !           HUNT FOR STRING VARIABLE
2200        POBD R2,-R6
2210        DCE                   !                   \   MAKE SURE THIS WASN'T
2220        JEN  SYNERR
2230        LDM  R56,=371,0       !     \   PUSH BINARY TOKEN ( 371 )
2240        PUMD R56,+R12
2250        PUBD R2,+R12          !          PUSH TOKEN OF STATEMENT
2260        RTN  
2270 ! 
2280 !       ON CCODE ( GOTO / GOSUB ) PARSE COD
2290 ONKBD  LDM  R56,=371,0       !     \   PUSH BINARY TOKEN ( 371 )
2300        PUMD R56,+R12
2310        PUBD R43,+R12         !         PUSH TOKEN OF STATEMENT
2320        JSB  =SCAN  
2330        CMB  R47,=210         !       IS GOTO/GOSUB NEXT ?
2340        JZR  ONK_OK
2350 SYNERR JSB  =ERROR+          !              - NO  - GENERATE ERROR 92 : SYNTAX
2360        BYT  92D
2370        RTN  
2380 ONK_OK JSB  =GOTOSU
2390        RTN  
2400 ! 
2410 ! 
2420 !       ROMFL !   MEANING         IPBIN ACTIO
2430 !         0 !     POWER ON        NONE - CAN'T GET HERE ( BINPGM'S 
2440 !         2 !     SCRATCH         REMOV
2450 !         4 !     RUN / INIT      SET-UP AND CLEAR ON KBD ACTIV
2460 !         6 !     PAUSE           SET-U
2470 !         8 !     ALLOCATE        NOTHIN
2480 !        10 !     DECOMPILE       NOTHIN
2490 ! 
2500 ! 
2510 INIT   LDMD R22,=BINTAB
2520        LDBD R20,=ROMFL       !       GET REASON FOR INITIALIZATION
2530        CMB  R20,=2
2540        JZR  UNINIT           !            /
2550        CMB  R20,=5
2560        JZR  UNINIT           !            /
2570        CMB  R20,=4
2580        JZR  INIT_2           !            /
2590        CMB  R20,=1
2600        JZR  INIT_2           !            /
2610        CMB  R20,=7
2620        JZR  INIT_2           !            /
2630        CMB  R20,=8D
2640        JCY  INITDN           !            /         ( AND DO NOTHING )
2650        JMP  INIT_3
2660 INIT_2 JSB  X22,OFFK.        !         DO 'OFF KBD'
2670        JSB  X22,OFFC. 
2680        JSB  X22,KCNV.        !        NO CONVERT TO START
2690 INIT_3 LDMD R41,=IOSP  
2700        LDM  R54,R41          !       GET SHORT FORM FOR COMPARE
2710        LDMD R66,X22,SVC_R 
2720        STMD R66,X22,SVCADR   !   /   IN SERVICE LINK
2730        LDMD R64,X22,MY_SVC
2740        CMM  R64,R54          !      IS IOSP ALREADY MY SERVICE LINK ?
2750        JZR  INITDN
2760        LDMD R74,X22,SVCERR   !      - NO  - IS THE OLD SVC LINK A DUMMY ?
2770        CMM  R74,R54
2780        JNZ  SAVOLD           !                      - NO  - SAVE IT AWAY
2790        LDB  R41,=236
2800 SAVOLD STMD R41,X22,OLDSVC   !   SAVE OLD SERVICE LINK
2810        STMD R64,=IOSP  
2820 INITDN LDB  R20,=377         !      \
2830        STBD R20,=IPHERE
2840        RTN  
2850 !       UN-INITIALIZ
2860 UNINIT BSZ  0                !                 UN-INITIALIZE!
2870        JSB  X22,KILIDL
2880        LDB  R40,=236         !      GET A DUMMY RETURN
2890        STBD R40,=KYIDLE
2900        LDMD R41,X22,OLDSVC   !   GET OLD EOL SERVICE CODE
2910        CMB  R41,R40
2920        JNZ  WASSVC
2930        LDMD R41,X22,SVCERR
2940 WASSVC STMD R41,=IOSP        !            - YES - SAVE OLD SVC CALL
2950 UN_DN  CLB  R20
2960        STBD R20,=IPHERE      !      /  TELL THE  WORLD THAT I HAVE SHUFFLED OFF
2970        RTN  
2980        LNK  MY&IP2.asm
