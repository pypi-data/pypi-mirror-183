         ABS 20000
!
! **********************************
! BEGINNING OF THE TAPE ROUTINES
! **********************************
! READ TAPSTS (177410) BITS:
!   0 =1 IF CARTRIDGE PRESENT
!   1 =1 IF STALL
!   2 =1 IF ILIM (CURRENT OVER LIMIT)
!   3 =1 IF WRITE ENABLED, 0=WRITE PROTECT
!   4 =1 IF HOLE (OR END OF TAPE)
!   5 =1 IF NOT GAP, =0 IF GAP
!   6 =1 IF SAW MOTOR TACHOMETER TICK
!   7 =1 IF READY
! WRITE TAPSTS (177410) BITS:
!   0 TRACK NUMBER (0 OR 1)
!   1 =1 TO POWER UP TAPE, =0 TO POWER DOWN
!   2 =1 MOTOR ON, =0 MOTOR OFF
!   3 =1 IF MOTOR FWD (TO END), =0 IF BACK (TO START)
!   4 =1 HIGH SPEED, =0 LOW SPEED
!   5 =1 TO WRITE DATA
!   6 =1 TO WRITE SYNC
!   7 =1 TO WRITE GAP
! **********************************************************
! THE CAPRICORN DIRECTORY IS FORMATTED AS FOLLOWS:
!
! SIX BYTES OF NAME - WITH TRAILING BLANKS
! ONE BYTE FILE#    - DIRECOTRY SPACE IS LIMITED TO 42
!                     ENTRIES, SO ONE BYTE IS SUFFICIENT
! ONE BYTE TYPE     - EIGHT BITS ARE ORDERED AS FOLLOWS (MSB TO LSB)
!                   7  NEXT AVAILABLE FILE
!                   6  EMPTY FILE
!                   5  CAPRICORN (BASIC) FILE
!                   4  DATA FILE
!                   3  BPGM FILE
!                   2  UNUSED
!                   1  SOFT WRITE PROTECT
!                   0  NO DIRECOTRY NAME LIST
! TWO BYTES RECORDS/FILE - # PHYSICAL RECS PER FILE
! TWO BYTES BYTES/RECORD - FOR PRGM FILES = 256
!                      FOR DATA FILES = 256 IF NOT SPECIFIED BY THE USER
!
! THUS, 12 BYTES/FILE FOR 256 BYTES IS 21 FILES/DIRECTORY-RECORD (OF WHICH
! THERE ARE TWO) WITH 4 BYTES LEFT OVER ON EACH DIRECTORY RECORD.  THREE
! BYTES ARE USED FOR FL1TK1, THE 1ST FILE-RECORD NUMBER ON TRACK ONE.
! ONE BYTE IS "DIRSEG", INDICATING RECORD 0 OR 1 OF THE DIRECTORY.
!
! **********************************************************
! (I *THINK* THIS TO BE TRUE...)
! THE HP-85 TAPE HAS 2 DIRECTORY RECORDS (21 FILENAMES EACH) *and* THERE
! ARE TWO COPIES OF THE ENTIRE DIRECTORY (SO 4 RECORDS TOTAL).  THE SECOND
! COPY OF THE DIRECTORY IS NEVER USED BY THE SYSTEM, BUT IS THERE AS A
! BACKUP IN CASE THE MAIN DIRECTORY GETS DAMAGED AND SOMEHOW THE 2ND COPY
! SURVIVES, THEN IT COULD BE USED (VIA BPGM TOOLS) TO RECOVER THE FILES
! ON THE TAPE.
!
! (I *KNOW* THIS TO BE TRUE...)
! THE RAM BUFFERS WERE ONLY BIG ENOUGH TO READ IN *ONE* RECORD OF THE
! DIRECTORY AT A TIME.  HENCE, THE TAPE SOFTWARE HAS TO KEEP TRACK OF
! WHICH HALF OF THE DIRECTORY IS IN MEMORY AT A TIME, AND THIS COULD
! CAUSE THE TAPE TO "THRASH" IF A PROGRAM WAS ACCESSING TWO DIFFERENT
! FILES (ALTERNATELY) THAT HAPPENED TO BE IN DIFFERENT HALVES OF THE DIRECTORY.
!
! *****************************************
! REWIND ROUTINES
! *****************************************
RW       JSB  =FREV.           ! SEND TO TAPE
F2HOLE   JSB  =FND2HL          ! FIND TWO SUCCESSIVE HOLES
         JEZ  F2HOLE           ! JIF 1 HOLE
         LDB  R30,=302         ! WRITE+WGAP+STOP
         JSB  =CHSTS           ! SEND TO TAPE
         LDBD R31,=TAPSTS      ! GET STAT. FOR WPR CHK
         ANM  R31,=10          ! ISOLATE WRITE PROTECT
         STBD R31,=WENABL      ! SET FLAG
         JSB  =NOTST-          ! FORCE COMPLETE STOP
         LDB  R30,=16          ! START SFWD
         JSB  =CHSTS           ! ADD TRACK AND GO
         LDM  R36,=300,1       ! 14" OF TACKS
LGL      JSB  =TWOHL1          ! FIND HOLES
         JEN  LGL              ! JIF DOUBLE HOLE FOUND
LOADPT   JSB  =GAPS?           ! GET LOAD HOLE
         JEZ  LOADPT           !
         JSB  =WAIT.5          ! WAIT 1"
         JSB  =WAIT.5          !
         RTN                   !
!
REWIN1   JSB  =TRACK1          ! SET TRACK 1
REWIND   JSB  =RW              ! REWIND, NO STOP
         JMP  STOPTP           ! STOP
! **********************************************
! FIND+ SHOULD BE USED FOR WRITE ACCESSES
! IT READS A HEADER AND FALLS THROUGH BACKUP(RE
! **********************************************
FIND+    PUMD R56,+R6          ! SAVE DATA ADDRESS
         PUMD R22,+R6          ! SAVE DATA LENGTH
         LDBD R22,=TOTALR      ! SET BASE FOR READ ERRS
         STBD R22,=ERBASE      !
         JSB  =FIND-           ! FIND AND REWIND TO GAP
         POMD R22,-R6          ! RECOVER DATA LENGTH
         POMD R56,-R6          !   AND DATA ADDRESS
         JEN  XX               !
! **********************************************
! REWGAP SPEEDS UP FROM DATA IN REVERSE AND
! LOCATES THE GAP PRECEDING THE DATA
! **********************************************
REWGAP   CLE                   ! CLEAR FLAG FOR JMP
         JMP  OVRCLE           !
! **********************************************
! REWGA* SPEEDS UP FROM ANYWHERE (MOST LIKELY GA
! AND GETS IN FRONT OF A RECORD PRECEDING THE G
! ITS PROPER USE IS FROM LONG GAP AT THE END OF
! TAPE TO REPOSITION PRECEDING THE EOTRACK RECO
! **********************************************
REWGA*   CLE                   !
         ICE                   !
OVRCLE   JSB  =STOPTP          ! STOP ANY MOTION
         JSB  =SREV.           !
         CLB  R60              ! HOLE FLAG FOR THIS ROUT
         JEZ  INDATA           ! JIF FOR REWGAP
REWNGP   JSB  =GAPS?           ! GET GAP-NOGAP CONDITION
         JEZ  NOHREW           ! JIF NO HOLE
         JSB  =FEWGSB          ! REWGAP SUB
         JMP  REWNGP           !
!
NOHREW   JOD  REWNGP           ! IN GAP, FIND DATA
INDATA   JSB  =FNDGAP          ! FIND GAP
         JEZ  WAIT+H           ! JIF GAP, NO HOLE
         JSB  =FEWGSB          ! DO SUB
         JMP  INDATA           !
!
WAIT+H   JSB  =WAIT.5          ! WAIT .5" THEN STOP
STOPTP   LDB  R30,=2           ! STOP!! COMMAND
WG+S.    JSB  =CHSTS           ! ISSUE STOP COMMAND
NOTST-   ARP  R30              !
NOTSTP   LDBD R30,=TAPSTS      !
         ORB  R77,R#           ! OR STATUS TO R77
         JPS  NOTSTP           ! WAIT FOR COMPLETE STOP
         ANM  R77,=20          ! ISOLATE HOLES
XX       RTN                   !
!
FEWGSB   ICB  R60              ! INCR. HOLE COUNT
         JOD  NOT2             ! NOT TWO HOLES YET
         JSB  =REWIND          ! REWIND, IM LOST
         JSB  =ER73D           ! FILE SEARCH ERROR
NOT2     JSB  =TMOHOL          ! TIMOUT HOLE
         RTN                   !
!
FND2HL   JSB  =TPERR?          !
         LRB  R#               ! LOOK FOR HOLE
         JEV  FND2HL           ! NO HOLE, SO LOOP
         JSB  =TMOHOL          ! HOLE FOUND, TIMEOUT
         LDM  R36,=6,0         ! .218" BETWEEN HOLES
TWOHL1   JSB  =TPERR?          !
         LRB  R#               !
         JEV  NOTMOT           ! JIF NO HOLE
TMOHOL   LDB  R34,=6           ! ALLOW 6 TACHS PER DOUG
         CLE                   ! FLAG NO HOLE FOR 6 TACH
NOEDGE   JSB  =TPERR?          !
         LRB  R#               ! HOLE?
         JOD  TACH?            ! JIF STILL HOLE
         CLE                   !
         ICE                   ! SET NO HOLE SEEN
TACH?    LRB  R#               !
         LRB  R#               ! TACH EDGE?
         JEV  NOEDGE           ! JIF NO EDGE
         DCB  R34              ! TACH EDGE FOUND
         JNZ  NOEDGE           ! JIF NOT RUN OFF YET
         JEN  FINTMO           ! E=0 IS TAPE RAN OFF
!
         JSB  =ERROR           !
         BYT  65D              ! TAPE RUN OFF
!
TERROR   LDB  R30,=1           !
T+       STBD R#,=SCRTYP       ! SET TYPE FOR SCRATCH
         JSB  =TAPEXT          ! STOP TAPE, CRT POWER UP
         LDMD R6,=SAVER6       ! RESTORE RTN STACK
FINTMO   RTN                   ! EXIT E<>0
!
WPR?     LDBD R31,=WENABL      ! CHECK WRITE EN FLAG
         JNZ  WPREX            !
!
         JSB  =ERROR           !
         BYT  60D              ! WRITE PROTECTED
!
TERRNO   CLB  R30              !
         JMP  T+               ! TAPE ERROR, NO SCRATCH
!
NOTMOT   LRB  R#               !
         LRB  R#               ! LOOK FOR TACH EDGE
         JEV  TWOHL1           ! NO TACH EDGE
         DCM  R36              ! DECR. TACH COUNT
         JNZ  TWOHL1           ! TACH. COUNT #0, KEEP LO
         CLE                   ! NO 2ND HOLE BEFORE COUN
WPREX    RTN                   ! E=0 IMPLIES SINGULAR HO
!
! **********************************************
! TPERR? - READ/WRITE SUBROUTINES
! **********************************************
TPERR?   BIN                   !
         LDBD R30,=TAPSTS      ! GET TAPE STATUS
         JOD  SRVER?           ! NO CART INSERT ERROR
!
ER62D-   JSB  =ERROR           !
         BYT  62D              ! CARTRIDGE OUT
!
         JMP  TERROR           !
!
SRVER?   LRB  R#               ! LOOK FOR SERVO ERROR
         JEV  CRLIM?           ! NO CURRENT LIMITING
!
ER74D    JSB  =ERROR           !
         BYT  74D              ! SERVO ERROR: STALL
!
         JMP  TERROR           ! EXIT
!
CRLIM?   LRB  R#               ! IGNORE CURRENT LIMIT
         LRB  R#               ! SHIFT FOR NEXT GUY
         RTN                   !
! **********************************************
! THESE ROUTINES WILL GUARANTEE AN EXIT BY:
!   1) RECEIVING A BYTE READY  E=0
!   2) COUNTING 5.5" OF TACHS WITH NO BYTE READY SO E<>0
!   3) CARTRIDGE OUT OR SERVO ERROR  E<>0
!      #3 IS AN IMMEDIATE ERROR EXIT
! CALLING ROUTINES MAY CLEAR R77 AND OBTAIN THE "OR" OF
! ALL STATUS (FOR HOLE DETECTION) FROM THIS ROUTINE
! **********************************************
TPRBYT   LDM  R14,=RBYT        ! GET READ ROUTINE ADDR.
COMMON   BIN                   !
         CLE                   ! CLEAR ERROR FLAG
         LDB  R36,=260         ! SET UP R36
RBRDY?   LDBD R31,=TAPSTS      ! GET TAPE STATUS
         JPS  RNBRDY           ! NO BYTE READY
         JSB  X14,ZRO          ! JSB TO READ OR WRITE
         ORB  R77,R31          ! SAVE THE STATUS INFO
         RTN                   !
!
RNBRDY   ORB  R77,R31          ! SAVE STATUS INFO
         ANM  R31,=103         ! LOOK FOR TACH EDGE
         JEV  ER62D-           ! LSB =0 IS CART OUT
         DCB  R31              ! THROW LSB AWAY
         JRN  ER74D            ! SERVO ERROR
         JLZ  RBRDY?           ! NO EDGE
         DCB  R36              ! DECR. TACH COUNT
         JNZ  RBRDY?           !
         ICE                   ! COUNT =0, BEEN TOO LONG
         CLB  R71              !
         ICB  R71              ! SET LONG GAP INDICATOR
         RTN                   !
! **********************************************
!
TPWBYT   LDM  R14,=WBYT        ! GET WRITE ROUTINE ADDR.
         JMP  COMMON           !
! **********************************************
!
RBYT     LDBD R32,=TAPDAT      ! GET DATA
         RTN                   !
!
WBYT     STBD R32,=TAPDAT      ! SEND DATA
         RTN                   !
!
! **********************************************
! FILE SEARCH ROUTINE
! REGISTERS USED:
!   50 READ ERRORS
!   71 LONG GAP INDICATOR
!   72 FILE-REC SEARCH FLAG
!   73 1ST TIME THIS LONG GAP
!   74 DIRECTION 0-LEF 2-RT
!   75 #HEADERS READ & SLOW-FAST FLAG
!   76 # HOLES SEEN
!   77 HOLE SEEN
! **********************************************
FIND-    CLM  R70              !
         LDMD R45,=FL1TK1      ! 1ST REC TRACK 1
         JZR  NOTKNO           !
         CLM  R36              ! FOR FILE#
         LDB  R36,R45          ! MOVE FILE#
FINDS    LDMD R64,=CURREC      ! ENTRY FOR SIF SEARCH
         LDMD R66,=CURFIL      ! FOR COMPARE
         STM  R46,R34          ! MOVE REC#
         CMM  R64,R34          ! FIND FILE>=FL1TK1?
         JNG  NOTKNO           ! NOPE
         LDBD R64,=TRACK       ! YES, CHANGING TRACKS?
         JSB  =TRACK1          ! SET TRACK 1
         TSB  R64              ! LOOK FOR CHANGE NOW
         JNZ  TRKSET           !   NO CHANGE IF <>0
TREWIN   JSB  =REWIND          ! CHANGE TRACKS, MUST R
         JMP  TRKSET           !   READY TO GO
!
NOTKNO   JSB  =TRACK0          ! SET TRACK 0
TRKSET   CMB  R75,=6           ! TOO MANY HEADERS?
         JCY  CLEICE           ! JIF TOO MANY
         JSB  =SFWD.           ! FIND A GAP
         TSB  R77              ! HOLE DURING SPEED UP?
         JNZ  HOLDRP           ! JIF YES
         JSB  =FNDGAP          !
         JEN  HOLDRP           ! JIF HOLE
HEDR1    LDB  R22,=6           ! READ 6 BYTES
         LDM  R56,=TIC         ! SET UP ADDRESS
         LDB  R30,=16          ! READ COMMAND
         JSB  =CHSTS           ! START READING
         JSB  =REDBLK          ! READ 6 BYTES
         JEN  READOK           ! E<>0 IS LONG GAP
         JZR  HEDFND           ! JIF CHECKSUM OK
         JSB  =ERCHK           ! CHECK READ ERRORS
         JSB  =REWGAP          ! REWIND TO GAP, TRY AGAIN
         JMP  HEDR1            !
!
HEDFND   LDBD R35,=TIC         ! UPPER BYTE OF FILE#
         ANM  R35,=7           ! ONLY 3 BITS COUNT
         LDBD R34,=HEDAD2      ! LOWER BYTE FILE#
         SBMD R34,=CURFIL      ! COMPUTE DIST. DIRECTION
         JNZ  WRGFIL           ! NOT AT FIND FILE NOW
         LDBD R35,=HEDAD3      ! GET RECORD #
         ANM  R35,=17          ! 4 BITS COUNT
         LDBD R34,=HEDAD4      ! GET LOWER BYTE
         SBMD R34,=CURREC      ! COMPUTE # REC GAPS
         JNZ  WRGREC           ! NOT THERE YET
         RTN                   ! FOUND FILE!!!!
!
READOK   TSB  R71              ! LONG GAP??
         JNZ  GAPDRP           ! JIF GAP
HOLDRP   DRP  R76              ! SET DRP FOR HOLE
TSTFLG   ICB  R#               ! INCR GAP OR HOLE COUNT
         JEV  GETBAK           ! JIF 2 TO REWIND - ERROR
         JSB  =REWGA*          ! GET IN FRONT OF RECORD
         CLB  R71              ! CLEAR GAP INDICATOR
         JMP  TRKSET           !
!
GAPDRP   DRP  R73              ! SET DRP FOR GAPS
         JMP  TSTFLG           !
!
GETBAK   JSB  =REWIND          !
CLEICE   CLE                   ! EXIT!!
         ICE                   !
         RTN                   !
! **********************************************
! WRONG RECORD SEARCH
! **********************************************
WRGREC   SAD                   ! SAVE STATUS
         ICB  R72              ! FLAG RECORD SEARCH
         LDM  R46,=FNDSGP      ! 1" GAP SEARCH
         PAD                   ! RESTORE STATUS
         JNC  REC.RT           ! JIF RECORD TO RIGHT
         JSB  =STOPTP          ! STOP IF LEFT
         LDB  R30,=6           ! REVERSE STATUS WORD
         JMP  RECSRC           ! JMP RECORD SEARCH
!
REC.RT   NCM  R34              ! # RECS TO RIGHT
         JZR  TRKSET           ! IF 0, I'M THERE
         LDB  R30,=16          ! FORWARD STATUS WORD
RECSRC   CMM  R34,=10,0        ! >8 RECS AWAY?
         JCY  FAST?            ! JIF YES
         ICB  R75              ! SET SO EXSRCH DOES REWND
         JMP  GOSRC            ! SLOW FWD OR REV
!
FAST?    CMB  R75,=2           ! BEGAN OUTSIDE FILE?
         JCY  GOSRC            ! JIF NO
         JMP  SETFST           ! SET FAST
! **********************************************
! WRONG FILE SEARCH
! **********************************************
WRGFIL   SAD                   ! SAVE STATUS
         LDM  R46,=FNDLGP      ! 2.5" GAP SEARCH
         PAD                   ! RESTORE STATUS
         JNC  FIL.RT           ! JIF FILE TO RIGHT
         JSB  =STOPTP          ! STOP IF LEFT
         LDB  R30,=6           ! REVERSE STATUS WORD
         LDBD R42,=TIC         ! ADJUST COUNT MAYBE
         JNG  FILSRC           ! JIF COUNT OK
BMP34    ICM  R34              ! INCR. GAP COUNT
         JMP  FILSRC           ! JMP FILE SEARCH
!
FIL.RT   LDB  R30,=16          ! FORWARD STATUS WORD
         TCM  R34              ! ADJUST COUNT
         LDBD R42,=TIC         !
         JNG  BMP34            ! ADJUST IF FILE HEADER
FILSRC   TSB  R75              ! 1ST TIME HERE?
         JNZ  GOSRC            ! JIF NO
! **********************************************
SETFST   ADB  R30,=20          ! MAKE SEARCH FAST
GOSRC    JSB  =WTPSTS          ! SEND STATUS WITH SPEED
MOVE     JSB  X46,ZRO          ! FIND FILE GAPS
         JEZ  DNCNT            ! FILE GAP FOUND IF E=0
         ICB  R75              ! SET FOR SLOW NEXT TIME
         TSB  R71              ! EVD GAP?
         JNZ  GAPDRP           ! JIF GAP
HOLE     TSB  R74              ! HOLE FOUND DURING GAP S
         JNZ  HOLDRP           ! JIF RIGHT
         ICB  R76              ! BUMP HOLE COUNT
         JEV  GETBAK           ! ERROR IF 2
         JSB  =REWIND          ! ELSE REWIND
TRKGTO   GTO TRKSET            ! LOOP IF 1
!
DNCNT    DCM  R34              ! COUNT DOWN FOR FILE GAP
         JZR  EXSRCH           !
         TSB  R72              ! RECORD SEARCH?
         JZR  MOVE             !
         CMM  R34,=10,0        ! GETTING CLOSE?
         JCY  MOVE             ! NOT YET
         LDB  R30,R74          ! GET DIRECTION
         LLB  R30              !
         LLB  R30              ! DIRECTION BIT IN PLACE
         ADB  R30,=6           ! MAKE IT A MOVER
         JSB  =CHSTS           !
         JMP  MOVE             !
!
EXSRCH   TSB  R74              ! RIGHT?
         JNZ  WHOA             ! <>0 IS YES
         TSB  R72              ! RECORD SEARCH?
         JNZ  RWNG             ! LEFT&YES, DO REWNGP
         TSB  R75              ! FAST?
         JZR  WHOA             !
RWNG     JSB  =REWNGP          ! SLOW, FIND GAP
WHOA     ICB  R75              ! SET FOR SLOW NEXT TIME
         JSB  =STOPTP          !
         TSB  R77              ! HOLE?
         JNZ  HOLE             ! JIF YES
         JMP  TRKGTO           ! NO HOLE, READ HEADER
!
ERCHK    LDBD R50,=TOTALR      ! LOAD SOFT READ ERRORS
         ICB  R50              !
         STBD R50,=TOTALR      ! BUMP TOTAL
         SBBD R50,=ERBASE      ! SUBTRACT BASE #ERRORS
         CMB  R50,=3           ! ALLOW 3
         JNZ  SURVIV           ! JIF SURVIVED
!
         JSB  =ERROR           !
         BYT  70D              ! READ ERROR
!
         JSB  =TERROR          ! EXIT
SURVIV   RTN                   !
! **********************************************
! GAP SEARCH AND TRACK SET STUFF
! **********************************************
GAPS?    CLE                   ! CLEAR TO NOTE HOLE
         JSB  =TPERR?          !
         LRB  R#               ! LOOK FOR GAP
         JEV  GAPS1            !
         ICE                   ! NOTE THE HOLE!
         LDB  R77,=20          ! SET HOLE SEEN
         DRP  R30              !
GAPS1    LRB  R#               !
GAPRTN   RTN                   !
! *****************************************************************
FNDGAP   JSB  =GAPS?           !
         JEN  FNDRTN           !
         JEV  FNDGAP           ! LOOP TILL GAP HIGH
FNDRTN   RTN                   !
! *****************************************************************
! FIND LONG GAP RETURNS THE FOLLOWING:
!   1) E=0 FOR AN IFG
!   2) E<>0 FOR HOLE FOUND
!   3) E<>0 AND R71<>0 FOR 12.5" GAP FOUND
! *****************************************************************
FNDSGP   JSB  =FNDGAP          ! FIND A GAP
         JEN  HOLEIN           ! HOLE FOUND
         LDB  R36,=300         ! 6 INCHES OF TACHS
LGLOOP   JSB  =TPERR?          !
         LRB  R#               !
         JOD  HOLEIN           ! HOLE DURING GAP
         LRB  R#               !
         JEV  OUTTST           ! NO MORE GAP
         LRB  R#               ! LOOK FOR TACH EDGES
         JEV  LGLOOP           ! NO TACH EDGE
         DCB  R36              ! DECR COUNTER
         JNZ  LGLOOP           ! KEEP LOOKING AT GAP
         ICB  R71              ! SET LONG GAP FLAG
HOLEIN   ICE                   ! INCR FOR 12" GAP/HOLE
         RTN                   ! RETURN WITH E<>0
!
OUTTST   CMB  R36,=230         ! 300-50=230 TACHS, ONLY 1" GONE BY IS LIT
         RTN                   ! EXIT
! *****************************************************************
FNDLGP   JSB  =FNDSGP          ! FIND LONG GAPS ROUTINE
         JEN  LGPRTN           ! EXIT WITH PROBLEMS
         JCY  FNDLGP           ! IFG WILL COUNT DOWN
LGPRTN   RTN                   ! PAST 230!!!
! *****************************************************************
TRACK0   CLB  R30              !
T0       STBD R#,=TRACK        ! TRACK 0
STSECU   RTN                   !
!
TRACK1   LDB  R30,=1           ! TRACK 1
         JMP  T0               !
