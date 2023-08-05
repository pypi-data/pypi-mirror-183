         ABS 40000
THIRT2   EQU 32
THIRT4   EQU 34
! ********************************************************************
! * ALLOCATION ROUTINES
! * THIS ROUTINE ALLOCATES ALL VARIABLES IN THE CURRENT PROGRAM (E.G.
! * THE ONE WHOSE PCB IS POINTED TO BY FWCURR). THE ROUTINE IS ENTERED
! * BY JSB AND SAVES AND RESTORES THE DCM FF STATUS.  IT REQUIRES NO
! * INPUT OTHER THAN THE GLOBAL SYSTEM POINTERS, HOWEVER ALL RESTISTERS
! * BEGINNING WITH R22 ARE CONSIDERED VOLATILE.
! ********************************************************************
!
! ********************************************************************
! ROMTOK/ROM#/TOKEN
! ********************************************************************
EROM     POMD R36,-R6          ! TRASH ONE RETURN
         JSB  =ROMCLA          ! GET ROM CLASS
         CMB  R17,=300         ! ROM MISSING?
         JCY  NXTBAD           ! JIF YES
         JMP  NXTGUD           ! ELSE LOOP
!
ROMCLA   LDM  R36,=GETNXT      ! JUMP ADDR
         JSB  =EXTRJM          ! GET ROM CLASS
ROMCL-   CMB  R36,=57          ! ROM CLASS?
         JNC  ROMCLR           ! JIF NO
         CLM  R36              ! ELSE = -1
         DCM  R36              !
! NOTE EXTRJM MAY SET ERRORS
ROMCLR   RTN                   ! AND RETURN
! ********************************************************************
! INITIALIZATION PART
! ********************************************************************
ALLOC    SAD                   ! SAVE DCM FF
         STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         PUMD R20,+R6          ! SAVE R20
         TSB  R16              !
         JOD  ALLO1            ! JIF CALC MODE
         JSB  =TSTALO          !
         JEN  XALLR            ! JIF ALLOCATED
         LDBD R#,X56,P.TYPE    !
         ADB  R#,=40           ! SET ALLOCATE BIT
         STBD R#,X56,P.TYPE    ! AND STORE BACK
ALLO1    BIN                   ! BINARY MODE
         LDB  R24,=10          ! ROMFL ALLOC
         JSB  =ALINI           ! INIT ROUTINE
! ********************************************************************
! MAIN LOOP
! ********************************************************************
NXTONE   CLM  R56              !
         STMD R56,=COMMON      ! COMMON DECLARED THIS TOK
         JSB  =GETNXT          ! GET NEXT TOKEN
NXTGUD   STMD R24,=ERRSTP      !
         CMB  R17,=300         ! ERR CHK FOR BIN PROG
         JCY  NXTBAD           !
         CMB  R36,=30          !
         JPS  NXTONE           ! JIF NOT ALLOCATABLE
         LLM  R36              !
         LDMD R36,X36,JATAB    ! GET JUMP ADDR
         JSB  X36,ZRO          ! GO ALLOCATE
         CMB  R17,=300         ! TEST ERRORS
         JNC  NXTONE           ! LOOP IF NO ERRORS
NXTBAD   TSB  R16              !
         JOD  XALL0            ! JIF CALC MODE
         STBD R17,=ERRTYP      ! REPORT LINE#
         JSB  =DALLOC          ! ELSE DEALLOCATE
         LDMD R36,=FWCURR      ! CLEAN UP AND GET OUT
         LDMD R12,X36,P.LEN    !
         ADM  R12,R36          !
         STMD R12,=NXTMEM      !
XALL0    CLE                   !
         DCE                   !
         JMP  XALL2            !
!
XALLR    JMP  XALL             ! PIGGY BACK JUMP
! ********************************************************************
! END OF CURRENT LINE OR DATA STMT
! ********************************************************************
SKPNXT   JSB  =SKIPL           ! SKIP THIS LINE
XALL1    POMD R36,-R6          ! RETURN ADDRESS
         JSB  =NXTLIN          !
         JEN  NXTONE           ! JIF NOT LAST LINE
         TSB  R16              !
         JOD  XALL             ! JIF CALC
         LDMD R2,=DFPAR1       ! DEF ACTIVE?
         JZR  XALL1A           ! JIF NO
!
         JSB  =ERROR           !
         BYT  38D              ! NO FNEND
!
         JMP  NXTBAD           !
XALL1A   STMD R30,=NXTMEM      !
         STM  R30,R12          !
         STMD R30,=STSIZE      !
         STMD R30,=TOS         !
         SBM  R30,R26          ! # BYTES
         ICM  R30              !
         ICM  R30              !
         PUMD R30,-R26         !
         JSB  =OPTIOX          ! SET OPTION BASE
! RETURNS WITH FWCURR IN R56
         LDMD R36,=NXTCOM      !
         SBMD R36,=FWUSER      ! LEN COMMON
         STMD R36,X56,P.COM    !
XALL     CLE                   !
XALL2    CLM  R20              !
         STMD R20,=ERRSTP      !
         POMD R20,-R6          ! RESTORE R20
         STBD R20,=GINTEN      ! ENABLE INTERRUPTS
         PAD                   !
         RTN                   !
! ********************************************************************
! ALLOCATE JUMP TABLE
! ********************************************************************
         DEF  ROMINI           ! -1 ROM CLASS > 56
JATAB    DEF  XALL1            ! 0  EOL
         DEF  VALOC            ! 1  FETCH VAR
         DEF  BININT           ! 2  INTEG CONST
         DEF  SVAL             ! 3  STORE VAR
         DEF  SKPCON           ! 4  REAL CONST
         DEF  SKPCON           ! 5  STR CONST
         DEF  FUNCAL           ! 6  USER FN CALL
         DEF  LINEAL           ! 7  JTRU LINE #
         DEF  LINEAL           ! 10 GOTO GOSUB
         DEF  RELJMP           ! 11 JMP REL
         DEF  DEFFN            ! 12 USER DEF
         DEF  DEFEND           ! 13 FNEND
         DEF  EROM             ! 14 EXT ROM
         DEF  OPTION           ! 15 OPTION BASE
         DEF  DEFEND           ! 16 FN RET
         DEF  FNASN            ! 17 FN LET
         DEF  SKPNXT           ! 20 DATA
         DEF  DIM              ! 21 DIM
         DEF  SHORT            ! 22 SHORT
         DEF  INT              ! 23 INTEGER
         DEF  COMM             ! 24 COM
         DEF  LINEAL           ! 25 ELSE JMP#
         DEF  RELJMP           ! 26 ELSE JMP REL
         DEF  LINEAL           ! 27 USING LINE #
! ********************************************************************
! FN LET/VAR TOK/NAME/NAME
! ********************************************************************
FNASN    POBD R23,+R24         ! GET VAR TOKEN
         ADB  R23,=200         ! FUNC FLAG
         LDMD R36,=DFPAR1      !
         JZR  DFERR            ! JIF NOT DEF
         LDMD R36,R24          ! NAME
         JSB  =FRMNA#          !
         LDMD R66,=FWCURR      !
         ADMD R66,=CURFUN      ! FUNC POINTER
         CMMD R36,R66          ! CORRECT FUNCTION?
         JNZ  DFERR            !
FNR3     LDMD R66,=CURFUN      ! DEF ADDR
         PUMD R66,+R24         !
         RTN                   !
! ********************************************************************
! RELJMP TOKEN/VAL/VAL
! ********************************************************************
RELJMP   ICM  R24              !
         ICM  R24              !
FRRET    RTN                   !
! ********************************************************************
! FNEND TOKEN/NAME/NAME
! ********************************************************************
DFERR    JSB  =ERROR+          !
         BYT  39D              ! NOT IN ACTIVE DEF
!
DEFEND   LDMD R66,=DFPAR1      !
         JZR  DFERR            !
         DCM  R66              ! DECR DEF POINTER
         CLM  R76              ! REL DEF JMP ADDR =
         LDB  R76,R47          !   BYTES +
         ADMD R76,=PCR         !   PCR +
         ADM  R76,=3,0         !   3 -
         SBMD R76,=FWCURR      !   FWCURR
         PUMD R76,-R66         ! STORE JUMP ADDR
DEFND1   JSB  =FNR3            ! GET DEF ADDR
         CLM  R#               !
         STMD R#,=DFPAR1       ! CLEAR ACTIVE DEF
         RTN                   !
! ********************************************************************
! SUBROUTINE VALOC
! THIS ROUTINE IS CALLED TO ALLOCATE A VARIABLE.  IT WILL BE ALLOCATED
! IN THE CURRENT PROGRAM AREA IF RUN, ELSE IT WILL BE ALLOCATED IN THE
! AREA POINTED TO BY LAVAIL.  IF RUN, THE VARIABLE WILL BE ASSIGNED AN
! ADDRESS RELATIVE TO FWCURR.  OTHERWISE AN ABSOLUTE ADDRESS WILL BE ASSIGNED.
!
! INPUT REGISTERS
!  R16     = CALC MODE FLAG
!  R20     = SCRATCH
!  R22     = ZERO IF DIM
!  R23     = TOKEN
!  R24     = PTR TO NAME IN STACK
!  R26     = FWA VARIABLES (IF RUN)
!  R30     = NEXT VARIABLE (IF RUN)
!  R40-R44 = PCB 7 - 11 (IF RUN)
!  R45-R47 = LINE # AND BYTES (IF RUN)
!
! OTHER REGISTERS USED
!  R32     = CURRENT VRBL PTR FOR SEARCH
!  R34     = SCRATCH
!  R36     = VARIABLE NAME FORM
!  R50-R77 = SCRATCH
! ********************************************************************
! NOTE - A() AND A(,) ALSO COME HERE WITH TOKENS 37 AND 40 RESPECTIVELY.
! FOR THESE TWO CASES THE TOKEN IS FORCED TO 2 FOR THE FRMNAM CALL AND
! THEN RESTORED.  IF THE ARRAY HAS NOT ALREADY BEEN DECLARED, E.G. VSRCH
! FAILS, THEN NARDIM CHECKS FOR TOKENS 37 AND 40 AND ALLOCATES THE
! DEFAULT ARRAY.
! ********************************************************************
! VAR TOKEN/NAME/NAME
! ********************************************************************
SVAL     SBB  R23,=20          !
VALOC    PUBD R23,+R6          ! SAVE TOKEN
         CMB  R23,=300         ! A() OR A(,) ?
         JNC  VALOC1           ! JIF NO
         LDB  R23,=2           ! LOOKS LIKE ARRAY
VALOC1   JSB  =FRMNAM          ! GO FORM NAME
         LDM  R52,R24          ! SAVE 24-31
         POBD R23,-R6          ! RESTORE TOKEN
         PUMD R52,+R6          ! SAVE PGM PTR
         LDMD R56,=DFPAR1      ! FN FLAG
         JZR  NTDEF            ! JIF NOT IN DEF
! ********************************************************************
! VARIABLES WITHIN DEFS
! ********************************************************************
         STM  R56,R26          ! FWA DEF VARIABLES
         LDMD R30,=DFPAR2      ! LWA DEF VARIABLES
         JSB  =VSRCH           !
         JEN  FNDIT            ! JIF FOUND
         POMD R74,-R6          !
         PUMD R74,+R6          ! SAVE IT
         STM  R74,R26          !
! ********************************************************************
! SEE IF THERE IS AN ALLOCATED PROGRAM
! ********************************************************************
NTDEF    JSB  =TSTALO          !
         BIN                   ! TSTALO SETS BCD
         JEZ  NOFIND           ! JIF NOT ALLOC
! ********************************************************************
! SEARCH FWCURR VARIABLE AREA
! ********************************************************************
         JSB  =VSRCH           ! SEARCH FOR VARIABLE
         JEZ  NOFIND           ! JIF NOT FOUND
TSTDUP   TSB  R22              ! CIF DIM
         JNZ  FNDIT            ! JIF NOT
!
         JSB  =ERROR           !
         BYT  35D              ! COM OR DIM EXISTING VRB
!
         JMP  FNDIT            !
!
NOFIND   TSB  R16              !
         JEV  RNMOD            ! JIF NOT CALC
! ********************************************************************
! SEARCH CALC MODE VARIABLE AREA
! ********************************************************************
         LDMD R26,=LAVAIL      ! FWA CALC VARIABLES
         LDMD R30,=CALVRB      !
         JSB  =VSRCH           !
!
! NOW IF FOUND, GO CHECK DUP DIM
! TO CATCH INTEGER A   SHORT A IN CALC MODE
!
         JEN  TSTDUP           ! JIF FOUND
! ********************************************************************
! VARIABLE NOT FOUND SO ALLOCATE
! ********************************************************************
RNMOD    JSB  =VSTOR           ! STORE VARIABLE
         TSB  R16              !
         JOD  FNDIT            ! JIF CALC
         POMD R56,-R6          ! TRASH OLD R30
         PUMD R30,+R6          ! SAVE NEW
! ********************************************************************
! VARIABLE ALLOCATED SO STORE ADDR
! ********************************************************************
FNDIT    POMD R30,-R6          ! RESTORE LWA + 1 VAR
         POMD R26,-R6          ! RESTORE FWA VAR VAR
         POMD R34,-R6          ! PROGRAM PTR
         TSB  R16              !
         JOD  RTNADR           ! JIF CALC
         LDMD R56,=COMMON      ! COMMON DECL THIS TOKEN
         ADM  R26,R56          !
         ADM  R30,R56          !
         ADM  R34,R56          !
         ADM  R32,R56          !
         SBMD R32,=FWCURR      ! RELATIVE ADDR IF RUN
RTNADR   CMB  R17,=300         ! ERRORS?
         JCY  RTNAD1           ! DONT STORE IF ERRORS
         PUMD R32,-R34         ! STORE ADDRESS
RTNAD1   RTN                   !
! ********************************************************************
! SUBROUTINE VSRCH
! THIS ROUTINE SEARCHES THE ALLOCATED VARIABLES FOR A MATCH ON THE NAME
! PASSED IN R36.  ON EXIT R32 WILL POINT TO THE VARIABLE IF FOUND, ELSE
! TO THE END OF THE LIST.  E # 0 IF FOUND ELSE E = 0.
! ********************************************************************
VSRCH    LDM  R32,R26          ! FWA VARIABLES
         ANM  R36,=317,377     ! CLEAR INT & SHORT
VLOOP    CLE                   ! SET NOT FOUND
         CMM  R32,R30          ! SEE IF DONE
         JCY  VSRTN            ! EXIT IF DONE
         ICE                   ! GET FOUND
         LDMD R66,R32          ! GET NAME
         ANM  R66,=317,77      ! CLEAR REMOTE, SHORT, INT,
         CMM  R66,R36          ! SEE IF MATCH
         JZR  VSRTN            ! JIF YES
         JSB  =SKPVR           ! GET NEXT VAR
         JMP  VLOOP            !
!
VSRTN    ADBD R36,=DIMFLG      ! RESTORE INT,SHORT,REAL
         RTN                   !
!
SKPVR    POMD R74,+R32         ! SKIP OVER NAME + 2
         TSB  R75              !
         JNG  VRTN             ! JIF REMOTE
         LLB  R75              ! TRACE
         LLB  R75              ! FUNC
         TSB  R75              !
         JPS  NOTFN            ! JIF NOT FUNC
         ADM  R32,=11,0        ! TRASH RTN,PCR,TOS,MEM,C
         POMD R76,+R32         ! NEW 76
NOTFN    STB  R74,R66          ! SAVE THE CLASS
         CMB  R74,=100         ! STR OR ARRAY?
         JCY  SARRAY           ! JIF STR OR ARRAY
         BCD                   !
         LRB  R66              ! TYPE LOWER
         ANM  R66,=3,0         ! AND ISOLATE
         BIN                   !
         JZR  VRTN+            ! JIF REAL
! ********************************************************************
! R66 CONTAINS A 1 IF THE CLASS IS INT AND A 2 IF THE CLASS IS SHORT.
! THIS CORRESPONDS TO THE AMOUNT TO BE SKIPPED.  NOTE - WE SKIPPED
! 2 WITH THE POP AT LABEL SKPVR.
! ********************************************************************
         ADM  R32,R66          ! ONE IF INT, 2 IF SHORT
         RTN                   !
!
SARRAY   ADM  R32,R76          ! ADD LEN
         DCM  R32              !
         DCM  R32              ! INC 4 FOR STR OR ARRAY
VRTN+    ADM  R32,=6,0         !
VRTN     RTN                   !
!
! SUBROUTINE VSTOR
! THIS ROUTINE STORES THE VARIABLE NAME AND DESCRIPTION IN THE VAR AREA
! ********************************************************************
VSTOR    LDM  R56,=10,0        !
         LDB  R76,R36          ! NAME
         JNG  STRR             ! JIF STRING
         BCD                   !
         LRB  R76              !
         BIN                   !
         CMB  R76,=4           ! TYPE > 3 ?
         JCY  STARR            ! JIF ARRAY
! ********************************************************************
! ALLOCATE SIMPOLE NUMERIC VARIABLE
! HEADER FORMAT IS: R76  NAME
!                        NAME
! ********************************************************************
         TSB  R76              !
         JZR  VSTOR1           ! JIF REAL
         ICB  R76              ! +2
         ICB  R76              !
         STB  R76,R56          !
VSTOR1   LDM  R#,R36           ! STORE NAME
         LDB  R0,=76           !
         LDM  R20,=2,0         !
VSTOR2   JSB  =STOR1           !
         RTN                   !
! ********************************************************************
! HEADER FORMAT IS:
!    R72 NAME
!        NAME
!        TOT LEN
!        TOT LEN
!        MAX LEN
!        MAX LEN
!        ACT LEN
!        ACT LEN
! ********************************************************************
STRR     STM  R56,R20          ! =10,0
         LDM  R56,=22,0        ! ASSUME NOT DIM
         LDB  R0,=70           ! ITS A STRING
         STM  R36,R70          ! STORE NAME
         TSB  R22              !
         JNZ  VSTR1            ! NICE GUESS YOU FOX
! ***** ALLOCATE DIMENSIONED STRINGS ***************
         JSB  =GETINT          !
         LDM  R56,R76          !
VSTR1    STM  R56,R72          !
         STM  R56,R74          ! MAX LEN
         JMP  VSTOR2           !
! ********************************************************************
! ALLOCATE ARRAYS
! HEADER FORMAT IS:
!  R70  NAME
!       NAME
!       TOTAL LEN
!       TOTAL LEN
!       MAX ROW
!       MAX ROW
!       MAX COL/377
!       MAX COL/377
! ********************************************************************
STARR    LDMD R76,=OPTBAS      !
         JPS  STARR1           ! JIF SET
         CLM  R76              !
         ICM  R76              !
         STMD R76,=OPTBAS      ! ELSE SET IT
STARR1   LDB  R0,=70           !
         STM  R36,R70          ! STORE NAME
         CLM  R72              !
         STMD R74,=RSTAR       ! ZERO RSTAR/CSTAR
         LDB  R74,=12          ! ASSUME NOT DIM VECTOR
         LDM  R20,R56          ! 10,0
         TSB  R22              !
         JNZ  NARDIM           ! JIF NOT ARRAY DIM
! **** ALLOCATE DIMENSIONED ARRAYS ****
         JSB  =GETINT          !
         STM  R76,R74          !
         CLM  R76              !
         DCM  R76              ! 377,377
         JSB  =GETINT          !
         JMP  STOR1C           ! GO CALC ARRAY SIZE
! ********************************************************************
! ALLOCATE DEFAULT ARRAYS
! ENTRY IS AT NARDIM
! SEARCH FORWARD USING GETNXT UNTIL THE "MATCHING" INDEX TOKEN IS FOUND
! AND ALLOCATE 1 OR 2 DIMENSIONS BASED ON THAT TOKEN.  IF A VARIABLE IS
! ENCOUNTERED DURING THE SEARCH, R24 WILL BE RESET TO THE VARIABLE SO NONE
! ARE SKIPPED.
! ********************************************************************
SAVIT    LDMD R66,=RSTAR       !
         JNZ  SAVIT1           ! JIF ALREADY SET
         STMD R24,=RSTAR       ! SAVE STACK PTR
SAVIT1   ICM  R24              !
         ICM  R24              !
         CMB  R23,=2           ! SEE IF ARRAY
         JNZ  NARD1            ! JIF NOT
NARDIM   CMB  R23,=300         ! A() OR A(,)
         JCY  STOR()           ! JIF YES
         LDBD R23,=CSTAR       !
         ICB  R23              !
         STBD R23,=CSTAR       ! INC ARRAY CTR
NARD1    JSB  =GETNXT          ! NEXT TOKEN
         TSM  R36              !
         JZR  ILLDIM           !
SFSG     CMB  R#,=32           ! CIF SUBS DIM 11-14
         JZR  TSTINX           !
         CMB  R#,=2            ! CIF INTEGER
         JNZ  NOTIN            ! JIF NO
         JSB  =BININT          !
         JMP  NARD1            !
NOTIN    CMB  R#,=4            !
         JNG  SAVIT            ! JIF VARIABLE
         JNZ  NARD1            ! JIF NOT CONSTANT
         JSB  =SKPCON          !
         JMP  NARD1            !
!
TSTINX   LDBD R67,=CSTAR       !
         DCB  R67              !
         STBD R67,=CSTAR       !
         JNZ  NARD1            ! JIF NOT THIS ARRAY
STOR()   LDB  R76,=12          !
         TSB  R23              !
         JEV  STOR0            ! JIF TWO DIM
         CLM  R76              !
         DCM  R76              ! 377,377
STOR0    LDMD R66,=RSTAR       !
         JZR  STOR1C           ! JIF STACK OK
         DCM  R66              !
         STM  R66,R24          ! ELSE RESET POINTER
STOR1C   LDMD R66,=OPTBAS      !
STOR1D   TCM  R66              ! 0 IF 1, ELSE -1 IF 0
         CMM  R66,R74          !
         JZR  ILLDIM           ! JIF OPTBAS 1 DIM 0
         TSM  R76              !
         JNG  STOR1E           ! JIF VECTOR
         CMM  R66,R76          !
         JZR  ILLDIM           ! JIF OPTBAS 1 DIM 0
STOR1E   JSB  =CALCSZ          !
         STM  R56,R72          !
STOR1    LDBD R67,=COMFLG      !
         JNZ  STOR1Y           ! JIF COM
         GTO STOR1X            !
!
ILLDIM   JSB  =ERROR+          !
         BYT  36D              ! ILLEGAL DIM
!
! ********************************************************************
! COMMON DECLARATION
! HEADER FORMAT IS:
!   R74 NAME
!       NAME W/REMOTE BIT
!       REMOTE ADDR
!       REMOTE ADDR
! ********************************************************************
STOR1Y   PUMD R70,+R6          !
         PUMD R56,+R6          !
         PUBD R0,+R6           !
         PUMD R20,+R6          !
         LDM  R20,=4,0         !
         LDM  R74,R*           !
         LDMD R76,=NXTCOM      !
         ICM  R76              !
         ICM  R76              ! POINT TO DATA
         ADB  R75,=200         ! SET REMOTE FLAG
         CLM  R56              !
         LDB  R0,=74           !
         JSB  =STOR1X          ! GO STORE IT
         POMD R20,-R6          !
         POBD R0,-R6           !
         POMD R56,-R6          !
         POMD R70,-R6          !
         LDBD R36,=DCLCOM      !
         JNZ  DECLAR           ! JIF ORIG DECLARATION
         LDMD R36,=NXTCOM      !
         CMMD R36,=FWPRGM      !
         JCY  COMERR           ! TOO MUCH COMMON
         LDMI R60,=NXTCOM      ! CIF TYPES MATCH
         LDB  R37,R60          !
         XRB  R37,R*           !
         ANM  R37,=360         ! ISOLATE STR ARR TYPE
         JNZ  COMERR           ! TYPE MISMATCH
         CMB  R0,=76           ! CIF SIMPLE
         JZR  ADDCOM           ! JIF YES
         ICM  R0               ! SKIP NAME
         ICM  R0               !
         LDM  R2,R62           ! MAX LEN STR OR ARRAY LEN
         CMM  R2,R*            ! MATCH?
         JNZ  COMERR           ! DONT MATCH
ADDCOM   ADM  R56,R20          ! TOTAL SIZE
ADDC1    ADMD R56,=NXTCOM      !
         STMD R56,=NXTCOM      !
         RTN                   !
!
COMERR   JSB  =ERROR+          !
         BYT  32D              ! COM ITEM MISMATCH
!
DECLAR   JSB  =TSTRM           ! CIF ROOM
         JNC  NOROOM           ! JIF NO
         LDM  R62,R22          !
         PUMD R62,+R6          ! SAVE R22-R27
         PUMD R32,+R6          !
         LDM  R22,R30          ! NXTMEM
         SBMD R22,=NXTCOM      ! # BYTES
         LDM  R24,R30          ! NXTMEM
         DCM  R24              ! LWA SOURCE
         STM  R24,R26          !
         ADM  R26,R56          !
         ADM  R26,R20          ! LWA SINK
         LDM  R12,R26          !
         ICM  R12              !
         STMD R12,=NXTMEM      !
         JSB  =MOVDN           !
         POMD R32,-R6          !
         POMD R62,-R6          !
         STM  R62,R22          ! RESTORE R22-R27
         PUMD R30,+R6          ! SAVE R30
         LDMD R30,=NXTCOM      !
         JSB  =STOR2R          !
         POMD R30,-R6          ! RESTORE R30
         ADM  R24,R20          ! BECAUSE WE MOVED THINGS
         STM  R20,R56          !
         STMD R20,=COMMON      !
         ADMD R20,=FWCURR      !
         STMD R20,=FWCURR      !
         LDMD R76,=STSIZE      !
         ADM  R76,R56          !
         STMD R76,=STSIZE      !
         JSB  =ADDC1           !
         STMD R#,=FWPRGM       !
         RTN                   !
!
NOROOM   JSB  =ERROR+          !
         BYT  19D              ! MEMORY OVERFLOW
!
STOR1X   JSB  =TSTRM           !
         JNC  NOROOM           ! JIF NOT ENOUGH MEM
         TSB  R16              ! TEST RUNFLAG
         JEV  STOR2            ! JIF NOT CALC
         STM  R36,R30          !
         STM  R36,R32          !
         STMD R36,=LAVAIL      !
STOR2    JSB  =STOR2R          ! STORE IT
         TSB  R16              !
         JEV  STOR3X           ! JIF RUN
         LDMD R36,=LAVAIL      ! FWA THIS VAR
         PUMD R32,+R6          ! SAVE R32
         LDM  R32,R36          !
         ADM  R32,R20          ! LWA THIS VAR
         JSB  =INIVLP          ! INITIALIZE IT
         POMD R32,-R6          ! RESTORE R32
         RTN                   !
!
STOR3X   ADM  R30,R20          ! ADD # BYTES
         STMD R30,=NXTMEM      ! UPDATE NEXT MEM
         STM  R30,R12          !
         RTN                   !
