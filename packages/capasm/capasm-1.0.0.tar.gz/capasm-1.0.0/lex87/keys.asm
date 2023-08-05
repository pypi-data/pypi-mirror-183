1000 !*********************************************************************
1010 !*                                                                   *
1020 !* TAKING THE 'KYIDLE' HOOK AND BUFFERING THE KEYBOARD               *
1030 !*                                                                   *
1040 !*             (c) 1981 Hewlett-Packard Co.                          *
1050 !*                                                                   *
1060 !*   THIS BINARY PROGRAM TAKES OVER THE 'KYIDLE' HOOK AND PUTS ALL   *
1070 !* KEYS PRESSED INTO A BUFFER EXCEPT FOR THOSE KEYCODES LISTED IN    *
1080 !* THE TABLE STARTING AT 'KEYTAB' (RIGHT NOW, THOSE KEYS TO BE LEFT  *
1090 !* FOR THE SYSTEM TO HANDLE ARE THE SOFT KEYS AND THE RESET KEY. THIS*
1100 !* COULD EASILY BE CHANGED BY MODIFYING THE 'KEYTAB' TABLE). THE     *
1110 !* BINARY ALSO WATCHES FOR 'SHIFT END LINE' AND 'SHIFT UP ARROW'     *
1120 !* (WHICH IS THE 'HOME' KEY. ('UP ARROW' AND 'HOME' ACTUALLY GENERATE*
1130 !* THE SAME KEYCODE AND CAN ONLY BE DIFFERENTIATED BY CHECKING TO SEE*
1140 !* IF THE SHIFT KEY IS UP OR DOWN.)) WHEN 'END LINE' OR 'UP ARROW' IS*
1150 !* PRESSED WITH THE SHIFT KEY DOWN, THE BINARY PROGRAM CHANGES THE   *
1160 !* KEYCODE TO A DIFFERENT UNIQUE KEYCODE SO THE BASIC PROGRAM CAN    *
1170 !* TELL THE DIFFERENCE. THIS, AND SIMILAR TECHNIQUES, COULD BE       *
1180 !* APPLIED TO MOST OF THE KEYBOARD.                                  *
1190 !*                                                                   *
1200 !*********************************************************************
1210 !*                                                                   *
1220 !* The following is a sample BASIC program showing how this binary   *
1230 !* program can be used:                                              *
1240 !*                                                                   *
1250 !*   100 TAKE KEYBOARD                                               *
1260 !*   110 A$=KEY$                                                     *
1270 !*   120 IF A$="" THEN 110                                           *
1280 !*   130 IF A$="E" THEN 200                                          *
1290 !*   140 DISP "THAT WAS THE " & A$ & " KEY."                         *
1300 !*   150 GOTO 110                                                    *
1310 !*   200 RELEASE KEYBOARD                                            *
1320 !*   210 DISP "DONE"                                                 *
1330 !*   220 END                                                         *
1340 !*                                                                   *
1350 !*********************************************************************
1360 MYBPGM#  EQU 50                 ! BINARY PROGRAM NUMBER
1370          NAM 50,KEYS            ! NAME BLOCK FOR BINARY
1380          DEF RUNTIM             ! ADDRESS OF RUNTIME ADDRESSES
1390          DEF ASCIIS             ! ADDRESS OF ASCII TABLE
1400          DEF PARSE              ! ADDRESS OF PARSE ADDRESSES
1410          DEF ERMSG              ! ADDRESS OF ERROR MESSAGES
1420          DEF INIT               ! ADDRESS OF INITIALIZATION ROUTINE
1430 RUNTIM   BSZ 2                  ! PLACE HOLDER
1440          DEF TAKE.              ! RUNTIME FOR 'TAKE KEYBOARD'
1450          DEF RELEAS.            ! RUNTIME FOR 'RELEASE KEYBOARD'
1460          DEF KEY$.              ! RUNTIME FOR 'KEY$'
1470          DEF REVDATE.           ! RUNTIME FOR REVISION
1480 PARSE    BSZ 2                  ! PLACE HOLDER
1490          DEF COMPARS            ! PARSE ROUTINE FOR 'TAKE KEYBOARD'
1500          DEF COMPARS            ! PARSE ROUTINE FOR 'RELEASE KEYBOARD'
1510          BYT 377,377            ! END OF RELOCATABLES
1520 !*********************************************************************
1530 ASCIIS   BSZ 0
1540          ASP "TAKE KEYBOARD"    ! TOKEN 1
1550          ASP "RELEASE KEYBOARD" ! TOKEN 2
1560          ASP "KEY$"             ! TOKEN 3
1570          ASP "REV DATE"         ! TOKEN 4
1580 ERMSG    BYT 377                ! END OF ASCII TABLE
1590 !*********************************************************************
1600 !*   BECAUSE THIS PROGRAM TAKES OVER 'KYIDLE', SOME SPECIAL TRICKS   *
1610 !* ARE NEEDED. 'KYIDLE' IS AN INTERRUPT HOOK WHICH MEANS THAT THE    *
1620 !* BASE ADDRESS OF THIS BINARY PROGRAM MAY NOT BE IN 'BINTAB'. A     *
1630 !* METHOD IS NEEDED FOR THE HOOK ROUTINE ('USEKEY' IN THIS CASE) TO  *
1640 !* KNOW WHAT THE BASE ADDRESS IS. SINCE THE 'KYIDLE' HOOK IS 7 BYTES *
1650 !* LONG AND IT ONLY TAKES 4 BYTES TO DO 'JSB =USEKEY' & 'RTN', 3     *
1660 !* BYTES ARE LEFT UNUSED (AND THAT WE CAN BE SURE NO ONE ELSE IS     *
1670 !* GOING TO USE, AS LONG AS THIS BINARY HAS THE HOOK, WHICH IS AS    *
1680 !* LONG AS IT MATTERS). TWO OF THESE BYTES ARE USED TO STORE THE     *
1690 !* BASE ADDRESS OF THIS BINARY PROGRAM. WE'VE NAMED THE LOCATION     *
1700 !* 'MYBTAB' AND DEFINED ITS ADDRESS AS 4 HIGHER THAN THAT OF 'KYIDLE'*
1710 !* (103703 AND 103677 RESPECTIVELY.)                                 *
1720 !*    THE 'INIT' ROUTINE DOESN'T HAVE TO DO ANYTHING IN THIS PROGRAM *
1730 !* SINCE 'LOAD' AND 'SCRATCH' CAN'T BE PERFORMED WHILE THE BINARY    *
1740 !* HAS THE HOOK, AND DURING A 'RESET' THE SYSTEM WILL HAVE ALREADY   *
1750 !* PUT 'RTN's BACK INTO 'KYIDLE'. WE ONLY TAKE THE HOOK WHEN A       *
1760 !* 'TAKE KEYBOARD' COMMAND IS EXECUTED, SO THERE'S NOTHING FOR INIT  *
1770 !* TO DO.                                                            *
1780 !*    THE BASIC PROGRAM WRITER NEEDS TO BE VERY CAREFUL, HOWEVER,    *
1790 !* USING THIS BINARY, BECAUSE IF HE WERE TO EXECUTE A 'STOP' OR 'END'*
1800 !* COMMAND WHILE THE HOOK IS TAKEN, THE KEYBOARD WILL EFFECTIVELY BE *
1810 !* LOCKED UP EXCEPT FOR THE 'RESET' KEY AND, THUS, 'RESET' WOULD THEN*
1820 !* BE THE USERS ONLY RECOURSE.                                       *
1830 !*********************************************************************
1840 INIT     RTN                    ! ALL DONE
1850 !*********************************************************************
1860 !* NEITHER 'TAKE KEYBOARD' OR 'RELEASE KEYBOARD' HAVE ANY PARAMETERS *
1870 !* SO THEY BOTH USE THE SAME PARSE ROUTINE, WHICH SIMPLY PUSHES OUT  *
1880 !* THE THREE BYTE SEQUENCE FOR THE KEYWORD AND THEN DOES A 'SCAN' FOR*
1890 !* THE SYSTEM, SO THAT R14 WILL HAVE THE NEXT TOKEN WHEN WE RETURN.  *
1900 !*********************************************************************
1910 COMPARS  LDM R56,=50,371        ! BPGM # AND SYSTEM TOKEN
1920          LDB R55,R43            ! GET THE BINARY PROGRAM TOKEN #
1930          STMI R55,=PTR2-        ! STORE IT ALL OUT TO PARSE STACK
1940          JSB =SCAN              ! DO A SCAN FOR THE SYSTEM
1950          RTN 
1960 !*********************************************************************
1970 !* 'REV DATE' IS A STRING FUNCTION WITH NO PARAMETERS WHICH RETURNS  *
1980 !* AS ITS STRING VALUE THE COPYRIGHT STATEMENT AND REVISION CODE OF  *
1990 !* THE BINARY PROGRAM.                                               *
2000 !*********************************************************************
2010          BYT 0,56               ! NO PARAMETERS, STRING FUNCTION
2020 REVDATE. BIN                    ! FOR ADMD R45,=BINTAB
2030          LDM R43,=40D,0         ! LOAD THE LENGTH OF THE STRING
2040          DEF DATE               !      AND THE ADDRESS OF THE STRING
2050          BYT 0                  !          (MUST BE THREE BYTE ADDRESS)
2060          ADMD R45,=BINTAB       ! MAKE THE ADDRESS ABSOLUTE
2070          PUMD R43,+R12          ! PUSH IT ALL ON THE OPERATING STACK
2080          RTN                    ! DONE
2090          ASC "31.102:veR  .oC drakcaP-ttelweH 2891 )c("
2100 DATE     BSZ 0                  ! PLACE HOLDER FOR THE LABEL (ADDRESS)
2110 !*********************************************************************
2120 !* THIS IS THE TABLE OF KEYS THAT THE BINARY PROGRAM SHOULD LET THE  *
2130 !* SYSTEM HANDLE, AND IT SHOULD NOT PUT THEM IN THE BUFFER. THE TABLE*
2140 !* IS TERMINATED BY A 377, WHICH IS A KEYCODE THE KEYBOARD CONTROLLER*
2150 !* IC IS INCAPABLE OF GENERATING.                                    *
2160 !*********************************************************************
2170 KEYTAB   BYT 200                ! K1
2180          BYT 201                ! K2
2190          BYT 202                ! K3
2200          BYT 203                ! K4
2210          BYT 241                ! K5
2220          BYT 242                ! K6
2230          BYT 234                ! K7
2240          BYT 204                ! K8
2250          BYT 205                ! K9
2260          BYT 206                ! K10
2270          BYT 207                ! K11
2280          BYT 245                ! K12
2290          BYT 254                ! K13
2300          BYT 223                ! K14
2310          BYT 213                ! RESET
2320          BYT 377                ! END OF INVALID KEY TABLE
2330 !*********************************************************************
2340 !*   THIS IS THE RUNTIME ROUTINE FOR THE 'TAKE KEYBOARD' KEYWORD. IT *
2350 !* INITIALIZES POINTERS TO THE BEGINNING AND END OF THE KEYBOARD     *
2360 !* BUFFER, WHICH EXISTS FARTHER DOWN IN THE BINARY PROGRAM, TAKES    *
2370 !* OVER THE 'KYIDLE' HOOK, AND INVALIDATES THE KEY REPEAT FLAG. IF   *
2380 !* THE KEY REPEAT FLAG IS VALID, THE LAST KEY IS TAKEN FROM THE      *
2390 !* BUFFER (USING THE 'KEY$' FUNCTION), AND A KEY IS STILL DEPRESSED  *
2400 !* THE LAST KEY WILL BE PUT BACK IN THE BUFFER SO THAT IT WILL REPEAT*
2410 !* AS LONG AS THE KEY IS HELD DOWN.                                  *
2420 !*********************************************************************
2430          BYT 241
2440 TAKE.    LDMD R46,=BINTAB       ! FOR RELATIVE ADDRESSING
2450          LDM R30,=KEYBUF        ! GET ADDRESS OF KEYBOARD BUFFER
2460          ADM R30,R46            ! MAKE IT ABSOLUTE
2470          STMD R30,X46,KEYPTR    ! INITIALIZE KEY POINTER
2480          ADM R30,=80D,0         ! POINT TO END OF BUFFER
2490          STMD R30,X46,KEYEND    ! INITIALIZE KEYEND
2500          LDM R30,=USEKEY        ! ADDRESS OF KEYBOARD SERVICE ROUTINE
2510          ADM R30,R46            ! MAKE IT ABSOLUTE
2520          STM R30,R43            ! COPY TO 43&44
2530          LDB R45,=236           ! 45='RTN'
2540          LDB R42,=316           ! 42='JSB'
2550 TAKEIT   STMD R#,=KYIDLE        ! STORE OUT RTN'S OR JSB=USEKEY,RTN,BINTAB
2560          LDB R#,=377            ! INVALID REPEAT FLAG
2570          STBD R#,X46,LASTKEY    ! SET IT
2580          RTN 
2590 !*********************************************************************
2600 !* THIS IS THE RUNTIME ROUTINE FOR THE 'RELEASE KEYBOARD' KEYWORD.   *
2610 !* ALL IT DOES IS PLACE RETURNS BACK INTO THE 'KYIDLE' HOOK, THUS,   *
2620 !* GIVING UP CONTROL OF THE KEYBOARD.                                *
2630 !*********************************************************************
2640          BYT 241
2650 RELEAS.  LDMD R46,=BINTAB       ! GET BPGM'S BASE ADDRESS
2660          LDM R52,=236,236,236,236,236,236 ! LOTS OF RTNS
2670          JMP TAKEIT             ! GO STORE TO HOOK
2680 !*********************************************************************
2690 !*  'USEKEY' IS AN INTERRUPT SERVICE ROUTINE SO IT MUST BE CAREFUL TO*
2700 !* SAVE ALL CPU STATUS AND CONTENTS AND THEN RESTORE THEM WHEN DONE. *
2710 !* THE SYSTEM HAS ALREADY DONE A 'SAD' BEFORE IT DID THE 'JSB' TO    *
2720 !* 'KYIDLE'. THE ROUTINE CHECKS TO SEE IF THE BUFFER IS FULL AND IF  *
2730 !* SO THROWS THE CURRENT KEYHIT AWAY. IT THEN CHECKS FOR THE SHIFTED *
2740 !* 'UP ARROW' OR 'END LINE' KEYS AND IF SO MODIFIES THE KEYCOD TO    *
2750 !* MATCH. IT THEN CHECKS THE 'KEYTAB' TABLE TO SEE IF THIS KEY SHOULD*
2760 !* BE IGNORED. IF IT IS IN THE TABLE, THE ROUTINE JUST CLEANS UP A   *
2770 !* LITTLE AND RETURNS BACK INTO THE SYSTEM KEY HANDLING ROUTINE.     *
2780 !* OTHERWISE, IT PUTS THE NEW KEYCODE IN THE BUFFER AND UPDATES THE  *
2790 !* BUFFER POINTER. IT THEN FIGURES OUT WHAT THE DRP SHOULD BE WHEN   *
2800 !* IT RETURNS FROM THE INTERRUPT SERVICE, AND PLACES A DRP COMMAND   *
2810 !* WHERE IT WILL BE EXECUTED JUST BEFORE RETURNING (THIS IS SO THE   *
2820 !* EXTENDED MEMORY CONTROLLER CAN KEEP TRACK OF THE DRP FOR MULTI-   *
2830 !* BYTE OPERATIONS.) IT THEN RESTORES REGISTERS, THROWS AWAY TWO     *
2840 !* RETURN ADDRESSES, AND RETURNS TO WHATEVER WAS HAPPENING BEFORE    *
2850 !* THE KEYBOARD INTERRUPTED.                                         *
2860 !*********************************************************************
2870 USEKEY   STBD R#,=GINTDS        ! DISABLE GLOBAL INTERRUPTS
2880          BIN                    ! FOR EVERYTHING
2890          PUMD R2,+R6            ! SAVE 2&3
2900          PUMD R40,+R6           ! SAVE THE 40'S
2910          LDM R40,R20            ! AND THE 20'S
2920          LDMD R26,=MYBTAB       ! FOR RELATIVE ANYTHING
2930          LDMD R20,X26,KEYPTR    ! GET THE KEY POINTER
2940          LDMD R22,X26,KEYEND    ! ADDRESS OF END OF BUFFER
2950          CMM R22,R20            ! BUFFER FULL?
2960          JZR RE-START           ! JIF IT IS
2970          LDBD R22,=KEYCOD       ! GET THE KEY CODE
2980          LDBD R25,=KEYSTS       ! GET KEYBOARD STATUS
2990          ANM R25,=10            ! MASK FOR SHIFT KEY
3000          JZR NOTSHIFT           ! JIF SHIFT KEY NOT DOWN
3010          CMB R22,=kUPCUR        ! UP CURSOR KEY?
3020          JNZ ENDLINE?           ! JIF NOT
3030          LDB R22,=kHOME         ! OTHERWISE MAKE IT THE HOME KEY
3040          JMP NOTSHIFT           ! FALL THROUGH
3050 ENDLINE? CMB R22,=kENDLINE      ! WAS IT THE ENDLINE KEY?
3060          JNZ NOTSHIFT           ! JIF NOT
3070          LDB R22,=kSENDLIN      ! MAKE IT SHIFT ENDLINE
3080 NOTSHIFT LDM R24,=KEYTAB        ! ADDRESS OF INVALID KEYS
3090          ADM R24,R26            ! MAKE IT ABSOLUTE
3100 KEYLOOP  POBD R23,+R24          ! GET AN INVALID KEYCODE
3110          CMB R23,=377           ! END OF TABLE?
3120          JZR KEYLOOP1           ! JIF IT IS
3130          CMB R23,R22            ! IS THIS KEY INVALID
3140          JNZ KEYLOOP            ! JIF NO MATCH
3150          JSB X26,FIXUP-R6       ! FIX UP THE R6 STACK
3160          JMP KEYRTN+            ! FALL THROUGH, LET THE SYSTEM HAVE IT
3170 KEYLOOP1 PUBD R22,+R20          ! APPEND TO THE BUFFER
3180          STMD R20,X26,KEYPTR    ! UPDATE THE POINTER
3190 RE-START CLB R20                ! \
3200          ICB R20                !  > RESTART THE KEYBOARD SCANNER
3210          STBD R20,=KEYCOD       ! /
3220          JSB X26,FIXUP-R6       ! FIX UP THE R6 STACK
3230          SBM R6,=4,0            ! TRASH TWO RETURNS
3240 KEYRTN   STBD R#,=GINTEN        ! RE-ENABLE GLOBAL INTERRUPTS
3250 DRP      BSZ 1                  ! FORCE THE DRP
3260          PAD                    ! RESTORE  THE STATUS
3270          RTN                    ! ALL DONE
3280 KEYRTN+  STBD R#,=GINTEN        ! RE-ENABLE INTERRUPTS
3290          RTN 
3300 FIXUP-R6 STMI R30,=MYBTAB       ! SAVE 30
3310          POMD R30,-R6           ! GET THE RETURN ADDRESS
3320          LDM R20,R6             ! COPY OF R6
3330          SBM R20,=20,0          ! GET DOWN TO MIDDLE OF THE SAD
3340          LDBD R20,R20           ! FETCH THE DRP BYTE
3350          ANM R20,=77,0          ! MASK OUT THE LAST DRP
3360          ADB R20,=100           ! MAKE IT INTO A DRP INSTRUCTION
3370          STBD R20,X26,DRP       ! STORE IT OUT
3380          STM R40,R20            ! RESTORE  THE 20'S
3390          POMD R40,-R6           ! RESTORE  THE 40'S
3400          POMD R2,-R6            ! RESTORE 2&3
3410          PUMD R30,+R6           ! PUT THE RETURN BACK
3420          LDMI R30,=MYBTAB       ! GET 30 BACK
3430          RTN                    ! ALL DONE
3440 !*********************************************************************
3450 !*   THIS IS THE RUNTIME ROUTINE FOR THE 'KEY$' KEYWORD. IT IS A     *
3460 !* STRING FUNCTION WITH NO PARAMETERS WHICH RETURNS A STRING WITH A  *
3470 !* LENGTH OF ONE WHOSE SOLE CHARACTER IS THE KEYCODE OF THE FIRST    *
3480 !* KEY IN THE KEYBOARD BUFFER. IF THE BUFFER WAS EMPTY, IT RETURNS   *
3490 !* A NULL STRING (LENGTH=0). WHEN IT TAKES A KEY OUT OF THE BUFFER,  *
3500 !* IT COLLAPSES ALL THE OTHER KEYCODES IN THE BUFFER AND ADJUSTS THE *
3510 !* BUFFER POINTER.                                                   *
3520 !*********************************************************************
3530          BYT 0,56
3540 KEY$.    BIN                    ! FOR EVERYTHING
3550          STBD R#,=GINTDS        ! DISABLE GLOBAL INTERRUPTS
3560          LDMD R14,=BINTAB       ! FOR ANYTHING RELATIVE
3570          LDM R20,=KEYBUF        ! ADDRESS OF KEYBOARD BUFFER
3580          ADM R20,R14            ! MAKE ADDRESS ABSOLUTE
3590          LDMD R22,X14,KEYPTR    ! GET POINTER INTO BUFFER
3600          CMM R22,R20            ! BUFFER EMPTY?
3610          JZR KEY$3              ! JIF IT IS
3620          LDM R30,R20            ! COPY 20
3630          POBD R32,+R20          ! GET A KEY
3640          STBD R32,X14,LASTKEY   ! SAVE LAST KEY FOR POSSIBLE REPEAT
3650 KEY$1    CMM R22,R20            ! BUFFER COLLAPSED
3660          JZR KEY$2              ! JIF IT IS
3670          POBD R33,+R20          ! GET A KEY
3680          PUBD R33,+R30          ! MOVE IT DOWN
3690          JMP KEY$1              ! LOOP
3700 KEY$2    DCM R22                ! ADJUST KEYPTR
3710          STMD R22,X14,KEYPTR    ! AND RESTORE  IT
3720 KEY$2+   CLM R22                ! \
3730          ICM R22                !  > LENGTH OF 1
3740 KEY$2++  PUMD R#,+R12           ! /
3750          LDM R55,=LASTKEY       ! ADDRESS OF KEYHIT
3760          BYT 0                  ! ---->  R57
3770          ADMD R55,=BINTAB       ! MAKE ADDRESS ABSOLUTE
3780          ICM R55                ! POINT TO AFTER THE KEY
3790          PUMD R55,+R12          ! PUSH ADDRESS OUT
3800          STBD R#,=GINTEN        ! RE-ENABLE GLOBAL INTERRUPTS
3810          RTN                    ! ALL DONE
3820 KEY$3    LDBD R32,X14,LASTKEY   ! CHECK LAST KEY
3830          CMB R32,=377           ! INVALID REPEAT?
3840          JZR KEY$4              ! JIF SO
3850          LDBD R32,=KEYSTS       ! GET KEYBOARD STATUS
3860          LRB R32                ! SHIFT STILL DOWN FLAG
3870          JOD KEY$2+             ! LET'S REPEAT IT
3880 KEY$4    LDB R32,=377           ! INVALID REPEAT FLAG
3890          STBD R32,X14,LASTKEY   ! SET INVALID REPEAT
3900          CLM R32                ! NO REPEAT, SO 0 LENGTH
3910          JMP KEY$2++            ! ONE MORE TIME
3920 ! ***********************************************************************
3930 LASTKEY  BSZ 1                  ! FOR KEY REPEATING PURPOSES
3940 KEYBUF   BSZ 80D                ! ALLOW UP TO 80 KEY STROKES IN BUFFER
3950 KEYPTR   BSZ 2                  ! POINTER TO INPUT POINT IN BUFFER
3960 KEYEND   BSZ 2                  ! POINTER TO END OF THE BUFFER
3970 kUPCUR   EQU 243                ! UP CURSOR KEYCODE
3980 kHOME    EQU 230                ! NEW HOME KEYCODE
3990 kENDLINE EQU 232                ! ENDLINE KEYCODE
4000 kSENDLIN EQU 227                ! NEW SHIFT END LINE KEYCODE
4010 ! ***********************************************************************
4020 ERROR+   DAD 10220              !
4030 PTR2-    DAD 177715             !
4040 SCAN     DAD 21110              !
4050 BINTAB   DAD 104070             !
4060 PTR2     DAD 177714             !
4070 ROMFL    DAD 104065             ! DEFINE SYSTEM ADDRESSES
4080 KYIDLE   DAD 103677             !
4090 GINTDS   DAD 177401             !
4100 GINTEN   DAD 177400             !
4110 MYBTAB   DAD 103703             !
4120 KEYCOD   DAD 177403             !
4130 KEYSTS   DAD 177402             !
4140          FIN                    ! TERMINATE ASSEMBLY
