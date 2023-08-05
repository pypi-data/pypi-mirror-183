1000 !*********************************************************************
1010 !* This binary program implements three CRT control statements:      *
1020 !*     AWRITE [<row>,<column>][,<string>]                            *
1030 !*     AREAD <string variable>                                       *
1040 !*     START CRT AT <absolute line #>                                *
1050 !* AWRITE allows you to do one of three things:                      *
1060 !*        1) force ALPHA mode without moving the cursor position     *
1070 !*        2) force ALPHA mode and move the cursor to a position which*
1080 !*           is relative to the top left of the current screen       *
1090 !*        3  force ALPHA mode and move the cursor to new position    *
1100 !*           and output a string at that location, leaving the cursor*
1110 !*           positioned at the beginning of the string.              *
1120 !*     In all cases the cursor is not actually displayed, until some *
1130 !*     other normal cursor movement occurs.                          *
1140 !* AREAD allows you to read a string of characters from the CRT into *
1150 !*     a string variable. Usually the cursor will have been moved to *
1160 !*     the correct position with the AWRITE statement.               *
1170 !* START CRT AT allows you to scroll the display up or down or jump  *
1180 !*     to an entirely different page, all under program control.     *
1190 !*     NOTE: this routine does not change the cursor's location in   *
1200 !*     CRT memory, so the cursor may get lost off of the screen when *
1210 !*     this command is used. It can be brought back by use of the    *
1220 !*     AWRITE statement, or by using the Home Cursor key.            *
1230 !* ALPHAB returns the revision date of the binary program.           *
1240 !*********************************************************************
1250 !*                                                                   *
1260 !* An example of how this binary might be used in BASIC is:          *
1270 !*    110 FOR I=1 TO 1000                                            *
1280 !*    120 START CRT AT IP(RND*50)                                    *
1290 !*    130 AWRITE RND*16,RND*80 @ AREAD A$                            *
1300 !*    140 AWRITE RND*16,RND*80,A$                                    *
1310 !*    150 NEXT I                                                     *
1320 !* This is guaranteed to turn any intelligent display into nonsense. *
1330 !*                                                                   *
1340 !*********************************************************************
1350 MYBPGM#  EQU 52                 ! BINARY PROGRAM NUMBER
1360          NAM 52,ALFA            ! NAME BLOCK FOR BINARY
1370          DEF RUNTIM             ! ADDRESS OF RUNTIME ADDRESSES
1380          DEF ASCIIS             ! ADDRESS OF ASCII TABLE
1390          DEF PARSE              ! ADDRESS OF PARSE ADDRESSES
1400          DEF ERMSG              ! ADDRESS OF ERROR MESSAGES
1410          DEF INIT               ! ADDRESS OF INITIALIZATION ROUTINE
1420 RUNTIM   BSZ 2                  ! PLACE HOLDER
1430          DEF ALFA.              ! RUNTIME LABEL FOR 'AWRITE'
1440          DEF AREAD.             ! RUNTIME FOR 'AREAD'
1450          DEF STARTAT.           ! CRT TOP LINE
1460          DEF REV.               ! RUNTIME FOR REVISION
1470 PARSE    BSZ 2                  ! PLACE HOLDER
1480          DEF ALPHAP             ! PARSE LABEL FOR 'AWRITE'
1490          DEF AREADP             ! PARSE LABEL FOR 'AREAD'
1500          DEF STARTATP           ! PARSE FOR TOP LINE
1510          BYT 377,377            ! END OF RELOCATABLES
1520 !*********************************************************************
1530 ASCIIS   BSZ 0
1540          ASP "AWRITE"           ! TOKEN 1
1550          ASP "AREAD"            ! TOKEN 2
1560          ASP "START CRT AT"     ! TOKEN 3
1570          ASP "ALPHAB"           ! TOKEN 4
1580 ERMSG    BYT 377                ! END OF ASCII TABLE
1590 !*********************************************************************
1600 INIT     RTN                    ! NO INITIALIZATION TO BE DONE
1610 !*********************************************************************
1620 STARTATP PUBD R43,+R6           ! SAVE TOKEN#
1630          JSB =NUMVA+            ! TRY TO GET A NUMBER
1640          JEZ ERR88              ! GOT AN ERROR
1650 OKAY     LDB R53,=371           ! BPGM TOKEN
1660          STBI R53,=PTR2-        ! STORE IT
1670          LDB R53,=MYBPGM#       ! GET MY BINARY NUMBER
1680          STBI R53,=PTR2-        ! STORE IT
1690          POBD R53,-R6           ! GET THE TOKEN NUMBER
1700          STBI R53,=PTR2-        ! STORE IT
1710          RTN                    ! ALL DONE
1720 !*********************************************************************
1730 ALPHAP   PUBD R43,+R6           ! SAVE TOKEN NUMBER
1740          JSB =NUMVA+            ! TRY TO GET A NUMBER
1750          JEZ OKAY               ! MUST BE JUST 'AWRITE'
1760          JSB =GETCMA            ! DEMAND A COMMA
1770          JSB =NUMVAL            ! DEMAND A NUMBER
1780          JEN OKAY2              ! JIF BOTH NUMBERS THERE
1790 ERR88    POBD R43,-R6           ! CLEAN UP R6
1800          JSB =ERROR+            ! ERROR HANDLING ROUTINE
1810          BYT 88D                ! ERROR NUMBER
1820 OKAY2    CMB R14,=54            ! MAKE SURE OF A COMMA
1830          JNZ OKAY               ! JIF JUST 'AWRITE X,Y'
1840          JSB =STREX+            ! PARSES A STRING EXPRESSION
1850          JEZ ERR88              ! JIF NO STRING TO ERROR
1860          JMP OKAY               ! OTHERWISE FINISH UP THE PARSING
1870 ! ***********************************************************************
1880 AREADP   PUBD R43,+R6           ! SAVE THE TOKEN
1890          JSB =SCAN              ! LET'S DO A SCAN
1900          JSB =STRREF            ! MUST BE A STRING REFERENCE
1910          JMP OKAY               ! FINISH THE PARSE
1920 ! ***********************************************************************
1930          BYT 0,56               ! NO PARAMETERS, STRING FUNCTION
1940 REV.     BIN                    ! FOR ADMD R45,=BINTAB
1950          LDM R43,=40D,0         ! LOAD THE LENGTH OF THE STRING
1960          DEF DATE               !      AND THE ADDRESS OF THE STRING
1970          BYT 0                  !          (MUST BE THREE BYTE ADDRESS)
1980          ADMD R45,=BINTAB       ! MAKE THE ADDRESS ABSOLUTE
1990          PUMD R43,+R12          ! PUSH IT ALL ON THE OPERATING STACK
2000          RTN                    ! DONE
2010          ASC "30.102:veR  2891 .oC drakcaP-ttelweH )c("
2020 DATE     BSZ 0                  ! PLACE HOLDER FOR THE LABEL (ADDRESS)
2030 ! ***********************************************************************
2040          BYT 241                ! BASIC STATEMENT
2050 ALFA.    BIN                    ! FOR MATH
2060          LDBD R37,=CRTSTS       ! CHECK CRT STATUS
2070          JPS INALPHA!           ! JIF ALREADY IN ALPHA MODE
2080          JSB =ALPHA.            ! IF NOT, MAKE IT SO
2090 INALPHA! CMMD R12,=TOS          ! ANYTHING ON THE R12 STACK
2100          JZR NO-ADR             ! JIF JUST 'AWRITE'
2110          JSB =DECUR2            ! KILL BOTH POSSIBLE CURSORS
2120          JSB =HMCURS            ! MOVE THE CURSOR TO THE HOME POSITION
2130          LDMD R14,=BINTAB       ! BECAUSE I'M RELATIVE
2140          CLM R43                ! FAKE 0 STRING LENGTH
2150          LDM R20,R12            ! COPY OF R12
2160          SBM R20,=25,0          ! SUBTRACT 25
2170          CMMD R20,=TOS          ! WHAT'S ON R12
2180          JNZ A-ONLY             ! JIF ONLY X,Y
2190          POMD R43,-R12          ! GET LENGTH AND ADDRESS OF STRING
2200 A-ONLY   STMD R43,X14,SAV-$     ! SAVE LENGTH AND ADDRESS
2210          JSB =TWOB              ! GET TWO BINARY NUMBERS OFF OF R12
2220 CALCADR  DCM R56                ! DECREMENT 'Y'
2230          JNG GOT-IT             ! JIF ADDRESS FIGURED OUT
2240          ADM R46,=120,0         ! ADD TO GET TO NEXT LINE
2250          JMP CALCADR            ! TRY FOR ANOTHER ONE
2260 GOT-IT   STM R46,R24            ! COPY ADDRESS DISPLACEMENT TO 26
2270          JSB =MOVCRS            ! MOVE THE CURSOR
2280          LDMD R43,X14,SAV-$     ! GET LENGTH AND ADDRESS OF STRING BACK
2290          LDM R56,R43            ! GET LENGTH
2300          JZR NO-ADR             ! JIF NO LENGTH
2310          STMD R45,=PTR2         ! SET MEMORY POINTER TO STRING ADDRESS
2320          LDM R36,R43            ! GET LENGTH
2330 ALOP     LDBI R32,=PTR2-        ! GET A CHARACTER
2340          JSB =CHKSTS            ! WAIT FOR CRT NOT BUSY
2350          STBD R32,=CRTDAT       ! STORE IT
2360          DCM R36                ! ANY CHARACTERS LEFT
2370          JNZ ALOP               ! JIF THERE ARE
2380 NO-ADR   RTN                    ! ALL DONE
2390 ! ***********************************************************************
2400          BYT 241                ! BASIC STATMENT
2410 AREAD.   BIN                    ! FOR MATH
2420          LDBD R37,=CRTSTS       ! GET CRT STATUS
2430          JPS INALPHA#           ! JIF ALREADY IN ALPHA MODE
2440          JSB =ALPHA.            ! IF NOT, MAKE IT SO
2450 INALPHA# JSB =DECUR2            ! KILL THE CURSORS
2460          POMD R73,-R12          ! GET STRING STUFF
2470          STM R73,R55            ! COPY TO 55
2480          PUMD R73,+R12          ! PUSH THE STUFF BACK
2490          CLB R57                ! CLEAR MSB
2500          JSB =RESMEM            ! LET'S GO RESEARVE SOME MEMORY
2510          STM R55,R73            ! COPY 55 TO 75
2520          STM R65,R75            ! COPY SINK ADDRESS
2530          STMD R65,=PTR2         ! SET MEMORY POINTER
2540          PUMD R73,+R12          ! PUSH STRING STUFF ONTO R12
2550          TSM R55                ! HOW BIG CAN I GO
2560          JZR DO-STO             ! JIF 0
2570          LDMD R34,=CRTBYT       ! GET CURRENT POSITION
2580          PUMD R34,+R6           ! SAVE IT
2590          JSB =BYTCR!            ! SET CURRENT POSITION
2600 ALOOP    JSB =INCHR             ! GO GET A CHARACTER
2610          STBI R32,=PTR2-        ! STORE IT
2620          JSB =RTCUR.            ! MOVE 1 BYTE
2630          DCM R55                ! ANY MORE
2640          JNZ ALOOP              ! JIF THERE ARE
2650          POMD R34,-R6           ! GET OLD CRTBYT BACK
2660          JSB =BYTCR!            ! SET CURRENT POSITION
2670 DO-STO   JSB =STOST             ! SAVE IT AWAY
2680          RTN                    ! ALL DONE
2690 ! ***********************************************************************
2700 ! *    START CRT AT THE SPECIFIED NUMBER                                *
2710 ! ***********************************************************************
2720          BYT 241
2730 STARTAT. JSB =ONEB              ! GET A NUMBER OFF OF R12
2740          BCD                    ! FOR MATH
2750          LLM R#                 ! *16
2760          BIN                    ! FOR THE REST
2770          STM R#,R#              ! COPY IT
2780          LLM R#                 ! *32
2790          LLM R#                 ! *64
2800          ADM R#,R#              ! *80
2810          STM R#,R#              ! COPY TO 46
2820          LDMD R#,=ASIZE         ! GET ALPHA SIZE INTO 76
2830          DRP R46                ! GET READY FOR 'MOD'
2840          JSB =MOD               ! MOD IT
2850          STM R#,R34             ! COPY RESULT TO 34 FOR 'SAD1'
2860          JSB =SAD1              ! SET CRT START ADDRESS
2870          RTN                    ! ALL DONE
2880 !*********************************************************************
2890 SAV-$    BSZ 5                  ! SAVE AREA FOR ALPHA
2900 !*********************************************************************
2910 NUMVA+   DAD 22403              !
2920 GETCMA   DAD 23477              !
2930 NUMVAL   DAD 22406              !
2940 STREXP   DAD 23724              !
2950 ERROR+   DAD 10220              !
2960 PTR2-    DAD 177715             !
2970 SCAN     DAD 21110              !
2980 STRREF   DAD 24056              !
2990 STREX+   DAD 23721              !
3000 BINTAB   DAD 104070             !
3010 CRTSTS   DAD 177702             !
3020 ONEB     DAD 12153              !
3030 PTR2     DAD 177714             !
3040 CHKSTS   DAD 13204              !
3050 CRTBAD   DAD 177701             !
3060 CRTDAT   DAD 177703             !
3070 ALPHA.   DAD 12413              !
3080 TOS      DAD 101744             ! DEFINE ADDRESSES
3090 DECUR2   DAD 13467              !
3100 HMCURS   DAD 13661              !
3110 TWOB     DAD 56760              !
3120 MOVCRS   DAD 13771              !
3130 RESMEM   DAD 31741              !
3140 CRTBYT   DAD 100206             !
3150 BYTCR!   DAD 14003              !
3160 INCHR    DAD 14262              !
3170 RTCUR.   DAD 13651              !
3180 STOST    DAD 46472              !
3190 ASIZE    DAD 104744             !
3200 SAD1     DAD 13723              !
3210 MOD      DAD 14216              !
3220          FIN                    ! TERMINATE ASSEMBLY