!
! ********************************************************************
! SUBROUTINE LINEAL
! THIS ROUTINE ALLOCATES LINE # REFERENCES BY REPLACING THE LINE #
! REFERENCE WITH ITS ADDRESS RELATIVE TO FWCURR.
!    JMP TOKEN/LINE#/LINE#
! ********************************************************************
LINEAL   LDMD R76,R24          ! GET LINE #
         JSB  =FNDLIN          ! GO FIND LINE #
         JEZ  FNDLN            ! JIF FOUND
!
         JSB  =ERROR+          !
         BYT  57D              ! REF NON-EXISTANT LINE
!
FNDLN    SBMD R36,=FWCURR      !
         PUMD R36,+R24         ! STORE IT
         RTN                   !
!
! ********************************************************************
! FN ALLOCATION
! THIS ROUTINE ALLOCATES USER DEFINED FUNCTIONS.
!    DEF TOKEN/NAME/NAME/JMP ADDR/JMP ADDR/2*PARAMS+STR/---PARAMS---
! ********************************************************************
DEFFN    LDMD R34,=DFPAR1      !
         JNZ  DEFDEF           ! JIF DEF WITHIN DEF
         LDM  R34,R24          !
         LDMD R73,R24          !
         LDB  R23,R77          !
         ANM  R23,=1           ! 1 IF STR
         LLB  R23              ! 2 IF STR
         ADB  R23,=201         ! 201 OR 203
         JSB  =CRDF?           ! ALLOC DEF IF NOT ALREADY
         JEZ  GOSTO1           ! JIF NEW
         LDMD R74,R32          ! NAME AND ADDR
         TSM  R76              !
         JNZ  DUPDEF           ! JIF ADDR # 0
         JSB  =GTADR           ! STORE ADDR
         STMD R74,R32          ! STORE IT BACK
GOSTO1   STM  R24,R34          !
         SBMD R32,=FWCURR      ! MAKE ADDRESS REL
         PUMD R32,-R34         ! PUSH ADDR
         STMD R32,=CURFUN      ! SAVE FOR FNEND ALLOCATION
         POMD R75,+R24         !
         STMD R24,=DFPAR1      !
         JSB  =SKPRS           !
         STMD R24,=DFPAR2      !
         RTN                   !
!
DUPDEF   JSB  =ERROR+          !
         BYT  37D              ! DUPLICATE DEF
!
DEFDEF   JSB  =ERROR+          !
         BYT  38D              ! DEF WITHIN DEF
!
GTADR    LDM  R76,R34          ! ADDR
         JZR  GTADR1           ! JIF REF FN
         SBMD R76,=FWCURR      ! REL ADDR
         ADM  R76,=4,0         !
GTADR1   RTN                   !
!
CRDF?    JSB  =FRMNAM          !
         JSB  =VSRCH           !
         JEN  CRDF1?           ! JIF FOUND
         STM  R36,R72          ! NAME
         JSB  =GTADR           ! REL ADDR IN R76
         STM  R#,R74           ! STORE ADDR
         CLM  R#               !
         LDM  R56,=17,0        ! ASSUME NOT STR
         LDM  R20,=6,0         !
         LDB  R0,=72           !
         CMB  R23,=201         !
         JNZ  GOSTO            ! JIF STR
         JSB  =STOR1           !
         JMP  GOSTOS           !
GOSTO    LDM  R56,=37,0        ! STR LEN
         JSB  =STOR1           !
         LDM  R76,R12          !
         SBM  R76,=30,0        ! POINT AT TOT LEN
         LDM  R66,=22,0        !
         PUMD R66,+R76         ! STORE TOT LEN
         PUMD R66,+R76         ! STORE MAX LEN
GOSTOS   CLE                   ! SET NEW
CRDF1?   RTN                   !
!
! ********************************************************************
! ALLOCATE FN CALL
! THIS ROUTINE ALLOCATES USER FUNCTION CALLS.
!   FN CALL TOKEN/NAME/NAME/# PARAMS/--PARAM TYPES(1 BYTE EACH)
! ********************************************************************
FUNCAL   CMB  R16,=1           !
         JZR  ILLCOM           !
         SBB  R23,=25          ! MAKE IT RIGHT
         JOD  NTSTRF           !
         ICB  R23              !
NTSTRF   ADB  R#,=200          ! FUNC FLAG
         CLM  R34              !
         JSB  =CRDF?           !
         LDM  R34,R24          !
         CLM  R66              !
         POBD R66,+R24         ! # PARAMS IN CALL
         SBMD R32,=FWCURR      ! MAKE IT RELATIVE
         PUMD R32,-R34         ! PUSH ADDR
         ADM  R24,R66          !
         RTN                   !
!
ILLCOM   JSB  =ERROR+          !
         BYT  88D              ! ILLEGAL STATEMENT
!
COMM     TSB  R16              !
         JOD  ILLCOM           ! COM IN CALC MODE
         LDMD R34,=DFPAR1      ! DEF?
         JNZ  ILLCOM           ! COM IN DEF ILLEGAL
         LDMD R34,=FWCURR      !
         LDBD R57,X34,P.TYPE   !
         LDB  R36,=200         !
         ORB  R36,R57          ! SET COMMON DECLARER FLAG
         STBD R36,X34,P.TYPE   !
         LDMD R36,=FWUSER      !
         CMMD R36,=FWPRGM      !
         JNZ  COMRTN           ! JIF ALREADY SOME
         STBD R37,=DCLCOM      ! SET COMMON DECLARATION
COMRTN   STBD R22,=COMFLG      ! SET COMMON FLAG
         CLB  R22              ! SET DIM FLAG
         RTN                   !
!
DIM      CLB  R76              ! DIMFLG = 0
         JMP  DIMCOM           !
!
INT      LDB  R76,=20          ! DIMFLG = 20
         JMP  DIMCOM           !
!
SHORT    LDB  R76,=40          ! DIMFLG = 40
DIMCOM   STBD R#,=DIMFLG       !
         CLB  R22              ! DIM FLAG
         RTN                   !
!
COMMD    RTN                   !
!
OPTION   LDMD R76,=OPTBAS      !
         JPS  OPTERR           !
         LDMD R75,R24          ! 32 AND TWO BYTES OF INT
         DCM  R76              ! 0 IF 1, 377 IF 0
         TCM  R76              ! 377 IF 0, 0 IF 377
         STMD R76,=OPTBAS      !
         RTN                   !
!
OPTERR   JSB  =ERROR+          !
         BYT  30D              ! ILLEGAL OPTION BASE
!
! ********************************************************************
! DEALLOCATION ROUTINES
!
! THIS ROUTINE DEALLOCATES ALL VARIABLE IN THE CURRENT PROGRAM IF ERRSTP
! IS ZERO.  IF ERRSTP IS NON-ZERO THEN DEALLOCATION CEASES AT THE TOKEN
! POINTED TO BY ERRSTP.
!
! THE ROUTINE IS ENTERED BY A JSB AND SAVES AND RESTORES THE DCM FF STATUS.
! IT REQUIRES NO INPUT OTHER THAN THE GLOBAL SYSTEM POINTERS, HOWEVER
! ALL REGISTERS BEGINNING WITH R20 ARE CONSIDERED VOLATILE.
!
! ********************************************************************
DALLOC   SAD                   ! SAVE DCN FF
         TSB  R16              !
         JOD  DALOC1           ! JIF CALC MODE
         JSB  =TSTALO          !
         JEN  DALLOD           ! JIF ALLOCATED
DALOC1   PAD                   !
         RTN                   !
!
DALLOD   BIN                   !
         STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         LDB  R24,=1           !
         STBD R24,=CONTOK      ! CONT NOW ILLEGAL
         LDMD R24,=FWCURR      !
         LDBD R24,X24,P.TYPE   !
         JPS  NEXTI            ! JIF NOT COMMON DECLARER
! **** DEALLOCATE COMMON ****
         LDMD R24,=FWPRGM      ! SOURCE
         STM  R24,R36          !
         LDMD R26,=FWUSER      ! SINK
         STMD R26,=FWPRGM      ! RESET FWPRGM
         STMD R26,=FWCURR      !
         LDM  R22,R12          !
         SBM  R22,R24          ! BYTES TO MOVE
         SBM  R36,R26          ! BYTES OF COMMON
         JSB  =FXRSET          ! GO ADJUST POINTERS
         LDMD R76,=ERRSTP      !
         JZR  DALLY            !
         SBM  R76,R36          !
         STMD R76,=ERRSTP      !
DALLY    JSB  =MOVUP           !
NEXTI    LDB  R24,=11          ! DALLOC ROMFL
         JSB  =ALINI           ! INIT ROUTINE
         ADM  R30,R26          ! LWA+1 VRBLS
         DCM  R30              !
         DCM  R30              !
!
! **** MAIN LOOP ****
!
NEXT     JSB  =GETNXT          ! GET NEXT VRBL
         CMMD R24,=ERRSTP      !
         JNZ  NEXT1            ! JIF NOT AT ERRSTP
         CLB  R47              !
         STMD R45,=AUTO#       ! LINE # FOR ERROR ROUTINE
         JMP  XDALL2           ! ELSE EXIT
!
NEXT1    CMB  R36,=30          !
         JPS  NEXT             ! JIF NOT DEALLOCATABLE
         LLM  R36              !
         LDMD R36,X36,JDTAB    ! GET JUMP ADDRESS
         JSB  X36,ZRO          ! GO DOIT
         CMB  R17,=300         ! ERRORS? DO NEXT
         JNC  NEXT             ! LOOP IF NO
         LDMD R26,=ERRSTP      ! ALLOC ERRORS?
         JNZ  NEXT             ! CONTINUE IF YES
!
! THIS CAN HAPPEN IF DALLOC PRGM WITH ROM OR BIN PRGM MISSING
!
         JSB  =LODSCR          !
         JMP  XDALL            !
!
! **** DALLOC JUMP TABLE ****
!
         DEF  ROMINI           ! -1 ROM CLASS > 56
JDTAB    DEF  XDALL1           ! 0
         DEF  VDALOC           ! 1
         DEF  BININT           ! 2
         DEF  SVALD            ! 3
         DEF  SKPCON           ! 4
         DEF  SKPCON           ! 5
         DEF  DALFNC           ! 6
         DEF  LINEDA           ! 7
         DEF  LINEDA           ! 10
         DEF  RELJMP           ! 11
         DEF  DALFN            ! 12
         DEF  DEFND1           ! 13
         DEF  ROMCLA           ! 14
         DEF  FRRET            ! 15 OPTION
         DEF  RELJMP           ! 16
         DEF  FRRET            ! 17
         DEF  SKPNX1           ! 20
         DEF  COMMD            ! 21
         DEF  COMMD            ! 22
         DEF  COMMD            ! 23
         DEF  COMMD            ! 24
         DEF  LINEDA           ! 25 ELSE JMP #
         DEF  RELJMP           ! 26 ELSE JMP REL
         DEF  LINEDA           ! 27 USING LINE #
!
SKIPL    CLM  R24              !
         LDB  R24,R47          ! LINE LEN
         ADMD R24,=PCR         !
         ADM  R24,=3,0         !
         RTN                   !
!
SKPNX1   JSB  =SKIPL           !
XDALL1   POMD R36,-R6          ! RETURN ADDR
         JSB  =NXTLIN          !
         JEN  NEXT             ! JIF NOT LAST LINE
         TSB  R16              !
         JOD  XDALL            ! JIF CALC
XDALL2   LDMD R30,=FWCURR      !
         LDBD R57,X30,P.TYPE   !
         ANM  R57,=37          ! CLEAR ALLOCATION,COMM,OP
         ADB  R57,=100         ! DEFAULT OPTION BASE
         STBD R57,X30,P.TYPE   ! STORE NEW PCB 7
         LDMD R34,X30,P.LEN    ! LENGTH
         ADM  R34,R30          ! PTR TO VAR AREA
         CLM  R56              !
         STMD R56,X30,P.COM    ! ZERO COM LEN
         ICM  R56              !
         ICM  R56              !
         STMD R56,R34          ! SET VAR LEN = 2
XDALL    STBD R#,=GINTEN       ! ENABLE INTERRUPTS
         PAD                   ! RESTORE DCM FF
         RTN                   ! EXIT
!
! ********************************************************************
! SUBROUTINE LINEDA
! THIS SUBROUTINE DEALLOCATES LINE NUMBERS
! AND REPLACES THE REL ADDR WITH THE ACTUAL LINE NUMBER
! ********************************************************************
LINEDA   LDMD R36,R24          ! REL ADDR
         ADMD R36,=FWCURR      ! ACTUAL ADDRESS
         POMD R34,+R36         ! LINE #
         PUMD R34,+R24         ! PUSH IT
         RTN                   !
!
! ********************************************************************
! FN DEALLOCATE
! THIS ROUTINE DEALLOCATES USER DEFINED FUNCTIONS
! ********************************************************************
DALFN    JSB  =VDALOC          ! DO COMMON PART
         POMD R75,+R24         !
SKPRS    LRB  R77              ! PAR COUNT
         TSB  R77              !
         JZR  NONP             ! JIF NO PARAMS
PARLP    STM  R24,R36          ! ADDR TO 36
         LDM  R24,=10,0        ! ASSUME SIMPLE
         POMD R66,+R36         ! NAME
         TSB  R66              ! STRING FLAG
         JPS  ADDEM            ! JIF SIMPLE
         POMD R24,+R36         ! TOTAL STRING LEN
         ADM  R24,=4,0         ! SKIP MAX & ACT LEN
ADDEM    ADM  R24,R#           !
         DCB  R77              !
         JNZ  PARLP            ! JIF MORE PARAMS
NONP     RTN                   !
! ********************************************************************
! DEALLOCATE FN CALLS
! THIS ROUTINE DEALLOCATES USER FUNCTION CALLS
! ********************************************************************
DALFNC   JSB  =VDALOC          !
         STM  R24,R36          !
         CLM  R24              !
         POBD R24,+R36         !
         ADM  R24,R36          !
         RTN                   !
! ********************************************************************
! SUBROUTINE VDALOC
!
! THIS ROUTINE IS CALLED TO DEALLOCATE A VARIABLE.  IF RUN, THE ADDRESS
! OF THE VARIABLE IS RELATIVE TO THE VARIABLE AREA OF THE CURRENT PROGRAM.
!
! INPUT REGISTERS
!
!  R23     = TOKEN
!  R24     = PTR TO ADDR IN STACK
!  R26     = FWA VARIABLES (IF RUN)
!  R30     = LWA + 1 OF VARIABLES (IF RUN)
!  R40-R44 = PCB 7-11 (IF RUN)
!  R44-R47 = LINE # AND BYTES (IF RUN)
!
! OTHER REGISTERS USED
!  R34     = SCRATCH
!  R36     = SCRATCH
!
! ********************************************************************
SVALD    SBB  R23,=20          !
VDALOC   CMB  R23,=300         ! A() OR A(,) ?
         JNC  VDALO1           ! JIF NO
         LDB  R23,=2           ! LOOKS LIKE ARRAY
VDALO1   JSB  =ASCNAM          ! NAME TO ASCII
         PUMD R36,+R24         !
         RTN                   ! EXIT
! ********************************************************************
! SUBROUTINE ASCNAM
!
! THIS ROUTINE WILL COINVERT THE VARIABLE FROM THE FORM DESCRIBED IN
! THE SUBROUTINE FRMNAM TO THE NORMAL ASCII FORM.
! ********************************************************************
ASCNAM   LDMD R34,R24          ! REL ADDR
         ADMD R34,=FWCURR      ! ABS ADDR
         LDMD R36,R34          ! NAME FORM
ASCNM1   ANM  R36,=17,37       !
         CMB  R36,=12          !
         JNZ  NTBLA            ! JIF NOT BLANK
         LDB  R36,=360         ! -20 SO IT COMES UP BLANK
NTBLA    ADB  R#,=60           ! NUM PART OR BLANK
         ADB  R37,=100         ! ALPHA PART
         RTN                   !
!
! ********************************************************************
! LOCAL SUBROUTINES
! ********************************************************************
!
! ********************************************************************
! SUBROUTINE ALINI
! THIS ROUTINE DOES THE INITIALIZATION FOR ALLOC AND DALLOC.
! ********************************************************************
ALINI    JSB  =EXTR1           ! SELECT ROM 0
         STBD R24,=ROMFL       !
         LDMD R24,=FWCURR      !
         LDMD R26,X24,P.LEN    !
         ADM  R26,R24          !
         LDMD R22,=FWUSER      !
         STMD R22,=NXTCOM      ! RESET NXTCOM
         CLM  R22              !
         STBD R22,=DCLCOM      ! NOT COMMON DECLARER
         STBD R22,=COMFLG      !
         STMD R22,=DFPAR1      !
         STBD R22,=DIMFLG      !
         ICM  R22              ! OPT BASE IF CALC
         POMD R30,+R26         !
         TSB  R16              !
         JEV  ALINI1           ! JIF NOT CALC MODE
         ADM  R30,R26          ! LWA VAR
         DCM  R30              !
         DCM  R30              !
         LDMD R24,=STSIZE      ! STACK PTR
         LDM  R45,=231,251,2   ! SIMULATE LAST LINE
         STMD R22,=OPTBAS      ! DEFAULT OPT BASE ZERO
         RTN                   !
!
ALINI1   LDM  R30,R26          !
         LDM  R56,=1,200       !
         STMD R56,=OPTBAS      !
         ADM  R24,=P.GO        ! PGM PTR TO LINE #
         CLM  R45              ! PRESET BYTES TO ZERO
         JSB  =NXTLIN          !
         RTN                   !
! ********************************************************************
! SUBROUTINE GETINT
! ********************************************************************
GETINT   LDBD R64,R24          ! NEXT TOKEN
         CMB  R64,=32          ! INT?
         JNZ  GETIR            ! JIF NOT
         POMD R64,+R24         ! TOKEN AND INT
BCDINT   PUMD R75,+R6          ! SAVE R75
         JSB  =INTORL          ! CONV TO REAL
         POMD R75,-R6          ! NOW RESTORE R75
         BIN                   !
         JSB  =CONINT          !
GETIR    RTN                   !
! ********************************************************************
! SUBROUTINE TSTRM
! ********************************************************************
TSTRM    TSM  R56              !
         JNG  TSRMRT           ! JIF TOO MUCH
         LDMD R66,=NXTMEM      !
         TSB  R16              !
         JEV  TSTR1            ! JIF RUN
         LDM  R66,R12          !
TSTR1    ADM  R66,=10,1        ! MUST BE 256+ EXTRA
         LDMD R36,=LAVAIL      !
         SBM  R36,R56          !
         SBM  R36,R20          !
         CMM  R36,R66          !
TSRMRT   RTN                   !
! ********************************************************************
! SUBROUTINE STOR2R
! ********************************************************************
STOR2R   STMD R*,R30           !
         LDM  R36,R30          !
         ADM  R36,R20          !
         ADM  R20,R56          !
STOR2Z   RTN                   !
!
! ********************************************************************
! GLOBAL SUBROUTINES
! ********************************************************************
!
! ********************************************************************
! SUBROUTINE GETNXT
!
! THIS ROUTINE WILL FIND THE NEXT TOKEN AND RETURN IT IN R23.
! INPUTS:
!   R24    = POINTER TO NEXT TOKEN
!   R45-46 = CURRENT LINE #
!   R47    = BYTES REMAINING THIS LINE
!
! OUTPUTS:
!   R24    = POINTER TO NEXT TOKEN
!   R45-46 = CURRENT LINE #
!   R47    = NEW BYTE COUNT
!   R23    = TOKEN
!   R33-37 = TOKEN CLASS
!
! ********************************************************************
GETNXT   LDMD R36,=R60+2       ! RUNTIME TABLE ADDRESS
         CLM  R56              !
         LDBD R56,R24          !
         POBD R23,+R24         ! GET TOKEN
         SBB  R23,=371         ! BIN PGROG
         STBD R23,=BINFLG      ! SET FLAG
         JNZ  GNX1             ! JIF NO
         POBD R56,+R24         ! SKIP DUMMY ROM#
         POBD R56,+R24         ! GET TOKEN
         LDMD R36,=BINTAB      ! BIN PROG ADDR
         JZR  ERRXX            ! JIF NOT LOADED
! CAPASM: inserted unreferenced label because a DRP Statement is in the ROM
NOREF1   LDMD R36,X36,THIRT2   ! EXECUTION TAB BASE ADDR
GNX1     STB  R56,R23          ! TOKEN TO 23
         LLM  R56              ! *2
         ADM  R56,R36          !
         LDMD R56,R56          ! EXECUTION ADDR
         POBD R36,-R56         ! ATTRIBUTES(CLASS)
         ANM  R36,=77,0        ! ISOLATE CLASS IN 36
         RTN                   !
!
ERRXX    JSB  =ERROR+          !
         BYT  50D              ! BINARY PROGRAM MISSING
!
! ********************************************************************
! SUBROUTINE NXTLIN
!
! THIS ROUTINE WILL CHECK FOR LAST LINE (E.G. 10000) AND IF NOT WILL
! ADVANCE TO THE NEXT LINE.
!
! INPUTS:
!  R45-46 = CURRENT LINE #
!  R24    = POINTER TO NEXT LINE
!
! OUTPUTS:
!  E      = 0 IF LAST LINE ELSE # 0
!  R24    = POINTER TO NEXT TOKEN
!  R45-46 = NEW LINE #
!  R47    = BYTES THIS LINE
!  R22    = 0 IF DIM ELSE # 0
!
! ********************************************************************
NXTLIN   CLE                   !
         BIN                   !
         LDM  R22,R45          ! LINE #
         CMM  R22,=231,251     ! LINE A999 ?
         JZR  NXLRTN           ! JIF YES
         ICE                   !
         CLB  R22              ! NOT COM OR SUB
         STBD R22,=COMFLG      !
         STBD R22,=DIMFLG      ! DEFAULT IS REALS
         ICB  R22              ! CLEAR DIM FLAG
         STMD R24,=PCR         ! LINE # FOR ERROR PROCESSING
         POMD R45,+R24         ! NEXT LINE AND BYTES
NXLRTN   RTN                   !
! ********************************************************************
! SUBROUTINE SKPCON
!
! THIS ROUTINE WILL SKIP OVER AN ARITH CONST OR A STRING CONST.
! ********************************************************************
SKPCON   CLM  R56              !
         LDB  R56,=10          ! ASSUME NUM CONST
         CMB  R23,=4           ! IS IT?
         JZR  SKPC1            ! NICE GUESS
         POBD R56,+R24         ! SO ITS A STRING
SKPC1    ADM  R24,R56          ! ADVANCE OVER CONST
         RTN                   ! EXIT
!
BININT   LDM  R56,=3,0         !
         JMP  SKPC1            !
! ********************************************************************
! SUBROUTINE FRMNAM
!
! THIS ROUTINE PUTS THE VARIABLE NAME IN R36-R37 IN THE FORM:
!
!   XYTTNNNN
!   RDFAAAAA
!
! WHERE:
!  X     = STRING FLAG
!  Y     = ARRAY FLAG
!  TT    = TYPE (0=REAL, 1=INTEGER, 2=SHORT, 3=AVAIL)
!  AAAAA = 1ST CHAR NAME - 100 OCT
!  R     = REMOTE FLAG
!  D     = TRACE FLAG
!  F     = FUNCTION FLAG
!  NNNN  = 2ND CHR NAME - 60 OCT (OR 12 IF BLANK)
!
! INPUT:
!  R23   = TOKEN OR TOKEN + 200 IF FUNC
!  DIMFLG SET (0=REAL, 20=INTEGER, 40=SHORT)
!
! ********************************************************************
FRMNAM   POMD R36,+R24         ! NUM AND ALPHA OF NAME
FRMNA#   CLM  R56              !
         LDB  R56,R23          ! TOKEN
         DCB  R56              ! TOKEN - 1
         BCD                   !
         LLM  R56              ! POSITION ARRAY,STR,FUNC
         BIN                   !
         LLM  R56              !
         LLM  R56              !
         ADBD R56,=DIMFLG      ! ADD DIM FLAG
         SBB  R37,=100         ! ALPHA - 100
         CMB  R36,=40          ! CHECK BLANK
         JNZ  FRM1             ! JIF NO
         LDB  R36,=72          !
FRM1     SBB  R#,=60           ! NUM - 60 OCT
         ORM  R#,R56           ! OR WITH TYPE
         RTN                   ! EXIT
! ********************************************************************
! SUBROUTINE CALCSZ
!
! THIS SUBROUTINE WILL CALCULATE THE ARRAY SIZE BASED ON THE MAX ROW IN R74,
! MAX COL IN R76, AND OPTION BASE.  THE RESULT IS PLACED IN R56.
! ********************************************************************
CALCSZ   LDBD R2,=DIMFLG       ! 0=REAL,20=INT,40=SHORT
         BCD                   !
         LRB  R2               ! JUST RT
         BIN                   !
         STM  R74,R60          ! SAVE ROW/COL
         LDM  R54,R60          ! ROW
         ADMD R54,=OPTBAS      ! ADD OPT BASE
         CLM  R56              !
         STM  R54,R64          !
         LLM  R54              ! ROW * 2
         DCB  R2               !
         JNZ  CALSZ1           ! JIF NOT INTEGER
         ADM  R54,R64          ! ROW * 3
         JMP  CALSZ2           ! GO FINISH
CALSZ1   LLM  R54              ! ROW * 4
         DCB  R2               !
         JZR  CALSZ2           ! JIF SHORT
         LLM  R54              ! ROW * 8
CALSZ2   TSB  R63              !
         JNG  VECTOR           !
         LDM  R66,R62          ! GET COL
         ADMD R66,=OPTBAS      ! ADD OPT BASE
         TSM  R56              ! OVERFLOW?
         JNZ  VCTER1           ! JIF YES
         LDM  R76,R54          ! ROW * 8
         CLM  R54              !
         JSB  =INTMUL          ! ROW * COL * TYPE(3,4,8)
VECTOR   TSM  R56              ! OVERFLOW?
         JZR  VCTER2           ! JIF NO
VCTER1   LDB  R55,=377         ! SET SIGN BIT
VCTER2   LDM  R56,R54          !
         LDM  R74,R60          ! RESTORE ROW COL
         RTN                   !
! ********************************************************************
! SUBROUTINE INIVAR
! THIS ROUTINE INITIALIZES PROGRAM VARIABLES
! ********************************************************************
INIVAR   BIN                   !
         CLM  R60              !
         LDMD R34,=FWCURR      ! FWA PROGRAM
         LDMD R36,X34,P.LEN    ! PROG LEN
         ADM  R36,R34          ! FWA VRBLS
         LDMD R32,R36          ! LEN VRBLS
         ADM  R32,R36          ! LWA VRBLS
         POMD R34,+R36         ! GET OVER LEN
         JMP  INVRTN           ! CIF ANY TO DO
!
INIVLP   POMD R54,+R36         ! NAME + 2
         TSB  R55              !
         JNG  INVRTN           ! JIF REMOTE
