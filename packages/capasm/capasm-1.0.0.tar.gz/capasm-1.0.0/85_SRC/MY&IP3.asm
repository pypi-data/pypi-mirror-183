0010 !  MY&IP3 - 3RD PART OF IPBI
0020 !        HED LOG EOL INTERRUPT COD
0030 ! 
0040 !       ON CCODE - EOL INTERRUP
0050 ! 
0060 LOGCCD LDB  R40,=200         !         GET 'ON CCODE' INDICATOR
0070        JMP  COMLOG           !            GOTO COMMON CODE
0080 ! 
0090 !       ON KBD ! - EOL INTERRUP
0100 ! 
0110 LOGONK CLB  R40              !              \
0120        STBD R40,X22,KEYSVC   !   /  DISARM EOL INTERRUPTS
0130        LDB  R40,=1           !           GET 'ON KBD' INDICATOR
0140 COMLOG JSB  X22,D_SERV       !        DEMAND END OF LINE SERVICE
0150        LDBD R41,X22,IPSVC    !    \   'OR' DEMAND INDICATION
0160        ORB  R41,R40          !                   SO THAT SIMULTANEOUS
0170        STBD R41,X22,IPSVC    !    /        DEMANDS WORK
0180        RTN  
0190 ! 
0200 !       DEMAND END OF LINE SERVIC
0210 ! 
0220 D_SERV LDB  R45,=2           !           \
0230        LDBD R44,=SVCWRD      !       \  SHOW THAT THE
0240        ORB  R44,R45          !           /       'IOROM' WANTS
0250        STBD R44,=SVCWRD      !      /        EOL SERVICE
0260        LDB  R44,=20          !          \   DEMAND EOL CHECK
0270        ORB  R17,R44          !          /
0280        RTN  
0290 ! 
0300 !       PUT KEY IN BUFFE
0310 ! 
0320 LOGKEY LDMD R24,X22,KBDCNT   !   GET COUNT IN BUFFER
0330        CMB  R24,=80D         !         \   IF COUNT>80 THEN
0340        JCY  KEYOVF           !            /      CLEAN UP KBD
0350        STM  R24,R20          !          SAVE A COPY OF COUNT
0360        ADM  R24,R22          !          \
0370        STBD R26,X24,KBDSAV   !   /   PUT KEYCODE IN THE BUFFER
0380        LDBD R27,X22,KEYSVC   !   \
0390        JZR  NOKLOG           !                IF EOL SERVICE IS ARMED
0400        JSB  X22,LOGONK       !        /      LOG EOL INTERRUPT
0410 NOKLOG ICM  R20              !              \   COUNT=COUNT+1
0420        STMD R20,X22,KBDCNT   !   /
0430        RTN  
0440 ! 
0450 !       KBD BUFFER OVERFLO
0460 ! 
0470 KEYOVF JSB  X22,MYBEEP       !        BEEP AT USER
0480        JSB  X22,OFFK.        !         DO 'OFF KBD'
0490        RTN                   !                  RETURN TO ISR TO TURN KBD BACK ON
0500 !       OR TO 'ON KBD' CODE FOR HOLD DOWN KEY
0510 !        HED END OF LINE SERVICE COD
0520 ! 
0530 !       EOL SERVICE LIN
0540 ! 
0550 MY_SVC BYT  316              !               \ JSB =EOLSVC
0560 SVCADR DEF  EOLSVC           !            /
0570        RTN  
0580 ! 
0590 !       DUMMY EOL SERVICE CODE !( WHAT THE MAINFRAM
0600 !            !                    INITIALIZES 'IOSP' TO 
0610 ! 
0620 SVCERR JSB  =ERROR+
0630        BYT  25
0640 ! 
0650 !       EOL SERVICE COD
0660 ! 
0670 EOLSVC STBD R#,=GINTDS       !       DISABLE INTERRUPTS
0680        BIN  
0690        LDMD R22,=BINTAB      !      GET BASE ADDRESS
0700        CMB  R16,=2           !           \   CHECK FOR A RUNNING PROGRAM
0710        JNZ  TRYINP           !            /
0720        CMMD R10,=PCR         !         \ IF NOT AT THE END OF THE LINE
0730        JNZ  TRYINP           !            /    THEN STILL NOT DONE WITH INPUT
0740 !       LDBD R75,X22,DO_SVC !  \ IF THIS IS THE NEXT LIN
0750 !       JZR E_CHK !             \   AFTER AN EOL BRANCH THE
0760 !       CLB  R75 !              /   CLEAR INDICATO
0770 !       STBD R75,X22,DO_SVC !  /    AND CHECK FOR TRAC
0780 !       LDB  R32,=375 !        \ CLEAR SERVICE DEMAN
0790 !       JSB =CLRBIT !          
0800 ! ESTRAC LDB !R37,R17           \ IF TRACE MOD
0810 !       ANM  R37,=10 !          \   THE
0820 !       JZR ESCHK+ !            
0830 !       JSB =TRA? !            /    TRAC
0840 ! ESCHK+ JMP SKPSVC !           DONE FOR NO
0850 E_CHK  LDBD R30,X22,IPSVC    !    \   CHECK FOR KBD OR ON CCODE
0860        JZR  CHK_EX           !            /         SERVICE REQUEST
0870        JOD  KBDSVC           !            KEYBOARD GETS FIRST CHANCE
0880 CCDSVC ANM  R#,=177,377      !      \   CLEAR SERVICE DEMAND
0890        STBD R#,X22,IPSVC     !     /
0900        LDMD R20,X22,CCDEOL   !   \   CHECK FOR VALID JUMP ADDRESS
0910        JZR  CHK_EX           !            /
0920        JMP  JAM_PC           !            PERFORM THE BRANCH
0930 KBDSVC ANM  R#,=376,377      !      \   CLEAR SERVICE DEMAND
0940        STBD R#,X22,IPSVC     !     /
0950        LDMD R20,X22,KEYEOL   !   \   CHECK FOR VALID JUMP ADDRESS
0960        JZR  SVC_EX           !            /
0970 JAM_PC JSB  =SETTR1          !           SET UP FOR BRANCH TRACE
0980        STMD R10,=ONFLAG      !      SAVE RETURN INCASE OF GOSUB
0990        LDM  R10,R20          !          JAM IN NEW BASIC.PC
1000        LDB  R16,=7           !           ???? FROM ON KEY # CODE
1010 !       STBD R16,X22,DO_SVC !  SET BRANCH INDICATO
1020 !       JMP SVC_EX !           DON`T CLEAR SERVICE DEMAN
1030 CHK_EX LDB  R32,=375         !       \   CLEAR SERVICE REQUEST
1040        JSB  =CLRBIT          !           /
1050 SVC_EX BSZ  0
1060        JSB  X22,OLDSVC       !        CALL I/O ROM EOL CODE
1070        BIN  
1080        LDMD R22,=BINTAB      !      GET BASE ADDRESS
1090        LDBD R20,X22,IPSVC    !    GET SERVICE FLAG
1100        JZR  SKPSVC           !            DON'T ASK IF NO SERVICE NEEDED
1110        JSB  X22,D_SERV
1120 SKPSVC STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
1130        RTN  
1140 ! 
1150 ! 
1160 TRYINP LDM  R20,R6           !          \   GET POINTER TO RETURN STACK
1170        SBM  R20,=4,0         !       /      SO EOLSVC CAN MODIFY RET. ADDR
1180        LDM  R46,=CLKHIT      !    LOAD TIMERS ENTRY POINT
1190        ANM  R32,=376,377     !  MASK OFF MY BITS
1200        TSB  R32              !          \  IF TIMERS HAVE INTERRUPTED
1210        JNZ  CNDHIT           !            /     THEN FINISHED
1220        LDM  R46,=CHREDT      !   LOAD 'JSB =CHEDIT' ENTRY POINT
1230        LDBD R45,=SVCWRD      !      \  IF KEY INTERRUPT
1240        JOD  CNDHIT           !            /     THEN FINISHED
1250        LDM  R46,=XCBIT3      !    OTHERWISE LET INPUT FINISH
1260 CNDHIT STMD R46,R20          !          MODIFY RETURN ADDRESS
1270        DRP  R32              !                BECAUSE OF R# IN CLKHIT
1280        JMP  SKPSVC
1290 ! 
1300 ! 
1310 ! 
1320 OLDSVC RTN                   !                   LINK INTO I/O ROM END OF LINE
1330        RTN                   !                   SERVICE CODE IF IT EXISTS
1340        RTN  
1350        RTN  
1360        RTN  
1370        RTN  
1380        RTN  
1390        RTN  
1400        RTN                   !                  SPARE RETURN - FOR SAFETY
1410 ! 
1420 ! 
1430 !       POTENTIAL PROBLEM 
1440 !       THIS CODE MIGHT CLEAR I/O ROM SERVICE REQUESTS WHEN THER
1450 !       ARE STILL ROUTINES TO BE SERVICE
1460 ! 
1470 ! 
1480 !       SOLUTION 
1490 !       THE I/O ROM ( OR ANY ROM THAT USES I/O ROM EOLSVC LINK 
1500 !       WILL CHECK TO SEE IF R17 HAS I/O SERVICE CLEARED - IF I
1510 !       DOES THAT ROM WILL NOT DO END-OF-LINE CHECKS FOR BRANCHIN
1520 !       BUT WILL CHECK TO SEE IF IT NEEDS SERVICE AND THEN SE
1530 !       'SVCWRD' AND REGISTER 17 IF IT DOES NEED SERVICE
1540 ! 
1550 !        HED ON CCODE / OFF CCOD
1560 ! 
1570 !       ON CCODE ( GOTO / GOSUB 
1580 ! 
1590        BYT  241
1600 ONCOD. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
1610        BIN  
1620        STMD R10,X22,CCDEOL   !   SAVE BASIC P.C.
1630        ADM  R10,=3,0         !       SKIP OVER GOTO/GOSUB
1640        LDB  R46,=TRUE        !     \  SET ON CCODE
1650        STBD R46,X22,CCD?     !     /      INDICATOR
1660        RTN  
1670 ! 
1680 !       OFF CCOD
1690 ! 
1700        BYT  241
1710 OFFC.  LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
1720        BIN  
1730        CLB  R46              !            \  CLEAR ON CCODE
1740        STBD R46,X22,CCD?     !     /      INDICATOR
1750        RTN  
1760 !        HED CRT CONTROL EXECUTION COD
1770 ! 
1780 !       CLINE !< Line 
1790 ! 
1800        BYT  241
1810 CLINE. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
1820        JSB  =ALPHA.          !           GO INTO ALPHA MODE
1830        JSB  =ONEB            !             GET BINARY VALUE OF Line
1840        BCD                   !                   \
1850        LLM  R46              !          \
1860        BIN                   !                     \   CRTRAM = Line * 64
1870        LLM  R46              !            /
1880        LLM  R46              !           /
1890        JSB  X22,STORAM       !        /
1900        RTN  
1910 ! 
1920 !       CCURSOR < Position 
1930 ! 
1940        BYT  241
1950 CCURS. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
1960        JSB  =ALPHA.          !           GO INTO ALPHA MODE
1970        JSB  X22,CLRCUR       !        CALL Clear_cursor
1980        JSB  =ONEB            !             GET BINARY VALUE OF Position
1990        BIN                   !                   \
2000        LLM  R46              !             CRTBYT = Position * 2
2010        JSB  X22,STOBYT       !        /
2020        RTN  
2030 ! 
2040 !       CCLEA
2050 ! 
2060        BYT  241
2070 CCLR.  LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
2080        JSB  =CRTWPO          !           TURN OFF CRT
2090        BIN  
2100        JSB  =ALPHA.          !           GO INTO ALPHA MODE
2110        CLM  R46              !           \
2120        JSB  X22,STOBYT       !           SET TO START OF CRT MEMORY
2130        JSB  X22,STORAM       !        /
2140        LDM  R46,=0,10        !     COUNT=2048
2150        LDB  R32,=15          !       CHARACTER=CR ( DISPLAYED AS BLANK )
2160 ! 
2170 !       THE CARRIAGE RETURN IS USED TO FILL THE SCREE
2180 !       BECAUSE IF BLANKS ARE USED AND THE USER TYPE
2190 !       CALCULATOR MODE LINES IN FOR EXECUTION THE SYSTE
2200 !       HUNTS TILL A CR IS FOUND OR 96 CHARACTERS - NO
2210 !       A FATAL BUG - BUT ANNOYING
2220 ! 
2230 !       POTENTIAL PROBLE
2240 ! 
2250 !       WHAT HAPPENS WHEN A SCREEN FULL OF BLANKS ( OR CR'S 
2260 !       IS TO BE DUMPED TO AN EXTERNAL PRINTER 
2270 ! 
2280 !       SOLUTIO
2290 ! 
2300 !       WHEN CCHR$ READS THE SCREEN - CHANGE AL
2310 !       CARRIAGE RETURNS INTO BLANKS
2320 ! 
2330 CL_LP  JSB  =CHKSTS          !           WAIT TIL CRT CHIP READY
2340        STBD R32,=CRTDAT      !      SEND CHARACTER
2350        DCM  R46              !          COUNT=COUNT-1
2360        JNZ  CL_LP            !             LOOP UNTIL COUNT=0
2370        JSB  X22,STORAM       !        CRTRAM = 0
2380        JSB  X22,STOBYT       !        CRTBYT = 0
2390        JSB  =CRTUNW          !           TURN ON CRT
2400        RTN  
2410 ! 
2420 !       CCPO
2430 ! 
2440        BYT  0,55             !              NUM FUNCTION - NO PARAMETERS
2450 CCPOS. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
2460        LDMD R46,=CRTBYT      !      GET CRT POSITION
2470        BIN  
2480        LRM  R47              !           MESSES UP 40-45 - DON'T CARE
2490 FNCRTN LDM  R36,R46          !     \
2500        JSB  =CONBIN          !           /  CONVERT BINARY TO REAL
2510        PUMD R40,+R12         !         PUSH VALUE ONTO STACK
2520        RTN  
2530 ! 
2540 !       CLPO
2550 ! 
2560        BYT  0,55             !              NUM FUNCTION - NO PARAMETERS
2570 CLPOS. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
2580        LDMD R46,=CRTRAM      !      GET CRT WINDOW POSITION
2590        BCD                   !                   FUNCTION IS NOT IN BCD MODE
2600        LRM  R47              !          \
2610        BIN                   !                    \
2620        LRM  R47              !            /  MAKE INTO 0 TO 63 VALUE
2630        LRM  R47              !           /
2640        JMP  FNCRTN           !            GO TO COMMON CODE
2650 ! 
2660 !       CCHR
2670 ! 
2680        BYT  40,56            !             STR FUNCTION - 2 NUMERIC PARAMETERS
2690 CCHR$. JSB  =TWOB            !             GET POSITION PARAMETERS
2700        BIN  
2710        LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
2720        LDM  R46,R56          !     GET POSITION
2730        STM  R26,R56          !       GET NUMBER OF CHARS TO READ
2740        JZR  NULLST           !            RETURN A NULL STRING IF LENGTH=0
2750        JNG  BADPRM           !            GIVE PARAM ERROR     IF LENGTH<0
2760        ANM  R46,=377,7       !    MASK TO POSITION TO PROPER SIZE
2770        LLM  R46              !        ADJUST BECAUSE OF NIBBLE ORGANIZATION OF CRT
2780        JSB  =ALPHA.          !           GO INTO ALPHA MODE
2790        JSB  =RSMEM-          !           RESERVE APPROPRIATE AMOUNT OF MEMORY
2800        JEN  CANTDO           !            CHECK TO MAKE SURE THERE IS ENOUGH MEMORY
2810        PUMD R56,+R12         !         PUSH LENGTH
2820        PUMD R26,+R12         !         PUSH POINTER
2830        JSB  X22,STOCRT       !        SET UP HARDWARE POSITION OF CRT
2840 CHR_LP JSB  =INCHR           !               GET CHARACTER
2850        PUBD R32,+R26         !            PUT CHARACTER IN STRING
2860        DCM  R56              !            DECREMENT COUNT OF NUMBER OF CHARACTERS
2870        JNZ  CHR_LP           !            LOOP UNTIL COUNT=0
2880        LDMD R46,=CRTBYT      !      GET VIRTUAL CURSOR POSITION
2890        JSB  X22,STOBYT       !        RESTORE CURRENT POSITION
2900        RTN  
2910 ! 
2920 CANTDO JSB  =ERROR           !            GIVE 'OUT OF MEMORY' ERROR
2930        BYT  19D
2940 ! 
2950 NULLST CLM  R54              !          \
2960        PUMD R54,+R12         !         /  PUSH 'NULL' STRING ONTO STACK
2970        RTN  
2980 ! 
2990 BADPRM JSB  =ERROR           !            GIVE 'BAD PARAMETER' ERROR
3000        BYT  89D
3010 ! 
3020 !       CWRITE <String_variable
3030 ! 
3040        BYT  241
3050 CWRT.  LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
3060        JSB  X22,FNDSTR       !        GET STRING INFORMATION
3070 CW_LP  JSB  X22,GETCHR       !        GET CHARACTER
3080        JEZ  CW_EX            !             IF NO MORE CHARACTERS THEN DONE
3090        JSB  X22,PUTCHR       !        SEND TO CRT
3100        JMP  CW_LP 
3110 CW_EX  BSZ  0
3120        RTN  
3130        LNK  MY&IP4.asm