!
! *****************************************************************
! STORE BIN RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
STORB.   STMD R6,=SAVER6       ! FOR ERRORS
         LDB  R56,=10          ! BPGMTY TYPE
         STBD R56,=FILTYP      ! SET FILE TYPE
         JSB  =GETNAM          ! GET THE NAME
         LDMD R56,=BINTAB      ! 0 IF NO BINARY
         JNZ  GETEND           ! GOT START, GET END
!
         JSB  =ERROR+          !
         BYT  50D              ! NO BINARYS
!
GETEND   LDMD R76,=LWAMEM      ! LAST WORD BINARY
         ICM  R76              ! LAST BYTE+1
         JMP  STORB-           ! GO STORE IT
!
! *****************************************************************
! STORE RUNTIME
! *****************************************************************
         BYT  141              ! ATTRIBUTES
STORE.   LDB  R0,=200          ! TEST STORE PROTECT
         JSB  =SECUR?          !
         JEN  STSECU           ! JIF SECURED FOR STORE
         LDB  R30,=CAPRTY      ! SET CAPR TYPE FILE
         STBD R30,=FILTYP      ! STORE TYPE
         STMD R6,=SAVER6       ! SAVE FOR ERROR RTN
         JSB  =GETNAM          ! GET FILE NAME
         JSB  =TAPINT          ! TAPE INIT B4 ALLOC SO USERS DONT PANIC
         JSB  =INIPGM          !
         JSB  =ST240+          !
         JSB  =TSTALO          ! ALLOCATED?
         JEN  NREPOR           ! JIF ALREADY THERE
         JSB  =ALLOC           ! ALLOCATE B4 STORE FOR FASTER LOAD/RUN
         JEZ  NREPO-           ! JIF ALLOCATE OK
         JSB  =REP.1           ! REPORT ALLOC ERROR
         JSB  =ST240+          ! RESET R17
         JMP  NREPOR           !
!
NREPO-   JSB  =INIVAR          ! ALLOC GOOD, INIT VARS.
NREPOR   LDMD R56,=FWCURR      ! START OF PGM
         LDBD R56,X56,P.TYPE   ! CHECK FOR COMMON
         JPS  NOCOMN           !
         JSB  =FXDIR           ! DEALLOCATE PGMS WITH COMMON
         LDMD R12,=NXTMEM      !
NOCOMN   STMD R12,=STSIZE      !
         LDMD R56,=FWCURR      ! GET START OF PGM
         LDMD R76,X56,P.LEN    ! GET PGM LENGTH
         BIN                   !
         ADM  R76,R56          ! COMPUTE LAST DATA ADDR
         LDBD R67,X56,P.TYPE   !
         ANM  R67,=40          ! ALLOCATION BIT
         JZR  STORB-           ! JIF NOT ALLOCATED
         ADMD R76,R76          ! GET DATA LENGTH
STORB-   STMD R76,=LSTDAT      !
         STMD R56,=NXTDAT      ! SET 1ST WORD TO STORE
         JSB  =TAPINT          !
         JSB  =WPR?            ! CHECK WRITE PROTECT
         JSB  =DSCAN           ! SCAN DIR. FOR NAME
         JEZ  GOTNAM           ! FOUND NAME
         JSB  =MTSCAN          ! LOOK FOR EMPTYS
         JMP  MT?              ! EMPTY OR MARK?
!
BADLEN   STMD R36,=AVAILP      ! KEEP OLD DIR ADDR
         LDBD R36,=DIRSEG      !
         STBD R36,=OLDSEG      ! KEEP OLD SEGMENT
         JSB  =MTSCAN          ! LOOK FOR EMPTYS
         STMD R36,=NEWAVA      ! KEEP NEW AVAIL LOC
         LDBD R36,=DIRSEG      !
         SBBD R36,=OLDSEG      !
         JZR  SAMSEG           ! OLD AND NEW IN SAME SEG
         JSB  =REDOPS          ! GET OLD SEGMENT
         JSB  =FIXOLD          ! MAKE ENTRYS FOR OLD
         JSB  =FIND+W          ! REWRITE THE SEGMENT
         JSB  =REDOPS          ! RESTORE NEW SEGMENT
         JMP  MT?-             !
!
SAMSEG   JSB  =FIXOLD          ! MAKE ENTRYS FOR OLD
MT?-     LDMD R36,=NEWAVA      !
MT?      LDBD R30,=MTFLAG      ! EMPTY OR MARK?
         JNZ  EMTEE            !
         GTO MARK.S            !
!
EMTEE    LDMD R42,=SAVNAM      !
         STMD R42,R36          ! MAKE DIRECTORY ENTRY
         LDBD R42,=FILTYP      ! SET TYPE
         STBD R42,X36,D.TYPE   !
         PUMD R36,+R6          ! SAVE DIRECTORY ADDR
         JSB  =FIND+W          ! REWRITE THE RECORD
         POMD R36,-R6          ! RESTORE DIR. ADDR.
         JMP  TYPOK            ! RE-CALC LEN, SET R/FILE
! *****************************************************************
GOTNAM   LDBD R33,X36,D.TYPE   ! DO TYPE CHECK
         LRB  R33              ! CHECK SOFT W/PROTECT
         JOD  ER22D+           ! JIF PROTECTED
         LLB  R33              ! SHIFT BACK FOR AND
         ANMD R33,=FILTYP      ! PROGRAM TYPE FILE?
         JNZ  TYPOK            !
!
ER68D    JSB  =ERROR           !
         BYT  68D              ! FILE TYPE
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
ER22D+   JSB  =ER22D           ! SOFT W/PROTECT
TYPOK    JSB  =GETCNT          ! GET PROGRAM LENGTH
         LDMD R34,X36,D.#R/F   ! GET DIR. FILE LENGTH
         STMD R34,=R/FILE      ! FOR RESTORE
         SBM  R34,R32          ! FILE BIG ENOUGH?
         JNC  BADLEN           ! NOPE
RESTOR   JSB  =FET44           ! FETCH FILE# TO 44
DO.BUF   JSB  =GETBUF          ! GET SOME PGM
         JEZ  NOBUFR           ! DONE IF E=0
         JSB  =WRTRND          ! WRITE RANDOM RECORD
         JMP  DO.BUF           !
!
NOBUFR   LDMD R30,=CURREC      !
         CMMD R30,=R/FILE      ! NEED TO WRITE EMPTY?
         JCY  TAPEXT           !
         CLB  R30              !
         JSB  =WRTRN-          ! WRITE RANDOM EMPTY
TAPEXT   JSB  =CRTPUP          ! POWER UP CRT
         STBI R#,=TINTEN       ! RE-ENABLE INTERRUPTS
         RTN                   !
! *****************************************************************
! RESTORE OF FILE ROUTINE COMPLETE
! *****************************************************************
!
! *****************************************************************
! MARK TAPE ROUTINE
! *****************************************************************
MRKFIX   JSB  =MFXSUB          !
         JSB  =FET46           ! FILE# TO R46
SAVE#    PUMD R46,+R6          ! SAVE FILE#
         ADM  R46,=1,200       ! NEXT FILE# AND AVAIL. B
         ADM  R36,=14,0        ! BUMP DIR. POINTER
         PUMD R36,+R6          ! SAVE POINTER
         CMM  R36,=DIREND      !
         JCY  TOFAR            ! OUT OF DIR SPACE
         STMD R40,R36          ! R40-45 IS GARBAGE
TOFAR    JSB  =FIND+W          ! FIND IT, WRITE IT
         POMD R36,-R6          ! GET POINTER BACK
         CMM  R36,=DIREND      ! DID I OVF BACK THERE?
         JNC  NOOVF2           ! NOPE
         LDBD R36,=DIREND      ! OVF ON 1, CANT DO MORE
         JNZ  NOOVF2           !
         LDM  R36,=DIRECT      !
         SBM  R36,=14,0        ! SET UP FOR ABOVE
         LDB  R46,=1           !
         STBD R46,=DIREND      !
         POMD R46,-R6          ! POP FILE # OFF R6
         JMP  SAVE#            !
!
NOOVF2   POMD R20,-R6          ! POP FILE#
         STMD R20,=ROMEND      !
         RTN                   !
! *****************************************************************
! MARK AND WRITE AND NEW FILE
! *****************************************************************
MARK.S   LDBD R41,=FILTYP      ! PROGRAM TYPE
         JSB  =GETCNT          ! R32 = LENGTH
         LDM  R30,=0,1         ! 256 BYTES
         JSB  =MRKFIX          ! FIX DIRECTORY
MRKGET   CLM  R34              !
         STMD R34,=CURREC      ! CLEAR CURREC
         JSB  =FIND+           ! FIND THE FILE
         JEZ  MARKOK           !
JSB131   JSB  =ER73D           ! NO FILE FOUND
MARKOK   JSB  =GETBUF          ! GET A BUFFER
         LDB  R30,=56          ! REWRTP - REWRITE THIS RECORD
MARKO+   LDM  R36,=IFGLEN      ! SET UP FOR IFG GAP
M.LOOP   STMD R36,=GAPLEN      ! SAVE GAPLEN
REDO     JSB  =WRTREC          ! DO THE RECORD
         JEN  JSB131           ! FAILURE TO SYNC
         JSB  =WSLACK          !
         JSB  =GETBUF          ! GET NEXT DATA DURING SL
         LDBD R31,=TAPSTS      ! GET HOLE ONE MORE TIME
         ANM  R31,=20          ! ISOLATE IT
         ORB  R77,R31          !
         LDMD R36,=GAPLEN      ! SET GAP LEN
         JSB  =IRG             ! DO THE GAP
         TSB  R77              ! HOLE DURING DATA AND GAP?
         JZR  STMOR?           ! NO, CHECK FOR CONTINUE
         LDBD R77,=TRACK       ! CHECK FOR VALID TRACK
         JZR  REC#>0           !
         JSB  =REWIND          ! OUT OF ROOM
!
         JSB  =ERROR           !
         BYT  65D              ! END OF TAPE
!
         CLM  R46              !
         PUMD R46,+R6          ! FOR PURGE "XX",0
         GTO PURJE             !
!
! *****************************************************************
! THIS IGNORES THE RARE POSSIBILITY OF A FILE EXACTLY ENDING WHEN
! THE HOLE OCCURS.  THE CODE REQUIRED TO ALLOW THIS CASE IS NOT
! WORTH THE GAINS, SO IT'S AN ERROR.
! *****************************************************************
REC#>0   JEZ  FILDUN           ! JIF DONE
         LDM  R36,=IRGLEN      !
         STMD R36,=GAPLEN      !
         JSB  =SETFL1          ! EOTRAK,REW,FIX DIR.,WGAP
         JMP  REDO             !
!
FILDUN   JSB  =SETFL1          ! EOTRAK,REW,FIX DIR.,WGAP
         JMP  F1EXIT           ! DO THE NEXT HDR.
!
STMOR?   LDB  R30,=116         ! MARK
         LDM  R36,=IRGLEN      !
         JEN  M.LOOP           ! NO HOLE SEEN IF HERE
F1EXIT   JSB  =DO.F1           ! DO THE NEXT HDR.
F1EX+    JSB  =REWGA*          !
         JSB  =TAPEXT          !
         RTN                   !
!
DO.F1    LDMD R34,=CURFIL      !
         ICM  R34              ! ENTRY POINT FOR SCRATCH
         STMD R34,=CURFIL      !
         CLM  R22              ! NO BYTES
         STMD R22,=CURREC      !
         STBD R22,=FILTYP      ! EMPTY TYPE
STRTT1   LDB  R30,=116         ! MARK
         JSB  =WRTREC          !
         CLM  R24              ! 408 BYTES
         JSB  =WSL1-           !  OF SLACK
         TSB  R77              !
         JZR  EOTRAK           !
         LDBD R36,=TRACK       ! WHAT TRACK?
         JZR  NOWARN           !
         JSB  =EOTRAK          !
         JMP  F1EX+            ! BACK UP
!
NOWARN   JSB  =SETFL1          ! EOTRAK,REW,FIX DIR., WGAP
         JMP  STRTT1           !
!
EOTRAK   LDM  R36,=220,1       ! EOTLEN = 12.5"
         JSB  =IRG             ! DO THE GAP
         LDB  R30,=312         ! STOP+WGAP
         JSB  =WG+S.           !
         RTN                   !
!
! *****************************************************************
! SET 1ST FILE ON TRACK 1
! *****************************************************************
SETFL1   LDMD R44,=CURFIL      !
         PUMD R44,+R6          ! PUSH TO STACK
         LDB  R45,R44          ! MOVE LSB
         STMD R45,=FL1TK1      ! SET FL1 TRACK 1
         STMD R45,=ERTEMP      !   AND TEMPORARY
         PUMD R22,+R6          ! SAVE BUFFER LENGTH
         PUMD R56,+R6          ! SAVE BUFFER ADDR.
         JSB  =EOTRAK          ! WRITE EOT
         JSB  =REWIND          ! REWIND TRACK 0
         JSB  =DOBOTH          ! WRITE BOTH DIR. RECS.
         JSB  =REWIN1          !
         POMD R56,-R6          ! RESTORE BUFFER ADDR.
         POMD R22,-R6          ! RESTORE BUFFER LENGTH
         POMD R44,-R6          ! RESTORE FILE,REC#
         STMD R44,=CURFIL      !
         LDM  R36,=IRGLEN      ! DO START GAP
         JSB  =IRG             !
         LDB  R30,=116         ! MARK
         RTN                   !
!
DOBOTH   JSB  =FIND+W          ! UPDATE CURRENT SEGMENT
         JSB  =REDOPS          ! GET OTHER SEGMENT
         LDMD R45,=ERTEMP      ! GET FL1TK1 BACK
         STMD R45,=FL1TK1      ! SET FL1TK1
         JSB  =FIND+W          !
         JSB  =REDOPS          ! GE BACK TO ORIGINAL
         RTN                   !
!
! *****************************************************************
! DIRECTORY SCAN
! THIS ROUTINE SCANS THE DIRECTORY FOR NAMES IN SAVNAM.  IT RETURNS
!    E=0 FOR NAME FOUND
!    E=1 FOR NO NAME, SPACE REMAINS
!    R36 IS THE POINTER INTO THE DIRECTORY
! *****************************************************************
DSCAN    CLB  R36              ! CLEAR USED AND AVAIL
         STBD R36,=USED?       !
DOTHER   LDM  R36,=DIRECT      !
DSCAN1   LDBD R52,X36,D.TYPE   ! GET TYPE
         JNG  LAVAFL           ! FOUND LAVAIL FILE
         LLB  R52              ! CHECK EMPTY
         TSB  R52              !
         JNG  BUMP             ! JIF EMPTY
         LDMD R52,R36          ! GET THE NAME
         CMMD R52,=TEMP22      ! COMPARE NAMES
         JNZ  BUMP             !
         CLE                   ! NAME FOUND!!!
         RTN                   !
!
BUMP     ADM  R36,=14,0        ! BUMP DIR. POINTER
         CMM  R36,=DIREND      ! OUT OF DIR SPACE?
         JNC  DSCAN1           ! NOT YET
CKUSED   LDBD R36,=USED?       ! OTHER SEGMENT USED?
         JZR  GETSEG           !
AVALEX   CLE                   !
         ICE                   ! NO NAME FOUND
         RTN                   !
!
GETSEG   ICB  R#               !
         STBD R#,=USED?        !
         JSB  =REDOPS          !
         JMP  DOTHER           !
!
LAVAFL   LDBD R36,=DIRSEG      !
         JZR  AVALEX           ! AVAIL FOUND, SEG 0
         JMP  CKUSED           !
!
! *****************************************************************
! SCAN FOR EMPTYS
! THIS ROUTINE SCANS THE DIRECTORY STARTING AT RECORD 0 LOOKING FOR
! EMPTYS (THAT ARE BIG ENOUGH) OR NEXT AVAILABLE DIRECTORY LOCATION.
! NEITHER OF THESE FOUND IS AN ABORT.
!   E=0 AND MTFLAG=0 FOR MARK
!   E<>0 AND MTFLAG<>0 FOR EMPTY AND RESTORE
!   RETURNS R36 POINTING @ NXT AVAIL
! *****************************************************************
MTSCAN   CLM  R46              ! TOTAL TAPE RECS.
         LDBD R36,=DIRSEG      ! GET CUR. DIR. SEGMENT
         JZR  NXTSEG           ! WE WANT 0
ESCAN1   PUMD R46,+R6          ! SAVE RECORD COUNT
         JSB  =REDOPS          ! IN 1, LOAD 0
         POMD R46,-R6          ! RESTORE RECORD COUNT
NXTSEG   LDM  R36,=DIRECT      ! SET ADDRESS
         JSB  =GETCNT          ! GET PROGRAM LENGTH
NXTONE   LDBD R52,X36,D.TYPE   ! CHECK TYPE
         CLE                   !
         JNG  USEIT            ! USE AVAIL
         LDMD R34,X36,D.#R/F   ! ACCUMULATE LENGTH
         ADM  R46,R34          !
         LLB  R52              !
         TSB  R52              ! EMPTY?
         JPS  NOEMPT           ! JIF NO
         DCE                   !
         SBM  R34,R32          !
         JCY  USEIT            ! USE EMPTY AND RESTORE
NOEMPT   ADM  R36,=14,0        ! BUMP DIR. POINTER
         CMM  R36,=DIREND      !
         JNC  NXTONE           ! OVF DIRECTORY?
         LDBD R36,=DIRSEG      !
         JZR  ESCAN1           ! OVF IN 0 OK
!
         JSB  =ERROR           !
         BYT  61D              ! >42 FILES (DIRECTORY OVF)
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
USEIT    CLB  R30              !
         BCD                   !
         ELB  R30              !
         STBD R30,=MTFLAG      !
         ERB  R30              !
         BIN                   !
WRTRTN   RTN                   !
!
! *****************************************************************
! STORE SUBROUTINES
! *****************************************************************
FIND+W   CLM  R44              ! SET DIRECTORY ADDR.
         STBD R44,=D2HOOK      ! FORCE 1ST HALF DIRECTORY
         LDBD R46,=DIRSEG      !
         STMD R44,=CURFIL      !
         JSB  =FINDW-          ! WRITE THE 1ST SEGMENT
         LDMD R46,=CURREC      !
         ICM  R46              ! ADD 2 FOR SPARE DIRECTORY
         STMD R46,=CURREC      !   (WRTREC ADDED 1 ALREADY)
FINDW-   LDM  R56,=DIRECT      ! SET ADDRESS
         CLM  R22              ! SET LENGTH
         STBD R22,=VALIDD      ! DECLARE INVALID DIRECTORY
         LDBD R30,=FILTYP      ! SAVE FILE TYPE
         PUBD R30,+R6          !
         LDB  R30,=40          !
         JSB  =WRTRN-          ! RANDOM WRITE
         JSB  =SETVAL          ! SET DIRECTORY VALID
         POBD R30,-R6          ! RESTORE FILE TYPE
         STBD R30,=FILTYP      !
         RTN                   !
!
! USERS OF WRTRND MUST SET:
!   R22 TO LENGTH
!   R56 TO ADDRESS
!   FILTYP TO TYPE
!
WRTRN-   STBD R#,=FILTYP       !
WRTRND   JSB  =FIND+           ! FIND THE RECORD
         JEN  ER73D            ! NO FILE FOUND
         LDB  R30,=56          ! REWRTP
         JSB  =WRTREC          ! WRITE THE RECORD
         JSB  =STOPTP          !
         LDB  R31,=4           ! PAUSE FOR 64 MS
         JSB  =CNTRTR          ! TO LET HEAD BIAS CHANGE
         JEZ  WRTRTN           !
!
ER73D    JSB  =ERROR           !
         BYT  73D              ! SEARCH (FIND ERROR)
!
         LDMD R30,=CURFIL      !
         JZR  ER73D*           !
TEXIT    JSB  =TERROR          ! EXIT
ER73D*   JSB  =TERRNO          ! NO SCRATCH TYPE
WRTREC   LDMD R26,=CURFIL      ! GET CURRENT RECORD#
         LDB  R46,=40          ! ALL 85 REC'S GET RESERV
         LDBD R47,=FILTYP      !
         JZR  ADTYPE           ! JIF EMPTY
         LDB  R46,=70          ! RESERVE+NON-EMPTY
ADTYPE   LDMD R24,=CURREC      !
         JNZ  NOT0R            ! JIF NOT ZERO
         ADB  R46,=200         ! ADD FILE I.D. BIT
NOT0R    ORB  R27,R46          ! INCLUDE BITS
         LDB  R46,=20          ! RESERVE FIELD = 1
         ORB  R25,R46          ! ALL 85 REC'S GET FIELD
         LDB  R23,=377         ! ALWAYS 256 AVAILABLE
WRTRC+   CLM  R46              ! FOR CHECKSUM
         DCB  R22              ! DECR. BYTE COUNT
         LDB  R32,=1           ! SYNC LSB
         STBD R32,=TAPDAT      ! SEND TO TAPE CONTROL
         JSB  =CHSTS           ! WRITE COMMAND
         CLB  R77              ! CLEAR TO NOTE HOLE
         LDB  R0,=27           ! INDEX FOR FILE MSB
NXTHED   LDB  R32,R*           ! GET BYTE INDEXED VIA R0
         JSB  =TPWBYT          ! SEND IT
         JEN  BODRTN           ! WRITE HEAD EARLY RTN
! *** E<>0 MEANS NEVER GOT SYNC'D UP ***
         DCB  R0               ! DECR INDEX
         LDB  R32,R*           ! GET NEXT BYTE
         JSB  =TPWBYT          ! SEND IT
         ADM  R46,R*           ! ACCUMULATE CHECKSUM
         DCB  R0               ! DECR INDEX
         CMB  R0,=21           ! LAST SET?
         JNZ  NXTHED           !
         JSB  =SNDSUM          ! SEND CHECKSUM
         LDBD R21,=FILTYP      ! CHECK FOR EMPTY
         JZR  WAIT2B           ! DONE IF 0
         LDMD R24,=CURREC      !
         ICM  R24              ! INCR. FOR NXT REC HED
         STMD R24,=CURREC      ! STORE NEXT RECORD #
         ICB  R22              ! INCR. FOR BYTE COUNT
         STB  R22,R23          ! SAVE FOR SLACK
         CLM  R46              ! CLEAR FOR CHECKSUM
RB1      POBD R32,+R56         ! GET NEXT BYTE
         STB  R32,R45          ! SET UP FOR CHECKSUM
         JSB  =TPWBYT          ! WRITE A BYTE
         POBD R32,+R56         ! GET SECOND BYTE OF PAIR
         STB  R32,R44          ! SET UP CHECKSUM BYTE2
         ADM  R46,R44          ! ACCUMULATE TO CHECKSUM
         JSB  =TPWBYT          ! WRITE THIS BYTE
         DCB  R22              ! DECR. FOR 1ST BYTE
         JZR  CHEKSM           !
         DCB  R22              ! DECR. FOR 2ND BYTE
         JNZ  RB1              !
CHEKSM   JSB  =SNDSUM          ! SEND CHECKSUM
WAIT2B   JSB  =TPWBYT          ! POSTAMBLE
         JSB  =TPWBYT          ! POSTAMBLE
         JSB  =TPWBYT          ! POSTAMBLE
! *** 3 BYTE READY'S ARE NECESSARY TO ALLOW THE LAST BYTE TO
! *** ARRIVE COMPLETELY ON TAPE
BODRTN   ANM  R77,=20          ! ISOLATE HOLE FLAG
         RTN                   !
!
! *****************************************************************
SNDSUM   LDB  R32,R47          ! MSB OF CHECKSUM
         JSB  =TPWBYT          !
         LDB  R32,R46          ! LSB OF CHECKSUM
         JSB  =TPWBYT          !
         RTN                   !
!
WSLACK   LDM  R24,=56,0        ! 302-256=46(DEC.)
         LDBD R33,=FILTYP      ! CALC HOW MUCH SLACK
         CMB  R33,=20          ! DATATY (DATA TYPE?)
         JZR  WSL1             ! JIF YES
         CLM  R24              !
         LDB  R24,R23          ! MOVE BYTE COUNT
         DCB  R24              !
         ICM  R24              ! 0->377->0,1
WSL1-    SBM  R#,=230,1        ! TOTAL FOR STORE IS 408
         TCM  R#               !
WSL1     LDB  R32,=377         ! ALL ONE'S
WSL11    JSB  =TPWBYT          ! SEND A BYTE
         DCM  R24              ! DECR. COUNTER
         JNZ  WSL11            !
         JMP  BODRTN           ! ISOLATE HOLE