INVNRM   LLB  R55              ! TRACE
         LLB  R55              ! FUNC
         TSB  R55              !
         JPS  INVNF            ! JIF NOT FUNC
         CLM  R70              !
         PUMD R70,+R36         ! TRASH RTN,PCR,TOS,MEM,C
         PUBD R70,+R36         !
         POMD R56,+R36         ! RESTORE R56
INVNF    TSB  R54              !
         JNG  INSTR            ! JIF STR
         LDM  R56,=10,0        ! TOTAL BYTES
         LDB  R67,=377         ! INDEF
         LDB  R0,=60           ! PUSH POINTER
         STB  R54,R77          ! TYPE TO 77
         LLB  R54              ! ARRAY FLAG UPPER
         BCD                   !
         LRB  R77              ! TYPE
         BIN                   !
         ANM  R77,=3           ! ISOLATE TYPE
         JZR  TSTAR            ! JIF REAL
         LDB  R0,=65           ! ASSUME INT
         LDB  R56,=3           !
         DCB  R77              !
         JZR  TSTAR            ! JIF INT
         DCB  R0               ! FOR SHORT
         ICB  R56              !
TSTAR    STM  R56,R76          ! COUNT / ITEM
         TSB  R54              !
         JNG  INARR            ! JIF ARRAY
         DCM  R36              !
         DCM  R36              ! MAKE IT RIGHT
INVR00   JSB  =ZERO1-          ! GO SET TO INDEF
INVRTN   CMM  R36,R32          ! SEE IF DONE
         JNZ  INIVLP           ! JIF NO
         RTN                   !
!
INARR    POMD R56,-R36         ! COUNT TO 56
         ADM  R36,=6,0         ! SKIP GARBAGE
         JMP  INVR00           !
!
INSTR    STM  R56,R64          ! MAX = TOTAL
         CLM  R66              !
         DCM  R66              ! ACT = -1
         PUMD R64,+R36         ! ACT LEN UNDEF
         LDB  R23,=3           ! MAKE IT BLANK
         JSB  =ZROMEM          ! GO DOIT
         JMP  INVRTN           !
! ********************************************************************
! SUBROUTINE ZROMEM
! THIS ROUTINE WILL ZERO OR BLANK A SPECIFIED ARA OF MEMORY
!
! INPUTS:
!  R36 = FWA
!  R56 = # BYTES
!  R23 = 3 THEN BLANKS ELSE ZEROS
!
! ********************************************************************
ZROMEM   LDB  R60,=40          ! ZERO OR BLANK A BLOCK OF MEMORY
         LDM  R61,R60          ! BLANK R60-R67
         CMB  R23,=3           ! STRING?
         JZR  ZROM1-           ! JIF YES
ZROM-    CLM  R60              ! ZERO R60
ZROM1-   JSB  =ZERO11          ! GO DO 10'S
         ADM  R56,=10,0        ! RESTORE COUNT
ZEROL2   TSM  R56              !
         JZR  ZEROX            ! EXIT IF DONE
ZEROL3   PUBD R60,+R36         ! FILL THE REST 1 AT A TIME
         DCM  R56              !
         JNZ  ZEROL3           ! TIL DONE
ZEROX    RTN                   !
ZERO10   CLM  R60              !
ZERO11   LDB  R0,=60           !
         LDM  R76,=10,0        !
ZERO1-   SBM  R56,R76          !
         JNC  ZEROX            ! JIF NOT R76 LEFT
         PUMD R*,+R36          ! zero (or blank) R76 of them
         JMP  ZERO1-           ! LOOP TO DO MORE
! ********************************************************************
! SUBROUTINE FNDLIN
! THIS ROUTINE WILL FIND THE LINE SPECIFIED BY THE LINE# IN R76.
!
! INPUTS:
!  R76 = GOAL
! OUTPUTS:
!  R36 = PTR TO CURRENT/FOUND LINE
!  E   = ZERO IF FOUND, ELSE NON-ZERO
! ********************************************************************
FNDLIN   BIN                   !
         LDMD R36,=FWCURR      !
         ADM  R36,=P.GO        !
FNDLOP   CLE                   !
         BCD                   !
         LDMD R66,R36          ! LINE #
         CMM  R66,R76          ! SEE IF = GOAL
         BIN                   !
         JZR  FNDRT            ! JIF YES
         JCY  FNDEX            ! JIF DONE
         JSB  =SKPLN           !
         JMP  FNDLOP           !
FNDEX    DCE                   ! NOT FOUND
FNDRT    RTN                   !
! ********************************************************************
! ROUTINE RTOIN
! REAL TO BCD INTEGER CONVERSION
! INPUT R60
! OUTPUT R65
! ********************************************************************
RTOIN    STM  R60,R70          ! SAVE ORIG FOR HOMER
RTOIN1   BCD                   ! ALTERNATE ENTRY
         CLE                   !
         CMB  R64,=377         ! INT?
         JCY  RTORTN           ! JIF YES, DONE
         STM  R60,R40          !
         JSB  =INFR3           ! SEP & INFRA
         CLM  R60              ! ANS IF SMALL
         TSM  R50              ! ZERO MANTISSA?
         JZR  BIG1-            ! JIF YES
         ICM  R36              ! EXP = -1
         JZR  RNDIT            ! JIF YES
         JLN  TSTBIG           ! JIF NEGATIVE EXPONENT
RNDSHF   LLM  R50              ! BRING TRAILING ZERO
         JZR  BIG2             ! JIF EXPONENT IS TOO BIG
         DCM  R36              ! DEC EXPONENT
         JNZ  RNDSHF           ! LOOP IF MORE TO BRING
         JMP  TSTBIG           !
!
BIG2     LDB  R53,=1           ! FORCE OVERFLOW
         JMP  TSTBIG           !
!
RNDIT    ADB  R47,=50C         ! ROUND
         JNC  TSTBIG           ! JIF NO OVERFLOW
         ICM  R50              ! ELSE INCR ANS
TSTBIG   CLE                   !
         ICE                   !
         LDM  R65,=99C,99C,9C  ! 99999 IN CASE OF ERROR
         TSM  R53              !
         JNZ  BIG1             ! JIF TOO BIG
         CMB  R52,=10C         !
         JCY  BIG1             ! JIF > 99999
         LDM  R65,R50          ! MOVE ANSWER TO 65
BIG1-    CLE                   !
BIG1     TSB  R32              !
         JRZ  RTORTN           ! JIF POSITIVE
         TCM  R65              ! ELSE COMPLEMENT
RTORTN   RTN                   !
! ********************************************************************
! SUBROUTINE CONINT
! CONVERTS THE F.P. CONSTANT IN R60-R67 TO AN OCTAL CONSTANT IN R76.
! OTHER REGISTERS USED: R32, R34, R36, R50
! ********************************************************************
CONINT   SAD                   ! SAVE ARP DRP
! **** FIRST, TRY A QUICKIE FOR SMALL POS #'S ****
         BCD                   !
         CLM  R76              !
         CLE                   !
         ELB  R67              ! GET MSdigit
         TSM  R60              ! SEE IF INTEGER 0 TO 9
         JNZ  CONIN1           ! JIF NO
         ELB  R76              ! ELSE SHIFT INTO RESULT AND DONE
         PAD                   !
         RTN                   !
!
CONIN1   ERB  R67              ! RESTORE ORIGINAL VALUE
         PUMD R32,+R6          !
         PUMD R40,+R6          !
         JSB  =RTOIN1          ! REAL TO INT
         CLM  R76              !
         TSB  R67              ! NEGATIVE?
         JLZ  CONIN2           ! JIF NO
         TCM  R65              ! ELSE COMPLEMENT
CONIN2   LDM  R36,=0,20        ! 10000
         LDM  R34,=4,0         ! GET LARGEST EXP
NXTVAL   BIN                   !
         LLB  R#               ! EXP * 2
         BCD                   !
         LDMD R56,X34,TABD     ! GET CONSTANT BCD VAL FROM TABLE
         STM  R56,R55          ! TURN INTO THREE BYTES WITH MSB=0
         CLB  R57              !
VALLOP   SBM  R65,R55          ! SUBTRACT IT OUT OF THE BCD INTEGER
         JNC  NXTCON           ! JIF VAL < TABD
         BIN                   !
         ADM  R76,R36          ! INC ANSWER
         BCD                   !
         JNO  VALLOP           ! REPEAT IF NO OVERFLOW
BIGNUM   LDM  R76,=377,177     ! LOAD BIGGEST POSITIVE INTEGER
SMLNUM   CLE                   !
         DCE                   !
NGTST    TSB  R32              !
         JRZ  CONOUT           !
         BIN                   !
         TCM  R76              !
CONOUT   POMD R40,-R6          !
         POMD R32,-R6          ! RESTORE R32
         PAD                   ! RESTORE ARP DRP
         RTN                   !
!
NXTCON   ADM  R65,R55          ! RESTORE
         BIN                   !
         LRM  R37              ! OCT VAL / 2
         LRM  R37              ! OCT VAL / 4
         LRM  R37              ! OCT VAL / 8
         LRB  R34              ! RESTORE EXP
         DCB  R34              ! DECREMENT EXP
         JPS  NXTVAL           ! JIF NOT END OF TABLE
         CLE                   !
         JMP  NGTST            ! GO SEE IF NEG
!
TABD     BYT  1C,0C            ! 2^0 (1 in BCD)
         BYT  8C,0C            ! 2^3 (8 in BCD)
         BYT  64C,0C           ! 2^6 (64 in BCD)
         BYT  12C,5C           ! 2^9 (512 in BCD)
         BYT  96C,40C          ! 2^12 (4096 in BCD)
!
! ********************************************************************
! SUBROUTINE CUROPT
! THIS ROUTINE WILL SET THE OPTION BASE TO THAT OF THE PROGRAM POINTED TO BY FWCURR
! ********************************************************************
CUROPT   SAD                   !
         BIN                   !
         CLM  R76              !
         ICB  R76              !
         TSB  R16              ! CALC?
         JOD  CUROPX           ! JIF CALC
         LDMD R76,=FWCURR      !
         LDBD R75,X76,P.TYPE   ! PCB 7
         CLM  R76              !
         ELB  R75              ! TRASH COMMON
         ELM  R75              !
CUROPX   STMD R76,=OPTBAS      !
         PAD                   !
         RTN                   !
! ********************************************************************
! VARIABLE FETCH STORE
! ********************************************************************
!
! ********************************************************************
! ROUTINES FETSV/FETSVA
! THESE ROUTINES WILL FETCH AN ARITHMETIC SIMPLE VARIABLE AND ITS ADDRESS.
! INPUTS:
!  R66 = REL ADDR OF VARIABLE
! OUTPUTS:
!  R34 = ABS ADDR OF VARIABLE
!  R46 = NAME FORM
!  R60 = VARIABLE VALUE
! ********************************************************************
FETSV    JSB  =FETSVA          ! GET ADDR
FETSVX   JSB  =FNUM            ! GET NUM
FETIND   CMB  R67,=377         ! INDEF?
         JNC  FEXIT            ! JIF NO
FEXER    CLM  R60              ! ZERO RESULT
!
         JSB  =ERROR+          !
         BYT  7D               ! INDEF VARIABLE
!
FETSVA   BIN                   ! FETCH SIMPLE VARIABLE ADDRESS
         CLM  R34              ! INITIALIZE R34 = FWCURR
         TSB  R16              !
         JOD  FETSV1           ! JIF CALC
         LDMD R34,=FWCURR      ! PROGRAM BASE ADDR OR 0 IF NOT RUN
FETSV1   ADM  R34,R66          ! ABS ADDR OF ENTRY
         POMD R46,+R34         ! GET NAME
         JPS  FEXIT            ! JIF NOT REMOTE
         LDMD R34,R34          ! REMOTE ADDR
         DCM  R34              ! BACK UP OVER NAME
         POBD R3,+R34          ! GET THE REMOTE NAME
         ANM  R3,=100          ! TRACE FLAG
         ORB  R47,R3           ! SET REMOTE TRACE
FEXIT    RTN                   ! AND EXIT
!
FNUM     LDB  R0,=60           ! ASSUME REAL
         BCD                   !
         LDB  R36,R46          ! TYPE
         LRB  R36              ! TYPE LOWER
         BIN                   !
         ANM  R36,=3,0         ! AND ISOLATE
         JZR  FEX1             ! JIF REAL
         LDB  R0,=65           ! TRY INT
         DCB  R36              !
         JZR  FEX2             ! JIF INT
! SHORTS TO REAL
         DCB  R0               !
         LDMD R*,R34           ! GET SHORT
         CLM  R36              ! SIGN EXP
         STM  R36,R60          ! CLEAR CRAP
         STM  R36,R62          ! MORE CRAP
         LDB  R36,R64          ! EXP
! AND STILL MORE CRAP
         STB  R37,R64          !
         BCD                   !
         CMB  R67,=377         ! UNINITIALIZED DATA
         JCY  FEXRTN           ! JIF YES
         LLM  R60              ! SIGNS TO E
         ELB  R32              ! TO 32
         TSB  R32              !
         JEV  FEX3A            ! JIF POS
         TCM  R36              ! ELSE COMPL SIGN
FEX3A    LLB  R37              ! POSITION UPPER EXP
         BIN                   !
         LRB  R32              ! SIGN MANT
         BCD                   !
         TSB  R32              !
         JEV  FEX3B            ! JIF POS
         ADB  R37,=9C          ! SET SIGN NEG
FEX3B    STM  R36,R60          ! SIGN/EXP TO 60
         BIN                   !
FEXRTN   RTN                   !
!
FEX2     LDB  R64,=377         ! INT FLAG
FEX1     LDMD R*,R34           ! LOAD INT/REAL
         RTN                   !
! ********************************************************************
! ROUTINES FETAV/FETAVA
! THESE ROUTINES WILL FETCH AN ARITHMETIC ARRAY VARIABLE AND ITS ADDRESS.
! INPUTS:
!  R12 = STACK PTR
! STACK IN:
!         PTR TO VARIABLE AREA (2 BYTES)
!         ROW DIM (2 BYTES)
!         COL DIM (2 BYTES)
!         DIM FLAG
!   R12----->
!
! OUTPUTS:
!  R34 = ARRAY VARIABLE ELEMENT ADDR
!  R60 = ARRAY VARIABLE ELEMENT VALUE
!
! ********************************************************************
FETAV    JSB  =FETAVA          ! FETCH ARRAY VARIABLE
         JMP  FETSVX           !
!
FETAVA   BIN                   ! FETCH ARRAY VARIABLE ADDRESS
         POBD R22,-R12         ! DIM FLAG
         PUBD R22,+R6          ! SAVE IT
         CLM  R26              !
S/DLOP   JSB  =ONEB            ! MAX COL OR ROW
         STM  R46,R74          !
         TSB  R22              ! 1 DIM ?
         JOD  S/DON            ! JIF YES
         ICB  R22              ! SO WE EXIT NEXT TIME
         LDM  R26,R74          ! SAVE COL
         JMP  S/DLOP           ! GO DO ROW
S/DON    STM  R26,R76          ! LOAD COL
         POMD R66,-R12         !
         JSB  =FETSVA          ! GET VARIABLE ADDRESS
! * NAME FORM IN R46 ****************
         STM  R74,R40          ! SAVE ROW COL
         POBD R44,-R6          ! DIM FLAG
         PUBD R16,+R6          ! SAVE CALC
         CMM  R34,R12          !
         JCY  CALCV            ! JIF CALC VAR
         CLB  R16              !
CALCV    JSB  =CUROPT          !
         POBD R16,-R6          ! RESTORE CALC
         LDM  R74,R40          ! RESTORE ROW COL
NTRMT    LDMD R32,=OPTBAS      !
         STM  R32,R30          ! COPY IT
         DCM  R32              !
         TCM  R32              ! ZERO IF OPT BAS 0 ELSE
         POMD R66,+R34         ! TRASH TOT SIZE
         POMD R66,+R34         ! POP MAX ROW
         LDM  R26,R74          !
         JSB  =TSTDIM          !
         POMD R66,+R34         ! POP MAX COL
         JPS  FETA1            ! JIF NOT VECTOR
         TSB  R44              ! ONE DIM ?
         JEV  DIMERR           ! JIF NO
         LDM  R66,R74          ! ROW
         SBM  R66,R32          ! MINUS OPTION BASE
         JMP  VCTOR            ! GO MPY
!
FETA1    LDM  R26,R76          !
         TSB  R44              ! TWO DIM ?
         JOD  DIMERR           ! JIF NO
         JSB  =TSTDIM          !
         LDM  R76,R74          ! ROW
         SBM  R76,R32          ! ROW - OPT BASE
         SBM  R26,R32          ! COL - OPT BASE
         ADM  R66,R30          ! MAX COL + OPTBAS
         CLM  R54              !
         JSB  =INTMUL          ! ROW * MAX COL
         LDM  R66,R54          !
         ADM  R66,R26          ! + COL
VCTOR    BCD                   !
         LDB  R57,R46          ! TYPE
         LRB  R57              ! TYPE RT
         ANM  R57,=3           ! ISOLATE TYPE
         BIN                   !
         STM  R66,R76          ! SAVE ROW OR ROW*COL
         LLM  R66              ! * 2
         DCB  R57              !
         JNZ  VCTOR1           ! JIF NOT INT
         ADM  R66,R76          ! * 3
         JMP  VCTOR2           ! GO FINISH
!
VCTOR1   LLM  R66              ! * 4
         DCB  R57              !
         JZR  VCTOR2           ! JIF SHORT
         LLM  R66              ! * 8
VCTOR2   ADM  R34,R66          ! GET ADDR
         RTN                   !
!
TSTDIM   CMM  R66,R26          ! MAX-GOAL
         JNG  DIMERR           !
         CMM  R26,R32          ! GOAL-BASE
         JNG  DIMERR           !
         RTN                   !
!
DIMERR   DCM  R6               !
         DCM  R6               !
!
         JSB  =ERROR+          !
         BYT  55D              ! SUBSCRIPT OUT OF RANGE
!
! ********************************************************************
! ROUTINE FETST
! THIS ROUTINE WILL FETCH THE ADDRESS AND LEN OF STRING VARIABLE AND
! PUSH THEM ON THE OPERATOR STACK.
! INPUTS:
!  R12 = STACK PTR
!
! STACK IN:
!          MAX STRING LENGTH (NOT NEEDED????)
!          PTR TO VARIABLE AREA (2 BYTES)
!  R12------->
!
! STACK OUT:
!          STRING LENGTH
!          STRING ADDRESS
!  R12-------->
!
! ********************************************************************
FETST    BIN                   ! FETCH STRING VARIABLE
         POMD R66,-R12         ! POP THE ADDRESS
         JSB  =FETSVA          ! GET ADDRESS
         POMD R52,+R34         ! POP TOT,MAX,ACT LEN
         JEZ  STRIND           ! JIF FETCH STRING
NULLDT   LDM  R56,R54          ! ELSE MAX TO 56
         JMP  FES3             !
!
STRIND   CMM  R56,=377,377     ! UNDEF?
         JNC  FES3             ! JIF NO
         CLM  R56              ! ZERO LEN
!
         JSB  =ERROR           !
         BYT  7D               ! UNDEF DATA
!
FES3     PUMD R56,+R12         ! AND PUSH IT BACK
         PUMD R34,+R12         !
         RTN                   !
!
! ********************************************************************
! ROUTINE STOSV
! THIS ROUTINE WILL STORE A VALUE IN THE SPECIFIED SIMPLE VARIABLE.
! INPUTS:
!  R12 = STACK IN
! STACK IN:
!                 PTR TO VARIABLE AREA (2 BYTES)
!                 VALUE TO STORE
!     R12----------->
! STACK OUT:
!                 VALUE JUST STORED
!     R12----------->
!
! ********************************************************************
! MULTI STORE NUM
! ********************************************************************
         BYT  43               ! ATTRIBUTES
STOSVM   JMP  STOSV            ! MULTI STORE
! ********************************************************************
! STORE NUM
! ********************************************************************
         BYT  31               ! ATTRIBUTES
STOSV    SAD                   ! STORE SIMPLE AND ARRAY VARIABLE
         LDB  R0,=60           ! ASSUME REAL
         POMD R60,-R12         ! GET REAL/INT
         PUMD R60,+R6          ! SAVE IT
         POMD R46,-R12         !
         PUMD R46,+R12         ! SAVE IT
         BCD                   !
         LRB  R46              !
         ANM  R46,=3,0         ! ISOLATE TYPE
         BIN                   !
         JZR  STSV1R           ! JIF REAL
         DCB  R46              !
         JNZ  STSV3            ! JIF NOT INT
         JSB  =RTOIN           ! REAL TO INT
         JEZ  STOSVJ           ! JIF OK
!
         JSB  =ERROR           !
         BYT  2D               ! OVERFLOW
!
STOSVJ   LDB  R0,=65           ! BECAUSE REPORT DESTROYS
STSV1R   JMP  STSV1            !
!
! REAL TO SHORT
!
STSV3    CLB  R32              ! SIGNS FLAG
         LDB  R0,=64           !
         CMB  R64,=377         ! INT?
         BCD                   !
         JNZ  STSV3Z           ! JIF NO
         CLB  R36              ! EXP IF MANT 0
         TSM  R65              !
         JLZ  STSV3X           ! JIF NOT NEG
         ICB  R32              !
         ICB  R32              ! MANT SIGN NEG
         TCM  R65              ! COMPL
STSV3X   JZR  STSV3Y           ! JIF MANT = 0
         LDB  R36,=5           ! EXP=5(MAX)
STSV3L   DCB  R36              ! DEC EXP
         LLM  R65              !
         JLZ  STSV3L           ! JIF NOT NORM
STSV3Y   JMP  STSV3D           ! GO FINISH
!
STSV3Z   LDM  R36,R60          ! EXP/SIGN
         LRB  R37              ! SIGN TO E
         JEZ  STSV3A           ! JIF MANT POS
         BIN                   !
         ICB  R32              ! SET MANT NEG
         ICB  R32              !
STSV3A   BCD                   !
         CMB  R37,=5           !
         JNC  STSV3B           ! JIF EXP POS
         TCM  R36              !
         BIN                   !
         ICB  R32              ! SET SIGN NEG
         BCD                   !
         ANM  R37,=17          ! TRASH EXTRA 9
STSV3B   ADM  R65,=5,0,0       ! ROUND
         JNC  STSV3C           ! JIF NO CARRY
         LDB  R67,=10C         ! ELSE ANS IS 1EN+1
         ICM  R36              ! INCR EXP
STSV3C   CMM  R36,=0,1         !
         JNC  STSV3D           ! JIF EXP < 100
         CLM  R36              ! ZERO EXP
         CLM  R65              ! AND MANTISSA
         TSB  R32              ! NEG EXP
         JEV  OVFLOD           ! JIF OVERFLO
!
         JSB  =ERROR           !
         BYT  1D               ! UNDER FLOW
!
         JMP  STS3C-           ! CONT IF DEFAULT
!
OVFLOD   JSB  =ERROR           !
         BYT  2D               ! OVER FLOW
!
         LDB  R36,=99C         !
         LDM  R65,=99C,99C,99C !
STS3C-   LDB  R0,=64           ! RELOAD R0 - ERROR KILLED
STSV3D   ERM  R32              !
         ERM  R67              ! SIGNS TO UPPER 60
         STB  R36,R64          ! EXP TO 64
STSV1    BIN                   !
         POMD R46,-R12         ! NAME FORM
         STM  R46,R30          ! SAVE IT
         LLB  R47              !
         TSB  R47              ! TRACE?
         JPS  TRAC-            !
         LLB  R46              ! ARRAY?
         TSB  R46              !
         JPS  TRAC-            ! JIF NO
         POBD R20,-R12         ! DIM FLAG
         POMD R74,-R12         ! GET ROW/COL
TRAC-    POMD R34,-R12         ! VARIABLE ADDR
         STMD R*,R34           !
         POMD R50,-R6          ! GET 50 BACK
         LDBD R26,R10          ! NEXT TOKEN
         CMB  R26,=24          ! MULTI STORE?
         JNZ  SVXIT            ! JIF NO
PBAC     PUMD R50,+R12         ! FOR NEXT TIME
SVXIT    TSB  R47              ! TRACE?
         JPS  SVRTN            ! JIF NO
         LDM  R46,R30          ! RESTORE NAME
         JSB  =FNUM            ! GET VAL AS STORED
         STM  R46,R36          ! NAME
         LLB  R46              ! POSITION ARRAY FLAG
         JSB  =TRCVBL          !
SVRTN    PAD                   !
         RTN                   !
! ********************************************************************
! ROUTINE STOST
! THIS ROUTINE WILL STORE THE STRING VALUE IN THE SPECIFIED STRING VAR.
! INPUTS:
!   R12 = STACK PTR
! STACK IN:
!                 PTR TO VARIABLE AREA (2 BYTES)
!                 SUBSTR LEN OR MAX LEN
!                 STR PTR OR STR PTR + OFFSET
!                 STR LEN
!                 STRING PTR (2 BYTES)
!    R12--------------->
!
! STACK OUT:
!                 STR LEN
!                 STR PTR (2 BYTES)
!    R12--------------->
!
! ********************************************************************
! MULTI-STORE STRING
! ********************************************************************
         BYT  43               !
STOSTM   JMP  STOST            ! MULTI STORE$
! ********************************************************************
! STORE STRING
! ********************************************************************
         BYT  31               !
STOST    SAD                   ! SAVE ARP/DRP
         BIN                   !
         POMD R26,-R12         ! SOURCE STR OINTER
         POMD R24,-R12         ! SOURCE STR LEN
         POMD R36,-R12         ! SINK STR POINTER
         POMD R32,-R12         ! SINK STR LEN
         POMD R66,-R12         ! BASE STR VARIABLE PTR
         LDBD R76,R10          ! NEXT TOKEN
         CMB  R76,=25          ! MULTI?
         JNZ  NOPUSH           ! JIF NO
         PUMD R24,+R12         ! PUSH LEN
         PUMD R26,+R12         ! PUSH POINTER
NOPUSH   JSB  =FETSVA          !
         STM  R46,R74          ! ANEM
         POMD R64,+R34         ! TOT,MAX LEN
         POMD R22,+R34         ! ACTUAL LEN
         CMM  R32,R24          ! SINK LEN - SOURCE LEN
         JPS  STOS2            ! JIF SINK GQ
         CMM  R36,R34          ! SINK = BASE ?
         JNZ  STOS1            ! GO TRUNCATE IF NO
         CMM  R66,R32          ! SINK LEN = MAX ?
         JZR  STOERX           ! JIF YES
STOS1    STM  R32,R24          ! ELSE TRUNCATE
STOS2    LDM  R56,R36          ! SINK ADDR
         SBM  R56,R34          ! SINK - BASE
         ADM  R56,R32          ! SIN = BASE + SINK LEN
         CMM  R66,R56          ! MAX -(SINK-BASE+SINK LEN)
         JPS  STOS3            ! JIF MAX GQ
!
STOERX   JSB  =ERROR           !
         BYT  56D              ! STRING OVERFLOW
!
         PAD                   !
         RTN                   !
