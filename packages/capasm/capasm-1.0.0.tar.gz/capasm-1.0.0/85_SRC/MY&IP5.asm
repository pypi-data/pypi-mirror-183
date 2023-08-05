0010 !  MY&IP5 - 5TH PART OF IPBI
0020 !        HED STRING AND BUFFER UTILITIE
0030 ! 
0040 !       FIND STRING INFORMATIO
0050 ! 
0060 FNDSTR JSB  =ALPHA.          !           GO INTO ALPHA MODE FOR CDISP,ETC.
0070 FNDSTP BIN                   !                 DON`T GO INTO ALPHA MODE FOR CPRINT
0080        POMD R62,-R12         !         GET STRING INFO OFF STACK
0090 !             !                R62-63     PACKED NAM
0100 !             !                R64-65     MAX LENGT
0110 !            !                 R66-67     ADDR OF FIRST BYT
0120        SBM  R66,=6,0         !         \   GET STRING ATTRIBUTES
0130        POMD R72,+R66         !         /
0140 !            !                 R72-73     TOTAL LENGT
0150 !            !                 R74-75     MAX   LENGT
0160 !            !                 R76-77     CUR.  LENGT
0170 !            !                 STRING LENGTH = R76-7
0180        TSM  R76              !              \  IF STRING IS UNINITIALIZED
0190        JPS  STR_OK           !                  THEN LENGTH=0
0200        CLM  R76              !              /
0210 STR_OK STM  R66,R14          !          SAVE STRING ADDRESS
0220        LDM  R36,R72          !          \
0230        CMM  R36,R74          !             IF MAX LEN <> TOT LEN
0240        JZR  NOTBUF           !            /     THEN
0250 !            !                       THE STRING IS A IOBUFFE
0260        DCM  R66              !              \
0270        DCM  R66              !                 CREATE ADDR OF FILL PTR
0280        STM  R66,R34          !          /
0290        ADM  R36,R66          !          \
0300        DCM  R36              !               \
0310        DCM  R36              !                 GET CONVERSION POINTER
0320        LDMD R36,R36          !           /
0330        STM  R36,R70          !          /
0340        LDM  R36,R74          !          \
0350        ADM  R36,R66          !           \
0360        ICM  R36              !               /  CREATE ADDR OF EMPTY PTR
0370        ICM  R36              !              /
0380        LDB  R75,=TRUE        !        BUF? = TRUE
0390        DCM  R14              !              PRE-DECREMENT R14 BECAUSE EMPTY PTR
0400 !            !                 IS OFF BY 
0410        JMP  FS_EX 
0420 NOTBUF CLB  R75              !              BUF? = FALSE
0430 FS_EX  LDMD R46,=CRTBYT      !      GET CURSOR POSITION
0440        LDMD R56,=CRTRAM      !      GET SCREEN START ADDRESS
0450        LDBD R74,X22,CCD?     !     GET ON CCODE INDICATOR
0460        RTN  
0470 ! 
0480 !       GET CHARACTER FROM STRING OR BUFFE
0490 ! 
0500 GETCHR CLE                   !                  SET DONE FLAG = TRUE
0510        TSB  R75              !              \  IF BUF? = TRUE THEN
0520        JZR  GC_STR           !            /
0530 !            !                 HANDLE THE STRING AS A BUFFE
0540        STBD R#,=GINTDS       !       DISABLE INTERRUPTS
0550        LDMD R24,R34          !          GET FILL PTR
0560        LDMD R26,R36          !          GET EMPTY PTR
0570        CMM  R24,R26          !          \  IF EMPTY <= FILL
0580        JCY  GC_BOK           !            /     THEN GO GET THE CHARACTER
0590 !            !                       ELSE   EMPTY BUFFE
0600 !            !                 DONE FLAG ALREADY = TRU
0610        CLM  R20              !              \
0620        STMD R20,R34          !          /  SET FILL TO 0
0630        ICM  R20              !              \
0640        STMD R20,R36          !          /  SET EMPTY TO 1
0650        JMP  RB_EX            !             DONE CLEARING BUFFER
0660 GC_BOK ADM  R26,R14          !          GET PTR TO ACTUAL CHARACTER
0670        POBD R32,+R26         !         GET CHARACTER
0680        SBM  R26,R14          !          \  SAVE NEW EMPTY PTR
0690        STMD R26,R36          !          /
0700        ICE                   !                  SET DONE FLAG = FALSE
0710 RB_EX  STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
0720        JSB  X22,CNVCHR       !        CONVERT CHARACTER
0730        JMP  GC_EX            !             DONE
0740 GC_STR TSM  R76              !              \  IF LENTGH = 0 THEN
0750        JZR  GC_EX            !             /     DONE
0760        DCM  R76              !              LENGTH=LENGTH-1
0770        POBD R32,+R14         !         GET THE CHARACTER
0780        ICE                   !                  SET DONE FLAG = FALSE
0790 GC_EX  RTN  
0800 ! 
0810 !       CHARACTER CONVERSIO
0820 ! 
0830 CNVCHR LDM  R20,R70          !          GET CONVERSION PTR
0840        JNZ  CEXIST           !            \  IF PTR = 0
0850 CC_EX  RTN                   !                  /     THEN NO CONVERSION
0860 CEXIST JPS  CC_PRS
0870 ! 
0880 !       CONVERSION BY INDE
0890 ! 
0900        POMD R2,+R20          !         GET LENGTH OF CONV STR
0910        TSB  R3               !              \ IF LENGTH > 255
0920        JNZ  CC_IND           !           /    THEN CAN ALWAYS CONVERT
0930        CMB  R2,R32           !          \ IF LENGTH < CHARACTER
0940        JNC  CC_EX            !            /    THEN CAN'T CONVERT
0950 CC_IND CLM  R2               !              \ GET PTR TO CONV. CHAR
0960        LDB  R2,R32
0970        ADM  R2,R20           !          /
0980        LDBD R32,R2           !          GET CONVERTED CHARACTER
0990        RTN  
1000 ! 
1010 !       CONVERSION BY PAIR
1020 ! 
1030 CC_PRS LDB  R2,=200          !          \ MAKE ADDR. INTO REAL ADDR IN R W
1040        ORB  R21,R2           !           /
1050        POMD R2,+R20          !         GET LENGTH OF CONV STR
1060        JEV  CC_OK            !            \  IF LENGTH ODD
1070 CC_OK+ DCM  R#               !       /     THEN SUBTRACT 1
1080 CC_OK  JZR  CC_EX            !            IF LENGTH=0 THEN CAN'T CONVERT
1090        POMD R0,+R20          !         GET MATCH CHARACTER AND REPLACE CHAR
1100        CMB  R0,R32           !        DOES IT MATCH SOURCE CHAR
1110        JZR  CC_FND           !             - YES
1120        DCM  R2               !        \  LENGTH = LENGTH - 2
1130        JMP  CC_OK+
1140 CC_FND LDM  R2,R0            !            GET OUT OF R0
1150        STB  R3,R32           !           GET CONVERTED CHARACTER
1160        RTN  
1170 !        HED REGISTER CONVENTION
1180 ! ***************************************************************************
1190 ! 
1200 !       REGISTERS !  USAGE                 WHERE USE
1210 ! 
1220 !       ---------------------------------------------------------------------
1230 ! 
1240 !       R0  !        COUNTER               CDIS
1250 !           !        SCRATCH PAD           CNVCH
1260 ! 
1270 !       R2-3 !       STRATCH PAD           CNVCH
1280 ! 
1290 !       R14-15 !     STRING ADDRESS        BUFFERS IN CDISP / CWRIT
1300 !           !        CHARACTER POINTER     STRINGS IN CDISP / CWRIT
1310 ! 
1320 !       R20-21 !     SCRATCH PA
1330 ! 
1340 !       R22-23 !     BASE ADDR. OF BINAR
1350 ! 
1360 !       R24-25 !     TEMP. FILL POINTER    BUFFERS IN CDISP / CWRIT
1370 ! 
1380 !       R26-27 !     TEMP. EMPTY POINTER   BUFFERS IN CDISP / CWRIT
1390 ! 
1400 !       R30 !        SCRATCH PAD           RETRH
1410 ! 
1420 !       R32 !        CURRENT CHARACTE
1430 ! 
1440 !       R33 !        SCRATCH PAD           SETCU
1450 ! 
1460 !       R34-35 !     FILL  POINTER ADDR.   BUFFERS IN CDISP / CWRIT
1470 ! 
1480 !       R36-37 !     EMPTY POINTER ADDR.   BUFFERS IN CDISP / CWRIT
1490 ! 
1500 !       R40-41 !     SCRATCH PAD           LOG EOL SERVIC
1510 ! 
1520 !       R44-45 !     SCRATCH PAD           LOG EOL SERVIC
1530 ! 
1540 !       R46-47 !     CURSOR POSITION       CRT CONTRO
1550 !           !        PRINT BUFFER POS.     CPRIN
1560 ! 
1570 !       R54 !        COUNTER               CPRIN
1580 ! 
1590 !       R56-57 !     START OF SCREEN POS
1600 ! 
1610 !       R66-67 !     SCRATCH PAD           TRYEOS ( IN CDISP 
1620 ! 
1630 !       R70-71 !     CONVERT TABLE PTR
1640 ! 
1650 !       R74 !        ON CCODE INDICATOR    CDIS
1660 ! 
1670 !       R75 !        BUFFER INDICATIO
1680 ! 
1690 !       R76-77 !     STRING LENGTH         STRINGS IN CDISP / CWRIT
1700 ! 
1710 ! 
1720 ! ***************************************************************************
1730 !        HED R/W LOCATIONS USED BY THE BINAR
1740 KEYSVC BSZ  1                !                 TRIGGER FOR EOL KBD BRANCHES
1750 KEYEOL BSZ  2                !                 JUMP ADDRESS FOR ON KBD
1760 KBDCNT BSZ  2                !                 NUMBER KEYCODES IN KBD BUFFER
1770 KBDSAV BSZ  80D              !               KBD BUFFER
1780 K_CNV  BSZ  2                !                 KBD CONVERSION PTR
1790 OLDKEY BSZ  1                !                 LAST KEY CODE
1800 KEYRPT BSZ  2                !                 COUNT VALUE FOR AUTO REPEAT
1810 CCDEOL BSZ  2                !                 JUMP ADDRESS FOR ON CCODE
1820 CCD?   BSZ  1                !                 ON CCODE INDICATOR
1830 IPSVC  BSZ  1                !                 SERVICE INDICATOR FOR ON KBD / ON CCODE
1840 PRTPTR BSZ  2                !                 POINTER INTO PRINT BUFFER ( OFFSET )
1850 PRTBUF ASC  "                                " ! 32D
1860 !           !                  CPRINT PRINTER BUFFE
1870 ! DO_SVC BSZ 1 !                TRACE EOL FLA
1880 !        HED EQUATE
1890 ! 
1900 !       ALPHABE
1910 ! 
1920 !       USED IN KEYWORD TABLES TO INDICATE THA
1930 !       THE END OF THE KEYWORD HAS OCCURE
1940 !       ( BY HAVING THE MOST SIGNIFICANT BIT SET 
1950 ! 
1960 A      EQU  301
1970 B      EQU  302
1980 C      EQU  303
1990 D      EQU  304
2000 E      EQU  305
2010 F      EQU  306
2020 G      EQU  307
2030 H      EQU  310
2040 I      EQU  311
2050 J      EQU  312
2060 K      EQU  313
2070 L      EQU  314
2080 M      EQU  315
2090 N      EQU  316
2100 O      EQU  317
2110 P      EQU  320
2120 Q      EQU  321
2130 R      EQU  322
2140 S      EQU  323
2150 T      EQU  324
2160 U      EQU  325
2170 V      EQU  326
2180 W      EQU  327
2190 X      EQU  330
2200 Y      EQU  331
2210 Z      EQU  332
2220 $      EQU  244
2230 ! 
2240 !       MISCELLANEOU
2250 ! 
2260 TRUE   EQU  377
2270 !        HED END OF BINAR
2280 DUMMY  RTN  
2290 ! 
2300 !       LENGTH OF BINAR
2310 ! 
2320 LENGTH BSZ  0
2330        LNK  MY&IP6.asm
