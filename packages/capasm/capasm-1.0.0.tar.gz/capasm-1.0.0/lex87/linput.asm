10 !**********************************************************************
20 !*                                                                    *
30 !*        A KEYWORD THAT IS PARSED INTO MORE THAN ONE TOKEN           *
40 !*                                                                    *
50 !*        A TOKEN WITH A CLASS OF 44 (MISC IGNORE AT DECOMPILE)       *
60 !*         that makes it invisible when the program is listed         *
70 !*                                                                    *
80 !*              (c) 1982 Hewlett-Packard Co.                          *
90 !*                                                                    *
100 !*   This binary program implements the BASIC statement 'LINPUT'     *
110 !* which acts exactly the same as the BASIC statement 'INPUT' except *
120 !* that it will only allow you to input a string value and that      *
130 !* string value may contain commas and/or quotes. The keyword stands *
140 !* for Line INPUT, as it allows the inputing of a line regardless    *
150 !* of what characters are in that line.                              *
160 !*                                                                   *
170 !*********************************************************************
180 !*                                                                   *
190 !* An example of how a BASIC program might use LINPUT is:            *
200 !*                                                                   *
210 !*    100 DISP "Address of destination";                             *
220 !*    110 LINPUT Dest_addr$                                          *
230 !*    120 PRINT# 1; Dest_addr$                                       *
240 !*                                                                   *
250 !*********************************************************************
260          NAM 51,LINPUT           ! SET UP PCB, BPGM # IS 51
270          DEF RUNTIM              ! POINTER TO RUNTIME ADDRESS TABLE
280          DEF ASCIIS              ! POINTER TO TABLE OF ASCII KEYWORDS
290          DEF PARSE               ! POINTER TO TABLE OF PARSE ADDRESSES
300          DEF ERMSG               ! POINTER TO TABLE OF ERROR MESSAGES
310          DEF INIT                ! POINTER TO INITIALIZATION ROUTINE
320 !*********************************************************************
330 !*  The way an INPUT statement works in the series 80 computers is   *
340 !* this: the keyword is actually parsed into two tokens, so the job  *
350 !* of doing an INPUT is split into three parts; two are performed by *
360 !* the two INPUT tokens and the third is performed by the system.    *
370 !* The first of the two tokens outputs a question mark to the CRT and*
380 !* puts the computer into a pseudo-calculator mode, which is known   *
390 !* as Idle-in-Input, by setting CSTAT (R16) to a 4, and then sets the*
400 !* immediate break bits in XCOM (R17) using "or"with 240(octal). Then*
410 !* the first token terminates its execution by returning to the      *
420 !* interpreter. The interpreter will see the immediate break bits in *
430 !* R17 and will drop out into the exec Loop. The exec will see that  *
440 !* the computer is in Idle-in-Input mode and will simply loop on     *
450 !* itself. At this point, the user starts typing his input (causing  *
460 !* keyboard interrupts, which set bits in R17 and SVCWRD, which cause*
470 !* the exec to call the character editor (CHEDIT), which echoes the  *
480 !* keys to the CRT, clears the SVCWRD flag, and returns to the exec).*
490 !* This continues until the END LINE key is pressed, which causes    *
500 !* CHEDIT to set a flag in the E register which will tell the exec   *
510 !* that END LINE has been pressed. This will cause the exec to resume*
520 !* execution of the BASIC program by re-entering the interpreter.    *
530 !* The third part of the INPUT is carried out by the second token of *
540 !* the INPUT statement. It takes the input line, parses and executes *
550 !* it, then stores the values in the appropriate variables.          *
560 !* LINPUT statement works in very much the same way. As a matter     *
570 !* of fact, the first two LINPUT tokens do nothing but call          *
580 !* the runtime code for the first of the INPUT tokens. The difference*
590 !* comes in the second token. For LINPUT, all we want to do is input *
600 !* a literal string with no expressions allowed, so we have no need  *
610 !* to parse and execute the input line. All we have to do is reverse *
620 !* the string so that the first character is at the highest address  *
630 !* and then store it in the string variable.                         *
640 !*********************************************************************
650 RUNTIM   BYT 0,0                 ! DUMMY ADDRESS FOR TOKEN #0 RUNTIME
660          DEF REV.                ! ADDRESS FOR TOKEN #1 RUNTIME ROUTINE
670          DEF LINPT.              ! ADDRESS FOR TOKEN #2 RUNTIME ROUTINE
680          DEF LIN$.               ! ADDRESS FOR TOKEN #3 RUTNIME ROUTINE
690 !*********************************************************************
700 PARSE    BYT 0,0                 ! DUMMY ADDRESS FOR KEYWORD #0 PARSE
710          BYT 0,0                 ! DUMMY FOR KEYWORD #1 PARSE (A FUNCTION)
720          DEF LINPRS              ! ADDRESS FOR KEYWORD #2 PARSE ROUTINE
730          BYT 377,377             ! TERMINATE RELOCATION OF ADDRESSES
740 !*********************************************************************
750 !*  The runtime table has three entries even though the ASCII and    *
760 !* parse tables have only two. The third entry in the runtime table  *
770 !* will only be used in conjunction with the second entry. If you    *
780 !* look at the parse routine for the second keyword (LINPUT) you will*
790 !* see that it pushes out both tokens 2 and 3. Normally, you want to *
800 !* keep a one for one relationship between entries in the ASCII,     *
810 !* PARSE, and RUNTIME tables, but there are times when you can play  *
820 !* tricks like this (if you're careful).                             *
830 !*********************************************************************
840 ASCIIS   ASP "LINPUTG"           ! KEYWORD #1 (REVISION DATE FUNCTION)
850          ASP "LINPUT"            ! KEYWORD #2
860 ERMSG    BYT 377                 ! TERMINATE ASCII AND ERROR MESSAGE TABLES
870 !*********************************************************************
880 ERR89    JSB =ERROR+             ! SET ERROR FLAGS IN R17 AND 'ERRORS'
890          BYT 89D                 ! SYSTEM ERROR MESSAGE #89 'INVALID PARAM'
900 !*********************************************************************
910 LINPRS   LDM R55,=2,51,371       ! LOAD TOKEN#, BPGM#, AND SYSTEM TOKEN
920          STMI R55,=PTR2-         ! STORE THEM ALL OUT TO PARSE STREAM
930          JSB =SCAN               ! SCAN THE INPUT STREAM FOR NEXT TOKEN
940          JSB =STRREF             ! TRY TO GET A STRING VARIABLE REFERENCE
950          JEZ ERR89               ! JIF NOT THERE, ERROR CONDITION
960          LDM R55,=3,51,371       ! ELSE LOAD SECOND TOKEN#, BPGM#, AND SYS
970          STMI R55,=PTR2-         ! STORE THEM OUT TO PARSE OUTPUT STREAM
980 INIT     RTN                     ! DONE FOR PARSING AND INITIALIZING
990 !*********************************************************************
1000 !*  LINPT. is the runtime code for the first of the two LINUT tokens.*
1010 !* It is responsible for the output of the question mark to the CRT  *
1020 !* and putting the computer into Idle-in-Input mode.                 *
1030 !*********************************************************************
1040          BYT 241                ! ATTRIB.,BASIC STATEMENT LEGAL AFTER THEN
1050 LINPT.   JSB =INPUT.            ! DO QUESTION MARK AND SET R16=4
1060          RTN                    ! DONE, WAIT FOR INPUT
1070 !*********************************************************************
1080 !*  LIN$. is the runtime code for the second of the the two LINUT    *
1090 !* tokens. It is responsible for reversing the string in memory so it*
1100 !* will be ready for storing into the string variable, and then doing*
1110 !* the actual store (by calling STOST). The R12 stack will already   *
1120 !* have been set up for the variable store by the tokens parsed by   *
1130 !* STRREF.                                                           *
1140 !*********************************************************************
1150          BYT 44                 ! ATTRIBUTE, MISCELLANEOUS IGNORE
1160 LIN$.    BIN                    ! BIN MODE FOR COUNTING
1170          LDMD R32,=INPTR        ! FETCH ADDRESS OF STRING THAT WAS INPUT
1180          STM R32,R14            ! SAVE A COPY
1190          CLM R36                ! PRE-SET LENGTH TO ZERO
1200 CHRCNT   POBD R35,+R32          ! GET THE NEXT BYTE FROM INPUT STRING
1210          CMB R35,=15            ! IS IT A CARRIAGE RETURN CHARACTER?
1220          JZR ENDOF$             ! JIF YES, WE'VE FOUND THE END AND LENGTH
1230          ICM R36                !    ELSE INCREMENT THE LENGTH
1240          JMP CHRCNT             !    AND LOOP TO CHECK THE NEXT CHARACTER
1250 ENDOF$   TSM R36                ! IS THE LENGHT ZERO?
1260          JZR DONE               ! JIF YES, RETURN A NULL STRING
1270          POBD R25,-R32          ! GET BACK TO LAST CHARACTER
1280 POPBLK   POBD R25,-R32          ! FETCH LAST CHARACTER FROM END OF STRING
1290          CMB R25,=40            ! IS IT A BLANK?
1300          JNZ DONE+              ! JIF NO, CONTINUE ON
1310          DCM R36                !    ELSE DECREMENT LENGTH (TRIM BLANKS)
1320          JNZ POPBLK             ! JIF LENGTH NOT ZERO
1330 DONE+    ICM R32                ! MOVE ADDRESS TO ONE HIGHER THAN END
1340          STM R32,R65            ! SET ADDRESS IN R65-R66
1350          CLB R67                ! CLEAR MOST SIGNIFICANT BYTE
1360 DOLOOP   CMM R14,R32            ! FRONT OF STRING HIGHER OR EQUAL TO END?
1370          JCY DONE               ! JIF YES
1380          LDBD R30,R14           !    ELSE GET BYTE FROM FRONT
1390          POBD R31,-R32          !    AND A BYTE FROM THE BACK
1400          STBD R30,R32           !    STORE THE FRONT BYTE IN BACK
1410          PUBD R31,+R14          !    AND THE BACK BYTE IN FRONT
1420          JMP DOLOOP             ! LOOP TIL STRING IS REVERSED IN PLACE
1430 DONE     PUMD R36,+R12          ! PUSH THE LENGTH OF STRING TO STACK
1440          PUMD R65,+R12          ! PUSH THE ADDRESS OF STRING TO STACK
1450          JSB =STOST             ! STORE THE STRING TO THE VARIABLE AREA
1460          RTN                    ! DONE
1470 !*********************************************************************
1480 !*  This is the runtime code for the revision date function, which is*
1490 !* a string function with no parameters which always returns the same*
1500 !* string value, the copyright notice and the revision code.          *
1510 !*********************************************************************
1520          BYT 0,56               ! ATTRIBUTES,STRING FUNCTION,NO PARAMETERS
1530 REV.     LDM R43,=44,0          ! LOAD LENGTH OF THE STRING
1540          DEF DATE               ! AND THE ADDRESS OF THE STRING
1550          BYT 0                  !    (IT NEEDS TO BE A THREE BYTE ADDRESS)
1560          BIN                    ! BIN MODE FOR ADDRESS MATH
1570          ADMD R45,=BINTAB       ! MAKE THE ADDRESS ABSOLUTE
1580          PUMD R43,+R12          ! PUSH THE LENGTH AND ADDRESS TO THE STACK
1590          RTN                    ! DONE
1600          ASC "82.111 .veR 2891 drakcaP-ttelweH )c(" ! THE REVISION STRING
1610 DATE     BSZ 0                  ! NEED LABEL HERE TO GET RIGHT ADDRESS
1620 !*********************************************************************
1630 BINTAB   DAD 104070             !
1640 ERROR+   DAD 10220              !
1650 INPTR    DAD 101143             !
1660 INPUT.   DAD 16314              ! LABEL DEFINITIONS
1670 PTR2-    DAD 177715             !
1680 SCAN     DAD 21110              !
1690 STOST    DAD 46472              !
1700 STRREF   DAD 24056              !
1710          FIN                    ! TERMINATE ASSEMBLY