!
STOS3    CMM  R34,R36          ! SINK PTR = BASE
         JNZ  NOPU0            ! JIF NO
         CMM  R66,R32          ! SINK LEN = MAX
         JNZ  NOPU0            ! JIF NO
         TSM  R24              ! SOURCE LEN = 0?
         JNZ  NOPU1            ! JIF NO
         PUMD R24,-R34         ! ELSE ACT LEN = 0
         JMP  STRTN1           ! SKIP MOVE
!
NOPU1    STM  R24,R32          ! SINK LEN = SOURCE
         STM  R24,R56          ! NEW ACTUAL
         JMP  NOPU2            !
!
NOPU0    CMM  R22,R56          ! ACTUAL - NEW
         JPS  ZRTEST           ! JIF ACTUAL GREATER
NOPU2    PUMD R56,-R34         ! ELSE NEW ACTUAL
ZRTEST   TSM  R24              ! SOURCE LEN = 0?
         JZR  TBFILL           ! YES - SO DONT MOVE ANY
S/TLOP   POBD R67,+R26         !
         PUBD R67,+R36         !
         DCM  R32              !
         DCM  R24              !
         JNZ  S/TLOP           !
TBFILL   TSM  R32              ! ANY BLANK FILL?
         JZR  STRTN1           ! JIF NO BLANK FILL
         LDB  R67,=40          !
S/TLP1   PUBD R67,+R36         !
         DCM  R32              !
         JNZ  S/TLP1           !
STRTN1   LLB  R75              ! TRCE
         TSB  R75              !
         JPS  STREXX           ! JIF NO
         STM  R46,R36          ! NAME
         JSB  =TRCFP           !
         LDB  R77,=44          ! $
         PUBD R77,+R12         ! PUSH DOLLAR
         JSB  =UNSTAK          !
         JSB  =TRCLP           !
STREXX   PAD                   !
         RTN                   !
!
! ********************************************************************
! DCOM
! ENTRY:
! R24    POINTS TO LINE
!   R30    POINTS TO DECOM BUFFER
!   R45-47 LINE# & LEN
! EXIT:
! DECOMPILED LINE IN BUFFER
! R24    POINTS TO NEXT LINE
!   R30    POINTS TO END DECOM BUFF
! ********************************************************************
DECOM    SAD                   !
         LDB  R36,=12          ! DECOM ROMFL
         STBD R36,=ROMFL       !
         CLB  R36              !
         STBD R36,=PRECNT      ! ZERO PRECEDENT GROUP CNT
         STBD R36,=ONFLG       ! ZERO "ON" FLAG
         STBD R36,=COMFLG      ! ZERO COM FLAG
         LDM  R36,R45          !
         JSB  =DCLIN#          !
         STMD R12,=TOS         ! SAVE STACK PTR
DECOM1   JSB  =DECOM2          !
         JMP  DECOM1           !
DECOM2   BIN                   !
         JSB  =GETNXT          ! NEXT TOKEN
         JSB  =ROMCL-          ! CIF ROM CLASS
         LLM  R36              !
         LDMD R36,X36,DCTAB    !
         JSB  X36,ZRO          !
         RTN                   !
!
         DEF  ROMINI           ! -1 ROM CLASS > 56
DCTAB    DEF  EOL              !  0 END OF LINE
         DEF  FETVAR           !  1 FETCH VARIABLE
         DEF  BINCON           !  2 BIN INTEGER
         DEF  STOVAR           !  3 STORE VARIABLE
         DEF  CONST            !  4 NUM FLOAT OR STR CONST
         DEF  SCNST            !  5 STRING CONST
         DEF  UFNCAL           !  6 USER FUNCTION CALL
         DEF  JMPL#            !  7 COND JMP LINE #
         DEF  GOLINE           ! 10 GOTO GOSUB
         DEF  JMPREL           ! 11 JMP REL
         DEF  UFNDEF           ! 12 USER FN DEF
         DEF  FNEND            ! 13 FNEND
         DEF  EXTROM           ! 14 EXT ROM
         DEF  RESWD            ! 15 OPTION BASE
         DEF  FNRTN            ! 16 USER FN RETURN
         DEF  FNASGN           ! 17 FN ASSIGN
         DEF  RESWD            ! 20 DATA
         DEF  RESWD+           ! 21 DIM/REAL
         DEF  RESWD+           ! 22 SHORT
         DEF  RESWD+           ! 23 INTEGER
         DEF  RESWD-           ! 24 COM
         DEF  EJMP#            ! 25 ELSE JMP#
         DEF  EJMPR            ! 26 ELSE JMP REL
         DEF  ULIN#            ! 27 USING LINE #
         DEF  ON               ! 30 ON
         DEF  PU=              ! 31 STORE
         DEF  SUBSCR           ! 32 SUBSCR
         DEF  INPUTR           ! 33 INPUT
         DEF  DIMSUB           ! 34 DIM SUBS
         DEF  PRNEOP           ! 35 PRINT EOL
         DEF  PRINTS           ! 36 PRINT STUFF
         DEF  MSCRTN           ! 37 DUMMY
         DEF  MSCRTN           ! 40 IMMED EXECUTE
         DEF  RESWD            ! 41 OTHER RESERVED WORD
         DEF  MISC             ! 42 MISC OUTPUT
         DEF  MSTOR            ! 43 MULTI STORE
         DEF  MSCRTN           ! 44 MISC IGNORE
         DEF  PRTFUN           ! 45 PRINT FUNCTIONS
         DEF  MSCRTN           ! 46 DUMMY
         DEF  MSCRTN           ! 47 DUMMY
         DEF  UNOP             ! 50 NUM UNARY OP
         DEF  BINOP            ! 51 NUM BINARY OP
         DEF  UNOP             ! 52 STR UNARY OP
         DEF  BINOP            ! 53 STR BINARY OP
         DEF  RWEX             ! 54 DUMMY
         DEF  SYSFUN           ! 55 NUM FUNC
         DEF  SYSFUN           ! 56 STR FUNC
!
! ********************************************************************
! END OF LINE PROCESSING 3-1-77
!
EOL      POMD R74,-R6          ! TRASH RETURN
         JSB  =UNSTAK          !
         LDMD R12,=TOS         ! RESET R12
         POBD R77,-R30         ! POP LAST CHAR
         CMB  R77,=40          ! BLANK?
         JZR  EOLEX            ! JIF BLANK
         PUBD R77,+R30         !
EOLEX    PAD                   !
         RTN                   !
! ********************************************************************
CONST    POMD R60,+R24         ! GET VALUE
CONST1   LDB  R22,=16          ! MARKER
         PUMD R22,+R12         ! PUSH MARKER AND TOKEN
         PUMD R60,+R12         ! PUSH VALUE
         RTN                   !
!
SCNST    LDB  R22,=16          !
         PUMD R22,+R12         !
         STM  R24,R34          !
         CMB  R24,=16          !
         JZR  FSADR            !
         CMB  R24,=17          !
         JNZ  SCNST1           !
FSADR    TCM  R34              !
SCNST1   PUMD R34,+R12         ! STRING POINTER
         STM  R24,R36          !
         CLM  R24              !
         POBD R24,+R36         ! STR LEN
         ADM  R24,R36          !
         RTN                   !
!
BINCON   POMD R65,+R24         ! GET BCD CONST
         JSB  =INTORL          ! GO CONVERT
         LDB  R23,=4           ! REAL TOKEN
         JMP  CONST1           ! NOW IT LOOKS LIKE REAL
!
! ********************************************************************
! DESIGN NOTE
!
! 16 AND 17 ARE USED AS STACK MARKERS AND THEREFORE MAY NOT APPEAR IN
! STRING ADDRESSES THAT GO ON THE STACK.  THE PROBLEM IS SOLVED BY
! CHECKING THE LSB OF THE ADDRESS FOR 16 OR 17.  IF FOUND, THE ADDRESS
! IS COMPLEMENTED.
!
! THIS MEANS THAT ADDRESSES OF STRING CONSTANTS MUST BE WITHIN THE FOLLOWING
! BOUNDARIES:  100000 < STRING ADDR < 177377
! ********************************************************************
!
! FETVAR 03-01-77
STOVAR   SBB  R23,=20          !
FETVAR   JSB  =GETNM           ! VAR NAME TO 36
         LDB  R22,=16          !
         PUMD R22,+R12         ! PUSH MARKER AND TOKEN
         PUMD R36,+R12         !
         CMB  R23,=300         ! A() OR A(,) ?
         JNC  FVRTN            ! JIF NO
         LDB  R36,=50          !
         PUBD R36,+R12         !
         LDM  R36,=54,51       ! ,)
         TSB  R23              !
         JOD  P1               ! JIF 1 DIM
         PUMD R36,+R12         ! ELSE PUSH ,)
         JMP  FVRTN            !
!
P1       PUBD R37,+R#          !
FVRTN    RTN                   !
!
! ********************************************************************
! BASIC RES WORDS & FN END 03-09-77
!
MVWRD    CLM  R20              !
         LDB  R20,R23          !
         DCM  R20              ! BIAS FOR ROM
         LDMD R26,=R60+4       ! ASCII TAB ADDR
         LDBD R77,=BINFLG      ! BIN PROG
         JNZ  MVNBIN           ! JIF NOT
         LDMD R26,=BINTAB      !
! CAPASM: unreferenced label inserted because a DRP statement is in the ROM
NOREF2   LDMD R26,X26,THIRT4   ! ASCII TABLE
         JMP  MVW1             !
!
MVNBIN   LDBD R77,=R60K        !
         JNZ  MVW1             ! JIF NOT ROM 0
         SBM  R20,=44,0        ! BIAS FOR SYSTEM
MVW1     PUMD R24,+R6          ! SAVE R24
         JSB  =BATS            !
         POMD R24,-R6          ! RESTORE R24
         RTN                   !
!
FNASGN   JSB  =MVWRD           !
         POBD R23,+R24         ! 1 OR 3 TOKEN
         JMP  FETVAR           !
!
FNEND    JSB  =MVWRD           !
FNRTN    ICM  R24              !
         ICM  R24              !
         RTN                   !
!
RESWD-   STBD R23,=COMFLG      ! SET COM FLAG
         JMP  RESWD            !
!
RESWD+   LDBD R20,=COMFLG      !
         JZR  RESWD            ! JIF NOT COMMON
         CMMD R12,=TOS         ! ANYTHING ON STAK?
         JZR  RESWD            ! JIF NO
         PUBD R23,+R6          ! SAVE TOKEN
         JSB  =UNSTAK          !
         LDB  R23,=54          ! COMMA
         PUBD R23,+R30         !
         POBD R23,-R6          ! RESTORE TOKEN
RESWD    CMB  R23,=233         ! BANG? (REMARK?)
         JNZ  RESWD1           ! JIF NO
         JSB  =UNSTAK          ! ELSE UNSTAK
         LDB  R23,=233         ! RELOAD BANG
RESWD1   JSB  =MVWRD           !
         LDB  R32,=40          !
         PUBD R32,+R30         !
RWRTN+   CLB  R36              !
RWRTN    STBD R#,=ONFLG        !
         JSB  =UNSTAK          !
RWEX     RTN                   !
!
ON       JSB  =MVWRD           !
         LDB  R32,=40          !
         PUBD R32,+R30         !
         LDB  R36,R23          !
         JMP  RWRTN            !
!
MISC     CMB  R23,=100         ! @?
         JNZ  MISCPU           ! JIF NO
         PUBD R23,+R12         ! PUSH TO STAK
         JMP  RWRTN+           ! GO UNSTAK
!
MISCPU   PUBD R23,+R30         !
MSCRTN   RTN                   !
!
! ********************************************************************
! GOTO & GOSUB 03-01-77
!
GOLINE   LDBD R37,=ONFLG       !
         JZR  GOL1             ! JIF NOT ON
         JNG  DOCOMA           ! JIF NOT FIRST
         TCB  R37              !
         STBD R37,=ONFLG       !
GOL1     JSB  =MVWRD           !
         LDB  R32,=40          ! BLANK
         PUBD R32,+R30         !
         JMP  DOLINE           !
!
DOCOMA   DCM  R30              !
         LDB  R37,=54          !
         PUBD R37,+R30         !
DOLINE   JSB  =GET2            ! GET LINE #
         JSB  =DCLIN#          !
         LDBD R36,R24          ! NEXT TOKEN
         CMB  R36,=16          !
         JNZ  GRTN             !
         DCM  R30              ! TRASH BLANK
GRTN     RTN                   !
!
GET2     POMD R36,+R24         ! NAME OR ADDR
         JSB  =TSTALO          !
         BIN                   !
         JEZ  GET2R            ! JIF NOT ALLOCATED
         ADMD R36,=FWCURR      !
         STM  R36,R66          !
         LDMD R36,R66          ! LOAD NAME
GET2R    RTN                   !
!
GETNM    JSB  =GET2            !
         JEZ  GETNR            ! JIF NOT ALLO
         JSB  =ASCNM1          ! GO CONVERT
GETNR    RTN                   !
!
! ********************************************************************
! RELATIVE JUMPS 03-01-77
!
!   JMPREL
!
THEN     ASC  "THEN "          !
ELSE     ASC  "ELSE "          !
IFB      ASC  "IF "            !
!
JMPREL   LDMD R75,=IFB         !
         PUMD R75,+R30         !
         JSB  =UNSTAK          !
         LDMD R73,=THEN        !
         PUMD R73,+R30         !
JMPEXX   JSB  =GET2            ! GET LINE #
JMPRTN   RTN                   !
!
JMPL#    JSB  =JMPREL          !
JMPEX    JSB  =DCLIN#          !
         RTN                   !
!
EJMPR    LDMD R75,R24          ! NEXT TOK TO 77
         CMB  R77,=37          ! ELSE JMP # ????
         JZR  JMPEXX           ! YES, THEN NO ELSE
         JSB  =UNSTAK          !
         LDMD R73,=ELSE        !
         PUMD R73,+R30         !
         JMP  JMPEXX           !
!
EJMP#    JSB  =EJMPR           !
         JMP  JMPEX            !
!
ULIN#    CMB  R23,=334         ! RESTORE LINE # ?
         JZR  ULIN#-           !
         LDB  R23,=313         !
         JSB  =RESWD1          ! DECOMPILE USING
ULIN#-   JSB  =GET2            ! GET LINE #
         JMP  JMPEX            ! OUTPUT IT
!
! ********************************************************************
! OPERATORS 03-01-77
!
! LST OPERATORS
!
! OPER
!
!   INPUT
! 	R23   TOKEN
! 	R56   POINTER TO LWA ATTRIBUTES
!
UNOP     POBD R55,-R56         ! OPER PREC
         JSB  =STAKB+          !
         JSB  =PRETS1          !
         JMP  PRETS3           !
!
BINOP    POBD R55,-R56         ! OPER PREC
         JSB  =STAKB           !
PRETST   ICB  R55              ! PREC + 1 FOR >= TEST
         JSB  =PRETS1          !
         JMP  PRETS2           !
!
PRETS1   LDBD R75,=PRECNT      ! CURRENT OPER COUNT
         LDMD R76,=LAVAIL      ! CURRENT OPER STAK
         STM  R36,R56          ! SAVE LOC
         LDM  R34,R12          !
         DCM  R36              !
         JSB  =OPTST           !
         RTN                   !
!
PRETS2   DCB  R55              ! RESTORE PREC
         LDM  R34,R2           ! RESTORE ORIG R36
         JSB  =POSIT           !
         JSB  =OPTST           !
PRETS3   PUMD R55,-R76         ! STORE PREC/LOC
         STMD R76,=LAVAIL      !
         ICB  R75              ! INC PREC COUNT
         STBD R75,=PRECNT      !
         RTN                   !
!
OPTST    PUMD R75,+R6          ! SAVE PRECNT STAK PTR
OPTLOP   TSB  R75              !
         JZR  OPTRTN           ! EXIT IF CNT 0
         DCB  R75              ! DEC COUNT
         POMD R65,+R76         ! NEXT PREC /LOC
         CMM  R66,R36          !
         JNC  OPTLOP           ! JIF STAK < LOW
         CMM  R66,R34          !
         JCY  OPTLOP           ! JIF STAK > HI
         CMB  R65,R55          ! STAK PREC < CURR PREC
         JCY  OPTLOP           ! JIF NO
         JSB  =EXPER           !
         JSB  =CLEAN           !
OPTRTN   POMD R75,-R6          !
         RTN                   !
!
EXPER    CLM  R32              !
         ICM  R32              !
         JSB  =EXPAND          !
         ICM  R36              !
         LDB  R70,=50          ! OPEN (
         PUBD R70,+R36         !
         PUMD R36,+R6          ! SAVE R36 FOR CLEAN
         LDM  R36,R34          !
         CLM  R32              !
         ICM  R32              !
         JSB  =EXPAND          !
         ICM  R36              !
         LDB  R70,=51          ! CLOSE )
         PUBD R70,+R36         !
         POMD R36,-R6          ! RESTORE R36
         RTN                   !
!
CLEAN    LDMD R76,=LAVAIL      !
         LDBD R75,=PRECNT      !
         JZR  CLNRTN           ! NOTHING ON STAK
CLNLOP   LDMD R65,R76          !
         CMM  R66,R36          ! STAK - LOW
         JNC  CLNEX            ! JIF STAK LO
         CMM  R66,R34          !
         JCY  CLNEX            ! JIF STAK HI
         LDB  R65,=100         ! HIGHEST PREC + SOME
CLNEX    PUMD R65,+R76         !
         DCB  R75              !
         JNZ  CLNLOP           ! JIF NOT DONE
CLNRTN   RTN                   !
!
STAKB+   JSB  =POSIT           ! NEXT MARKER
         CLM  R32              !
         ICM  R32              !
         JSB  =EXPAND          !
         ICM  R36              !
         JMP  STAKB1           !
!
STAKB    JSB  =POSIT           !
STAKB1   PUMD R36,+R6          ! SAVE R36
         PUMD R30,+R6          ! SAVE R30
         JSB  =MVWRD           !
         STM  R30,R32          ! NEW R30
         POMD R30,-R6          ! RESTORE ORIG R30
         POMD R36,-R6          ! RESTORE R36
         SBM  R32,R30          ! LEN OPER
         DCM  R32              !
         JZR  NOEXPR           ! JIF OPER 1 BYTE
         PUMD R32,+R6          ! SAVE LEN
         JSB  =EXPAND          ! MAKE ROOM
         POMD R32,-R6          ! LEN AGAIN
NOEXPR   STM  R36,R2           ! SAVE R36
         LDM  R34,R30          !
DOIT1    POBD R77,+R34         ! NEXT BYTE OF OPER
         PUBD R77,+R36         ! TO STAK
         DCM  R32              !
         JPS  DOIT1            ! LOOP IF MORE
         RTN                   !
!
! ********************************************************************
! SOME USEFUL UTILITIES 03-01-77
!
EXPAND   PUBD R23,+R6          ! SAVE TOKEN
         PUMD R24,+R6          ! SAVE R24
         LDM  R22,R12          !
         SBM  R22,R36          ! # BYTES TO MOVE
         LDM  R24,R12          ! LWA + 1 SOURCE
         LDM  R26,R12          !
         ADM  R26,R32          ! LWA + 1 SINK
         ADM  R12,R32          ! UPDATE R12
         JSB  =MOVDN           !
         POMD R24,-R6          ! RESTORE R24
         POBD R23,-R6          ! RESTORE TOKEN
         RTN                   !
!
POSIT    LDM  R36,R12          !
PLOOP    POBD R0,-R36          ! NEXT TOKEN
         BIN                   !
         CMB  R0,=16           ! IS IT OPER MARKER
         JNZ  PLOOP            !
PRTN     RTN                   !
!
! ********************************************************************
! LINE NUMBERS 03-01-77
!
DCLIN#   LDB  R57,=4           ! EXP
         BCD                   !
SLOP     TSB  R37              !
         JLN  SDON             ! JIF NORMALIZED
         LLM  R36              !
         JZR  SDON             ! JIF LINE # = 0
         DCB  R57              ! DEC EXP
         JMP  SLOP             !
SDON     ELM  R36              !
LINLP1   ELM  R36              !
         ANM  R36,=17,377      !
! TEST FOR 12 OCTAL AND MAKE IT 9 BCD
         CMB  R36,=12          ! END STOP MISSING LINE?
         JNZ  LINLP2           ! JIF NO
         DCB  R36              ! ELSE MAKE IT 11
LINLP2   ADB  R36,=60          ! MAKE ASCII
         PUBD R36,+R30         ! PUSH IT OUT
         DCB  R57              !
         JNZ  LINLP1           ! JIF MORE
         LDB  R57,=40          ! BLANK
         PUBD R57,+R30         !
         BIN                   !
         RTN                   !
!
! ********************************************************************
! PROCESS OPER STAK 03-01-77
!
UNSTAK   CLB  R77              !
         STBD R77,=RSELEC      ! ROM 0
         JSB  =CLNOPS          !
         CMMD R12,=TOS         !
         JZR  UNSRT1           ! JIF STACK EMPTY
         LDB  R36,=17          !
         PUBD R36,+R12         !
         LDMD R12,=TOS         !
         POBD R23,+R12         ! SCRAP FIRST MARKER
         CMB  R23,=16          !
         JNZ  UNSL1            !
UNSLOP   POBD R23,+R12         ! NEXT TOKEN
UNSL1    CMB  R23,=17          !
         JZR  UNSRTN           !
         CMB  R23,=363         ! A()
         JZR  SPVAR            ! JIF YES
         CMB  R23,=364         ! A(,)
         JZR  SPVAR            ! JIF YES
         CMB  R23,=4           !
         JPS  NTVAR            ! JIF NOT VARIABLE
SPVAR    JSB  =DCVAR           !
         JMP  UNSLOP           !
!
NTVAR    JNZ  NTNCON           ! JIF NOT NUM CONST
         JSB  =DCNCON          !
         JMP  UNSLOP           !
!
NTNCON   CMB  R23,=7           !
         JPS  NTSCON           ! JIF NOT STR CONST
         JSB  =DCSCON          !
         JMP  UNSLOP           !
!
NTSCON   CMB  R23,=41          ! SEE IF BANG
         JNZ  NTBANG           ! JIF NO
         PUBD R23,+R30         !
         JMP  DCSCON           !
!
NTBANG   CMB  R23,=16          ! SEE IF MARKER
         JNZ  PUSHIT           ! JIF NOT SEP
         LDB  R23,=54          !
PUSHIT   PUBD R23,+R30         !
         JMP  UNSLOP           ! LOOP IF MORE
!
UNSRTN   LDMD R12,=TOS         ! RESET R12
         LDB  R34,=40          !
         PUBD R34,+R30         ! PUSH A BLANK
UNSRT1   RTN                   !
!
! DCVAR
!
DCVAR    POMD R36,+R12         !
         PUBD R37,+R30         ! FIRST CHAR
         CMB  R36,=40          !
         JZR  SKBLN            ! JIF BLANK
         PUBD R36,+R30         ! SECOND CHAR
SKBLN    CMB  R23,=3           ! STRING?
         JNZ  STORTN           !
         LDB  R36,=44          ! $
         PUBD R36,+R#          !
STORTN   RTN                   !
!
! DCNCON
!
DCNCON   POMD R40,+R12         ! NUM CONST
         JSB  =CVNUM           !
         BIN                   !
         RTN                   !
!
! DCSCON
!
DCSCON   POMD R36,+R12         ! STR ADDR
         JNG  DCSCN1           !
         TCM  R36              !
DCSCN1   CMB  R23,=5           ! QUOTED?
         JNZ  SMLOP+           ! JIF NOT
         LDB  R34,=42          !
         PUBD R34,+R30         !
         JSB  =SMLOP+          !
         LDB  R34,=42          ! QUOTE
         PUBD R34,+R30         !
         RTN                   !
!
SMLOP+   POBD R22,+R36         ! STR LEN
         JZR  DCSRTN           ! JIF ZERO
SMLOOP   POBD R34,+R36         !
         PUBD R34,+R30         !
         DCB  R22              !
         JNZ  SMLOOP           ! LOOP IF NOT DONE
DCSRTN   RTN                   !
!
CLNOPS   BIN                   !
         CLM  R34              !
         LDBD R34,=PRECNT      !
         LDMD R36,=LAVAIL      !
         ADM  R36,R34          !
         ADM  R36,R34          !
         ADM  R36,R34          !
         STMD R36,=LAVAIL      !
         STBD R35,=PRECNT      ! ZERO COUNT
         RTN                   !
!
! ********************************************************************
! MISC TOKENS 03-21-77
!
SUBSCR   LDM  R76,=50,51       ! "(",")"
         TSB  R23              !
         JOD  CAL1             !
CAL2     JSB  =TWODIM          !
         JMP  TSTSTO           !
!
DIMSUB   LDM  R76,=133,135     ! "[","]"
         TSB  R23              !
         JEV  CAL2             ! JIF TWO DIM
CAL1     JSB  =ONEDIM          !
TSTSTO   LDM  R34,R12          !
         JSB  =CLEAN           !
         RTN                   !
!
TWODIM   JSB  =POSIT           !
         LDB  R32,=54          !
         PUBD R32,+R36         !
ONEDIM   JSB  =POSIT           !
         PUBD R76,+R36         !
         PUBD R77,+R12         !
         RTN                   !
!
MSTOR    LDB  R77,=54          ! COMMA
         CMBD R23,R24          !
         JZR  MSTOR-           ! JIF NEXT MULTI ALSO
PU=      LDB  R77,=75          ! "="
         JSB  =MSTOR-          !
         JSB  =UNSTAK          !
         RTN                   !
!
MSTOR-   LDMD R36,=TOS         !
MST1     POBD R76,+R36         !
         CMB  R76,=16          ! MARKER ?
         JZR  MST1             ! JIF MARKER
MST2     POBD R#,+R#           !
         CMB  R#,=16           ! MARKER?
         JNZ  MST2             ! JIF NOT MARKER
         PUBD R77,-R36         !
         RTN                   !
!
PRNEOP   LDB  R34,=40          ! BLANK
         JMP  ITSCOM           !
!
PRINTS   PUBD R23,+R6          !
         JSB  =UNSTAK          !
         BIN                   !
         LDB  R34,=54          !
         POBD R23,-R6          !
         JEV  ITSCOM           !
         LDB  R34,=73          ! ASCII ;
ITSCOM   DCM  R30              ! TRASH WHATEVER
         PUBD R34,+R30         !
         RTN                   !
!
INPUTR   POBD R36,+R24         ! SKIP STORE TOKEN
         RTN                   !
!
! ********************************************************************
! SYSTEM FUNCTIONS 03-01-77
!
! SYSFUN
! INPUT
! R23  TOKEN
! R56  POINTER TO LWA ATTRIBUTES
!
SYSFUN   LDB  R32,=54          ! LOAD UP COMMA
         POBD R77,-R56         ! PARAM COUNT
         BCD                   !
         LRB  R77              ! ISOLATE PARAM COUNT
         BIN                   !
         DCB  R77              ! NO COMMAS IF ZERO OR ON
         JPS  SYFN1            ! JIF ONE OR MORE
         LDB  R32,=16          !
         PUBD R32,+R12         ! PUSH MARKER
         STM  R12,R36          !
         ICM  R12              !
         JSB  =STAKB1          ! GO MOVE FUNC NAME
         RTN                   ! AND EXIT