!
! *****************************************************************
! PGM LENGTH--NEW FILE/CREATE SUBROUTINE
! *****************************************************************
GETCNT   LDMD R32,=CR.CNT      ! DATA FILE COUNT
         LDBD R30,=FILTYP      ! FOR CREATE OR STORE?
         CMB  R30,=20          ! DATATY
         JZR  DACNT            !
         LDMD R32,=LSTDAT      ! COMPUTE PGM LENGTH
         SBMD R32,=NXTDAT      !   IN RECORDS
GETCN+   TSB  R#               !
         DRP  R33              !
         JZR  ZERO32           !
         ICB  R33              !
ZERO32   STB  R#,R32           !
         CLB  R#               !
DACNT    RTN                   !
!
MFXSUB   LDMD R42,=SAVNAM      ! GET NAME
         STMD R42,R36          ! STORE NAME
         STMD R32,X36,D.#R/F   ! SET # RECS/FILE
INSUBM   STBD R41,X36,D.TYPE   ! STORE TYPE
         STMD R30,X36,D.#B/R   ! SET #BYTES/RECORD
         RTN                   !
!
FIXOLD   LDMD R36,=AVAILP      ! GET OLD ADDRESS
FXOLD1   LDM  R30,=0,1         ! 256 BYTES/RECORD
         LDB  R41,=100         ! TYPE=EMPTY
         JMP  INSUBM           !
!
! *****************************************************************
! MISC TAPE CONTROL ROUTINES
! *****************************************************************
IRG      LDB  R30,=316         ! SET WGAP COMMAND
         JMP  WTPST+           ! JMP IN PAST HOLE CLEAR AND COUNT SET
!
WAIT.5   LDM  R36,=20,0        ! SET UP OCUNT FOR .5"
         JMP  GETSTS           !
!
SFWD.    LDB  R30,=16          ! SFWD COMMAND
         JMP  WTPSTS           !
!
SREV.    LDB  R30,=6           ! SREV COMMAND
         JMP  WTPSTS           !
!
FFWD.    LDB  R30,=36          ! FFWD COMMAND
         JMP  WTPSTS           !
!
FREV.    LDB  R30,=26          ! FREV COMMAND
!
! FALL THROUGH TO WTPSTS.  DON'T USE "E" IN THIS ROUTINE
!
WTPSTS   CLB  R77              ! CLEAR HOLE FLAG
         LDM  R36,=10,0        ! .25" SPEED UP
WTPST+   JSB  =CHSTS           ! INCLUDE TRACK IN STATUS
GETSTS   JSB  =TPERR?          !
         LRB  R#               ! LOOK FOR HOLE
         JEV  NOHO             !
         LDB  R77,=20          !
         DRP  R30              !
NOHO     LRB  R#               !
         LRB  R#               ! LOOK FOR TACHS
         JEV  GETSTS           !
         DCM  R36              !
         JNZ  GETSTS           ! DO THIS FOR 8 TACHS
         RTN                   !
!
CHSTS    ADBD R30,=TRACK       ! INCLUDE TRACK IN COMMAND
         STBD R30,=TAPSTS      ! SEND COMMAND
         LRB  R30              !
         LRB  R30              !
         JEV  CHSRTN           !
         ANM  R30,=2,377       ! SAVE DIRECTION
         STB  R30,R74          !
CHSRTN   RTN                   !
!
! *****************************************************************
! THIS ROUTINE GETS BUFFER-FULS FOR STORE TO SEND T
! IT RETURNS THE ADDRESS IN R56, THE COUNT IN R22,
! E=0 IF NOTHING TO STORE THIS TIME.
! *****************************************************************
GETBUF   CLE                   !
         LDBD R22,=FILTYP      ! GET FILE TYPE
         JNG  ERASEG           ! 200 IS ERASETAPE
         CMB  R22,=20          ! DATATY - CREATE?
         JZR  CREATG           ! JIF YES
         CLB  R22              ! 256 BYTES
         LDMD R66,=NXTDAT      ! NEXT DATA ADDRESS
         CMMD R66,=LSTDAT      ! LAST LINE DONE?
         JCY  NO.ICE           !
         STM  R66,R56          ! SET POINTER FOR STORE
         ADM  R66,=0,1         ! 256 BYTES?
         STMD R66,=NXTDAT      ! UPDATE NXTDAT
         CMMD R66,=LSTDAT      ! DONE YET?
         JNC  DO.ICE           ! MORE RECORDS AFTER THIS
         LDMD R66,=LSTDAT      ! COMPUTER # REMAINING
         SBMD R66,=NXTDAT      !
         STB  R66,R22          ! SET COUNT
DO.ICE   ICE                   ! SET LAST LINE
NO.ICE   RTN                   !
!
! *****************************************************************
CREATG   LDMD R46,=CR.CNT      ! GET COUNTER
         JZR  E0               ! JIF DONE
         DCM  R46              ! DECR. COUNTER
         STMD R46,=CR.CNT      !
         LDM  R56,=RECBUF      ! SET FOR STORE
CRG+     ICE                   !
         CLM  R22              !
E0       RTN                   !
!
! *****************************************************************
ERASEG   LDBD R57,=CURREC      ! CHECK FOR DONE
         CMB  R57,=4           ! DO 0-3
         JZR  E0               ! JIF DONE
         ANM  R57,=1           ! SET DIRSEG
         STBD R57,=DIRSEG      !
         LDM  R56,=DIRECT      ! DATA LOC.
         JMP  CRG+             !
!
! *****************************************************************
! LOAD/GET ROUTINES
! *****************************************************************
         BYT  241              ! ATTRIBUTES
LOADB.   STMD R6,=SAVER6       !
         LDMD R30,=LWAMEM      ! SET LOAD LIMIT
         STMD R30,=LSTDAT      !
         LDB  R30,=10          ! BPGMTY
         STBD R30,=FILTYP      !
         JSB  =GETNAM          ! GET FILE NAME
         LDMD R24,=LAVAIL      !
         LDMD R22,=BINTAB      ! BINARY LOADED?
         JNZ  BCRASH           ! JIF YES
         STBD R22,=GINTDS      ! DISABLE INTERRUPTS
         LDMD R22,=LWAMEM      !
         SBM  R22,R24          ! BYTES TO MOVE
         ICM  R24              ! LAVAIL+1 = FWA SOURCE
         LDM  R26,R12          ! FWA SINK
         JSB  =MOVUP           !
         PUMD R26,+R6          ! LOAD BIN PTR
         JSB  =LOADB+          ! GO DO LOAD
         LDMD R26,=NXTDAT      ! PTR TO END OF LOAD
         POMD R30,-R6          ! GET LOAD BIN PTR
LDB.+    CMB  R17,=300         ! POST-PROCESSING (CF MS ROM)
         JNC  LOADB1           ! JIF NO ERROR
         STM  R30,R26          ! RESET FOR MOVE
         CLM  R30              ! ADJ=0
         JMP  LOADB2           ! DONT UPDATE RMSTART
!
BCRASH   JSB  =ERROR+          !
         BYT  25D              ! TWO BIN PROGS
!
LOADB1   SBM  R30,R26          ! NEG ADJ
         LDM  R34,R30          ! NEG ADJ
         ADMD R34,=LWAMEM      ! FWA BIN AFTER MOVE
         ICM  R34              !
         STMD R34,=BINTAB      ! SET BIN PTR
LOADB2   LDM  R24,R26          !
         DCM  R24              !
         LDM  R22,R26          !
         SBM  R22,R12          ! BYTES TO MOVE
         LDMD R26,=LWAMEM      ! LWA SINK
         JSB  =MOVEDN          ! GO MOVE
! NOW ADJUST PTRS
         LDB  R22,=5           ! # PTRS TO ADJ
         LDM  R26,=LAVAIL      ! WHERE TO START
LOADBL   LDMD R36,R26          ! GET NEXT PTR
         ADM  R36,R30          ! ADJ VALUE
         PUMD R36,+R26         ! PUSH IT BACK
         DCB  R22              ! DECR. COUNT
         JNZ  LOADBL           ! LOOP TIL ALL ADJUSTED
!
! NOTE: THE FOLLOWING IS NOT ENTIRELY ACCURATE.
! IT WAS FROM EARLIER IN THE DESIGN PROCESS, AND
! THE LAYOUT/WORKING OF BPGMS CHANGED AFTER THIS
! COMMENT, BUT I'M LEAVING IT HERE AS IT WAS.
!
! *****************************************************************
! Now do binary program table relocation.  Add base address to all
! relative pointers.  The binary must be laid out as follows:
! ------------------------ THE HEADER --------------------------
! 30 bytes of header
! ------------------POINTERS TO TABLES--------------------------
! two bytes of zero (to be replaced by base addr)
! offset of runtime table
! offset of ascii table
! offset of basic statement type parse
! offset of error messages
! ---------------------TERMINATOR-------------------------------
! offset of initialization routine
! ---------------TABLES OF DEFS (OFFSETS)-----------------------
! runtime table DEF's
! basic parse table DEF's
! initialization DEF
! ------------------TERMINATOR-----------------------------------
! 377,377 to flag end of relocatables.  MUST BE HERE
! -----------------------TABLES CONTAINING VALUES----------------
! ascii table
! error message table
! *****************************************************************
         JSB  =LOADOK          ! TURN ON CRT & ENABLE INTERRTUPS
         CMB  R17,=300         ! ERRORS?
         JCY  BADLDB           ! JIF YES
         STM  R34,R36          ! GET OFFSET FOR
         ADM  R34,=30,0        !   HEADER
         LDMD R32,R34          ! 0 IF NEW BIN
! OLD LOAD ADDRESS IF FROM STOREBIN
         PUMD R36,+R34         ! PUSH NEW LOAD ADDRESS
         SBM  R36,R32          ! ADJUST R36:
! R36=R36-0 IF NEW LOAD BIN
! R36=R36-R32(OLD ADDRESS) IF STOREBIN
RELOCB   LDMD R32,R34          ! GET NEXT POINTER
         CMM  R32,=377,377     ! DONE?
         JZR  RLODUN           ! JIF YES
         ADM  R32,R36          ! ADD BASE ADDR
         PUMD R32,+R34         ! RESTORE, MOVE TO NEXT
         JMP  RELOCB           ! CONTINUE
!
! *****************************************************************
! RELOCATION COMPLETE.  NOW DO BINARY PROGRAM INITIALIZATION
!
RLODUN   LDB  R22,=3           !
         STBD R22,=ROMFL       ! SET FOR INIT
         JSB  =ROMINI          ! TELL ROMS AND BPGM
BADLDB   RTN                   ! DONE
!
! *****************************************************************
! CHAIN ENTRY, LOAD.
! *****************************************************************
CALTAP   STMD R42,=SAVNAM      ! SET FOR DSCAN
         JSB  =LOAD+           !
         JMP  LDCOMN           !
!
! *****************************************************************
! LOAD RUNTIME
! *****************************************************************
         BYT  141              ! ATTRIBUTES
LOAD.    STMD R6,=SAVER6       !
         JSB  =GETNAM          !
         LDB  R36,=5           ! LOAD = ROMINI #5
         JSB  =SCRAST          ! STORE AND SCRATCH
AUTOST   STMD R6,=SAVER6       ! FOR AUTOST
         ICB  R16              ! FOR ERRORS
         JSB  =LOAD+           ! FOR ERROR INTERCEPT
         CLB  R16              !
LDCOMN   CMB  R17,=300         ! ERRORS?
         JNC  LOADOK           ! JIF NO
         LDBD R47,=SCRTYP      ! SCRATCH TYPE ERROR?
         JZR  LOADOK           ! JIF NO
!
! THIS LETS CHAIN"NAME" GO THROUGH WITHOUT TRASHING CALLING PROGRAM
!
LODSCR   JSB  =SCRAT+          ! TRASH MEM
         JSB  =RSETGO          ! FIX POINTERS
LOADOK   LDM  R20,=GINTEN      ! SET FOR ENABLE
         STMD R20,=TINTEN      !  IN TAPEXT
         JSB  =TAPEXT          ! UP CRT, ENABLE INTERRUPTS
         RTN                   !
!
! *****************************************************************
! LOAD(BIN), CHAIN SUBS
! *****************************************************************
LOAD+    LDB  R56,=40          ! SET FILE TYPE = CAPRTY
         STBD R56,=FILTYP      !
         LDMD R56,=LAVAIL      ! SET LOAD LIMIT
         STMD R56,=LSTDAT      !
         LDMD R56,=FWCURR      ! SET LOAD ADDRESS
LOADB+   STMD R#,=NXTDAT       !
LOADB&   JSB  =TAPIN-          !
         LDB  R#,=1            ! LSB OF GINTDS
         STBD R#,=TINTEN       !
         JSB  =DSCAN           ! NAME IN DIR?
         JEZ  LNAME            ! LOAD NAME IS HERE
!
ER67D    JSB  =ERROR           !
         BYT  67D              ! FILE NAME
!
         JSB  =TERRNO          !
LNAME    JSB  =FET44           ! FILE# TO R44
         LDBD R47,X36,D.TYPE   ! TYPE CHECK
         ANMD R47,=FILTYP      !
         JNZ  TYPOK2           !
         JSB  =ER68D           ! WRONG FILE TYPE
TYPOK2   LDMD R46,X#,D.#R/F    ! SET RECS/FILE
         STMD R46,=R/FILE      !
NXTREC   LDMD R56,=NXTDAT      ! SET LOAD ADDRESS
         JSB  =READ85          ! READ A RECORD
         JEZ  RECOK            ! RECORD'S OK
LOADEX   LDBD R36,=FILTYP      ! WAS IT ASCII?
         CMB  R36,=10          ! BPGMTY
         JZR  OVEREX           !
         LDMD R12,=NXTDAT      ! SET 12 AND NXTMEM
         STMD R12,=NXTMEM      !
OVEREX   RTN                   ! EXIT TAPE ROUTINE
!
! *****************************************************************
! MOVE LOAD RECORD
! AT THIS POINT, WE HAVE A RECORD IN TAPE BUFFER
! *****************************************************************
RECOK    STMD R56,=NXTDAT      ! SET NEXT LOAD POINT
         ADM  R56,=0,1         ! ADD 256 OR EXTRA
         CMMD R56,=LSTDAT      ! OVF?
         JCY  MEMOVF           ! JIF YES
         LDMD R56,=CURREC      !
         ICM  R56              !
         STMD R56,=CURREC      !
         CMMD R56,=R/FILE      ! MORE FILE?
         JCY  LOADEX           ! NOPE
         JMP  NXTREC           !
!
MEMOVF   JSB  =ERROR           !
         BYT  19D              ! MEM OVF
!
         JSB  =TERROR          ! EXIT
!
! DONE PROCESSING CAPR BUFFER HERE
!
! *****************************************************************
! READ RECORD ROUTINE
!
TAPIN-   BIN                   ! SET BINARY
         LDM  R20,R6           ! SAVE R6 FOR ERR EXIT
         DCM  R20              !
         DCM  R20              !
         STMD R20,=SAVER6      !
TAPINT   JSB  =TYPE2           ! CHECK TAPE IN, POWER UP
         LDBD R#,=VALIDD       ! VALID DIRECTORY?
         JOD  REDOPX           ! EXIT IF YES
         JSB  =SET0S           ! SET 0 IN CASE OF ERROR ON TRACK 1
         JSB  =REWIND          !
         CLB  R#               ! FORCE READ OF 0
         ICB  R#               !
         STBD R#,=DIRSEG       !
REDOPS   CLM  R43              !
         STBD R43,=VALIDD      ! SET DIRECTORY INVALID
         ICB  R43              ! FOR XRB
         LDBD R46,=DIRSEG      !
         XRB  R46,R43          ! COMPL. DIRSEG
         ADBD R46,=D2HOOK      ! OR HOOK FOR 2ND DIRECTORY
         STMD R44,=CURFIL      !
         ICB  R43              !
         STBD R43,=D2HOOK      ! D2HOOK = 2
         LDM  R56,=DIRECT      ! LOAD ADDR.
         JSB  =READ85          ! CALL RANDOM READ
         JSB  =STOPTP          ! STOP THE MOVEMENT
         LDBD R22,=CURREC      ! 1ST OR 2ND HALF
         LRB  R22              !
         JNZ  SETVAL           ! JIF 2ND HALF
         STBD R22,=D2HOOK      ! RESTORE 1ST HALF PTR
SETVAL   CLB  R22              ! SET VALID DIRECTORY
         ICB  R22              !
         STBD R22,=VALIDD      !
REDOPX   RTN                   !
!
! *****************************************************************
! RANDOM RECORD READ
! THIS ROUTINE RETURNS E=0 FOR SAME FILE, ALL OK
!   E=1 FOR DONE WITH LOADING FILE
!   ERROR EXIT FOR EMPTY RECORD 0
!
EMPTY    LDBD R#,=HEDADR       !
         JNG  EMPTY+           !
         CLE                   !
         ICE                   !
         RTN                   !
!
EMPTY+   JSB  =ERROR           ! OCCURS IF STORE TO TAPE BEGUN WITH NO WRITE AFTER DIRECTORY U
         BYT  64D              ! AND NEW FILE USED
!
         JSB  =TERRNO          !
ER73D+   JSB  =ER73D           !
REDRND   STMD R#,=LOADAD       !
REDRN*   LDBD R#,=TOTALR       ! SET BASE FOR READ ERROR
         STBD R#,=ERBASE       !
REDRN+   JSB  =FIND-           ! FIND & KEEP GOING
         JEN  ER73D+           !
         LDB  R47,=30          ! TO ISOLATE TYPE
         ANMD R47,=HEDADR      ! GET TYPE
         JZR  EMPTY            !
         LDBD R22,=HEDAD6      ! GET FILE LENGTH
         ICB  R22              !
         JSB  =REDBL+          ! READ BUFFER, SAVE HOLE
         JZR  GOODRD           ! GOOD READ
         JSB  =ERCHK           ! CHECK READ ERROR COUNT
         JSB  =REWGA*          ! REWIND, TRY AGAIN
         JMP  REDRN+           !
GOODRD   CLE                   !
         RTN                   ! SAME FILE, HAPPY RECORD
!
READ85   JSB  =REDRND          ! READ RANDOM REC.
READ8+   JEN  EMPT85           ! MSROM 2ND PART TAPE READ
         LDBD R24,=HEDADR      ! CHECK RESERVE BIT
         LLB  R24              !
         LLB  R24              !
         TSB  R24              !
         JPS  NOCAPR           ! JIF NOT RESERVED
         LDBD R24,=HEDAD3      ! DEMAND FREE FIELD=1
         BCD                   !
         ELB  R24              !
         BIN                   !
         DCE                   !
         JEN  NOCAPR           ! JIF NOT 1
EMPT85   RTN                   ! E=0 IF CAPR & NOT EMPTY
!
NOCAPR   JSB  =ERROR           !
         BYT  75D              ! NOT HP85 RECORD
!
         JSB  =TERROR          ! SCRATCH TYPE
!
! *****************************************************************
! READ BLOCK ROUTINE
! THIS ROUTINE READS DATA INTO A BUFFER SET IN R56 FOR A COUNT IN R22.
! IT WILL ABORT EARLY ONLY UPON A COUNT DOWN OF TOO MANY TACH EDGES
! BEFORE RECEIVING A "DATA READY" FROM THE TAPE ELECTRONICS.
!
! IT SETS R77<>0 IF A HOLE IS DETECTED DURING THE READ
! AND ASSUMES R77=0 UPON ENTRY.
! *****************************************************************
REDBL+   LDMD R56,=LOADAD      ! GET LOAD ADDRESS
REDBLK   CLM  R46              ! CLEAR ACCUMULATOR
REDLUP   JSB  =TPRBYT          ! GET A BYTE
         JEN  REDOUT           !
         PUBD R32,+R56         ! PUSH IT TO MEMORY
         STB  R32,R45          ! PUT IN R45
         JSB  =TPRBYT          ! GET SECOND HALF
         JEN  REDOUT           !
         STB  R32,R44          ! PUT IN R44
         ADM  R46,R44          ! ACCUMULATE
         DCB  R22              ! DECR. BYTE COUNT
         JZR  CHKSUM           ! LAST BYTE NO GOOD
         PUBD R32,+R56         ! BYTE IS GOOD
         DCB  R22              ! DECR. BYTE COUNT
         JNZ  REDLUP           !
CHKSUM   JSB  =TPRBYT          ! READ THE CHECKSUM
         LDB  R33,R32          !
         JSB  =TPRBYT          ! SECOND HALF
REDOUT   ANM  R77,=20          ! ISOLATE HOLE
         CMM  R46,R32          ! COMPARE CHECKSUMS
         RTN                   !
!
! *****************************************************************
! TAPE INIT ROUTINE
!
TYPE2    JSB  =ISITIN          ! CHECK TAPE IN
XPORT^   BIN                   !
         STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         JSB  =CRTPOF          ! DOWN CRT
         LDB  R31,=2           ! UP TAPE
         STBD R31,=TAPSTS      !
         LDBD R31,=PRMODE      ! TAPE WAS ALREADY ON?
         JNG  ITSUP            !
         ADB  R31,=200         ! FLAG TAPE ON
         STBD R31,=PRMODE      !
         LDB  R31,=36          ! 500 MS
         JSB  =CNTRTR          !
ITSUP    RTN                   !
!
ISITIN   BIN                   !
         CLE                   !
         LDM  R30,=GINTEN      ! SET UP FOR RE-ENABLE
         STMD R30,=TINTEN      ! INDIRECT ENABLE HOOK
         LDBD R30,=TAPSTS      ! TAPE NEW?
         JOD  PONEX            ! JIF NO
         JSB  =SET0S           ! CLEAR TRACK, VALIDD,FL1T
         STBD R#,=D2HOOK       ! CLEAR HOOK ON NEW TAPE
         CLE                   !
         ICE                   !
         LDBD R#,=TAPSTS       ! TAPE IN AT ALL?
         JOD  PONEX            ! JIF YES
!
ER62D    JSB  =ERROR           !
         BYT  62D              ! TAPE OUT
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
PONEX    RTN                   !
!
! *****************************************************************
! SCRATCH TAPE (ERASE TAPE)
!
         BYT  241              ! ATTRIBUTES
ERAST.   STMD R6,=SAVER6       ! SAVE FOR ERRORS
         JSB  =TYPE2           ! TURN ON, REWIND
         JSB  =RW              !
         JSB  =TRACK1          ! SET TRACK 1
         JSB  =WPR?            ! CHECK WRITE PROTECT
         JSB  =EOTRAK          ! WRITE 12.5" GAP
         JSB  =SET0S           ! SET TR0,CLR ASN BUFFS
         JSB  =RW              !
         LDM  R36,=40,0        ! IRGLEN
         JSB  =IRG             ! WRITE THE FIRST GAP
         CLM  R40              ! SET UP DIRECTORY
         STBD R40,=D2HOOK      ! CLEAR HOOK!!
         STMD R44,=CURFIL      !
         STMD R44,=DIRSEG      ! FL1TK1 & SEG = 0
         ICB  R46              ! FOR FILE# 1
         LDB  R47,=200         ! FOR GETBUF
         STBD R47,=FILTYP      !   AND WRTREC
         LDM  R56,=DIRECT      ! SET WRITE ADDRESS
         STMD R40,R56          ! MAKE DIR. ENTRY
         CLM  R22              ! DATA COUNT
         LDB  R30,=116         ! MARK (NEW WRITE)
         JSB  =MARKO+          ! WRITE THE DIR.
         CLB  R30              !
         STBD R30,=DIRSEG      ! "LOAD" 0TH SEGMENT
         JSB  =SETVAL          ! SET VALID DIRECTORY
         RTN                   !
!
! *****************************************************************
! REWIND TAPE
! *****************************************************************
         BYT  241              ! ATTRIBUTES
REWIN.   STMD R6,=SAVER6       ! SAVE FOR ERROR RTN
         JSB  =REWS1           !
GOTOXT   GTO TAPEXT            !
!
REWS1    JSB  =TYPE2           ! DO INIT
         JSB  =REWIND          !
CATOUT   RTN                   !
!
! *****************************************************************
! CONDITION TAPE
! *****************************************************************
         BYT  241              ! ATTRIBUTES
CTAPE.   STMD R6,=SAVER6       ! SAVE FOR ERRORS
         JSB  =REWS1           ! TURN ON, REWIND
         JSB  =FFWD.           ! FAST FORWARD
CONDLP   JSB  =FNDGAP          ! WAIT FOR HOLE
         JEZ  CONDLP           ! JMP TILL HOLE
         JSB  =REWIND          !
CTAPEJ   JMP  GOTOXT           !
!
! *****************************************************************
! CAT
! *****************************************************************
         BYT  241              ! ATTRIBUTES
CAT.     STMD R6,=SAVER6       ! FOR ERRORS
         JSB  =ISITIN          ! CHECK TAPE IN
         LDBD R#,=VALIDD       ! GOOD DIRECTORY?
         JOD  CATGO            ! JIF YES
         JSB  =TAPINT          ! DO INIT
         JSB  =TAPEXT          ! TURN CRT ON
