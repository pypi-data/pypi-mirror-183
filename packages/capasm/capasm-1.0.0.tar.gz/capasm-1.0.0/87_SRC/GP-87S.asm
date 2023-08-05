01000 !  **********************************************************************
01050 !  *                                                                     
01100 !  *       GENERAL PURPOSE BINARY PROGRAM FOR THE HP-87     09/29/81     
01150 !  *                                                                     
01200 !  *             FOR GEMINI SYSTEM RELEASE 8                             
01250 !  *                                                                     
01300 !  **********************************************************************
01350 MYBPGM#  EQU  26               !  BINARY PROGRAM NUMBER
01400          NAM  26,GP-87B        !  NAME BLOCK FOR BINARY
01450          DEF  RUNTIM           !  ADDRESS OF RUNTIME ADDRESSES
01500          DEF  ASCIIS           !  ADDRESS OF ASCII TABLE
01550          DEF  PARSE            !  ADDRESS OF PARSE ADDRESSES
01600          DEF  ERMSG            !  ADDRESS OF ERROR MESSAGES
01650          DEF  INIT             !  ADDRESS OF INITIALIZATION ROUTINE
01700 RUNTIM   BSZ  2                !  PLACE HOLDER
01750          DEF  FLABL.           !  RUNTIME LABEL FOR 'FAST LABEL'
01800          DEF  ALFA.            !  RUNTIME LABEL FOR 'ALPHA'
01850          DEF  AREAD.           !  RUNTIME FOR 'AREAD'
01900          DEF  TAKE.            !  RUNTIME FOR 'TAKE KEYBOARD'
01950          DEF  RELEAS.          !  RUNTIME FOR 'RELEASE KEYBOARD'
02000          BSZ  2                !  RUNTIME FOR 'SGCLEAR'
02050          DEF  LINPUT.          !  RUNTIME FOR 'LINPUT'
02100          DEF  STARTAT.         !  CRT TOP LINE
02150          DEF  REV.             !  RUNTIME FOR REVISION
02200          DEF  KEY$.            !  RUNTIME FOR 'KEY$'
02250          DEF  HGL?$.           !  RUNTIME FOR 'HGL?$'
02300          DEF  MSUS$.           !  RUNTIME FOR 'MSUS$'
02350          BSZ  2                !  RUNTIME FOR 'TRIM$'
02400          DEF  LIN$.            !  RUNTIME FOR HIDDEN TOKEN
02450 PARSE    BSZ  2                !  PLACE HOLDER
02500          DEF  FLABLP           !  PARSE LABEL FOR FAST LABEL
02550          DEF  ALPHAP           !  PARSE LABEL FOR 'ALPHA'
02600          DEF  AREADP           !  PARSE LABEL FOR 'AREAD'
02650          DEF  COMPARS          !  PARSE ROUTINE FOR 'TAKE KEYBOARD'
02700          DEF  COMPARS          !  PARSE ROUTINE FOR 'RELEASE KEYBOARD'
02750          BSZ  2                !  PARSE FOR SGCLEAR
02800          DEF  LINPUTP          !  PARSE LABEL FOR 'LINPUT'
02850          DEF  STARTATP         !  PARSE FOR TOP LINE
02900          BYT  377,377          !  END OF RELOCATABLES
02950 !  **********************************************************************
03000 ASCIIS   ASP  "FAST LABEL"     !  TOKEN 1
03050          ASP  "AWRITE"         !  TOKEN 2
03100          ASP  "AREAD"          !  TOKEN 3
03150          ASP  "TAKE KEYBOARD"  !  TOKEN 4
03200          ASP  "RELEASE KEYBOARD" !  TOKEN 5
03250          ASP  "SGCLEAR"        !  TOKEN 6
03300          ASP  "LINPUT"         !  TOKEN 7
03350          ASP  "START CRT AT"   !  TOKEN 10
03400          ASP  "REV"            !  TOKEN 11
03450          ASP  "KEY$"           !  TOKEN 12
03500          ASP  "HGL?$"          !  TOKEN 13
03550          ASP  "MSUS$"          !  TOKEN 14
03600          ASP  "TRIM$"          !  TOKEN 15
03650 ERMSG    BYT  377              !  END OF ASCII TABLE
03700          BYT  240              !  HIDDEN TOKEN 16
03750 !  **********************************************************************
03800 INIT     BIN                   !  FOR COMPARES & MATH
03850          LDMD R34,=ROMFL       !  WHY AM I HERE
03900          CMB  R34,=1           !  SCRATCH?
03950          JNZ  INITRTN          !  RETURN IF NOT
04000          LDMD R34,=BINTAB      !  LOAD UP BINTAB FOR RELATIVE ADDRESING
04050          JSB  X34,RELEAS.      !  RELEASE THE KEYBOARD
04100 INITRTN  RTN                   !  ALL DONE
04150 !  **********************************************************************
04200 FLABLP   PUBD R43,+R6          !  SAVE THE TOKEN NUMBER
04250          JSB  =NUMVA+          !  CHEW UP A NUMBER
04300          JEZ  ERR89            !  JIF THERE WASN'T ONE
04350          JSB  =GETCMA          !  DEMAND A COMMA
04400          JSB  =NUMVAL          !  GET ANOTHER NUMBER
04450          JEZ  ERR89            !  ERROR OUT IF THERE ISN'T ONE
04500          JSB  =GETCMA          !  DEMAND A COMMA
04550          JSB  =STREXP          !  CHEW UP A STRING EXPRESSION
04600          JEZ  ERR89            !  ERROR OUT IF IT'S MISSING
04650          JSB  =GETCMA          !  DEMAND A COMMA
04700          JSB  =NUMVAL          !  CHEW UP THE LAST NUMBER
04750          JEN  OKAY             !  JUMP AROUND ERROR IF OKAY
04800 ERR89    POBD R43,-R6          !  CLEAN UP THE R6 STACK
04850          JSB  =ERROR+          !  CALL ERROR HANDLING ROUTINE
04900          BYT  89D              !  ERROR 89 - INVALID PARAMETER
04950 !  **********************************************************************
05000 LINPUTP  LDM  R65,=7,26,371    !  JUST THE 'INPUT.' STUFF
05050          STMI R65,=PTR2-       !  SHOVE IT OUT
05100          JSB  =SCAN            !  GET READY FOR 'STRREF'
05150          JSB  =STRREF          !  FIND A STRING REFERENCE
05200          JEZ  ERR89            !  JIF NOT TO ERROR 89
05250          LDM  R65,=16,26,371   !  HIDDEN TOKEN
05300          STMI R65,=PTR2-       !  SHOVE IT OUT
05350          RTN                   !  DONE
05400 !  **********************************************************************
05450 STARTATP PUBD R43,+R6          !  SAVE TOKEN#
05500          JSB  =NUMVA+          !  TRY TO GET A NUMBER
05550          JEZ  ERR88            !  GOT AN ERROR
05600 !  **********************************************************************
05650 OKAY     LDB  R53,=371         !  BPGM TOKEN
05700          STBI R53,=PTR2-       !  STUFF IT OUT
05750          LDB  R53,=MYBPGM#     !  GET MY BINARY NUMBER
05800          STBI R53,=PTR2-       !  STUFF IT OUT
05850          POBD R53,-R6          !  GET THE TOKEN NUMBER
05900          STBI R53,=PTR2-       !  STUFF IT OUT
05950          RTN                   !  ALL DONE
06000 !  **********************************************************************
06050 ALPHAP   PUBD R43,+R6          !  SAVE TOKEN NUMBER
06100          JSB  =NUMVA+          !  TRY TO GET A NUMBER
06150          JEZ  OKAY             !  MUST BE JUST 'ALPHA'
06200          JSB  =GETCMA          !  DEMAND A COMMA
06250          JSB  =NUMVAL          !  DEMAND A NUMBER
06300          JEN  OKAY2            !  JIF BOTH NUMBERS THERE
06350 ERR88    POBD R43,-R6          !  CLEAN UP R6
06400          JSB  =ERROR+          !  ERROR HANDLING ROUTINE
06450          BYT  88D              !  ERROR NUMBER
06500 OKAY2    CMB  R14,=54          !  MAKE SURE OF A COMMA
06550          JNZ  OKAY             !  JIF JUST 'ALPHA X,Y'
06600          JSB  =STREX+          !  CHEW UP A STRING EXPRESSION
06650          JEZ  ERR88            !  JIF NO STRING TO ERROR
06700          JMP  OKAY             !  OTHERWISE FINISH UP THE PARSING
06750 !  **********************************************************************
06800 AREADP   PUBD R43,+R6          !  SAVE THE TOKEN
06850          JSB  =SCAN            !  LET'S DO A SCAN
06900          JSB  =STRREF          !  MUST A STRING REFERENCE
06950          JMP  OKAY             !  FINISH THE PARSE
07000 !  **********************************************************************
07050 COMPARS  PUBD R43,+R6          !  SAVE TOKEN#
07100          JSB  =SCAN            !  DO A SCAN FOR SYSTEM
07150          JMP  OKAY             !  ALL DONE
07200 !  **********************************************************************
07250          BYT  0,56             !  NO PARAMETERS, STRING FUNCTION
07300 REV.     BIN                   !  FOR ADMD R45,=BINTAB
07350          LDM  R43,=40D,0       !  LOAD THE LENGTH OF THE STRING
07400          DEF  DATE             !       AND THE ADDRESS OF THE STRING
07450          BYT  0                !           (MUST BE THREE BYTE ADDRESS)
07500          ADMD R45,=BINTAB      !  MAKE THE ADDRESS ABSOLUTE
07550          PUMD R43,+R12         !  PUSH IT ALL ON THE OPERATING STACK
07600          RTN                   !  DONE
07650          ASC  "03.901:veR  2891 .oC drakcaP-ttelweH )c("
07700 DATE     BSZ  0                !  PLACE HOLDER FOR THE LABEL (ADDRESS)
07750 KEYTAB   BYT  200              !  K1
07800          BYT  201              !  K2
07850          BYT  202              !  K3
07900          BYT  203              !  K4
07950          BYT  241              !  K5
08000          BYT  242              !  K6
08050          BYT  234              !  K7
08100          BYT  204              !  K8
08150          BYT  205              !  K9
08200          BYT  206              !  K10
08250          BYT  207              !  K11
08300          BYT  245              !  K12
08350          BYT  254              !  K13
08400          BYT  223              !  K14
08450          BYT  213              !  RESET
08500          BYT  377              !  END OF INVALID KEY TABLE
08550 !  **********************************************************************
08600          BYT  241              !  BASIC STATEMENT
08650 FLABL.   BIN                   !  FOR MATH, COMPARES, etc.
08700          LDBD R37,=CRTSTS      !  CHECK CRTSTS
08750          JNG  INGRAF           !  JIF ALREADY IN A GRAPH MODE
08800          JSB  =GRAPH.          !  FORCE TO GRAPHICS IF NOT
08850 INGRAF   LDM  R34,=62,0        !  WIDTH OF NORMAL GRAPHICS (BYTES)
08900          ANM  R37,=100         !  MASK OUT CRTSTS FOR GRAPH ALL
08950          JZR  GOTSIZ           !  JIF GRAPH NORMAL
09000          LDM  R34,=104,0       !  WIDTH OF CRT IF IN ALL (BYTES)
09050 GOTSIZ   LDMD R14,=BINTAB      !  BECAUSE THIS BINARY PROG. IS RELATIVE
09100          PUMD R34,+R6          !  SAVE WIDTH ON R6
09150          JSB  =ONEB            !  GET THE INVERSE VIDEO FLAG
09200          STBD R#,X14,INVRS?    !  SAVE IT
09250          POMD R45,-R12         !  GET THE LABEL ADDRESS OFF OF R12
09300          STMD R45,X14,LABADR   !  SAVE IT
09350          POMD R20,-R12         !  GET THE LABEL LENGTH OFF OF R12
09400          STMD R20,X14,LABLEN   !  SAVE IT
09450          JSB  =ONEB            !  GET THE Y-POSITION
09500          STM  R#,R0            !  SAVE IT IN R0,R1
09550          JSB  =ONEB            !  GET THE X-POSITION
09600          POMD R34,-R6          !  RETRIEVE CRT WIDTH FROM R6
09650          ADM  R46,=340,20      !  ADD GRAPHICS BASE TO X-POSITION
09700 CALCAD   DCM  R0               !  DECREMENT Y-POSITION
09750          JNG  GOTADR           !  JIF NEGATIVE TO GOT ADDRESS
09800          ADM  R46,R34          !  ADD CRT WIDTH FOR EACH Y-POSITION
09850          JMP  CALCAD           !  LOOP
09900 GOTADR   LDBD R20,X14,INVRS?   !  LOAD UP INVERSE VIDEO FLAG
09950          BCD                   !  FOR SAVING FLAG IN 'E'
10000          ERB  R20              !  GET IT INTO 'E'
10050          BIN                   !  BACK TO BINARY MODE
10100          LDMD R20,X14,LABLEN   !  LOAD UP LABEL LENGTH
10150          JZR  ANYRTN           !  JIF NULL STRING
10200          LDMD R75,X14,LABADR   !  LOAD UP LABEL ADDRESS
10250          STMD R75,=PTR2        !  SET MEMORY POINTER TO LABEL
10300 LENLOP   LDBI R24,=PTR2-       !  GET A CHARACTER
10350          ANM  R24,=177,0       !  FORCE CHARACTER TO 0 THRU 177
10400          LLM  R24              !  MULTIPLY IT BY 2
10450          LLM  R24              !  BY 4
10500          LLM  R24              !  BY 8
10550          ADM  R24,=CHRTAB      !  ADD DISPLACEMENT TO DATA TABLE
10600          ADM  R24,R14          !  MAKE IT ABSOLUTE
10650          LDB  R26,=11          !  NUMBER OF BYTES TO WRITE OUT
10700          STM  R46,R56          !  SAVE CRT ADDRESS IN 56
10750          CLB  R27              !  CLEAR FIRST BYTE
10800 OUTLOP   JSB  =CHKSTS          !  WAIT FOR CRT NOT BUSY
10850          STMD R56,=CRTBAD      !  SET CRT ADDRESS
10900          ADM  R56,R34          !  INCREMENT IT TO NEXT LINE
10950          JEZ  NOTINV           !  JIF IF NOT INVERSE VIDEO
11000          NCB  R27              !  COMPLEMENT THE BYTE FOR INVERSE
11050 NOTINV   STBD R27,=CRTDAT      !  STORE THE BYTE TO THE CRT
11100          POBD R27,+R24         !  GET NEXT BYTE
11150          DCB  R26              !  DECREMENT BYTE COUNTER
11200          JNZ  OUTLOP           !  JIF MORE BYTES FOR THIS CHARACTER
11250          ICM  R46              !  INCREMENT CRT POSITION FOR NEXT CHAR.
11300          DCM  R20              !  DECREMENT LABEL LENGTH
11350          JNZ  LENLOP           !  JIF THERE ARE MORE CHARACTERS
11400 ANYRTN   RTN                   !  ALL DONE
11450 !  **********************************************************************
11500          BYT  241              !  BASIC STATEMENT
11550 ALFA.    BIN                   !  FOR MATH
11600          LDBD R37,=CRTSTS      !  CHECK CRT STATUS
11650          JPS  INALPHA!         !  JIF ALREADY IN ALPHA MODE
11700          JSB  =ALPHA.          !  IF NOT, MAKE IT SO
11750 INALPHA! CMMD R12,=TOS         !  ANYTHING ON THE R12 STACK
11800          JZR  NO-ADR           !  JIF JUST 'ALPHA'
11850          JSB  =DECUR2          !  KILL BOTH POSSIBLE CURSORS
11900          JSB  =HMCURS          !  KILL BOTH POSSIBLE CURSORS
11950          LDMD R14,=BINTAB      !  BECAUSE I'M RELATIVE
12000          CLM  R43              !  FAKE 0 STRING LENGTH
12050          LDM  R20,R12          !  COPY OF R12
12100          SBM  R20,=25,0        !  SUBTRACT 25
12150          CMMD R20,=TOS         !  WHAT'S ON R12
12200          JNZ  A-ONLY           !  JIF ONLY X,Y
12250          POMD R43,-R12         !  GET LENGTH AND ADDRESS OF STRING
12300 A-ONLY   STMD R43,X14,SAV-$    !  SAVE LENGTH AND ADDRESS
12350          JSB  =TWOB            !  GET TWO BINARY NUMBERS OFF OF R12
12400 CALCADR  DCM  R56              !  DECREMENT 'Y'
12450          JNG  GOT-IT           !  JIF ADDRESS FIGURED OUT
12500          ADM  R46,=120,0       !  ADD TO GET TO NEXT LINE
12550          JMP  CALCADR          !  TRY FOR ANOTHER ONE
12600 GOT-IT   STM  R46,R24          !  COPY ADDRESS DISPLACEMENT TO 26
12650          JSB  =MOVCRS          !  MOVE THE CURSOR
12700          LDMD R43,X14,SAV-$    !  GET LENGTH AND ADDRESS OF STRING BACK
12750          LDM  R56,R43          !  GET LENGTH
12800          JZR  NO-ADR           !  JIF NO LENGTH
12850          STMD R45,=PTR2        !  SET MEMORY POINTER TO STRING ADDRESS
12900          LDM  R36,R43          !  GET LENGTH
12950 ALOP     LDBI R32,=PTR2-       !  GET A CHARACTER
13000          JSB  =CHKSTS          !  WAIT FOR CRT NOT BUSY
13050          STBD R32,=CRTDAT      !  STUFF IT OUT
13100          DCM  R36              !  ANY CHARACTERS LEFT
13150          JNZ  ALOP             !  JIF THERE ARE
13200 NO-ADR   RTN                   !  ALL DONE
13250 !  **********************************************************************
13300          BYT  241              !  BASIC STATMENT
13350 AREAD.   BIN                   !  FOR MATH
13400          LDBD R37,=CRTSTS      !  GET CRT STATUS
13450          JPS  INALPHA#         !  JIF ALREADY IN ALPHA MODE
13500          JSB  =ALPHA.          !  IF NOT, MAKE IT SO
13550 INALPHA# JSB  =DECUR2          !  KILL THE CURSORS
13600          POMD R73,-R12         !  GET STRING STUFF
13650          STM  R73,R55          !  COPY TO 55
13700          PUMD R73,+R12         !  PUSH THE STUFF BACK
13750          CLB  R57              !  CLEAR MSB
13800          JSB  =RESMEM          !  LET'S GO RESEARVE SOME MEMORY
13850          STM  R55,R73          !  COPY 55 TO 75
13900          STM  R65,R75          !  COPY SINK ADDRESS
13950          STMD R65,=PTR2        !  SET MEMORY POINTER
14000          PUMD R73,+R12         !  PUSH STRING STUFF ONTO R12
14050          TSM  R55              !  HOW BIG CAN I GO
14100          JZR  DO-STO           !  JIF 0
14150          LDMD R34,=CRTBYT      !  GET CURRENT POSITION
14200          PUMD R34,+R6          !  SAVE IT
14250          JSB  =BYTCR!          !  SET CURRENT POSITION
14300 ALOOP    JSB  =INCHR           !  GO GET A CHARACTER
14350          STBI R32,=PTR2-       !  STUFF IT OUT
14400          JSB  =RTCUR.          !  MOVE 1 BYTE
14450          DCM  R55              !  ANY MORE
14500          JNZ  ALOOP            !  JIF THERE ARE
14550          POMD R34,-R6          !  GET OLD CRTBYT BACK
14600          JSB  =BYTCR!          !  SET CURRENT POSITION
14650 DO-STO   JSB  =STOST           !  SAVE IT AWAY
14700          RTN                   !  ALL DONE
14750 !  **********************************************************************
14800          BYT  241
14850 LINPUT.  JSB  =INPUT.          !  DO THE INPUT
14900          RTN  
14950 !  **********************************************************************
15000          BYT  44               !  MISCELLANEOUS IGNORE
15050 LIN$.    BIN                   !  FOR EVERYTHING
15100          LDMD R32,=INPTR       !  GET THE INPUT POINTER
15150          STM  R32,R14          !  KEEP A COPY FOR LATER
15200          CLM  R36              !  INITIALIZE LENGTH TO 0
15250 CHRCNT   POBD R35,+R32         !  GET A CHAR.
15300          CMB  R35,=15          !  CHECK FOR CR
15350          JZR  ENDOF$           !  JIF SO
15400          ICM  R36              !  INCREMENT LENGTH IF NOT
15450          JMP  CHRCNT           !  AND LOOP
15500 ENDOF$   TSM  R36              !  TEST LENGTH FOR 0
15550          JZR  DONE             !  JIF SO
15600          POBD R25,-R32         !  BACK UP ONE
15650 POPBLK   POBD R25,-R32         !  BACK UP ONE MORE AND....
15700          CMB  R25,=40          !      CHECK FOR A BLANK
15750          JNZ  DONE+            !  IF IT'S NOT A BLANK, QUIT.
15800          DCM  R36              !  ELSE DECREMENT LENGTH
15850          JNZ  POPBLK           !  AND LOOP IF ANY LEFT
15900 DONE+    ICM  R32              !  INCREMENT STRING ADDRESS TO LWA+1
15950          STM  R32,R65          !  COPY TO 65 FOR 3-BYTE ADDRESS
16000          CLB  R67              !  CLEAR MSB
16050 DOLOOP   CMM  R14,R32          !  CHECK TO SEE IF DONE FLIPPING
16100          JCY  DONE             !  JIF SO
16150          LDBD R30,R14          !  GET A CHAR FROM THE FRONT
16200          POBD R31,-R32         !  GET A CHAR FROM THE BACK
16250          STBD R30,R32          !  PUT THE FRONT IN THE BACK
16300          PUBD R31,+R14         !  PUT THE BACK IN THE FRONT
16350          JMP  DOLOOP           !  & LOOP
16400 DONE     PUMD R36,+R12         !  PUSH LENGTH ONTO R12
16450          PUMD R65,+R12         !  PUSH THE ADDRESS ONTO R12
16500          JSB  =STOST           !  STORE THE STRING
16550          RTN                   !  ALL DONE
16600 !  **********************************************************************
16650          BYT  241
16700 TAKE.    LDMD R46,=BINTAB      !  FOR RELATIVE ADDRESSING
16750          LDM  R30,=KEYBUF      !  GET ADDRESS OF KEYBOARD BUFFER
16800          ADM  R30,R46          !  MAKE IT ABSOLUTE
16850          STMD R30,X46,KEYPTR   !  INITIALIZE KEY POINTER
16900          ADM  R30,=80D,0       !  POINT TO END OF BUFFER
16950          STMD R30,X46,KEYEND   !  INITIALIZE KEYEND
17000          LDM  R30,=USEKEY      !  ADDRESS OF KEYBOARD SERVICE ROUTINE
17050          ADM  R30,R46          !  MAKE IT ABSOLUTE
17100          STM  R30,R43          !  COPY TO 43&44
17150          LDB  R45,=236         !  45='RTN'
17200          LDB  R42,=316         !  42='JSB'
17250 TAKEIT   STMD R42,=KYIDLE      !  STORE OUT RTN'S OR JSB=SERVICE RTN
17300          LDB  R42,=377         !  INVALID REPEAT FLAG
17350          STBD R42,X46,LASTKEY  !  SET IT
17400          RTN  
17450 !  **********************************************************************
17500          BYT  241
17550 RELEAS.  LDM  R42,=236,236,236,236,236,236 !  LOTS OF RTNS
17600          JMP  TAKEIT           ! 
17650 !  **********************************************************************
17700 USEKEY   STBD R#,=GINTDS       !  DISABLE GLOBAL INTERRUPTS
17750          BIN                   !  FOR EVERYTHING
17800          PUMD R2,+R6           !  SAVE 2&3
17850          PUMD R40,+R6          !  SAVE THE 40'S
17900          LDM  R40,R20          !  AND THE 20'S
17950          LDMD R26,=MYBTAB      !  FOR RELATIVE ANYTHING
18000          LDMD R20,X26,KEYPTR   !  GET THE KEY POINTER
18050          LDMD R22,X26,KEYEND   !  ADDRESS OF END OF BUFFER
18100          CMM  R22,R20          !  BUFFER FULL?
18150          JZR  RE-START         !  JIF IT IS
18200          LDBD R22,=KEYCOD      !  GET THE KEY CODE
18250          LDBD R25,=KEYSTS      !  GET KEYBOARD STATUS
18300          ANM  R25,=10          !  MASK FOR SHIFT KEY
18350          JZR  NOTSHIFT         !  JIF SHIFT KEY NOT DOWN
18400          CMB  R22,=kUPCUR      !  UP CURSOR KEY?
18450          JNZ  ENDLINE?         !  JIF NOT
18500          LDB  R22,=kHOME       !  OTHERWISE MAKE IT THE HOME KEY
18550          JMP  NOTSHIFT         !  FALL THROUGH
18600 ENDLINE? CMB  R22,=kENDLINE    !  WAS IT THE ENDLINE KEY?
18650          JNZ  NOTSHIFT         !  JIF NOT
18700          LDB  R22,=kSENDLIN    !  MAKE IT SHIFT ENDLINE
18750 NOTSHIFT LDM  R24,=KEYTAB      !  ADDRESS OF INVALID KEYS
18800          ADM  R24,R26          !  MAKE IT ABSOLUTE
18850 KEYLOOP  POBD R23,+R24         !  GET AN INVALID KEYCODE
18900          CMB  R23,=377         !  END OF TABLE?
18950          JZR  KEYLOOP1         !  JIF IT IS
19000          CMB  R23,R22          !  IS THIS KEY INVALID
19050          JNZ  KEYLOOP          !  JIF NO MATCH
19100          JSB  X26,FIXUP-R6     !  FIX UP THE R6 STACK
19150          JMP  KEYRTN+          !  FALL THROUGH
19200 KEYLOOP1 PUBD R22,+R20         !  APPEND TO THE BUFFER
19250          STMD R20,X26,KEYPTR   !  UPDATE THE POINTER
19300 RE-START CLB  R20              !  \
19350          ICB  R20              !   > RESTART THE KEYBOARD SCANNER
19400          STBD R20,=KEYCOD      !  /
19450          JSB  X26,FIXUP-R6     !  FIX UP THE R6 STACK
19500          SBM  R6,=4,0          !  TRASH TWO RETURNS
19550 KEYRTN   STBD R#,=GINTEN       !  RE-ENABLE GLOBAL INTERRUPTS
19600 DRP      BSZ  1                !  FORCE THE DRP
19650          PAD                   !  RESTORE  THE STATUS
19700          RTN                   !  ALL DONE
19750 KEYRTN+  STBD R#,=GINTEN       !  RE-ENABLE INTERRUPTS
19800          RTN  
19850 FIXUP-R6 STMI R30,=MYBTAB      !  SAVE 30
19900          POMD R30,-R6          !  GET THE RETURN ADDRESS
19950          LDM  R20,R6           !  COPY OF R6
20000          SBM  R20,=20,0        !  GET DOWN TO MIDDLE OF THE SAD
20050          LDBD R20,R20          !  PLUCK IT OUT
20100          ANM  R20,=77,0        !  MASK OUT THE LAST DRP
20150          ADB  R20,=100         !  MAKE IT INTO A DRP INSTRUCTION
20200          STBD R20,X26,DRP      !  STUFF IT OUT
20250          STM  R40,R20          !  RESTORE  THE 20'S
20300          POMD R40,-R6          !  RESTORE  THE 40'S
20350          POMD R2,-R6           !  RESTORE 2&3
20400          PUMD R30,+R6          !  PUT THE RETURN BACK
20450          LDMI R30,=MYBTAB      !  GET 30 BACK
20500          RTN                   !  ALL DONE
20550 !  **********************************************************************
20600          BYT  0,56
20650 KEY$.    BIN                   !  FOR EVERYTHING
20700          LDMD R14,=BINTAB      !  FOR ANYTHING RELATIVE
20750          LDM  R20,=KEYBUF      !  ADRESS OF KEYBOARD BUFFER
20800          ADM  R20,R14          !  MAKE ADDRESS ABSOLUTE
20850          LDMD R22,X14,KEYPTR   !  GET POINTER INTO BUFFER
20900          CMM  R22,R20          !  BUFFER EMPTY?
20950          JZR  KEY$3            !  JIF IT IS
21000          STBD R#,=GINTDS       !  DISABLE GLOBAL INTERRUPTS
21050          LDM  R30,R20          !  COPY 20
21100          POBD R32,+R20         !  GET A KEY
21150          STBD R32,X14,LASTKEY  !  SAVE LAST KEY FOR POSSIBLE REPEAT
21200 KEY$1    CMM  R22,R20          !  BUFFER COLLAPSED
21250          JZR  KEY$2            !  JIF IT IS
21300          POBD R33,+R20         !  GET A KEY
21350          PUBD R33,+R30         !  MOVE IT DOWN
21400          JMP  KEY$1            !  LOOP
21450 KEY$2    DCM  R22              !  ADJUST KEYPTR
21500          STMD R22,X14,KEYPTR   !  AND RESTORE  IT
21550          STBD R#,=GINTEN       !  RE-ENABLE GLOBAL INTERRUPTS
21600 KEY$2+   CLM  R22              !  \
21650          ICM  R22              !   > LENGTH OF 1
21700 KEY$2++  PUMD R#,+R12          !  /
21750          LDM  R55,=LASTKEY     !  ADDRESS OF KEYHIT
21800          BYT  0                !  ---->  R57
21850          ADMD R55,=BINTAB      !  MAKE ADDRESS ABSOLUTE
21900          ICM  R55              !  POINT TO AFTER THE KEY
21950          PUMD R55,+R12         !  PUSH ADDRESS OUT
22000          RTN                   !  ALL DONE
22050 KEY$3    LDBD R32,X14,LASTKEY  !  CHECK LAST KEY
22100          CMB  R32,=377         !  INVALID REPEAT?
22150          JZR  KEY$4            !  JIF SO
22200          LDBD R32,=KEYSTS      !  GET KEYBOARD STATUS
22250          LRB  R32              !  SHIFT STILL DOWN FLAG
22300          JOD  KEY$2+           !  LET'S REPEAT IT
22350 KEY$4    CLM  R32              !  NO REPEAT, SO 0 LENGTH
22400          JMP  KEY$2++          !  ONE MORE TIME
22450 !  **********************************************************************
22500 !  *     MSUS$ - RETURNS MSUS GIVEN A VOLUME LABEL                       
22550 !  **********************************************************************
22600          BYT  30,56            !  STRING FUNCTION, 1 STRING PARAMETER
22650 MSUS$.   JSB  =ROMJSB          !  BECAUSE IT'S BANK SELECTABLE
22700          DEF  MSIN             !  INITLIALIZE MS ROM
22750          VAL  MSROM#           !  WHICH BANK TO SELECT
22800          BIN                   !  FOR EVERYTHING
22850          LDM  R30,R6           !  COPY OF R6
22900          ADM  R30,=7,0         !  WHERE I WILL WANT TO RETURN TO IF ERROR
22950          STMD R30,=SAVER6      !  WHERE MS ROM RETURNS TO ON ERROR
23000          LDB  R40,=2           !  WHAT TO DECODE
23050          JSB  =ROMJSB          !  BECAUSE IT'S BANK SELECTABLE
23100          DEF  DECODE           !  DECODE VOLUME LABEL
23150          VAL  MSROM#           !  WHICH ROM TO SELECT
23200          TSB  R17              !  ANY ERRORS?
23250          JNG  MSUSRTN          !  JIF SO
23300          LDMD R44,=ACTMSU      !  GET THE ACTIVE MSUS
23350          CLB  R44              !  CLEAR LSB
23400          LDM  R20,=6,0         !  MAX POSSIBLE LENGTH OF MSUS
23450          BIN                   !  FOR MATH
23500          ADB  R45,=3           !  SELECT CODE START AT 3
23550          JNC  <4               !  JIF SELECT IS NOT 10
23600          ICB  R44              !  MAKE IT 10
23650          JMP  GOTIT            !  FINISH UP
23700 <4       DCB  R20              !  LENGTH IS ONLY 5
23750          LDM  R44,R45          !  COPY TO LOWER REGISTER
23800 GOTIT    ADM  R#,=60,60,60,60  !  CONVERT NUMBERS INTO ASCII
23850          LDMD R14,=BINTAB      !  FOR RELATIVE ADDRESSING
23900          LDM  R22,=STUFF-      !  ADDRESS OF WHERE IT GOES
23950          ADM  R22,R14          !  MAKE IT ABSOLUTE
24000          PUBD R47,+R22         !  PUSH OUT THE 4 BYTES IT REVERSE ORDER
24050          PUBD R46,+R22         !    "   "   "  "   "    "    "      "
24100          PUBD R45,+R22         !    "   "   "  "   "    "    "      "
24150          PUBD R44,+R22         !    "   "   "  "   "    "    "      "
24200          PUMD R20,+R12         !  PUSH OUT THE LENGTH
24250          LDM  R45,=STUFF       !  ADDRESS OF WHERE IT WILL COME FROM
24300          BYT  0                !  FOR 3-BYTE ADDRESSING
24350          ADMD R45,=BINTAB      !  MAKE IT AN ABSOLUTE ADDRESS
24400          PUMD R45,+R12         !  PUSH ADDRESS OF STING ONTO R12
24450 MSUSRTN  RTN                   !  ALL DONE
24500 !  **********************************************************************
24550 !  *    HGL?$(A$,X) - RETURN STRING UNDERLINED IF X#0                    
24600 !  **********************************************************************
24650          BYT  50,56            !  STRING FUNCTION, 1 STRING & 1 NUMERIC
24700 HGL?$.   JSB  =ONEB            !  GET HIGHLITE FLAG
24750          JZR  HGL?$1           !  JIF NOT TO BE HIGHLIGHTED
24800          LDB  R34,=200         !  INVERSE VIDEO MASK
24850          JMP  HGL?$2           !  JUMP TO COMMON
24900 HGL?$1   CLB  R34              !  LET'S NOT HIGHLITE IT
24950 HGL?$2   POMD R45,-R12         !  ADDRESS OF SOURCE STRING
25000          POMD R30,-R12         !  LENGTH OF SOURCE STRING
25050          PUMD R30,+R12         !  PUT IT BACK
25100          STM  R30,R55          !  COPY LENGTH
25150          CLB  R57              !  FOR 3-BYTE STUFF
25200          JSB  =RESMEM          !  GO RESEARVE SOME TEMP. MEMORY
25250          JEN  HGL?$RTN         !  JIF MEM OVF
25300          PUMD R65,+R12         !  PUSH ADDRESS ONTO R12
25350          STMD R65,=PTR2        !  SET EMC SINK POINTER
25400          LDMD R55,=PTR1        !  GOT TO SAVE THIS ONE
25450          STMD R45,=PTR1        !  SET EMC SOURCE POINTER
25500 HGL?$3   DCM  R30              !  ANY MORE CHARS?
25550          JNG  HGL?$4           !  JIF NOT
25600          LDBI R20,=PTR1-       !  GET A CHAR
25650          ORB  R20,R34          !  OR IN INVERSE MASK
25700          STBI R20,=PTR2-       !  SHOVE IT OUT
25750          JMP  HGL?$3           !  LOOP
25800 HGL?$4   STMD R55,=PTR1        !  RESTORE THIS ONE
25850 HGL?$RTN RTN                   !  ALL DONE
25900 !  **********************************************************************
25950 !  *    START CRT AT THE SPECIFIED NUMBER                                
26000 !  **********************************************************************
26050          BYT  241
26100 STARTAT. JSB  =ONEB            !  GET A NUMBER OF OF R12
26150          BCD                   !  FOR MATH
26200          LLM  R#               !  *16
26250          BIN                   !  FOR THE REST
26300          STM  R#,R#            !  COPY IT
26350          LLM  R#               !  *32
26400          LLM  R#               !  *64
26450          ADM  R#,R#            !  *80
26500          STM  R#,R#            !  COPY TO 46
26550          LDMD R#,=ASIZE        !  GET ALPHA SIZE INTO 76
26600          DRP  R46              !  GET READY FOR 'MOD'
26650          JSB  =MOD             !  MOD IT
26700          STM  R#,R34           !  COPY RESULT TO 34 FOR 'SAD1'
26750          JSB  =SAD1            !  SET CRT START ADDRESS
26800          RTN                   !  ALL DONE
26850 !  **********************************************************************
26900 !  *              CHARACTER DATA FOR FAST LABEL                          
26950 !  **********************************************************************
27000 CHRTAB   BYT  4,14,34,74,34,14,4,0
27050          BYT  10,0,10,20,42,42,34,0
27100          BYT  174,0,104,50,20,50,104,0
27150          BYT  174,0,104,144,124,114,104,0
27200          BYT  0,0,64,110,110,110,64,0
27250          BYT  70,104,104,170,104,104,170,0
27300          BYT  174,104,40,20,40,104,174,0
27350          BYT  0,0,20,50,50,104,174,0
27400          BYT  0,20,40,174,40,20,0,0
27450          BYT  0,0,74,110,110,110,60,0
27500 $10      BYT  20,70,124,20,20,20,20,0
27550          BYT  100,40,20,50,104,104,104,0
27600          BYT  0,0,44,44,44,70,100,0
27650          BYT  0,0,0,0,0,0,0,0
27700          BYT  0,4,70,120,20,20,20,0
27750          BYT  0,4,70,150,50,50,50,0
27800          BYT  70,104,104,174,104,104,70,0
27850          BYT  74,120,120,170,120,120,174,0
27900          BYT  0,0,50,124,134,120,74,0
27950          BYT  20,70,104,104,174,104,104,0
28000 $20      BYT  20,0,70,110,110,110,64,0
28050          BYT  50,70,104,104,174,104,104,0
28100          BYT  50,0,70,110,110,110,64,0
28150          BYT  50,70,104,104,104,104,70,0
28200          BYT  50,0,70,104,104,104,70,0
28250          BYT  50,104,104,104,104,104,70,0
28300          BYT  50,0,104,104,104,104,70,0
28350          BYT  100,100,100,174,100,100,100,0
28400          BYT  30,30,30,30,30,30,30,30
28450          BYT  0,0,0,377,377,0,0,0
28500 $30      BYT  30,44,40,160,40,40,174,0
28550          BYT  30,30,30,377,377,30,30,30
28600          BYT  0,0,0,0,0,0,0,0
28650          BYT  10,10,10,10,10,0,10,0
28700          BYT  50,50,50,0,0,0,0,0
28750          BYT  50,50,174,50,174,50,50,0
28800          BYT  20,74,120,70,24,170,20,0
28850          BYT  140,144,10,20,40,114,14,0
28900          BYT  40,120,120,40,124,110,64,0
28950          BYT  10,10,10,0,0,0,0,0
29000 $40      BYT  20,40,100,100,100,40,20,0
29050          BYT  20,10,4,4,4,10,20,0
29100          BYT  20,124,70,20,70,124,20,0
29150          BYT  0,20,20,174,20,20,0,0
29200          BYT  0,0,0,0,10,10,20,0
29250          BYT  0,0,0,174,0,0,0,0
29300          BYT  0,0,0,0,0,10,0,0
29350          BYT  0,4,10,20,40,100,0,0
29400          BYT  70,104,114,124,144,104,70,0
29450          BYT  20,60,20,20,20,20,70,0
29500 $50      BYT  70,104,4,30,40,100,174,0
29550          BYT  174,4,10,30,4,104,70,0
29600          BYT  10,30,50,110,174,10,10,0
29650          BYT  174,100,170,4,4,104,70,0
29700          BYT  34,40,100,170,104,104,70,0
29750          BYT  174,4,10,20,40,40,40,0
29800          BYT  70,104,104,70,104,104,70,0
29850          BYT  70,104,104,74,4,10,160,0
29900          BYT  0,0,20,0,20,0,0,0
29950          BYT  0,0,20,0,20,20,40,0
30000 $60      BYT  4,10,20,40,20,10,4,0
30050          BYT  0,0,174,0,174,0,0,0
30100          BYT  100,40,20,10,20,40,100,0
30150          BYT  70,104,104,10,20,0,20,0
30200          BYT  70,104,124,130,130,100,74,0
30250          BYT  70,104,104,174,104,104,104,0
30300          BYT  170,104,104,170,104,104,170,0
30350          BYT  70,104,100,100,100,104,70,0
30400          BYT  170,104,104,104,104,104,170,0
30450          BYT  174,100,100,170,100,100,174,0
30500 $70      BYT  174,100,100,170,100,100,100,0
30550          BYT  74,100,100,100,114,104,74,0
30600          BYT  104,104,104,174,104,104,104,0
30650          BYT  70,20,20,20,20,20,70,0
30700          BYT  4,4,4,4,4,104,70,0
30750          BYT  104,110,120,140,120,110,104,0
30800          BYT  100,100,100,100,100,100,174,0
30850          BYT  104,154,124,124,104,104,104,0
30900          BYT  104,104,144,124,114,104,104,0
30950          BYT  70,104,104,104,104,104,70,0
31000 $80      BYT  170,104,104,170,100,100,100,0
31050          BYT  70,104,104,104,124,110,64,0
31100          BYT  170,104,104,170,120,110,104,0
31150          BYT  70,104,100,70,4,104,70,0
31200          BYT  174,20,20,20,20,20,20,0
31250          BYT  104,104,104,104,104,104,70,0
31300          BYT  104,104,104,104,50,50,20,0
31350          BYT  104,104,104,124,124,154,104,0
31400          BYT  104,104,50,20,50,104,104,0
31450          BYT  104,104,50,20,20,20,20,0
31500 $90      BYT  174,4,10,20,40,100,174,0
31550          BYT  174,140,140,140,140,140,174,0
31600          BYT  0,100,40,20,10,4,0,0
31650          BYT  174,14,14,14,14,14,174,0
31700          BYT  20,50,104,0,0,0,0,0
31750          BYT  0,0,0,0,0,0,174,0
31800          BYT  100,40,20,10,0,0,0,0
31850          BYT  0,0,70,4,74,104,74,0
31900          BYT  100,100,130,144,104,104,170,0
31950          BYT  0,0,0,74,100,100,74,0
32000 $100     BYT  4,4,64,114,104,104,74,0
32050          BYT  0,0,70,104,174,100,70,0
32100          BYT  10,20,20,70,20,20,20,0
32150          BYT  0,0,74,104,74,4,30,0
32200          BYT  100,100,130,144,104,104,104,0
32250          BYT  0,10,0,30,10,10,34,0
32300          BYT  0,4,0,4,4,44,30,0
32350          BYT  40,40,44,50,60,50,44,0
32400          BYT  30,10,10,10,10,10,34,0
32450          BYT  0,0,150,124,124,124,124,0
32500 $110     BYT  0,0,130,144,104,104,104,0
32550          BYT  0,0,70,104,104,104,70,0
32600          BYT  0,0,170,104,170,100,100,0
32650          BYT  0,0,70,110,70,10,4,0
32700          BYT  0,0,54,60,40,40,40,0
32750          BYT  0,0,74,100,70,4,170,0
32800          BYT  0,20,70,20,20,20,10,0
32850          BYT  0,0,104,104,104,110,64,0
32900          BYT  0,0,104,104,50,50,20,0
32950          BYT  0,0,104,104,124,124,50,0
33000 $120     BYT  0,0,104,50,20,50,104,0
33050          BYT  0,0,104,50,20,40,100,0
33100          BYT  0,0,174,10,20,40,174,0
33150          BYT  20,40,40,100,40,40,20,0
33200          BYT  20,20,20,0,20,20,20,0
33250          BYT  20,10,10,4,10,10,20,0
33300          BYT  0,0,40,124,10,0,0,0
33350          BYT  124,50,124,50,124,50,124,0 ! 
33400 !  **********************************************************************
33450 LASTKEY  BSZ  1
33500 INVRS?   BSZ  1                !  INVERSE VIDEO FLAG (FAST LABEL)
33550 SAV-$    BSZ  0                !  SAVE AREA FOR ALPHA
33600 LABLEN   BSZ  2                !  LABEL LENGTH (FAST LABEL)
33650 LABADR   BSZ  3                !  LABEL ADDRESS (FAST LABEL)
33700 KEYBUF   BSZ  80D
33750 KEYPTR   BSZ  2
33800 KEYEND   BSZ  2
33850 STUFF-   BSZ  4
33900          ASC  "M:"
33950 STUFF    BSZ  0
34000 kUPCUR   EQU  243
34050 kHOME    EQU  230
34100 kENDLINE EQU  232
34150 kSENDLIN EQU  227
34200 !  **********************************************************************
34250 NUMVA+   DAD  22403
34300 GETCMA   DAD  23477
34350 NUMVAL   DAD  22406
34400 STREXP   DAD  23724
34450 ERROR+   DAD  10220
34500 PTR2-    DAD  177715
34550 SCAN     DAD  21110
34600 STRREF   DAD  24056
34650 STREX+   DAD  23721
34700 BINTAB   DAD  104070
34750 CRTSTS   DAD  177702
34800 GRAPH.   DAD  12574
34850 ONEB     DAD  12153
34900 PTR2     DAD  177714
34950 CHKSTS   DAD  13204
35000 CRTBAD   DAD  177701
35050 CRTDAT   DAD  177703
35100 ALPHA.   DAD  12413
35150 TOS      DAD  101744
35200 DECUR2   DAD  13467
35250 HMCURS   DAD  13661
35300 TWOB     DAD  56760
35350 MOVCRS   DAD  13771
35400 RESMEM   DAD  31741
35450 CRTBYT   DAD  100206
35500 BYTCR!   DAD  14003
35550 INCHR    DAD  14262
35600 RTCUR.   DAD  13651
35650 STOST    DAD  46472
35700 INPUT.   DAD  16314
35750 INPTR    DAD  101143
35800 ROMFL    DAD  104065
35850 KYIDLE   DAD  103677
35900 GINTDS   DAD  177401
35950 GINTEN   DAD  177400
36000 MYBTAB   DAD  103703
36050 KEYCOD   DAD  177403
36100 KEYSTS   DAD  177402
36150 MSIN     DAD  70652
36200 DECODE   DAD  70766
36250 ACTMSU   DAD  103560
36300 ROMJSB   DAD  6223
36350 SAVER6   DAD  104066
36400 MSROM#   EQU  320
36450 PTR1     DAD  177710
36500 PTR1-    DAD  177711
36550 ASIZE    DAD  104744
36600 SAD1     DAD  13723
36650 MOD      DAD  14216
36700          FIN  