!
SYFN1    DCB  R77              !
         JNG  SYFN2            ! JIF DONE
         JSB  =POSIT           ! FIND MARKER
         PUBD R32,+R36         ! PUSH COMMA
         JMP  SYFN1            !
!
SYFN2    JSB  =POSIT           !
         LDM  R34,R12          !
         JSB  =CLEAN           !
         JSB  =STAKB+          ! GO MOVE FUN NAME
         LDM  R34,R12          !
         DCM  R36              !
         JSB  =EXPER           ! GO DO PARENS
         RTN                   !
!
PRTFUN   JSB  =SYSFUN          ! DO COMMON PART
         POMD R36,+R24         ! NEXT TWO BYTES
         CMM  R36,=6,0         ! NULL STR ?
         JZR  PRTFEX           ! JIF YES
         PUMD R36,-R24         ! ELSE RESTORE IT
PRTFEX   RTN                   !
!
! ********************************************************************
! USER FUNCTION CALLS 03-01-77
!
UFNCAL   JSB  =GETNM           ! NAME
         PUMD R36,+R6          ! SAVE IT
         POBD R77,+R24         ! PARAM COUNT
         JZR  FN0              ! JIF NO PARAMS
PLOP     POBD R36,+R24         !
         DCB  R77              !
         JZR  PLOP1            !
         JSB  =POSIT           !
         LDB  R34,=54          !
         PUBD R34,+R36         !
         JMP  PLOP             ! LOOP IF MORE
!
PLOP1    JSB  =POSIT           !
         LDB  R77,=50          !
         LDB  R0,=76           !
         POMD R34,-R6          ! RESTORE NAME
         JSB  =FNNAM           !
         JSB  =EXPAND          !
         ICM  R36              !
         PUMD R*,+R36          !
         LDB  R77,=51          !
         LDM  R34,R12          !
         PUBD R77,+R12         !
         JSB  =CLEAN           !
         RTN                   !
!
FN0      LDB  R36,=16          ! MARKER
         PUBD R36,+R12         !
         LDB  R0,=77           !
         POMD R34,-R6          !
         JSB  =FNNAM           !
         PUMD R*,+R12          !
         RTN                   !
!
! FNNAME
!
FNNAM    CLM  R32              !
         ICB  R32              !
         TSB  R23              !
         JEV  NSTRNG           !
         LDB  R*,=44           !
         DCB  R0               !
         ICB  R32              !
NSTRNG   CMB  R34,=40          ! 2ND BYTE NAME = BLANK?
         JZR  ONEBT            ! JIF YES
         LDB  R*,R34           ! 2ND CHAR NAME
         DCB  R0               !
         ICB  R32              !
ONEBT    LDB  R*,R35           ! 1ST BYTE NAME
         DCB  R0               !
         ICB  R32              !
         LDB  R*,=116          ! ASCII 'N'
         DCB  R0               !
         LDB  R*,=106          ! ASCII 'F'
         ICB  R32              !
         ICB  R32              !
         RTN                   !
!
BEQB     ASC  " = "            !
DEF      ASC  "DEF FN"         !
!
! ********************************************************************
! USER FUNCTION DEF 03-01-77
! ********************************************************************
UFNDEF   LDMD R72,=DEF         !
         PUMD R72,+R30         !
         JSB  =GETNM           ! NAME
         ICM  R24              ! SKIP JMP ADDR
         ICM  R24              !
         POBD R23,+R24         ! PARAM COUNT/STR FLAG
         JSB  =FNNAMM          !
         BIN                   !
         LDB  R34,R23          !
         LRB  R34              ! PARAM COUNT
         JZR  NOPARS           ! JIF NO PARAMS
         LDB  R35,=50          ! OPEN (
         PUBD R35,+R30         ! OPEN TO OUTPUT
         LDB  R74,=16          !
PARLOP   LDB  R75,=1           ! SIMPLE VAR TOKEN
         LDM  R56,=10,0        !
         POMD R36,+R24         ! NAME
         TSB  R36              !
         JPS  NSTR             ! JIF NOT STRING
         LDB  R75,=3           ! STR TOKEN
         POMD R56,+R24         ! TOT LEN
         POMD R64,+R24         ! TRASH MAX ACT LEN
NSTR     JSB  =ASCNM1          !
         STM  R36,R76          !
         PUMD R74,+R12         !
         ADM  R24,R56          ! INC OVER PARAM
         CMB  R75,=3           ! STRING?
         JNZ  NSTR1            ! JIF NO
         LDM  R75,=135,133,4   ! ][4
         CMM  R56,=22,0        ! DEFAULT LEN?
         JZR  NSTR1            ! JIF YES
         STM  R56,R36          ! BIN VAL TO 36
         PUMD R34,+R6          ! SAVE R34
         JSB  =CONBIN          ! GO CONV
         PUMD R76,+R12         ! [4
         PUMD R40,+R12         ! VALUE
         PUBD R75,+R12         ! ]
         POMD R34,-R6          ! RESTORE R34
NSTR1    DCB  R34              ! DECREMENT COUNT
         JNZ  PARLOP           ! LOOP IF MORE
         LDB  R35,=51          ! CLOSE )
         PUBD R35,+R12         !
         JSB  =UNSTAK          !
         DCM  R30              !
NOPARS   LDMD R75,=BEQB        !
         LDBD R36,R24          !
         CMB  R36,=16          !
         JZR  NOEQU            ! NO = IF EOL
         CMB  R36,=41          !
         JNZ  PUEQU            ! = IF NOT BANG
NOEQU    DRP  R77              !
         JMP  PUEQ1            !
!
PUEQU    DRP  R75              !
PUEQ1    PUMD R#,+R30          !
         RTN                   !
!
FNNAMM   PUBD R37,+R30         ! 1ST BYTE OF NAME
         CMB  R36,=40          ! BLANK?
         JZR  ONEBYT           ! JIF YES
         PUBD R36,+R30         ! 2ND BYTE OF NAME
ONEBYT   TSB  R23              !
         JEV  NOSTR            ! JIF NOT STRING FUN
         LDB  R37,=44          !
         PUBD R37,+R#          !
NOSTR    RTN                   ! EXIT
!
! ********************************************************************
! EXTERNAL ROMS
!
EXTROM   LDM  R36,=DECOM2      ! EXTERNAL ROM DECOMPILE
EXTRJM   BIN                   !
         POBD R76,+R24         ! ROM #
         STBD R76,=RSELEC      ! ROM SELECT
         CMBD R76,=R60K        ! IS ROM THERE?
         JNZ  ERROM            ! JIF NO, GIVE "rom missing" ERROR
         JSB  X36,ZRO          ! CALL THE DECOMPILE ROUTINE
EXTR1    CLB  R77              !
         STBD R77,=RSELEC      ! SELECT ROM 0
         RTN                   !
!
ERROM    JSB  =ERROR           !
         BYT  21D              ! ROM MISSING
!
         JMP  EXTR1            !
!
! ********************************************************************
! BASIC TOKEN DECOMPILE 2-2-77
!
! BATS - BASIC TOKEN DECOMPILE
! ROUTINE TO SEARCH THE PARSING TABLE AND BASTAB TO CONVERT TOKENS > 100 OCTAL
! TO BASIC VERBS.  THE ROUTINE IS ENTERED WITH THE FOLLOWING REGISTERS SET:
!
! R20 - BIASED TOKEN
! R26 - BASE ADDRESS OF BASIC TAB
! R30 - OUTPUT BUFFER POINTER
!
BATS     BIN                   ! BASIC TOKEN DECOMPILE
         STM  R20,R36          ! SAVE BIASED TOKEN
POSLP    DCM  R36              !
         JNG  MVLOP            ! JIF WE'RE THERE, ELSE SKIP THIS ONE
POSLP1   POBD R32,+R26         ! BASIC TAB BYTE
         JPS  POSLP1           ! LOOP IF NO PARITY
         ANM  R32,=177,0       ! TRASH PARITY
         JMP  POSLP            ! JIF YES
!
MVLOP    POBD R32,+R26         ! POP ASCII
         STB  R32,R24          ! SAVE IT
         ANM  R32,=177,0       ! TRASH PARITY
         PUBD R32,+R30         ! AND PUSH IT TO BUFFER
         TSB  R24              !
         JPS  MVLOP            ! JIF MORE
         RTN                   !
!
! ********************************************************************
! ********************************************************************
! MATH ROUTINES - WRITTEN BY HOMER RUSSELL
! ********************************************************************
! ********************************************************************
!
! ********************************************************************
! MAIN LN(X) SUBROUTINE
! ********************************************************************
!
LN20     JSB  =ONER            ! GET REAL X
         JSB  =SEP10           ! SEPARATE X
LN22     TSM  R40              ! M(X)=0?
         JNZ  LN24             ! JIF M(X)#0
!
         JSB  =ERROR+          ! ELSE REPORT LN(0) OR LOG(0)
         BYT  12D              !
!
LN24     TSB  R32              ! X>0?
         JRZ  LN30             ! JMP & FIND LN(X) IF X>0
!
         JSB  =ERROR+          ! ELSE REPORT LOG OF NEG NO.
         BYT  13D              !
!
LN36     STM  R40,R50          ! COPY X
         SBB  R47,=20          ! X-1
         JSB  =SHF10           ! ACCUM - J; NORM X-1 RIOR TO /
         STM  R36,R34          ! MOVE EXP(X-1) TO R34
         CLM  R36              ! EXP(X)=0
         TSM  R40              ! X=1?
         JZR  LN34             ! JIF YES; DONE, LOG(1)=0 IN R40
         JSB  =UT210           ! SWAP X AND X-1
LN38     JSB  =DIV20           ! (X-1)/X OR X/(X+1)
         ICM  R36              ! MOVE DEC ALL WAY TO LEFT
LN40     STM  R36,R34          ! MOVE EXP
         CLM  R70              ! CLEAR PQ AREA
         TCM  R34              ! J
         CMM  R34,=8C,0C       ! J>=8?
         JLZ  LN80             ! JIF YES; NO PQ NEEDED
         CLE                   ! READY FOR PSEUDO-DIVIDE
         JMP  LN50             ! JMP TO PSEUDO-DIVIDE LOOP
!
LN30     TSM  R36              ! 1<=X<10?
         JZR  LN36             ! JIF YES
         TCM  R40              ! 10-10XM
LN32     ICM  R36              ! MOVE DEC ALL WAY TO LEFT
         STM  R36,R26          ! SAVE EX
         CLM  R36              ! EXP(1-XM)
         JSB  =SHF10           ! SHIFT OUT LEADING 0'S
         JSB  =LN40            ! -B0=1-XM; GO FIND LN
         PUMD R40,+R12         ! SAVE M(LN(XM))
         CLM  R40              ! READY FOR EX
         CLB  R33              ! S(LN10)
         LDM  R46,R26          ! MOVE EX
         JPS  LN33             ! JIF POS
         TCM  R46              ! ABS(EX)
         NCB  R32              ! GIVES -EX
LN33     STM  R36,R14          ! SAVE EXP(LN(XM))
         LDM  R36,=3C,0C       ! MAX EXP(EX)
         JSB  =SHF10           ! ELIM LEAD 0'S IN EX
         CLM  R34              ! EXP(LN10)
         LDMD R50,=TBL2        ! M(LN10)
         JSB  =MPY30           ! (EX)(LN10)
         LDM  R34,R14          ! GET EXP(LN(XM))
         POMD R50,-R12         ! GET M(LN(XM))
         NCB  R33              ! LN(XM)<0
         JSB  =ADD20           ! LNX=LN(XM)+(EX)(LN10)
LN34     RTN                   ! END
!
LN62     DCE                   ! -BI(10 TO J)-BI-1
         ICB  R70              ! INCREMENT PQ DIGIT
LN50     STM  R40,R60          ! COPY BI(10 TO J)
         TSM  R36              ! J=0?
         JZR  LN58             ! JIF YES; DECADE 0, NO SHIFTS
         ERM  R67              ! 1ST RT SHIFT TO ALIGN BI FOR +
LN52     STB  R67,R0           ! SAVE CONTENTS OF E
         LDB  R31,R36          ! SHIFT COUNTER
         JMP  LN56             ! CONTINUE
!
LN54     LRM  R67              ! SHIFT BI
LN56     ICB  R31              ! INCREMENT COUNTER
         JNZ  LN54             ! LOOP TILL CTR=0; BI ALIGNED
         LLB  R0               ! RESTORE E
LN58     ADM  R40,R60          ! (-BI)(10 TO J)+(-BI)
         JNC  LN60             ! JIF NO CARRY
         ICE                   ! ELSE UP DIGIT IN E
LN60     JEN  LN62             ! JIF E#0; MORE TO CURRENT DECAD
         SBM  R40,R60          ! RESTORE TO VAL BEFORE OVERDRAFT
         STM  R40,R60          ! COPY (-BI)(10 TO J)
         LLM  R70              ! SHIFT PQ
         CMB  R36,=93C         ! ALL 8 PQ DIGITS DONE?
         JZR  LN80             ! EXIT PSEUDO-DIV LOOP IF=0
         DCM  R36              ! ELSE DECREMENT PQ DIGIT CTR
         LLM  R40              ! MIN 1 RT SHIFT; THIS IS 1ST
         JMP  LN52             ! CONTINUE LOOP
!
LN80     DCM  R36              ! DEC PT TO NORMAL SPOT
         JSB  =NEWR            ! GO CALCULATE R/(1-.5R)
         CLB  R32              ! S(LNXM)=0
         LDM  R34,=TBL1        ! POINT TO 1ST LN CONSTANT
         LLM  R40              ! TEMP SHIFT R
         DCM  R36              ! ADJUST EXP
         JMP  LN96             ! JMP TO PSEUDO-MULTIPLY LOOP
!
LN92     DCB  R#               ! DECREMENT PSEUDO-QUOTIENT DIG
         ADM  R40,R#           ! ACCUMULATE PARTIAL SUM PS
         JNC  LN94             ! JIF NO CARRY
         ICE                   ! ELSE ADJUST DIGIT IN E
LN94     TSB  R70              ! DONE WITH CURRENT PQ DIGIT?
         JRN  LN92             ! LOOP TILL PQ DIGIT = 0
LN96     TSM  R70              ! PQ=0?
         JZR  LN98             ! EXIT LOOP WHEN PQ=0
         ERM  R47              ! ELSE SHIFT PS
         LRM  R74              ! SHIFT PQ
         POMD R60,+R34         ! GET NEXT LN CONSTANT
         ICM  R36              ! ADJUST EXP(LN(XM))
         CLE                   ! LEAD DIGIT = 0 INITIALLY
         ARP  R60              ! SET ARP FOR TIGHT LOOP
         JMP  LN94             ! JMP TO TIGHT LOOP
!
NEWR     TSM  R40              ! R=0?
         JZR  NEWR2            ! JIF R=0; R/(1-.5R)=0
         PUMD R40,+R12         ! ELSE TEMP SAVE M(R)
         STM  R36,R34          ! TEMP SAVE EXP(R)
         LRM  R47              ! PROTECT FOR CARRY
         STM  R40,R50          ! READY TO FORM 5R
         ADM  R40,R40          ! 2R
         ADM  R40,R40          ! 4R
         ADM  R40,R50          ! 5R
         JSB  =BRTS35          ! SHIFT 5R RIGHT
         POMD R50,-R12         ! GET M(R)
         TCM  R40              ! M(1-.5R)
         JNZ  LN84             ! JIF 5R NOT=0 AFTER SHIFTING
         LDM  R40,R50          ! ELSE ANSWER=R
         LDM  R36,R34          ! RESTORE EXP(R)
NEWR2    RTN                   ! RTN WITH ANSWER=R
!
LN84     DCM  R36              ! EXP(1-.5R)=-1
         JMP  DIV17            ! NEW R=R/(1-.5R) AND EXIT
!
LN98     JEZ  LN99             ! JIF MSD=0 IN E
         ERM  R47              ! ELSE SHIFT IT INTO R40
         ICM  R36              ! ADJUST EXP
LN99     JMP  SHF10            ! SHIFT OUT LEAD 0'S & EXIT
!
! ********************************************************************
! LN E
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
LN5      JSB  =LN20            ! GET LN(X)
         JMP  DIV11            ! DO RONF
!
! ********************************************************************
! ********************************************************************
! DIVIDE AND SHIFT ROUTINES
! ********************************************************************
! ********************************************************************
!
DIV17    TCM  R36              ! EXP(ANS)=EXP(A)+(-EXP(B)),UTI
         CLE                   ! LEFT DIGIT OF A=0
         CMM  R50,R40          ! IS A>=B?
         JCY  DIV77            ! JIF A>=B
         LLM  R50              ! ELSE SHIFT LEFT DIG OF A TO E
         DCM  R34              ! ADJUST EXP DUE TO SHIFT
DIV77    LDB  R30,=15C         ! COUNTER (16 DIGIT MANTISSAS)
         CLB  R31              ! READY FOR LEFT DIGIT OF A
         ELB  R31              ! LEFT DIGIT OF A TO R31, 0 TO E
         JSB  =UT110           ! CALC SGN, EXP, INIT R40 AND R60
         JMP  DIV79            ! GO DO DIVIDE
!
DIV30    LLM  R50              ! SHIFT R; LEFT DIGIT TO E
         ELB  R31              ! LEFT DIG OF R TO R31, 0 TO E
DIV79    DRP  R50              ! DRP READY FOR TIGHT LOOP
         JMP  DIV50            ! JMP TO TIGHT LOOP
!
DIV39    DCB  R31              ! BORROW 1 FROM LEFT DIGIT OF R
         DRP  R50              ! DRP READY FOR TIGHT LOOP
DIV40    ICE                   ! INCREMENT FOR EACH SUBTRACT
DIV50    SBM  R#,R#            ! CAST OUT MULTIPLES OF DENOM
         JCY  DIV40            ! CONTINUE TILL DONE
         TSB  R31              ! IS LEFT DIGIT OF R=0?
         JNZ  DIV39            ! LOOP TILL = 0
         ADM  R50,R#           ! ELSE OVERDRAFT; RESTORE R
         ELM  R40              ! SAVE NEW DIGIT OF ANSWER
         DCB  R30              ! DECREMENT DECADE COUNTER
         JPS  DIV30            ! CONTINUE IF R33>=0
DIV99    RTN                   ! END
!
! ********************************************************************
! DIVIDE
! ********************************************************************
         BYT  11,51            ! ATTRIBUTES
DIV2     JSB  =TWOR            ! GET A AND B (REAL) FOR A/B
DIV10    JSB  =SEP15           ! SEPARATE A AND B
DIV14    JSB  =DIV88           ! GET UNPACKED QUO IN 32,36,40
DIV11    GTO RONF              ! ROUND, NFR, AND EXIT
!
DIV88    TSM  R40              ! TEST FOR 0 DENOMINATOR
         JNZ  DIV20            ! GO DO DIVIDE IF NO
!
         JSB  =ERROR           ! GO FLAG DIVIDE BY 0 OCCURRED
         BYT  8D               !
!
DIV89    LRB  R33              ! SGN TO E
         GTO FTR88             ! DIRECT RETURN WITH OVF VALUE
!
DIV20    JSB  =DIV17           ! GO DO A/B
SHF10    TSM  R40              ! TEST MANTISSA
         JNZ  SHF30            ! IF M#0 GO SHIFT OFF LEAD 0'S
         GTO LCOM1             ! SET SGN=EXP=0 AND EXIT ROUTINE
!
SHF20    DCM  R36              ! ADJUST EXPONENT
         LLM  R40              ! SHIFT OUT LEAD ZERO
SHF30    JLZ  SHF20            ! KEEP LOOPING TILL NO LEAD 0'S
         RTN                   ! END ROUTINE
!
! ********************************************************************
! LOG BASE 10
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
LOGT5    JSB  =LN20            ! FIND LN(X)
         JSB  =LOGCOM          ! GO GET READY FOR DIVIDE
         LDMD R40,=TBL2        ! GET MANT(LN(10))
         JMP  DIV14            ! LOG(X), ROUND, NFR & EXIT
!
! ********************************************************************
! REM (REMAINDER)
! ********************************************************************
         BYT  40,55            ! ATTRIBUTES
REM10    CLB  R2               ! FLAG FOR IP(X) (INTEGER PART)
         JMP  MOD20            ! GO CALC RMD(A,B)=A-B(IP(A/B))
!
! ********************************************************************
! MOD (MODULO)
! ********************************************************************
         BYT  11,51            ! ATTRIBUTES
MOD10    CLB  R2               ! CLEAR FLAG AREA
         ICB  R2               ! FLAG=0 FOR INT(X) (FLOOR(X))
MOD20    JSB  =TWOR            ! REAL B TO R40, REAL A TO R50
         JSB  =UT210           ! B TO R50, A TO R40
         TSM  R50              ! B=0?
         JNZ  MOD35            ! JIF B#0
MOD30    PUMD R40,+R12         ! PUSH ANS=A ONTO STACK
         RTN                   ! EXIT WITH ANS ON STACK
!
MOD40    GTO NFR               ! PACK ANS=A AND PUT ON STACK
!
MOD50    LRM  R47              ! GENERATE CARRY AREA
         LRM  R57              ! ALIGN M(B)
MOD60    SBM  R40,R50          ! CAST OUT MULTIPLES OF B
         JCY  MOD60            ! LOOP TILL OVERDRAFT
         ADM  R40,R50          ! RECOVER FROM OVERDRAFT
         LLM  R40              ! FOR NEXT LOWER DECADE
         DCM  R30              ! DECREMENT COUNTER
         JPS  MOD60            ! LOOP TILL ALL DECADES DONE
         LDM  R36,R34          ! EXP(ANS)=EXP(B)
         TSB  R2               ! DOING REMAINDER FUNCTION?
         JZR  MOD70            ! JIF YES, ALREADY HAVE RMD ANS
         CMB  R33,R32          ! SGN(A)=SGN(B)?
         JRZ  MOD70            ! JIF YES, ALREADY HAVE MOD ANS
         STB  R33,R32          ! SGN(ANS)=SGN(B)
         TSM  R40              ! A-K*B=0 EXACTLY?
         JZR  MOD70            ! ANS=0 IF R40=0
         LLM  R50              ! ELSE SHIFT B TO ALIGN WITH R40
         SBM  R50,R40          ! GET ANSWER
         STM  R50,R40          ! MOVE M(ANS)
MOD70    GTO SHRONF            ! SHIFT OFF LEAD 0'S OF ANS, DONE
!
MOD35    TSM  R40              ! A=0?
         JZR  MOD30            ! JIF A=0 (THEN ANS=A=0)
         JSB  =SEP15           ! SEPARATE A AND B
         LDM  R30,R36          ! DUPLICATE EXP(A)
         SBM  R30,R34          ! EXP(A)-EXP(B)
         JPS  MOD50            ! JIF EXP(A)>=EXP(B)
         TSB  R2               ! DOING REMAINDER FUNCTION?
         JZR  MOD40            ! JIF YES (THEN RMD(A,B)=A)
         CMB  R32,R33          ! SGN(A)=SGN(B)?
         JRZ  MOD40            ! JIF YES (THEN A MOD B = A)
         JMP  ADD15            ! ELSE A MOD B = A+B
!
! ********************************************************************
! CHANGE SIGN
! ********************************************************************
         BYT  10,50            ! ATTRIBUTES
CHSROI   POMD R40,-R12         ! GET VALUE
         CMB  R44,=377         ! IS IT REAL?
         JCY  CHS10X           ! JIF NO
CHS10    TSM  R40              ! IS X=0?
         JZR  CHS11            ! DO NOTHING IF NUMBER IS ZERO
         LLB  R41              ! SAVE XS IN E
         NCB  R41              ! CHANGE SIGN (0 TO 9 OR 9 TO 0)
         ERB  R41              ! RESTORE XS
CHS11    PUMD R40,+R12         ! PUSH ANSWER ON STACK & EXIT
         RTN                   !
!
CHS10X   TCM  R45              ! TEN'S COMP
         JMP  CHS11            ! PUSH IT OUT & EXIT
!
! ********************************************************************
! SUBTRACT
! ********************************************************************
         BYT  7,51             ! ATTRIBUTES
SUBROI   JSB  =TWOSEP          ! GET 2 REALS OR INTS
SBROI+   JSB  =SUBIL           ! TO SUB INNER LOOP
         JMP  ADSUEX           ! EXIT TO PUSH RESULT
!
SUB10    JSB  =SEP15           ! SEPARATE THE MOTHER
SUB11    NCB  R32              ! CHANGE SIGN OF B
         JMP  ADD15            ! NOW ADD
!
! ********************************************************************
! ADD
! ********************************************************************
         BYT  7,51             ! ATTRIBUTES
ADDROI   JSB  =TWOSEP          ! GET 2 REALS OR INTS
ADROI+   JSB  =ADSU            ! TO INNER LOOP
ADSUEX   GTO MPYEX             ! EXIT TO PUSH RESULT
!
SUBIL    NCB  R32              ! CHS OF B IN CASE REAL
         JEZ  ADD20            ! JIF BOTH REALS
         TCM  R45              ! ELSE COMPLEMENT B
ADSU     JEZ  ADD20            ! JIF BOTH REALS
ADRI10   ADM  R45,R55          ! A+B
         JLZ  ADD8             ! JIF SUM OK
         CMB  R47,=90C         ! GOOD SUM IF LEFT DIG=9
         JLZ  ADD8             ! JIF SUM OKAY NEG INTEGER
         CLB  R32              ! SIGN POS
         CMB  R47,=50C         ! TEST SIGN
         JNC  POSGN            ! JIF SIGN IS POS
         TCM  R45              ! MAKE MANTISSA POS
         NCB  R32              ! MAKE ITS SIGN NEG
POSGN    CLM  R53              ! NEED TO CLEAR R40 TAIL
         STM  R53,R40          ! CLEAR R40 TAIL
         LDM  R36,=5C,0C       ! EXP ANS=5
ADD8     RTN                   ! END
!
ADD9     JSB  =TWOR            ! DEMAND TWO REALS
! ADD10 IS ONLY USED BY INTERNAL "ODDBALL" CALLS
ADD10    JSB  =SEP15           ! SEPARATE OUT FOR ODDBALL CALLS
ADD15    JSB  =ADD20           ! DO THE ADD
         JMP  EXP11            ! DO THE RONF THING
!
ADD20    TSM  R50              ! IS A = 0?
         JZR  OPND=0           ! JIF YES
! IF THE NUMBER IN R50 IS ZERO, DO NOTHING!
         TSM  R40              ! IS B = 0?
         JNZ  A&B#0            ! JIF NO
! IF R40 IS ZERO, R50 IS YOUR ANSWER!
         LDM  R40,R50          ! MANTISSA TO OUTPUT
         LDM  R36,R34          ! MOVE EXPONENT
         LDB  R32,R33          ! MOVE SIGN
