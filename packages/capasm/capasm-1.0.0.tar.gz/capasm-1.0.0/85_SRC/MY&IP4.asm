0010 !  MY&IP4 - 4TH PART OF IPBI
0020 !       CDISP <String_variable
0030 ! 
0040        BYT  241
0050 CDISP. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
0060 !       JSB X22,CLRCUR !       CALL Clear_cursor     (1 14 80 TIM
0070        JSB  X22,FNDSTR       !        GET STRING / BUFFER INFORMATION
0080 !  FOR I=1 TO LEN(String$
0090 CD_LP  JSB  X22,GETCHR       !        Char=NUM(String$[I,I])
0100        JEN  CDCONT           !            \  IF NO MORE CHARACTERS THEN
0110 CD_EX  JSB  X22,SETCUR       !              CALL Set_cursor
0120        RTN                   !                  /     SUBEXIT
0130 !            !                 THE SETCUR MIGHT NOT B
0140 !            !                 NECESSAR
0150 ! 
0160 CDCONT CMB  R32,=40          !          \ IF Char<32 THEN GOTO Control_char
0170        JNC  CNTRL            !             /
0180 ! 
0190        JSB  X22,PUTCHR       !        CALL Write_crt
0200        JSB  X22,TRYEOS       !        CALL End_of_screen
0210        JMP  CD_LP            !             GOTO End_case
0220 ! 
0230 CNTRL  PUBD R32,+R6          !          \
0240        JSB  X22,CLRCUR       !          CALL Clear_cursor   (1 14 80 TIM)
0250        POBD R32,-R6          !          /
0260        CMB  R32,=16          !          \ IF Char>=14 THEN GOTO Control_code
0270        JCY  CD_CC            !             /
0280        CLB  R33              !              \
0290        LLB  R32              !               \
0300        ADM  R32,R22          !            \  ON CASE Char GOTO JUMP TABLE
0310        LDMD R32,X32,JMPTBL   !     /
0320        DCM  R32              !               /
0330        LDM  R4,R32           !           /
0340 ! 
0350 ! 
0360 CD_CC  TSB  R74              !              \  IF NO ON CCODE
0370        JZR  CD_LP            !             /     THEN GOTO End_case
0380        STBD R#,=GINTDS       !       TURN OFF INTERRUPTS
0390        JSB  X22,LOGCCD       !        LOG IN EOL SERVICE INTERRUPT
0400        TSB  R75              !              \  IF NOT A BUFFER
0410        JZR  CD_EX2           !            /     THEN SUBEXIT
0420        DCM  R26              !              \
0430        STMD R26,R36          !          /  RE-POSITION BUFFER
0440 CD_EX2 STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
0450        JMP  CD_EX            !             SUBEXIT
0460 ! 
0470 ! 
0480 CD_BL  JSB  X22,MYBEEP       !        BEEP
0490        JMP  CD_LP            !             GOTO End_case
0500 ! 
0510 ! 
0520 CD_BS  CMM  R46,R56          !          \ IF CRTBYT=CRTRAM THEN
0530        JZR  NO_BS            !             /    GOTO End_case
0540        DCM  R46              !              \
0550        DCM  R46              !                CRTBYT=CRTBYT-2
0560        JSB  X22,STOBYT       !        /
0570 NO_BS  JMP  CD_LP            !             GOTO End_case
0580 ! 
0590 ! 
0600 CD_LF  ADM  R46,=100,0       !       \  DROP DOWN 32 CHARACTERS
0610        JSB  X22,STOBYT       !        /
0620        JSB  X22,CLRLIN       !        PUT OUT 32 BLANKS TO SCREEN
0630        SBM  R46,=100,0       !       \  REPOSITION CURSOR
0640        JSB  X22,STOBYT       !        /
0650        JSB  X22,TRYEOS       !        CALL End_of_screen
0660 CD_LP2 JMP  CD_LP            !             GOTO End_case
0670 ! 
0680 ! 
0690 CD_FF  ADM  R46,=100,0       !       \
0700        JSB  X22,STORAM       !             SET CURSOR TO NEXT LINE
0710        JSB  X22,STOBYT       !        /
0720        LDB  R0,=20           !           \
0730 FF_LP  JSB  X22,CLRLIN       !         \   CLEAR 16 LINES
0740        DCB  R0               !                /
0750        JNZ  FF_LP            !             /
0760        LDM  R46,R56          !          \
0770        JSB  X22,STOBYT       !        /   POSITION SCREEN TO CURRENT LINE
0780        JMP  CD_LP2           !            GOTO End_case
0790 ! 
0800 ! 
0810 CD_CR  ANM  R46,=300,17      !      \ CRTBYT=INT(CRTBYT/64)*64
0820        JSB  X22,STOBYT       !        /
0830        JMP  CD_LP2           !            GOTO End_case
0840 !        HED CPRIN
0850 ! 
0860 !       CPRINT <String_variable
0870 ! 
0880        BYT  241
0890 CPRNT. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
0900        JSB  X22,FNDSTP       !        GET STRING / BUFFER INFORMATION
0910        LDMD R46,X22,PRTPTR   !   GET PRINT BUFFER POINTER
0920 !            !                 FOR I=1 TO LEN(String$
0930 CP_LP  JSB  X22,GETCHR       !        Char=NUM(String$[I,I])
0940        JEN  CPCONT           !            \  IF NO MORE CHARACTERS THEN
0950 CP_EX  STMD R46,X22,PRTPTR   !         SAVE PRINTER BUFFER POINTER
0960        RTN                   !                  /     SUBEXIT
0970 ! 
0980 CPCONT CMB  R32,=40          !          \ IF Char<32 THEN GOTO Control_char
0990        JNC  CNTRLP           !            /
1000 ! 
1010        JSB  X22,PRTCHR       !        CALL Print_char
1020        JMP  CP_LP            !             GOTO End_case
1030 ! 
1040 CNTRLP CMB  R32,=16          !         \ IF Char>=14 THEN GOTO Control_code
1050        JCY  CP_CC            !             /
1060        CLB  R33              !           \
1070        LLB  R32              !           \
1080        ADM  R32,R22          !        \  ON CASE Char GOTO JUMP TABLE
1090        LDMD R32,X32,PRTTBL   !     /
1100        DCM  R32              !          /
1110        LDM  R4,R32           !       /
1120 ! 
1130 ! 
1140 CP_CC  TSB  R74              !          \  IF NO ON CCODE
1150        JZR  CP_LP            !             /     THEN GOTO End_case
1160        STBD R#,=GINTDS       !       TURN OFF INTERRUPTS
1170        JSB  X22,LOGCCD       !        LOG IN EOL SERVICE INTERRUPT
1180        TSB  R75              !        \  IF NOT A BUFFER
1190        JZR  CP_EX2           !            /     THEN SUBEXIT
1200        DCM  R26              !         \
1210        STMD R26,R36          !          /  RE-POSITION BUFFER
1220 CP_EX2 STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
1230        JMP  CP_EX            !             SUBEXIT
1240 ! 
1250 ! 
1260 CP_BL  JSB  X22,MYBEEP       !        BEEP
1270        JMP  CP_LP            !             GOTO End_case
1280 ! 
1290 ! 
1300 CP_BS  TSM  R46              !         \ IF ALREADY AT LEFT MARGIN THEN
1310        JZR  NO_BSP           !            /    GOTO End_case
1320        DCM  R46              !        BACK UP POINTER IN PRINT BUFFER
1330 NO_BSP JMP  CP_LP            !             GOTO End_case
1340 ! 
1350 ! 
1360 CP_LF  JSB  X22,DMPPRT       !        DUMP THE CURRENT BUFFER TO THE PRINTER
1370        JMP  CP_LP            !             GOTO End_case
1380 ! 
1390 ! 
1400 CP_FF  JSB  X22,DMPPRT       !        DUMP AND CLEAR THE PRINT BUFFER
1410        CLM  R46              !           SET POINTER TO THE LEFT MARGIN
1420        LDB  R54,=4           !        \
1430 FF_LPP JSB  X22,DMPPRT       !         \   PRINT 4  LINES
1440        DCB  R54              !           /
1450        JNZ  FF_LPP           !            /
1460        JMP  CP_LP            !             GOTO End_case
1470 ! 
1480 ! 
1490 CP_CR  CLM  R46              !          SET POINTER IN PRINTER BUFFER TO ZERO
1500        JMP  CP_LP            !             GOTO End_case
1510 !        HED CRT AND PRINTER UTILITIE
1520 ! 
1530 !       CLEAR CURRENT LIN
1540 ! 
1550 CLRLIN LDB  R20,=15          ! 
1560        LDB  R21,=41          !       COUNT = 33 ( IN CASE OF LF )
1570 CLN_LP JSB  =CHKSTS          !           WAIT FOR CRT CHIP
1580        STBD R20,=CRTDAT      !      SEND CHARACTER TO CRT
1590        DCB  R21              !           COUNT=COUNT-1
1600        JNZ  CLN_LP           !            LOOP UNTIL COUNT=0
1610        ADM  R46,=100,0       !        \  POSITION CURSOR AT NEXT LINE
1620        JSB  X22,STOBYT       !        /
1630        RTN  
1640 ! 
1650 !       SET CURSO
1660 ! 
1670 SETCUR JSB  =INCHR           !            GET CURRENT CURSOR CHARACTER
1680        LDB  R33,=200         !      \
1690        ORB  R32,R33          !     /  SET CURSOR BIT
1700 CURCOM LDMD R46,=CRTBYT      !      BECAUSE INTIALIZATION HASN'T
1710 !           !                  OCCURED FOR CLRCU
1720        JSB  X22,STOBYT       !        REPOSITION CRT
1730        JSB  =CHKSTS          !           \  SEND CHARACTER TO THE CRT
1740        STBD R32,=CRTDAT      !      /
1750        JSB  X22,STOBYT       !        REPOSITION CRT
1760        RTN  
1770 ! 
1780 !       CLEAR CURSO
1790 ! 
1800 CLRCUR JSB  =INCHR           !            GET CURRENT CURSOR CHARACTER
1810        ANM  R32,=177,377     !   MASK OUT CURSOR BIT
1820        JMP  CURCOM           !            GOTO COMMON CURSOR CODE
1830 ! 
1840 !       END OF SCREEN SCROLLIN
1850 ! 
1860 TRYEOS CMM  R46,R56          !      \  IF CRTBYT > CRTRAM THEN
1870        JZR  EOS_EX           !                  TRY NORMAL TEST
1880        JCY  EOSNRM           !            /
1890 !           !                        OTHERWISE WRAP-AROUND OCCURRE
1900        LDM  R66,=0,20        !     \     IF (4096-CRTRAM)+CRTBYT < 512
1910        SBM  R66,R56          !       \       THEN NO END OF SCREEN OCCURED
1920        ADM  R66,R46          !        \      ELSE DO END OF SCREEN ADJUST
1930        CMM  R66,=377,3       !     /
1940        JNC  EOS_EX           !             /
1950        JMP  DO_EOS           !            /
1960 EOSNRM LDM  R66,R56          !   \  IF CRTBYT-CRTRAM > 512 THEN
1970        ADM  R66,=377,3       !    \
1980        SBM  R66,R46          !   /    THEN DO END OF SCREEN ADJUST
1990        JCY  EOS_EX           !            /     ELSE NO END OF SCREEN OCCURRED
2000 DO_EOS ADM  R56,=100,0       !  \   CRTRAM=CRTRAM+64
2010        JSB  X22,STRAM2       !        /
2020        JSB  X22,CLRLIN       !        CLEAR THE NEXT LINE ON THE SCREEN
2030        SBM  R46,=100,0       !  \   RE-POSITION CURSOR
2040        JSB  X22,STOBYT       !        /
2050 EOS_EX RTN  
2060 ! 
2070 !       STORE CRTBY
2080 ! 
2090 STOBYT ANM  R46,=377,17      !  MASK TO PROPER SIZE
2100        STMD R46,=CRTBYT      !      STORE IN R/W LOCATION
2110 STOCRT JSB  =CHKSTS          !           IS CRT CHIP READY ?
2120        STMD R46,=CRTBAD      !      STORE IN CRT CHIP
2130        RTN  
2140 ! 
2150 !       STORE CRTRA
2160 ! 
2170 STORAM DRP  R46              !                NORMAL ENTRY POINT
2180 STRAM2 SAD                   !                   SAVE ARP&DRP
2190        JSB  =RETRHI          !           DEMAND A RETRACE
2200        PAD                   !                   RESTORE ARP&DRP
2210        ANM  R#,=300,17       !  MASK TO PROPER SIZE
2220        STMD R#,=CRTRAM       !       STORE IN R/W LOCATION
2230        STMD R#,=CRTSAD       !       STORE IN CRT CHIP
2240        STM  R#,R56           !  SAVE IN LOCAL R/W MEMORY
2250        RTN  
2260 ! 
2270 !       WRITE CHARACTER TO CR
2280 ! 
2290 PUTCHR JSB  =CHKSTS          !           WAIT TILL CRT IS READY
2300        STBD R32,=CRTDAT      !      SEND CHARACTER TO THE CRT
2310        ICM  R46              !  \
2320        ICM  R46              !     CRTBYT=CRTBYT+2
2330        JSB  X22,STOBYT       !        /
2340        RTN  
2350 ! 
2360 !       BEE
2370 ! 
2380 !       DONE MYSELF BECAUSE THE SYSTEM COUNTS RETRACE
2390 !       AND HAS INTERRUPTS DISABLED - TOO COSTLY IN CP
2400 !       TIME FOR TERMINAL EMULATOR CAPABILITIE
2410 ! 
2420 MYBEEP LDB  R20,=100         !  \
2430        STBD R20,=KEYSTS      !      /  START STANDARD BEEP
2440        LDM  R20,=377,5       !  \
2450 BP_LP  DCM  R20              !     LOOP FOR A WHILE
2460        JNZ  BP_LP            !             /
2470        STBD R20,=KEYSTS      !      TURN OFF BEEP
2480        RTN  
2490 ! 
2500 ! 
2510 ! 
2520 ! 
2530 !       DUMP THE PRINT BUFFE
2540 ! 
2550 DMPPRT PUMD R36,+R6          !          SAVE BUF PTR INFO
2560        LDM  R36,=32D,0       !  DETERMINE HOW MANY BLANKS
2570        LDM  R20,R22          !  COPY BINTAB
2580        ADM  R20,=31D,0       !  POINT TO END OF BUFFER
2590 DMP_LP LDBD R32,X20,PRTBUF   !   GET A CHARACTER FROM THE BACK OF THE BUFFER
2600        CMB  R32,=40          !  IF IT IS A BLANK
2610        JNZ  DO_DMP           !               THEN DECREMENT # CHARS TO PRINT
2620        DCM  R20
2630        DCB  R36
2640        JNZ  DMP_LP           !            LOOP UNTIL 0 CHARS TO PRINT
2650 DO_DMP BSZ  0                !                 \ SAVE IMPORTANT REGISTERS
2660        PUMD R46,+R6          !          /
2670        LDM  R26,R22          !  \ GENERATE ADDRESS OF PRINT BUFFER
2680        ADM  R26,=PRTBUF      !  /
2690        JSB  =PRDVR1          !           PRINT DATA
2700        POMD R46,-R6          !          \ RESTORE IMPORTANT REGISTERS
2710        POMD R36,-R6          !          /
2720 ! 
2730 !       CLEAR PRINT BUFFE
2740 ! 
2750 CLRPRT LDM  R20,R22          !    COPY BINTAB
2760        LDB  R0,=32D          !  CONSTANT FOR CLEARING 32 BYTES
2770        LDB  R32,=40          !  BLANK CHARACTER FOR BUFFER
2780 CLR_LP STBD R32,X20,PRTBUF   !   PUT BLANK INTO BUFFER
2790        ICM  R20              !  ADVANCE INDEX REGISTER
2800        DCB  R0               !  DECREMENT COUNT
2810        JNZ  CLR_LP
2820        RTN  
2830 ! 
2840 !       PUT CHARACTER INTO PRINTER BUFFE
2850 ! 
2860 PRTCHR ICM  R46              !  GET OFFSET TO NEXT CHARACTER
2870        LDM  R56,R22          !  GET COPY OF BINTAB
2880        ADM  R56,R46          !  ADD IN OFFSET
2890        DCM  R56
2900        STBD R32,X56,PRTBUF   !   STORE CHARACTER IN THE BUFFER
2910        CMM  R46,=32D,0       !  \ IF THAT WAS THE LAST CHAR
2920        JNZ  PC_EX            !             /    THEN
2930        JSB  X22,DMPPRT       !             DUMP THE PRINT BUFFER
2940        CLM  R46              !  SET PRINT BUFFER OFFSET BACK TO LEFT MARGIN
2950 PC_EX  RTN  
2960        LNK  MY&IP5.asm