CATGO    JSB  =DISP.           !
         LDM  R26,=CATHED      ! PUT OUT HEADER
         LDM  R36,=40,0        ! 32 BYTES
         JSB  =DRV12.          ! SEND IT
         LDBD R44,=DIRSEG      ! IN SEGMENT 0?
         JZR  GOTS0            ! JIF YES
OUTLUP   JSB  =XPORT^          ! POWER UP XPORT
         JSB  =REDOPS          ! READ OPPOSITE DIRSEG
         JSB  =TAPEXT          ! UP CRT
GOTS0    LDM  R36,=DIRECT      ! DIRECTORY LOC.
CATLOP   LDM  R26,=INPBUF      ! GET CAT ENTRY ADDRESS
         CMB  R17,=300         ! ERRORS?
         JCY  CATOUT           ! JIF YES, EXIT
         LDBD R42,=SVCWRD      ! KEY PRESS?
         JOD  CATOUT           ! JIF YES, EXIT
         LDMD R42,=BLANKS      ! SET UP FOR NAME
         CLM  R56              ! FOR INDEXING LATER
         LDBD R56,X36,D.TYPE   ! GET FILE TYPE
         JNG  CATOUT           !
         JOD  BLDUN-           ! JIF SECURED
         LLB  R56              !
         TSB  R56              !
         JNG  BLDUN            ! JIF EMPTY
         LDMD R42,R36          ! GET THE NAME
         JMP  BLDUN            !
!
BLDUN-   LLB  R#               !
BLDUN    PUMD R42,+R26         ! PUSH IT OUT
         LDBD R42,X36,D.FIL#   ! EXTENDED FILE TYPE?
         JPS  NOT***           ! JIF NOT
         CLM  R56              ! FORCE STARS
NOT***   LDMD R42,=BLANKS      !
         LRB  R56              ! NULL->100  ALL->4
         LRB  R56              ! NULL->40   ALL->2
         LRB  R56              ! NULL->20   ALL->1
         JLN  DNSHFT           ! JIF NULL
         LRB  R56              ! PRGM->4  ALL->0
         LLB  R56              ! PRGM->10 ALL=0
         LLB  R56              ! PRGM->20 ALL=0
         JLZ  DNSHFT           ! JIF DATA,BPGM,ALL
         LDB  R56,=14          ! FORCE PRGM INDEX
DNSHFT   LDMD R44,X56,CATTAB   ! GET FILE TYPE
         PUMD R42,+R26         !
         PUMD R36,+R6          ! SAVE DIR. POINTER
         LDMD R36,X36,D.#B/R   !
         JSB  =CATCO-          ! INT 2 FLT 2 ASCII
         POMD R#,-R#           ! POP DIR. POINTER
         PUMD R#,+R#           ! SAVE DIR. POINTER
         JSB  =COMLOG          ! LOG. LENGTH TO R36
         LDM  R26,R30          ! SET UP FOR FORMN
         JSB  =CATCO-          ! INT. 2 FLT. 2 ASCII
         POMD R#,-R#           ! POP DIR. ADDRESS
         PUMD R#,+R#           ! SAVE IT
         JSB  =FET36           ! FILE# TO R36
         LDM  R26,R30          ! SET UP FOR FORMN
         LDB  R54,=4           !
         JSB  =CATCOM          ! INT. 2 FLT. 2 ASCII
         JSB  =CATENT          ! PUSH CR, CODE IN GFYY D
         JSB  =DRV12.          ! PRINT ALL THIS
         POMD R36,-R6          ! GET POINT BACK
         ADM  R36,=14,0        ! BUMP POINTER
         CMM  R36,=DIREND      ! OUT OF BOUNDS?
         JNC  CATLOP           ! JIF NO
ENDLOP   LDBD R36,=DIRSEG      !
         JNZ  EXCAT            !
         GTO OUTLUP            !
!
SET0S    JSB  =TRACK0          !
         JSB  =CLASNT          !
         CLM  R45              !
         STBD R45,=VALIDD      !
         STMD R45,=FL1TK1      !
EXCAT    RTN                   !
!
CATCO-   LDB  R54,=7           ! 8 BYTE FIELD
CATCOM   CLM  R70              !
         ICB  R71              !
         LDB  R76,R54          !
         CLM  R55              ! CLEAR THE REST OF 54
         JSB  =CONBIN          ! R36 BIN TO R40 FLOAT
         CLM  R66              !
         JSB  =FORMN+          !
         BIN                   !
         DRP  R36              !
         ARP  R6               !
         RTN                   !
!
! *****************************************************************
! *****************************************************************
CATHED   ASC  "NAME    TYPE  BYTES   RECS FILE" !
         BYT  15               ! CR FOR IO GUYS
CATTAB   ASC  "****BPGMDATAPROGNULL" !
! *****************************************************************
! RENAME ROUTINE
! *****************************************************************
         BYT  241              ! ATTRIBUTES
RENAM.   JSB  =TAPIN-          !
         JSB  =WPR?            ! WRITE PROTECTED?
         JSB  =GETNAM          !
         STMD R#,=SAVNM2       ! SAVE THE NEW NAME
         JSB  =DSCAN           ! NEW NAME NEW?
         JEN  NODUPE           !
!
ER63D    JSB  =ERROR           !
         BYT  63D              ! DUPE FILE NAME
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
NODUPE   JSB  =GETNAM          ! GET OLD NAME
         JSB  =DSCAN           ! IS IT HERE?
         JEN  NONAM?           ! JIF NO
FNDIT!   LDMD R42,=SAVNM2      ! REPLACE NAME
         STMD R42,R#           !
FIX      JSB  =FIND+W          ! REWRITE DIRECTORY
FIXEX    GTO TAPEXT            ! EXIT
!
NONAM?   JSB  =ER67D           !
!
! *****************************************************************
! PURGE
! *****************************************************************
PURGE.   BYT  241              ! ATTRIBUTES
         JSB  =TAPIN-          !
         JSB  =WPR?            !
         LDM  R26,R12          ! CHECK FOR PARAM
         SBMD R26,=TOS         !
         CMM  R26,=5,0         ! 4 IS STRING ONLY
         JNC  NOPARM           !
         JSB  =ONEB            ! GET PARAMETER
         DRP  R46              !
NOPARM   PUMD R#,+R6           ! SAVE "PARAM"
         JSB  =GETNAM          ! GET FILE NAME
PURJE    JSB  =DSCAN           !   TO BE PURGED
         POMD R46,-R6          ! POP PARAM
         JEN  NONAM?           !
         JNZ  JUSTP            ! SIMPLE PURGE IF <>0
         LDMD R45,=FL1TK1      ! CHECK IF FL1TK1 KNOWN
         JZR  PURGE-           ! JIF NO
         LDM  R30,R46          ! MOVE REC#
         CLM  R32              !
         LDB  R32,R45          ! MOVE FILE#
         CLM  R44              !
         JSB  =FET46           ! FETCH FILE# TO R46
         CMM  R44,R30          !
         JCY  PURGE-           ! JIF GREATER
         CLM  R55              !
         STMD R55,=FL1TK1      ! SET UP FL1TK1
         STMD R55,=ERTEMP      !   AND ERTEMP
         LDB  R55,=200         !
         STBD R55,X36,D.TYPE   ! SET NXT AVAIL FILE
         JSB  =DOBOTH          ! WRITE BOTH RECS OF DIR.
FJMP     JMP  FIXEX            !
!
PURGE-   LDB  R46,=200         ! DECLARE LAST AVAIL FILE
PURGE+   STBD R#,X36,D.TYPE    !   IN TYPE
         JMP  FIX              !
!
JUSTP    JSB  =FET46           !
         STM  R46,R34          ! PURGE FILE# TO R34
         LDM  R14,=SCANZ       ! ROUTINE ADDRESS
         CLE                   ! INIT FLAG
         JSB  =DUMPCO          ! SCAN BUFFERS
         JEN  NONAM?           ! JIF MATCH FOUND
         JSB  =FXOLD1          ! PURGE IT
         JMP  FIX              !
!
SCANZ    JEN  SCANEX           ! JIF MATCH FOUND
         JSB  =SETF#           ! FETCH DATA FILE#
         CLE                   ! IGNORE SOFT W/PROTECT
         CMB  R#,R34           ! COMPARE FILE #S
         JNZ  SCANEX           ! JIF NOT EQUAL
         ICE                   ! SET FLAG, MATCH FOUND
SCANEX   RTN                   !
!
! SCANZ LEAVES
!   R36 = DIRECTORY ADDRESS OF PURGE "FILE"
!   R34 = PURGE "FILE" NUMBER
!   R26 = DATA FILE INDEX
!   R46 = DATA FILE NUMBER
!
! *****************************************************************
! SECURITY
! *****************************************************************
         BYT  241              ! ATTRIBUTES
SECUR.   STMD R6,=SAVER6       ! FOR ERRORS
         JSB  =SECURC          ! SECURE COMMON
         JCY  NAMESC           ! JIF NAME SECURE
         ANM  R33,=40          ! CAPRTY (PGM FILE?)
         JZR  ER22D            ! JIF NO
         JSB  =SREADR          ! READ RECORD
         JNZ  ER22D            ! JIF ALREADY SECURED
         JSB  =SBYTE           ! BUILD SECURE BYTE
STFLAG   STBD R#,X56,P.SFLG    ! SET FLAG
         LDMD R30,=SECURN      ! LOAD SECURE CODE
         STMD R30,X56,P.SCOD   ! SET SECURE NAME
         LDB  R30,=40          ! CAPRTY (SET TYPE)
         STBD R30,=FILTYP      !
         JSB  =WRTRND          ! RWRITE RECORD
SECEXT   JMP  FJMP             !
!
NAMESC   ORB  R33,R47          ! ADD BITS
         JMP  PURGE+           !
!
NMEUN    NCB  R47              ! COMPLIMENT MASK
         ANM  R33,R47          ! TAKE OUT BIT
         JMP  PURGE+           !
!
! *****************************************************************
! UNSECURE
! *****************************************************************
         BYT  141              ! ATTRIBUTES
UNSEC.   STMD R6,=SAVER6       ! FOR ERRORS
         JSB  =SECURC          ! COMMON CODE
         JCY  NMEUN            ! UNSECURE IF 2,3
         ANM  R33,=40          ! CAPRTY (PGM TYPE?)
         JZR  ER22D            ! JIF NO
         JSB  =SREADR          ! READ RECORD
         JZR  SECEXT           ! ALREADY UNSECURED
         LDMD R32,X#,P.SCOD    ! CHECK SECURE CODE
         CMMD R32,=SECURN      ! SAME?
         JNZ  ER22D            ! JIF NO
         JSB  =SBYTE           ! BUILD SECURE BYTE
         NCB  R#               !
         ANM  R#,R30           ! DROP BIT(S)
         JMP  STFLAG           !
!
ER22D    JSB  =ERROR           !
         BYT  22D              ! SECURITY
!
         JSB  =TERRNO          !
SECURC   JSB  =ONEB            ! GET SECURE #
         ANM  R46,=3,0         ! ISOLATE 3 BITS
         STBD R46,=SEC#        ! SAVE EM
         JSB  =GETNAM          ! POP SECURE CODE
         LDM  R36,R42          ! USE 1ST TWO
         NCM  R36              ! SCRAMBLE THE CODE
         LLM  R36              ! LEFT ROTATE
         JNC  SHIFTD           !   THE
         ICM  R36              !      BITS
SHIFTD   STMD R#,=SECURN       ! SAVE EM
         JSB  =GETNAM          ! GET FILE NAME
         JSB  =TAPINT          !
         JSB  =WPR?            ! CHECK WRITE PROTECT
         JSB  =DSCAN           !
         JEZ  SECNAM           !
         JSB  =ER67D           ! NO NAME FOUND
SECNAM   LDBD R33,X36,D.TYPE   !
         LDBD R47,=SEC#        ! RELOAD SECURE #
         CMB  R47,=2           ! WORK ON DIRECTORY?
         SAD                   ! SAVE THIS STATUS
         NCB  R47              ! IF 2,3 WE GET 2,1
         ANM  R47,=3           !
         ICB  R47              !
         PAD                   ! GET STATUS BACK
         RTN                   !
!
SREADR   JSB  =FET44           ! FILE# TO R44
         LDM  R56,=RECBUF      !
         JSB  =READ85          ! READ 1ST RECORD
         CLM  R22              !
         LDBD R22,=HEDAD6      ! GET REC LENGTH
         ICM  R22              !
         LDM  R56,=RECBUF      !
         LDBD R30,X56,P.SFLG   ! FETCH SECURE FLAG
         RTN                   !
!
SBYTE    LDB  R37,=1           ! 0->1
         LDBD R32,=AXIS3       ! 1->201
         DRP  R37              !
         JZR  SRTN             !
         ADB  R37,=200         !
SRTN     RTN                   !
!
GETNAM   BIN                   !
         POMD R34,-R12         ! POP ADDRESS OFF STACK
         POMD R0,-R12          ! POP LENGTH
         JZR  YUKNAM           !
         LDMD R42,R34          ! GET 6 BYTES
         CMM  R0,=6,0          ! USE 6 IF LEN>5
         JCY  STRNAM           !
         ADB  R0,=42           ! INDEX
!
! WATCH OUT FOR THIS, IT DOES ARP 40'S!!!!!
! THE EXTRA 40 IS FOR CAT. WHO NEEDS SIX
! THE NUMBER OF BLANKS LOADED DEPENDS UPON THE VALUE
! IN R0, AND THE REMAINING GET EXECUTED AS ARP R40 INSTRUCTIONS.
! THE 101,251 IS LDM R*,=
!
         BYT  101,251          ! LOAD INDIRECT THROUGH REGISTER 0 INTO SOME R40'S REGISTERS
BLANKS   BYT  40,40,40,40,40,40 ! A BUNCH OF BLANKS AND/OR ARP 40S
STRNAM   STMD R42,=TEMP22      ! SAVE THE BLANK-FILLED FILE NAME
         RTN                   !
!
YUKNAM   JSB  =ERROR           !
         BYT  82D              ! BAD STRING EXPR
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
!
! *****************************************************************
! CREATE (DATA FILE)
! *****************************************************************
         BYT  241              ! ATTRIBUTES
CREAT.   JSB  =TAPIN-          !
         JSB  =WPR?            !
         LDM  R46,=0,1         ! FOR 1 PARAM CASE
         STMD R46,=B/REC       ! BYTES PER RECORD
         JSB  =ONEB            ! GET ONE NUMBER
         JEN  ER47             ! JIF OVF
         LDM  R26,R12          !
         SBMD R26,=TOS         ! ANOTHER ON STACK
         CMM  R26,=5,0         ! 4 BYTES IS STRING
         JNC  R#ONLY           !
         STMD R46,=B/REC       !
         JSB  =ONEB            ! GET OTHER PARAM
         JEN  ER47             !
R#ONLY   TSM  R46              !
         JZR  ER47             ! 0 RECORDS IS ERROR
         JNG  ER47             ! - IS ERROR
         STM  R46,R66          ! SET FOR INTMUL
         LDMD R76,=B/REC       ! GET BYTES PER REC
         JNG  ER47             ! - IS ERROR
         CMM  R76,=4,0         ! <4 BYTES/REC IS ERROR
         JCY  MULTIP           !
!
ER47     JSB  =ERROR           !
         BYT  89D              ! INVALID PARAMS
!
         JSB  =TERRNO          ! NO SCRATCH TYPE
MULTIP   JSB  =INTMUL          !
         TSB  R54              ! MAKE RESULT MULT OF 256
         JZR  R55OK            !
         ICM  R55              !
R55OK    TSB  R57              ! JIF TOO MANY
         JNZ  ER47             !
         LDM  R66,R55          ! MOV 2 BYTE
         JZR  ER47             ! INCREMENT TO ZERO?
         STMD R66,=CR.CNT      ! COUNT FOR GETBUF
         JSB  =GETNAM          ! NOW THE NAME
         JSB  =DSCAN           !
         JEN  LIKNAM           ! NAME FOUND IS ERROR
         JSB  =ER63D           ! DUPE FILE NAME
LIKNAM   LDB  R41,=20          ! DATATY (SET TYPE FOR GETCNT)
         STBD R41,=FILTYP      !   IN MTSCAN
         JSB  =MTSCAN          ! FIND EMPTY OR NXTAVAIL
         LDMD R30,=B/REC       ! SET R30 TO BYTES/REC
         LDB  R41,=20          ! DATATY (SET TYPE)
         DRP  R32              !
         JEZ  MCREAT           ! E=0 IS NXTAVAIL
         LDMD R32,X36,D.#R/F   ! GET #RECS THIS FILE
         STMD R32,=R/FILE      ! FOR RESTOR
         STMD R32,=CR.CNT      ! EOF'S IN ALL RECS!!!
         PUMD R36,+R6          ! SAVE DIR POINTER
         JSB  =MFXSUB          !
         JSB  =FIND+W          ! WRITE OUT DIRECTORY
         POMD R36,-R6          ! POP DIR POINTER
         JSB  =FIL377          ! FILL BUFFER
         GTO RESTOR            !
!
MCREAT   LDMD R#,=CR.CNT       ! R32=PHYS REC COUNT
         ADM  R46,R32          ! CHECK TAPE TOTAL RECS.
         CMM  R46,=123,3       ! >851?
         JNC  MC+              ! JIF NO
!
         JSB  =ERROR           ! TAPE FULL
         BYT  65D              ! END OF TAPE
!
         JSB  =TERRNO          !
!
MC+      JSB  =MRKFIX          ! FIX THE DIRECTORY
         JSB  =FIL377          ! FILE REC WITH 377
         GTO MRKGET            !
!
FIL377   LDM  R26,=RECBUF      ! SET ADDR.
         LDM  R30,=377,0       ! 1'S, 256 COUNT
ALL1.S   PUBD R30,+R26         ! PUSH 377
         DCB  R31              ! DOWN COUNT
         JNZ  ALL1.S           ! TILL ALL DONE
         RTN                   !