OPND=0   RTN                   ! DONE IF ONE OPND IS ZERO
!
A&B#0    SBM  R34,R36          ! T=EXP(A)-EXP(B)
         JZR  EXP=             ! JIF EQUAL EXPONENTS
         JPS  SWAP+-           ! JIF IN WRONG ORDER
         TCM  R34              ! CHANGE COUNTER TO >0
         JMP  ADDNOW           ! EVERYTHING COOL NOW
!
! EXPONENTS SAME, SEE IF LARGER MANT IS IN R40
!
EXP=     CMM  R40,R50          ! SEE WHICH MANTISSA IS BIGGER
         JCY  ADDNOW           ! JIF ALREADY CORRECT
SWAP+-   LDM  R60,R40          ! SWAP MANTISSAE
         STM  R50,R40          ! THIS COSTS 3 BYTES EXTRA
         LDM  R50,R60          !  (JSB =UT210 DOES IT ALSO)
         STB  R32,R60          ! SWAP SIGNS THRU R60
         LDB  R32,R33          ! R33 TO R32
         STB  R60,R33          ! R60 TO R33
         ADM  R36,R34          ! LARGER EXP, EXP(A), TO R36
ADDNOW   XRB  R33,R32          ! =0 IF SGN(A)=SGN(B), ELSE=9
         LLB  R33              ! +/- INDICATOR & LEAD 0/9 INCR
         JZR  ADD40            ! JMP IF SIGNS THE SAME
         TCM  R50              ! OPP SGNS; NEGATE MANT IN R50
ADD40    CMM  R34,=16C,0C      ! EXP DIFF>=16?
         ARP  R33              ! SET ARP FOR MANT ALIGN LOOP
         JNC  ADD50            ! JMP IF <16 SHIFTS OF SMALL M
ADD95    GTO SHF10             ! GO ELIM LEAD ZEROS AND END
!
ADD52    LRM  R57              ! SHIFT RT SMALL MANT TO ALIGN
         ADB  R57,R#           ! GIVES LEAD 9'S OR LEAD 0'S
ADD50    DCB  R34              ! BEGIN LOOP TO SHIFT SMALL M
         JCY  ADD52            ! CONTINUE LOOP TILL SHIFTS DONE
         ADM  R40,R50          ! M(LG)+-M(SM).OMPL OF OTHER
! FOR SUBTRACT, CARRY IS ALWAYS 1
         JNC  ADD95            ! IF CARRY
         TSB  R33              ! IS THIS A SUBTRACT
         JNZ  ADD95            ! JIF YES, DONE
         CLE                   ! CREATE A 1 IN 3
         ICE                   ! AND
         ERM  R47              ! PUT AS 1ST DIGIT OF ANS
         ICM  R36              ! FIX EXP
         RTN                   ! DONE
!
! ********************************************************************
! EXP(X)
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
EXP5     JSB  =ONER            ! GET REAL X
         JSB  =EXP18           ! GO CALCULATE EXP(X)
EXP11    JMP  SQR11            ! ROUND, NFR, AND EXIT
!
! ********************************************************************
! SQUARE ROOT SUBROUTINE
! ********************************************************************
SQR65    ADM  R40,R70          ! INCREMENT ANSWER DIGIT
SQR45    SBM  R50,R40          ! GENERATE NEW REMAINDER
         JCY  SQR65            ! CONTINUE UNTIL OVERDRAFT
         ADM  R50,R40          ! RECOVER FROM OVERDRAFT
         LLM  R50              ! FOR NEXT DECADE
         SBM  R40,R60          ! ANNIHILATE OLD 5 CONSTANT
         LRM  R77              ! NEW CONST 0...1...0 INCREMENT
         LRM  R67              ! NEW CONST 0...5...0 INCREMENT
         DCB  R30              ! DECREMENT DECADE COUNTER
         JCY  SQR40            ! QUIT AFTER 15 DIGITS GENERATED
         LLM  R40              ! KILL LEADING ZERO
SQR99    JMP  ADD95            ! SHIFT OUT LEAD 0'S & EXIT
!
! ********************************************************************
! SQUARE ROOT
! ********************************************************************
         BYT  20,55            !
SQR5     JSB  =ONER            ! GET REAL X
         TSB  R41              ! NEGATIVE INPUT?
         JRZ  SQR15            ! IF NOT, JUMP AND CONTINUE
!
         JSB  =ERROR+          ! ERROR: SQRT OF NEG NO.
         BYT  10D              !
!
SQR15    JSB  =SEP10           ! UNPACK X
         JSB  =SQR30           ! GO DO SQUARE ROOT
SQR11    GTO RONF              ! ROUND, NFR, AND EXIT
!
SQR30    LRM  R47              ! 5M NEEDS CARRY AREA
         STM  R40,R50          ! M
         ADM  R50,R50          ! 2M
         ADM  R50,R50          ! 4M
         ADM  R50,R40          ! 5M IN R50
         LDM  R34,R36          ! EXP
         JOD  SQR35            ! JIF EXP IS ODD
         LRM  R57              ! 5M DECIMAL ALIGNMENT
SQR35    TSM  R50              ! IS 5M=0?
         JNZ  SQR36            ! JIF NOT 0
         CLM  R40              ! ELSE ANS=0
         RTN                   ! END
!
SQR36    ADM  R36,R36          ! 2 EXP
         ADM  R36,R36          ! 4 EXP
         ADM  R36,R34          ! 5 EXP IN R34
         LRM  R37              ! EXP(ANS)=INT(5EXP/10)
         CMB  R35,=50C         ! LEAD DIGIT FOR EXP=0 IF EXP>0
         JNC  SQR37            ! JMP IF EXP>=0
         ADB  R37,=90C         ! GENERATE LEAD DIGIT=9
SQR37    LDB  R30,=14C         ! SET UP DECADE COUNTER
         CLM  R70              ! READY FOR INCREMENTING CONST 1
         ICB  R77              ! GENERATE THE CONSTANT 1
         CLM  R60              ! CLEAR CONSTANT AREA
         LDB  R66,=50C         ! LOAD CONSTANT 5
         CLM  R40              ! INITIALIZE ANSWER ACCUMULATOR
SQR40    ADM  R40,R60          ! ADD CONSTANT
         JMP  SQR45            ! GO GENERATE RT. DIGIT OF BYTE
!
! ********************************************************************
! MULTIPLY SUBROUTINES
! ********************************************************************
MPY10    JSB  =MPY28           ! GO MULTIPLY INNER LOOP
MPY11    JMP  SQR11            ! DO RONF
!
MPY28    JSB  =SEP15           ! GO UNPACK A AND B
MPY30    JSB  =UT110F          ! CALC SGN, EXP
         LDB  R0,=57           ! INITIALIZE POINTER
         LDM  R60,R40          !
         ORM  R60,R50          ! TRAILING ZERO INDICATOR
         JZR  MPY36            ! 0*0=0
         BIN                   ! MODE FOR POINTER INCREMENT
