01000 MYBP#    EQU  32
01010          NAM  32,REDZER  
01020          DEF  RUNTIM  
01030          DEF  TOKS    
01040          DEF  PARSE   
01050          DEF  ERMSG   
01060          DEF  INIT    
01070 RUNTIM   BYT  0,0
01080          DEF  MAT.             !  FOR 'MAT' KEYWORD (JUST DOES A 'RTN')
01090          DEF  OTHER            !  FOR 'ZER' KEYWORD ATTRIBUTES
01100          DEF  REDIM.           !  FOR 'REDIM' KEYWORD (JUST DOES A 'RTN')
01110          BYT  0,0              !  DUMMY FOR BYT 377
01120          DEF  ZER.             !  ACTUAL RUNTIME FOR 'ZER'
01130          DEF  DUMMY=.          !  RUNTIME FOR '=' (JUST A 'RTN')
01140          DEF  REDIM1           !  RUNTIME FOR ONE-DIM 'REDIM'
01150          DEF  REDIM2           !  RUNTIME FOR TWO-DIM 'REDIM'
01160 PARSE    BYT  0,0              ! 
01170          DEF  MATPAR           !  'MAT' PARSE ADDRESS
01180          DEF  ERRPAR           !  'ZER' PARSE ADDRESS (ERROR OUT)
01190          DEF  REDPAR           !  'REDIM' PARSE ADDRESS
01200          BYT  377,377          !  TERMINATE RELOCATION
01210 ERMSG    BYT  200              !  FIRST NINE ERROR MESSAGES ARE DUMMIES
01220          BYT  200,200,200,200  !      BECAUSE WE DON'T WANT A WARNING,
01230          BYT  200,200,200,200  !          WE WANT A HARD ERROR
01240          ASP  "DIM SIZE"       !  ERROR MESSAGE FOR ERROR# 366
01250          BYT  377              !  TERMINATE ERROR MESSAGE TABLE
01260 INIT     RTN                   !  NO INITIALIZATION
01270 ! ***************************************************************
01280 MATPAR   LDB  R57,=371         !  LOAD THE SYSTEM MARKER TOKEN
01290          LDB  R56,=MYBP#       !  LOAD OUR BINARY PROGRAM NUMBER
01300          LDB  R55,R43          !  GET THE BPGM TOKEN #
01310          STMI R55,=PTR2-       !  PUSH THEM OUT TO PARSE STREAM
01320          JSB  =NARRE+          !  GET A SIMPLE NUMERIC VAR AS AN ARRAY REF
01330          CMB  R14,=EQUALS      !  CHECK FOR THE EQUAL SIGN
01340          JZR  OKMAT            !  JIF IT'S THERE
01350 ERRPAR   JSB  =ERROR+          !  OTHERWISE ERROR OUT
01360          BYT  88D              !  BAD STATEMENT
01370 OKMAT    JSB  =SCAN            !  GET PAST THE EQUAL SIGN
01380          CMB  R43,=2           !  CHECK FOR TOKEN 2 IN BPGM ('ZER')
01390          JNZ  ERRPAR           !  JIF NOT THERE TO ERROR
01400          LDB  R57,=371         !  LOAD SYS MARKER TOKEN
01410          LDB  R56,=MYBP#       !  GET OUR BPGM #
01420          LDB  R55,=5           !  LOAD '=' TOKEN NUMBER
01430          STMI R55,=PTR2-       !  PUSH IT ALL OUT TO PARSE STACK
01440          LDB  R55,=6           !  LOAD 'ZER' TOKEN #
01450          STMI R55,=PTR2-       !  PUSH IT ALL OUT AGAIN
01460          JSB  =SCAN            !  DO A SCAN FOR THE SYSTEM
01465 ! ********************************************************************
01470          RTN                   !  DONE
01480 REDPAR   LDB  R57,=371         !  LOAD THE SYSTEM MARKER TOKEN
01490          LDB  R56,=MYBP#       !  GET OUR BPGM #
01500          LDB  R55,R43          !  GET THE 'REDIM' KEYWORD TOKEN
01510          STMI R55,=PTR2-       !  PUSH IT ALL OUT TO THE PARSE STACK
01520 ALOOP    JSB  =SCAN            !  GET THE NEXT TOKEN
01530          CMB  R14,=2           !  IS IT AN ARRAY REFERENCE?
01540          JNZ  ERRPAR           !  JIF NO, BAD STATEMENT
01550          JSB  =PSH45           !  ELSE PUSH OUT THE ARRAY REF AND NAME
01560          LDB  R32,=7           !  LOAD 1-DIM TOKEN AS DEFAULT
01570          LDMD R30,=BINTAB      !  GET BASE ADDRESS FOR JSB
01580          JSB  X30,SUBSCR       !  GO HANDLE THE SUBSCRIPTS
01590          JEZ  ERRPAR           !  JIF BAD SUBSCRIPTING
01600          CMB  R14,=COMMA       !  ELSE CHECK FOR MORE REDIMS
01610          JZR  ALOOP            !  LOOP IF MORE TO DO
01620          RTN                   !  ELSE DONE
01630 ! ************************************************************************
01640 TOKS     ASP  "MAT"            ! 
01650          ASP  "ZER"            !  KEYWORD TABLE
01660          ASP  "REDIM"          ! 
01670          BYT  377              !  TERMINATE SALT PORTION OF TABLE
01680          ASP  "ZER"            ! 
01690          BYT  275              !  'HIDDEN' TOKENS
01700          BYT  377              ! 
01710 ! ************************************************************************
01720 SUBSCR   PUBD R36,+R6          !  SAVE 36
01730          JSB  =NUMVAL          !  GET A NUMERIC VALUE FOR FIRST SUBSCRIPT
01740          POBD R36,-R6          !  RECOVER 36
01750          JEZ  SUBRTN           !  JIF NO SUBSCRIPT, ERROR FROM CALLER
01760          CMB  R14,=COMMA       !  CHECK FOR COMMA, SECOND SUBSCRIPT?
01770          JNZ  RTPAR            !  JIF NONE
01780          ICB  R32              !  IF 2nd ONE WAS THERE, INC TOK # TO 2-DIM
01790          PUBD R36,+R6          !  SAVE 36
01800          JSB  =NUMVA+          !  SCAN AND GET THE SECOND SUBSCRIPT
01810          POBD R36,-R6          !  RECOVER 36
01820          JEZ  SUBRTN           !  JIF NOT THERE, RETURN AND ERROR
01830 RTPAR    CMB  R14,=CLOSE       !  LOOK FOR CLOSE PARANTHESIS
01840          CLE                   !  PRESET FLAG TO ERROR CONDITION
01850          JNZ  SUBRTN           !  JIF CLOSE NOT THERE
01860          JSB  =SCAN            !  ELSE SCAN PAST IT
01870          LDM  R56,=32,371      !  LOAD BPGM # AND SYS MARKER TOK
01880          LDB  R55,R32          !  GET BPGM TOK #
01890          STMI R55,=PTR2-       !  PUSH IT ALL TO THE PARSE STACK
01900          CLE                   !  SET THE ERROR FLAG
01910          ICE                   !         TO NO ERROR
01920 SUBRTN   RTN                   !  DONE
01930 ! **************************************************************
01940          BYT  41               !  ATTRIBUTE FOR 'ZER' KEYWORD
01950 OTHER    RTN                   !  DO NOTHING
01960          BYT  5,51             !  PRECEDENCE AND ATTRIBUTE OF DUMMY '='
01970 DUMMY=.  RTN                   !  DO NOTHING
01980          BYT  241              !  ATTRIBUTE OF 'REDIM' AND 'MAT' KEYWORDS
01990 REDIM.   BSZ  0                ! 
02000 MAT.     RTN                   !  DO NOTHING
02010 ! **************************************************************
02020          BYT  0,55             !  HIDDEN 'ZER' TOK NEEDS TO LOOK LIKE A
02021 !                                !    FUNCTION FOR DECOMPILE PURPOSE
02030 ZER.     POMD R65,-R12         !  GET THE ADDRESS OF THE ARRAY HEADER
02040          JSB  =FETSVA          !  MAKE SURE IT'S ABSOLUTE IN CASE PGM MODE
02050 ZERCOM   LDMD R75,=PTR2-       !  GET THE POINTER ADDRESS FOR TRACING
02060          LDMI R65,=PTR2-       !  GET THE TOTAL SIZE OF THE ARRAY IN BYTES
02070          LDMI R54,=PTR2-       !  GET PAST THE MAX ROW AND MAX COL
02080          CLM  R50              !  CLEAR R50-57 FOR PUSHING ZEROES
02090 ZERLOP   SBM  R65,=10,0,0      !  KNOCK THE BYTE COUNT DOWN BY 8
02100          JNC  <10              !  JIF LESS THAN 8 TO GO
02110          STMI R50,=PTR2-       !  ELSE PUSH OUT 8 ZEROES
02120          JMP  ZERLOP           !  LOOP TIL LESS THAN 8 TO GO
02130 <10      ADM  R#,=10,0,0       !  GET BACK A NON-NEGATIVE COUNT
02140          JZR  ZERDON           !  JIF ZERO, DONE
02150 ZERLOP2  STBI R50,=PTR2-       !  ELSE PUSH OUT 1 ZERO
02160          DCM  R65              !  DECREMENT COUNT BY ONE
02170          JNZ  ZERLOP2          !  JIF NOT DONE
02180 ZERDON   RTN                   !  THAT'S ALL, FOLKS.
02190 ! **********************************************************
02200          BYT  32               !  CLASS IS 'SUBSCRIPT'
02210 REDIM1   LDMD R14,=BINTAB      !  GET BASE ADDRESS FOR LATER
02220          JSB  =ONEB            !  GET THE ONE SUBSCRIPT
02230          PUMD R46,+R6          !  SAVE IT ON RTN STACK
02240          POMD R65,-R12         !  GET THE ADDRESS OF THE ARRAY
02250          JSB  =FETSVA          !  MAKE SURE IT'S RELATIVE AND GET HEADER
02260          STBD R46,X14,SAVHED   !  SAVE HEADER FOR TRACING
02280          LDMI R65,=PTR2-       !  GET PAST THE TOTAL SIZE
02290          LDMI R64,=PTR2-+      !  GET THE MAX ROW AND MAX COL
02300          LDM  R76,R64          !  GET THE MAX COL INTO R76-77
02310          CMM  R76,=377,377     !  CHECK FOR 1-DIM (IF MAX COL=377,377)
02320          JZR  VECTOR1          !  JIF YES, IT'S A VECTOR
02330          LDMD R20,=PGMOPT      !  ELSE GET THE OPTION BASE
02340          JZR  OPTB1            !  JIF OPTION BASE 1
02350          ICM  R76              !  ELSE ADD ONE ELEMENT TO MAX COL
02360          ICM  R66              !        AND TO MAX ROW
02370 OPTB1    JSB  =INTMUL          !  GET THE NUMBER OF ELEMENTS IN ORIGINAL
02380 OPTB1-   CLM  R44              !  PREPARE FOR COMPARING
02390          POMD R36,-R6          !  GET THE NEW 1-DIM MAX ROW
02400          STM  R36,R44          !  SET FOR COMPARING
02410          TSM  R20              !  CHECK OPTION BASE
02420          JZR  OPT1             !  JIF OPTION BASE 1
02430          ICM  R44              !  ELSE INCREMENT NEW TOTAL ELEMENTS
02440 OPT1     CMM  R54,R44          !  IF NEW<=OLD THEN
02450          JCY  RED1OK           !      GOTO REDIM OK
02460          JSB  X14,ERRSET       !          ELSE ERROR (SET BPGM #)
02470          JSB  =ERROR+          !                     (REPORT ERROR)
02480          BYT  366              !                     ('DIM SIZE')
02490 RED1OK   CLM  R64              !  WE'RE REDIM-ING TO A VECTOR, SO
02500          DCM  R64              !      SET MAX COL TO 377,377
02510          LDM  R66,R36          !  GET MAX ROW
02520          STMI R64,=PTR2-+      !  STORE OUT TO ARRAY VARIABLE SPACE
02530          LDMI R65,=PTR2+       !  GET PTR2 BACK TO RIGHT SPOT
02540          LDBD R46,X14,SAVHED   !  RECOVER ARRAY HEADER BYTE
02550          JSB  X14,ZERCOM       !  GO ZERO THE ARRAY AND TRACE
02560          RTN                   !  DONE
02570 SAVHED   BSZ  1                !  HEADER BYTE SAVE AREA
02580 VECTOR1  CLM  R54              !  IF ARRAY WAS VECTOR IT'S EASY TO
02590          STM  R66,R54          !      CALCULATE THE TOTAL # OF ELEMENTS
02600          LDMD R20,=PGMOPT      !  BUT BE SURE YOU CHECK OPTION BASE
02610          JZR  OPTB1-           !      AND IF OPTION BASE 0
02620          ICM  R54              !          THEN BE SURE TO ADJUST COUNT
02630          JMP  OPTB1-           !  THEN FINISH
02640 ERRSET   LDBD R36,=ERRORS      !  HAVE ANY UNREPORTED ERRORS OCCURRED?
02650          JNZ  NOERR            !  JIF YES
02660          LDB  R36,=MYBP#       !  ELSE GET OUR BPGM #
02670          STBD R36,=ERRBP#      !  SET IF FOR THE SYSTEM
02680 NOERR    RTN                   !  DONE
02690 ! **********************************************************
02700          BYT  32               !  CLASS IS 'SUBSCRIPT'
02710 REDIM2   LDMD R14,=BINTAB      !  GET BASE ADDRESS FOR LATER
02720          JSB  =TWOB            !  GET THE NEW MAX ROW AND MAX COL
02730          PUMD R46,+R6          !  SAVE THEM ON THE RTN STACK
02740          PUMD R56,+R6          ! 
02750          POMD R65,-R12         !  GET THE ADDRESS OF THE ARRAY
02760          JSB  =FETSVA          !  MAKE SURE THAT IT'S ABSOLUTE
02770          STBD R46,X14,SAVHED   !  SAVE THE HEADER BYTE FOR TRACING
02790          LDMI R65,=PTR2-       !  GET PAST THE TOTAL SIZE
02795          PUMD R65,+R12         !  SAVE FOR LATER
02900          POMD R66,-R6          !  GET NEW MAX ROW
02910          POMD R76,-R6          !  GET NEW MAX COL
02920          PUMD R76,+R6          !  SAVE THEM AGAIN
02930          PUMD R66,+R6          ! 
02940          LDMD R20,=PGMOPT      !  IS OPTION BASE 1?
02950          JZR  OPTB3            !  JIF YES
02960          ICM  R76              !  ELSE ADJUST MAX COL
02970          ICM  R66              !     AND MAX ROW
02980 OPTB3    JSB  =INTMUL          !  CALCULATE TOTAL # OF ELEMENTS IN NEW
02981          STM  R54,R64          !  COPY FOR ADDING
02982          BCD                   !  FOR 4-BIT SHIFT
02983          LRB  R46              !  GET THE TYPE IN BITS 0-1
02984          BIN                   !  FOR ELSEWISE
02985          ANM  R46,=3,0         !  GET REAL,INTEGER, OR SHORT
02986          ADM  R46,R14          !  FOR INDEXING
02987          LDBD R36,X46,#BYTES   !  GET # BYTES/TYPE
02988 BYTE     ADM  R54,R64          !  ADD AGAIN
02989          DCB  R36              !  DEC BYTE/TYPE COUNT
02990          JNZ  BYTE             !  JIF NOT DONE
02991          POMD R64,-R6          !  RECOVER NEW ROW,COL
02999          POMD R45,-R12         !  RECOVER OLD TOTAL
03000          CMM  R45,R54          !  IS NEW<=OLD?
03010          JCY  RED2OK           !  JIF YES, OK
03020          JSB  X14,ERRSET       !  SET BPGM # FOR SYSTEM ERROR ROUTINE
03030          JSB  =ERROR+          !  REPORT ERROR
03040          BYT  366              !  'DIM SIZE'
03080 RED2OK   STMI R64,=PTR2-+      !  STORE THEM TO THE VARIABLE AREA
03090          LDMI R65,=PTR2+       !  MOVE THE PTR BACK TO COMMON SPOT
03100          LDBD R46,X14,SAVHED   !  RECOVER THE ARRAY HEADER BYTE
03110 !         JSB X14,ZERCOM         ! GO ZERO THE ARRAY AND TRAC
03120          RTN                   !  DONE
03150 #BYTES   BYT  7,2,3
03185 ! ********************************************************************
03190 BINTAB   DAD  104070           ! 
03200 CLOSE    EQU  51               ! 
03210 COMMA    EQU  54               ! 
03220 EQUALS   EQU  65               ! 
03230 ERRBP#   DAD  103371           ! 
03240 ERROR+   DAD  10220            ! 
03250 ERRORS   DAD  100123           ! 
03260 FETSVA   DAD  45305            ! 
03270 INTMUL   DAD  53673            ! 
03280 NARRE+   DAD  23461            ! 
03290 NUMVA+   DAD  22403            ! 
03300 NUMVAL   DAD  22406            !  LABEL DEFINITIONS
03310 ONEB     DAD  12153            ! 
03320 PGMOPT   DAD  104214           ! 
03330 PTR2-    DAD  177715           ! 
03340 PTR2-+   DAD  177717           ! 
03350 PTR2+    DAD  177716           ! 
03360 PSH45    DAD  24476            ! 
03370 SCAN     DAD  21110            ! 
03380 TWOB     DAD  56760            ! 
03390          FIN                   !  SOURCE TERMINATION
