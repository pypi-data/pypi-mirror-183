1000 !*********************************************************************
1010 !*  This binary program implements the SAVE and GET statements for   *
1020 !* turning programs into normal strings in a DATA file and turning   *
1030 !* normal strings back into lines of a BASIC program.                *
1040 !*  The syntax for the two statements is:                            *
1050 !*     SAVE <file name>[,<beginning line>][,<ending line>]           *
1060 !*     GET <file name>                                               *
1070 !*  SAVE calculates the size of the DATA file needed by listing the  *
1080 !* program and counting the total length of the strings (plus the    *
1090 !* three bytes of header per string required by the file manager).   *
1100 !* It does this by taking over IOTRFC and forcing the select code to *
1110 !* a value that will cause the listed strings to go out through the  *
1120 !* hook. LSSET is an entry point in the LIST routine that lists the  *
1130 !* entire program. After the size of the data file is known, it is   *
1140 !* created (any old one of that name already in existence will be    *
1150 !* purged first) and then the program is listed again, this time with*
1160 !* the lines (as strings) being printed out to the data file.        *
1170 !*  GET opens the data file, reads a string, copies the string to    *
1180 !* the input buffer INPBUF, then calls the PARSER, which will parse  *
1190 !* the line and edit it into the program, if no errors occur. If a   *
1200 !* parse error occurs, an exclamation point is inserted into the line*
1210 !* after the line number and the line is parsed again as a comment.  *
1220 !* GET has to create a dummy string variable area in the binary      *
1230 !* program for the strings to be read into, because RDSTR. does a    *
1240 !* call to STOST before it returns, and STOST expects all the usual  *
1250 !* information on the stack and an associated variable area (in      *
1260 !* other words, we have to trick the system when we call RDSTR.).    *
1270 !*********************************************************************
1280          NAM 41,SAVG            ! SET UP THE PROGRAM CONTROL BLOCK
1290          DEF RUNTIM             ! PTR TO THE RUNTIME ADDRESSES
1300          DEF TOKS               ! PTR TO THE KEYWORDS
1310          DEF PARSE              ! PTR TO THE PARSE ADDRESSES
1320          DEF ERMSG              ! PTR TO THE ERROR MESSAGE TABLE
1330          DEF INIT               ! PTR TO THE INITIALIZATION ROUTINE
1340 RUNTIM   BYT 0,0                ! DUMMY RUNTIME ADDRESS FOR TOK# 0
1350          DEF SAVE.              ! RUNTIME ADDRESS FOR TOK# 1
1360          DEF REVISON.           ! RUNTIME ADDRESS FOR TOK# 2
1370          DEF GET.               ! RUNTIME ADDRESS FOR TOK# 3
1380 PARSE    BYT 0,0                ! DUMMY PARSE ADDRESS FOR TOK# 0
1390          DEF SAVPARS            ! PARSE ADDRESS FOR TOK# 1
1400          BYT 0,0                ! DUMMY PARSE ADDRESS FOR TOK# 3
1410          DEF GETPARS            ! PARSE ADDRESS FOR TOK# 3
1420 ERMSG    BYT 377,377            ! TERMINATE RELOCATION AND ERROR TABLE
1430 INIT     RTN                    ! NO INITIALIZATION
1440 TOKS     ASP "SAVE"             ! KEYWORD #1
1450          ASP "GET SAVE"         ! KEYWORD #2
1460          ASP "GET"              ! KEYWORD #3
1470          BYT 377                ! TERMINATE KEYWORD TABLE
1480 !*********************************************************************
1490 SAVPARS  PUBD R43,+R6           ! SAVE CURRENT TOKEN
1500          JSB =STREX+            ! GET THE FILE NAME
1510          JEN OK1                ! JIF IT WAS THERE
1520 ERR      POBD R43,-R6           ! ELSE CLEAN UP STACK
1530          JSB =ERROR+            ! REPORT THE ERROR
1540          BYT 88D                ! BAD STATEMENT
1550 OK1      CMB R14,=54            ! COMMA?
1560          JNZ PARSCOMN           ! JIF NO LINE NUMBERS
1570          JSB =G012N             ! ELSE GET ONE OR TWO LINE NUMBERS
1580          LDBI R56,=PTR2+        ! CLEAN UP PARSE STREAM
1590 PARSCOMN LDM R56,=41,371        ! BPGM# AND SYSTEM TOKEN
1600          POBD R55,-R6           ! RECOVER BPGM TOKEN #
1610          STMI R55,=PTR2-        ! STORE THEM OUT TO THE PARSE STREAM
1620          RTN                    ! DONE
1630 !*********************************************************************
1640 GETPARS  PUBD R43,+R6           ! SAVE THE INCOMING TOKEN
1650          JSB =STREX+            ! GET THE FILE NAME
1660          JEZ ERR                ! JIF NOT THERE
1670          JMP PARSCOMN           ! ELSE FINISH UP
1680 !*********************************************************************
1690          BYT 241                ! BASIC STATEMENT, LEGAL AFTER THEN
1700 SAVE.    JSB =CLEAR.            ! CLEAR THE CRT
1710          LDMD R10,=BINTAB       ! GET OUR BASE ADDRESS
1720          LDM R26,=SAVING        ! GET THE RELATIVE ADDRESS OF MSG
1730          ADM R26,R10            ! MAKE IT ABSOLUTE
1740          LDM R36,=20,0          ! LOAD THE LENGTH OF THE MSG
1750          JSB =OUTSTR            ! OUTPUT THE MSG
1760          LDMD R41,=IOTRFC       ! SAVE THE REAL HOOK CONTENTS
1770          STMD R41,X10,SAVIOTFC  ! STORE IT AWAY
1780          LDMD R40,=SCTEMP       ! SAVE THE REAL SELECT CODE
1790          STMD R40,X10,SAVSCTEM  ! STORE IT AWAY
1800          LDM R72,=231,231,11,0,0,0 ! LOAD DEFAULT LIST PARAMETERS
1810          STMD R72,=LLDCOM       ! SET THEM
1820          LDM R20,R12            ! COPY STACK POINTER
1830          SBM R20,=5,0           ! TAKE OFF STRING STUFF
1840          CMMD R20,=TOS          ! ANYTHING ELSE THERE?
1850          JZR DO-IT              ! JIF NO, USE DEFAULTS
1860          JSB =ONEI              ! ELSE GET ONE NUMBER OFF
1870          LDM R20,R12            ! COPY STACK POINTER
1880          SBM R20,=5,0           ! ADJUST FOR STRING STUFF
1890          CMMD R20,=TOS          ! ANY MORE?
1900          JZR STOLIN1            ! JIF NO
1910          STMD R45,=LLDCOM       ! ELSE SET LAST LINE DECOMPILE
1920          JSB =ONEI              ! GET THE FIRST LINE
1930 STOLIN1  STMD R45,=FLDCOM       ! SET THE FIRST LINE DECOMPILE
1940 DO-IT    POMD R43,-R12          ! GET THE STRING
1950          STMD R43,X10,FILENAME  ! SAVE IT AWAY
1960          CLM R50                ! SET UP FOR A FLOATING POINT 1
1970          LDB R57,=10C           ! THAT FINISHES IT
1980          PUMD R50,+R12          ! PUSH TO STACK FOR ASSIGN# 1 TO
1990          PUMD R43,+R12          ! PUSH FILE NAME BACK
2000          PUMD R10,+R6           ! SAVE OUR BASE ADDRESS
2010          JSB =ROMJSB            ! SELECT THE MSTORAGE ROM
2020          DEF ASSIG.             ! ASSIGN BUFFER # 1 TO FILE
2030          VAL MSROM#             ! ROM TO SELECT
2040          POMD R10,-R6           ! RECOVER OUR BASE
2050          CMB R17,=300           ! ANY ERRORS?
2060          JNC ITSTHERE           ! JIF NO, IT WAS THERE AND DATA FILE
2070          LDBD R20,=ERRORS       ! GET REASON
2080          CMB R20,=67D           ! FILE NAME ERROR?
2090          JZR CREATIT            ! JIF IT WASN'T THERE
2100          GTO RESTORE            ! ELSE BAIL OUT
2110 ITSTHERE PUMD R10,+R6           ! SAVE OUR BASE
2120          STMD R12,=TOS          ! MAKE SURE STACK LOOKS GOOD
2130          LDMD R73,X10,FILENAME  ! GET THE FILE NAME BACK
2140          PUMD R73,+R12          ! PUSH IT TO THE STACK
2150          JSB =ROMJSB            ! SELECT THE ROM
2160          DEF MSPUR.             ! PURGE THE FILE
2170          VAL MSROM#             ! ROM TO SELECT
2180          POMD R10,-R6           ! RECOVER OUR BASE ADDRESS
2190          JMP CREATIT            ! CONTINUE
2200 CALCRTN  POMD R10,-R6           ! RECOVER BASE
2210          GTO RESTORE 
2220 CREATIT  PUMD R10,+R6           ! SAVE OUR BASE
2230          ANM R17,=77            ! CLEAN UP THE ERROR FLAG
2240          CLB R20                ! AND THE OTHER ONE
2250          STBD R20,=ERRORS       ! OUT IN RAM
2260          LDM R36,=COUNT         ! GET THE REL ADDRESS OF ROUTINE
2270          ADM R36,R10            ! MAKE IT ABSOLUTE
2280          STM R36,R45            ! SET IT
2290          LDB R47,=236           ! LOAD A RTN OPCODE
2300          LDB R44,=316           ! LOAD A JSB OPCODE
2310          STMD R44,=IOTRFC       ! TAKE THE HOOK
2320          LDMD R72,=LLDCOM       ! SAVE LIST POINTERS
2330          PUMD R72,+R6           !   ON THE RTN STACK
2340          CLM R70                ! ZERO THE SELECT CODE
2350          STMD R70,=SCTEMP       ! SET THE SELECT CODE
2360          STMD R75,=NXTDAT       ! INITIALIZE BYTE COUNT TO 0
2370          PUBD R16,+R6           ! SAVE CSTAT
2380          LDB R16,=2             ! FAKE RUN MODE
2390          JSB =LSSET             ! LIST THE PROGRAM
2400          POBD R16,-R6           ! RESTORE CSTAT
2410          POMD R72,-R6           ! RESTORE THE LIST POINTERS
2420          STMD R72,=LLDCOM       ! RESET FIRST/LAST LINE POINTERS
2430          CLB R50                ! FOR THE MULTI-BYTE ADDS
2440          LDMD R45,=NXTDAT       ! GET THE BYTE COUNT
2450          JZR CALCRTN            ! JIF NOTHING THERE
2460          ADM R45,R46            ! WE NEED TO ADD THREE BYTES FOR EACH
2470          ADM R45,R46            !   RECORD BECAUSE OF THE HEADER USED EACH
2480          ADM R45,R46            !   TIME A STRING CROSSES RECORD BOUNDARY
2490          ADM R45,=3,0,0         ! AN EXTRA THREE
2500          TSB R45                ! IS IT ZERO?
2510          JZR NOINC              ! JIF YES
2520          ICM R46                ! ELSE ROUND IT UP
2530 NOINC    LDM R55,R46            ! SET IT FOR CONBI3
2540          JSB =CONBI3            ! CONVERT IT TO FLOATING-POINT
2550          POMD R10,-R6           ! RECOVER OUR BASE
2560          PUMD R10,+R6           ! SAVE IT AGAIN
2570          LDMD R53,X10,FILENAME  ! GET THE FILE NAME
2580          PUMD R53,+R12          ! PUSH IT TO STACK
2590          PUMD R40,+R12          ! PUSH THE NUMBER OF RECORDS DESIRED
2600          LDM R54,=377,56C,2C,0  ! MAKE 256 BYTE RECORDS
2610          PUMD R50,+R12          ! PUSH IT TO THE STACK
2620          JSB =ROMJSB            ! SELECT THE ROM
2630          DEF MSCRE.             ! CREATE THE FILE
2640          VAL MSROM#             ! ROM #
2650          POMD R10,-R6           ! RECOVER OUR BASE
2660          CMB R17,=300           ! ANY ERRORS ON THE CREATE?
2670          JCY SAVEX              ! JIF YES
2680          PUMD R10,+R6           ! SAVE OUR BASE
2690          JSB X10,ASNPRT         ! ASSIGN THE BUFFER AND DO THE MSPRNT
2700          POMD R10,-R6           ! RECOVER OUR BASE
2710          CMB R17,=300           ! ANY ERRORS IN THE ASSIGN?
2720          JNC PRINT              ! JIF NO
2730 SAVEX    GTO RESTORE            ! BAIL OUT
2740 ASNPRT   STMD R12,=TOS          ! MAKE SURE STACK LOOKS GOOD
2750          CLM R50                ! FIX UP FOR REAL 1
2760          LDB R57,=10C
2770          PUMD R50,+R12          ! PUSH IT TO THE STACK
2780          LDMD R53,X10,FILENAME  ! GET THE FILE NAME
2790          PUMD R53,+R12          ! PUSH IT TO THE STACK
2800          JSB =ROMJSB            ! SELECT THE ROM
2810          DEF ASSIG.             ! ASSIGN THE BUFFER
2820          VAL MSROM#             ! ROM#
2830          CMB R17,=300           ! ANY ERRORS?
2840          JCY ASNRTN             ! JIF YES, DO NO MORE
2850          CLM R40                ! ELSE MAKE A 1
2860          LDB R47,=10C           !  (FLOATING POINT 1)
2870          PUMD R40,+R12          ! PUSH IT TO THE STACK
2880          JSB =ROMJSB            ! SELECT THE ROM
2890          DEF MSPRNT             ! DO THE READ#
2900          VAL MSROM#             ! ROM #
2910 ASNRTN   RTN                    ! DONE
2920 PRINT    LDM R36,=SAVERECS      ! GET THE REL ADDRESS OF OUR ROUTINE
2930          ADM R36,R10            ! MAKE IT ABSOLUTE
2940          STM R36,R45            ! SET IT
2950          LDB R47,=236           ! LOAD A RTN OPCODE
2960          LDB R44,=316           ! LOAD A JSB OPCODE
2970          STMD R44,=IOTRFC       ! TAKE THE HOOK
2980          PUBD R16,+R6           ! SAVE CSTAT
2990          LDB R16,=2             ! FAKE RUN MODE
3000          PUMD R10,+R6           ! SAVE OUR BASE
3010          JSB =LSSET             ! LIST AND PRINT# IT
3020          CLM R36                ! LINE LEN OF 0
3030          POMD R10,-R6           ! RECOVER OUR BASE
3040          PUMD R10,+R6           ! SAVE IT AGAIN
3050          JSB X10,SAVERECS       ! PRINT A NULL STRING AT THE END
3060          JSB =ROMJSB            ! SELECT THE ROM
3070          DEF PREOL.             ! DO THE END OF LINE PRINTING
3080          VAL MSROM#             ! ROM #
3090          POMD R10,-R6           ! RECOVER OUR BASE
3100          POBD R16,-R6           ! RESTORE CSTAT
3110          JSB X10,CLOSE          ! CLOSE THE FILE
3120 RESTORE  LDMD R71,X10,SAVIOTFC  ! GET THE OLD HOOK
3130          STMD R71,=IOTRFC       ! RESTORE IT
3140          LDMD R70,X10,SAVSCTEM  ! GET THE OLD SELECT CODE
3150          STMD R70,=SCTEMP       ! RESTORE IT
3160 FINMSG   JSB =CLEAR.            ! CLEAR THE CRT
3170          LDM R26,=MESAGE        ! LOAD THE ADDRESS OF THE MSG
3180          ADM R26,R10            ! MAKE IT ABSOLUTE
3190          LDM R36,=4,0           ! LOAD THE LEN
3200          JSB =OUTSTR            ! OUTPUT THE STRING
3210          RTN                    ! DONE
3220 MESAGE   ASC "DONE"
3230 !*********************************************************************
3240 CLOSE    CLM R40                ! NEED ANOTHER 1
3250          LDB R47,=10C           ! FINISH THE 1
3260          PUMD R40,+R12          ! PUSH TO STACK
3270          LDM R46,=1,0           ! LENGTH OF THE "*" STRING
3280          PUMD R46,+R12          ! PUSH IT TO STACK
3290          LDM R45,=STAR          ! ADDRESS OF THE ASTERISK
3300          BYT 0                  ! NEED A THREE BYTE ADDRESS
3310          ADM R45,R10            ! MAKE IT ABSOLUTE
3320          CLB R47                ! CLEAN UP THE MS BYTE
3330          PUMD R45,+R12          ! PUSH THE ADDRESS
3340          PUMD R10,+R6           ! SAVE OUR BASE
3350          JSB =ROMJSB            ! SELECT THE ROM
3360          DEF ASSIG.             ! CLOSE THE BUFFER
3370          VAL MSROM#             ! ROM# TO SELECT
3380          POMD R10,-R6           ! RECOVER THE BASE
3390          RTN                    ! DONE
3400 !*********************************************************************
3410 COUNT    BIN                    ! FOR THE MATH
3420          CLB R40                ! FOR THE MULTI-BYTE ADD
3430          ADM R36,=4,0           ! ADD SOME FOR THE HEADER
3440          LDMD R45,=NXTDAT       ! GET THE PREVIOUS COUNT
3450          ADM R45,R36            ! ADD THE CURRENT LINE LEN
3460          STMD R45,=NXTDAT       ! SAVE THE NEW COUNT
3470          RTN                    ! DONE
3480 !*********************************************************************
3490 SAVERECS PUMD R36,+R12          ! PUSH THE LEN OF THE LINE
3500          STM R26,R24            ! COPY OF START
3510          ADM R26,R36            ! MOVE TO END OF STRING
3520          STM R26,R45            ! GET THE ADDRESS
3530          CLB R47                ! CLEAR THE MOST SIGNIFICANT BYTE
3540          PUMD R45,+R12          ! PUSH THE ADDRESS
3550 SAVLOOP  CMM R24,R26            ! DONE?
3560          JCY PRINT-IT           ! JIF YES
3570          POBD R30,-R26          ! FETCH LAST BYTE
3580          LDBD R31,R24           ! FETCH FIRST BYTE
3590          STBD R31,R26           ! SWAP THEM
3600          PUBD R30,+R24          ! DITTO
3610          JMP SAVLOOP            ! LOOP TIL DONE
3620 PRINT-IT JSB =ROMJSB            ! SELECT THE ROM
3630          DEF PRSTR.             ! PRINT THE STRING
3640          VAL MSROM#             ! ROM#
3650          RTN 
3660 !*********************************************************************
3670          BYT 141                ! BASIC STATEMENT, LEGAL AFTER THEN
3680 GET.     BIN                    ! FOR ADDRESS MATH
3690          LDMD R10,=BINTAB       ! LET'S GET OUR BASE
3700          POMD R43,-R12          ! GET THE FILE NAME
3710          STMD R43,X10,FILENAME  ! SAVE IT AWAY
3720          CLB R16
3730          JSB =FXLEN             ! MAKE SURE THE PROGRAM'S DEALLOCATED
3740          JSB =CLEAR.            ! CLEAR THE SCREEN
3750          LDM R26,=GETTING       ! GET ADDRESS OF MESSAGE
3760          ADMD R26,=BINTAB       ! MAKE IT ABSOLUTE
3770          LDM R36,=17,0          ! LOAD THE LENGTH OF THE MESSAGE
3780          JSB =OUTSTR            ! OUTPUT THE MESSAGE
3790          JSB =DECUR2            ! GET RID OF THE CURSOR
3800          JSB =DNCURS            ! MOVE DOWN ONE LINE
3810 BIN1     LDM R10,R4             ! GET THE PC
3820          BIN                    ! GOOD FOR ADDRESS MATH
3830          SBM R10,=BIN1          ! GET OUR BASE ADDRESS
3840          STMD R10,=BINTAB       ! RESTORE BINTAB CASE 'FXLEN' DESTROYED
3850          JSB X10,ASNPRT         ! TRY TO OPEN THE FILE
3860          CMB R17,=300           ! ANY ERRORS?
3870          JNC OKGET              ! JIF NO, IT'S THERE
3880          LDMD R10,=BINTAB       ! GET OUR BASE
3890          GTO FINMSG             ! OUTPUT THE MESSAGE
3900 OKGET    LDM R10,R4             ! GET PC
3910          BIN                    !
3920          SBM R10,=OKGET         ! GET OUR BASE ADDRESS
3930          STMD R10,=BINTAB       ! SET IT IN CASE PARSING BLEW IT AWAY
3940          LDMD R45,=NXTMEM       ! GET HIGH ADDRESS OF AVAILABLE SPACE
3950          SBMD R45,=LAVAIL       ! GET AVAILABLE MEMORY COUNT
3960          CMM R45,=0,2,0         ! ENOUGH MEMORY LEFT?
3970          JCY OKGET2             ! JIF YES
3980          JSB =ERROR             ! ELSE REPORT ERROR
3990          BYT 19D                ! MEM OVF
4000          GTO FINMSG             ! OUTPUT 'DONE' MESSAGE
4010 GETDON   LDBD R40,=ERRORS       ! GET REASON FOR ERROR
4020          CMB R40,=107           ! END OF FILE ERROR?
4030          JZR EOFERR             ! JIF YES
4040          CMB R40,=110           ! END OF RECORD ERROR?
4050          JNZ BADERR             ! JIF NO, LET IT GO
4060 EOFERR   CLM R40                ! ELSE CLEAR ERROR FLAGS
4070          STMD R40,=ERLIN#       !  ---
4080          STBD R40,=ERRTYP       ! ---
4090          ANM R17,=77            !    AND IN XCOM
4100 BADERR   JSB =ST240+            ! SET IMMEDIATE BREAK BITS
4110 BIN5     LDM R10,R4             ! COPY OF PC
4120          BIN                    ! FOR ADDRESS MATH
4130          SBM R10,=BIN5          ! GET BASE ADDRESS
4140          JSB X10,CLOSE          ! CLOSE THE FILE
4150          GTO FINMSG             ! OUTPUT THE 'DONE' MESSAGE
4160 OKGET2   LDMD R12,=TOS          ! RESET STACK POINTER
4170          LDM R45,=BUFFER        ! GET THE ADDRESS OF THE BUFFER
4180          BYT 0                  ! AS A THREE BYTE QUANTITY
4190          ADMD R45,=BINTAB       ! MAKE IT ABSOLUTE
4200          PUMD R45,+R12          ! PUSH TO STACK
4210          LDM R51,=240,0,0,0,0,0,200 ! TOTAL SIZE, NAME PTR, HEADER
4220          PUMD R51,-R45          ! FAKE VARIABLE HEADER AREA
4230          LDM R64,=0,0,240,0     ! CURRENT LEN, MAX LEN
4240          PUMD R64,-R45          ! MORE VARIABLE HEADER STUFF
4250          PUBD R57,+R12          ! PUSH STUFF FOR STOST: HEADER
4260          PUMD R66,+R12          !           MAX LEN STRING VAR (0,1)
4270          PUMD R45,+R12          !           ADDRESS OF FIRST BYTE OF $ VAR
4280          PUMD R66,+R12          !           MAX LEN TO STORE INTO
4290          PUMD R45,+R12          !           ADDRESS TO STORE INTO
4300          STMD R45,X10,BUFADR    ! SAVE BUFFER ADDRESS
4310          JSB =ROMJSB            ! CALL A BANK SELECT ROM
4320          DEF RDSTR.             ! READ A STRING FROM THE FILE
4330          VAL MSROM#             ! IT'S THE MASS STORAGE ROM
4340          CMB R17,=300           ! ANY ERRORS ?
4350          JCY GETDON             ! JIF YES
4360          LDMD R10,=BINTAB       ! ELSE GET BASE ADDRESS
4370          LDMD R26,X10,BUFADR    ! GET ADDRESS OF BUFFER
4380          BIN 
4390          LDM R30,=INPBUF        ! GET ADDRESS OF INPUT BUFFER
4400          LDB R32,=40            ! LOAD A BLANK
4410          PUBD R32,+R30          ! PUSH IT TO BUFFER
4420          LDMD R24,R26           ! GET THE LEN OF THE STRING READ
4430          JZR GOTBUF             ! JIF NO CHARACTERS
4440 SWAP     POBD R32,-R26          ! GET THE NEXT CHARACTER
4450          PUBD R32,+R30          ! PUSH IT TO INPUT BUFFER
4460          DCM R24                ! DECREMENT LEN COUNT
4470          JNZ SWAP               ! JIF MORE TO DO
4480 GOTBUF   LDM R36,R30            ! COPY END OF BUFFER PTR
4490          SBM R36,=INPBUF        ! MINUS THE START OF BUFFER
4500          STMD R36,X10,BUFLEN    ! SAVE IN CASE OF ERROR FOR PRINT
4510          LDB R24,=15            ! LOAD A CR CHARACTER
4520          PUBD R24,+R30          ! PUSH IT OUT FOR PARSER
4530          PUBD R25,+R6           ! SAVE A 0 FLAG ON R6 FOR ERROR TRAP
4540          CMB R36,=81D           ! DO WE NEED TO MOVE THE CURSOR DOWN?
4550          JNC PARSIT             ! JIF NO
4560          JSB =DNCURS            ! MOVE CURSOR DOWN A ROW
4570 PARSIT   CLB R16                ! FOR LINEDR
4580          LDMD R20,=ASNTBL       ! SAVE ASSIGN BUFFER POINTER
4590          PUMD R20,+R6           ! ON THE R6 STACK
4600          LDMD R42,=LAVAIL       ! SAVE SOME SYSTEM POINTERS
4610          PUMD R42,+R6           ! ON THE R6 STACK
4620          LDMD R42,=RTNSTK       ! SAVE SOME MORE
4630          PUMD R42,+R6           ! SAME PLACE
4640          LDMD R45,=LWAMEM       ! SAVE SOME MORE
4650          PUMD R45,+R6           ! AGAIN
4660          LDMD R45,=LAVAIL       ! MOVE LWAMEM
4670          STMD R45,=LWAMEM       !   UP TO LAVAIL
4680          JSB =RSETGO            ! RESET EVERYTHING UP
4690          JSB =PARSER            ! TRY TO PARSE THE LINE
4700          POMD R45,-R6           ! START RECOVERING THINGS
4710          STMD R45,=LWAMEM       !
4720          POMD R42,-R6           !
4730          STMD R42,=RTNSTK       !
4740          POMD R42,-R6           !
4750          STMD R42,=LAVAIL       !
4760          POMD R20,-R6           !
4770          STMD R20,=ASNTBL       !
4780          LDB R16,=1             !
4790          CMB R17,=300           ! ANY ERRORS?
4800          JCY FIXIT              ! JIF YES
4810          BIN                    ! CONFIRM MATH MODE
4820          DCM R6                 ! THROW AWAY ERROR TRAP FLAG
4830          GTO OKGET              ! LOOP
4840 FIXIT    POBD R36,-R6           ! RECOVER ERROR TRAP FLAG
4850          JNZ ERREXIT            ! JIF TWO ERRORS
4860          ICB R36                ! SET FLAG
4870          PUBD R36,+R6           ! PUT IT BACK
4880          ANM R17,=77            ! CLEAR ERROR FLAGS
4890          CLM R40                ! CLEAR ERROR FLAGS
4900          STMD R40,=ERLIN#       ! CLEAR ERROR FLAGS
4910          STBD R40,=ERRTYP       ! CLEAR ERROR FLAGS
4920          LDM R24,=INPBUF        ! GET ADDRESS OF BUFFER
4930          STM R24,R22            ! COPY
4940          ICM R24                ! MOVE AHEAD TO THE FIRST CHARACTER
4950 MOVE-1   POBD R20,+R24          ! GET THE FIRST CHARACTER
4960          PUBD R20,+R22          ! MOVE IT BACK ONE PLACE
4970          CMB R20,=40            ! A BLANK ?
4980          JZR MOVE-1             ! JIF YES
4990          JSB =DIGIT             ! IS IT A DIGIT?
5000          JEN MOVE-1             ! JIF YES
5010          LDB R20,=41            ! ELSE LOAD A !
5020          PUBD R20,-R22          ! PUSH IT TO THE HOLE
5030          JSB =PRINT.            ! SET THE SCTEMP SELECT CODE
5040 BIN3     LDM R10,R4             ! GET PC
5050          BIN                    ! CALCULATE BASE IN CASE PARSER DESTROYED
5060          SBM R10,=BIN3          !    BINTAB
5070          LDMD R36,X10,BUFLEN    ! GET LENGTH OF BUFFER
5080          LDM R26,=INPBUF        ! GET THE START ADDRESS
5090          JSB =DRV12.            ! PRINT THE LINE
5100          GTO PARSIT             ! GOT PARSE IT AS A COMMENT
5110 ERREXIT  LDM R10,R4             ! GET CURRENT ADDRESS
5120          BIN                    ! FOR ADDRESS MATH
5130          SBM R10,=ERREXIT       ! GET BPGM'S BASE ADDRESS
5140          GTO FINMSG             ! GO DISPLAY 'DONE' MESSAGE
5150 !*********************************************************************
5160          BYT 0,56
5170 REVISON. BIN                    ! FOR ADDRESS MATH
5180          LDM R43,=40D,0         ! LEN OF STRING
5190          DEF DATE               ! ADDRESS AS TWO BYTE REL
5200          BYT 0                  ! THERE'S THE THIRD BYTE
5210          ADMD R45,=BINTAB       ! NOW IT'S ABSOLUTE
5220          PUMD R43,+R12          ! PUSH TO RETURN STACK
5230          RTN                    ! DONE
5240          ASC "81.202 .veR 2891 .oC drakcaP-ttelweH )c("
5250 DATE     BSZ 0
5260 !*********************************************************************
5270 SAVING   ASC "SAVE IN PROGRESS"
5280 GETTING  ASC "GET IN PROGRESS"
5290 DONE     ASC "DONE"
5300          ASC "*"
5310 STAR     BSZ 0
5320 SAVIOTFC BSZ 7
5330 SAVSCTEM BSZ 10
5340 FILENAME BSZ 5
5350 BUFADR   BSZ 3
5360 BUFLEN   BSZ 2
5370          BSZ 300
5380 BUFFER   BSZ 0
5390 !*********************************************************************
5400 ASNTBL   DAD 100125
5410 ASSIG.   DAD 65466
5420 BINTAB   DAD 104070
5430 CALVRB   DAD 100030
5440 CLEAR.   DAD 14225
5450 CONBI3   DAD 4516
5460 DECUR2   DAD 13467
5470 DIGIT    DAD 21710
5480 DNCURS   DAD 13751
5490 DRV12.   DAD 6722
5500 ERLIN#   DAD 100114
5510 ERROR    DAD 10223
5520 ERROR+   DAD 10220
5530 ERRORS   DAD 100123
5540 ERRTYP   DAD 100124
5550 FLDCOM   DAD 100053
5560 FXLEN    DAD 31001
5570 G012N    DAD 24707
5580 INPBUF   DAD 100236
5590 IOTRFC   DAD 103643
5600 LAVAIL   DAD 100025
5610 LLDCOM   DAD 100050
5620 LSSET    DAD 6445
5630 LWAMEM   DAD 100041
5640 MSCRE.   DAD 65176
5650 MSPRNT   DAD 66221
5660 MSPUR.   DAD 64604
5670 MSROM#   DAD 320
5680 NXTDAT   DAD 101645
5690 NXTMEM   DAD 100022
5700 ONEI     DAD 56736
5710 OUTSTR   DAD 14020
5720 PARSER   DAD 20000
5730 PREOL.   DAD 70464
5740 PRINT.   DAD 71332
5750 PRSTR.   DAD 66662
5760 PTR2-    DAD 177715
5770 PTR2+    DAD 177716
5780 RDSTR.   DAD 67314
5790 ROMJSB   DAD 6223
5800 RSETGO   DAD 5700
5810 RTNSTK   DAD 100033
5820 SCTEMP   DAD 101721
5830 ST240+   DAD 21067
5840 STREX+   DAD 23721
5850 TOS      DAD 101744
5860 FIN      FIN 