MPY31    ICB  R0               ! INCREMENT POINTER
         TSB  R*               ! FOUND#0?
         JZR  MPY31            ! JIF NO
         STM  R50,R60          ! ORIGINAL MULTIPLIER
         SBB  R0,=20           ! POINTER=4X
         TSB  R*               ! CHECK FOR NON-ZERO
         JZR  MPY32            ! JIF R40=MPYR( > TRAIL 0'S)
         STM  R40,R60          ! ELSE R50 IS THE MULTIPLIER
         LDM  R40,R50          ! SET UP TO ELIM TRAIL 0'S
MPY32    CLM  R50              ! CLEAR UPPER DIGS OF MPYR
         STM  R*,R50           ! ELIM MPYR TRAIL 0'S
         CLM  R40              ! INITIALIZE ACCUMULATE AREA
         ARP  R60              ! SET ARP FOR TIGHT LOOP
         BCD                   ! RESET MODE FOR REST OF MPY
         TSM  R50              ! TRAP OUT ZERO
         JZR  MPY36            ! JIF ANS=0
MPY77    LRM  R57              ! SHIFT OUT TRAILING 0'S OF MPY
         JEZ  MPY77            ! LOOP TILL NO TRIALING 0'S
         CLB  R0               ! WHERE LEFTMOST DIGIT ACCUMULATES
         DRP  R40              ! READY FOR TIGHT LOOP
MPY50    ADM  R#,R#            ! ACCUMULATE ANSWER
         JNC  MPY52            ! JIF NO CARRY TO LEFTMOST DIGIT
         ICB  R0               ! TALLY ONE IN LEFTMOST DIGIT
         DRP  R40              ! RESET DRP
MPY52    DCE                   ! DECREMENT COUNTER
MPY60    JEN  MPY50            ! KEEP ACCUMULATING TILL E=0
         LRB  R0               ! LEFT DIGIT TO E, 0 TO R0
         TSM  R50              ! SEE IF=0 YET
         JNZ  MPY70            ! CONTINUE IF#0
         JEZ  MPY36            ! DONE IF LEFT DIGIT=0
         ERM  R47              ! GET LEFT DIGIT FROM E
         ICM  R36              ! ADJUST EXP DUE TO ABOVE SHIFT
MPY36    GTO SHF10             ! SHIFT OUT LEAD 0'S AND EXIT
!
MPY70    ERM  R47              ! SHIFT, READY FOR NEXT DECADE
         LRM  R57              ! NEXT MULTIPLIER DIGIT TO E
         DRP  R40              ! RESET DRP
         JMP  MPY60            ! GO TO TIGHT LOOP
!
! ********************************************************************
! MULTIPLY
! ********************************************************************
         BYT  11,51            ! ATTRIBUTES
MPYROI   JSB  =TWOSEP          ! 2 INTS OR 2 REALS
         JSB  =MPYR            ! GO MULTIPLY THEM
MPYEX    CMB  R44,=377         ! INTEGER RESULT?
         JNC  MPY11            ! JIF REAL
         PUMD R40,+R12         ! ELSE PUSH INT ON STK
         RTN                   ! EXIT
!
MPYR     JEZ  MPY30            ! JIF REALS
         CLB  R0               ! CLEAR SIGN FLAG
         TSB  R57              ! SEE IF NEG
         JPS  SGN2             ! JIF POS
         TCM  R55              ! MAKE POS
         ICB  R0               ! FLAG 1 SIGN
SGN2     TSB  R47              ! SEE IF OTHER NO. NEG
         JPS  SGN3             ! JIF POS
         TCM  R45              ! MAKE POS
         ICB  R0               ! FLAG 1 SIGN
SGN3     CMM  R45,R55          ! WHICH IS LARGEST?
         JCY  NOFLIP           ! JIF 40>=50
         JSB  =UT210           ! SMALLEST TO R50
NOFLIP   CLM  R70              ! READY FOR MULTIPLICAND
         STM  R45,R70          ! MULTIPLICAND
         CLM  R40              ! CLEAR ACCUMULATOR
         STM  R55,R50          ! RT JUSTIFY MULTIPLIER IN R50
         JZR  POS              ! TRAP OUT ZERO
         CLM  R53              ! CLEAR LEFT END R50 GARBAGE
MPYLOP   LRM  R52              ! NEXT MPYR DIGIT TO E
         DRP  R40              ! FOR TIGHT LOOP
         ARP  R70              ! FOR TIGHT LOOP
         JMP  TSTEZ            ! GO MPY BY CURRENT DIGIT IN E
!
ADLOOP   ADM  R#,R#            ! ACCUMULATE ANSWER
         DCE                   ! MULTIPLIER DIGIT DECREMENT
TSTEZ    JEN  ADLOOP           ! LOOP TILL E=0
         LLM  R70              ! FOR NEXT DECADE ALIGNMENT
         TSM  R50              ! ANY MORE#0 MULTIPLIER DIGITS?
         JNZ  MPYLOP           ! LOOP TILL MULTIPLIER DEPLETED
         CLM  R70              ! READY FOR TEST CONSTANT
         LDB  R72,=10C         ! MAX INTEGER TEST CONSTANT
         CMM  R42,R72          ! ANS TOO BIG IN ABS VALUE?
         JCY  OOPS             ! JIF ABS(ANS) > 99999
         LDM  R45,R40          ! ANSWER TO UPPER PART OF R40
         TSB  R0               ! TEST SGN FLAG FOR POS/NEG ANS
         JEV  POS              ! JIF ANS POS
         TCM  R45              ! ELSE MAKE ANS NEGATIVE
POS      LDB  R44,=377         ! INTEGER TAG
         RTN                   ! END
!
OOPS     CLB  R32              ! SIGN POS
         TSB  R0               ! TEST SIGN
         JEV  OOPS1            ! JIF POS
         NCB  R32              ! SIGN NEG
OOPS1    GTO INFR9             ! EXP=15, SHF10
!
! ********************************************************************
! ENTRY: R66 IS MULTIPLIER
!        R76 IS MULTIPLICAND
! EXIT:  R54 IS THE RESULT - 4 BYTES LONG
!   NOTE THAT THE ANSWER IS A FULL 32 BIT NUMBER AND THAT THE SIGN BIT MAY BE SET!!
! ********************************************************************
INTMUL   SAD                   ! SAVE BIN BCD
         BIN                   ! BUT I NEED BINARY
         PUMD R60,+R6          ! SAVE FOR HOMER
         PUMD R74,+R6          ! SAVE FOR HOMER
         CLM  R54              ! CLEAR ACCUMULATOR
         STM  R76,R74          ! MOVE B DOWN TO R74
         CLM  R76              ! NOW ZERO MOST SIG BYTES
         STM  R66,R60          ! MAKE OPERAND 2 BYTES
MLOOP    JZR  INTM2            ! JIF MULTIPLIER NOW ZERO
         JEV  DONTAD           ! JIF NO ADD THIS TIME
         ADM  R54,R74          ! ADD B TO ACCUM
DONTAD   LLM  R74              ! DOUBLE R74
         LRM  R61              ! MOVE R60 ONE BIT
         JMP  MLOOP            ! CONTINUE THE LOOP
!
INTM2    POMD R74,-R6          ! RESTORE R74
         POMD R60,-R6          ! RESTORE R60
         PAD                   ! RESTORE BCD/BIN
         RTN                   ! DONE
!
! ********************************************************************
! RANDOM NUMBER GENERATOR ROUTINE
! ********************************************************************
         BYT  0,55             ! ATTRIBUTES
RND10    CLB  R47              ! IN CASE 0000X
         CLM  R50              ! ZERO OUT ACCUMULATOR
         LDMD R70,=X(K-1)      ! GET LAST RANDOM NUMBER
         LRM  R77              ! WANT LAST RN RIGHT JUSTIFIED
         LDM  R60,=67C,84C,92C,30C,11C,85C,2C,0C !
! LOOP MULTIPLIER A
         LDM  R36,=15C,0C      ! MULTIPLY LOOP COUNTER
         ARP  R70              ! SET ARP
RND40    LRM  R67              ! GET MULTIPLIER DIGIT
         DRP  R50              ! SET DRP
         JMP  RND31            ! JUMP TO TIGHT LOOP
!
RND30    DCE                   ! DECREMENT MULTIPLIER DIGIT
         ADM  R#,R#            ! ADD R70 TO R50
RND31    JEN  RND30            ! LOOP TILL E=0
         LRM  R57              ! SHIFT NEW RT DIG OF PROD TO E
         ERM  R47              ! SAVE NEW DIGIT OF PROD IN R40
         DCB  R36              ! DECREMENT COUNTER
         JNZ  RND40            ! CONTINUE MULTIPLY LOOP
         STMD R40,=X(K-1)      ! SAVE NEW RANDOM NUMBER
         DCM  R36              ! EXP(RN)=-1
         JSB  =SHF10           ! ELIMINATE LEAD ZEROS
         LLB  R37              ! ADJUST EXP FOR PACKING
         STM  R36,R40          ! PACK IN EXP
         PUMD R40,+R12         ! PUSH ANSWER ON STACK & EXIT
         RTN                   ! DONE
!
! ********************************************************************
! Y ^ X
! ********************************************************************
         BYT  14,51            ! ATTRIBUTES
YTX5     JSB  =TWOR            ! GET X AND Y (REAL)
         JSB  =UT210           ! SWAP INPUTS AROUND
         STMD R50,=TEMP22      ! SAVE X
         JSB  =SEP15           ! SEPARATE SGN,MANT,EXP(Y)
         TSM  R42              ! TEST FOR 0 TO X POWER
         JZR  YTX12            ! JMP IF Y=0
         TSB  R32              ! TEST FOR NEG Y
         JRZ  YTX14            ! JMP IF Y POS
         TSB  R35              ! TEST FOR NEG EXP(X)
         JLN  YTX16            ! JMP IF NEG EXP(X)
         JMP  YTX18            ! JMP INTO X INTEGER TEST LOOP
!
YTX20    TSM  R34              ! EXP(X) REDUCED TO ZERO?
         JZR  YTX16            ! JMP IF YES
         DCM  R34              ! OTHERWISE DECREMENT EXP(X)
YTX18    LLM  R52              ! SHIFT MANT(X)
         JNZ  YTX20            ! CONTINUE LOOP IF RESIDUAL#0
         TSM  R34              ! TEST X FOR EVEN OR ODD
         JNZ  YTX14            ! JMP IF X EVEN
         ELB  R57              ! GET LAST DIGIT OF M(X) FROM E
         JOD  YTX22            ! JMP IF MANT(X) ODD
YTX14    CLB  R32              ! ZERO FOR POSITIVE ANSWER
YTX22    STB  R32,R22          ! SAVE SGN(ANS)
         JSB  =LN30            ! CALCULATE LN(Y)
         LDMD R50,=TEMP22      ! GET X
         JSB  =SEP20           ! SEPARATE IT
         JSB  =MPY30           ! X LN(Y)
         JSB  =EXP20           ! Y TO X = E TO XLN(Y)
         LDB  R32,R22          ! SGN(Y TO X) TO R32
YTX11    JMP  CSEC11           ! ROUND, NFR, AND EXIT
!
YTX12    TSM  R52              ! MANT(X)=0?
         JNZ  YTX26            ! JMP IF MANT(X)#0
!
         JSB  =ERROR           ! 0 TO 0 POWER ERROR
         BYT  6D               !
!
         LDB  R47,=10C         ! DEFAULT ANSWER = 1
         JMP  SGN6             ! PUSH ANSWER ON STACK & EXIT
!
YTX26    TSB  R33              ! TEST FOR X NEG
         JRZ  SGN6             ! JMP IF POS
!
         JSB  =ERROR           ! REPORT OVF IN YTX ROUTINE
         BYT  5D               !
!
         JMP  INF10            !
!
YTX16    JSB  =ERROR+          ! ERROR: NEG Y TO NON-INT PWR
         BYT  9D               !
!
! ********************************************************************
! SGN()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
SGN5     JSB  =ONER            ! GET REAL X IN R40
         LRB  R41              ! SAVE SIGN
         TSM  R40              ! TEST INPUT
         JZR  SGN6             ! GIVE ANS=0 IF X=0
         CLM  R40              ! ZERO OUT, REDY FOR A 1
         ICB  R47              ! ABS(ANS)=1
         ELM  R41              ! POSITION THE 1 AND ADD SIGN
SGN6     GTO NFR2              ! PUSH ANSER ON STACK & EXIT
!
DRCOM    JSB  =ONER            ! GET REAL T
         STM  R40,R50          ! COPY IT TO R50
         CLM  R40              ! CLEAR CONSTANT AREA
         JSB  =SEP20           ! SEP T IN R50
         JMP  LCOM1            ! SET SGN=EXP=0 AND EXIT
!
LOGCOM   STM  R36,R34          ! EXP(X) READY FOR DIVIDE
         STM  R40,R50          ! MANT(LN(X)) READY FOR DIVIDE
         STB  R32,R33          ! SGN(LN(X)) READY FOR DIVIDE
LCOM1    CLB  R32              ! SET SGN=0
         CLM  R36              ! SET EXP=0
LCOM2    RTN                   ! RETURN TO MAIN ROUTINE
!
! ********************************************************************
! SEC()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
SEC10    LDM  R26,=0C,90C      ! STATUS FOR COS
         JSB  =FTR12           ! CALCULATE COS
         TSM  R40              ! COS=0?
         JNZ  CSEC30           ! JIF#0
         JSB  =FTR78           ! ELSE EXIT TO ANS=+INFINITY
!
! ********************************************************************
! CSEC()
! ********************************************************************
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
CSEC10   LDM  R26,=9C,90C      ! STATUS FOR SIN
         JSB  =FTR12           ! CALCULATE SIN
         TSM  R40              ! SIN=0
         JNZ  CSEC30           ! JMP IF NOT ZERO
!
         JSB  =ERROR           ! ELSE REPORT ANS=+INFINITY
         BYT  3D               !
!
! ********************************************************************
! NOTE: CSEC10 ERRORS FALL THROUGH THE TWO BYTES OF INTF10 ATTRIBUTES
! AND THEN DO INF10.  THE TWO BYTES ARE BOTH HARMLESS ARP'S.
! ********************************************************************
!
! ********************************************************************
! INF()
! ********************************************************************
         BYT  0,55             ! ATTRIBUTES
INF10    JSB  =FTR77           ! DIRECT RETURN WITH + INF
CSEC30   JSB  =FTR53           ! 1/(SIN OR COS)
CSEC11   JMP  FTR15            ! ROUND, PACK, & RTN WITH ANS
!
! ********************************************************************
! COT()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
COT10    LDM  R26,=9C,9C       ! STATUS FOR COT
         JMP  FTR11            !
!
! ********************************************************************
! SIN()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
SIN10    LDM  R26,=9C,90C      ! SIN ENTRY
         JMP  FTR11            !
!
! ********************************************************************
! COS()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
COS10    LDM  R26,=0C,90C      ! COS ENTRY
         JMP  FTR11            !
!
! ********************************************************************
! TAN()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
TAN10    CLM  R26              ! TAN ENTRY
FTR11    JSB  =FTR12           ! GO CALCULATE FUNCTION VALUE
FTR15    JMP  RAD11            ! ROUND, NFR, AND EXIT
!
! ********************************************************************
! PI()
! ********************************************************************
         BYT  0,55             ! ATTRIBUTES
PI10     LDM  R40,=0C,0C,59C,53C,26C,59C,41C,31C ! PI FUNCTION
         JMP  ABS6             ! PUSH ANSWER ON STACK & EXIT
!
! ********************************************************************
! CEIL()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
CEIL10   JSB  =CHSROI          ! GIVES -X
         JSB  =INT5            ! FLOOR(-X)
         JSB  =CHSROI          ! CEIL(X) = -FLOOR(-X)
         RTN                   ! END
!
! OVERFLOW/UNDERFLOW ROUTINE
!
OVF19    JSB  =ERROR           ! GO SAY UNDERFLOW OCCURRED
         BYT  1D               !
!
OVF10    TSM  R40              ! TEST FOR MANTISSA=0
         JZR  LCOM1            ! IF=0, SET EXP=SGN=0 & EXIT
         CMB  R37,=5C          ! TESET EXP SIZE
         JNC  INFR10           ! JMP(RTN) IF OK POS EXP
         CMM  R36,=1C,95C      ! TEST EXP SIZE
         JCY  INFR10           ! JMP(RTN) IF OK NEG EXP
         CLM  R40              ! OVF OR UF. CLEAR MANT(X)
         CMB  R37,=50C         ! TEST EXP SIZE
         JCY  OVF19            ! JMP IF UNDERFLOW
         LDM  R36,=99C,4C      ! EXP(X)=499
         NCM  R42              ! MANT(X)=99...90000
!
         JSB  =ERROR+          ! GO SAY OVERFLOW OCCURRED
         BYT  2D               !
!
! ********************************************************************
! RAD() DEGREES TO RADIANS
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
RAD10    JSB  =DRCOM           ! COMMON SETUP WITH RAD TO DEG
         LDB  R36,=2C          ! EXP(45)+1
         LDB  R47,=45C         ! 45 TO R40
!
! EVERETT KASER - AUG 2016
! BOGOSITY ALERT!!!  THE COMMENT ON THE PREVIOUS LINE (WITHOUT A ! IN THE ORIGINAL
! SOURCE) WAS APPARENTLY INTERPRETED BY CASM AS AN ARP INSTRUCTION, SO THERE'S AN
! EXTRANEOUS ARP INSTRUCTION HERE THAT DOESN'T SHOW IN THE ORIGINAL SOURCE, ALTHOUGH
! THE BYTE OF INSTRUCTION (ARP R45) *DOES* SHOW IN THE ORIGINAL CODE.  DIV20 DOESN'T
! CARE WHAT THE ARP IS ON ENTRY, SO THIS IS AN EXTRA BYTE OF CODE THAT WAS ACCIDENTALLY
! INCLUDED BUT WHICH DIDN'T CAUSE ANY BUGS DURING EXECUTION.
!
         ARP  R45              !
         JSB  =DIV20           ! T/450
         LDMD R50,=DCON1       ! GET PI/4
         CLB  R33              ! SGN(PI/4)=0
         CLM  R34              ! EXP(PI/4)+1
         JSB  =MPY30           ! T(RAD)=T(DEG) X PI/180
RAD11    JMP  RONF             ! ROUND, NFR, AND EXIT
!
! ********************************************************************
! ABS()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
ABS5     JSB  =ONER            ! GET REAL X
         LRB  R41              ! SHIFT OUT OLD SIGN
         LLB  R41              ! SHIFT IN ZERO
ABS6     JMP  NFR2             ! PUSH ANSWER ON STACK & EXIT
!
INTFRA   JSB  =ONER            ! GET REAL X
INFR3    JSB  =SEP10           ! SEPARATE IT
INFR4    STM  R36,R34          ! DUPLICATE EXP(X)
         CLM  R50              ! INITIAL INT(X)
         TSB  R35              ! ABS(X) >= 1?
         JLN  INFR10           ! JIF X<1 (INT(X)=0, FRA(X)=X)
INFR5    TSM  R40              ! ANYTHING LEFT TO SHIFT?
         JZR  INFR10           ! JIF NO NON-ZERO DIGITS LEFT
         LLM  R40              ! ELSE SHIFT LEFT DIGIT TO E
         ELM  R50              ! THEN TO R50 FOR INT(X)
         DCM  R36              ! DECR INT(X) DIGIT COUNT
         JCY  INFR5            ! LOOP IF MORE INT(X) DIGITS
INFR10   RTN                   ! RTN
!
! ********************************************************************
! INT() FLOOR()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
INT5     CLB  R2               ! CLEAR FLAG AREA
         ICB  R2               ! FLAG=1 FOR FLOOR(X) (=INT(X))
         JMP  IP4              ! GO FIND ANSWER
!
! ********************************************************************
! INTDIV
! ********************************************************************
         BYT  11,51            ! ATTRIBUTES
INTDIV   JSB  =TWOR            ! DEMAND REAL A AND B
IDIV+2   JSB  =SEP15           ! SEPARATE A AND B
         JSB  =DIV88           ! 16 DIGIT ANSWER FOR A/B
         CLB  R2               ! FLAG=0 FOR IP(X)
         JMP  IP3              ! FIND INT(16 DIGIT SEPARATED X)
!
INFR1    CLB  R2               ! FLAG=0 SAYS FIND IP(X)
INFR2    JSB  =INFR4           ! SPLIT APART IP(X), FP(X)
         JSB  =UT210           ! IP(X) TO R40, FP(X) TO R50
         TSM  R50              ! FP(X)=0?
         JZR  TRUNC            ! JIF X=INT (REAL) ALREADY
         TSB  R2               ! IP(X) OR INT(X)
         JZR  TRUNC            ! JIF IP(X)
         TSB  R32              ! X<0?
         JRZ  TRUNC            ! JIF X>=0 (NO ANS ADJUST NEC)
         ICM  R40              ! ELSE ANS=NEXT SMALLEST INTEGER
INFR9    LDM  R36,=15C,0C      ! INITIALIZE EXP(ANS)
         GTO SHF10             ! ELIM LEAD 0'S, ADJ EXP & EXIT
!
TRUNC    JSB  =SHF10           ! SHIFT OUT LEAD 0'S
         LDM  R36,R34          ! RESTORE EXP(X)
         RTN                   ! IP(X) OR INT(X) IN 32,36,40
!
! ********************************************************************
! FP()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
FP5      JSB  =INTFRA          ! GEN FP(X) IN R32, R36, R40
SHRONF   JSB  =SHF10           ! SHIFT OUT LEAD ZEROS
RONF     JSB  =ROU10           ! ROUND RESULT
NFR      JSB  =NFR5            ! JSB TO NFR INNER LOOP
NFR2     DRP  R40              ! POINT AT RESULT TO BE PUSHED
NFR3     PUMD R#,+R12          ! PUSH RESULT ON STACK
         RTN                   ! RETURN
!
NFR5     JSB  =OVF10           ! CHECK FOR OVERFLOW
         STM  R36,R40          ! PACK IN EXPONENT
         LRB  R32              ! PUT SIGN IN E
         ELB  R41              ! PACK UP SIGN
         RTN                   ! RETURN
!
! ********************************************************************
! EPS()
! ********************************************************************
         BYT  0,55             ! ATTRIBUTES
EPS10    JSB  =TRC01           ! GET 1
         LDB  R51,=50C         ! GIVES 1E-500
         ICB  R50              ! GIVES 1E-499
         JMP  NFR3             ! GO PUSH ANS ON STACK AND EXIT
!
! ********************************************************************
! DEG() RADIANS TO DEGREES
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
DEG10    JSB  =DRCOM           ! COMMON SETUP WITH DEG TO RAD
         ICM  R34              ! 10T
         ICM  R34              ! 100T
         JSB  =TRC7            ! GET PI/2
         LDM  R40,R70          ! MOVE IT TO R40
         JSB  =DIV20           ! 100T/(PI/2)
         STM  R40,R50          ! 100T/(PI/2)
         LRM  R57              ! .1(100T/(PI/2))
         SBM  R40,R50          ! .9(100T/(PI/2))=T IN DEG
         JMP  SHRONF           ! SHIFT, ROUND, NFR, AND EXIT
!
! ********************************************************************
! IP()
! ********************************************************************
         BYT  20,55            ! ATTRIBUTES
IP5      CLB  R2               ! FLAG=0 FOR IP(X)
IP4      JSB  =ONEROI          ! GET X
         JEN  NFR2             ! JIF BCD INTEGER ALREADY
         JSB  =SEP10           ! SEPARATE X
IP3      JSB  =INFR2           ! ELSE FIND IP(X) OR INT(X)
         JSB  =RONF            ! PACK UP ANS AND PUT ON STACK
         POMD R60,-R12         ! GET ANSWER
         JSB  =RTOIN           ! TRY TO CONVERT IT TO BCD INT
         LDB  R64,=377         ! INT TAG IN CASE CONVERTED OK
         DRP  R60              ! ANS PTR IN CASE CONVERTED OK
         JEZ  NFR3             ! JIF ANSWER CONVERTED TO BIN OK
         DRP  R70              ! ELSE POINT TO FLOATING ANSWER
         JMP  NFR3             ! GO PUSH ANSWER ONTO STACK
!
! ********************************************************************
! MAIN FORWARD TRIG SUBROUTINE
! ********************************************************************
FTR12    JSB  =ONER            ! GET REAL T=THETA FROM STACK
         JSB  =SEP10           ! SEPARATE SGN,MANT,EXP(T)
         CLB  R22              ! INITIALIZE S4=0
         TSB  R32              ! T<0?
         JRZ  FTR14            ! JMP IF THETA>=0
         CLB  R32              ! SET T>0 (REFLECT ABOUT X-AXIS)
         TSM  R26              ! S6=0?
         JLZ  FTR19            ! JIF S6=0 (TAN OR COT)
         JRZ  FTR14            ! JIF S6=9 & S10=0 (COS)
FTR19    NCB  R22              ! SIN(-T)=-SIN(T) (CSEC,TAN,COT)
FTR14    LDBD R25,=DRG         ! GET DEG,RAD,GRD INDICATOR
         JPS  FTR16            ! JIF RADIANS
         JEV  FTR18            ! JIF DEGREES
         STM  R40,R60          ! T IN GRDS.
         LRM  R67              ! .1T
         SBM  R40,R60          ! .9T (GIVES T IN DEGREES)
FTR18    CLM  R70              ! GET READY TO LOAD CONST
         LDB  R77,=45C         ! LOAD ANGLE CONSTANT 45
         DCM  R36              ! XX.XXX MANT(T) DEC LOC ADJUST
         TSB  R37              ! T<10 DEG?
         JLN  FTR20            ! JMP IF T<10 DEG
         DCM  R36              ! XXX.XX MANT(T) DEC LOC ADJUST
         JCY  FTR20            ! JMP IF 100 DEG <= T
         ICM  R36              ! XX.XXX MATN(T) DEC LOC ADJUST
         LRM  R47              ! GIVES 0XX.XX MANT(T)
FTR20    STM  R70,R50          ! STORE PI/4 OR 45
         TSB  R37              ! T IN FIRST QUADRANT?
         JLZ  FTR24            ! JIF NO
         TSB  R25              ! DEG OR RAD MODE?
         JNG  FTR32            ! JMP IF DEG
         LRM  R47              ! ADJUST DEC LOC AND EXP
         ICM  R36              ! RAD FORMAT=0.XX, DEG=XX.X
         JMP  FTR32            ! T FORMAT=X.XX RAD, XX.X DEG
!
FTR16    LDMD R70,=DCON1       ! PI/4 TO R70
         JMP  FTR20            ! CONTINUE
!
FTR24    LRM  R57              ! CREATE ROOM FOR LEFT CARRY
         ADM  R50,R50          ! PI/2 OR 90
         ADM  R50,R50          ! PI OR 180
         ADM  R50,R50          ! 2*PI OR 360 IN R50
         CLE                   ! CREATE LEAD 0
         ICE                   ! DUMMY OFFSET FUE TO NEXT INSTR
FTR17    DCE                   ! BORROW 1 FROM LEFT DIGIT
FTR25    SBM  R40,R#           ! CAST OUT 2PI/360 AT HIGH DECADE
         JCY  FTR25            ! LOOP TIL OVERDRAFT
         JEN  FTR17            ! JIF CAN BORROW ONE FROM E
         ADM  R40,R#           ! ELSE RECOVER FROM OVERDRAFT
         LLM  R40              ! PREPARE FOR NEXT LOWER DECADE
         DCM  R36              ! DECREMENT DECADE COUNTER
         JCY  FTR25            ! LOOP TIL ALL DECADES DONE
         CLM  R36              ! EXP(T)=0. X.XX RAD, XXX.X DEG.
         ERM  R47              ! RESTORE R40
         LDM  R50,R70          ! PI/4 OR 45 TO R50
         LRM  R57              ! RAD: CARRY SLOT, DEG: DEC ALGN.
         ADM  R50,R50          ! PI/2 (1.57...) OR 090.00.
FTR26    SBM  R40,R50          ! T-(PI/2 OR 90)
         JNC  FTR28            ! JIF OVERDRAFT
         NCB  R26              ! CHANGES TRIG FUNCTION TO ITS CO-FN
         JRN  FTR29            ! WAS COS OR TAN: CHS OF ANS.
         TSB  R27              ! COT OR SIN?
         JLN  FTR26            ! JIF NOT COT
FTR29    NCB  R22              ! CHS OF VALUE OF ANS OF TRIG FN
         JMP  FTR26            ! CONTINUE LOOPING
!
FTR38    ADM  R40,R50          ! RECOVER FROM OVERDRAFT
         JMP  FTR34            ! CONTINUE
!
FTR28    ADM  R40,R50          ! RECOVER FROM OVERDRAFT
         TSB  R25              ! DEG OR RAD?
         JPS  FTR30            ! JIF RAD
         LLM  R40              ! ADJUST DEC LOCATION TO XX.X.
FTR30    LDM  R50,R70          ! GET PI/4 OR 45
FTR32    TSB  R37              ! DOES T HAVE NEG EXP?
         JLN  FTR34            ! JIF YES
         TSB  R25              ! DEG OR RAD?
         JNG  FTR36            ! JIF DEG
         LRM  R57              ! ALIGN DEC(0.7...):RAD MODE.
FTR36    SBM  R40,R50          ! T-(PI/4 OR 45)
         JNC  FTR38            ! JIF T<45 ALREADY
         SBM  R40,R50          ! T-(PI/2 OR 90)
         TCM  R40              ! (PI/2 OR 90)-T
         NCB  R26              ! CHANGE TO CO-FUNCTION
FTR34    JSB  =SHF10           ! ELIMINATE LEADING ZEROES
FTR40    TSB  R25              ! DEG OR RAD TEST
         JPS  FTR42            ! JIF RAD
         JSB  =UT210           ! MAT(T) TO R50, 45 TO R40
         STM  R36,R34          ! MOVE EXP FOR DIVIDE
         CLM  R36              ! EXP(45/10)
         ICM  R36              ! EXP(45)
         JSB  =DIV20           ! T/45
         LDMD R70,=DCON1       ! PI/4 TO R70
         STM  R70,R50          ! PI/4 TO R50
         CLM  R34              ! SET EXPONENT FOR PI/4
         JSB  =MPY30           ! (T/4.5) TIMES PI/4
FTR42    LDM  R20,=7C,0C       ! INITIALIZE PQ COUNTER
         LDM  R30,=TBL3        ! POINTER TO TRIG CONSTANT TABLE
         LDM  R34,R36          ! DUPE EXPONENT
         ICM  R34              ! INC EXP(T)
         JLZ  FTR62            ! JIF .1<=T<1.
         LRM  R47              ! ADJUST FORMAT OF T TO 0.XX.
FTR46    ICM  R34              ! INC EXP(T)
         JLZ  FTR62            ! JIF EXP(T)=0
         POMD R60,+R30         ! DUMMY POP TO INCR R30 BY 10
         DCB  R20              ! DECREMENT PQ COUNTER
         JNZ  FTR46            ! LOOP IF PQ CTR # 0
         STB  R22,R32          ! SMALL ANGLE PATH; SETUP SGN(T)
         LLM  R40              ! ELIM LEAD ZERO CREATED ABOVE
         TSM  R26              ! WHICH FN IS BEING CALCULATED
         JRZ  FTR60            ! JIF TAN OR COS
         JLN  FTR54            ! JIF SIGN, ANS=T
FTR53    JSB  =TRC01           ! GET CONST 1
         JSB  =DIV20           ! COMPUTE ANS = 1/T
FTR54    RTN                   ! RETURN WITH ANSWER
!
FTR62    CLM  R50              ! CLEAR PQ AREA
         LLM  R40              ! LEFT DIG TO E FOR PQ0 ROUTINE
FTR64    POMD R70,+R30         ! GET NEXT TRIG CONSTANT
         JSB  =PQO10           ! COMPUTE PQ DIGIT
         DCB  R20              ! DECREMENT PQ COUNTER
         JNZ  FTR64            ! JMP(LOOP) IF NOT ZERO
         ERM  R47              ! RECOVER FROM LAST SHIFT IN PQ0
         LRM  R47              ! READY FOR PSEUDO-MULTIPLY
         LRM  R57              ! PROPERLY POSITION PSEUDO-QUO
         CLM  R60              ! CLEAR X ACCUMULATOR
         ICB  R67              ! INITIALIZE FIRST
         LLB  R67              ! X TO 1
         LDM  R36,=7C,0C       ! J=7, AND CLEAR EXP(X) AREA
         JMP  FTR66            ! BEGIN PSEUDO-MULTIPLY LOOP
!
FTR68    DCB  R31              ! J=J-1
         LRM  R77              ! Z(10 TO (-J)) LAST TIME THRU
         LRM  R77              ! Z(10 TO(-2J)) LAST TIME THRU
FTR70    TSB  R31              ! J REDUCED TO 0 YET?
         JNZ  FTR68            ! JMP (LOOP) IF NOT = 0 YET
         ADM  R40,R60          ! Z = Z+X
         SBM  R60,R70          ! X=X-Z(10 TO (-2J))
FTR66    STM  R40,R70          ! SAVE Z
         STB  R36,R31          ! SAVE J
         TSB  R50              ! CURRENT PQ DIGIT = 0?
         JRZ  FTR72            ! JMP IF = 0
         DCB  R50              ! DECREMENT CURRENT PQ DIGIT
         JMP  FTR70            ! GO TO SHIFT LOOP
!
FTR72    LRM  R57              ! GET NEXT PQ DIGIT
         TSM  R50              ! ANY MORE NON-ZERO PQ DIGITS?
         JZR  FTR74            ! JMP IN NO MORE
         DCB  R36              ! REDUCE J FOR NEXT DECADE
         LRM  R47              ! SHIFT THE SUM
         JMP  FTR66            ! CONTINUE PSEUDO-MULTIPLY LOOP
!
FTR60    JLZ  FTR54            ! JIF TAN, ANS=T
         CLM  R40              ! COS(T)=
         LDB  R47,=10C         ! +1 OR -1
         CLM  R36              ! EXP(ANS)=0
         JMP  FTR84            ! GO GET SGN AND RTN WITH ANS
!
FTR74    LDM  R50,R60          ! MOVE X TO R50
         CLM  R34              ! EXP(Y)=0
         CLM  R32              ! SIGNS THE SAME FOR DIVIDE
         TSB  R26              ! WHICH FUNCTION?
         JRN  FTR76            ! JIF SIN OR COT
         JSB  =UT210           ! SWAP X AND Y(10 TO J)
         TCM  R36              ! REPLACE J BY -J
FTR76    TSM  R40              ! DENOMINATOR=0?
         JNZ  FTR79            ! JMP IF NOT =0
         TSB  R27              ! TAN?
         JLN  FTR54            ! JIF NOT TAN OR COT
         JRZ  FTR78            ! JIF TAN
!
         JSB  =ERROR           ! REPORT COT FOR T ON X AXIS
         BYT  3D               !
!
         JMP  FTR77            ! GO GIVE ANS = +INF
!
FTR78    JSB  =ERROR           ! TRIG OVERFLOW
         BYT  4D               !
!
FTR77    CLE                   ! SGN +INF=0
FTR99    CLM  R40              ! READY FOR ALL 9'S
FTR88    NCM  R40              ! TAN90=9.99...99E499
         LDB  R41,=4C          ! SGN(MANT)=0. EXP=499
         ELB  R41              ! PACK IN SIGN OF OVF ANS
FTR73    PUMD R40,+R12         ! PUSH ANSWER ONTO STACK
         POMD R0,-R6           ! POP RETURN STACK AND RETURN
         RTN                   ! DONE
!
FTR79    TCM  R36              ! MAKES EXP(NUM) INCR IN SHF10
         JSB  =SHF10           ! PROTECT FOR 10/0N... DIV BUG
         JSB  =DIV20           ! GIVES TAN OR COT
         TSB  R27              ! WHICH FUNCTION?
         JLZ  FTR84            ! JMP IF TAN OR COT
         STM  R36,R34          ! DUPLICATE EXP(TAN)
         STM  R40,R50          ! DUPLICATE MANTISSA
         JSB  =MPY30           ! SQUARE TAN(T) (OR COT(T))
         JSB  =TRC01           ! GET CONSTANT 1
         JSB  =ADD20           ! ADD 1
         JSB  =SQR30           ! SQR(1+TANTAN) OR SQR(1+COTCOT)
         JSB  =FTR53           ! ANS = SIN OR COS
FTR84    STB  R22,R32          ! SGN(ANS)
         RTN                   ! RETURN WITH ANSWER
!
TRC7     LDMD R70,=DCON1       ! GET PI/4
         LRM  R77              ! LEFT CARRY DIGIT AREA
         ADM  R70,R70          ! PI/2
         RTN                   ! END
!
TRC01    CLB  R33              ! SGN(CONST)=0
TRCS1    CLM  R50              ! ZERO OUT CONSTANT AREA
         LDB  R57,=10C         ! MANT(CONST)=1
         CLM  R34              ! EXP(CONST)=0
         RTN                   ! END
!
RNDINI   LDMD R40,=RNDS        ! DEFAULT SEED TO R40
         JMP  RSET20           ! GO STORE SEED AND EXIT
!
! ********************************************************************
! RANDOMIZE
! ********************************************************************
         BYT  241              !
RNDIZ.   JSB  =ON?R            ! GET OPTIONAL PARAMETER
         JEN  CFP              ! JIF USER SUPPLIED SEED
RNTIME   JSB  =TIME.           ! GET SYSTEM TIME
         POMD R40,-R12         ! POP TIME IN MILLISECONDS
         JZR  RNTIME           ! TRY AGAIN IF ZERO
CFP      JSB  =SEP10           !
RNDSET   TSM  R40              ! RANDOMIZE 0?
         JZR  RSET20           ! JIF YES
RSET9    ICM  R36              ! FIX UP ZERO OTHERWISE
         JPS  RSET10           ! QUIT WHEN EXP GOES POSITIVE
         LRM  R47              ! SHIFT MANTISSA
         JNZ  RSET9            ! LOOP IF MANT#0
RSET10   STB  R36,R41          ! CONCATENATE 2 DIGITS OF EXP
         LDB  R40,=10C         ! CONCATENATE A 1
RSET20   STMD R#,=X(K-1)       ! STORE THE NEW SEED
         RTN                   ! RTN CONTROL TO CALLING ROUTINE
!
! ********************************************************************
! ROUND ROUTINE
ROU10    STM  R40,R50          ! COPY MANTISSA
         CLM  R52              ! CLEAR ALL BUT LAST 4 DIGITS
         ADM  R40,R50          ! ADD TO ORIGINALK MANTISSA
         JNC  SEP41            ! CARRIES IF M>=9999999999995
         LDB  R47,=10C         ! MANT=100000000000
         ICM  R36              ! ADJUST EXPONENT
         JMP  SEP41            ! GO CLEAR R40 AND R41 AND EXIT
!
SEP20    LDM  R34,R50          ! UNPACK B: EXP(B) TO R34
         LRB  R35              ! SGN(MANT) TO E
         CMB  R35,=5C          ! EXP SIGN NEG?
         JNC  SEP30            ! JMP IF EXP SIGN POS
         ADB  R35,=90C         ! EXP IN R34M IN 10 COMPL FORM
SEP30    ELB  R33              ! SGN(B) TO R33
         CLB  R50              ! CLEAR NON-
         CLB  R51              !    MANTISSA DIGITS
SEP35    RTN                   ! END
!
TWOSEP   JSB  =TWOROI          ! GET THE DATA
         JEN  SEP35            ! DONE IF INTEGER
SEP15    BCD                   !
         LDM  R34,R50          ! EXP TO R34
         CLB  R50              ! CLEAR EXP
         CLB  R51              !
         LRB  R35              ! SIGN TO E
         CMB  R35,=5C          ! SIGN OF EXP?
         JNC  SAP30            ! JIF EXP SIGN POS
         ADB  R35,=90C         ! EXP IN R34M IN 10 COMP FORM
SAP30    ELB  R33              ! SIGN(B) TO R33
! NOW DOING OLD SEP10
SEP10    LDM  R36,R40          ! UNPACK A:EXP TO R36
         LRB  R37              ! SGN(MANT) TO E
         CMB  R37,=5C          ! EXP SIGN NEGATIVE?
         JNC  SAP40            ! JIF NO, POSITIVE
         ADB  R37,=90C         ! AT 90 BCD TO MAKE R36 EXP IN 10'S COMPLEMENT FORM
SAP40    ELB  R32              ! SGN(A) TO R32
         CLE                   !
SEP41    CLB  R40              ! CLEAR EXP
         CLB  R41              !
DONE     RTN                   ! DONE
!
! ********************************************************************
! UTILITY ROUTINES
! ********************************************************************
UT110    STM  R40,R60          ! MANT TO R60
         CLM  R40              ! INITIALIZE
UT110F   ADM  R36,R34          ! ADD EXPONENTS
         XRB  R32,R33          ! CALCULATE SIGN OF ANSWER
         ARP  R60              ! SET ARP
         RTN                   ! END
!
UT210    STM  R50,R60          ! R50 TO TEMP
         LDM  R50,R40          ! R40 TO R50
         STM  R60,R40          ! TEMP TO R40
         RTN                   ! END
!
! ********************************************************************
! EXP/TRIG PSEUDO-QUOTIENT ROUTINE
PQO30    DCE                   ! BORROW FROM E
PQO20    ICB  R50              ! TALLY 1 FOR SUCCESSFUL SUBTRACT
PQO10    SBM  R40,R70          ! SUBTRACT LN(1+(10 TO (-J)))
         JCY  PQO20            ! LOOP TILL OVERFLOW
         JEN  PQO30            ! CONTINUE LOOP IF E#0
         ADM  R40,R70          ! RECOVER FROM OVERDRAFT
         LLM  R50              ! READY PQ AREA FOR NEXT DIGIT
         LLM  R40              ! R40 & E READY FOR NEXT DECADE
         RTN                   ! END
!
! ********************************************************************
! MIN()
! ********************************************************************
         BYT  40,55            ! ATTRIBUTES
MIN10    JSB  =TWOR            ! GET REAL A AND B
         JSB  =UT210           ! PUT B IN R50, A IN R40
         PUMD R40,+R12         ! REAL COPY OF A ON STACK
         PUMD R50,+R12         ! REAL COPY OF B ON STACK
         JMP  MAX11            ! CONTINUE
!
! ********************************************************************
! MAX()
! ********************************************************************
         BYT  40,55            ! ATTRIBUTES
MAX10    JSB  =TWOR            ! GET REAL A AND B
         PUMD R50,+R12         ! REAL COPY OF A TO STACK
         PUMD R40,+R12         ! REAL COPY OF B TO STACK
MAX11    JSB  =SEP15           ! SEPARATE A AND B
         NCB  R32              ! NEGATE B FOR A-B (B-A IF MIN)
         JSB  =ADD20           ! A+(-B) OR B+(-A)
         POMD R50,-R12         ! POP B; A STILL ON STACK
         TSB  R32              ! A-B POS? (B-A POS?)
         JRZ  MAX30            ! IF POS, ANS=A (BOTH CASES)
         POMD R40,-R12         ! RID STACK OF A
         PUMD R50,+R12         ! PUT ANS=B ON STACK
MAX30    RTN                   ! END
!
! ********************************************************************
! MAIN EXP(X) SUBROUTINE
! ********************************************************************
EXP18    JSB  =SEP10           ! SEPARATE X
EXP20    JSB  =EXP17           ! CACULATE EXP(X0) - 1
         JSB  =TRCS1           ! GET 1 BUT LEAVE R33 ALONE
         JSB  =ADD20           ! (EXP(X0)-1)+1
         ADM  R36,R14          ! K=EXP(ANS)
         TSB  R32              ! X<0?
         JRZ  EXP22            ! JIF X POS
         CLB  R32              ! SGN=0
         JSB  =FTR53           ! EXP(X) = 1/EXP(ABS(X))
EXP22    RTN                   ! END
!
EXP17    STB  R32,R33          ! SAVE SGN(X) (NEWR KILLS R32)
         LDM  R24,=TBL2        ! PT TO LN10; BOTTOM OF LN TABLE
         CLM  R50              ! CLEAR PQ AREA
         CLM  R26              ! J=0
         CLM  R14              ! K ACCUMULATOR FOR X-KLN(10)
         CLE                   ! FOR PRESCALE & ENTERING PQO
         CMB  R37,=50C         ! EXP(X)<0?
         JCY  EXP30            ! JIF EXP(X)<0
         LDMD R70,R24          ! GET LN(10)
         ARP  R70              ! SET ARP
EXP66    ERB  R30              ! SAVE E
         LLM  R14              ! FOR NEXT DECADE IN EXP(ANS)
         LLB  R30              ! RESTORE E
         JMP  EXP24            ! TO CAST OUT LN(10)'S
!
EXP26    DCE                   ! BORROW FROM E
EXP25    ICM  R14              ! K = K+1
EXP24    SBM  R40,R#           ! X-LN(10)
         JCY  EXP25            ! LOOP TIL OVERDRAFT
         JEN  EXP26            ! LOOP TILL E=0
         ADM  R40,R#           ! RECOVER FROM OVERDRAFT
         LLM  R40              ! LEFT DIGIT TO E; 0 IN FROM RT
         CMM  R14,=99C,9C      ! EXP(ANS)>998
         JNC  EXP28            ! JIF EXP(ANS) TOO BIG
         LDM  R14,=98C,9C      ! LARGE EXP FOR OVF
         CLM  R36              ! SET EXP(R40)=0
         CLM  R40              ! READY FOR #0 MANTISSA
         NCM  R42              ! #0 MANTISSA
EXP29    RTN                   ! RTN TO OUTER LOOP
!
EXP28    DCM  R36              ! DECR EXP(X) EACH LOWER DECADE
         JNC  EXP31            ! JIF EXP(X) DEPLETED
         JMP  EXP66            ! LOOP & SUB LN10'S NEXT LWR DEC
!
EXP30    LDM  R26,R36          ! COPY EXP(X)
         NCM  R26              ! J=ABS(EXP(X))-1
         CMM  R26,=8C,0C       ! J<=7?
         JCY  EXP34            ! JIF J>7
         BIN                   ! ELSE SET MODE FOR SHIFTS
         LLM  R26              ! GIVES 2J
         LLM  R26              ! GIVES 4J
         LLM  R26              ! GIVES 8J
         SBM  R24,R26          ! POINT TO JTH LN CONSTANT
         BCD                   ! RESET MODE
EXP31    POMD R70,-R24         ! GET NEXT LN CONSTANT
         JSB  =PQO10           ! GET NEXT PQ DIGIT
         BIN                   ! SET MODE FOR COMPARE
         CMM  R24,=TBL1        ! LAST TABLE ENTRY YET?
         BCD                   ! RESET MODE
         JNZ  EXP31            ! LOOP TILL ALL PQ DIGITS FOUND
         ERM  R47              ! RECOVER FROM LAST SHIFT IN PQO
         LDM  R26,=7C,0C       ! J=7
         LDM  R36,=92C,99C     ! EXP(R) = -8
EXP34    STM  R50,R70          ! SAVE PSEUDO QUOTIENT
         JSB  =NEWR            ! GO CALCULATE R/(1-.5R)
         STB  R33,R32          ! RESTORE S(X)
         JMP  EXP39            ! JMP TO PSEUDO-MULTIPLY LOOP
!
EXP38    DCM  R26              ! NO. OF RT SHIFTS DESIGNATOR
EXP39    LRM  R74              ! NEXT PQ DIGIT TO RT END OF R70
         TSM  R70              ! PSEUDO-QUOTIENT=0?
         JZR  EXP29            ! EXIT WHEN PQ EXHAUSTED
         LRM  R47              ! LEAD 0
         ICM  R36              ! ADJUST EXP(EXP(X0)-1)
         JMP  EXP42            ! GO SEE IF CURRENT PQ DIGIT=0
!
EXP40    LRM  R57              ! SHIFT P
EXP41    DCM  R24              ! DECR SHIFT COUNTER
         JCY  EXP40            ! LOOP TILL CTR<0
         ADM  R40,R50          ! NEW P=P+SHIFTED P
         ADM  R47,=20          ! NEW P=NEW P+(10 TO J)
EXP42    TSB  R70              ! CURRENT PQ DIGIT = 0?
         JRZ  EXP38            ! JIF DONE WITH CURRENT PQ DIGIT
         DCB  R70              ! ELSE DECR CURRENT PQ DIGIT
         STM  R40,R50          ! COPY P=-PARTIAL PRODUCT
         LDM  R24,R26          ! COPY SHIFT COUNTER
         JMP  EXP41            ! GO SHIFT P
!
DCON1    BYT  80C,44C,97C,33C,16C,98C,53C,78C !
TBL1     BYT  34C,0C,0C,0C,95C,99C,99C,99C !
         BYT  34C,33C,0C,0C,50C,99C,99C,99C !
         BYT  31C,33C,33C,0C,0C,95C,99C,99C !
         BYT  34C,8C,33C,33C,0C,50C,99C,99C !
RNDS     BYT  32C,53C,83C,30C,33C,0C,95C,99C !
         BYT  83C,80C,16C,53C,8C,33C,50C,99C !
         BYT  87C,24C,43C,80C,79C,1C,31C,95C !
         BYT  54C,94C,59C,5C,18C,47C,31C,69C !
TBL2     BYT  46C,40C,99C,92C,50C,58C,2C,23C !
TBL3     BYT  3C,62C,11C,49C,52C,86C,66C,99C ! TRIG CONSTANT TABLE
         BYT  38C,52C,66C,86C,66C,66C,99C,99C !
         BYT  67C,86C,66C,66C,66C,99C,99C,99C !
         BYT  67C,66C,66C,66C,99C,99C,99C,99C !
         BYT  67C,66C,66C,99C,99C,99C,99C,99C !
         BYT  67C,66C,99C,99C,99C,99C,99C,99C !
         BYT  67C,99C,99C,99C,99C,99C,99C,99C !
!
!
! ********************************************************************
! REAL/INTEGER DATA FETCH
! DATA LOCATION AT ROUTINE EXIT:
! ONER: REAL IN R40
! ONEI: BCD INT IN R40
! ONEROI: REAL IN R40 OR INTEGER IN R40
! ONEB: BINARY INT IN R40
! TWO---: B=1ST OFF STACK IN R40, A=2ND IN R50
! SOME EXTRA STUFF TO GET ONE INTEGER
! ********************************************************************
!
! ********************************************************************
! ONEB - GET ONE BIN INT, 32767 IF TOO BIG
! RETURNS E<>0 FOR OVF, UNDERFLOW
ONEB     BCD                   ! GET 1 NUMBER OFF R12 AS 15-BIT SIGNED BINARY
         POMD R60,-R12         ! GET VAL FROM STAK
         CMB  R64,=377         ! INT?
         JNC  REALB            ! JIF REAL
         LRB  R65              ! LSB TO E
         TSM  R65              !
         JNZ  ONEB1            ! JIF NOT SMALL INT
         CLM  R76              !
         ELB  R76              ! ANS TO 46
         CLE                   !
ONEBJ    STM  R76,R46          !
         BIN                   !
         RTN                   !
!
ONEB1    ELB  R65              !
         JSB  =INTORL          ! CONVERT TO REAL
REALB    JSB  =CONINT          ! CONV 60 TO BIN INT IN 76
         JMP  ONEBJ            !
!
! ********************************************************************
! ONEI - GET ONE BCD INT, 99999 IF TOO BIG
ONEI     JSB  =ONEROI          ! GET ONE OF EITHER
         JEN  ONEIOK           ! JIF INTEGER FOUND
         LDM  R60,R40          ! MOVE ANSWER TO R60
         JSB  =RTOIN           ! CONVERT TO BCD INTEGER
         LDB  R44,=377         !
         LDM  R45,R65          !
         RTN                   ! DONE
!
! ********************************************************************
! TWOB - GET TWO BIN INT, EXIT IN BIN
TWOB     JSB  =ONEB            ! GET TWO NUMBERS OFF R12 AS 15-BIT SIGNED #'S
         STM  R46,R26          !
         JSB  =ONEB            ! GET THE 2ND ONE
         STM  R46,R56          !
         LDM  R46,R26          !
         RTN                   !
!
! ********************************************************************
! ONER - GET ONE REAL, CONVERT IF NECESSARY
ONER     POMD R60,-R12         ! GET TAG
ONER+    CMB  R64,=377         ! IS NO. ON STACK REAL?
         JNC  FLORTN           ! JIF YES
RIDF20   JSB  =INTORL          ! CONVERT IT TO FLOATING
FLORTN   BCD                   ! REALS MUST BE BCD
         STM  R60,R40          !
ONEIOK   CLE                   ! NEEDED FOR TWOROI AND ONEI
         RTN                   ! END
!
! ********************************************************************
! TWOR - GET TWO REALS, CONVERT IF NECESSARY
TWOR     JSB  =ONER            ! GET ONE OF THEM
         STM  R40,R50          ! SAVE FIRST RESULT
         JSB  =ONER            ! NOW GET SECOND ONE
         JSB  =UT210           ! A TO R50, B TO R40
         RTN                   ! DONE
!
! ********************************************************************
! ONEROI - FETCH ONE REAL OR INTEGER
ONEROI   CLE                   ! RESET FLAG
         POMD R40,-R12         ! GET VALUE
         CMB  R44,=377         ! IS NO. ON STACK REAL?
         JNC  ROIRTN           ! JIF YES (DONE)
         ICE                   ! FLAG INTEGER
ROIRTN   RTN                   ! DONE
!
! ********************************************************************
! TWOROI - GET 2 REAL OR INTEGER
!
! THERE ARE FOUR CASES OF TWOROI:
!           B    A
!          R44  R54
! CASE 1:  377  377  BOTH INTEGERS
! CASE 2:  377  BCD  B REAL, A INTEGER
! CASE 3:  BCD  377  A REAL, B INTEGER
! CASE 4:  BCD  BCD  BOTH REAL
!
! MODE ON RETURN IS BCD
!
TWOROI   CLE                   ! FOR INCREMENT
         POMD R40,-R12         ! GET B
         POMD R50,-R12         ! GET A WHILE ARP = 12
         CMB  R54,=377         ! IS A REAL?
         JNC  CASE34           ! JIF YES
         CMB  R44,=377         ! ARE BOTH INTEGERS?
         JNC  CASE2            ! JIF NO, CASE 2
         ICE                   ! FLAG INTEGERS
         RTN                   ! DONE, CASE 1 IS EASY
!
CASE2    LDM  R60,R50          !
         JSB  =INTORL          ! CONVERT A
         STM  R60,R50          !
         CLE                   ! FLAG REALS
         RTN                   ! DONE
!
CASE34   CMB  R44,=377         ! IS B INTEGER?
         JNC  TWORTN           ! JIF CASE 4, DONE
! CASE 3 - B IS INTEGER, SO CONVERT IT
         LDM  R60,R40          ! GET B TO 60 FOR INTORL
         JSB  =INTORL          ! CONVERT B
         STM  R60,R40          !
         CLE                   ! FLAG REALS
TWORTN   RTN                   ! DONE
!
! ********************************************************************
! CONVERT A TAGGED INTEGER TO A REAL #
INTORL   BCD                   ! CONVERT A TAGGED INTEGER TO A REAL #
         CLM  R36              ! EXP/SIGN
         STM  R36,R62          ! CLEAR CRAP
         CLB  R64              ! MORE CRAP
         TSB  R67              !
         JPS  INTOR1           ! JIF MANT POS
         TCM  R65              ! COMPL
         LDB  R37,=9C          ! SET SIGN NEG
INTOR1   TSM  R65              !
         JZR  INTORX           ! JIF ZERO
         LDB  R36,=5C          ! EXP
INTOR2   TSB  R67              !
         JLN  INTORX           ! JIF NORMALIZED
         LLM  R65              ! SHIFT
         DCB  R36              ! DEC EXP
         JMP  INTOR2           ! LOOP
!
INTORX   STM  R36,R60          ! SIGN/EXP
         RTN                   !
!
! ********************************************************************
! ********************************************************************
! FUNCTION CALL RUNTIME
! ********************************************************************
! ********************************************************************
         BYT  6                ! ATTRIBUTES
FNCAL.   BIN                   ! MAKE THAT ADD WORK!
         POMD R34,+R10         ! GET ADDRESS OF DEF IN V
         ADMD R34,=FWCURR      ! MAKE IT ABSOLUTE
         ICM  R34              ! SKIP NAME
         ICM  R34              !
         POMD R24,+R34         ! DEF ADDR
!
! NOW R34 POINTS TO TABLE ENTRY FOR THE DEF AND R24 POINTS TO THE DEF ITSELF
!
         ADMD R24,=FWCURR      ! MAKE IT ABS
         LDMD R46,R34          ! RTN ADDR
         JZR  CALOK            ! NOT RECURSIVE CALL
         CLM  R46              ! CRASH CURRENT RETURN
         PUMD R46,+R34         ! OK NEXT TIME
!
ER42     JSB  =ERROR+          !
         BYT  42D              ! RECURSIVE FN CALL
!
CALOK    POBD R32,+R24         ! # PARAMS IN DEF
         LRB  R32              !
         PUMD R24,+R6          ! FOR PCR
         PUMD R34,+R6          ! SAVE RTN ADDR SLOT
         POBD R34,+R10         ! # PARAMS IN CALL
         CMB  R34,R32          !
         JNZ  BADP             ! PARAM MISMATCH
         TSB  R34              !
POPPAR   JZR  LINKOK           !
         PUBD R#,+R6           ! SAVE PAR COUNT
         POBD R33,+R24         ! DEF PAR TYPE
         POBD R32,+R10         ! CALL PAR TYPE
         ERB  R32              ! STR FLAG TO CARRY
         ERB  R32              ! STR FLAG UPPER
         ANM  R32,=200,200     ! ISOLATE TYPE
         CMB  R32,R33          !
         JNZ  BADP1            ! PARAM MISMATCH
         POBD R77,+R24         ! THROW AWAY NAME
         TSB  R32              !
         JNZ  STRPR.           ! JIF STRING
         JSB  =ONER            ! GET VALUE TO BE PASSED
         BIN                   ! BACK TO BIN
         PUMD R40,+R24         ! STORE IT
TSTMO    POBD R34,-R6          ! RESTORE PAR COUNT
         DCB  R34              ! COUNT DOWN
         JMP  POPPAR           ! TEST FOR 0 IN LOOP
!
! STRING PARAMETERS - USE STOST ROUTINE
!
STRPR.   LDM  R32,R24          ! DEST STR
         SBMD R32,=FWCURR      ! REL
         DCM  R32              ! POINT TO NAME
         DCM  R32              !
         PUMD R24,+R6          ! SAVE 24
         JSB  =SSTR            !
         POMD R24,-R6          ! RESTORE R24
         POMD R42,+R24         ! GET LENGTH OF STRING
         ADM  R24,R42          ! SKIP THE STRING
         JMP  TSTMO            ! GET NEXT PARAMETER
!
LINKOK   LDMD R32,=FWCURR      !
         POMD R34,-R6          ! RTN ADDR SLOT
         PUMD R10,+R34         ! SAVE RETURN ADDR
         LDMD R66,=PCR         !
         PUMD R66,+R34         ! SAVE PCR
         LDMD R66,=TOS         !
         PUMD R66,+R34         ! SAVE TOS
         LDMD R66,X32,P.RMEM   ! RESERVED MEMORY
         PUMD R66,+R34         ! SAVE MEM
         CLM  R66              !
         STMD R66,X32,P.RMEM   ! LOOK LIKE NONE
         PUBD R16,+R34         ! SAVE CSTAT
LINK1    LDM  R10,R24          ! DO JSB TO FN STATEMENT
         POMD R24,-R6          !
         SBM  R24,=11,0        ! !!A CHANGE!!
!        SBM  R24,=10,0        ! RHIS WAS VERSION P1
!
! IF WE WANT TO REPORT THIS TRACE, WE MUST DO IT HERE, SINCE THE 16 IS BYPASSED
!
         STMD R24,=PCR         !
         RTN                   ! DONE
!
BADP1    POBD R74,-R6          !
BADP     POMD R74,-R6          ! RESTORE R6
!
ER40     JSB  =ERROR+          !
         BYT  40D              ! PARAM MISMATCH
!
SSTR     POMD R44,-R12         ! LEN / ADDR
         PUMD R32,+R12         ! STR BASE ADDR
         POMD R52,+R24         ! TOT MAX ACT LEN
         LDM  R56,R54          ! MAX LEN
         PUMD R56,+R12         !
         PUMD R24,+R12         ! ADDR
         PUMD R44,+R12         ! SOURCE LEN ADDR
         JSB  =STOST           !
         RTN                   !
!
! ********************************************************************
! FN RETURN
! ********************************************************************
         BYT  16               ! ATTRIBUTES
FNRET.   BIN                   ! LET FN(;;=)
         CMMD R12,=TOS         ! FN RESULT ON STAK?
         JZR  FNRTN.           ! JIF NO
         JSB  =FNGET           ! SINGLE LINE FN RETURN
         JMP  DORTN            !
!
FNGET    BIN                   !
         POMD R24,+R10         ! DEF VRBL ADDR
         ADMD R24,=FWCURR      ! MAKE IT ABS
         POMD R34,+R24         ! NAME
         POMD R32,+R24         ! ADDR
         LDMD R32,R24          ! RA
         CLM  R36              !
         PUMD R36,+R24         ! ZERO RA
         LDMD R36,=FWCURR      !
         TSM  R32              ! RETURN ADDRESS = 0?
         JZR  BADFN            ! JIF YES - BAD CALL
         POMD R30,+R24         ! GET PCR
         POMD R66,+R24         ! TOS
         STMD R66,=TOS         ! RESTORE IT
         POMD R66,+R24         ! P.RMEM
         STMD R66,X36,P.RMEM   ! RESTORE P.RMEM
         POBD R16,+R24         ! GET CSTAT
         RTN                   !
!
! ********************************************************************
! FN END
! ********************************************************************
         BYT  313              ! ATTRIBUTES
FNRTN.   JSB  =FNGET           ! FNEND RETURN
         ANM  R34,=200,0       ! ISOLATE STR FLAG
         JNZ  STRV             ! JIF STRING
         POMD R60,+R24         ! NUMERIC VALUE
         JSB  =FETIND          ! DO UNDEFINED TEST
         PUMD R60,+R12         ! PUSH VALUE
         JMP  DORTN            !
!
STRV     POMD R52,+R24         ! TOT,MAX,ACT LEN
         LDM  R34,R24          ! FOR STRIND
         JSB  =STRIND          ! CHECK UNDEF AND PUSH R1
DORTN    JSB  =FNDRTN          ! GO SET UP RETURN
         RTN                   ! *DORTN DOES SETTR1*
!
BADFN    DCM  R6               !
         DCM  R6               ! TRASH RETURN
!
         JSB  =ERROR+          !
         BYT  39D              ! ILLEGAL FN CALL
!
! ********************************************************************
! FN LET
! ********************************************************************
         NCM  R#               ! ATTRIBUTES
FNLET.   BIN                   ! LET FN
         POBD R24,+R10         ! STEP OVER 1 OR 3 TOKEN
         POMD R24,+R10         ! DEF VRBL ADDR
         ADMD R24,=FWCURR      ! MAKE IT ABS
         POMD R32,+R24         ! NAME
         ADM  R24,=11,0        ! ADDR,RTN,TOS,MEM,+1 BYTE
         TSB  R32              !
         JPS  NTSTR            ! JIF NOT STR
         SBMD R24,=FWCURR      !
         PUMD R24,+R12         ! ADDR TO STAK
         PUMD R24,+R12         !   AND AGAIN
         CLE                   !
         DCE                   !
!
! THIS WORKS BECAUSE R12 POINTS AT CSTAT AND IT CAN NEVER LOOK LIKE A REMOTE NAME
!
         JSB  =FETST           !
         RTN                   !
!
NTSTR    POMD R34,+R24         ! SKIP 2
         PUMD R24,+R12         ! STORE ADDR TO STAK
         PUMD R32,+R12         ! NAME FORM TO STAK
         RTN                   !
!
! ********************************************************************
! INPUT
! ********************************************************************
QMARK    BYT  77               ! ASCII ?
! ********************************************************************
         BYT  241              ! ATTRIBUTES
INPUT.   BIN                   ! FOR COMPARES
         CMB  R16,=2           ! RUN?
         JNZ  INPER            ! INPUT ILLEGAL IN RUN
         STMD R10,=INPR10      ! SAVE R10
         STMD R12,=INPTOS      ! SAVE STACK FOR ERRORS
         LDBD R3,=CRTWRS       ! SET UP FLAG
         JZR  INALFA           !
         LDB  R32,=77          ! SPIT OUT QMARK IN GRAPH
         JSB  =INGRAF          !
         JMP  SETR22           !
!
INALFA   JSB  =COPSUB          ! CIF SCTEMP=1 OR 2
         JZR  INALF1           ! JIF NO
         LDBI R#,=P.PTR        ! BUFFER PTR
         JNZ  INALF2           ! JIF BUFFER NOT EMPTY
INALF1   JSB  =DISP.           ! SET UP THINGS
INALF2   CLM  R54              !
         ICM  R54              ! PUSH 1 FOR STRING LENGTH
         LDM  R26,=QMARK       ! GET ADDRESS OF ?
         JSB  =TRAFIC          ! APPEND TO BUFFER
         JSB  =PRLINE          ! PRINT IT
SETR22   LDM  R22,=INPBUF      ! USE INPBUF FOR INPUT
         STMD R22,=INPTR       ! BUFFER
!
! SET CALVRB SO WE CAN TRACK CALC MODE VARIABLES LATER
!
         LDB  R16,=4           ! SET IDLE IN INPUT
         JSB  =SET240          !
         RTN                   !
!
INPER    JSB  =ERROR+          !
         BYT  88D              ! BAD STMT
!
! ********************************************************************
! INPUT STRING
! ********************************************************************
         BYT  33               ! ATTRIBUTES
INPU$.   BIN                   ! INPUT STRING
         STMD R12,=STSIZE      ! FOR PARSE
         STMD R12,=TOS         !
         STMD R10,=INPR10      ! SAVE R10
         LDM  R10,=INCOM$      ! COMPLETION ADDR
         STMD R10,=INPCOM      !
         LDMD R10,=INPTR       ! SET UP FOR PARSE
         JSB  =GCHAR           ! FIRST NON-BLANK
!
! This is a crucial GCHAR because it must skip leading blanks in case of
! unquoted string.  To preserve the skipping, need to save R10 in INPTR,
! but THIS occurrence of INPTR will be one byte off.  So that is ALWAYS one
! byte off, must check for CR first.
!
         CMB  R20,=15          ! CR HERE, SO NO DCM LATER?
         JZR  INPNUL           ! JIF YES, STORE INPUTR LATER
         STMD R10,=INPTR       ! STORE R10+1
!
! THE NEXT 5 LINES ACOID A SCAN WHEN INPUT IS OBVIOUSLY NOT A STRING EXPRESSION
!
         CMB  R20,=42          ! QUOTED STRING?
         JZR  YESSTR           ! JIF YES, STREXP
         STB  R20,R21          ! SAVE FOR UNSHIFTED
         JSB  =ALFA            ! ALPHABETIC?
         JEZ  NOTSTR           ! JIF NO
         LDB  R20,R21          ! RESTORE UNSHIFTED CHAR
YESSTR   JSB  =STREX+          ! STR EXPR?
         JEN  INPCO            ! JIF FOUND STR EXP
NOTSTR   LDMD R10,=INPTR       ! AND INPTR
         DCM  R10              ! CR WAS NOT POSSIBLE!
INPNUL   LDMD R12,=TOS         ! AND R12
         LDB  R14,=42          ! LOOK LIKE QUOTED STRING
         JSB  =UNQUOT          ! UNQUOTE STR TO , OR CR
         JMP  INPCO            ! NOW EXIT
!
INCOM$   BIN                   !
         POMD R44,-R12         ! STR POINTERS
         CMM  R46,R12          !
         JCY  INCM$1           ! JIF STR NOT WITHIN STAK
         LDM  R56,R44          ! STR LEN
         JSB  =RSMEM-          !
         LDM  R22,R56          ! BYTES TO MOVE
         LDM  R24,R46          ! FWA SOURCE
         STM  R26,R46          ! NEW STR ADDR
         JSB  =MOVUP           ! GO MOVE THE STR
INCM$1   LDMD R12,=STSIZE      ! RESET R12
         POMD R54,-R12         ! DEST STR
         PUMD R54,+R12         ! PUSH IT BACK
         LDM  R56,R46          ! ADDRESSES =
         CMM  R54,R44          ! DEST SIZE >= ?
         JNC  ER56             ! JIF STR ERROR
         PUMD R44,+R12         ! PUSH SOURCE STR POINTER
         JMP  INCML            ! DO COMMON COMPLETION
!
! ********************************************************************
! INPUT NUMERIC
! GETS ONE NUMERIC VALUE AND PUTS ON STACK (DOES NOT STORE!)
! ********************************************************************
         BYT  33               ! ATTRIBUTES
INPUN.   BIN                   ! GCHAR NEEDS BINARY
         STMD R12,=STSIZE      ! FOR PARSER
         STMD R10,=INPR10      ! SAVE R10
         LDM  R10,=INVOM.      ! COMPLETION ADDR
         STMD R10,=INPCOM      ! SAVE COMPLETION
         LDMD R10,=INPTR       ! SET UP FOR PARSE
         JSB  =GCHAR           !
         JSB  =NUMVA+          ! PARSE NUM VALUE
         JEZ  ER43             ! JIF NUMVAL NOT FOUND
         CMB  R14,=15          ! ONLY CR AND COMMA ARE
         JZR  INPCO            !   VALID HERE, MUST FLAG
         CMB  R14,=54          !   STRING LIKE "YES" AS
         JNZ  ER43             !   NON-NUMERIC (Y IS VRB
INPCO    LDB  R34,=16          !
         PUBD R34,+R12         ! PUSH EOL
         CMB  R20,=15          ! CR?
         JZR  INPN1.           ! JIF CR
         LDMI R36,=INPR10      !
         DRP  R37              ! EXPECTING MORE
         JSB  =TSTEND          !
         JEZ  ER45             ! JIF NO
         CMB  R14,=54          ! COMMA?
         JNZ  ER44             ! JIF NO
         DCM  R10              ! DCM FOR NEXT PASS
INPN1.   STMD R10,=INPTR       ! FOR NEXT TIME
         LDB  R16,=5           ! SET EXECUTING IN INPUT
         JSB  =SET240          ! FORCE EXIT
         RTN                   !
!
INVOM.   POMD R40,-R12         ! GET #
         LDMD R12,=STSIZE      ! RESTORE R12
         PUMD R40,+R12         ! PUSH #
INCML    LDMD R10,=INPR10      ! RESTORE R10
! NOW WE CLEAN UP IN CASE IN FOR/NEXT
         JSB  =RELMEM          !
         LDMD R34,=CALVRB      ! TRASH CALC VARB
         STMD R34,=LAVAIL      !
         LDB  R15,=2           ! INPUT COMPLETE
         ORB  R17,R15          !
         JSB  =SET240          ! RETURN TO EXEC
         RTN                   !
!
ER56     JSB  =ERROR           !
         BYT  56D              ! STRING OVERFLOW
!
         JMP  BADA..           !
!
ER43     JSB  =ERROR           !
         BYT  43D              ! NUMERIC INPUT
!
         JMP  BADA++           !
!
ER44     JSB  =ERROR           !
         BYT  44D              ! TOO FEW INPUTS
!
         JMP  BADA++           !
!
ER45     JSB  =ERROR           !
         BYT  45D              ! TOO MANY INPUTS
!
BADA++   LDMD R34,=ERGOTO      ! ON ERROR?
         JZR  BADA..           ! JIF NO
         DCM  R6               ! TRASH 1 RETURN
         DCM  R6               !
BADA..   LDMD R10,=PCR         ! RESET PC
         BIN                   ! ADD NEEDS BINARY
         ADM  R10,=3,0         ! SKIP OVER L.N., LENGTH
         LDMD R12,=INPTOS      ! RESET TOP OF STACK
         JSB  =RELMEM          ! RELEASE TEMP MEMORY
         JSB  =REPORT          ! REPORT IT
         RTN                   ! DONE
!
! ********************************************************************
! PRINT ARRAY
! ********************************************************************
         BYT  36               ! ATTRIBUTES
P#ARAY   BIN                   ! PRINT AN ARRAY TO A DATA FILE
         POMD R44,-R12         ! R44=ADDR; R46=NAME
         POMD R52,+R44         ! POP ARRAY LEN,ROW,COL
         PUMD R44,+R6          ! SAVE ADDR,NAME
         LDM  R34,R44          ! 1ST ELEM ADDRESS
         JSB  =LENCAL          ! CALC DATA LENGTH
         PUMD R36,+R6          ! SAVE DATA LENGTH
         LDM  R36,R52          ! MOVE ARRAY LEN
         PUMD R36,+R6          ! SAVE IT
NXTELP   JSB  =FNUM            ! FETCH NUMBER (R60)
         LDM  R40,R60          ! FOR PRNT#N
         JSB  =PRNT#N          !
         POMD R40,-R6          !
         STM  R40,R30          !
         CMB  R17,=300         ! ERRORS?
         JCY  EXITPA           ! JIF YES, EXIT PRINT ARRAY
         SBM  R46,R44          ! COUNT DOWN LENGTH
         JZR  EXITPA           !
         ADM  R30,R44          ! NEXT ADDRESS
         STM  R30,R34          ! ADDRESS IN R34 FOR FNUM
         STM  R30,R40          ! FOR NEXT LOOP
         PUMD R40,+R6          ! ADDR,NAME,DLEN,ARAYLEN
         LDM  R46,R42          ! MOVE NAME FOR FNUM
         JMP  NXTELP           !
!
EXITPA   RTN                   !
!
         BSZ  34               ! END OF CODE IN ROM (ZEROED OUT)
!
         BYT  213,101,64,307   ! ROM CHECKSUMS
         FIN