!
! *****************************************************************
! TAPE DATA STORE/LOAD - ASSIGN# <FILE#>,<FILENAME>
! *****************************************************************
! ASNTBL IS A 20 BYTE TABLE OF RELATIVE ADDRESSES REFERENCED TO RTNSTK,
! POINTING TO EACH ASSIGNED FILE'S TABLE AND BUFFER.
!    2 BYTES = 0 IF CLOSED
! OR 2 BYTES = RELATIVE ADDRESS (SEE ABOVE) IF OPEN
!
! THE FORMAT OF THE ASSIGNMENT TABLE IS:
!
!    2 BYTES  - FWCURR OF PGM WHO OPENED
! A.PGMU 2    - FWCURR OF CURRENT USING PGM
! A.PEND 4    - BUFFER PENDING FLAG (FOR STORE
! A.FILE 5    - PHYSICAL FILE #
! A.ERFL 6    - OVF OR ERROR FLAG
! A.PPTR 7    - PHYSICAL POINTER
! A.PREC 10   - PHYSICAL RECORD #
! A.LPTR 12   - LOGICAL POINTER
! A.LREC 14   - LOGICAL RECORD #
! A.#R/F 16   - # RECORDS / FILE
! A.#B/R 20   - # BYTES / RECORD
! A.MSUS 22   - MASS STORAGE UNIT SPEC.
!   23-33     - NOT USED
! A.DATA 34   - 256 BYTES OF DATA
! A.RESL 434
! ASNLEN 12  (10 DECIMAL FILES ALLOWED)
! *****************************************************************
! DISC DATA BUFFER POINTER ALLOCATION
! *****************************************************************
! CURLOC 2  - FWCURR OF PGM WHO OPENED
! A.PGMU 2  - FWCURR OF CURRENT USING PGM
! A.PEND 4  - BUFFER PENDING FLAG
! A.HEAD 5  - DISC HEAD # THIS SECTOR
! A.ERFL 6  - OVF, ERROR FLAG
! A.PPTR 7  - PHYSICAL POINTER
! A.SCTR 10 - PHYSICAL SECTOR #
! A.TRAK 11 - DISC TRACK # THIS SECTOR
! A.LPTR 12 - LOGICAL POINTER
! A.LREC 14 - LOGICAL RECORD #
! A.#R/F 16 - # SECTORS / FILE
! A.#B/R 20 - # BYTES / SECTOR
! A.MSUS 22 - MASS STORAGE UNIT SPEC.
! A.SCOD 23 - SELECT CODE, UNIT#
!   24-33   - NOT DEFINED
! A.DATA 34 - 256 BYTES DATA
! A.RESL 434
! ASNLEN 12 (10 FILES ALLOWED)
! *****************************************************************
         BYT  241              ! ATTRIBUTES
ASIGN.   JSB  =TAPIN-          ! TAPE IN, ETC?
         JSB  =GETNAM          !
         CMB  R#,=52           ! '*' (IS IT A CLOSE-FILE OP?)
         JNZ  NCLOSE           ! JIF NO
         CMB  R0,=43           ! LENGTH=1?
         JNZ  NCLOSE           ! ALLOW "*xxxxx"
! *****************************************************************
! CLOSE FILE
!
         JSB  =GET#1           !
         JNZ  CLOS1            ! FILE OPEN?
!
         JSB  =WARN            !
         BYT  66D              ! FILE NOT OPEN
!
         JMP  EXASIN           !
!
CLOS1    JSB  =DOCLOS          ! DO THE CLOSE
EXASIN   GTO TAPEXT            !
!
NCLOSE   JSB  =DSCAN           ! SEARCH FOR NAME
         JEZ  ASNNAM           ! NAME NOT FOUND ERROR
         JSB  =ER67D           !
ASNNAM   STMD R36,=CURCAT      ! SAVE CUR. CAT. LOC.
         LDBD R47,X36,D.TYPE   ! DATA FILE TYPE?
         STBD R47,=DTAWPR      ! SAVE FOR SOFT PTCT
         ANM  R47,=20          ! DATATY
         JNZ  OKSOFR           !
         JSB  =ER68D           ! WRONG FILE TYPE
OKSOFR   JSB  =GET#1           ! POP STACK VALUE
         JZR  ITSCLS           ! ZERO IF CLOSED
         JSB  =DOCLOS          ! CLOSE IT
         CMB  R17,=300         ! ERRORS ON CLOSE?
         JCY  CLRRTN           ! JIF YES
         STMD R6,=SAVER6       ! RESET SAVER6
ITSCLS   LDMD R36,=CURCAT      ! LOAD DIRECTORY LOC.
         JSB  =FET44           ! SET CURFIL
         LDM  R56,=A.RESL      ! 256 + HEADER BYTES
         JSB  =ASIGNL          ! COMPUTE FWA ASSIGN BUFF
         SBMD R22,=LAVAIL      !
         JSB  =GETMEM          ! MOVE ROUTINE
         JEN  EXASIN           !
         STMD R26,=CURLOC      ! STORE ABSOLUTE ADDR.
         LDMD R46,=CURASN      ! LOAD INDEX
         LDMD R76,=RTNSTK      !
         SBM  R76,R26          !
         STMD R76,R46          ! STORE REL. ADDRESS
         LDMD R40,=FWCURR      ! MAKE ASSIGN ENTRIES
         LDM  R42,R40          ! OPENER IS USER
         CLM  R44              !
         LDBD R45,=DTAWPR      ! CHECK SOFT PROTECT
         LRB  R45              !
         LRB  R45              ! SHIFT BIT TO CY
         SAD                   ! SAVE BIT
         CLB  R45              !
         PAD                   ! RESTORE BIT
         ERB  R#               ! CARRY TO MSBIT
         ADBD R45,=CURFIL      ! ADD FILE#
         STMD R40,R26          ! 1ST EIGHT BYTES
         CLM  R40              !
         STMD R44,X26,A.MSUS   ! DC100 MSUS = 0
         ICB  R44              ! LOGICAL REC=1
         STMD R40,X26,A.PREC   !
         LDMD R36,=CURCAT      ! GET CUR CAT LOC FOR IND
         JSB  =COMLOG          ! COMPUTE RECS PER FILE
         STMD R36,X26,A.#R/F   ! SET RECS/FILE
         STMD R32,X26,A.#B/R   ! SET BYTES PER REC
         JSB  =SETFER          ! SET FILE ERROR
         JSB  =READ85          !
         JSB  =TAPEXT          ! CRTON, TAPEOFF
CLRERF   LDMD R26,=CURLOC      ! INDEX ADDRESS
         CLB  R36              !
         STBD R36,X26,A.ERFL   ! CLEAR ERROR FLAG
CLRRTN   RTN                   !
!
! COMLOG COMPUTES THE LOGICAL RECORD COUNT BASED ON TOTAL BYTES
! IN FILE (R45-R47) AND LOGICAL # BYTES PER RECORD (R32-R34).
! THE RESULT RETURNS IN R36.
!
COMLOG   CLB  R45              !
         LDMD R46,X36,D.#R/F   ! R45=BYTES THIS FILE
         CLB  R34              ! 3RD BYTE OF R32
         LDMD R32,X36,D.#B/R   ! BYTES PER REC
COMLO+   CLM  R36              ! COUNTER
LOGLUP   SBM  R45,R32          ! DECR. BYTE COUNT
         JNC  LOGDUN           !
         ICM  R36              ! BUMP RECORD COUNT
         JNO  LOGLUP           ! JMP IF NO OVF
         LDM  R36,=377,177     ! FORCE 32767
LOGDUN   RTN                   !
!
! ASIGNL RETURNS R22=FWA ASIGN BUFFS
!
ASIGNL   LDMD R22,=RTNSTK      !
         LDB  R75,=ASNLEN      ! RTNSTK-424*(#AS.BUFFS.)
         LDM  R66,=ASNTBL      ! STEP THROUGH TABLE
NXTPOP   POMD R30,+R66         ! FILE OPEN?
         JZR  NOAD             ! JIF CLOSED
         SBM  R22,=A.RESL      ! BUMP COUNT
NOAD     DCB  R75              ! COUNT DOWN 10
         JNZ  NXTPOP           !
         RTN                   !
!
! *****************************************************************
! CLOSE FILE
!
DOCLOS   JSB  =WRTDA-          !
CLOSE+   STM  R26,R22          ! R26=BUFFER START
         DCM  R26              !
         STM  R26,R24          ! R24=SOURCE ADDRESS
         ADM  R26,=A.RESL      ! R26=SINK ADDRESS
         SBMD R22,=LAVAIL      ! COMPUTER COUNT
         JSB  =MOVEDN          !
         LDMD R20,=CALVRB      ! MOVE CALVRB
         ADM  R20,=A.RESL      !   BY BUFFER LENGTH
         STMD R20,=CALVRB      !
         LDMD R20,=LAVAIL      ! MOVE LAVAIL, TOO
         ADM  R20,=A.RESL      !
         STMD R20,=LAVAIL      !
         LDB  R75,=ASNLEN      !
         LDM  R66,=ASNTBL      !
         LDMI R24,=CURASN      ! GET REL. PTR.
NXTPO1   POMD R30,+R66         ! UPDATE REL. POINTERS
         JZR  BGRSOK           ! IGNORE ZEROS
         CMM  R30,R24          ! OMPARE RELATIVE PTRS.R
         JNC  BGRSOK           !
         JNZ  NXT2             !
         CLM  R30              ! THIS IS CLOSE FILE
         JMP  PUSH0            !
!
NXT2     SBM  R#,=A.RESL       ! ADJUST IF FURTHER
PUSH0    PUMD R#,-R66          !   FROM REFERENCE
         POMD R#,+R66          !      THAN CLOSED FILE
BGRSOK   DCB  R75              !
         JNZ  NXTPO1           !
         RTN                   !
!
! *****************************************************************
! GET# FOR ASSIGN, PRINT#, READ#
! *****************************************************************
GET#1    JSB  =ONEB            ! GET ASSBGN #
         TSM  R46              !
         JNZ  NUMOK            ! ZERO IS NO GOOD
BAD#     JSB  =ER47            ! BAD PARAMS
NUMOK    CMM  R#,=13,0         ! 11 OR MORE IS BAD
         JCY  BAD#             !
GET#1+   DCM  R#               !
         LLM  R#               ! DOUBLE TO INDEX TABLE
         ADM  R#,=ASNTBL       ! MAKE ABS. ADDRESS
         STMD R#,=CURASN       !
         LDMD R26,R46          ! GET RELATIVE ADDRESS
         JZR  QUIT             !
         SBMD R26,=RTNSTK      ! GET ACTUAL ADDRESS
         TCM  R26              !
         STMD R26,=CURLOC      ! SAVE CURRENT LOCATION
QUIT     RTN                   !
!
CLASNT   LDM  R14,=CLOSE+      ! SET ADDRESS
DUMPCO   BIN                   ! IN BINARY
         LDM  R46,=12,0        ! TEN ENTRIES
CLRAS+   PUMD R#,+R6           ! SAVE COUNTER
         JSB  =GET#1+          ! GET 0(CLOSED) OR CURLOC
         JZR  NEXTCL           ! JIF CLOSED
         LDBD R22,X26,A.MSUS   ! JIF NOT TAPE
         JNZ  NEXTCL           ! DONT CLOSE IF DISC
         PUMD R14,+R6          ! SAVE ADDRESS
         JSB  X14,ZRO          ! DO THE SUBROUTINE
         POMD R14,-R6          ! RESTORE ADDRESS
NEXTCL   POMD R46,-R6          ! POP COUNTER
         DCM  R46              !
         JNZ  CLRAS+           !
         RTN                   !
!
BUFDMP   LDM  R14,=WRTDA-      ! SET ADDRESS
         LDM  R30,=GINTEN      ! SET UP FOR INT. ENABLE
         STMD R30,=TINTEN      ! TAPE INTERRUPT ENABLE
         JSB  =DUMPCO          ! DUMP BUFFERS
         JSB  =TAPEXT          ! PWR UP IF NEED BE
         RTN                   !
!
! *****************************************************************
! CLEAR ASSIGN TABLE/WRITE DATA RECORD
! WRTDAT MAY TURN XPORT ON, BUT DOES NOT TURN IT OFF OR CRT BACK ON
! *****************************************************************
WRTDA-   STMD R6,=SAVER6       ! SO CLOSE RETURNS TO RELEASE MEM
WRTDAT   JSB  =SETF#           !
         LDMD R#,X#,A.PREC     ! AND RECORD#
         STMD R#,=CURREC       !
         LDBD R#,X#,A.PEND     ! BUFFER PENDING
         JZR  SERIAL           ! JIF NO TO EXIT
         JEZ  NOSPTC           ! JIF NOT SOFT PROTECT
         JSB  =ER22D           ! SOFT DATA PROTECT
NOSPTC   LDBD R#,X#,A.ERFL     ! CHECK ERROR FLAG
         JPS  NOFER            ! JIF NO FILE ERROR
         JSB  =ER72D           !
NOFER    JSB  =TYPE2           ! CHECK TAPE IN
         LDBD R#,=WENABL       ! CHECK WRITE ENABLE
         JNZ  NPTCT            ! JIF OK
!
         JSB  =ERROR           !
         BYT  60D              ! WRITE PROTECT
!
SETFER   LDMD R56,=CURLOC      ! INDEX, WRITE ADDRESS
         LDB  R37,=200         ! MSBIT
         LDBD R36,X56,A.ERFL   ! GET ERROR FLAG
         ORB  R36,R37          !
         STBD R36,X56,A.ERFL   ! RESTORE FLAG
         ADM  R56,=A.DATA      ! DATA ADDRESS
         RTN                   !
!
NPTCT    JSB  =SETFER          ! SET FILE ERROR
         CLM  R22              ! SET COUNT
         LDB  R30,=20          ! DATATYSET TYPE
         JSB  =WRTRN-          !
         JSB  =CLFBIT          ! CLR FILE BIT
         CLB  R#               !
         STBD R#,X#,A.PEND     ! CLEAR PENDING FLAG
SERIAL   RTN                   !
!
SETF#    CLE                   !
         LDBD R46,X26,A.FILE   ! GET FILE#
         JPS  R46OK            ! NO SOFT PROTECT
         ICE                   ! NOTE SOFT PROTECT
R46OK    ANM  R#,=177,0        ! ISOLATE FILE#
         STMD R#,=CURFIL       ! SET FILE#
         RTN                   !
!
! *****************************************************************
! READ# / PRINT# SETUP (EXACTLY THE SAME)
! *****************************************************************
         BYT  241              ! ATTRIBUTES
! PRNT#.
READ#.   STMD R6,=SAVER6       !
         JSB  =ISITIN          ! SET ENABLE EXIT, CK. TAP
         LDBD R26,=CRTWRS      ! SET FOR CRTOFF,ON
         STBD R26,=CRTONT      ! CRT ON-OFF TAPE
         CLB  R26              !
         STBD R26,=RANDOM      ! SET TO SERIAL
         DCB  R26              ! SET INTERCEPT
         STBD R26,=SCT+7       !
         LDM  R26,R12          ! SERIAL OR RANDOM?
         SBMD R26,=TOS         !
         TSB  R26              ! CAN BE 10 OR 20
         JLN  RNDPR#           ! 20 = 2 VALS = RND
         JSB  =GET#1           ! GET ASSIGN #
         JNZ  RDPR#S           !
!
ER66D    JSB  =ERROR           !
         BYT  66D              ! FILE CLOSED
!
         JSB  =TERRNO          !
RDPR#S   LDBD R36,X26,A.ERFL   ! CURRENT REC# VALID?
         JPS  NOFERR           ! NO FILE ERROR
FILERR   JSB  =ER72D           ! FILE ERROR
NOFERR   LRB  R#               ! CHECK FILE OVF
         JOD  FILERR           ! JIF FILE OVF
         JSB  =CLRERF          ! CLEAR ERROR FLAG
         RTN                   !
!
RNDPR#   JSB  =ONEB            ! GET REC#
         STM  R46,R24          ! SAVE IT
         JNZ  GORND            !
         JSB  =ER47            ! RANDOM READ TO 0 ERROR
GORND    JSB  =GET#1           ! GET ASSIGN #
         JZR  ER66D            !
RDPR#R   LDB  R36,=1           ! SET RANDOM <>0
         STBD R36,=RANDOM      !
         LDBD R36,X26,A.ERFL   ! ZERO ERFL IF NO FILE
         JPS  CLEARE           ! -RECORD ERROR
         LDBD R36,X26,A.PEND   ! DATA PENDING?
         JNZ  CLEARE           ! JIF YES, TRY WRITING AGAIN
         CLM  R36              ! SET INVALID PHYS. REC#
         DCM  R36              !
         STMD R36,X26,A.PREC   ! FORCE RE-READ OF REC
CLEARE   CLB  R#               !
         STBD R#,X#,A.ERFL     ! CLEAR
         LDM  R#,R24           ! MOVE FOR OUTLR
         JMP  OUTLR+           !
!
! COMMENTS: SERIAL PRNT#. AND READ#. CRASH ON HARD FILE ERRORS (ERFL NEG.).
! SERIAL ACCESS CRASHES ON FILE OVF.
! RANDOM ACCESS CLEARS THE LSB OF ERFL
!
! *****************************************************************
! READ/WRITE 1 BYTE & ADVANCE
!
WT+ADV   JSB  =ONEBCM          ! CHECK ERROR, COMPUTE ADDR
         STBD R#,R#            ! R32,R66
         LDB  R#,=1            ! SET PENDING FLAG
         STBD R#,X26,A.PEND    !
         JMP  ADVANC           !
!
RD+ADV   JSB  =ONEBCM          ! CHECK ERROR, COMPUTE ADDR
         LDBD R#,R#            ! R32,R66
         STBD R#,=AXIS3        ! SAVE TILL EXIT
ADVANC   LDBD R#,X26,A.PPTR    ! INCR. PHYS PTR
         ICB  R#               !
         JNZ  NOPOVF           ! JIF NO PHYS OVF
         JSB  =WRTDAT          ! WRITE IF NECESSARY
NOPOVF   LDMD R36,X26,A.#B/R   ! BYTES/RECORD
         LDMD R66,X26,A.LPTR   ! INCR. LOG PTR
         ICM  R66              !
         CMM  R66,R36          ! OVF LOG RECORD?
         JCY  OUTLR            ! JIF OUTSIDE L.RECORD
RSPTR    STM  R66,R64          !
         LDMD R66,X26,A.LREC   !
         JMP  LROK+            !
!
OUTLR    LDBD R46,=RANDOM      !
         STBD R46,X26,A.ERFL   ! 0 IF SERIAL, 1 IF RANDOM
REDNXT   LDMD R26,=CURLOC      ! MUST SET R26
         LDMD R36,X26,A.LREC   ! INCR. LOG REC#
         ICM  R36              !
OUTLR+   LDMD R66,X26,A.#R/F   ! COMPARE TO RECS/FILE
         CMM  R66,R36          !
         JCY  LROK             ! JIF NO OVF FILE
         LDB  R66,=2           ! NOTE FILE OVF
         STBD R66,X26,A.ERFL   ! ADD FILE OVF TO ERFL
         JMP  REST32           !
!
LROK     CLM  R64              ! 0 LPTR
         LDM  R66,R36          ! MOVE LREC
LROK+    STMD R64,X26,A.LPTR   ! SET LPTR,LREC
         DCM  R66              ! FOR INTMUL
         LDMD R76,X26,A.#B/R   !
         JSB  =INTMUL          !
         LDMD R26,=CURLOC      !
         LDMD R64,X26,A.LPTR   ! ADD LPTR OFFSET
         CLM  R66              !
         ADM  R54,R64          ! INTO PHYS RECORD
         LDMD R66,X26,A.PREC   ! SAME PRECORD?
         CMM  R66,R55          !
         DRP  R54              !
         JZR  NOR/W            ! NO NEED TO ADVANCE
         PUMD R54,+R6          ! SAVE POINTERS
         JSB  =WRTDAT          ! WRT CUR PREC IF NECESSARY
         POBD R55,-R6          ! TRASH MSBYTE
         POMD R55,-R6          ! RESTORE POINTERS
         STMD R55,X26,A.PPTR   ! R55=PREC POINTER
         STMD R56,=CURREC      ! R5657=PHYS REC#
         JSB  =SETF#           ! SET FILE #
         JSB  =TYPE2           ! TAPE IN CHECK
         JSB  =SETFER          ! ADD FILE ERROR
         JSB  =READ85          ! READ REC.
         LDBD R30,=CRTONT      ! CRT ON ENTRY?
         JRZ  PUP              ! JIF YES
         LDB  R30,=2           ! HALT TAPE
!
! NOTE: THIS SETS TRACK 0 IN HDWARE, BUT LEAVES THE SOFTWARE INTACT.  SHOULD BE
! OK FOR NEXT ACCESS TO TAPE CAUSE SOFTWARE WILL RESET TRACK.
!
         STBD R30,=TAPSTS      !
         STBD R30,=GINTEN      ! ENABLE INTERRUPTS
         JMP  CLFBIT           !
!
PUP      JSB  =TAPEXT          !
CLFBIT   LDMD R26,=CURLOC      ! LOAD INDEX
         LDBD R36,X26,A.ERFL   ! GET ERROR FLAG
         LLB  R36              !
         LRB  R36              ! DROP MSBIT
         STBD R36,X26,A.ERFL   ! RESTORE FLAG
         JMP  REST32           !
!
NOR/W    STBD R#,X26,A.PPTR    ! SET PPTR
REST32   LDBD R32,=DATUM       ! RESTORE R32 FOR READS
         RTN                   !
!
! NEW PREC=INT((BYTES/REC * (LREC#-1) + LPTR)/256
! NEW PPTR=((BYTES/REC * (LREC#-1) + LPTR)) MOD 256
!
ONEBCM   BIN                   ! COMMON R/W ROUTINE
         LDMD R26,=CURLOC      !
         LDBD R66,X26,A.ERFL   ! CHECK ERROR FLAG
         JZR  DATAOK           !
!
ER72D    JSB  =ERROR           !
         BYT  72D              ! RECORD# ERROR
!
         JSB  =TERRNO          !
DATAOK   CLM  R#               !
         LDBD R#,X#,A.PPTR     !
         ADM  R#,R#            !
! CAPDIS generates 313 034, ROM code is: 313 034 000 A.DATA is EQU 34
         ADM  R#,=A.DATA       ! POINT AT DATUM
         DRP  R32              !
         ARP  R66              !
         RTN                   !
!
! *****************************************************************
! PRINT STRING RUNTIME
! *****************************************************************
PRNT#$   BIN                   !
         STMD R46,=RESDAT      ! R44=LEN,R46=ADDR ON ENTRY
         ADM  R46,R44          ! COMPUTE EODATA
         STMD R46,=RESEND      !
         LDB  R46,=337         ! ENTIR$
         STBD R46,=DATYPE      ! INIT HEADER TYPE
         LDM  R46,R44          !
DOCHK    ADM  R#,=3,0          ! ADD FOR HEADER BYTES
         STMD R#,=DATLEN       !
         JSB  =LENCHK          ! OVF LREC?
         JCY  INBND$           !
         SBM  R#,R76           ! AMT DATA WHICH FITS
         STMD R#,=DATLEN       !
         CMM  R#,=4,0          ! SHOULD I EVEN START?
         JCY  ITFITS           ! JIF YES
         JSB  =REDNXT          ! ADVANCE TO NXT LREC
         LDMD R26,=CURLOC      ! BUFFER LOC
         LDBD R26,X26,A.ERFL   ! FILE OVF?
         JZR  DOBUMP           ! JIF NO
REC#ER   JSB  =ER72D           ! OVF, NEED RECORD#
ITFITS   LDBD R32,=DATYPE      !
         CMB  R32,=337         ! ENTIR$ (1ST TIME SET START)
         JZR  USTART           ! USE START
         LDB  R32,=177         ! MIDDL$ (ELSE SET MIDDLE STRING)
         JMP  OVER             !
!
USTART   LDB  R#,=317          ! START$
OVER     STBD R#,=DATYPE       !
         JSB  =USEHOL          ! WRITE TYPE, STRING
DOBUMP   LDMD R46,=RESEND      ! COMPUTER REMAINDER
         SBMD R46,=RESDAT      !
         JMP  DOCHK            !
!
INBND$   LDBD R32,=DATYPE      ! USE WHOLE STRING
         CMB  R32,=337         ! ENTIR$ OR END OF STRING
         JZR  USEHOL           !
         LDB  R32,=157         ! END$
USEHOL   JSB  =WT+ADV          ! WRITE TYPE
         LDMD R#,=RESEND       ! WRITE LENGTH
         SBMD R#,=RESDAT       !
         PUBD R33,+R6          ! SAVE SECOND HALF
         JSB  =WT+ADV          !
         POBD R#,-R6           ! RESTORE SEC HALF
         JSB  =WT+ADV          !
         LDMD R26,=DATLEN      ! LENGTH=LENGTH-3 NOW
         SBM  R26,=3,0         !
         STMD R26,=DATLEN      !
WSTRNG   LDMD R26,=DATLEN      !
         JZR  WREOR            !
         DCM  R26              ! DECR DATA COUNT
         STMD R26,=DATLEN      !
         LDMD R26,=RESDAT      ! WRITE DATA LOOP
         POBD R32,+R26         ! GET DATA BYTE
         STMD R26,=RESDAT      ! BUMP DATA PTR
         JSB  =WT+ADV          ! SEND THE BYTE
         JMP  WSTRNG           !
!
! *****************************************************************
! PRINT# NUMERIC
! *****************************************************************
PRNT#N   BIN                   !
         LDM  R56,=10,0        ! RESERVE 10 BYTES
         STMD R56,=DATLEN      ! SAVE DATA LENGTH
RD=17    STMD R40,R12          ! PUT THE DATA THERE
         ICB  R40              ! DONT LET STRING FLAG TH
         JRZ  RD=17            ! JIF "STRING FLAG"
         STMD R12,=RESDAT      ! SAVE LOC
         JSB  =LENCHK          ! CHECK FOR OVF LOG. REC.
         JCY  WSTRNG           !
         CMM  R#,=10,0         ! WILL IT FIT EVER?
         JNC  REC#ER           ! JIF NO
         JSB  =REDNXT          ! READ THE NEXT REC.
         JMP  WSTRNG           !
!
WREOR    LDMD R#,=CURLOC       ! MOVE EOR ALONG
         LDBD R66,X26,A.ERFL   ! WITH EACH DATUM
         JNZ  WDUNN            ! ERFL HERE IS RANDOM BIT
         LDMD R66,X26,A.LPTR   !   OR FILE OVF
         JZR  WDUNN            ! NO EOR AT START OF RECORD
         JSB  =DATAOK          ! COMPUTE ADDRESS
         LDB  R#,=357          ! R32 = EOR
         STBD R#,R#            ! R32-> [R66]
         STBD R#,X26,A.PEND    ! SET DATA PENDING TOO
WDUNN    RTN                   !
!
! *****************************************************************
! PRINT# SUBS
!
LENCHK   LDMD R26,=CURLOC      ! ASSIGN LOC.
         LDMD R66,X26,A.LPTR   !
         STM  R66,R76          ! SAVE LOG. PTR.
         ADMD R66,=DATLEN      ! ADD DTA LENGTH TO PTR
         LDMD R36,X26,A.#B/R   !
         CMM  R36,R66          ! OVF LOG. REC.?
         JCY  WRTN             ! JIF NO
         SAD                   ! SAVE THIS CARRY BIT
         LDBD R0,=RANDOM       ! CHECK RANDOM
         JZR  DOPAD            ! JIF NOT RANDOM
!
ER69D    JSB  =ERROR           !
         BYT  69D              ! RANDOM OVF
!
         JSB  =TERRNO          !
DOPAD    PAD                   ! RESTORE CY BIT
WRTN     RTN                   !
!
! *****************************************************************
! READ NUMERIC
!
EORN     JSB  =OUTLR           !
READ#N   JSB  =R#COMN          ! COMMON TO READN/$
         JRN  ITSDAT           !
         CMB  R32,=360         ! EOR?
         JZR  EORN             ! YES, ADVANCE TO NXT REC
!
ER33D    JSB  =ERROR+          !
         BYT  33D              ! BAD DATA TYPE
!
ITSDAT   LDM  R56,=10,0        ! SET DATA LEN
         STMD R12,=RESDAT      ! SET PUSH ADDRESS
         JSB  =GETDAT          ! GET 8 BYTES
         ADM  R12,=10,0        ! BUMP FOR SYSTEM
         JSB  =STOSV           ! GIVE TO SYSTEM
         RTN                   !
!
GETDAT   STMD R56,=DATLEN      ! STORE DATA LENGTH
         JZR  EORERN           ! JIF NULL STRING
         JSB  =LENCHK          !
         JCY  INBNDR           ! SPAN LRECORD?
         SBM  R36,R76          ! YES IMPLIES STRING
         STMD R36,=DATLEN      !
         JSB  =INBNDR          ! READ SEGMENT OF DATA
         JSB  =S$HDR           ! HANDLE STRING HEADER
         JMP  GETDAT           !
!
INBNDR   JSB  =RD+ADV          ! GET BYTE, ADVANCE
         LDMD R26,=RESDAT      !
         PUBD R32,+R26         ! PUSH DATA TO RESMEM
         STMD R26,=RESDAT      ! UPDATE ADDR.
         LDMD R26,=DATLEN      !
         DCM  R26              ! DECR. DATA COUNT
         STMD R26,=DATLEN      !
         JNZ  INBNDR           !
EORERN   RTN                   !
!
S$HDR    JSB  =RD+ADV          ! SKIP STRING TYPE
         JSB  =RD+ADV          ! GET STRING LENGTH
         PUBD R#,+R6           ! SAVE LOW ORDER BYTE
         JSB  =RD+ADV          ! GET HIGH ORDER BYTE
         STB  R#,R57           ! MOVE R32 TO R57
         POBD R56,-R6          ! POP LOW ORDER BYTE
         RTN                   !
!
! *****************************************************************
! READ STRING ROUTINE
!
EOR$     JSB  =OUTLR           ! ADVANCE ON EOR
READ#$   JSB  =R#COMN          !
         JRN  ER33D            ! ALL STRING TYPES GIVE RD
         TSB  R#               ! FIX POSITIVE!!
         JPS  ALL$             ! JIF END$ (157+1)
         CMB  R#,=360          !
         JZR  EOR$             ! ADVANCE ON EOR
         CMB  R#,=340          ! ENTIRE STRING?
         JZR  ALL$             ! JIF YES
         LDBD R#,=RANDOM       ! CHECK RANDOM
         JZR  ALL$             ! JIF NOT RANDOM
         JSB  =ER69D           ! RANDOM OVF
ALL$     LDMD R40,X26,A.LPTR   !
         SBM  R46,R40          ! #BYTES/REC - LOG. PTR.
         CMM  R46,=4,0         ! ADVANCE ON HEADER ONLY
         JNC  EOR$             !
         JSB  =S$HDR           ! HANDLE STRING HEADER
         JSB  =RSMEM-          ! RESERVE SPACE FOR STRING
         JEN  NOPE$            ! NO ROOM FOR STRING
         PUMD R56,+R12         ! PUSH STRING LENGTH
         PUMD R26,+R12         ! PUSH STRING ADDRESS
         STMD R26,=RESDAT      !
         JSB  =GETDAT          ! FETCH THE STRING
         JSB  =STOST           ! LET SOMEONE STORE IT
         RTN                   !
!
R#COMN   JSB  =RELMEM          ! RELEASE PREVIOUS MEMORY
         JSB  =ONEBCM          ! COMMON CODE
         LDBD R#,R#            ! R32,R66
         ICB  R#               ! 0 HERE IS EOF
         JNZ  NOTEOF           !
!
         JSB  =ERROR           !
         BYT  71D              ! READ ON EOF
!
         JSB  =TERRNO          ! EXIT
NOTEOF   RTN                   !
!
NOPE$    LDMD R26,=CURLOC      ! BACK UP 3 BYTES
         LDMD R66,X26,A.LPTR   !
         DCM  R66              !
         DCM  R66              !
         DCM  R66              !
         GTO RSPTR             ! RESET POINTERS
!
! *****************************************************************
! FILE# FETCH
!
FET36    BIN                   !
         SBM  R36,=DIRECT      ! FILE# = (R36-<DIRECT>)/12
ICBR37   ICB  R37              ! R37=0 AFTER SBM
         SBB  R36,=14          ! TAKE OFF 12
         JCY  ICBR37           ! JUMP TILL <0
         LDB  R36,R37          ! MOVE FILE#
         LDBD R37,=DIRSEG      ! ADD 21?
         JZR  FETDUN           ! JIF DONE
         CLB  R37              !
         ADB  R36,=25          ! ADD 21
FETDUN   RTN                   !
!
FET44    JSB  =FET46           ! FETCH # TO 46
         STM  R46,R44          ! MOVE IT TO R44
         CLM  R46              !
         STMD R44,=CURFIL      ! SET CURFIL
         RTN                   !
!
FET46    PUMD R36,+R6          ! SAVE R36
         JSB  =FET36           ! FETCH TO R36
         STM  R36,R46          ! MOVE FILE#
         POMD R36,-R6          ! RESTORE R36
         RTN                   !
!
! *****************************************************************
! *****************************************************************
! END OF TAPE ROUTINES - BEGINNING OF CRT ROUTINES
! *****************************************************************
! *****************************************************************
!
! *****************************************************************
! GRAPHICS MAPPING
! *****************************************************************
CRMAPY   LDM  R20,=10,0        ! SET UP INDEX
         JSB  =MAP.            ! MAP Y WITH INDEX
         JEN  MAPRTN           !
         STB  R76,R77          ! COMPLETE Y MAPPING IF NO BOUNDARY SEEN
         CLB  R76              !
         STMD R76,=YMAPT       ! SET R76
         RTN                   !
!
CRMAPX   CLM  R20              ! CLEAR INDEX
MAP.     JSB  =ONER            ! GET A COPY FOR X(Y)
         PUMD R40,+R12         ! SAVE A COPY
         LDMD R50,X20,CRXMIN   ! GET XMIN
         JSB  =COMFLT          ! COMPARE XMIN TO X
         JEZ  DOMAP            ! X < XMIN EXITS
POP50    POMD R50,-R12         ! CLEAN STACK
         RTN                   !
!
DOMAP    STMD R50,=XDIFF       ! SAVE "XDIFF"
         POMD R50,-R12         ! GET A COPY OF X
         LDMD R40,X20,CRXMAX   ! GET XMAX
         JSB  =COMFLT          ! COMPARE X TO XMAX
         JEN  MAPRTN           ! X >= XMAX, EXIT
         TSM  R20              !
         JNZ  GETFCT           ! USE Y DIFF
         LDMD R50,=XDIFF       ! USE X DIFF
GETFCT   LDMD R40,X20,XFACT    ! SCALE TO DOMAIN 0-127 (OR 0-255)
         JSB  =DIV10           !
         POMD R60,-R12         !
         JSB  =CONINT          ! ROUND TO OCTAL INTEGER 0
         CLE                   ! CONTINUE FOR YMAPPING
MAPRTN   BIN                   !
         RTN                   !
!
! *****************************************************************
! IMOVE X,Y
! *****************************************************************
         BYT  241              ! ATTRIBUTES
IMOVE.   JSB  =IDRSUB          ! IDRAW SUBROUTINE
         JMP  MOVE.            !
!
! *****************************************************************
! MOVE X,Y
! *****************************************************************
         BYT  241              ! ATTRIBUTES
MOVE.    CLB  R30              !
         STBD R30,=PENUPF      !
MOVE.1   JSB  =TWOR            ! GET X AND Y
         STMD R40,=LASTY       ! SET LAST Y
         STMD R50,=LASTX       ! SET LAST X
MOVE.3   PUMD R50,+R12         ! PUSH X BACK ON
         PUMD R40,+R12         ! PUSH Y BACK ON
MOVE.2   JSB  =GRAF?           !
         JSB  =CRMAPY          !
         JEN  POP50            ! OUTSIDE BOUNDS
         PUBD R77,+R6          ! PUSH UPPER BYTE 0-191
         JSB  =CRMAPX          !
         POBD R77,-R6          !
         JEN  RETURN           !
DRAW1-   STMD R76,=XMAP        !
DRAW1    BIN                   ! BIN IN CASE SOMEONE DID BCD
         STMD R76,=CRTGBA      ! STORE 0-48K MAP ADDR
PLOT7    CLB  R75              ! CLEAR FOR 2 SHIFTED BIT
PLOT8    LRM  R77              ! SHIFT ADDRESS TO 24K
         LRM  R77              ! SHIFT ADDRESS TO 12K
         JSB  =CHKSTS          ! CHECK STATUS FOR ADDR.
         ADM  R76,=0,20        ! ADD OFFSET TO RAM ADDRESS
         STMD R76,=CRTBAD      ! SEND ADDRESS TO CRT
         CLE                   !
RETURN   RTN                   !
!
! *****************************************************************
GRAF?    LDBD R30,=CRTWRS      ! GET CRT STATUS
         JNG  L92              ! JIF ALREADY IN GRAPHICS MODE
         JSB  =GRAPH.          ! ELSE SWITCH MODES
L92      RTN                   !
!
! *****************************************************************
! XAXIS RUN-TIME ROUTINE
! *****************************************************************
AXSUB1   BIN                   !
         LDM  R36,R12          ! COMPUTE # PARAMS
         SBMD R36,=TOS         ! SUBTRACT TOS
         LRM  R37              !
         LRM  R37              !
         LRM  R37              ! DIVIDE BY 8
         DCB  R36              ! OFFSET ONLY?
         JZR  ONE.P            ! ONE PARAMETER
         DCB  R36              ! TWO PARAMS?
         JNZ  FOUR.P           ! NOPE, MUST BE 4
         JSB  =TWOR            ! GET START AND FINISH
         JMP  TWO              !
!
FOUR.P   JSB  =TWOR            ! GET START AND FINISH
         STMD R50,=START       ! STORE TEMP
         STMD R40,=FINISH      ! STORE FINISH
         JSB  =TWOR            ! GET Y AND TIC
         STMD R40,=TIC         ! SAVE TIC
         LDMD R40,=FINISH      ! GET FINISH BACK
         PUMD R40,+R12         ! PUSH START(X)
         PUMD R50,+R12         ! PUSH Y OFFSET
         LDMD R60,=START       ! GET START
         PUMD R60,+R12         ! PUSH START
         PUMD R50,+R12         ! PUSH Y OFFSET
         JMP  AX.GO            !
!
ONE.P    JSB  =ONER            ! GET Y OFFSET IN R40
         STM  R40,R50          ! MOVE 40 TO 50
         CLM  R40              ! 0 TIC
TWO      STMD R40,=TIC         ! SAVE TIC
         LDMD R40,X20,CRXMAX   ! FINISH = XMAX
         PUMD R40,+R12         !
         STMD R40,=FINISH      !
         LDMD R40,X20,CRXMIN   ! START = XMIN
         STMD R40,=START       !
         PUMD R50,+R12         ! Y OFFSET
         PUMD R40,+R12         ! X START
         PUMD R50,+R12         ! Y OFFSET
AX.GO    LDMD R40,=LASTX       ! SAVE CURR. POINT
         PUMD R40,+R6          !
         LDMD R40,=LASTY       !
         PUMD R40,+R6          !
         LDMD R46,=XMAP        !
         PUMD R46,+R6          !
         PUBD R20,+R6          ! SAVE Y FLAG
         JSB  =SWAP?           ! SWAP FOR Y AXIS??
         JSB  =MOVE.1          ! MOVE TO START POINT AND DONT CHANGE PENUP!!
         POBD R20,-R6          ! RESTORE Y FLAG
         JSB  =SWAP?           ! SWAP FOR Y AXIS??
         JSB  =DRAW.1          ! DRAW TO END
         POMD R46,-R6          ! RESTORE CURR. POINT
         STMD R46,=XMAP        !
         POMD R40,-R6          !
         STMD R40,=LASTY       !
         POMD R40,-R6          !
         STMD R40,=LASTX       !
         JEN  SUB1.X           !
         ICE                   !
         LDMD R40,=TIC         ! GET TIC OFF
         JZR  SUB1.X           ! EXIT NO TICS
         TSB  R41              ! - TIC?
         JRZ  NOSWAP           !
         LDMD R40,=START       ! SWAP START AND FINISH
         LDMD R50,=FINISH      !
         STMD R50,=START       !
         STMD R40,=FINISH      !
NOSWAP   CLE                   !
SUB1.X   BIN                   !
         RTN                   !
!
! *****************************************************************
SWAP?    JZR  SWAP.X           ! THE POP BEFORE THE SUB
         JSB  =TWOR            ! GET TWO OFF
         PUMD R40,+R12         ! PUSH 1ST ON 1ST
         PUMD R50,+R12         ! PUSH 2ND ON 2ND
SWAP.X   RTN                   ! EXIT
!
! *****************************************************************
! XAXIS ROUTINE
! *****************************************************************
         BYT  241              ! ATTRIBUTES
XAXIS.   CLM  R20              ! CLEAR FOR INDEXED LOAD
         JSB  =AXSUB1          ! DO THE AXIS PART
         JEN  EXIT2            !
         LDMD R46,=MTFLAG      ! GET Y ADDRESS
         LDB  R0,=47           ! SET DRP FOR R*
         LDM  R36,=2,276       ! +2 ADD, 276 COMPARE
         LDM  R14,=CRMAPX      ! FOR JSB X14
         JSB  =TICLEN          ! COMP. TICLEN AND ADDR.
         CMB  R#,=300          ! FUNNY FIX FOR YTICS
         JNC  AXCOMN           ! Y+2 IS OK
         DCB  R#               ! 277 OR 300
         DCB  R#               ! 276 OR 277
         XRB  R#,R45           ! 277 OR 276
         JMP  AXCOMN           !
!
! *****************************************************************
! YAXIS ROUTINE
! *****************************************************************
         BYT  241              !
YAXIS    LDM  R20,=10,0        ! SET UP INDEX
         JSB  =AXSUB1          ! DO THE AXIS
         JEN  EXIT2            ! EXIT IF ERRORS
         LDMD R46,=CRTGBA      ! SET UP FOR TICS
         LDB  R0,=46           ! SET DRP FOR TICLEN
         LDM  R36,=376,376     ! -2 ADD,376 COMPARE
         LDM  R14,=CRMAPY      ! FOR JSB X14
         JSB  =TICLEN          ! COMP. TICLEN AND ADDR.
         CLB  R47              ! CLEAR UPPER BYTE
         CMB  R46,=254D        ! 0, 1 GOT TO 254,255
         JNC  AXCOMN           !
         ICB  R46              ! 255 OR 0
         ICB  R46              ! 0 OR 1
         XRB  R46,R45          ! 1 OR 0
AXCOMN   STMD R46,=AXIS2       ! STORE START X
         JMP  P5Y              !
!
EXIT2    LDMD R12,=TOS         ! CLEAN UP STACK
         RTN                   !
!
YTIC     LDM  R34,=START       ! SET START AND END
         CLM  R46              ! CLEAR NAME FOR CKLOOP
         LDM  R26,=FINISH      !
         JSB  =CKLOOP          ! USE FOR-NEXT ROUTINE
         JEN  EXIT2            !
         LDMD R40,=START       ! PUSH CUR. PT. ON STACK
         PUMD R40,+R12         !
P5Y      JSB  X14,ZRO          ! DO THE MAP
         JEN  YTIC             ! OFF SCREEN, GOTO NEXT
         ADMD R76,=AXIS2       ! ADD X-OFFSET
         JSB  =DRAW1           ! COMPUTE THE ADDRESS
         LDM  R26,=0,377       ! FOR XAXIS
         TSM  R20              ! IS IT X?
         JZR  ITSX             ! JIF YES
         LDM  R26,=1,0         ! FOR YAXIS
ITSX     LDBD R36,=AXIS3       ! GET COUNTER FROM TEMP
         ICB  R36              ! +1
AXLOOP   JSB  =GETPT.          !
         LDMD R76,=CRTGBA      ! GET CURR 48K ADDR.
         ADM  R76,R26          ! NEXT ADDRESS
         STMD R76,=CRTGBA      ! SAVE IT
         JSB  =PLOT7           ! 48K TO 12K ADDR.
         DCB  R36              ! DECR. COUNTER
         JNZ  AXLOOP           !
         JMP  YTIC             !
!
! *****************************************************************
! AXIS SUBROUTINE
! THIS ROUTINE COMPUTES THE STARTING LOCATION AND NUMBER OF DOTS TO
! CREATE SMALL AXES WHICH FORM THE TICS ON AXIS STATEMENTS.
!
TICLEN   LDMD R50,=START       ! SET START FOR AXES
         PUMD R50,+R12         ! ON STACK
         LDB  R45,=4           ! SET COUNT TO 5
         TSB  R*               ! LOOK FOR ZERO
         JNZ  CHECK1           ! NOT LEFT EDGE
SET2CT   LDB  R45,=1           ! SET COUNT TO 2
         JMP  STOREV           ! STORE THEM
!
CHECK1   CMB  R*,=1            ! X=1?
         JNZ  CHKUPR           ! CHECK UPPER LIMITS
SET4CT   LDB  R45,=3           ! SET COUNT TO 4
         JMP  STOREV           ! STORE THEM
!
CHKUPR   CMB  R*,R37           ! X-2=374? OR Y+2=300?
         JZR  SET4CT           ! SET COUNT TO 4
         ICB  R37              ! INCR. FOR COMPARE
         CMB  R*,R37           ! X-2=375 OR Y+2=301?
         JZR  SET2CT           ! SET COUNT TO 2
STOREV   STBD R45,=AXIS3       ! STORE COUNT
         LDB  R45,=1           ! FOR XOR TO COME
         ADB  R*,R36           ! +OR- 2 FROM AXIS
         RTN                   !
!
! *****************************************************************
! E=0 IF R40>=R50 *** SUB10 DOES R50-R40
COMFLT   BCD                   !
         JSB  =SUB10           ! COMPARE TO FLOAT. #S
         CLE                   !
         POMD R50,-R12         ! GET OFF STACK
         JZR  EZERO            !
         TSB  R51              ! TEST FOR RIGHT DIGIT
         JRN  EZERO            !
         ICE                   !
EZERO    RTN                   !
!
! *****************************************************************
! PLOT RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
PLOT.    LDBD R30,=PENUPF      ! MOVE, PLOT, PENDN IF PENUP
         JNZ  DRAW.            !
         JSB  =MOVE.           ! GO DO MAPPING OF X,Y
         LDB  R30,=1           !
         STBD R30,=PENUPF      ! SET PENUPF AFTER MOVE!!
         JEN  SOMRTN           !
GETPT.   JSB  =INCHR           ! GET PT. AT CURRENT ADDR.
         LDMD R76,=CRTGBA      !
         JSB  =PLOT7           ! 48K TO 12K TO CRT RESTOR
         LDB  R31,=200         ! BUILD PLOT WORD
GETPS-   BCD                   !
         CLB  R30              ! IF ANYBODY WANTS SHIFTED
         LRB  R75              ! GET 2 BITS TO BOTTOM OF
         JEV  NOHOOK           ! JIF EVEN
!
! THIS IS A SPECIAL HOOK FOR "LABEL" AND ANYONE ELSE
! WHO WOULD LIKE A 4-BIT SHIFT RATHER THAN 0-3
!
         LDB  R75,=20          ! 20 WILL BECOME 4
NOHOOK   BIN                   !
         LRB  R#               !
         LRB  R#               !
         JZR  GETPSY           !
SHFTIT   LRM  R31              ! SHIFT PLOT WORD
         DCB  R75              !
         JNZ  SHFTIT           !
GETPSY   LDBD R33,=PLOTSY      ! GET PLOT BYTE
         JZR  ANDIT            !
         ORB  R32,R31          ! OR IN THE BYTE
         JMP  SENDIT           !
!
ANDIT    NCB  R31              ! COMPLEMENT 31
         ANM  R32,R31          ! AND 32 WITH PLOT BYTE
SENDIT   STBD R32,=CRTDAT      ! SEND TO CRT
SOMRTN   RTN                   !
!
! *****************************************************************
! IDRAW RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
IDRAW.   JSB  =IDRSUB          ! DO THE ADDS
         JMP  DRAW.            !
!
IDRSUB   LDMD R40,=LASTY       ! GET LAST Y PLOTTED
         PUMD R40,+R12         ! PUSH ON STACK
         BCD                   !
         JSB  =ADDROI          ! Y+LASTY
         POMD R40,-R12         ! GET OFF STACK
         PUMD R40,+R6          ! SAVE ON R6
         LDMD R40,=LASTX       ! GET LAST X PLOTTED
         PUMD R40,+R12         ! PUSH ON STACK
         JSB  =ADDROI          ! X+LASTX
         POMD R50,-R6          ! GET Y+LASTY
         PUMD R50,+R12         ! PUSH TO STACK
         RTN                   !
!
! *****************************************************************
! DRAW RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
DRAW.    CLB  R30              !
         ICB  R30              !
         STBD R30,=PENUPF      ! SET PEN DOWN
DRAW.1   LDMD R40,=LASTX       !
         STMD R40,=XBPRIM      !
         LDMD R40,=LASTY       !
         STMD R40,=YBPRIM      !
         JSB  =TWOR            ! POP COORDINATES
         STMD R50,=XAPRIM      !
         STMD R50,=LASTX       !
         STMD R40,=YAPRIM      !
         STMD R40,=LASTY       !
         LDM  R20,=10,0        ! SET UP INDEX
NXTSID   STM  R20,R22          !
         ANM  R22,=10,0        !
         LDMD R50,X22,XAPRIM   ! A COMPONENT
         LDMD R40,X20,CRXMIN   ! BOUNDARY
         JSB  =COMFLT          ! COMPARE
         TSB  R20              ! 0,10 IS MIN COMPARE
         JNG  MAXCOM           !
         TSM  R50              ! INTERCEPT BOUNDARY CASE
         JZR  GTOS5            !
         JEZ  NOTS5            !
GTOS5    GTO S5                !
!
MAXCOM   JEZ  GTOS5            !
NOTS5    LDMD R50,X22,XBPRIM   ! B COMPONENT
         LDMD R40,X20,CRXMIN   ! BOUNDARY
         JSB  =COMFLT          ! COMPARE
         TSB  R20              ! 0,10 IS MIN COMPARE
         JNG  MAXCM2           !
         TSM  R50              ! INTERCEPT BOUNDARY CASE
         JZR  S4               !
         JEN  S4               !
SEXIT    CLE                   !
         ICE                   !
         RTN                   !
!
MAXCM2   JEN  SEXIT            !
S4       STM  R22,R24          ! R24=0,10 OR 20,30
C.AORB   LDMD R40,=YAPRIM      !
         LDMD R50,=XBPRIM      !
         JSB  =SEP15           ! SEPARATE THE #S
         JSB  =MPY30           !
         PUBD R32,+R6          !
         PUMD R36,+R6          !
         PUMD R40,+R6          ! SAVE THE VALUE
         LDMD R40,=XAPRIM      !
         LDMD R50,=YBPRIM      !
         JSB  =SEP15           ! SEPARATE THE #S
         JSB  =MPY30           !
         POMD R50,-R6          ! RESTORE 1ST #
         POMD R34,-R6          !
         POBD R33,-R6          !
         NCB  R32              !
         JSB  =ADD20           ! =W
         PUBD R32,+R6          !
         PUMD R36,+R6          !
         PUMD R40,+R6          !
         BIN                   !
         LDM  R26,R22          !
         ADM  R26,R22          !
         ADM  R26,R22          !
         TCM  R26              !
         BCD                   ! R26 = 0 OR -30
         LDMD R40,X22,YAPRIM   !
         LDMD R50,X26,YBPRIM   ! CALC A OR B
         JSB  =SEP15           ! SEPARATE THE #S
         NCB  R33              !
         JSB  =ADD20           !
         LDMD R50,X20,CRXMIN   ! BOUNDARY
         JSB  =SEP20           !
         JSB  =MPY30           !
         NCB  R32              !
         POMD R50,-R6          !
         POMD R34,-R6          !
         POBD R33,-R6          !
         JSB  =ADD20           ! W-(BOUNDARY)*(A OR B)
         PUMD R40,+R6          !
         PUMD R36,+R6          !
         PUBD R32,+R6          !
         BIN                   !
         TCM  R22              ! R22 = 0 OR -10
         TCM  R26              ! R26 = 0 OR +30
         BCD                   !
         LDMD R40,X22,XBPRIM   !
         LDMD R50,X26,XAPRIM   ! CALC B OR A
         JSB  =SEP15           ! SEPARATE THE #S
         NCB  R33              !
         JSB  =ADD20           !
         POBD R33,-R6          !
         POMD R34,-R6          !
         POMD R50,-R6          !
         TSM  R40              ! CHECK FOR 0 DIVIDE
         JZR  VALKNO           !
         JSB  =DIV20           ! CALCULATE OTHER COORDINATES
         JSB  =RONF            ! PACK IT UP
         POMD R40,-R12         !
STPRIM   LDMD R50,X20,CRXMIN   ! GET BOUNDARY
         STMD R50,X24,XAPRIM   ! R50 IS KNOWN VALUE
         LDM  R22,=10,0        !
         XRM  R24,R22          ! 0->10  .  10->0
         STMD R40,X24,XAPRIM   ! STORE COMPUTE VALUE
S6       BIN                   !
         SBM  R20,=10,0        ! NEXT INDEX
         CMB  R20,=350         !
         JZR  DRAWGO           !
         GTO NXTSID            !
!
VALKNO   LDMD R40,X20,CRXMIN   ! USE BOUNDARY
         JMP  STPRIM           !
!
S5       LDMD R50,X22,XBPRIM   !
         LDMD R40,X20,CRXMIN   ! BOUNDARY
         JSB  =COMFLT          ! COMPARE
         TSB  R20              ! 0,10 IS MIN COMPARE
         JNG  MAXCM3           !
         TSM  R50              ! INTERCEPT BOUNDARY CASE
         JZR  S6               !
         JEN  S6               !
COMPB    LDM  R24,R22          ! COMPUTE B
         BIN                   !
         ADB  R24,=20          ! R24 = 20 OR 30
         BCD                   !
         GTO C.AORB            !
!
MAXCM3   JEZ  S6               !
         JMP  COMPB            !
!
DRAWGO   LDMD R40,=XBPRIM      ! DO OLD PT. 1ST
         PUMD R40,+R12         !
         LDMD R40,=YBPRIM      !
         PUMD R40,+R12         !
         JSB  =MOVE.2          ! FIX 1ST PT.
         LDMD R46,=XMAP        ! SAVE OLD POINT
         PUMD R46,+R6          !
         LDMD R40,=XAPRIM      !
         PUMD R40,+R12         !
         LDMD R40,=YAPRIM      !
         PUMD R40,+R12         !
         JSB  =MOVE.2          ! MOVE TO NEW PT.
         POMD R24,-R6          ! RECOVER XB,YB
DRAWC    STB  R25,R26          ! MOVE YB
         CLB  R25              !
         CLB  R27              ! CLEAR UPPER BYTES
         CLM  R50              ! R51 = S<45 FLAG
         LDMD R56,=XMAP        ! XA,YA
         STB  R56,R50          ! FOR LOOP COMPARE
         STB  R56,R54          !
         LDB  R56,R57          !
         CLB  R57              ! R54=XA,0,YA,0
         CLM  R34              !
         ICM  R34              !
         STM  R34,R20          ! XINCR,YINCR
         CMB  R24,R54          ! XB TO XA
         JNC  XINCOK           ! JIF XB<XA
         TCM  R34              ! XINCR=-1
XINCOK   CMB  R26,R56          ! YB TO YA
         JNC  YINCOK           ! JIF YB<YA
         TCM  R20              ! YINCR=-1
YINCOK   LDM  R46,R56          ! COMPUTE DY
         SBM  R46,R26          !
         JPS  YOK              ! ABS VALUE
         TCM  R46              !
YOK      LDM  R56,R54          ! COMPUTE DX
         SBM  R56,R24          !
         JPS  XOK              ! ABS VALUE
         TCM  R56              !
XOK      CMM  R#,R46           ! SLOPE > 45 ?
         JCY  S<45             ! JIF NO
         ICB  R51              ! SET FLAG > 45
         LDBD R50,=YMAP        ! SET Y COMPARE
         LDM  R36,R34          ! SWAP XINCR,YINCR
         STM  R20,R34          !
         LDM  R20,R36          !
         LDM  R36,R56          ! SWAP DX,DY
         STM  R46,R56          !
         LDM  R46,R36          !
         LDM  R36,R24          ! SWAP X,Y
         STM  R26,R24          !
         LDM  R26,R36          !
S<45     LDM  R36,R46          ! D=2DY-DX
         LLM  R36              !
         SBM  R36,R56          !
LUP<45   TSB  R51              ! WHICH CASE?
         JZR  DO<45            ! JIF <45 CASE
         STB  R26,R76          ! FETCH X VALUE
         STB  R24,R77          ! FETCH Y VALUE
         JMP  GODRAW           !
!
! FOR S<45:
!  R36 = D
!  R34 = XINCR
!  R20 = YINCR
!  R56 = DX
!  R46 = DY
!  R24 = X
!  R26 = Y
! FOR S>45 SWAP 34,20  56,46  24,26
!
DO<45    STB  R24,R76          ! FETCH X VALUE
         STB  R26,R77          ! FETCH Y VALUE
GODRAW   JSB  =DRAW1           ! ADDRESS CRT
         JSB  =GETPT.          ! PLOT
         CMB  R24,R50          ! DONE?
         JZR  DRAWEX           ! JIF YES
         TSM  R36              ! D<0?
         JNG  INCRX            ! JIF YES
         SBM  R36,R56          ! D=D-2DX
         SBM  R36,R56          !
         ADM  R26,R20          ! Y=Y+YINCR
INCRX    ADM  R36,R46          ! +2DY
         ADM  R36,R46          !
         ADM  R24,R34          ! X=X+XINCR
         JMP  LUP<45           !
!
DRAWEX   CLE                   !
         RTN                   !
!
! *****************************************************************
! LDIR RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
LDIR.    JSB  =ONEI            ! GET THE VALUE
         CMM  R45,=105,0,0     ! 45 DEG OR MORE IS 90
         JCY  STLDIR           ! ELSE 0
         CLM  R45              !
STLDIR   ORB  R#,R46           ! IF <>0, GET SOME BITS
         ORB  R#,R47           !
         STBD R#,=LDIRF        ! STORE IT
         RTN                   !
!
! *****************************************************************
! LABEL RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
LABEL.   LDMD R40,=LASTY       !
         LDMD R50,=LASTX       !
         JSB  =MOVE.3          !
         STB  R75,R14          ! SAVE R75 FOR HORIZ POSITIONING
         POMD R34,-R12         ! GET STRING ADDRESS
         POMD R22,-R12         ! GET STRING LENGTH
         JEN  NOMAPS           ! NO LABEL-OFF SCREEN
         JZR  NOMAPS           ! NO LABEL-0 LENGTH
         LDM  R56,=0,376       ! -512=8LINES*64ADDRS.
         SBM  R76,=2,0         ! FOR VERTICAL ORIGIN
         LDBD R20,=LDIRF       ! VERTICAL?
         JNZ  VRTICL           !
         LDM  R56,=2,0         !
         ADM  R76,R56          ! BUMP 76 BACK
         JMP  LABLGO           !
!
VRTICL   ADB  R14,=100         ! 1 BIT OVER FOR VERTICAL
!
! 0>100, 100>200, 200>300 BUT 300>0 RATHER THAN 400, SO 0 HAS HOOK
!
         JNZ  LABLGO           !
         NCB  R14              ! GETPS- CATCHES THIS FOR
LABLGO   STMD R76,=CRTGBA      !
         POBD R32,+R34         ! GET CHAR
         JSB  =REDROM          ! READ ROM, SEND CHAR
         LDMD R76,=CRTGBA      !
         ADM  R76,R56          ! BUMP TO NEXT LOC
         DCM  R22              !
         JNZ  LABLGO           !
NOMAPS   RTN                   !
!
! *****************************************************************
! THIS ROUTINE TAKES A CHARACTER IN R32 AND READS THE DOT PATTERN
! COMPOSING IT INTO R40-R47
!
REDROM   JSB  =GETRDY          ! DEMAND PRINTER READY
         STBD R32,=PRCHAR      ! SEND CHAR TO PRINTER
         LDB  R0,=40           ! SET INDEX AND READ COL.
!
! DONE READING ROM
!
SNDSTS   STBD R0,=PRSTS        ! READ COMMAND
         LDBD R*,=PRCHAR       ! READ CHAR
         ICB  R0               ! NEXT INDEX
         CMB  R0,=50           ! MORE COLS?
         JNZ  SNDSTS           ! YES
         LDBD R0,=LDIRF        ! VERTICAL?
         JNZ  TITOL            ! JIF YES
!
! THIS ROUTINE ROTATES DOT PATTERN IN R40-47 TO
! HORIZONTAL IN R40 FOR THE TITLE STATEMENT
!
ROTATE   LDB  R70,=10          ! COUNTER
         BIN                   !
OUTLUPR  CLB  R32              ! CLEAR FOR SHIFT BYTE
         LDB  R0,=40           ! SET INDEX
INRLUP   LLB  R32              ! SHIFT R32
         TSB  R*               ! LOOK FOR LOW BIT
         JEV  SHFT1            ! NO BIT
         ICB  R32              ! BIT FOUND
SHFT1    ICB  R0               ! INCR. INDEX
         CMB  R0,=50           ! LAST INDEX?
         JNZ  INRLUP           ! NOPE
         PUBD R32,+R12         ! SAVE BYTE
         LRM  R47              ! SHIFT 8 BYTES
         DCB  R70              ! DECR. COUNTER
         JNZ  OUTLUPR          ! DO ANOTHER COLUMN STACK
         POMD R40,-R12         ! BRING BACK 10 BYTES
!
! ROTATE COMPLETE
!
TITOL    LDMD R76,=CRTGBA      ! RESTORE R76
         LDB  R0,=40           ! SET INDEX
TIT2     CMM  R76,=376,77      ! ADDRESS OUT OF BOUNDS?
         JCY  ICBR0            ! YEP, IGNORE
         CMM  R76,=0,20        ! LESS THAN 4K?
         JNC  ICBR0            ! YEP, IGNORE
         JSB  =CHKSTS          !
         STMD R76,=CRTBAD      !
         JSB  =INCHR           ! GET CURRENT BYTE AT ADD
         STB  R#,R15           ! R32 TO R15 TEMP
         JSB  =INCHR           ! NEXT BYTE OVER
         PUBD R#,+R6           ! SAVE R32
         LDB  R#,R15           ! RESTORE 1ST BYTE
         STMD R76,=CRTBAD      ! RESET ADDRESS
         STB  R*,R31           ! SET 31 WITH NEXT BYTE
         LDB  R75,R14          ! # SHIFT BITS
         JSB  =GETPS-          ! CHECK PLOT MODE, SEND B
         POBD R#,-R6           ! POP 2ND BYTE
         LDB  R31,R30          ! RECOVER SHIFTED OUT BIT
         JSB  =CHKSTS          ! CHECK STATUS B4 SENDING
         JSB  =GETPSY          ! 2ND BYTE ALREADY SHIFTED
ICBR0    SBM  R76,=100,0       ! ONE LINE UP FOR EVERYBODY
         ICB  R0               ! MORE BYTES THIS CHAR?
         CMB  R0,=50           ! DONE YET?
         JNZ  TIT2             ! EXIT ON 70
         RTN                   !
!
! *****************************************************************
! BPLOT (BLOCK PLOTING) RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
BPLOT.   JSB  =GRAF?           ! MAKE GRAPHICS MODE IF NOT ALREADY
         JSB  =ONEB            ! GET THE LOOP COUNTER
         STM  R46,R44          ! SAVE FOR INNER LOOP
         POMD R34,-R12         ! STRING ADDRESS
         POMD R22,-R12         ! STRING LENGTH
         JZR  UNW1             ! JIF 0-LEN STRING, NOP
BPLOT+   LDBD R40,=PRMODE      ! CHECK 2ND BIT OF PRMODE
         LRB  R40              !
         JEV  NOWPOT           ! JIF NO WIPEOUT
         JSB  =CRTWPO          !
NOWPOT   LDMD R76,=XMAP        ! 48K ADDRESS
NXTB     CMM  R76,=374,277     ! LAST 4 BITS?
         JCY  UNW              ! JIF YES
         STMD R76,=XMAP        ! SET XMAP
         JSB  =DRAW1           ! MAP TO CRT
         LDM  R46,R44          ! INNER LOOP COUNTER
NXTBPL   TSB  R40              ! CHECK FOR WIPEOUT
         JEV  DISABL           ! JIF CRT ON
         JSB  =INCHR-          ! GET THE BYTE
         JMP  GOTBYT           !
!
DISABL   JSB  =INCHR           ! MUST DISABLE
GOTBYT   LDMD R76,=CRTGBA      !
         ADM  R76,=10,0        ! FOR NEXT TIME
         STMD R76,=CRTGBA      !
         SBM  R76,=10,0        ! BACK UP
         JSB  =PLOT7           ! IN HARDWARE
         POBD R33,+R34         ! GET STRING BYTE
         XRB  R33,R32          ! COMBINE EM
         STBD R33,=CRTDAT      ! SEND DATA
         DCM  R22              ! MORE BYTES
         JNZ  CONTU            !
         LDMD R76,=XMAP        ! BUMP FOR "NXT" BPLOT
         ICB  R77              !
         CMM  R76,=0,300       ! OUT OF RANGE?
         JCY  UNW              ! JIF YES
         STMD R76,=XMAP        !
UNW      TSB  R40              ! CHECK 2ND BIT FOR CRTUNW
         JEV  UNW1             !
         JSB  =CRTUNW          !
UNW1     RTN                   !
!
CONTU    DCM  R46              ! INNER LOOP ZERO?
         JNZ  NXTBPL           !
         LDMD R76,=XMAP        !
         ICB  R77              ! DROP DOWN A LINE
         JMP  NXTB             !
!
! *****************************************************************
! KEYBOARD INTERRUPT SERVICE ROUTINE
! *****************************************************************
KEYSRV   SAD                   !
         JSB  =KYIDLE          ! KEYBOARD INTERCEPT?
         STBD R32,=GINTDS      !
         PUMD R32,+R6          ! PUSH R32 TO STACK
         LDBD R32,=KEYCOD      !
         CMB  R32,=213         ! RESET KEY?
         JNZ  NORSET           ! JIF NO
RSTART   LDM  R6,=STACK        ! RELOAD R6
         JSB  =RESET.          ! EXECUTE RESET
         LDB  R30,=1           !
         STBD R30,=KEYCOD      ! RESTART SCANNER
         GTO DOCUR.            ! GOTO THE EXEC LOOP
!
NORSET   LDBD R33,=SVCWRD      ! GET SVC WORD
         DRP  R32              !
         JOD  HAVE1            ! ALREADY HAVE A KEY
         BIN                   !
         ICB  R33              !
         STBD R33,=SVCWRD      !
         STBD R32,=KEYHIT      !
HAVE1    LDB  R#,=20           ! BIT 4 IN 17
         ORB  R17,R32          ! SET SERVICE REQUEST
         JSB  =EOJ1            ! RESET COUNTER
         LDB  R#,=1            !
         STBD R#,=KEYCOD       ! AND RESTART SCANNER
!
! HAVE1 ON LDB32=20 INSURES NO KEYBOARD LOCKUP IF SOME TURKEY MESSES UP R17
!
         POMD R#,-R6           ! R#=R32
         STBD R#,=GINTEN       !
         PAD                   !
         RTN                   !
!
COUNTK   BIN                   !
         LDBD R31,=KEYCNT      ! COUNTER
LOOPKE   LDBD R30,=KEYSTS      !
         LRB  R30              ! LOOK FOR KEY STILL DOWN
         JEV  EOJ2             ! NOPE, GET OUT
         LDBD R30,=CRTSTS      !
         LRB  R30              !
         JEV  LOOPKE           ! WAIT FOR RETRACE HIGH
LOOPK2   LDBD R#,=KEYSTS       ! EXIT FOR KEYUP
         LRB  R#               !
         JEV  EOJ2             !
         LDBD R#,=CRTSTS       ! WAIT FOR RETRACE LOW
         LRB  R#               !
         JOD  LOOPK2           !
         DCB  R31              ! REPEAT KEY?
         JNZ  LOOPKE           ! NOT YET
         LDBD R31,=KRPET2      ! GET MINOR SPEED FROM R
         STBD R31,=KEYCNT      ! REPEAT THE KEY
         LDBD R31,=KEYCOD      ! GET KEY
         STBD R31,=KEYHIT      ! SET FLAG WITH KEY
         LDB  R31,=20          !
         ORB  R17,R31          !
         STBD R17,=GINTDS      ! DISABLE INTERRUPTS
         LDBD R32,=SVCWRD      ! AND SET KEYBOARD
         LDB  R31,=1           !   INTO SERVICE REQUEST
         ORB  R31,R32          !      WORD, BIT 0
         STBD R31,=SVCWRD      !
         STBD R31,=GINTEN      ! ENABLE INTERRUPTS
         RTN                   !
!
EOJ2     LDB  R32,=376         !
         JSB  =CLRBIT          !
EOJ1     LDBD R32,=KRPET1      ! RESET COUNTER
         STBD R32,=KEYCNT      !
         RTN                   !
!
! *****************************************************************
! FLIP RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
FLIP.    LDB  R36,=200         ! CHANGE FLIP FLOP
         STBD R36,=KEYSTS      ! TO KEYBOARD
         RTN                   !
!
! *****************************************************************
! CLEAR RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
CLEAR.   LDM  R36,=0,2         ! 512 CHARS
         STBD R36,=EDMOD2      ! CLEAR INSERT/REPLACE
         LDMD R34,=CRTBYT      ! SET START
         ANM  R34,=300,377     ! FRONT THIS LINE
         JSB  =CRTBL+          !
         JSB  =HMCURS          ! MOVE CURSOR HOME
         JSB  =CRTUNW          ! TURN ON CRT
         JMP  CURS             ! SPIT CURSOR
!
! *****************************************************************
! CRT SUBROUTINES 2-7-77
! *****************************************************************
! CURSOR ON CRT ROUTINE
! THIS ROUTINE POSITIONS A CURSOR UNDER THE CHARACTER AT THE
! CURRENTLY ADDRESSED CRT HARDWARE LOCATION. IT DOES NOT ECHO A
! CUROSR IF THE CRT IS CURRENTLY DISPLAYING GRAPHICS
!
! REGISTERS USED: 24,25,30-35
!
OUTSTR   JSB  =OUTST+          ! SPIT OUT BUFFER, FALL THROUGH
CURS     LDBD R30,=CRTWRS      ! LOOK FOR ALPHA MODE
         JNG  CURSED           ! DONT DO IT IF IN GRAPHICS
         LDB  R33,=200         ! SET UP MASK FOR MSBIT
         JSB  =INCHR           ! FETCH CURRENT CHAR
         ORB  R#,R33           ! TOGGLE MSBIT
         JSB  =CHKSTS          ! CHECK STATUS FOR FIX
         LDMD R34,=CRTBYT      ! GET LAST BYTE ADDRESS
         STMD R34,=CRTBAD      ! SEND TO CRT
         JSB  =OUTCH1          ! OUTPUT CHARACTER WITHOUT
         JSB  =LTCURS          !
CURSED   RTN                   !
!
! *****************************************************************
! ONE CHARACTER TO CRT
! R32 HAS DATA CHARACTER WHEN CALLED
!
OUTCHR   JSB  =OUTCH1          !
         JMP  SCROL?           !
!
! *****************************************************************
! STRING OUT TO CRT
! OUTPUTS STRING TO CRT - SCROLLS IN NEW LINE WHEN NEEDED.
! CALLED WITH COUNT (MULTI-BYTE) IN R36
!
HLFLIN   BIN                   !
         TSM  R36              ! ZERO LENGTH LINE?
         JZR  ZEROLN           !
LOOP3    POBD R32,+R26         ! POP CHAR FROM BUFFER
         JSB  =OUTCHR          ! OUTPUT ONE CHARACTER
         DCM  R36              ! INCREMENT COUNTER
         JNZ  LOOP3            ! LOOP UNTIL N CHARACTERS
ZEROLN   RTN                   !
!
! *****************************************************************
! OUTPUT STRING TO CRT R36=COUNT - R26=ADDRESS
!
OUTST+   JSB  =HLFLIN          ! SEND THE NON-BLANKS
         LDMD R34,=CRTBYT      ! SETUP FOR ENTRY FROM EXE
         BIN                   !
         LLM  R34              !
         LLM  R34              ! LOOK FOR BEGIN OF LINE
         TSB  R34              ! TEST FOR START OF LINE
         JZR  SCR???           ! SOL, SO DON'T EXTEND BLANKS
BLK&SC   JSB  =BLKLIN          ! EXTEND BLANKS TO EOL
SCR???   LRM  R35              ! SET 34M BACK
         LRM  R35              !
SCROL?   JSB  =BOTMR?          ! TEST FOR TOP OF SCREEN
         JNZ  L12              ! NO, DONE
SCRBLK   JSB  =BLKLIN          ! EXTEND BLANKS TO EOL
         JSB  =UPCURS          ! MOVE CURSOR UP
         TCM  R24              ! R24 <- (64)
         JSB  =ENTSCR          ! SET START ADDRESS
L12      RTN                   !
!
BOTMR?   SBM  R34,=0,4         ! TEST FOR TOP OF SCREEN
         ANM  R34,=377,17      !
         CMMD R34,=CRTRAM      !
         RTN                   !
!
! *****************************************************************
! READ CHARACTER FROM CRT
! INCHR- IS TO BE USED BY FOLKS GUARANTEEING THAT THE CRT IS WIPED-OUT.
!
INCHR-   JSB  =CHKSTS          ! CRT BUSY?
NOTWPO   LDBD R32,=CRTWRS      ! NO, ISSUE READ REQUEST
         ICB  R32              ! ADD READ REQUEST BIT
         STBD R32,=CRTSTS      ! SEND TO CONTROLLER
LOOP2    LDBD R#,=CRTSTS       ! GET CRT STATUS
         JEV  LOOP2            ! DATA READY?
         LDBD R#,=CRTDAT       ! YES, GET DATA
ARTN     RTN                   ! DONE
!
INCHR    STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         JSB  =CHKSTS          ! CRT BUSY
         JSB  =RETRHI          ! DEMAND RETRACE
         JSB  =NOTWPO          ! FETCH CHAR
         STBD R#,=GINTEN       ! ENABLE INTERRUPTS
         RTN                   !
!
! *****************************************************************
! CURSOR MOVEMENT ROUTINES
! THE ROUTINES BELOW WERE ADDED FOR CURSOR MOVEMENT
! ABOUT 1K OF THE 4K RAM FOR HIGH RESOLUTION ALPHA.
! ONLY LTCUR. IS USED 5/5/77 IN THE CHEDIT OF G1.
! *****************************************************************
UPCUR.   LDMD R34,=CRTBYT      ! GET BYTE ADDRESS
         ANM  R34,=300,17      ! THROW AWAY BOTTOM 6 BITS
         CMMD R34,=CRTRAM      ! ON 1ST LINE?
         JNZ  UPCURS           ! NOPE
         LDM  R24,=300,3       ! YEP, SO GO 15 LINES DN.
         JMP  MOVCURS          !
!
DNCUR.   JSB  =DNCURS          ! MOVE DOWN A LINE
         SBM  R#,=0,4          ! LOOK BACK 16 LINES
         ANM  R#,=300,17       ! THROW AWAY BOTTOM 6 BITS
         CMMD R#,=CRTRAM       !
         JNZ  ARTN             !
         LDM  R24,=0,374       ! BACK UP 16 LINES
         JMP  MOVCURS          !
!
LTCUR.   LDMD R34,=CRTBYT      ! GET BYTE ADDR.
         CMMD R34,=CRTRAM      ! AM i IN 1ST PLACE?
         JNZ  LTCURS           ! NO
         LDM  R24,=376,3       ! 1022 ADDRESSES AWAY
         JMP  MOVCURS          ! MOVE THERE
!
RTCUR.   JSB  =RTCURS          ! MOVE RIGHT
         JSB  =BOTMR?          ! AT BOTTOM?
         JZR  HMCURS           ! JIF YES
         RTN                   !
!
! *****************************************************************
! MOVE THE CURSOR UP, DOWN, LEFT, RIGHT ONE POSITION WITH WRAP AROUND ON THE CRT
!
UPCURS   LDM  R24,=300,377     ! DECREMENT TO MOVE UP (-64)
         JMP  MOVCURS          !
!
DNCURS   LDM  R24,=100,0       ! INCREMENT TO MOVE DOWN (+64)
         JMP  MOVCURS          !
!
LTCURS   LDM  R24,=376,377     ! DECREMENT TO MOVE LEFT (-2)
         JMP  MOVCURS          !
!
RTCURS   LDM  R24,=2,0         ! INCREMENT TO MOVE RIGHT (2)
MOVCURS  BIN                   !
         LDMD R34,=CRTBYT      !
         ADM  R34,R24          ! BYTE ADDRESS+BYTE ADDRESS
         ANM  R34,=377,17      ! MOD 10000
BYTCR!   DRP  R34              !
BYTCRT   SAD                   ! SAVE DRP
         JSB  =CHKSTS          ! CRT BUSY?
         PAD                   ! RESTORE DRP
         STMD R#,=CRTBYT       ! STORE BYTE ADDRESS IN MEMORY
         STMD R#,=CRTBAD       ! SEND TO CRT CONTROL
         RTN                   !
!
OUTCH1   JSB  =ALPHA.          ! FORCE TO ALFA
         JSB  =CHKSTS          !
         STBD R32,=CRTDAT      ! NO, OUTPUT CHARACTER
         JMP  RTCURS           ! KEEP UP WITH RAM MOVEMENT
!
! *****************************************************************
! KEY LABEL RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
KEYLA.   BIN                   ! FOR RUNTIME
         JSB  =ALPHA.          ! SET TO ALPHA IF NOT THERE
         JSB  =DECUR2          ! REMOVE THE CURSOR !!
         LDMD R34,=CRTRAM      ! GET START ADDRESS
         ADM  R34,=100,3       ! ADD 14 LINES
         ANM  R34,=377,17      ! MOD 4K
         JSB  =BYTCR!          ! SEND ADDR. TO CRT
         LDB  R32,=137         ! SEPARATOR CHAR.
         JSB  =L8              ! SPIT OUT 1 LINE OF EM
         LDM  R26,=LEGEND      !
         LDB  R36,=100         ! 64 BYTES PER KEYLABEL
LOOP4    POBD R32,+R26         ! POP CHAR FROM BUFFER
         JSB  =OUTCH1          ! SEND CHAR
         DCB  R36              ! DECR. COUNTER
         JNZ  LOOP4            !
HMCURS   LDMD R34,=CRTRAM      !
         JMP  BYTCRT           ! TELL CRT CONTROL
!
! *****************************************************************
CLREOL   LDMD R66,=CRTBYT      ! SAVE ADDR.
         JSB  =BLKLIN          ! BLANK THE LINE
EOL1     DRP  R66              ! RESET CUR LOC
         JMP  BYTCRT           !
!
! *****************************************************************
! REMOVE TWO CURSORS FROM THE SCREEN
!
DECUR2   LDBD R30,=CRTWRS      ! IN ALPHA?
         JNG  ERTN             ! JIF NO
         LDMD R66,=CRTBYT      ! SAVE CUR LOC
         JSB  =INCHR           ! FETCH 2ND CHAR
         STB  R#,R33           ! SAVE IT
         JSB  =LTCUR.          ! MOVE LEFT WITH WRAP
         JSB  =INCHR           ! FETCH 1ST CHAR
         ANM  R#,=177,177      ! TRASH MSBITS
         DRP  R34              ! FROM LTCUR.
         JSB  =BYTCRT          ! RESTORE 1ST BYTE LOC
         LDBD R#,=EDMOD2       ! 1 CURS IF NOT INSERT
         JZR  DECUR1           !
         STBD R32,=CRTDAT      ! SEND 1ST BYTE
DECUR1   JSB  =RTCUR.          ! MOVE RIGHT WITH WRAP
         STBD R33,=CRTDAT      ! SEND 2ND BYTE
         JMP  EOL1             !
!
! *****************************************************************
! SCROLL UP, DOWN
!
SCRDN    JSB  =UPCURS          ! MOVE CURSOR UP A LINE
ENTSCR   LDMD R34,=CRTRAM      ! SET START ADDR.
         ADM  R34,R24          ! 24 SET BY UPCURS
         ANM  R34,=377,17      ! THROW AWAY GARBAGE
SAD1     JSB  =RETRHI          ! DEMAND RETRACE
         STMD R34,=CRTRAM      !
         STMD R34,=CRTSAD      !
ERTN     RTN                   !
!
SCRUP    JSB  =DNCURS          ! MOVE CURSOR DOWN A LINE
         JMP  ENTSCR           !
!
! *****************************************************************
! CRT ON-OFF-INIT
!
! WIPEOUT SCREEN
CRTWPO   LDB  R31,=2           !
WPO10    BIN                   !
         LDBD R30,=CRTWRS      ! GET MEM STATUS
         ORB  R30,R31          ! SEND WPO
         STBD R30,=CRTWRS      ! SENT TO MEMORY
         STBD R30,=CRTSTS      ! SENT TO CRT
         JMP  RETRHI           ! WAIT FOR RETRACE
!
! *****************************************************************
CRTPOF   JSB  =CRTWPO          ! SHUT OFF VIDEO
         JSB  =RETRA1          ! DEMAND LEAD EDGE OF RETRACE
         LDB  R31,=6           ! POF AND WPO
         JMP  WPO10            ! SEND POWER-OFF AND WIPE-OUT
!
CRTPUP   CLB  R31              !
         STBD R31,=TAPSTS      ! FORCE XPORT DOWN IF CRT
         LDBD R31,=PRMODE      ! FLAG TAPE OFF
         LLB  R31              !
         LRB  R31              !
         STBD R31,=PRMODE      !
         JSB  =GETRDY          ! DEMAND PRINTER NOT BUSY
         LDBD R31,=CRTWRS      !
         ANM  R31,=373         !
         STBD R31,=CRTSTS      !
         STBD R31,=CRTWRS      !
         LDB  R31,=3           ! COUNT 3 RETRACES
         JSB  =CNTRTR          ! 50 MS
         JMP  CRTUNW           !
!
! RETRACE BIT ODD  = DISPLAY
! RETRACE BIT EVEN = RETRACE
!
RETRA1   DRP  R30              !
         BIN                   !
RETRA-   LDBD R#,=CRTSTS       !
         LRB  R#               !
         JEV  RETRA-           ! WAIT FOR RETRACE HIGH
RETRHI   DRP  R30              !
         BIN                   !
RETRH+   LDBD R#,=CRTSTS       !
         LRB  R#               !
         JOD  RETRH+           ! WAIT FOR RETRACE LOW
         RTN                   !
!
CNTRTR   JSB  =RETRA1          ! GET RETRACE
         DCB  R31              ! EXIT YET?
         JNZ  CNTRTR           !
         RTN                   !
!
! *****************************************************************
! GCLEAR RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
GCLR.    JSB  =CRTWPO          ! WIPE OUT SCREEN
         LDB  R#,=202          ! MAKE IT GRAPHICS
         STBD R#,=CRTWRS       ! FOR CRTUNW
         STBD R#,=CRTSTS       ! MUST TELL HARDWARE ELSE IT WRAPS AS IN ALPHA AFTER 1 "PAGE"
         CMMD R12,=TOS         ! ANY PARAMS?
         JNZ  GOTPAR           ! NOPE
GRINOF   JSB  =GRINIT          !
         JMP  CRTUNW           !
!
GOTPAR   JSB  =CRMAPY          ! COMPUTER CLEAR ADDRESS
         JEN  GRINOF           ! VALUE OFF SCREEN
         LDM  R36,=0,300       ! COMPUTER COUNT
         SBM  R36,R76          ! R36=# ROWS TO CLR (*256
         LRM  R37              !
         LRM  R37              ! R36=# ROWS *32 BYTES PER ROW
         LRM  R37              !
         LDBD R32,=PLOTSY      ! SET R32
         JSB  =GRINI+          !
!
! **** FALL THROUGH TO CRTUNW!!!!!
!
CRTUNW   LDBD R31,=CRTWRS      ! FETCH CURRENT CRT STATUS
         ANM  R31,=371         ! WPO, POF = 0
         STBD R31,=CRTWRS      !
         STBD R31,=CRTSTS      !
UWRTN    RTN                   !
!
! *****************************************************************
! ALPHA RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
ALPHA.   LDBD R30,=CRTWRS      !
         JPS  UWRTN            ! JIF ALREADY THERE
         JSB  =CRTWPO          ! WPO BEFORE CHANGE
         LDB  R30,=2           !
         STBD R30,=CRTWRS      ! STORE ALFA MODE
         JSB  =CHKSTS          !
         LDMD R34,=CRTBYT      !
         STMD R34,=CRTBAD      ! GET CURRENT BYTE
         LDMD R34,=CRTRAM      !
A/G      STMD R#,=CRTSAD       ! SET START ADDRESS
         JMP  CRTUNW           !
!
! *****************************************************************
! GRAPH RUNTIME
! *****************************************************************
         BYT  241              ! ATTRIBUTES
GRAPH.   LDBD R30,=CRTWRS      !
         JNG  UWRTN            ! JIF ALREADY THERE
         JSB  =CRTWPO          ! WPO BEFORE CHANGE
         LDB  R30,=202         !
         STBD R30,=CRTWRS      ! STORE GRAPHICS MO
         JSB  =CHKSTS          !
         LDM  R34,=0,20        ! SET GRA. START AD
         JMP  A/G              !
!
! *****************************************************************
! CRT TURN-ON ROUTINES
!
CRTINT   LDB  R30,=202         ! INITIALIZE MEMORY
         STBD R30,=CRTWRS      !
         STBD R30,=CRTSTS      ! MUST TELL HARDWARE TO PREVENT WRAP AROUND
         JSB  =GRINIT          ! ZERO GRAPHICS
         JSB  =CRTBLK          ! BLNAK ALPHA
CJMP     JMP  CRTUNW           ! TURN ON IN ALPHA
!
! GRAPHICS INITIALIZATION TO ZEROS
!
GRINIT   LDBD R32,=PLOTSY      ! SET R32 TO INIT CHAR
GRIN++   CLM  R76              ! A0 FOR BYTE ADDRESS
         LDM  R36,=0,30        ! SET COUNTER
GRINI+   JSB  =PLOT8           ! ADDR. CRTBAD
         LDM  R#,=0,20         ! SET SAD
         STMD R#,=CRTSAD       !
         NCB  R32              ! ERASE WITH PLOTSY
         JMP  L7               !
!
! ALPHA INITIALIZATION TO BLANKS
!
CRTBLK   CLM  R34              ! 0 START, BYTE ADDR.
         LDM  R36,=0,10        ! 512*4 CHARS
CRTBL+   JSB  =CRTWPO          ! WIPEOUT BEFORE MODE CHANGE
         LDB  R#,=2            ! SET ALPHA MODE, WPO
         STBD R#,=CRTWRS       ! SEND TO MEMORY
         STBD R#,=CRTSTS       ! SEND TO CRT
         JSB  =CHKSTS          !
         JSB  =SAD1            ! SET START ADDRESS
         JSB  =BYTCR!          ! TELL BYTE ADDRESSES
         LDB  R32,=15          ! CR CHAR
L7       JSB  =CHKSTS          ! CHECK STATUS
         STBD R32,=CRTDAT      !
         DCM  R36              ! DECREMENT COUNTER
         JNZ  L7               !
         RTN                   !
!
! EXTEND BLANKS TO REMAINDER OF LINE ON CRT.  CURRENT POSITION IN R34 AT ENTRY!
!
BLKLIN   LDB  R32,=15          !
         BIN                   !
L8       JSB  =OUTCH1          !
         LLM  R#               !
         LLM  R#               !
         TSB  R#               ! LOWER BYTE =0?
         JNZ  L8               ! NO, LOOP
         RTN                   !
!
! CHECK CRT STATUS
!
CHKSTS   DRP  R30              !
         BIN                   !
L90      LDBD R#,=CRTSTS       ! GET CRT STATUS
         JNG  L90              !
         RTN                   !
!
! *****************************************************************
! INTERRUPT SERVICE ROUTINE FOR THE SYSTEM CLOCK, INCREMENTS THE
! DATE AND SETS TIMER 0 CLEAR AND READY TO INTERRUPT
! 24x60x60x1000 MS FROM NOW
! *****************************************************************
CLKSR0   SAD                   ! SAVE CPU STATUS
         STBD R40,=GINTDS      ! DISABLE INTERRUPTS
         PUMD R40,+R6          ! SAVE R40
         PUMD R50,+R6          ! AND R50
         LDM  R50,R30          ! AND R30-37
         PUMD R50,+R6          !
         LDB  R55,=40          ! ADDRESS AND CLR INTERRUPT
         JSB  =TIMWST          !
         CLM  R44              ! GET #MSCECS PER DAY
         LDM  R46,=100,206     ! 86400
         JSB  =TIMRDY          ! SET TIMER 0 WITH ONE DA
         STMD R44,=CLKDAT      !
         LDMD R45,=DATE        ! GET THE DATE
         BCD                   !
         ICM  R45              !
         LLB  R47              !
         LRB  R47              ! DUMP UPPER HALF IF ANY
         STMD R45,=DATE        ! RESTORE IT
         POMD R50,-R6          !
         STM  R50,R30          ! RESTORE REGS
         POMD R50,-R6          !
         CLM  R40              !
         STMD R40,=TIME        ! CLEAR BASE TIME
         POMD R40,-R6          ! RESTIRE R40
         STBD R40,=GINTEN      ! ENABLE INTERRUPTS
         PAD                   ! RESTORE CPU STATUS
         RTN                   !
!
! *****************************************************************
! INTERRUPT SERVICE ROUTINES FOR TIMERS 1-3
! *****************************************************************
CLKSR3   SAD                   !
         STBD R36,=GINTDS      !
         PUMD R36,+R6          !
         PUBD R55,+R6          !
         LDB  R36,=20          !
         LDB  R55,=340         ! REENABLE FOR TIMER3
         JMP  CLCOMN           !
!
CLKSR2   SAD                   !
         STBD R36,=GINTDS      !
         PUMD R36,+R6          !
         PUBD R55,+R6          !
         LDB  R36,=10          !
         LDB  R55,=240         ! REENABLE FOR TIMER2
         JMP  CLCOMN           !
!
CLKSR1   SAD                   !
         STBD R36,=GINTDS      !
         PUMD R36,+R6          !
         PUBD R55,+R6          !
         LDB  R36,=4           !
         LDB  R55,=140         ! REENABLE FOR TIMER1
!
CLCOMN   LDB  R37,=20          !
         ORB  R17,R37          ! SET SERVICE REQUEST
         LDBD R37,=SVCWRD      !
         ORB  R37,R36          ! SET BIT FOR CLOCK
         STBD R37,=SVCWRD      !
         JSB  =TIMWST          ! REENABLE TIMER
         POBD R55,-R6          ! RESTORE R55
         POMD R36,-R6          !
         STBD R36,=GINTEN      !
         PAD                   !
         RTN                   !
!
TIMWST   JSB  =TIMRDY          !
         STBD R55,=CLKSTS      ! OUTPUT STATUS
         RTN                   !
!
TIMRDY   LDBD R37,=CLKSTS      !
         JPS  TIMRDY           ! LOOP IF NOT READY
         RTN                   !
!
! *****************************************************************
! DELETE RUNTIME
! *****************************************************************
         BYT  141              ! ATTRIBUTES
DELET.   JSB  =SECTST          ! SEE IF SECURED
         JCY  DELRTN           ! JIF YES
         JSB  =FXLEN           ! FIX DIR & ZERO LEN
         CMB  R17,=300         !
         JCY  DELRTN           ! JIF ERRORS
         JSB  =TO?I            ! GET 2 INT
         JEZ  ERR91            ! JIF NONE
         BCD                   !
         DCE                   !
         JEN  DELET1           ! JIF TWO LINE #
         STM  R45,R55          ! ELSE LAST = FIRST
DELET1   CMM  R55,R45          ! LAST >= FIRST
         JNC  ERR89            ! JIF NO
         BIN                   !
         LDM  R76,R45          ! GOAL = FIRST
         JSB  =FNDLIN          !
         STM  R36,R26          ! SAVE FWA SINK
         LDM  R76,R55          ! GOAL = LAST
         JSB  =FNDLIN          !
         JEN  DELET2           ! JIF NOT FOUND
         JSB  =SKPLN           ! ELSE SKIP ONE MORE
DELET2   STM  R36,R24          ! FWA SOURCE
         SBM  R36,R26          ! INCR MOVED
         LDM  R22,R12          !
         SBM  R22,R24          ! BYTES TO MOVE
         JSB  =FXRSET          ! RESET POINTERS
         JSB  =MOVUP           !
         JSB  =ST240+          !
DELRTN   RTN                   !
!
FXLEN    BIN                   !
         JSB  =FXDIR           ! DEALLO & FIX MEM
         LDMD R36,=FWCURR      !
         CLM  R76              !
         STMD R76,X36,P.LEN    ! ZERO PROGRAM LEN
         RTN                   !
!
ERR91    JSB  =ERROR+          !
         BYT  91D              ! MISSING PARAM
!
ERR89    JSB  =ERROR+          !
         BYT  89D              ! INVALID PARAM
!
SECTST   LDB  R0,=1            !
         JSB  =SECUR?          ! LIST SECURED?
         CMB  R17,=300         ! CARRY IF YES
         RTN                   !
!
! *****************************************************************
! LINE EDITOR 02-18-77 (EDITING A LINE OF BASIC PROGRAM)
! *****************************************************************
LINEDR   JSB  =SECTST          ! LIST SECURED?
         JNC  LINEDR1          ! DONT DO IT IF ERRORS
LINEDR2  LDMD R12,=NXTMEM      ! TRASH LINE IF ERR
         RTN                   !
!
LINEDR1  JSB  =FXLEN           ! FXDIR & ZERO PGM LEN
         CMB  R17,=300         !
         JCY  LINEDR2          ! JIF ERRORS
         LDMD R56,=STSIZE      !
         POMD R76,-R56         ! CURRENT LINE #
         JSB  =FNDLIN          !
         STM  R36,R76          ! SAVE POINTER
         JEN  INSER            ! JIF NOT FOUND
         JSB  =DELET           !
INSER    JSB  =INSRT           !
         ICM  R12              !
         ICM  R12              !
         SBMD R12,=STSIZE      !
         ADMD R12,=NXTMEM      ! R12-(STSIZE-2)+NXTMEM
         STMD R12,=NXTMEM      !
FXRTNX   RTN                   !
!
! SHOULD CLEAR TIMERS, KEYS, ON ERROR, & ASSIGN BUFFER
!
FXDIR    LDMD R36,=FWCURR      ! FWA PROG
         CLM  R40              !
         STMD R40,X36,P.DATL   ! CLEAR P.DATL-P.GSUB
         LDMD R30,X36,P.LEN    !
         JZR  FXRTNX           ! JIF PGM LEN 0
         LDBD R31,X36,P.TYPE   ! ALLOC BIT
         JSB  =RSETGO          !
         ANM  R31,=40          ! ISOLATE ALLOCATION BIT
         JZR  FXRTN            ! JIF NOT ALLOCATED
         PUBD R16,+R6          ! SAVE CSTAT
         CLB  R16              ! SET TO IDLE
         JSB  =DALLOC          ! DEALLOCATE
         POBD R16,-R6          !
         CMB  R17,=300         !
         JCY  FXRTN            ! EXIT IF ERRORS
         LDM  R24,=P.LEN       !
         ADMD R24,=FWCURR      !
         POMD R26,+R24         ! PGM LEN
         ADMD R26,=FWCURR      ! FWA SINK
         STMD R26,=NXTMEM      ! RESET NXTMEM
         LDMD R24,=STSIZE      ! FWA SOURCE
         TSB  R16              !
         JOD  FXDIR2           !
         DCM  R24              !
         DCM  R24              !
FXDIR2   LDM  R22,R12          ! REL R10
         SBM  R22,R24          ! # BYTES
         LDM  R36,R24          !
         SBM  R36,R26          ! INCR MOVED
         JSB  =FXRST-          ! RESET POINTERS
         JSB  =MOVUP           !
FXRTN    RTN                   !
!
INSRT    LDM  R24,R12          ! LWA + 1 SOURCE
         DCM  R24              !
         LDM  R22,R12          !
         SBM  R22,R76          ! # BYTES TO MOVE
         LDM  R26,R12          !
         SBM  R26,R56          !
         CMM  R26,=5,0         ! CIF > 4
         JNG  INSEX            ! JIF NOT
         LDM  R56,R12          !
         ADM  R26,R12          !
         STM  R26,R12          !
         DCM  R26              !
         JSB  =MOVEDN          ! GO MAKE A HOLE
         LDM  R22,R12          !
         SBM  R22,R56          ! # BYTES
         LDM  R24,R56          ! FWA SOURCE
         LDM  R26,R76          ! FAW SINK
         JSB  =MOVUP           ! GOT INSERT
INSEX    LDM  R12,R56          !
         RTN                   !
!
DELET    STM  R36,R26          ! FWA SINK
         JSB  =SKPLN           !
         STM  R#,R24           ! FWA SOURCE
         SBM  R#,R26           ! BYTES
         LDM  R22,R12          !
         SBM  R22,R24          ! BYTES TO MOVE
         SBM  R12,R36          ! NEW R12
         SBM  R56,R36          ! NEW NXTMEM
         JSB  =MOVUP           ! GO MOVE EM
         RTN                   !
!
FXRSET   BIN                   !
         LDMD R34,=NXTMEM      !
         SBM  R34,R36          !
         STMD R34,=NXTMEM      !
FXRST-   LDMD R34,=STSIZE      !
         SBM  R34,R36          !
         STMD R34,=STSIZE      !
         LDMD R34,=TOS         !
         SBM  R34,R36          !
         STMD R34,=TOS         !
         SBM  R12,R36          !
         RTN                   !
!
! *****************************************************************
! MEMORY MOVE ROUTINES
! *****************************************************************
!
! MOVEDN ENTRY: (moves 'down', meaning to HIGHER addresses)
!   R22 BYTE COUNT
!   R24 LWA SOURCE (Last Word Available, ie, highest address to move)
!   R26 LWA SINK
!
MOVEDN   PUMD R50,+R6          ! DON'T BLOW AWAY R50
         ICM  R24              ! LWA +1 FOR POP
         ICM  R26              ! LWA + 1 FOR POP
MOVD10   SBM  R22,=10,0        ! -10
         JNG  MOVDL-           ! JIF NOT 10 LEFT
         POMD R50,-R24         ! SOURCE
         PUMD R50,-R26         ! TO SINK
         JMP  MOVD10           !
!
MOVDL-   ADM  R22,=10,0        !
         DCM  R24              !
         DCM  R26              !
         CLM  R32              !
         DCM  R32              ! - 1
         JMP  MOVEM            !
!
! MOVEUP ENTRY: (moves 'up', meaning to LOWER addresses)
!   R22 BYTE COUNT
!   R24 FWA SOUCE (First Word Available, ie, lowest address to move)
!   R26 FWA SINK
!
MOVUP    PUMD R50,+R6          ! DON'T BLOW AWAY R50
MOVU10   SBM  R22,=10,0        !
         JNG  MOVUL-           ! JIF NOT 10 LEFT
         POMD R50,+R24         ! SOURCE
         PUMD R50,+R26         ! TO SINK
         JMP  MOVU10           ! LOOP
!
MOVUL-   ADM  R22,=10,0        ! RESTORE R22
         CLM  R32              !
         ICM  R32              !
MOVEM    TSM  R22              ! ANY TO MOVE?
         JZR  EXMOV            ! JIF COUNT = ZERO
         LDBD R50,R24          ! LOAD SOURCE
         STBD R50,R26          ! STORE SINK
         ADM  R24,R32          ! UPDATE POINTERS
         ADM  R26,R32          !
         DCM  R22              ! DECR COUNT
         JNZ  MOVEM            !
EXMOV    POMD R50,-R6          ! RESTORE R50
         RTN                   !
!
! *****************************************************************
! RESERVE / RELEASE MEMORY
! *****************************************************************
! RESMEM - RESERVE AND ZERO MEMORY
! R54 = NUMBER BYTES
! R26 = FWA RESERVED AREA
!
RESMEM   LDM  R56,R54          !
         JSB  =RSMEM-          !
         CLM  R56              !
         RTN                   !
!
RSMEM-   SAD                   !
         BIN                   !
         CLE                   !
         LDMD R26,=LAVAIL      !
         SBM  R26,R56          ! FWA
         SBM  R26,=40,0        ! MUST BE 40 LEFT
         CMM  R12,R26          ! SEE IF ROOM
         JCY  ERRMEM           ! JIF NO
         ADM  R26,=40,0        ! RESTORE LAVAIL
         STMD R26,=LAVAIL      !
         LDMD R34,=FWCURR      !
         LDMD R32,X34,P.RMEM   !
         ADM  R32,R56          !
         STMD R32,X34,P.RMEM   !
         PAD                   !
         RTN                   !
!
ERRMEM   PAD                   !
!
         JSB  =ERROR           !
         BYT  19D              ! MEMORY OVERFLOW
!
         CLE                   !
         DCE                   !
         RTN                   !
!
! RELMEM - RELEASE MEMORY
!
RELMEM   LDMD R34,=FWCURR      !
         LDMD R56,X34,P.RMEM   !
         JZR  RELRTN           ! JIF NONE TO RELEASE
RLMEM-   SAD                   !
         BIN                   !
         LDMD R36,=LAVAIL      !
         ADM  R36,R56          ! NEW LAVAIL
         CMMD R36,=RTNSTK      !
         JNC  RELOK            ! JIF LAVAIL < RTNSTK
         JNZ  ERRMEM           ! JIF LAVAIL # NXTDIR
RELOK    STMD R36,=LAVAIL      !
         CLM  R56              !
         STMD R56,X34,P.RMEM   !
RELRT1   PAD                   !
RELRTN   RTN                   !
!
! *****************************************************************
! SECURITY CODES
! SECUR? EXPECTS A MASK IN R0 AND RETURNS E=0 IF NO SURE BIT IN THAT POSITION IS SET
! *****************************************************************
SECUR?   CLE                   !
         LDMD R36,=FWCURR      !
         LDBD R31,X36,P.SFLG   ! LOAD SECURE BITS
         ANM  R31,R0           ! AND WITH MASK
         JZR  NOSCUR           ! JIF NO SECURE
!
         JSB  =ERROR           !
         BYT  22D              ! SECURED
!
         CLE                   !
         ICE                   !
NOSCUR   RTN                   !
!
! *****************************************************************
! ERRN RUNTIME
! *****************************************************************
         BYT  0,55             !
ERNUM.   CLM  R36              ! MAKE MSB ZERO
         LDBD R36,=ERNUM#      ! GET ERROR NUMBER
         JSB  =CONBIN          ! CONVERT TO BINARY
         JMP  PUSH40           ! PUSH TO STACK
!
! *****************************************************************
! ERRL RUNTIME
! *****************************************************************
         BYT  0,55             !
ERRL.    LDMD R45,=ERLIN#      ! GET VALUE
         CLB  R47              ! ONLY 2 BYTES COUNT
         CMB  R46,=251         ! IST IT A999? (FINAL INVISIBLE LINE?)
         JNC  I#PU45           ! JIF NO
         LDB  R46,=231         ! CHANGE TO 9999
I#PU45   LDB  R44,=377         ! SET UP TO OUTPUT R45
PUSH40   PUMD R40,+R12         ! PUSH IT
         RTN                   ! DONE
!
! *****************************************************************
! DATE RUNTIME
! *****************************************************************
         BYT  0,55             !
DATE.    LDMD R45,=DATE        ! GET DATE
         JMP  I#PU45           ! PUSH IT TO STACK
!
! *****************************************************************
! TEST EOL
! *****************************************************************
TSTEN+   DRP  R20              !
TSTEND   BIN                   !
         CLE                   ! PRESET FLAG TO "END OF STATEMENT"
         CMB  R#,=16           ! CR (EOL TOKEN)?
         JZR  TSTENX           !
         CMB  R#,=100          ! @ (CONCATENATED BASIC STATEMENT)?
         JZR  TSTENX           !
         CMB  R#,=233          ! ! (REMARK TOKEN)?
         JZR  TSTENX           !
         ICE                   ! SET FLAG TO "NOT END OF STATEMENT"
TSTENX   RTN                   !
!
! *****************************************************************
! CHECKSUM AN 8K ROM
! *****************************************************************
RSUM8K   LDM  R34,=377,17      ! COUNT = (8K/2)-1
RSUM#K   CLM  R40              ! SUM=0, DATA REG=0
RSUM     POMD R36,+R32         ! POP 2 BYTES FROM ROM
         ADM  R44,R36          ! ADD TO SUM
         DCM  R34              ! DECREMENT COUNT
         JNZ  RSUM             ! REPEAT TIL COUNT=0
         ADM  R46,R44          ! ADD MSREG TO LSREG
         NCM  R46              ! COMPLEMENT SUM
         CMMD R46,R32          ! COMPL SUM = CHECKSUM?
         RTN                   ! RETURN Z=TRUE IF CHECKSUM OK
!
         BSZ  23               ! UNUSED BYTES TO END OF 8K ROM
!
         BYT  330,113,41,10    ! ROM CHECKSUMS
         FIN
