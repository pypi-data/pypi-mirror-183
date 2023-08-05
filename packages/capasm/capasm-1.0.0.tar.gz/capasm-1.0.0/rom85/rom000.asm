         ABS 60000
! *******************************************************************
! *******************************************************************
! *******************************************************************
! *******************************************************************
R60K     BYT  0                ! ROM#: 0
         BYT  377              ! one's complement of ROM #
         DEF  BTAB.R           ! RUNTIME TABLE
         DEF  ASCIIS           ! ASCII TABLE
         DEF  BASICS           ! PARSE TABLE
         DEF  ERMSG            ! ERROR MESSAGES
         DEF  R0INIT           ! INITIALIZATION
R0INIT   RTN                   !
!
! *******************************************************************
! RUNTIME TABLE
! *******************************************************************
!        ROUTINE                 NAME               TOKEN  ATTRIBUTEs
!        ============            ================== =====  ==========
BTAB.R   DEF  ERRORX           ! ERROR                 0   0,44
         DEF  FTSVL            ! SNV                   1   0,1
         DEF  SVADR            ! SAV                   2   0,1
         DEF  FTSTL            ! STRVAR                3   0,1
         DEF  ICONST           ! REAL CONST            4   0,4
         DEF  SCONST           ! "QUOTED STRING"       5   0,5
         DEF  SCONST           ! UNQUOTED STRING       6   0,5
         DEF  STOST            ! STO. STRING           7   0,31
         DEF  STOSV            ! STORE SV             10   0,31
         DEF  AVADR1           ! 1-DIM ADR (STO ARY)  11   0,32
         DEF  AVADR2           ! 2-DIM ADR (STO ARY)  12   0,32
         DEF  AVVAL1           ! 1-DIM VAL (FET ARY)  13   0,32
         DEF  AVVAL2           ! 2-DIM VAL (FET ARY)  14   0,32
         DEF  ERRORX           ! CARRIAGE RTN         15   0,44
         DEF  GORTN            ! END STMT             16   0,0
         DEF  ERRORX           ! DUMMY                17   0,44
         DEF  ERRORX           ! DUMMY                20   0,44
         DEF  FTADR            ! SNV ADR              21   0,3
         DEF  SVADR+           ! SAV ADR              22   0,3
         DEF  FTSTLS           ! SAVE STRING          23   0,3
         DEF  STOSVM           ! MULTI-STO.           24   0,43
         DEF  STOSTM           ! MULTI-STO$           25   0,43
         DEF  FNCAL.           ! NUM FUNC CALL        26   0,6
         DEF  FNCAL.           ! STR FUNC CALL        27   0,6
         DEF  JTRUE#           ! JUMP TRUE            30   0,7
         DEF  ERRORE           ! ILLEGAL END          31   0,44
         DEF  INTCON           ! INT CONST            32   0,2
         DEF  JFALSR           ! JMP FALSE            33   0,11
         DEF  JMPREL           ! JMP REL              34   0,26
         DEF  SUBST1           ! 1-DIM SUB-STR        35   0,34
         DEF  SUBST2           ! 2-DIM SUB-STR        36   0,34
         DEF  EJMP#            ! ELSE J#              37   0,25
         DEF  ERRORX           ! DUMMY                40   0,44
         DEF  ERRORX           ! DUMMY                41   0,44
         DEF  P#ARAY           ! ARRAY PRINT#         42   0,36
         DEF  ERRORX           ! DUMMY                43   0,44
         DEF  R#ARAY           ! ARRAY READ#          44   0,44
         DEF  ERRORX           ! :                    45   0,44
         DEF  CONCA.           ! & CONCAT             46   10,53
         DEF  NOP47.           ! ;                    47   0,42
         DEF  ERRORX           ! (                    50   0,44
         DEF  ERRORX           ! )                    51   0,44
         DEF  MPYROI           ! *                    52   11,51
         DEF  ADDROI           ! +                    53   7,51
         DEF  ERRORX           ! ,                    54   0,44
         DEF  SUBROI           ! - DIADIC             55   7,51
         DEF  ERRORX           ! .                    56   0,44
         DEF  DIV2             ! /                    57   11,51
         DEF  YTX5             ! ^                    60   14,51
         DEF  UNEQ$.           ! #                    61   6,53
         DEF  LEQ$.            ! <=                   62   6,53
         DEF  GEQ$.            ! >=                   63   6,53
         DEF  UNEQ$.           ! <>                   64   6,53
         DEF  EQ$.             ! =                    65   6,53
         DEF  GR$.             ! >                    66   6,53
         DEF  LT$.             ! <                    67   6,53
         DEF  CHSROI           ! - MONADIC            70   10,50
         DEF  UNEQ.            ! #                    71   6,51
         DEF  LEQ.             ! <=                   72   6,51
         DEF  GEQ.             ! >=                   73   6,51
         DEF  UNEQ.            ! <>                   74   6,51
         DEF  EQ.              ! =                    75   6,51
         DEF  GR.              ! >                    76   6,51
         DEF  LT.              ! <                    77   6,51
         DEF  ATSIGN           ! @                   100   0,42
         DEF  ONERR.           ! ON ERROR            101   0,241
         DEF  OFFER.           ! OFF ERROR           102   0,241
         DEF  ONKEY.           ! ON KEY#             103   0,241
         DEF  OFKEY.           ! OFF KEY#            104   0,241
         DEF  AUTO.            ! AUTO                105   0,141
         DEF  BEEP.            ! BEEP                106   0,241
         DEF  CLEAR.           ! CLEAR               107   0,241
         DEF  CONTI.           ! CONT                110   0,141
         DEF  ONTIM.           ! ON TIMER#           111   0,241
         DEF  INIT.            ! INIT                112   0,141
         DEF  LIST.            ! LIST                113   0,241
         DEF  BPLOT.           ! BPLOT               114   0,241
         DEF  STIME.           ! SETTIME             115   0,241
         DEF  CHAIN.           ! CHAIN               116   0,241
         DEF  SECUR.           ! SECURE              117   0,241
         DEF  PRNT#.           ! READ#               120   0,241
         DEF  RENAM.           ! RENAME              121   0,241
         DEF  ALPHA.           ! ALPHA               122   0,241
         DEF  CRT.             ! CRT IS              123   0,241
         DEF  RUN.             ! RUN                 124   0,141
         DEF  DEG.             ! DEG                 125   0,241
         DEF  DISP.            ! DISP                126   0,241
         DEF  GCLR.            ! GCLEAR              127   0,241
         DEF  SCRAT.           ! SCRATCH             130   0,141
         DEF  DEFA+.           ! DEFAULT ON          131   0,241
         DEF  JMPLN#           ! GOTO                132   0,210
         DEF  JMPSUB           ! GOSUB               133   0,210
         DEF  PRNT#.           ! PRINT #             134   0,241
         DEF  GRAD.            ! GRAD                135   0,241
         DEF  GRAPH.           ! GRAPH               136   0,241
         DEF  INPUT.           ! INPUT               137   0,241
         DEF  IDRAW.           ! IDRAW               140   0,241
         DEF  FNLET.           ! LET FN              141   0,217
         DEF  NOP.             ! LET                 142   0,241
         DEF  PRALL.           ! PRINT ALL           143   0,241
         DEF  CAT.             ! CAT                 144   0,241
         DEF  DRAW.            ! DRAW                145   0,241
         DEF  ON.              ! ON                  146   0,230
         DEF  LABEL.           ! LABEL               147   0,241
         DEF  WAIT.            ! WAIT                150   0,241
         DEF  PLOT.            ! PLOT                151   0,241
         DEF  PRINS.           ! PRINTER IS          152   0,241
         DEF  PRINT.           ! PRINT               153   0,241
         DEF  RAD.             ! RAD                 154   0,241
         DEF  RNDIZ.           ! RANDOMIZE           155   0,241
         DEF  READ.            ! READ                156   0,241
         DEF  STORB.           ! STORE BIN           157   0,241
         DEF  RESTO.           ! RESTORE             160   0,241
         DEF  RETRN.           ! RETURN              161   0,241
         DEF  OFTIM.           ! OFF TIMER#          162   0,241
         DEF  MOVE.            ! MOVE                163   0,241
         DEF  FLIP.            ! FLIP                164   0,241
         DEF  STOP.            ! STOP                165   0,241
         DEF  STORE.           ! STORE               166   0,141
         DEF  PENUP.           ! PENUP               167   0,241
         DEF  TRCVB.           ! TRACE VRBL          170   0,241
         DEF  TRCAL.           ! TRACE ALL           171   0,241
         DEF  XAXIS.           ! XAXIS               172   0,241
         DEF  YAXIS.           ! YAXIS               173   0,241
         DEF  COPY.            ! COPY                174   0,241
         DEF  NORMA.           ! NORMAL              175   0,241
         DEF  ERAST            ! ERASE TAPE          176   0,241
         DEF  SKIPI            ! INTEGER             177   0,323
         DEF  SKIPS            ! SHORT               200   0,322
         DEF  DELET.           ! DELETE              201   0,141
         DEF  SCALE.           ! SCALE               202   0,241
         DEF  SKIP!            ! REMARK              203   0,241
         DEF  OPTIO.           ! OPTION BASE         204   0,315
         DEF  SKIPC            ! COM                 205   0,324
         DEF  SKIPEM           ! DATA                206   0,320
         DEF  SKPDEF           ! DEF FN              207   0,312
         DEF  SKIPD            ! DIM                 210   0,321
         DEF  KEYLA.           ! KEY LABEL           211   0,241
         DEF  STOP.            ! END                 212   0,241
         DEF  FNRTN.           ! FN END              213   0,313
         DEF  FOR.             ! FOR                 214   0,341
         DEF  ERRORT           ! IF                  215   0,344
         DEF  SKIPIT           ! IMAGE               216   0,341
         DEF  NEXT.            ! NEXT                217   0,341
         DEF  UNSEC.           ! UNSECURE            220   0,141
         DEF  ERRORT           ! LET (IMPLY)         221   0,244
         DEF  ASIGN.           ! ASSIGN              222   0,241
         DEF  CREAT.           ! CREATE              223   0,241
         DEF  PURGE.           ! PURGE               224   0,241
         DEF  REWIN.           ! REWIND              225   0,241
         DEF  LOADB.           ! LOADBIN             226   0,241
         DEF  PAUSE.           ! PAUSE               227   0,241
         DEF  LOAD.            ! LOAD                230   0,141
         DEF  SKIPR            ! REAL                231   0,321
         DEF  RENUM.           ! REN                 232   0,141
         DEF  SKIP!            ! !                   233   0,241
         DEF  DEFA-.           ! DEFAULT OFF         234   0,241
         DEF  PEN.             ! PEN                 235   0,241
         DEF  PLIST.           ! PLIST               236   0,241
         DEF  LDIR.            ! LDIR                237   0,241
         DEF  IMOVE.           ! IMOVE               240   0,241
         DEF  FNLET.           ! FN ILET             241   0,217
         DEF  CTAPE.           ! CTAPE               242   0,241
         DEF  TRACE.           ! TRACE               243   0,241
         DEF  TO.              ! TO                  244   0,41
         DEF  OR.              ! OR                  245   2,51
         DEF  MAX10            ! MAX                 246   40,55
         DEF  TIME.            ! TIME                247   0,55
         DEF  DATE.            ! DATE                250   0,55
         DEF  FP5              ! FP                  251   20,55
         DEF  IP5              ! IP                  252   20,55
         DEF  EPS10            ! EPSILON             253   0,55
         DEF  REM10            ! RMD                 254   40,55
         DEF  CEIL10           ! CEIL                255   20,55
         DEF  ATN2.            ! ATN(X/Y)            256   40,55
         DEF  ERRORX           ! DUMMY               257   0,44
         DEF  SQR5             ! SQR                 260   20,55
         DEF  MIN10            ! MIN                 261   40,55
         DEF  ERRORX           ! DUMMY               262   0,44
         DEF  ABS5             ! ABS                 263   20,55
         DEF  ICOS             ! ACS                 264   20,55
         DEF  ISIN             ! ASN                 265   20,55
         DEF  ITAN             ! ATN                 266   20,55
         DEF  SGN5             ! SGN                 267   20,55
         DEF  ERRORX           ! DUMMY               270   0,44
         DEF  COT10            ! COT                 271   20,55
         DEF  CSEC10           ! CSC                 272   20,55
         DEF  ERRORX           ! DUMMY               273   0,44
         DEF  EXP5             ! EXP                 274   20,55
         DEF  INT5             ! INT                 275   20,55
         DEF  LOGT5            ! LGT (10)            276   20,55
BASICS   DEF  LN5              ! LOT (E)             277   20,55
         DEF  ERRORX           ! DUMMY               300   0,44
         DEF  SEC10            ! SEC                 301   20,55
         DEF  CHR$.            ! CHR$                302   20,56
         DEF  VAL$.            ! VAL$                303   20,56
         DEF  LEN.             ! LEN                 304   30,55
         DEF  NUM.             ! NUM                 305   30,55
         DEF  VAL.             ! VAL                 306   30,55
         DEF  INF10            ! INF                 307   0,55
         DEF  RND10            ! RND                 310   0,55
         DEF  PI10             ! PI                  311   0,55
         DEF  UPC$.            ! UPC$                312   30,56
         DEF  USING.           ! USING               313   0,341
         DEF  ERRORX           ! THEN                314   0,44
         DEF  TAB.             ! TAB                 315   20,45
         DEF  STEP.            ! STEP                316   0,41
         DEF  EXOR.            ! EXOR                317   2,51
         DEF  NOT.             ! NOT                 320   10,50
         DEF  INTDIV           ! DIV (\)             321   11,51
         DEF  ERNUM.           ! ERRN                322   0,55
         DEF  ERRL.            ! ERRL                323   0,55
         DEF  RESET.           ! RESET               324   0,44
         DEF  AND.             ! AND                 325   4,51
         DEF  MOD10            ! MOD                 326   11,51
         DEF  ERRORX           ! ELSE                327   0,44
         DEF  SIN10            ! SIN                 330   20,55
         DEF  COS10            ! COS                 331   20,55
         DEF  TAN10            ! TAN                 332   20,55
         DEF  NOP2.            ! TO (ASSIGN)         333   77,51
         DEF  RSTO..           ! RESTORE LN          334   0,227
         DEF  ERRORX           ! DUMMY               335   0,44
         DEF  ERRORX           ! [                   336   0,44
         DEF  ERRORX           ! ]                   337   0,44
         DEF  INTDIV           ! \                   340   11,51
         DEF  POS.             ! POS                 341   52,55
         DEF  DEG10            ! RTD                 342   20,55
         DEF  RAD10            ! DTR                 343   20,55
         DEF  INT5             ! FLOOR               344   20,55
         DEF  ERRORX           ! DUMMY               345   0,44
         DEF  READN.           ! READ (NUM)          346   0,44
         DEF  ULIN#.           ! USING LINE #        347   0,327
         DEF  INPUN.           ! INP NUMERIC         350   0,33
         DEF  INPU$.           ! INP STRING          351   0,33
         DEF  FNRET.           ! LET FN(::=)         352   0,16
         DEF  READS.           ! READ$               353   0,44
         DEF  PRLINE           ! PRINT END           354   0,35
         DEF  SEMIC.           ! PRINT;              355   0,36
         DEF  COMMA.           ! PRINT,              356   0,36
         DEF  SEMIC$           ! PRINT;$             357   0,36
         DEF  COMMA$           ! PRINT,$             360   0,36
         DEF  ERRORX           ! DUMMY               361   0,241
         DEF  STEPK.           ! STEP KEY            362   0,241
         DEF  FTADR            ! 1-DIM ARRAY REF     363   0,1
         DEF  FTADR            ! 2-DIM ARRAY REF     364   0,1
         DEF  TEST.            ! TEST KEY            365   0,341
         DEF  ERRORX           ! DUMMY               366   0,44
         DEF  ERRORX           ! DUMMY               367   0,44
         DEF  ROM:GO           ! EXTERNAL ROM        370   0,214
         DEF  BP:GO            ! BINARY PROG         371   0,214
         DEF  ERRORX           ! DUMMY               372   0,44
         DEF  ERRORX           ! DUMMY               373   0,44
         DEF  ERRORX           ! DUMMY               374   0,44
         DEF  ERRORX           ! DUMMY               375   0,44
         DEF  ERRORX           ! DUMMY               376   0,44
         DEF  ERRORX           ! DUMMY               377   0,44
! *******************************************************************
! PARSE TABLE
! BASICS + 100, FIRST 100 NOT USED
! *******************************************************************
!                                TOKEN#  NAME
!                                ======  ====================
         DEF  ONERRO           !  101    ON ERROR
         DEF  PUSH1A           !  102    OFF ERROR
         DEF  ONKEY#           !  103    ON KEY#
         DEF  OFKEY#           !  104    OFF KEY#
         DEF  G012N            !  105    AUTO
         DEF  G0OR2N           !  106    BEEP
         DEF  PUSH1A           !  107    CLEAR
         DEF  G01N             !  110    CONT
         DEF  ONTIME           !  111    ON TIMER#
         DEF  PUSH1A           !  112    INIT
         DEF  G012N            !  113    LIST
         DEF  G$N              !  114    BPLOT
         DEF  GET2N            !  115    SETTIME
         DEF  GET1$            !  116    CHAIN
         DEF  SECURE           !  117    SECURE
         DEF  READ#            !  120    READ #
         DEF  RENAME           !  121    RENAME
         DEF  PUSH1A           !  122    ALPHA
         DEF  GET1N            !  123    CRT IS
         DEF  G01N             !  124    RUN
         DEF  PUSH1A           !  125    DEG
         DEF  PRINT            !  126    DISP
         DEF  TRY1N            !  127    GCLEAR
         DEF  PUSH1A           !  130    SCRATCH
         DEF  PUSH1A           !  131    DEFAULT ON
         DEF  GOTOSU           !  132    GOTO
         DEF  GOTOSU           !  133    GOSUB
         DEF  PRINT#           !  134    PRINT #
         DEF  PUSH1A           !  135    GRAD
         DEF  PUSH1A           !  136    GRAPH
         DEF  INPUT            !  137    INPUT
         DEF  GET2N            !  140    IDRAW
         DEF  FNLET            !  141    LET FN
         DEF  LET              !  142    LET
         DEF  PUSH1A           !  143    PRINT ALL
         DEF  PUSH1A           !  144    CAT
         DEF  GET2N            !  145    DRAW
         DEF  ON               !  146    ON
         DEF  GET1$            !  147    LABEL
         DEF  GET1N            !  150    WAIT
         DEF  GET2N            !  151    PLOT
         DEF  GET1N            !  152    PRINTER IS
         DEF  PRINT            !  153    PRINT
         DEF  PUSH1A           !  154    RAD
         DEF  TRY1N            !  155    RANDOMIZE
         DEF  READ             !  156    READ
         DEF  GET1$            !  157    STORE BIN
         DEF  RESTOR           !  160    RESTORE
         DEF  PUSH1A           !  161    RETURN
         DEF  GET1N            !  162    OFF TIMER#
         DEF  GET2N            !  163    MOVE
         DEF  PUSH1A           !  164    FLIP
         DEF  PUSH1A           !  165    STOP
         DEF  GET1$            !  166    STORE
         DEF  PUSH1A           !  167    PENUP
         DEF  TRCVB            !  170    TRACE VRBL
         DEF  PUSH1A           !  171    TRACE ALL
         DEF  G12OR4           !  172    XAXIS
         DEF  G12OR4           !  173    YAXIS
         DEF  PUSH1A           !  174    COPY
         DEF  PUSH1A           !  175    NORMAL
         DEF  PUSH1A           !  176    ERASE TAPE
         DEF  TYPSTM           !  177    INTEGER
         DEF  TYPSTM           !  200    SHORT
         DEF  G012N            !  201    DELETE
         DEF  GET4N            !  202    SCALE
         DEF  REM              !  203    REM
         DEF  OPTION           !  204    OPTION
         DEF  COM              !  205    COM
         DEF  DATA             !  206    DATA
         DEF  DEF              !  207    DEF FN
         DEF  DIM              !  210    DIM
         DEF  PUSH1A           !  211    KEY LABEL
         DEF  PUSH1A           !  212    END
         DEF  FNEND            !  213    FN END
         DEF  FOR              !  214    FOR
         DEF  IF               !  215    IF
         DEF  REM              !  216    IMAGE
         DEF  NEXT             !  217    NEXT
         DEF  SECURE           !  220    UNSECURE
         DEF  ILET             !  221    LET (IMPLY)
         DEF  ASSIGN           !  222    ASSIGN
         DEF  G$N+NN           !  223    CREATE
         DEF  GET$N?           !  224    PURGE
         DEF  PUSH1A           !  225    REWIND
         DEF  GET1$            !  226    LOADBIN
         DEF  PUSH1A           !  227    PAUSE
         DEF  GET1$            !  230    LOAD
         DEF  TYPSTM           !  231    REAL
         DEF  G012N            !  232    REN
         DEF  REM              !  233    !
         DEF  PUSH1A           !  234    DEFAULT OFF
         DEF  GET1N            !  235    PEN
         DEF  G012N            !  236    PLIST
         DEF  GET1N            !  237    LDIR
         DEF  GET2N            !  240    IMOVE
         DEF  FNLET            !  241    FN ILET
         DEF  PUSH1A           !  242    CTAPE
         DEF  PUSH1A           !  243    TRACE
!
! *******************************************************************
! RUNTIME ERROR ROUTINES
! *******************************************************************
         BYT  44               !
ERRORX   JSB  =ERROR+          !
         BYT  15D              ! BAD TOKEN
!
! *******************************************************************
! NOTE: They save a few bytes here, since the runtime code for ERRORT
! and ERRORE is the same, but the ATTRIBUTES are different, and the
! ATTRIBUTE byte for ERRORE is 044, which (as code) is an ARP 44
! instruction, which doesn't hurt anything, so ERRORT actually
! EXECUTES the attribute byte for ERRORE before falling into the
! common routine
! *******************************************************************
         BYT  344              ! ATTRIBUTE FOR ERRORT
ERRORT   BYT  44               ! ATTRIBUTE FOR ERRORE
ERRORE   JSB  =ERROR+          !
         BYT  48D              ! MISSING STOP OR END
!
! *******************************************************************
! RUNTIME FETCH, STORE, OPTION BASE
! *******************************************************************
         BYT  42               ! ATTRIBUTES
ATSIGN   STMD R12,=TOS         ! @ SIGN
         JSB  =RELMEM          !
         RTN                   !
!
! *******************************************************************
! NOTE - The following NOP's can be grouped
!   only if attributes are harmless when executed (ARPs and DRPs)
! *******************************************************************
         BYT  241              ! NOP ATTRIBUTES
NOP.     BYT  41               ! LET keyword entry point and NOP47. ATTRIBUTES
NOP47.   BYT  1,51             ! SEMI-COLON (;) entry point and NOP2. ATTRIBUTES
NOP2.    RTN                   ! TO (ASSIGN)
!
! *******************************************************************
! *******************************************************************
         BYT  4                ! ATTRIBUTES
ICONST   POMD R70,+R10         ! FETCH CONSTANT
         PUMD R70,+R12         ! PUSH ONTO STACK
         RTN                   !
!
! *******************************************************************
! *******************************************************************
         BYT  2                ! ATTRIBUTES
INTCON   POMD R75,+R10         ! FETCH BINARY CONST
I#PUSH   LDB  R74,=377         ! PUSH MARKER
         PUMD R70,+R12         ! TO STACK
         RTN                   ! DONE
!
! *******************************************************************
! *******************************************************************
         BYT  3                ! ATTRIBUTES
SVADR+   JMP  SVADR            !
!
! *******************************************************************
! *******************************************************************
         BYT  1                ! ATTRIBUTES
SVADR    POMD R24,+R10         ! POP ADDR
         PUMD R24,+R12         ! AND PUSH ON OPER STAK
         RTN                   !
!
! *******************************************************************
! *******************************************************************
         BYT  1                ! ATTRIBUTES - Fetch Simple numeric Variable
FTSVL    POMD R66,+R10         ! POP ADDRESS
         JSB  =FETSV           ! GO FETCH VARIABLE
SVVAL3   PUMD R60,+R12         ! PUSH THE VALUE
         RTN                   !
! *******************************************************************
         BYT  3                ! ATTRIBUTES
FTSTLS   CLE                   ! SAVE STR
         DCE                   !
         JMP  FTST1            !
!
! *******************************************************************
! *******************************************************************
         BYT  1                ! ATTRIBUTES
FTSTL    CLE                   ! STRVAR
FTST1    POMD R24,+R10         ! POP ADDR
         PUMD R24,+R12         ! AND PUSH ON OPER STACK
         JEZ  FTST2            ! JIF STORE VARIABLE
         PUMD R24,+R12         !
FTST2    JSB  =FETST           ! GO FETCH VARIABLE
         RTN                   !
!
! *******************************************************************
! *******************************************************************
         BYT  315              ! ATTRIBUTES
OPTIO.   POMD R64,+R10         ! TRASH INTEGER TOKEN AND INTEGER
         RTN                   ! AND EXIT
!
! *******************************************************************
! USED BY ALLOCATOR
OPTIOX   LDMD R56,=FWCURR      ! FWA PRGM
         LDMD R36,=OPTBAS      !
         LRB  R36              !
         ERB  R36              !
         ERB  R36              !
         LDBD R37,X56,P.TYPE   !
         ANM  R37,=277         ! CLEAR OPTION BASE FLAG
         ORB  R37,R36          ! SET OPTION BASE
         STBD R37,X56,P.TYPE   ! RESTORE
         RTN                   !
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
DEFA+.   CLB  R36              ! DEFAULT ON - CLEAR FLAG
         ICB  R36              ! SET TO ON
         JMP  STORDF           ! STORE IT
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
DEFA-.   CLB  R36              ! DEFAULT OFF - CLEAR FLAG
STORDF   STBD R#,=DEFAUL       ! STORE 0 OR ONTOK
         RTN                   ! DONE
!
! *******************************************************************
! RUNTIME ARRAY FETCH, STORE
! *******************************************************************
         BYT  32               ! ATTRIBUTES
AVADR1   CLB  R20              ! 1-DIMADR - EXTRA ENTRY POINT
         ICB  R20              !
         JMP  PU20             !
!
! *******************************************************************
! *******************************************************************
         BYT  32               !
AVADR2   CLB  R20              ! 2-DIM ADR - GET TOKEN IN 20
PU20     PUBD R#,+R12          !   AND PUSH ON STACK
         JSB  =FETAVA          ! GET ADDRESS
         PUMD R34,+R12         ! PUSH ADDR
         LDB  R74,R47          !
         LLB  R74              ! TRACE?
         TSB  R74              !
         JPS  PNAM             ! JIF NO
         LDM  R73,R40          ! ROW/COL
         PUMD R73,+R12         ! AND PUSH
PNAM     PUMD R46,+R12         ! PUSH NAME FORM
         RTN                   !
!
! *******************************************************************
! *******************************************************************
         BYT  32               ! ATTRIBUTES
AVVAL1   CLB  R20              ! 1-DIM VALUE - EXTRA ENTRY POINT
         ICB  R20              !
         JMP  PU20+            !
!
! *******************************************************************
! *******************************************************************
         BYT  32               ! ATTRIBUTES
AVVAL2   CLB  R20              ! 2-DIM VALUE - GET TOKEN IN 20
PU20+    PUBD R#,+R12          !   AND PUSH ON STACK
         JSB  =FETAV           ! GET VALUE
         PUMD R60,+R12         ! GO PUSH
         RTN                   ! DONE
! *******************************************************************
         BYT  3                ! ATTRIBUTES
FTADR    POMD R66,+R10         ! POP ADDR
         BIN                   !
         JSB  =FETSVA          ! GO FETCH VAR ADDR
FTAPU    PUMD R34,+R12         !
         PUMD R46,+R12         ! NAME
         RTN                   !
!
! *******************************************************************
! RUNTIME STRING, SUBSTRING
! *******************************************************************
         BYT  5                ! ATTRIBUTES
SCONST   CLM  R36              ! QUOTED STRING
         POBD R36,+R10         ! POP LENGTH
         PUMD R36,+R12         ! PUSH LENGTH
         PUMD R10,+R12         ! PUSH ADDR
         BIN                   !
         ADM  R10,R36          ! STEP 10 PAST CONST
SCORTN   RTN                   ! THATS ALL, FOLKS!
!
! *******************************************************************
! *******************************************************************
         BYT  34               ! ATTRIBUTES -  2 DIM SUBST
SUBST2   JSB  =TWOB            ! SUB1 TO 46, SUB2 TO 56
SUBS2+   CLE                   ! CLEAR ERROR FLAG
         STM  R46,R76          ! SAVE SUB2
         LDM  R46,R56          ! SUB1 TO 46
         POMD R56,-R12         ! OLD PTR
         POMD R66,-R12         ! LD COUNT
         CMM  R66,R76          ! OLD COUNT-SUB2
         JPS  STPTR            ! JIF NO OVERFLOW
         STM  R66,R76          ! SUB2 = OLD COUNT
         ICE                   ! SET ERROR
         JMP  STPTR            !
!
! *******************************************************************
! *******************************************************************
         BYT  34               ! ATTRIBUTES - 1-DIM SUBST
SUBST1   JSB  =ONEB            ! FIRST BYTE
SUBS1+   CLE                   ! CLEAR ERROR FLAG
         POMD R56,-R12         ! LEN PTR
         POMD R76,-R12         !
STPTR    SBM  R76,R46          ! NEW LEN
         ICM  R76              ! BIASED BY 1
         JPS  STPTR1           ! JIF NO OVERFLOW
         CLM  R76              !
         ICE                   !
STPTR1   DCM  R46              !
         JPS  STPTR2           ! JIF START >= 1
         CLM  R46              ! START = 1
         ICE                   ! SET ERROR
STPTR2   STM  R76,R54          !
         ADM  R56,R46          ! NEW PTR
         PUMD R54,+R12         ! PUSH IT
         JEZ  SCORTN           ! JIF NO ERRORS
!
STRERR   JSB  =ERROR+          !
         BYT  56D              ! STRING OVERFLOW
!
! *******************************************************************
! RUNTIME MODE SET, REM, SKIP
! *******************************************************************
         BYT  241              ! ATTRIBUTES
DEG.     LDB  R36,=90C         ! DEGREE FLAG = 90
STODRG   STBD R#,=DRG          ! PUT INTO DRG FLAG
         RTN                   ! SIMPLE!
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
RAD.     CLB  R36              ! RADIAN FLAG = 0
         JMP  STODRG           ! STORE IT
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
GRAD.    CLB  R36              ! GRAD FLAG=99
         DCB  R36              ! MAKE IT 99
         JMP  STODRG           ! STORE IT
!
! *******************************************************************
! *******************************************************************
         BYT  323              ! ATTRIBUTES
SKIPI    JMP  SKIPIT           ! INTEGER
!
! *******************************************************************
! *******************************************************************
         BYT  321              ! ATTRIBUTES
SKIPR    JMP  SKIPIT           ! REAL
!
! *******************************************************************
! *******************************************************************
         BYT  322              ! ATTRIBUTES
SKIPS    JMP  SKIPIT           ! SHORT
!
! *******************************************************************
! *******************************************************************
         BYT  321              ! ATTRIBUTES
SKIPD    JMP  SKIPIT           ! DIM
!
! *******************************************************************
! *******************************************************************
         BYT  324              ! ATTRIBUTES
SKIPC    JMP  SKIPIT           ! COM
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
SKIP!    JMP  SKIPIT           ! REMARK
!
! *******************************************************************
! *******************************************************************
         BYT  320              ! ATTRIBUTES
SKIPEM   JMP  SKIPIT           ! DATA
! *******************************************************************
         BYT  341              ! ATTRIBUTES
SKIPIT   TSB  R16              ! CALC
         DRP  R12              ! SO WE DONT CONFUSE DISP
         JOD  SKIPT1           ! JIF CLAC
         LDMD R36,=PCR         ! GET LINENO AND
         JSB  =SKPLN           !
SKIPT1   STM  R#,R10           ! ADD TO PC
         GTO GORTN             ! SKIP ENTIRE LINE
!
SKPLN    BIN                   !
SKPLP    STM  R36,R32          ! CURRENT LINE #
         POMD R36,+R32         ! LINE #
         CLM  R36              ! FOR MULTI
         POBD R36,+R32         ! BYTE COUNT
         ADM  R36,R32          ! POINTER TO NEXT LINE
         RTN                   !
!
! *******************************************************************
         BYT  341              ! ATTRIBUTE FOR REMARK
!
! NOTE: The above attribute byte is probably wasted space, as there
! was a REMRK. runtime routine right after it, that was later commented
! out, and there's no label on the next line that would allow this attribute
! to be used... so, wasted byte that SHOULD have been commented out.
!
! *******************************************************************
         BYT  241              ! ATTRIBUTE FOR PRINTER IS
PRINS.   LDM  R20,=PS.C.       ! PRINTER PARAM
         JMP  SOMEIS           ! DO COMMON "IS"
!
! *******************************************************************
! *******************************************************************
         BYT  241              ! ATTRIBUTES
CRT.     LDM  R20,=CS.C.       ! GET CRT SELECT CODE
SOMEIS   JSB  =ONER            ! GET PARAMETER
         TSM  R40              ! ERROR IF 0
         JZR  PISER            ! JIF 0
         STMD R40,R20          ! SET CRT SELECT CODE
         RTN                   !
!
PISER    JSB  =ERROR+          !
         BYT  89D              ! INVALID PARAM
!
TST5     JSB  =TWOROI          ! GET A AND B
         JEN  TSTINT           ! JIF INTEGERS FOUND
         XRM  R40,R50          ! ARE THEY EQUAL?
         RTN                   !
!
TSTINT   XRM  R55,R45          ! SEE IF X=Y
         RTN                   !
!
! *******************************************************************
! RUNTIME - GET OPTIONAL PARAMETERS
! *******************************************************************
TO?I     JSB  =ON?I            ! GET ONE INT
         JEZ  NON?I            ! JIF NONE
         PUMD R40,+R6          ! SAVE FIRST
         JSB  =ON?I            ! GET SECOND
         POMD R#,-R6           ! FIRST TO R#
         ICE                   ! COUNT = 1 OR 2
NON?I    RTN                   !
!
ON?I     CLE                   ! SET FLAG FOR INTEGER
         ICE                   !
         JMP  ON?IR            ! DO COMBINED ROUTINE
!
ON?R     CLE                   ! CLEAR FLAG FOR REAL
ON?IR    BIN                   ! COMPARES BINARY
         CMMD R12,=TOS         ! IS STACK EMPTY
         BCD                   ! FOR RETURN
         JZR  NON?IR           ! JIF STACK EMPTY
         JNC  NON?IR           ! JIF STACK BACKWARD
         JEN  GETINT           ! JIF WE WANT INTEGER
         JSB  =ONER            ! GET ONE REAL
         JMP  GOT?IR           ! DONE
!
GETINT   JSB  =ONEI            ! GET ONE INTEGER
GOT?IR   CLE                   !
         DRP  R50              !
         ICE                   !
         RTN                   !
!
NON?IR   CLM  R40              ! RETURN ZERO
         CLE                   ! NOT FOUND
         RTN                   !
!
! *******************************************************************
! RUNTIME - RELATIONAL OPERATORS
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
EQ.      JSB  =TST5            ! SEE IF X=Y
         JMP  ZRTRUE           ! ZRO=TRUE
!
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
UNEQ.    JSB  =TST5            ! SEE IF X=Y
         JNZ  TRUE.            ! NO, NEQ TRUE
         JMP  FALSE.           ! YES, NEQ FALSE
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
LT.      JSB  =SUBT            ! SUBTRACT THEM
         JEN  LT.I             ! JIF INTEGERS
         JRN  TRUE.            ! JIF A-B NEGATIVE
         JMP  FALSE.           ! NO, A>=B
!
LT.I     JNG  TRUE.            ! JIF A-B NEGATIVE
         JMP  FALSE.           !
!
! *******************************************************************
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
LEQ.     JSB  =SUBT            ! SUBTRACT THEM
         JEN  LEQ.I            ! JIF INTEGERS
         JRN  TRUE.            ! JIF X-Y NEGATIVE
         TSM  R40              ! CHECK FOR ZERO
ZRTRUE   JZR  TRUE.            ! JIF ZERO
         JMP  FALSE.           !
!
LEQ.I    JNG  TRUE.            ! JIF X-Y < 0
         JMP  ZRTRUE           ! SAME AS FLOATING
!
! *******************************************************************
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
GR.      JSB  =SUBT            ! SUBTRACT THEM
         JEN  GR.I             ! JIF INTEGERS
         TSM  R40              ! CHECK SIGN
         JZR  FALSE.           ! JIF X=Y
         TSB  R41              ! CHECK SIGN
RZTRUE   JRZ  TRUE.            ! JIF X>Y
         JMP  FALSE.           ! X<Y
!
GR.I     JZR  FALSE.           ! JIF X=Y
PSTRUE   JPS  TRUE.            ! JIF X-Y>0
         JMP  FALSE.           ! X<Y
!
! *******************************************************************
! *******************************************************************
         BYT  6,51             ! ATTRIBUTES
GEQ.     JSB  =SUBT            ! SUBTRACT THEM
         JEZ  RZTRUE           ! RZ=TRUE
         JMP  PSTRUE           ! POS=TRUE
!
SUBT     JSB  =SUBROI          ! SUBTRACT THEM
         JSB  =ONEROI          ! GET RESULT
         JEN  SUBTI            ! JIF INTEGER
         TSB  R41              ! CHECK THE SIGN
         RTN                   !
!
SUBTI    TSM  R45              ! CHECK NUMBER
         RTN                   !
!
! *******************************************************************
! RUNTIME LOGICAL OPERATORS
! *******************************************************************
         BYT  4,51             ! ATTRIBUTES
AND.     JSB  =TWOROI          ! GET X,Y
         TSM  R55              ! CHECK X
         JZR  FALSE.           ! ONE FALSE, ALL FALSE
! GENERAL "LOGICAL IF 45 ZERO GO TO FALSE"
L45ZF    TSM  R45              ! HOW ABOUT Y?
         JZR  FALSE.           ! FALSE
TRUE.    CLM  R45              ! ANSWER IS INTEGER 1
         ICB  R45              !
PUSHTF   JSB  =I#PU45          ! SET 377, PUSH 40
         RTN                   !
!
! *******************************************************************
!
! *******************************************************************
         BYT  10,50            ! ATTRIBUTES
NOT.     JSB  =ONEROI          ! GET THE NUMBER
! GENERAL "LOGICAL IF 45 ZERO GO TO TRUE"
L45ZT    TSM  R45              !
         JZR  TRUE.            ! JIF FALSE MAKE TRUE
FALSE.   CLM  R45              ! ANSWER IS INTEGER 0
         JMP  PUSHTF           ! PUSH IT
!
! *******************************************************************
!
! *******************************************************************
         BYT  2,51             ! ATTRIBUTES
OR.      JSB  =TWOROI          ! GET X,Y
         TSM  R55              ! CHECK X
         JNZ  TRUE.            ! JIF ONE FALSE (ALL FLASE)
         JMP  L45ZF            ! IF R45 ZERO, FALSE
!
! *******************************************************************
!
! *******************************************************************
         BYT  2,51             ! ATTRIBUTES
EXOR.    JSB  =TWOROI          ! GET X,Y
         TSM  R55              ! CHECK X
         JZR  L45ZF            ! IF R55=0, R45 ZERO IF FALSE
         JMP  L45ZT            ! R55#0, R45 ZERO IS TRUE
!
! *******************************************************************
! RUNTIME - BINARY PROGRAM
! *******************************************************************
         BYT  214              ! ATTRIBUTES
BP:GO    BIN                   ! FOR ADDS
         CLM  R30              ! CLEAR R30,31
         POBD R30,+R10         ! GET DUMMY BYTE (FAKE BPGM/ROM #)
         POBD R30,+R10         ! GET TOKEN OFFSET
         LDMD R34,=BINTAB      ! GET BASE ADDRESS
         STM  R34,R36          ! ALSO TO R36
         ADM  R34,=30,0        ! POINT TO POINTERS
         POMD R32,+R34         ! GET "BASE ADDRESS"
         CMM  R32,R36          ! IS IT CORRECT?
         JNZ  BPERR            ! MISSING B.P.
         POMD R32,+R34         ! GET RUNTIME BASE
         ADM  R32,R30          ! ADD TOKEN NUMBER
         ADM  R32,R30          !    TWICE
         LDMD R32,R32          ! GET RUNTIME ADDRESS
         JSB  X32,ZRO          ! GO THERE
         RTN                   ! DONE
!
BPERR    JSB  =ERROR+          !
         BYT  50D              ! BIN PRGM MISSING
!
! *******************************************************************
! ASCII SYSTEM TABLE (KEYWORDS)
! *******************************************************************
ASCIIS   ASP  ":"              ! 45
         ASP  "&"              ! 46
         ASP  ";"              ! 47
         ASP  "("              ! 50
         ASP  ")"              ! 51
         ASP  "*"              ! 52
         ASP  "+"              ! 53
         ASP  ","              ! 54
         ASP  "-"              ! 55
         ASP  "."              ! 56
         ASP  "/"              ! 57
         ASP  "^"              ! 60
         ASP  "#"              ! 61
         ASP  "<="             ! 62
         ASP  ">="             ! 63
         ASP  "<>"             ! 64
         ASP  "="              ! 65
         ASP  ">"              ! 66
         ASP  "<"              ! 67
         ASP  "-"              ! 70
         ASP  "#"              ! 71
         ASP  "<="             ! 72
         ASP  ">="             ! 73
         ASP  "<>"             ! 74
         ASP  "="              ! 75
         ASP  ">"              ! 76
         ASP  "<"              ! 77
         ASP  "@ "             ! 100
         ASP  "ON ERROR"       ! 101
         ASP  "OFF ERROR"      ! 102
         ASP  "ON KEY#"        ! 103
         ASP  "OFF KEY#"       ! 104
         ASP  "AUTO"           ! 105
         ASP  "BEEP"           ! 106
         ASP  "CLEAR"          ! 107
         ASP  "CONT"           ! 110
         ASP  "ON TIMER#"      ! 111
         ASP  "INIT"           ! 112
         ASP  "LIST"           ! 113
         ASP  "BPLOT"          ! 114
         ASP  "SETTIME"        ! 115
         ASP  "CHAIN"          ! 116
         ASP  "SECURE"         ! 117
         ASP  "READ#"          ! 120
         ASP  "RENAME"         ! 121
         ASP  "ALPHA"          ! 122
         ASP  "CRT IS"         ! 123
         ASP  "RUN"            ! 124
         ASP  "DEG"            ! 125
         ASP  "DISP"           ! 126
         ASP  "GCLEAR"         ! 127
         ASP  "SCRATCH"        ! 130
         ASP  "DEFAULT ON"     ! 131
         ASP  "GOTO"           ! 132
         ASP  "GOSUB"          ! 133
         ASP  "PRINT#"         ! 134
         ASP  "GRAD"           ! 135
         ASP  "GRAPH"          ! 136
         ASP  "INPUT"          ! 137
         ASP  "IDRAW"          ! 140
         ASP  "LET FN"         ! 141
         ASP  "LET"            ! 142
         ASP  "PRINT ALL"      ! 143
         ASP  "CAT"            ! 144
         ASP  "DRAW"           ! 145
         ASP  "ON"             ! 146
         ASP  "LABEL"          ! 147
         ASP  "WAIT"           ! 150
         ASP  "PLOT"           ! 151
         ASP  "PRINTER IS"     ! 152
         ASP  "PRINT"          ! 153
         ASP  "RAD"            ! 154
         ASP  "RANDOMIZE"      ! 155
         ASP  "READ"           ! 156
         ASP  "STOREBIN"       ! 157
         ASP  "RESTORE"        ! 160
         ASP  "RETURN"         ! 161
         ASP  "OFF TIMER#"     ! 162
         ASP  "MOVE"           ! 163
         ASP  "FLIP"           ! 164
         ASP  "STOP"           ! 165
         ASP  "STORE"          ! 166
         ASP  "PENUP"          ! 167
         ASP  "TRACE VAR"      ! 170
         ASP  "TRACE ALL"      ! 171
         ASP  "XAXIS"          ! 172
         ASP  "YAXIS"          ! 173
         ASP  "COPY"           ! 174
         ASP  "NORMAL"         ! 175
         ASP  "ERASETAPE"      ! 176
         ASP  "INTEGER"        ! 177
         ASP  "SHORT"          ! 200
         ASP  "DELETE"         ! 201
         ASP  "SCALE"          ! 202
         ASP  "REM"            ! 203
         ASP  "OPTION BASE"    ! 204
         ASP  "COM"            ! 205
         ASP  "DATA"           ! 206
         ASP  "DEF FN"         ! 207
         ASP  "DIM"            ! 210
         ASP  "KEY LABEL"      ! 211
         ASP  "END"            ! 212
         ASP  "FN END"         ! 213
         ASP  "FOR"            ! 214
         ASP  "IF"             ! 215
         ASP  "IMAGE"          ! 216
         ASP  "NEXT"           ! 217
         ASP  "UNSECURE"       ! 220
!        CAPASM generates 240, rom code is 200 for the next line
!        ASP  " "              ! 221 
         BYT  200
         ASP  "ASSIGN#"        ! 222
         ASP  "CREATE"         ! 223
         ASP  "PURGE"          ! 224
         ASP  "REWIND"         ! 225
         ASP  "LOADBIN"        ! 226
         ASP  "PAUSE"          ! 227
         ASP  "LOAD"           ! 230
         ASP  "REAL"           ! 231
         ASP  "REN"            ! 232
         ASP  "!"              ! 233
         ASP  "DEFAULT OFF"    ! 234
         ASP  "PEN"            ! 235
         ASP  "PLIST"          ! 236
         ASP  "LDIR"           ! 237
         ASP  "IMOVE"          ! 240
         ASP  "FN"             ! 241
         ASP  "CTAPE"          ! 242
         ASP  "TRACE"          ! 243
         ASP  "TO"             ! 244
         ASP  " OR "           ! 245
         ASP  "MAX"            ! 246
         ASP  "TIME"           ! 247
         ASP  "DATE"           ! 250
         ASP  "FP"             ! 251
         ASP  "IP"             ! 252
         ASP  "EPS"            ! 253
         ASP  "RMD"            ! 254
         ASP  "CEIL"           ! 255
         ASP  "ATN2"           ! 256
         BYT  200              ! 257
         ASP  "SQR"            ! 260
         ASP  "MIN"            ! 261
         BYT  200              ! 262
         ASP  "ABS"            ! 263
         ASP  "ACS"            ! 264
         ASP  "ASN"            ! 265
         ASP  "ATN"            ! 266
         ASP  "SGN"            ! 267
         BYT  200              ! 270
         ASP  "COT"            ! 271
         ASP  "CSC"            ! 272
         BYT  200              ! 273
         ASP  "EXP"            ! 274
         ASP  "INT"            ! 275
         ASP  "LGT"            ! 276
         ASP  "LOG"            ! 277
         BYT  200              ! 300
         ASP  "SEC"            ! 301
         ASP  "CHR$"           ! 302
         ASP  "VAL$"           ! 303
         ASP  "LEN"            ! 304
         ASP  "NUM"            ! 305
         ASP  "VAL"            ! 306
         ASP  "INF"            ! 307
         ASP  "RND"            ! 310
         ASP  "PI"             ! 311
         ASP  "UPC$"           ! 312
         ASP  "USING"          ! 313
         ASP  "THEN"           ! 314
         ASP  "TAB"            ! 315
         ASP  "STEP"           ! 316
         ASP  " EXOR "         ! 317
         ASP  "NOT "           ! 320
         ASP  " DIV "          ! 321
         ASP  "ERRN"           ! 322
         ASP  "ERRL"           ! 323
         BYT  200              ! 324
         ASP  " AND "          ! 325
         ASP  " MOD "          ! 326
         ASP  "ELSE"           ! 327
         ASP  "SIN"            ! 330
         ASP  "COS"            ! 331
         ASP  "TAN"            ! 332
         ASP  " TO "           ! 333
         BYT  200              ! 334
         BYT  200              ! 335
         ASP  "["              ! 336
         ASP  "]"              ! 337
         ASP  "\"              ! 340
         ASP  "POS"            ! 341
         ASP  "RTD"            ! 342
         ASP  "DTR"            ! 343
         ASP  "FLOOR"          ! 344
         BYT  200              ! 345
         BYT  377              ! END OF TABLE
! *******************************************************************
! ERROR MESSAGES
! *******************************************************************
ERMSG    ASP  "0"              ! 0
         ASP  "UNDERFLOW"      ! 1
         ASP  "OVERFLOW"       ! 2
         ASP  "COT/CSC=INF"    ! 3
         ASP  "TAN/SEC=INF"    ! 4
         ASP  "0^NEG"          ! 5
         ASP  "0^0"            ! 6
         ASP  "NULL DATA"      ! 7
         ASP  "/ZERO"          ! 8
!
! THE REST OF THE ERROR MESSAGES ARE NON-DEFAULT
!
         ASP  "NEG^NON-INT"    ! 9
         ASP  "SQR(-)"         ! 10
         ASP  "ARG OUT OF RANGE" ! 11
         ASP  "LOG(0)"         ! 12
         ASP  "LOG(-)"         ! 13
         BYT  200              ! 14 DUMMY
!
! SYSTEM ERRORS
!
         ASP  "SYSTEM"         ! 15
         ASP  "CONTINUE BEFORE RUN" ! 16
         ASP  "FOR NESTING"    ! 17
         ASP  "GOSUB NESTING"  ! 18
         ASP  "MEM OVF"        ! 19
         ASP  "OUT OF PAPER"   ! 20
         ASP  "ROM MISSING"    ! 21
         ASP  "SECURED"        ! 22
         ASP  "SELF TEST"      ! 23
         BYT  200              ! 24
         ASP  "TWO BIN PROGS"  ! 25
         BYT  200              ! 26 DUMMY
         BYT  200              ! 27 DUMMY
         BYT  200              ! 28 DUMMY
         BYT  200              ! 29 DUMMY
!
! PROGRAM ERRORS
!
         ASP  "OPTION BASE"    ! 30
         ASP  "CHAIN"          ! 31
         ASP  "COM MISMATCH"   ! 32
         ASP  "DATA TYPE"      ! 33
         ASP  "NO DATA"        ! 34
         ASP  "DIM EXIST VRBL" ! 35
         ASP  "DIM ILLEGAL"    ! 36
         ASP  "DUP FN"         ! 37
         ASP  "NO FNEND"       ! 38
         ASP  "FN MISSING"     ! 39
         ASP  "FN PARAM"       ! 40
         ASP  "FN="            ! 41
         ASP  "RECURSIVE FN CALL" ! 42
         ASP  "NUMERIC INPUT"  ! 43
         ASP  "TOO FEW INPUTS" ! 44
         ASP  "TOO MANY INPUTS" ! 45
         ASP  "NEXT MISSING"   ! 46
         ASP  "NO MATCHING FOR" ! 47
         ASP  "END"            ! 48
         ASP  "NULL DATA"      ! 49
         ASP  "BIN PROG MISG"  ! 50
         ASP  "RETURN W/O GOSUB" ! 51
         ASP  "IMAGE"          ! 52
         ASP  "PRINT USING"    ! 53
         ASP  "TAB"            ! 54
         ASP  "SUBSCRIPT"      ! 55
         ASP  "STRING OVF"     ! 56
         ASP  "MISSING LINE"   ! 57
         BYT  200              ! 58 DUMMY
         BYT  200              ! 59 DUMMY
!
! TAPE ERRORS
!
         ASP  "WRITE PROTECT"  ! 60
         ASP  ">42 FILES"      ! 61
         ASP  "CARTRIDGE OUT"  ! 62
         ASP  "DUP NAME"       ! 63
         ASP  "EMPTY FILE"     ! 64
         ASP  "END OF TAPE"    ! 65
         ASP  "FILE CLOSED"    ! 66
         ASP  "FILE NAME"      ! 67
         ASP  "FILE TYPE"      ! 68
         ASP  "RANDOM OVF"     ! 69
         ASP  "READ"           ! 70
         ASP  "EOF"            ! 71
         ASP  "RECORD"         ! 72
         ASP  "SEARCH"         ! 73
         ASP  "STALL"          ! 74
         ASP  "NOT HP-85 FILE" ! 75
         BYT  200              ! 76 DUMMY
         BYT  200              ! 77 DUMMY
         BYT  200              ! 78 DUMMY
         BYT  200              ! 79 DUMMY
!
! SYNTAX ERRORS
!
         ASP  ") EXPECTED"     ! 80
         ASP  "BAD EXPRESSION" ! 81
         ASP  "STRING EXPR"    ! 82
! CAPASM ERROR: cannot parse the stmt below, syntax altered
!        ASP  ""," MISSING"    ! 83
         ASP  13,"," MISSING    ! 83
         ASP  "EXCESS CHARS"   ! 84
         ASP  "EXPR TOO BIG"   ! 85
         ASP  "ILLEGAL AFTER THEN" !
         ASP  "BAD DIM"        ! 87
         ASP  "BAD STMT"       ! 88
         ASP  "INVALID PARAM"  ! 89
         ASP  "LINE >9999"     ! 90
         ASP  "MISSING PARAM"  ! 91
         ASP  "SYNTAX"         ! 92
!
! *******************************************************************
! CLOCK FIRMWARE
! *******************************************************************
! THIS ROUINE ADDS A BASE TIME FROM RAM AND THE ELAPSED TIME FROM THE
! SYSTEM CLOCK TO GIVE ACTUAL TIME (IN SECONDS).
! *******************************************************************
         BYT  0,55             ! ATTRIBUTES
TIME.    CLB  R55              ! ADDRESS TIMER 0
         STBD R55,=GINTDS      ! DISABLE FOR THE MOMENT
         JSB  =TIMWST          !
         CLM  R40              ! CLEAR UPPER 4 BYTES+
         JSB  =TIMRDY          ! TIME TO 44-47
         LDMD R44,=CLKDAT      !
         STBD R44,=GINTEN      ! RE-ENABLE EVERYONE
         LDM  R36,=4,0         ! MS TO SEC
         BCD                   !
         CLB  R32              ! SGN IS +
         JSB  =SHRONF          ! SHIFT AND PACK
         LDMD R50,=TIME        ! GET BASE TIME
         POMD R40,-R12         ! GET INITIAL TIME
         JSB  =ADD10           ! COMPUTE ACTUAL TIME
         RTN                   !
! *******************************************************************
! THIS ROUINE RETURNS THE JULIAN DATE ON THE STACK.
! THIS ROUTINE SETS THE SYSTEM CLOCK TO INTERRUPT ON THE #SECS FROM
! NOW UNTIL MIDNIGHT (AT WHICH POINT THE INTERRUPT ROUTINE WILL
! INCREMENT THE DATE IN RAM).  THE LOWER PORTION OF THE ROUTINE
! SHIFTS THE USER "SEC" INPUT TO MILLISEC FOR INPUT TO THE SYS CLOCK.
! *******************************************************************
         BYT  241              !
STIME.   JSB  =ONEI            ! GET DATE OFF STACK
         PUMD R45,+R6          !   AND SAVE IT
         JSB  =ONER            ! REAL TIME
         TSB  R41              ! - TIME?
         JRZ  TIMOK.           ! JIF +
         POMD R45,-R6          ! CLEAN R6
!
ER89D    JSB  =ERROR+          !
         BYT  89D              ! ERROR 89: INVALID PARAM
!
TIMOK.   PUMD R40,+R6          ! SAVE BASE TIME
         CLM  R50              ! GENERATE 86400
         LDB  R50,=4           ! EXPONENT
         LDM  R56,=100,206     !
         BCD                   !
         JSB  =SUB10           ! BUILD TERMINAL COUNT
         POMD R60,-R6          ! POP BASE TIME
         POMD R55,-R6          ! POP DATE
         POMD R40,-R12         ! POP TERM. COUNT
         LLB  R57              ! DUMP SIGN
         LRB  R57              !
         TSB  R41              ! - TERMINAL COUNT?
         JRN  ER89D            ! JIF YES
         STMD R60,=TIME        ! BASE TIME
         STMD R55,=DATE        ! DATE
         LDM  R55,=32,4,0      ! STATUS, EXPONENT
         JSB  =INTSET          ! START TIMER
WT41MS   LDBD R#,=CLKSTS       ! LET TIMER CLEAR
         JNG  WT41MS           ! WAIT FOR 1 MS
         RTN                   !
!
! [SORRY, THESE COMMENTS ARE TRUNCATED IN THE LISTING]
! COMMENTS: SETTIME USES ONEI FOR "SEONCDS SINCE MIDNIGHT"
! AND CHECKS FOR VALUES OUTSIDE 0-86400
! WHICH WILL RESULT IN AN ERROR.
! ON TIMER USES INTSET SO THAT 1-999
! GIVES THE EXPECTED RESULT WHILE AL
! ARE FORCED TO 0.  THIS WILL GENERATE
! IMMEDIATE INTERRUPT.
! THE NEXT INTERRUPT WOULD THEN
! OCCUR 27+ HOURS LATER.
! ALSO NOTE THAT ON TIMER IGNORES TH
!
! *******************************************************************
! WAIT RUNTIMNE
! *******************************************************************
!
         BYT  241              !
WAIT.    BCD                   ! WAIT X MILLISECONDS
         CLM  R40              !
         ICB  R40              !
         LDB  R42,=146         ! GENERATE 16.666666666
         STM  R42,R43          ! PROPOGATE THEM
         ICB  R42              ! 67
         LDB  R47,=26          ! MSBYTE
         PUMD R40,+R12         ! PUSH TO STACK
         JSB  =DIV2            ! WAIT N>> N/16
         JSB  =ONEI            !
         TSB  R16              !
         JOD  NOWAIT           !
         BCD                   !
CK47     TSB  R47              ! NEGATIVE?
         JLN  NOWAIT           ! JIF YES
         LDBD R27,=SVCWRD      ! EXIT ON KEYHIT
         JOD  NOWAIT           !
         JSB  =RETRA1          !
         BCD                   !
         DCM  R45              ! DOWN COUNT
         JNZ  CK47             !
NOWAIT   RTN                   !
!
! *******************************************************************
! TIMER INTERRUPT ROUTINES
! *******************************************************************
ONCLK1   LDMD R34,=TIMTAB      !
CLK2EN   BIN                   !
         JZR  CLKOUT           ! IF SOMEONE STARTS TIMER
         TSB  R16              !
         JOD  CLKOUT           ! JIF CALC MODE
         JZR  CLKOUT           ! JIF IDLE
         CMB  R16,=6           ! DON'T ALLOW 6 EITHER
         JZR  CLKOUT           !
         LDMD R36,=ONFLAG      !
         JNZ  CLKOUT           !
         STMD R10,=ONFLAG      ! STORE RETURN
         LDM  R10,R34          ! ON TIMER ADDR
         JSB  =SETTR1          ! SET TRACE & "FROM"
         LDB  R16,=7           ! RUN MODE ENTER IN MIDDLE
CLKOUT   CLE                   !
         RTN                   !
!
ONCLK2   LDMD R34,=TIMTB2      !
         JMP  CLK2EN           !
!
ONCLK3   LDMD R34,=TIMTB3      !
         JMP  CLK2EN           !
!
! *******************************************************************
! ON TIMER RUNTIME
! *******************************************************************
         BYT  241              !
ONTIM.   JSB  =ONER            ! TURN ON A TIMER
         STM  R40,R20          ! SAVE TIMEOUT AMT.
         JSB  =ONEB            ! WHICH TIMER?
         TSB  R16              !
         JOD  NONTIM           ! JIF ODD
! NOTE: IF R16 IS ODD, COMPARE IS ODD
         STB  R46,R55          !
         DCM  R46              ! 1-3 > 0-2
         STM  R46,R36          !
         LDM  R40,R20          ! TIMEOUT TO 40
         CMM  R36,=3,0         !
         JNC  TIMOK            !
!
BADPAR   JSB  =ERROR+          !
         BYT  89D              ! BAD PARAMS
!
TIMOK    LLM  R#               ! DOUBLE FOR INDEX
         STMD R10,X36,TIMTAB   !
         ADM  R10,=3,0         ! SKIP OVER GOTO/GOSUB #
         TSB  R55              ! CLEAR CARRY
         ERB  R55              ! SHIFT RIGHT
         ERB  R55              !   2 PLACES
         ERB  R55              !   (+1 FOR CARRY)
         ADB  R55,=72          ! TIMER #, GO, CLR, ENABLE
         LDM  R56,=7,0         !
INTSET   BCD                   !
         JSB  =SEP10           ! SEPARATE EXPONENT
         CMM  R56,R36          ! EXP OUT OF RANGE
         JCY  SHFTCK           ! JIF NO
         CLM  R40              ! FORCE A 0
SHFTCK   CMM  R36,R56          ! EXP 4 OR MORE?
         JCY  SETEN            ! JIF YES
         LRM  R47              ! NO, SHIFT TERM COUNT
         JZR  SETEN            ! EXIT WITH 0
         ICM  R36              ! INCR. EXPONENT
         JMP  SHFTCK           ! LOOP
!
! *******************************************************************
! POWER ON ROUTINE FOR SYSTEM CLOCK
! *******************************************************************
TIME0    LDB  R55,=32          ! clear, go, enable timer 0
         CLM  R44              !
         LDM  R46,=100,206     ! make 86400000 (milliseconds in a day)
SETEN    STBD R#,=GINTDS       ! disable interrupts
         JSB  =TIMRDY          ! SEND STATUS
         STBD R55,=CLKSTS      !
! MUST NOT USE TIMWST HERE FOR LACK OF CYCLES
         STMD R44,=CLKDAT      ! STORE TERM. COUNT
         STBD R44,=GINTEN      ! ENABLE INTERRUPTS
NONTIM   RTN                   !
!
! *******************************************************************
! OFF TIMER RUNTIME
! *******************************************************************
         BYT  241              ! ATTRIBUTES
OFTIM.   JSB  =ONEB            ! GET TIMER #
         CMM  R46,=4,0         ! (ONEB LEAVES BIN MODE)
         JCY  BADPAR           !
         STB  R46,R55          ! SAVE FOR WRSTATUS
         DCM  R46              ! FOR INDEX
         LLM  R46              ! DOUBLE
         CLM  R20              !
         STMD R20,X46,TIMTAB   ! CLEAR TABLE ENTRY
! CARRY IS ALREADY 0, SO SHIFT MOVES IN A ZERO
         ERB  R55              ! SHIFT RIGHT
         ERB  R55              !    2 PLACES
         ERB  R55              !    (+1 FOR CARRY)
         ADB  R55,=45          ! ADD STOP, DISABLE, CLR SV
         JSB  =TIMWST          ! SEND THE STATUS
         RTN                   !
! *******************************************************************
! SCALE RUNTIME ROUTINE
! *******************************************************************
         BYT  241              ! ATTRIBUTES
SCALE.   STMD R12,=SAVER6      ! SAVE STACK POINTER
         JSB  =SCASUB          ! SCALE SUBROUTINE
         JEZ  S.EROR           ! SCALE ERROR
         JSB  =TWOR            ! GET TO NEXT TWO
         JSB  =SCASUB          ! SCALE SUBROUTINE
         JEZ  S.EROR           ! SCALE ERROR
         JSB  =TWOR            !
         STMD R40,=CRYMAX      !
         STMD R50,=CRYMIN      !
         LDM  R20,=20,31       ! 191 CONSTANT (MAX HEIGHT GRAPHICS)
         LDM  R22,=10,0        ! INDEX
         JSB  =SETFCT          !
         JSB  =TWOR            !
         STMD R40,=CRXMAX      !
         STMD R50,=CRXMIN      !
         LDM  R20,=120,45      ! 255 CONSTANT (MAX WIDTH GRAPHICS)
         CLB  R22              !
         JSB  =SETFCT          !
S.EROR   RTN                   !
!
! *******************************************************************
! SCALE SUBROUTINE POPS STACK, COMPARES VALUES
!
SCASUB   JSB  =TWOR            ! YMAX TO 50, YMIN TO 40
         LDMD R12,=SAVER6      ! PROTECT STACK
         JSB  =COMFLT          ! COMPARE TWO VALUES
         JRN  L99              ! NO ERROR YET
!
! NOTE: THIS ALSO CATCHES A 0 DIFFERENCE AS ERROR
!
         JSB  =ERROR           !
         BYT  89D              ! INVALID PARAMETERS
!
         CLE                   !
         RTN                   !
!
L99      CLE                   !
         ICE                   !
         RTN                   !
!
SETFCT   JSB  =COMFLT          !
         CLM  R40              !
         ICB  R40              !
         ICB  R40              ! SET EXPONENT
         LDM  R46,R20          ! GET CONSTANT
         JSB  =DIV10           ! COMPUTE YFACTOR
         POMD R50,-R12         ! GET OFF STACK
         STMD R50,X22,XFACT    !
         RTN                   !
!
! *******************************************************************
! PEN RUNTIME
! *******************************************************************
         BYT  241              !
PEN.     JSB  =ONER            ! GET AN INTEGER
         BIN                   !
         CLB  R47              !
         TSB  R41              ! MAKE 0 OR 377
         JRN  PSYMOK           !
         DCB  R47              !
PSYMOK   STBD R47,=PLOTSY      ! STORE SYMBOL IN MEMORY
PENRTN   RTN                   !
!
! *******************************************************************
! PENUP RUNTIME
! *******************************************************************
         BYT  241              !
PENUP.   CLB  R30              ! GET 0
         STBD R30,=PENUPF      ! CLEAR PENUP FLAG
         RTN                   !
!
! *******************************************************************
! GRAPHICS INPUT SUBROUTINE
! *******************************************************************
INGRAF   CLB  R76              !
         STBD R76,=LDIRF       ! SET HORIZONTAL
         LDMD R76,=XMAP        ! GET LAST ADDRESS
         JSB  =INGSUB          ! GRAPHICS INPUT SUB
         LDMD R76,=XMAP        ! SET NEXT ADDRESS
         ADM  R76,=10,0        !
         CMM  R76,=0,300       ! MOD 48K CHECK
         JCY  NOSETX           !
         STMD R76,=XMAP        !
NOSETX   RTN                   !
!
INGSUB   JSB  =DRAW1           ! DO THE ADDRESSING
         STB  R75,R14          ! BITS FOR POSITIONING
         STMD R76,=CRTGBA      ! SAVE 12K ADDR
         JSB  =REDROM          ! SEND THE CHAR
         RTN                   !
!
! *******************************************************************
! FOR RUNTIME
! FOR STAK ENTRY FORMAT:
!  FOR VARIABLE ADDRESS   2 BYTES
!  FINAL VALUE            8 BYTES
!  STEP VALUE             8 BYTES
!  LOOP ADDRESS           2 BYTES
! *******************************************************************
         BYT  341              !
FOR.     BIN                   !
         LDMD R65,R10          !
         JSB  =FETSVA          ! GO GET ADDRESS
         LDMD R26,=LAVAIL      !
         JSB  =GETFC           ! GET FOR-LOOP COUNT IN 20
         STM  R26,R2           ! SAVE LAVAIL
         STB  R20,R0           ! SAVE FOR-LOOP COUNT
FLOOP    LDMD R36,R26          ! GET NEXT FOR-VAR ADDR
         DCB  R0               ! DECREMENT COUNT
         JNG  FOR1             ! JIF NO MORE
         ADM  R26,=26,0        ! MOVE TO NEXT ENTRY
         CMM  R36,R34          ! ABSOLUTE ADDRESSES MATCH?
         JNZ  FLOOP            ! JIF NO MATCH
         DCM  R26              ! LWA SINK
         LDM  R24,R26          ! SAVE FOR MOVDN
         SBM  R24,=26,0        ! LWA SOURCE
         LDM  R22,R24          !
         SBM  R22,R2           ! BYTES TO MOVE
         ICM  R22              ! MAKE IT RIGHT
         ADM  R2,=26,0         ! NEW LAVAIL
         STMD R2,=LAVAIL       ! SAVE IT
         DCB  R20              ! DEC COUNT
         JSB  =MOVDN           ! GO MOVE IT, OPEN A HOLE
FOR1     LDM  R26,R2           ! RESTORE R26
         SBM  R26,=66,0        ! RESERVE SPACE + 40
         CMM  R26,R12          ! ENOUGH SPARE ROOM?
         JNC  ERR1             ! JIF NO
         ADM  R26,=40,0        ! RESTORE LAVAIL
         ICB  R20              ! INC FOR LOOP CNT
         JCY  ERR2             ! JIF TOO MANY FOR-LOOPS NESTED
         STBD R20,X30,P.FCNT   ! # ACTIVE LOOPS
         STMD R26,=LAVAIL      ! UPDATE FOR STAK
         PUMD R34,+R26         ! FOR var ABS ADDR
         CLM  R50              !
         PUMD R50,+R26         ! "TO" VALUE
         LDM  R54,=377,1,0,0   ! DEFAULT "STEP" VALUE (INTEGER 1)
         PUMD R50,+R26         ! "STEP" VALUE
         RTN                   !
!
ERR1     JSB  =ERROR+          !
         BYT  19D              ! OUT OF MEMORY
!
ERR2     JSB  =ERROR+          !
         BYT  17D              ! > 255 ACTIVE FOR LOOPS
!
GETFC    LDMD R30,=FWCURR      ! START OF PROGRAM
         LDBD R20,X30,P.FCNT   ! GET COUNT
         RTN                   !
!
! *******************************************************************
! 'TO' RUNTIME
! *******************************************************************
         BYT  41               !
TO.      LDMD R26,=LAVAIL      !
         BIN                   !
         POMD R34,+R26         ! SNV ADDR
         POMD R50,-R12         ! GET REAL OR INTEGER
         PUMD R50,+R26         ! STORE FV
         LDBD R46,R10          ! NEXT TOKEN
         JSB  =TSTEND          ! CR,@,!
         JEZ  CKDON            ! JIF YES
         RTN                   ! ELSE RETURN
!
! *******************************************************************
! 'STEP' RUNTIME
! *******************************************************************
         BYT  41               !
STEP.    LDMD R26,=LAVAIL      !
         BIN                   !
         POMD R34,+R26         ! SNV ADDR
         POMD R50,+R26         ! FINAL VALUE
         POMD R40,-R12         ! INCR
         STMD R40,R26          ! STORE INCR
CKDON    POMD R70,+R26         ! STEP OVER INCR
         LDMD R36,=PCR         !
         PUMD R36,+R26         ! PCR
         PUMD R10,+R26         ! PUSH PC
         SBM  R26,=14,0        ! BACK TO INCR
         DCM  R34              ! DEC ADDR
         DCM  R34              ! POINT AT NAME
         POMD R46,+R34         ! GET NAME
         JSB  =FNUM            ! NUM TO 60
         BCD                   !
         LDM  R40,R60          !
         JSB  =CKDONE          ! GO SEE IF DONESTACK
         JEN  SKPFOR           ! JIF DONE
STPRTN   RTN                   ! ELSE RETURN
!
! *******************************************************************
SKPFOR   BIN                   !
         JSB  =SETTR1          ! SET TRACE "JUMPED" FLAG
         LDMD R26,=LAVAIL      !
         POMD R30,+R26         ! SNV ADDR
         LDMI R45,=PCR         ! CURRENT LINE # BYTES
         LDM  R24,R10          ! PC
SKPLOP   POBD R36,+R24         ! NEXT TOKEN
         CMB  R36,=16          ! EOL?
         JNZ  TSTNXT           ! JIF NOT EOL
! MAY NOT BE REAL EOL
         LDMD R36,=PCR         ! PTR TO CURRENT LINE
         POMD R34,+R36         ! LINE #
         CLM  R34              !
         POBD R34,+R36         ! BYTE COUNT
         ADM  R34,R36          ! PTR TO END
         CMM  R34,R24          ! EOL?
         JNZ  SKPLOP           ! JIF NOT REAL EOL
         JSB  =NXTLIN          ! ELSE NEXT LINE
         JEZ  ENDPGM           ! JIF END
         JMP  SKPLOP           ! ELSE LOOP
!
TSTNXT   CMB  R36,=217         ! CIF NEXT
         JNZ  SKPLOP           ! JIF NO
         POMD R75,-R24         ! GET VARIABLE
         PUMD R75,+R24         ! PUSH IT BACK
         LDM  R66,R75          ! VARIABLE ADDR
         PUMD R45,+R6          ! SAVE 45
         JSB  =FETSVA          ! GET ABS ADDR
         POMD R45,-R6          ! RESTORE 45
         CMM  R34,R30          ! SEE IF RIGHT NEXT
         JNZ  SKPLOP           ! JIF NO
         STM  R24,R10          !
         JSB  =EXNXT           ! RESET LAVAIL & COUNT
         BCD                   !
         RTN                   ! GO TO NEXT LINE
!
ENDPGM   JSB  =ERROR+          !
         BYT  46D              ! FOR W/O MATCHING NEXT
!
MATH2    CLE                   !
         CMB  R44,=377         !
         JNC  ROI              !
         CMB  R54,=377         !
         JNC  ROI              !
         RTN                   !
!
ROI      CLE                   !
         PUMD R40,+R12         !
         PUMD R50,+R12         !
         DCE                   !
         RTN                   !
!
CKLOOP   BCD                   !
         POMD R70,+R26         ! LIMIT
         PUMD R70,+R12         ! SAVE IT
         PUMD R34,+R12         ! ADDR
         PUMD R46,+R12         ! AND NAME FOR STORE
         JSB  =FNUM            ! CURRENT VALUE
         BCD                   !
         LDM  R40,R60          ! TO R40
         LDMD R50,R26          ! INCR
         JSB  =MATH2           ! PREPARE FOR ADD
         JEZ  ADRR             ! JIF BOTH INT
ADDRR    JSB  =ADD9            ! ADD REALS
         POMD R40,-R12         ! GET RESULT
         JMP  ADDR1            !
!
ADRR     STM  R45,R75          ! SAVE 45
         ADM  R45,R55          ! ADD
         JLZ  ADDR1            ! JIF NO OFLOW
         CMB  R47,=220         !
         JLZ  ADDR1            !
         LDM  R45,R75          ! RESTORE R45
         JSB  =ROI             !
         JMP  ADDRR            !
!
ADDR1    POMD R56,-R12         ! NAME
         STM  R56,R76          ! SAVE A COPY
         ANM  R56,=60,100      ! TYPE AND TRACE
         JZR  ADDR1A           ! JIF REAL AND NOT TRACE
         PUMD R76,+R12         ! PUSH BACK NAME
         PUMD R40,+R12         ! PUSH VAL
         PUMD R40,+R6          ! SAVE VAL
         PUMD R26,+R6          ! SAVE FOR STAK PTR
         JSB  =STOSV           !
         POMD R26,-R6          ! RESTORE FOR STAK PTR
         POMD R40,-R6          !
         JMP  ADDR1B           !
!
ADDR1A   POMD R36,-R12         ! ADDR
         STMD R40,R36          !
ADDR1B   POMD R50,-R12         ! LIMIT
CKDONE   JSB  =MATH2           ! SET UP SUB
         JEZ  SUBR             ! JIF BOTH INT
SUBRR1   JSB  =SUBROI          ! SUBTRACT REALS
         POMD R40,-R12         ! GET RESULT
         JMP  NEXT1            !
!
SUBR     STM  R45,R75          ! SAVE R45
         TCM  R55              ! COMPL R55
         ADM  R45,R55          !
         JLZ  NEXT1            ! JIF NO OFLOW
         CMB  R47,=90C         !
         JLZ  NEXT1            !
         LDM  R45,R75          ! ELSE RESTORE 45
         JSB  =ROI             !
         JSB  =ADD9            !
         POMD R40,-R12         ! GET RESULT
!
! IF (CV-LIM)*SIGN(INC) >= 0 THEN EXIT FOR LOOP
!
NEXT1    POMD R50,+R26         ! POP INCR
         BCD                   !
         LLB  R41              ! SIGN UPPER IF REAL
         LDB  R0,=42           !
         CMB  R44,=377         !
         JNC  TSTR1            ! JIF REAL
         LDB  R0,=45           !
         CLB  R41              ! SIGN POS
         TSB  R47              ! TEST NEG
         JLZ  TSTR1            ! JIF POS
         DCB  R41              ! SIGN NEG
TSTR1    LLB  R51              ! SIGN UPPER
         CMB  R54,=377         !
         JNC  TSTR2            ! JIF REAL
         CLB  R51              ! SIGN POS
         TSB  R57              ! TEST NEG
         JLZ  TSTR2            ! JIF POS
         DCB  R51              ! SET SIGN NEG
TSTR2    CLE                   !
         XRB  R51,R41          ! SIGNS SAME?
         JNG  TSRTN            ! JIF NO
         TSM  R*               ! RESULT ZERO
         JZR  TSRTN            ! JIF YES
         DCE                   !
TSRTN    RTN                   !
!
! *******************************************************************
! 'NEXT' RUNTIME
! *******************************************************************
         BYT  341              !
NEXT.    BIN                   !
         JSB  =GETFC           ! GET FOR COUNT TO R20
         JZR  NXERR            ! JIF NO ACTIVE FOR LOOPS
         POMD R46,-R12         ! GET THE NAME
         POMD R36,-R12         ! "NEXT" SNV ADDR
         LDMD R26,=LAVAIL      ! "FOR" STAK PTR
         POMD R34,+R26         ! "FOR" SNV ADDR
         CMM  R34,R36          !
         JNZ  NXTST            ! JIF FOR NEXT MISMATCH
         JSB  =CKLOOP          ! INC CV & CIF DONE
         JEN  EXNXT            ! JIF DONE FOR LOOP
         JSB  =SETTR1          ! SET TRACE "JUMPED" FLAG
         STM  R10,R36          ! SAVE OLD PC
         POMD R10,+R26         ! GET PCR
         STMD R10,=PCR         ! AND STORE IT
         POMD R10,+R26         ! GET PC
         TSB  R16              !
         JEV  NEXTEX           ! JIF RUN MODE
         CMMD R10,=NXTMEM      !
         JNC  NXERR            ! JIF PRGM MODE NEXT
         CMM  R10,R36          !
         JCY  NXERR            ! JIF > INCOMING 10
NEXTEX   RTN                   ! GO TO TOP OF LOOP
!
EXNXT    BIN                   !
         LDMD R36,=LAVAIL      !
         ADM  R36,=26,0        !
         STMD R36,=LAVAIL      ! RESET FOR STAK
         JSB  =GETFC           !
         DCB  R#               !
         STBD R#,X30,P.FCNT    ! DEC "FOR" COUNT
         RTN                   ! AND EXIT
!
NXERR    JSB  =ERROR+          !
         BYT  47D              ! NEXT W/O MATCHING FOR
!
NXTST    PUMD R36,+R12         ! "NEXT" SNV TO STAK
         PUMD R46,+R12         ! NAME TO STAK
         JSB  =EXNXT           ! ADV TO NEXT "FOR"
         JMP  NEXT.            !
!
! *******************************************************************
! "ON KEY #" RUNTIME
! *******************************************************************
         BYT  241              !
ONKEY.   BIN                   ! ON KEY#
         LDMD R34,=TOS         ! TOP OF STAK
         ADM  R34,=10,0        ! +KEY #
         SBM  R34,R12          ! -STAK
         JZR  ONK1             ! JIF NO STR
         POMD R26,-R12         ! STR ADDR
         POMD R34,-R12         ! STR LEN
ONK1     JSB  =KEY2            !
         STMD R10,X46,KEYTAB   ! SET ON KEY ADDR
         JSB  =KCLR            ! CLEAR OLD LABEL
         CMM  R34,=11,0        ! KEYLABEL LEN
         JNC  SZOK             ! JIF <= 8
         LDM  R34,=10,0        ! ELSE MAKE IT 8
SZOK     TSM  R#               !
         JZR  LEGDUN           ! JIF NO LEGEND
KSETLP   POBD R32,+R26         !
         PUBD R32,+R76         ! NEXT CHAR LEG
         DCM  R34              ! DEC COUNT
         JNZ  KSETLP           ! LOOP IF MORE
LEGDUN   BIN                   ! FOR ADD
         ADM  R10,=3,0         ! SKIP OVER "GOTO LINE#"
         RTN                   !
!
KEY2     JSB  =ONEB            ! KEY NUMBER
         DCM  R46              ! KEY-1
         LLM  R46              ! (KEY-1)*2
         RTN                   !
!
! *******************************************************************
! "ON ERROR" RUNTIME
! *******************************************************************
         BYT  241              !
ONERR.   STMD R10,=ERGOTO      ! STORE EXECUTION ADDR
         JMP  LEGDUN           ! SKIP GOTO ADDR
!
! *******************************************************************
! "OFF KEY #" RUNTIME
! *******************************************************************
         BYT  241              !
OFKEY.   BIN                   ! OFF KEY#
         JSB  =KEY2            ! GET KEY NUMBER AS TABLE OFFSET
         CLM  R36              !
         STMD R36,X46,KEYTAB   ! CLEAR ON KEY ADDR
KCLR     LDM  R46,=10,40       ! COUNT/BLANK
         ADB  R76,=3           ! 1234->4567 & 5678->0123
         ANM  R76,=7,0         !
         LLM  R76              ! *2
         LLM  R76              ! *4
         LLM  R76              ! *8
         ADM  R76,=LEGEND      ! KEY LABEL ADDR
         STM  R76,R56          ! SAVE
KCLRLP   PUBD R47,+R#          ! BLANK NEXT
         DCB  R46              ! DEC COUNT
         JNZ  KCLRLP           ! JIF MORE
         RTN                   !
!
! *******************************************************************
! "OFF ERROR" RUNTIME
! *******************************************************************
         BYT  241              !
OFFER.   CLM  R36              ! STORE ZERO
         STMD R36,=ERGOTO      ! IN "ON ERROR" LOC
         RTN                   ! DONE
!
! *******************************************************************
! "ON" GOTO/GOSUB RUNTIME
! *******************************************************************
         BYT  230              !
ON.      JSB  =ONEI            ! GET #
         DCM  R45              ! DECREMENT IT
         JNG  INVAL            ! JIF < 1
         ICM  R45              ! RESTORE COUNT
         LDBD R56,R10          ! GOTO/GOSUB TOKEN
ONLP1    POMD R65,+R10         !
         CMB  R65,R56          ! CIF GOTO/GOSUB
         JNZ  INVAL            ! JIF NO
         DCM  R45              !
         JNZ  ONLP1            ! JIF NOT THE ONE
         LDM  R36,R10          ! SAVE NEXT ADDR
         PUMD R65,-R10         ! RESTORE R10
ONLP2    POMD R65,+R36         ! POP NEXT
         CMB  R65,R56          ! GOTO/GOSUB
         JZR  ONLP2            ! JIF YES
         PUMD R65,-R36         ! RESTORE R36
         STMD R36,=ONFLAG      ! STORE RETURN ADDR
         RTN                   !
!
INVAL    JSB  =ERROR+          !
         BYT  11D              ! JUMP OUT OF RANGE
!
! *******************************************************************
! UNFORMATTED PRINT 02-17-77
! *******************************************************************
!
! *******************************************************************
! "CRT IS" RUNTIME
! *******************************************************************
         BYT  241              !
DISP.    LDMD R40,=CS.C.       ! SET 'CRT IS' SELECT CODE
!
! THE FOLLOWING DOES "LDM R50,=" OF THE FOLLOWING 4 ADDRESSES
!
         DRP  R50              !
         BYT  251              ! LDM
         DEF  DISBUF           !
         DEF  DISPTR           !
         DEF  DSFLAG           !
         DEF  DISPLN           !
         JMP  DOCOM            ! SET THE FLAG
!
! *******************************************************************
! "PRINTER IS" RUNTIME
! *******************************************************************
         BYT  241              !
PRINT.   LDMD R40,=PS.C.       ! SET 'PRINTER IS' S.C.
!
! THE FOLLOWING DOES "LDM R50,=" OF THE FOLLOWING 4 ADDRESSES
!
PRIN.+   DRP  R50              ! SET POINTERS
         BYT  251              ! LDM
         DEF  PRTBUF           !
         DEF  PRTPTR           !
         DEF  PRFLAG           !
         DEF  PRNTLN           !
DOCOM    STMD R#,=P.BUFF       ! DO COMMON STUFF
         CLB  R#               !
         STBD R#,=USING?       ! CLEAR USING!!
         ICB  R#               !
         STBI R#,=P.FLAG       ! SET FLAG
         STMD R40,=SCTEMP      ! SET SC FOR TRAFIC COP
         RTN                   !
!
! PRINT LINE ENTRY
!
PRNFMT   CMM  R36,=1,0         ! CHAR COUNT = 1?
         JNZ  NTPRL            ! JIF NOT EOL
         LDBD R34,R26          ! GET CHAR FROM BUFFER
         CMB  R34,=15          ! IS IT CR?
         JNZ  NTPRL            ! JIF NO
         GTO PEOL              ! GTO 70355 (PEOL)
!
NTPRL    LDMI R22,=P.PTR       !
         JZR  NOTOVR           ! JIF BUFFER EMPTY
         ADM  R36,R22          ! CHAR COUNT + P.PTR
         CLM  R34              !
         LDBI R34,=LINELN      ! DEVICE LINE LENGTH
         CMM  R34,R36          ! LINELN-(PRTPTR+BYTES)
         JPS  NOTOVR           ! JIF IT WILL FIT
         LDBD R77,=USING?      ! USING FLAG SET?
         JNZ  NOTOVR           ! JIF YES
         JSB  =WRTLIN          ! GO WRITE IT
         LDM  R36,R54          ! NUMBER OF BYTES
NOTOVR   LDMI R30,=P.PTR       !
         ADMD R30,=P.BUFF      ! CURRENT LOCATION
         LDBI R22,=P.PTR       ! CURRENT POINTER
         TSM  R54              !
         JZR  MOVEDN           ! JIF NONE TO MOVE
MVLUP    POBD R36,+R26         ! GET FROM BUFFER
         PUBD R36,+R30         ! PUSH INTO PRINT BUFFER
         ICB  R22              ! INC PTR
         JSB  =TSTEOL          ! END OF LINE?
MVCKD    DCM  R54              ! DEC COUNT
         JNZ  MVLUP            ! JIF SOME LEFT
         JSB  =TSTEOL          ! CIF AT EOL
         TSB  R22              ! AT BEGINNING OF LINE?
         JZR  PRFEX            ! JIF YES
         LDB  R36,R22          !
ZNTST    SBB  R36,=25          ! 25 = ZONELN
         JZR  PRFEX            ! JIF BEGIN ZONE
         JPS  ZNTST            ! LOOP IF NOT CURRENT ZONE
MOVEDN   TSB  R20              ! SEMI?
         JNZ  PRFEX            ! JIF YES
! ELSE STEP TO NEXT ZONE
         LDB  R36,R22          ! ELSE STEP TO NEXT ZONE
NXLOOP   SBB  R36,=25          ! ZONELN
         JPS  NXLOOP           ! LOOP IF NOT THIS ZONE
         TCB  R36              ! MAKE IT POSITIVE
         LDB  R76,=40          ! LOAD A BLANK
         CLB  R23              ! FOR MULTI OP
NXLOP1   LDMD R2,=P.BUFF       ! BUFFER PTR
         ADM  R2,R22           ! CURRENT PTR
         STBD R76,R2           ! MOVE BLANK
         JSB  =TSTEOL          ! SEE IF EOL
         JZR  NXZRTN           ! JIF YES
         ICB  R22              ! INCREMENT CURRENT PTR
         DCB  R36              ! DEC COUNT
         JNZ  NXLOP1           ! LOOP IF NOT DONE
         JSB  =TSTEOL          !
PRFEX    STBI R22,=P.PTR       ! STORE NEW VALUE
         RTN                   !
!
TSTEOL   LDBI R2,=LINELN       !
         CMB  R22,R2           !
         JNC  NXZRTN           ! JIF NOT EOL
BUFF     JSB  =WRTLIN          !
NXZRTN   RTN                   !
!
PEOL     LDBI R22,=P.PTR       !
         JNZ  BUFF             ! JIF BUFF NOT EMPTY
         LDB  R60,=40          ! 'SPACE' CHAR
         STBI R60,=P.BUFF      !
         LDBI R22,=P.FLAG      !
         JZR  CLEAN            ! JIF ALREADY PRINTED
         JMP  BUFF             !
!
! *******************************************************************
! PRINT EOL RUNTIME
! *******************************************************************
         BYT  35               ! PRINT EOL ATTRIBUTES
PRLINE   BIN                   ! DUMP THE PRINT BUFFER
         LDBD R54,=SCT+7       ! INTERCEPT FOR TAPE?
         CMB  R54,=377         !
         JNZ  PRLIN1           ! JIF NOT TAPE
         TSB  R16              ! CALC MODE?
         JEV  BUFFEX           ! EXIT IF NO
         JSB  =BUFDMP          ! DUMP BUFFERS
BUFFEX   RTN                   !
!
PRLIN1   LDBD R22,=USING?      !
         JZR  PRLIN2           ! JIF NOT USING
         PUMD R10,+R6          ! SAVE R10
         LDMD R10,=IMCADR      ! CURRENT IMAGE ADDR
         LDMD R30,=IMCLEN      ! CURRENT LENGTH
         LDMD R36,=IMSADR      ! FWA IMAGE
         CMM  R36,R10          ! AT BEGIN OF IMAGE
         JNZ  PRLIN3           ! JIF NO
         LDBI R22,=P.FLAG      ! FIRST PRINT TOKEN?
         JZR  PRLN2-           ! JIF NO
PRLIN3   JSB  =SCANLX          !
PRLN2-   POMD R10,-R6          ! RESTORE R10
PRLIN2   CLM  R54              !
         ICM  R54              ! BYTE COUNT FOR REMEM
         JSB  =RESMEM          !
         JEN  CLEAN            ! JIF NO ROOM
         LDB  R36,=15          ! LOAD EOL CHAR AND STORE IT TO BUFFER
         STBD R36,R26          !
         JSB  =TRAFIC          ! DUMP IT
CLEAN    LDMD R12,=TOS         ! RESET R12
         JSB  =RELMEM          ! RELEASE MEMORY
         RTN                   !
!
WRTLIN   PUMD R26,+R6          ! SAVE R26
         PUMD R54,+R6          ! SAVE CHARACTER COUNT
         CLM  R36              !
         LDB  R36,R22          !
         LDMD R26,=P.BUFF      !
         JSB  =DRV12.          ! SEND THE MESSAGE
         LDMD R30,=P.BUFF      ! AND POWER UP CRT
         POMD R54,-R6          ! RESTORE COUNT
         POMD R26,-R6          ! RESTORE R26
         CLM  R22              !
         STBI R22,=P.FLAG      ! CLEAR FLAG
         STMI R22,=P.PTR       ! RESET PRINTER POINTER
         RTN                   !
!
! *******************************************************************
! PRINT/DISP USING IMAGE STUFF
! *******************************************************************
!
! *******************************************************************
! 'USING' RUNTIME
! *******************************************************************
         BYT  41               !
USING.   BIN                   ! USING
         POMD R74,-R12         ! LINE# OR STR ADDR
! CAPASM: unreferenced label inserted because a DRP command is in the ROM
UNREF0   STM  R74,R70          ! START AND CURRENT
         STMD R70,=IKSLEN      ! STORE EM
         LDB  R77,=177         !
         STBD R77,=USING?      ! SET USING FLAG
         RTN                   !
!
! *******************************************************************
! "USING #" RUNTIME
! *******************************************************************
         BYT  27               !
ULIN#.   BIN                   ! USING LINE #
         POMD R36,+R10         ! POINTER TO IAMGE LINE
         ADMD R36,=FWCURR      ! MAKE IT ABSOLUTE
         POMD R63,+R36         ! LINE##BYTE IMTOK STRTOK
         CLM  R74              !
         POBD R74,+R36         ! STR LEN
         CMB  R66,=216         !
         JNZ  USERR            ! JIF NOT IMAGE
         LDM  R76,R36          ! STR ADDR
         JMP  USEXIT           !
!
! *******************************************************************
! "PRINT STRING, " RUNTIME
! *******************************************************************
         BYT  36               !
COMMA$   LDBD R20,=USING?      ! SEMI IF USING/ELSE COMMA
         JMP  STR              !
!
! *******************************************************************
! "PRINT STRING; " RUNTIME
! *******************************************************************
         BYT  36               !
SEMIC$   CLB  R20              ! PRINT A STRING FOLLOWED BY SEMICOLON
         ICB  R20              ! STRING FLAG
STR      POMD R44,-R12         ! STR ADDR/LEN
         JSB  =TAPTST          ! INTERCEPT FOR TAPE?
         JNZ  NOTTAP           ! JIF NOT
         GTO PRNT#$            ! GTO A30576
!
NOTTAP   JSB  =CALSCN          ! SAVE REG AND SCAN
         JCY  P$RTN            ! EXIT IF ERRORS
         BIN                   !
         TSM  R54              !
         JNZ  DUFMT            ! JIF NOT DEFAULT FMT
         LDM  R54,R44          ! LEN =
         CLM  R56              !
         TSM  R54              !
         JZR  COMRTN           ! JIF NULL STRING
         DCB  R73              ! STRING FORMAT
DUFMT    TSB  R73              !
         JPS  FMTER1           ! JIF NOT STR FORMAT
         JSB  =RESFIL          ! RESERVE AND BLANK FILL
         JEN  P$RTN            ! JIF OUT OF MEM
         LDM  R24,R46          ! STR ADDR
         LDM  R22,R44          ! BYTES
         CMM  R22,R54          ! DATA > IMAGE ?
         JNC  FUFMT1           ! JIF NO
         LDM  R22,R54          ! ELSE TRUNCATE
         STM  R22,R44          !
FUFMT1   JSB  =MOVUP           ! COPY STRING INTO BUFFER
         SBM  R26,R44          ! RESERVE R26
COMRTN   JSB  =TRAFIC          ! CALL TRAFFIC COP
P$RTN    CLB  R22              ! SET FLAG
         STBI R22,=P.FLAG      ! SET FLAG
         RTN                   !
!
USERR    JMP  FMTER1           !
!
! *******************************************************************
! "PRINT NUMBER," RUNTIME
! *******************************************************************
         BYT  36               !
COMMA.   LDBD R20,=USING?      ! SEMI IF USING ELSE COMMA
         JMP  TSTUS            !
!
! *******************************************************************
! "PRINT NUMBER;" RUNTIME
! *******************************************************************
         BYT  36               !
SEMIC.   CLB  R20              ! PRINT A NUMBER FOLLOWED BY A SEMICOLON
         ICB  R20              ! STR FLAG
TSTUS    JSB  =ONER            ! GET REAL VALUE
         JSB  =TAPTST          ! CIF TAPE
         JNZ  TAP-NO           ! JIF NO
         GTO PRNT#N            ! GTO A31022: PRNT#N
!
CALSCN   PUMD R40,+R6          ! SAVE IT
         PUMD R10,+R6          ! SAVE R10
         PUMD R20,+R6          ! SAVE R20
         JSB  =SCANN           ! GO SCAN IMAGE
! R54 MUST CONTAIN CHR COUNT AND R23 = 3 FOR BLANK FILL
         POMD R20,-R6          ! RESTORE R20
         POMD R10,-R6          ! RESTORE R10
         POMD R40,-R6          ! RESTORE NUMBER
         CMB  R17,=300         ! ERRORS?
         RTN                   ! DONE
!
TAP-NO   JSB  =CALSCN          ! SAVE REG AND SCAN
         JCY  P$RTN            ! EXIT IF ERRORS
         TSM  R54              !
         JNZ  UFMT             ! JIF NOT DEFAULT
KFMT     JSB  =ARITH           !
         BIN                   !
         TSB  R70              ! TEST SIGN
         JNG  KFMT1            ! JIF K FORMAT
         ICM  R54              ! ONE TRAILING SPACE
KFMT1    CLM  R66              !
UFMT     TSB  R73              !
         JNG  FMTER1           ! NOT ARITH FORMAT
         JSB  =RESFIL          ! RESERVE AND ZERO FILL
         JEN  P$RTN            ! JIF OUT OF MEM
         JSB  =FORMN           !
         JMP  COMRTN           !
!
FMTER1   JSB  =ERROR+          ! ERROR 53: PRINT USING
         BYT  53D              ! PRINT USING
!
RESFIL   JSB  =RESMEM          ! RESERVE MEMORY
         JEN  RESRTN           ! JIF MEM OVFLO
RESFL1   LDM  R36,R26          ! FWA
         LDB  R23,=3           ! TO BLANK FILL
         LDM  R56,R54          ! BYTE COUNT
         BIN                   !
         PUMD R66,+R6          ! SAVE R66
         PUMD R70,+R6          ! SAVE R70
         JSB  =ZROMEM          ! GO BLANK FILL
         POMD R70,-R6          ! RESTORE R70
         POMD R66,-R6          ! RESTORE R66
RESRTN   RTN                   !
!
CVNUM    CLB  R70              ! FORMAT A REAL # TO ASCII FOR OUTPUT
         DCB  R70              ! SIGN FLAG NEG
         STM  R30,R26          !
         JSB  =ARITH           !
FORMN+   JSB  =RESFL1          ! FORMAT NUMBER
         CLM  R66              ! NO C OR P
FORMN    TSB  R72              ! I/O IMAGE?
         JPS  FORMNC           ! JIF NO
         LDM  R2,=3,0          ! TELL EM WHAT WE EXPECT
         JSB  =IMERR           !
         RTN                   !
!
FORMNC   BCD                   !
         PUMD R54,+R6          ! SAVE LEN
         PUMD R24,+R6          ! SAVE R24
         PUMD R66,+R6          !
         JSB  =SEP10           !
         JSB  =ROUND           !
         TSB  R73              !
         JNZ  FRMN1            ! JIF E FORMAT
         JSB  =INFR4           !
         LDM  R36,R34          ! EXP TO 36
FRMN1    LDM  R30,R26          !
         POMD R66,-R6          ! RESTORE C/P COUNT
         JSB  =OUTC/P          ! GO OUTPUT THEM
         JSB  =SIGNN           !
         JSB  =LDIGIT          !
         JSB  =RADIX           ! HANDLE REST OF NUMBER
         JSB  =RDIGIT          !
         JSB  =EFORM           !
         POMD R24,-R6          ! RESTORE BYTE CNT
         BIN                   !
         POMD R54,-R6          ! RESTORE COUNT
! DECR COUNT BY R2 SET IN EFORM
         CLM  R74              !
         LDB  R74,R2           !
         SBM  R54,R74          !
         RTN                   !
!
! ARITH/CVNUM
! ENTRY: R40 = VAL
! EXIT: REGS SET AS IN SCANN
!
ARITH    LDB  R71,=4           ! SET FILL AS 0'S
         CLM  R72              !
         LDB  R72,=56          ! PERIOD
         LDM  R36,R40          ! GET EXPONENT AND SIGN
         STM  R36,R34          ! DUP IT
         BCD                   !
         LRB  R37              ! TRASH THE SIGN
         LDM  R62,R42          ! COPY MANTISSA
         JNZ  TSEXP            ! JIF NON ZERO
         ICM  R76              ! CHARS LEFT = 1
         JMP  INT?             ! JMP TO SETUP EXIT
!
TSEXP    CMB  R37,=5           !
         JPS  NGEXP            ! JIF NEG EXPONENT
         CMM  R36,=12C,0C      ! CMP 12 (DEC)
         JPS  NR3              ! JIF EXP > 11
         LDB  R76,R36          !
         ICM  R76              !
NR12     JSB  =CHRRT           !
INT?     LDM  R36,R74          ! CHARS RIGHT
         JNZ  SETCNT           ! SET UP RETURN
         CLB  R72              !
SETCNT   LDM  R56,R74          ! CHARS RIGHT
         ADM  R56,R76          ! PLUS CHARS LEFT
         TSB  R70              ! TEST SIGN
         JNG  INCS?            !
         JNZ  INCS             ! GO INC IF # 0
INCS?    TSB  R41              !
         JRZ  NOINCS           ! JIF POS
INCS     ICM  R56              !
NOINCS   TSB  R72              !
         JZR  NODEC            ! JIF NO DECIMAL
         ICM  R56              ! +DEC
NODEC    TSB  R73              !
         JZR  ARDON+           ! JIF NOT E
         ADM  R56,=5,0         ! FOR EXP
ARDON+   STM  R56,R54          !
         CLM  R56              !
ARDON    PUMD R70,+R6          !
         PUMD R66,+R6          ! SAVE C/P COUNT
         CLM  R60              !
         LDB  R60,=7           !
         LDM  R64,R54          !
         JSB  =CONINT          ! CONVERT TO BIN
         CLM  R54              !
         STM  R76,R54          !
         POMD R66,-R6          ! RESTORE C/P COUNT
         POMD R70,-R6          !
         RTN                   !
!
NR3      LDM  R62,R42          ! MATISSA AGAIN
         ICM  R76              ! CHR LT = 1
         JSB  =CHRRT           !
         LDB  R73,=2           ! E=2
         JMP  SETCNT           !
!
NGEXP    NCM  R36              ! MAKE EXP POS
         ANM  R37,=17          ! #LEAD ZEROS TO BRING
         TSM  R36              !
MVAGN    JZR  NR12             ! JIF NONE
         LRM  R67              !
         TSB  R61              !
         JLN  NR3              ! JIF SHIFTED OUT NON-ZERO
         DCM  R36              !
         JMP  MVAGN            !
!
CHRRT    LDM  R34,=12C,0C      ! MAX CHARS RIGHT = 12 DEC
         SBM  R34,R76          ! MAX RIGHT - LEFT = MAX
         JZR  CHRTEX           ! JIF ZERO
SHFAGN   TSB  R62              !
         JRN  CHRTEX           ! JIF NEXT DIGIT # 0
         LRM  R67              !
         DCM  R34              !
         JNZ  SHFAGN           !
CHRTEX   STM  R34,R74          ! SAVE CHARS RIGHT
         RTN                   !
!
! SCANN - SCAN FOR FORMAT ITEM
!
! ENTRY
!   R10 - CURRENT IMAGE POINTER
!   R30 - CHAR IN IMAGE
! EXIT
!   R54 - CHAR CNT (=0 IF DEFAULT FORMAT)
!   R70 - SIGN
!        -1 - IF NEG ELSE NULL
!         0 - IN DIG LEFT IF NEG ELSE NULL
!         1 S - IF NEG ELSE + (DEFAULT)
!         2 M - IF NEG ELSE BLANK
!   R71 - FILL
!        -1 DEFAULT
!         0 DZ
!         1 D
!         2 *Z
!         3 *
!         4 Z
!   R72 - DECIMAL (ZERO,COMMA,OR PERIOD)
!   R73 - E FORMAT/A FORMAT
!        -1 A
!         0 NONE
!         1 E FORMAT (IMAGE)
!         2 E FORMAT (SUPPRESS +,-,AND LEAD ZERO)
!   R74 - CHR RT
!   R76 CHR LT
!   R66 - C/P COUNT
!
SCANN    BIN                   ! SCAN FOR FORMAT ITEM
         CLM  R54              ! clear character count
         LDBD R46,=USING?      ! get USING flag
         JNZ  SCANUS           ! jif USING
         CLM  R70              ! clear SCANN flags
         LDB  R70,=2           ! sign (M)
         RTN                   !
!
SCANUS   JSB  =SCANL           ! GET PAST LEADING GARBAGE
         CLM  R66              ! C/P COUNT
         CLM  R70              ! SCANN FLAGS
         DCB  R71              ! DEFAULT FILL
         CLM  R54              !
         JEN  SCANL1           ! JIF NOT WRAPAROUND
         JMP  FMTER2           ! ELSE ERROR
!
SCANLP   JSB  =GETREP          ! GET REPLICATION
SCANL1   JSB  =FCHAR+          ! GET CHR FLAG
         LLM  R36              ! TIMES 2
         LDMD R36,X36,TYTAB    ! ADDRESS
         JSB  X36,ZRO          ! GO DO IT
         CMB  R17,=300         ! ERRORS?
         JNC  SCANLP           ! LOOP IF NO
         RTN                   ! ELSE EXIT
!
TYTAB    DEF  IMERR?           !  0 END
         DEF  STRNG            !  1 A
         DEF  ZEE              !  2 Z
         DEF  STARR            !  3 *
         DEF  DEE              !  4 D
         DEF  RADX             !  5 .
         DEF  RADXR            !  6 R
         DEF  SIGNF            !  7 S
         DEF  SIGNF            ! 10 M
         DEF  SEP              ! 10 C
         DEF  SEPS             ! 11 P
         DEF  EEE              ! 11 E
         DEF  KAA              ! 12 K
         DEF  IMERR?           ! 13 ILLEGAL OR SEP
!
ZEE      LDB  R32,=4           ! FILL CODE
         TSB  R71              !
         JNG  SFILL            ! JIF NO FILL CHR YET
         CMB  R71,R32          !
         JZR  SFILL1           ! JIF FILL TYPE 4
         DCM  R44              !
         JNZ  FMTER2           ! ERROR IF CNT # 1
         ICM  R44              !
         CMB  R20,=56          !
         JZR  DCFILL           ! JIF NEXT
         CMB  R20,=122         ! R?
         JZR  DCFILL           ! JIF R
         JSB  =CKSEP           ! CIF SEPARATOR
         JEZ  FMTER2           ! JIF NOT
         JSB  =DCFILL          ! GO UPDATE COUNT
         GTO DONE?             ! AND EXIT SINCE SEP
!
DCFILL   DCB  R71              !
         JMP  SFILL1           !
!
SFILL    LDB  R#,R32           ! FILL TO R71
SFILL1   TSB  R72              !
         JNZ  FMTER2           ! JIF DECIMAL SEEN
CHRAD-   BCD                   !
         ADM  R76,R44          ! CHR LT + REPL
CHRAD    ADM  R54,R44          ! CHR + REPL
CHRADX   RTN                   !
!
STARR    LDB  R32,=3           ! FILL CODE
STAR1    TSB  R71              !
         JNG  SFILL            ! JIF FILL NEG
         CMB  R71,R32          ! FILL MATCH?
         JZR  SFILL1           ! JIF YES
FMTER2   JMP  FMTERR           !
!
DEE      LDB  R32,=1           ! FILL
         TSB  R72              !
         JZR  STAR1            ! JIF NO DECIMAL
         BCD                   !
         ADM  R74,R44          ! CHR RT + REPL
         JMP  CHRAD            ! GO ADD CHRS
!
RADXR    LDB  R14,=54          ! COMMA
RADX     TSB  R72              !
         JNZ  FMTERR           ! JIF DECIMAL SEEN
         LDB  R72,R14          ! SET . OR COMMA
CREP1    BCD                   !
         DCM  R44              !
         JNZ  FMTERR           ! JIF REPL # 1
         ICM  R44              !
         JMP  CHRAD            ! GO ADD CHRS
!
SIGNF    TSB  R70              !
         JNZ  FMTERR           ! JIF SIGN SEEN
         TSM  R54              !
         JNZ  FMTERR           ! JIF NOT FIRST CHAR
         CMB  R14,=123         !
         JZR  INC1             ! JIF S
         ICB  R70              !
INC1     ICB  R70              !
         JMP  CREP1            !
!
SEPS     JSB  =SEP1            ! GO CONVERT TO BIN
         TCM  R34              ! NEG TO FLAG PERIOD
         JMP  SEP2             ! GO FINISH UP
!
SEP      JSB  =SEP1            ! GO CONV TO BIN
SEP2     PUMD R34,+R12         ! PUSH CHR CNT
         ICM  R66              ! C/P CNT
         TSM  R76              ! CHR LT 0?
         JZR  FMTERR           ! ERROR IF SO
         JMP  CREP1            !
!
SEP1     PUMD R54,+R6          ! SAVE 54
         JSB  =ARDON           ! GO CONVERT
         LDM  R34,R54          ! RESULT TO 34
         POMD R54,-R6          ! RESETORE 54
         BIN                   !
SPRTN    RTN                   ! AND EXIT
!
EEE      TSB  R73              !
         JNZ  FMTERR           ! JIF E OR A SEEN
         ICB  R73              !
         BCD                   !
         DCM  R44              !
         JNZ  FMTERR           ! JIF REPL # 1
         LDB  R44,=5           ! REPL = 4
         JMP  CHRAD            !
!
KAA      DCB  R70              !
         BCD                   !
         TSM  R54              !
         JNZ  FMTERR           ! JIF CHR CNT # 0
         DCM  R44              !
         JNZ  FMTERR           ! JIF REPL # 1
         RTN                   !
!
IMERR?   JSB  =CKSEP           ! CIF SEPARATOR
         JEZ  CKCLO            ! JIF NOT SEP
         DCM  R44              !
         JZR  DONE?            ! JIF REPL = 1
!
FMTERR   JSB  =ERROR+          !
         BYT  52D              !
!
CKCLO    CMB  R20,=51          ! CLOSE
         JZR  CLSFND           ! Change 8/23/78
         CLM  R2               !
         ICM  R2               !
         ICM  R2               ! TELL EM WHAT WE EXPECT
         JSB  =IMERR           !
         TSM  R2               ! FOUND SEP
         JNG  CKCLOR           ! JIF YES
!
         JSB  =ERROR           !
         BYT  52D              !
!
CKCLOR   DCM  R6               !
         DCM  R6               ! TRASH 1 RETURN
         RTN                   !
!
CLSFND   DCM  R10              ! SO SCANL SEES )
         ICM  R30              ! MAKE COUNT RIGHT
DONE?    STMD R30,=IMCLEN      ! CURRENT IMAGE LEN
         STMD R10,=IMCADR      ! CURRENT IMAGE ADDR
         JSB  =ARDON           ! CONVERT TO BIN IN 54
         JMP  CKCLOR           !
!
STRNG    TSB  R73              !
         JNZ  FMTERR           ! JIF E OR A SEEN
         DCB  R73              ! SET A FORMAT
         GTO CHRAD             ! GO STORE COUNT IN 54
!
! *******************************************************************
! SCANL - SCAN LEADING GARBAGE
! ENTRY
!   R65 - ACTIVE REPL CNT
!   R10 - CURRENT IMAGE POINTER
!   R30 - CHAR IN IMAGE
!   R20 - NEXT CHAR
! EXIT
!   R10 - CURRENT IMAGE POINTER
!   R30 - CHAR IN IMAGE
! *******************************************************************
LTABL    BYT  130,42,50,51,57  ! ASCII X"()/
!
SCANL    LDMD R10,=IMCADR      ! IMAGE ADDR
         STM  R10,R36          ! SAVE START
         LDMD R30,=IMCLEN      ! IMAGE LEN
SCANLX   BIN                   !
         STMD R36,=IMWADR      ! WRAP ADDRESS
SCNLGO   JSB  =GCHAR#          !
         JEZ  SCANLS           ! JIF END
SCANLR   JSB  =WTEST           ! CHECK WRAP
         JSB  =GETREP          ! GET REPLICATION
         LDM  R34,=LTABL       !
         LDM  R24,=6,0         !
         JSB  =FCHAR           !
         JEN  PROCHR           ! JIF FOUND
SCANLS   JSB  =WTEST           ! TEST WRAP
         JSB  =CKSEP           !
         JEZ  SCLRT+           ! JIF NOT SEP
         JSB  =WTEST           ! TEST WRAP
         JMP  SCNLGO           ! AND LOOP
!
SCLRT+   CLM  R2               ! TELL EM WAHT WE EXPECT
         JSB  =IMERR           !
         TSM  R2               !
         JNG  SCANLR           ! JIF HE FOUND ONE
         ICE                   ! CELAR WRAPAROUND
SCLRTX   RTN                   !
!
FMTER4   JMP  FMTERR           !
!
WTEST    CLE                   !
         BIN                   !
         TSM  R30              !
         JPS  SCLRTX           ! JIF COUNT POS
         LDMD R2,=IMWADR       ! WRAP ADDR
         CMMD R2,=IMSADR       ! =START ADDR?
         JNZ  SCLRTX           ! RETURN IF NO WRAP
         JMP  CKCLOR           !
!
PROCHR   LLM  R36              !
         LDMD R36,X36,LJTAB    !
         JSB  X36,ZRO          ! GO DO IT
         CMB  R17,=300         ! ERRORS?
         JNC  SCANLR           ! LOOP IF NO ERRORS
         RTN                   ! ELSE EXIT
!
FMTER3   JMP  FMTER4           !
!
LJTAB    DEF  FMTER4           !
         DEF  EX               ! X
         DEF  QLIT             ! "
         DEF  LTBRAC           ! (
         DEF  RTBRAC           ! )
         DEF  SENDCR           ! /
!
RTBRAC   LDBD R65,=USING?      !
         JPS  FMTER4           ! JIF REPL CNT 0
         PUMD R52,+R6          ! SAVE 52
         POMD R52,-R12         ! POP CURRENT REPL
         BCD                   !
         DCM  R56              ! DECR COUNT
         BIN                   !
         JNZ  RSET             ! JIF NOT DONE THIS REPL
         DCB  R65              !
RTBREX   STBD R#,=USING?       ! UPDATE REPL COUNT
RTBRX1   POMD R52,-R6          ! RESTORE R52
         RTN                   !
!
RSET     PUMD R52,+R12         ! PUSH IT BACK
         LDM  R30,R54          ! CHR CNT
         LDM  R10,R52          !
         JSB  =GCHAR#          ! GET FIRST CHAR
         JMP  RTBRX1           !
!
LTBRAC   PUMD R52,+R6          ! SAVE R52
         DCM  R10              ! MAKE IT RIGHT
         STM  R10,R52          ! IMAGE POINTER
         ICM  R10              ! RESET R10
         ICM  R30              ! ADJUST COUNT
         STM  R30,R54          ! CHAR CNT
         DCM  R30              ! RESET R30
         LDM  R56,R44          ! REPL
         PUMD R52,+R12         !
         LDBD R65,=USING?      !
         ICB  R65              ! INCREMENT REPL COUNT
         JZR  FMTER3           ! EXIT IF TOO MANY
         JMP  RTBREX           !
!
QLIT     PUMD R10,+R12         ! SAVE START
QLCOM    CMB  R20,=42          !
         JZR  QMOV             ! JIF END QUOTE
         JSB  =GCHAR-          ! NEXT NON BLANK CHAR
         JEZ  FMTER3           ! JIF NONE
         JMP  QLCOM            ! LOOP
!
QMOV     POMD R26,-R12         ! STARTING
         DCM  R26              !
         LDM  R22,R10          !
         SBM  R22,R26          ! BYTE COUNT
         DCM  R22              !
         STM  R22,R54          !
         CLM  R56              !
         JSB  =GCHAR#          ! GET NEXT CHAR
SPECOT   PUMD R30,+R12         ! SAVE FOR NEXT TIME
         PUMD R10,+R12         !
         JSB  =TRAFIC          !
         POMD R10,-R12         !
         POMD R30,-R12         !
         RTN                   !
!
EX       LDM  R55,R44          ! REPL(BCD)
         LDB  R54,=377         ! FLAG
         PUMD R50,+R12         !
         JSB  =ONEB            ! CONV TO BIN INT
         CLM  R54              !
         STM  R46,R54          ! BIN INT
         CLM  R76              !
         JSB  =RESFIL          ! GO RESERVE AND FILL
         JEN  SC12RT           ! JIF OUT OF MEM
         JMP  SPECOT           !
!
SENDCR   LDB  R21,=15          ! CR
SENDCC   JSB  =SC12?           ! SELECT CODE 1 OR 2?
         JEZ  NTSTD            ! JIF NOT SC 1 OR 2
         LDBI R36,=P.PTR       !
         JNZ  SENDC1           ! JIF BUFF NOT EMPTY
SENDC2   CMB  R17,=300         ! ERRORS?
         JCY  SC12RT           ! EXIT IF SO
         CLB  R36              !
         ICB  R36              !
         STBI R36,=P.PTR       ! BUFF CNT = 1
         LDB  R36,=40          !
         STBI R36,=P.BUFF      ! BLANK CHAR
SENDC1   PUMD R44,+R6          ! SAVE REPL
         CLM  R54              !
         ICM  R54              !
         JSB  =RESMEM          !
         JEN  SENDCL           ! JIF OUT OF MEM
         STBD R21,R26          !
         JSB  =SPECOT          !
SENDCL   POMD R44,-R6          ! GET REPL
         BCD                   !
         DCM  R44              !
         JNZ  SENDC2           ! LOOP IF MORE TO SEND
         RTN                   !
!
NTSTD    LDM  R54,R44          ! REPL
         JSB  =RESMEM          !
         JEN  SC12RT           ! JIF OUT OF MEM
         BCD                   !
         STM  R26,R36          ! SAVE ADDR
NTSTL    PUBD R21,+R36         !
         DCM  R44              ! DEC COUNT
         JNZ  NTSTL            ! LOOP IF MORE
         JMP  SPECOT           !
!
SC12?    PUMD R40,+R6          ! PROTECT R40
         JSB  =COPSUB          ! GET SELECT CODE
         CLE                   ! FALSE FLAG
         JZR  POPR40           ! JIF IO
         ICE                   ! TRUE FLAG
POPR40   POMD R40,-R6          ! RESTORE R40
SC12RT   RTN                   !
! *******************************************************************
! FCHAR - IDENTIFY FRMAT CHAR
! ENTRY
!   R10 - IMAGE POINTER
!   R20 - NEXT CHAR
!   R30 - CHAR IN IMAGE
!   R44 - REPL
! EXIT
!   R10 - IMAGE POINTER
!   R20 - NEXT CHAR
!   R30 - CHAR IN IMAGE
!   R44 - REPL
!   R14 - CHAR
!   R36 - CHAR FLAG
! *******************************************************************
!
CTABL    ASC  "AZ*D.RSMCPEK"   !
!
FCHAR+   LDM  R34,=CTABL       !
         LDM  R24,=15,0        !
! RETURNS E=0 IF NOT FOUND
FCHAR    BIN                   !
         CLE                   ! SET NOT FOUND
         CLM  R36              !
         TSM  R30              ! BYTES REMAINING
         JNG  FCRTN            !
         STB  R20,R14          ! CHAR TO 14
         CMB  R20,=54          !
         JZR  FCRTN            ! EXIT IF SEP
         JSB  =IDCHAR          ! GO IDENTIFY CHAR
         JEZ  FCRTN            ! JIF NOT FOUND
         JSB  =GCHAR-          ! NEXT CHAR
         JEZ  FCRT1            ! JIF NO MORE
! DONT REPEAT () OR "
         CMB  R14,=50          ! OPEN (
         JZR  FCRTN            !
         CMB  R14,=51          ! CLOSE )
         JZR  FCRTN            !
         CMB  R14,=42          ! QUOTE "
         JZR  FCRTN            !
         CMB  R20,=40          ! BLANK SPACE
         JNZ  TSTRP1           ! JIF NOT BLANK
TSTRP    JSB  =GCHAR#          ! NEXT NON BLANK
         JEZ  FCRT1            ! JIF NO MORE
TSTRP1   CMB  R14,R20          !
         JNZ  FCRTN            ! JIF NO MATCH
         BCD                   !
         ICM  R44              ! INCR REPL
         TSM  R46              ! >9999?
         JZR  TSTRP            ! JIF NO
         DCM  R44              ! ELSE RESET
         JMP  TSTRP            ! LOOP
!
FCRT1    ICE                   !
         BIN                   !
FCRTN    RTN                   !
!
! GETREP - GET REPLICATION
!
GETREP   CLM  R44              !
GLOP     BCD                   !
         JSB  =DIGIT           ! DIGIT?
         JEZ  GLOPT            ! JIF NO
         TSB  R45              ! 4 DIGITS
         JLN  GLOPL            ! JIF YES
         ERB  R20              ! TO E
         ELM  R44              ! THEN 44
GLOPL    JSB  =GCHAR#          ! NEXT CHAR
         JMP  GLOP             !
!
GLOPT    TSM  R44              !
         JNZ  FND1             ! JIF NOT ZERO
         ICM  R44              ! ELSE MAKE IT ONE
FND1     BIN                   !
         RTN                   !
!
! IDCHAR - IDENTIFY FMT CHAR
! RETURN E=0 IF NOT FOUND
!
IDCHAR   CLE                   !
         CLM  R36              !
IDCHR1   ICM  R36              !
         CMM  R36,R24          !
         JZR  FCRTR            ! JIF NONE
         POBD R32,+R34         ! NEXT CHAR FROM TABLE
         CMB  R32,R14          ! IS THIS IT????
         JNZ  IDCHR1           ! JIF NOT FOUND
         ICE                   ! SET FOUND
FCRTR    RTN                   !
!
! GCHAR# - GET NEXT NON BLANK CHAR
! GCHAR- - GET NEXT CHAR
!
GCHAR#   JSB  =GCHAR-          ! GET NEXT CHAR
         JEZ  GCRTN            ! JIF NONE
         CMB  R20,=40          !
         JZR  GCHAR#           ! LOOP IF BLANK
         RTN                   !
!
GCHAR-   BIN                   !
         CLE                   !
         DCM  R30              !
         JNG  GCRTN            ! EXIT IF NEG
         POBD R20,+R10         ! GET NEXT CHAR
         ICE                   !
GCRTN    RTN                   !
!
! CKSEP - CHECK FOR SEPARTOR
! RETURN E=0 IF NOT FOUND
!
CKSEP    BIN                   !
         TSM  R30              ! END OF IMAGE?
         JPS  CKRST            ! JIF NO
         LDMD R30,=IKSLEN      ! ELSE RESET TO START
         LDMD R10,=IMSADR      !
CKINC    CLE                   !
         ICE                   ! FOUND SEP FLAG
         RTN                   !
!
CKRTN    CLM  R2               !
         ICM  R2               ! TELL EM WHAT WE EXPECT
         JSB  =IMERR           !
         TSM  R2               !
         JNG  CKINC            ! JIF FOUND ONE
         CLE                   !
         RTN                   !
!
CKRST    CMB  R20,=54          !
         JZR  CKINC            ! JIF COMMA
         CMB  R20,=57          !
         JNZ  CKRTN            ! JIF NOT
SPSEP    DCM  R10              ! BACK UP POINTER
         ICM  R30              ! INC COUNT
         JMP  CKINC            ! SET FLAG AND EXIT
!
! ROUND - ROUND NUMERIC VALUE
! EXP + DIGRT + 1
!    IF NEG OR > 11 THEN EXIT, ELSE
!    SHIFT 5 RT TO POSITION AND ADD
! ENTRY
!   R32 - SIGN
!   R36 - EXP
!   R40 - MANTISSA W/TRAILING ZEROS
!   R74 - CHR RT (BCD)
!
ROUND    TSM  R40              !
         JZR  RNDEX            ! DON'T ROUND ZERO
         CLM  R50              !
         LDB  R57,=120         ! FORM OF .5 (bcd)
         LDM  R34,R36          ! EXPONENT
         ICM  R34              ! EXP+1
         TSB  R73              !
         JZR  NRE              ! JIF NOT E
         LDM  R34,R76          ! DIG LT
NRE      ADM  R34,R74          !  + DIG RT
         JNC  COMPR            ! OK IF NO CARRY
         TSB  R73              !
         JNZ  RNDEX            ! EXIT IF E
         TSB  R37              ! EXP SIGN
         JLZ  RNDEX            ! JIF EXP POS
COMPR    CMM  R34,=12C,0C      ! 12 BCD
         JNC  POS.5L           ! JIF < 12
         RTN                   !
!
POS.5    LRM  R57              !
POS.5L   DCB  R34              !
         JCY  POS.5            !
ADD.5    ADM  R42,R52          !
         JNC  RNDEX            !
         LRM  R47              !
         ADB  R47,=20          !
         ICM  R36              ! INC EXP
RNDEX    RTN                   !
!
! OUTC/P - OUTPUT COMMA/PERIOD SEPARATORS
! ENTRY
!   R30 - BUFFER FWA
!   R66 - C/P COUNT
!   R12 - STACK POINTER
!      C/P CHR POS, C IF POS ELSE P
!
OUTC/P   TSM  R66              !
         JZR  OUTCEX           ! JIF NONE
         BIN                   !
OUTCLP   LDB  R34,=54          !
         POMD R24,-R12         !
         JPS  PUIT             ! JIF COMMA
         TCM  R24              ! MAKE IT POS
         LDB  R34,=56          !
PUIT     ADM  R24,R26          !
         PUBD R34,+R24         !
         DCM  R66              ! DECREMENT CNT
         JNZ  OUTCLP           ! JIF NOT DONE
         BCD                   !
OUTCEX   RTN                   !
!
! LDIGIT - OUTPUT DIGITS LEFT OF DECIMAL
! ENTRY
!   R30 - OUTPUT BUFFER POINTER
!   R76 - DIGITS LEFT
!   R50 - DIGITS JUST RT
!   R36 - EXP
!
LDIGIT   TSB  R73              !
         JZR  LD1              ! JIF NOT E
         LDM  R50,R40          ! VAL TO 52
LD1      TSM  R50              !
         JLN  NORM             ! JIF NORMALIZED
         JNZ  NSHFT            ! JIF NON-0
         TSM  R76              ! DIGITS LEFT?
         JZR  LDEXIT           ! JIF NO ALLOW 0 WITH .DD
         JMP  NORM             ! ELSE DONT NORM ZERO
!
NSHFT    LLM  R50              !
         JLZ  NSHFT            ! JIF NOT NORMALIZED
NORM     LDM  R34,R76          ! CHR LT (BIN)
         TSB  R73              !
         JZR  NOTE             ! JIF NOT E
         SBM  R36,R76          ! EXP - CHR LT
         ICM  R36              ! +1
         JMP  OUTE             !
!
NOTE     LDM  R24,R36          ! EXPONENT
         JLN  FILLIT           ! JIF NEG EXP
SUBIT    SBM  R34,R24          !
         DCM  R34              ! CHRLT - (EXP+1)
FILLIT   TSM  R34              !
         JNG  OVFLO            ! JIF OVERFLOW
         JZR  SETFIL           ! JIF NO LEAD ZEROES
         JSB  =FILL            !
         TSM  R72              ! CIF DONE
         JZR  LDEXIT           ! JIF YES
! LOOKING FOR C OR P
         LDBD R23,R30          ! GET ONE MORE
         CMB  R23,=40          ! BLANK?
         JZR  SETFIL           ! JIF YES
         CMB  R22,=60          ! IS FILL ZEROES?
         JNZ  PUFILL           ! JIF NO
         LDB  R22,R23          ! SAME CHAR READ
PUFILL   PUBD R22,+R30         ! ELSE FILL IT
SETFIL   CMB  R71,=2           ! BLANK FILL?
         JCY  SETFL1           ! JIF NO
         JSB  =SIGNFF          ! GO DO FLOATING SIGN
SETFL1   LDB  R71,=4           ! FILL IS 0'S
         LDM  R34,R36          ! EXP
         JLN  LDEXIT           ! JIF NEG EXP
         CMM  R34,=12C,0C      ! 12 BCD
         JPS  OUTMO            ! JIF EX > 11
         ICM  R34              !
OUTE     TSM  R34              !
         JZR  LDEXIT           ! JIF NONE TO OUTPUT
         JSB  =OUTDIG          ! OUTPUT EXP + 1 DIGITS
         JMP  LDEXIT           !
!
OUTMO    LDM  R34,=12C,0C      ! 12 BCD
         JSB  =OUTDIG          ! OUTPUT 12 DIGITS
         LDM  R34,R36          ! EXP
         ICM  R34              !
         SBM  R34,=12C,0C      ! OUTPUT (EXP+1)-12 0'S
         JSB  =FILL            !
LDEXIT   TSB  R73              !
         JNZ  LDEX1            ! JIF E
         LDM  R50,R40          !
LDEX1    RTN                   !
!
OVFLO    JSB  =ERROR+          ! WARNING: OVERFLOW
         BYT  2                !
!
OUTDIG   LLM  R50              !
         CLB  R22              !
         ELB  R22              !
         BIN                   !
         ADB  R22,=60          ! MAKE IT ASCII
         BCD                   !
         JSB  =OUT1            ! GO OUTPUT ONE DIGIT
         JNZ  OUTDIG           ! LOOP IF NOT DONE
         RTN                   !
!
FILL     LDB  R22,=40          !
         CMB  R71,=2           !
         JNG  TSTZ             ! FILL IS BLANK
         LDB  R22,=52          !
         CMB  R71,=4           !
         JNG  TSTZ             ! FILL IS *
         LDB  R22,=60          ! FILL IS ZERO
TSTZ     DCM  R76              !
         JNZ  OUT1C            ! JIF NOT LAST
         TSB  R71              !
         JOD  OUT1C            ! JIF NOT DZ OR *Z OR Z
         LDB  R22,=60          ! ZERO FILL THIS CHAR
OUT1C    JSB  =OUT1            ! GO OUTPUT ONE DIGIT
         JNZ  TSTZ             ! LOOP IF MORE
         RTN                   !
!
OUT1     LDB  R0,=22           ! CHAR TO OUTPUT (IN R22)
         LDBD R23,R30          ! LOAD NEXT
         CMB  R23,=40          ! BLANK?
         JZR  OUT1X            ! JIF YES
         ICM  R34              ! ELSE DONT COUNT IT
         BIN                   !
         CMB  R22,=40          ! BLANK FILL?
         JZR  OUT1X-           ! JIF BLANK
         CMB  R22,=52          ! * FILL?
         JZR  OUT1X-           ! JIF * FILL
         LDB  R0,=23           ! ELSE PUSH OUT SAME CHAR (IN R23)
OUT1X-   BCD                   !
         JSB  =OUT1X           ! GO DO IT
         JMP  OUT1             ! AND LOOP
!
OUT1X    PUBD R*,+R30          ! PUSH OUT CHAR
         DCM  R34              ! DEC COUNT
         RTN                   !
!
! SIGN - OUTPUT + OR - OR BLANK OR NOTHING
! ENTRY
!   R70 - AS DESCRIBED IN SCANN
!   R32 - SIGN
!   R30 - OUTPUT POINTER
!
SIGNFF   JSB  =SIGNX           ! NOW DO SIGN
         POMD R24,-R30         ! LAST 2 BYTES
         BIN                   !
         CMM  R30,R26          ! CIF WITHIN BOUNDS
         JNC  SIGNFX           ! JIF NOT
         CMB  R24,=60          ! ZERO
         JNZ  SIGNFX           ! JIF NO
         STB  R25,R24          ! SIGN TO 24
         LDB  R25,=60          ! ZERO TO 25
SIGNFX   PUMD R24,+R30         ! RESTORE IT
         CMM  R76,=2,0         ! CIF 2 BYTES LEFT
         JNC  SIGNF1           ! JIF NO
         LDB  R24,=40          !
         CMBD R24,R30          ! NEXT = BLANK?
         JZR  SIGNF1           ! JIF YES
         POBD R25,-R30         ! POP SIGN/FILL
         PUMD R24,+R30         ! OUT WITH LEADING BLANK
SIGNF1   BCD                   !
         RTN                   !
!
SIGNN    TSB  R32              ! SIGN
         JRZ  SIGN1            ! JIF POS
         TSB  R70              ! SIGN REQUESTED?
         JNZ  SIGN1            ! JIF YES
         DCM  R76              ! ELSE DECR DIGITS LEFT
SIGN1    TSB  R73              ! E?
         JNZ  SIGNX            ! JIF YES
         TSB  R71              ! FILL
         JNG  SIGNX            ! JIF DEFAULT FILL
         CMB  R71,=2           ! BLANK FILL
         JNC  SGNEX            ! JIF YES
SIGNX    LDB  R34,=55          !
         TSB  R32              !
         JRN  OUTSGN           ! NEG ,SO OUTPUT IT
         LDB  R34,=53          !
         BIN                   !
         DCB  R70              !
         BCD                   !
         JNG  SGNEX            ! NO SIGN SO EXIT
         JZR  OUTSGN           ! S ,SO OUTPUT +
         LDB  R34,=40          ! SPACE CHAR
OUTSGN   PUBD R34,+R30         ! OUTPUT SIGN
SGNEX    RTN                   !
!
! RADIX - OUTPUT RADIX
! ENTRY
!   R30 - OUTPUT BUFFER POINTER
!   R72 - ZERO,COMMA, OR PERIOD
!
RADIX    TSB  R72              !
         JZR  RADEX            ! JIF ZERO
         PUBD R72,+R30         ! OUTPUT RADIX
RADEX    RTN                   !
!
! RDIGIT - OUTPUT RIGHT DIGITS
! ENTRY
!   R30 - OUTPUT BUFFER POINTER
!   R74 - CHT RT (BCD)
!   R50 - DIGITS JUST LT ZERO FILL
!
RDIGIT   LDB  R71,=4           ! FILL IS ZEROS
         LDM  R76,R74          ! DIGITS RT
         JZR  RDEXIT           ! JIF NONE
         TSB  R73              !
         JNZ  RDLP1            ! JIF E
         LDM  R34,R36          ! EXP
         JLZ  RDLP1            ! JIF EXP POS
         NCM  R34              !
         CMM  R34,R76          !
         JNC  RDLP2            ! JIF EXP < RDIGIT
         LDM  R34,R76          ! MAX FILL
RDLP2    TSM  R#               !
         JZR  RDLP1            ! JIF NO FILL
         JSB  =FILL            !
RDLP1    LDM  R34,R76          !
         JZR  RDEXIT           ! JIF NONE LEFT
         JSB  =OUTDIG          !
RDEXIT   RTN                   !
!
! EFORM - E FORMAT
! ENTRY
!   R30 - OUTPUT BUFFER POINTER
!   R73 - E FORMAT
!      -1  A
!       0  NOT A OR E
!       1  E+-NNN
!       2  E SUPRESS LEAD ZEROS,-,+
!   R36 - EXPONENT
!
EFORM    CLB  R2               !
         TSB  R73              !
         JZR  EXPEX            ! JIF NONE
         LDB  R22,=105         ! E
         PUBD R22,+R30         !
         LDB  R22,=373         ! PLUS - 60
         ELM  R36              !
         JEZ  SGN+             ! JIF EXP SGN POS
         TCM  R36              ! MAKE EXP POS
         LDB  R22,=375         ! MINUS - 60
         JSB  =OUT2            ! GO OUTPUT IT
         JMP  DONUM            !
!
SGN+     JSB  =CNDOU           !
DONUM    BCD                   !
         LDB  R32,=3           !
DONLUP   ELM  R36              ! NEXT EXP DIG
         CLB  R22              !
         ELB  R22              !
         JZR  OUTN             ! JIF ZERO
         LDB  R73,=1           ! NO MORE SUP
OUTN     JSB  =CNDOU           !
CIFDN    BCD                   !
         DCB  R32              !
         JNZ  DONLUP           ! JIF MORE
EXPEX    RTN                   !
!
CNDOU    BIN                   !
         TSB  R73              !
         JOD  OUT2             ! JIF NOT SUPPRESS
         ICB  R2               ! FOR LATER DECR
         RTN                   !
!
OUT2     BIN                   !
         ADB  R22,=60          !
         PUBD R22,+R30         !
         RTN                   !
!
! *******************************************************************
! TAB RUNTIME
! *******************************************************************
         BYT  20,45            !
TAB.     JSB  =ONEB            ! GET THE NUMBER
         DCM  R46              ! TAB - 1
         JPS  TAB1             ! JIF > 0
!
         JSB  =WARN            !
         BYT  54D              ! WARNING: ILLEGAL TAB
!
         CLM  R46              ! DEFAULT TAB IS 1
TAB1     CLM  R56              !
         LDBI R56,=LINELN      !
MODLOP   SBM  R46,R56          !
         JPS  MODLOP           ! JIF > 32
         ADM  R46,R56          ! ELSE RESTORE VAL
DOIT     CLM  R22              !
         LDBI R22,=P.PTR       !
         SBM  R46,R22          ! TAB - PRTPTR
         JPS  MVBLKS           ! JIF TAB >= CURRENT
         ADM  R46,R22          ! RESTORE TAB
         PUMD R46,+R6          ! AND SAVE IT
         SBM  R56,R22          ! GET TO END OF LINE
         JSB  =MVBLK1          ! GO MOVE TO END
         POMD R46,-R6          ! RESTORE TAB
MVBLKS   STM  R#,R56           !
MVBLK1   JSB  =RSMEM-          !
         STM  R56,R54          ! SAVE COUNT
         LDB  R23,=3           ! SO WE BLANK FILL
         LDM  R36,R26          ! FWA
         JSB  =ZROMEM          ! GO BLANK IT
         JSB  =TRAFIC          !
DONNE    RTN                   !
!
! *******************************************************************
! RESTORE RUNTIME 02-22-77
! DATA STATEMENT SEARCH - DASRC/DASRCC
! *******************************************************************
! RESTORE LN #
! *******************************************************************
         BYT  227              !
RSTO..   BIN                   ! RESTORE LN
         POMD R36,+R10         ! LINE # POINTER
         ADMD R36,=FWCURR      ! MAKE IT ABSOLUTE
         JMP  RESTO2           !
!
! *******************************************************************
! RESTORE
! *******************************************************************
         BYT  241              !
RESTO.   BIN                   ! RESTORE
         CLM  R76              ! LINE # 0
RESTO1   JSB  =FNDLIN          !
RESTO2   JSB  =DASRC1          !
         JEN  RSTOK            ! WE DIDNT FIND IT
!
RSTERR   JSB  =ERROR+          !
         BYT  34D              ! MISSING DATA STMT
!
RRTN     LDMD R34,=FWCURR      !
         STMD R36,X34,P.DATL   !
         POMD R74,+R36         ! POINT PAST DATA TOKEN
         STMD R36,X34,P.DATA   !
         CLE                   !
         ICE                   !
RSTOK    RTN                   !
!
DASRC    BIN                   !
         LDMD R34,=FWCURR      !
         LDMD R36,X34,P.DATL   !
DASRCC   JSB  =SKPLN           !
DASRC1   LDMD R74,R36          ! LINE#/BYTES/1ST TOKEN
         CMM  R77,=206         ! IS IT DATA
         JZR  RRTN             ! IT IS!
         CMM  R74,=231,251,2,31 ! LAST LINE?
         JNZ  DASRCC           ! NOPE
         CLE                   ! YUP, SO NOT FOUND
         RTN                   !
!
! *******************************************************************
! 'READ' RUNTIME 01-28-77
! *******************************************************************
         BYT  241              !
READ.    CLM  R40              ! SET UP NON-TAPE INTERCEPT
         STMD R40,=SCTEMP      !
         RTN                   !
!
! *******************************************************************
! READ NUMBER
! *******************************************************************
         BYT  44               !
READN.   CLB  R20              ! READ (NUM)
         LDBD R47,=SCT+7       !
         JSB  =TAPTST          ! TAPE?
         JNZ  READDT           !
         GTO READ#N            !
!
TAPTST   LDBD R57,=SCT+7       ! TAPE FLAG
         BIN                   !
         CMB  R57,=377         ! TAPE?
         RTN                   !
!
! *******************************************************************
! READ STRING
! *******************************************************************
         BYT  44               !
READS.   CLB  R20              ! READ$
         DCB  R20              ! STRING FLAG
         JSB  =TAPTST          ! TAPE INTERCEPT?
         JNZ  READDT           ! JIF NO
         GTO READ#$            ! GOTO 31334 (READ TAPE)
!
READDT   LDMD R34,=FWCURR      !
         LDMD R36,X34,P.DATA   !
         JNZ  CKEOL            ! JIF P.DATA SET
         CLM  R76              ! LINE # 0
         JSB  =RESTO1          ! GO SET IT
         JEZ  DATEXP           ! JIF NO DATA
CKEOL    JSB  =NXDATA          ! GET NEXT DATA
         PUMD R10,+R6          ! SAVE R10
         LDM  R10,R36          ! DATA POINTER
         TSB  R20              !
         JNZ  STR$             ! JIF STRING
         CMB  R34,=4           !
         JNZ  TSTIN            ! JIF NOT REAL
         JSB  =ICONST          !
STONUM   JSB  =STOSV           !
RDRTN    LDMD R56,=FWCURR      !
         STMD R10,X56,P.DATA   ! UPDATE POINTER
RDRTN1   POMD R10,-R6          ! RESTORE R10
NXRTN    RTN                   !
!
TSTIN    CMB  R34,=32          !
         JNZ  TYPERR           ! JIF ERROR
         JSB  =INTCON          !
         JMP  STONUM           !
!
STR$     CMB  R34,=6           ! UNQUOTED STRING?
         JZR  STR$1            ! JIF YES
         CMB  R34,=5           ! QUOTED STRING?
         JNZ  TYPERR           ! JIF NO, INVALID TYPE
STR$1    JSB  =SCONST          !
         JSB  =STOST           !
         JMP  RDRTN            !
!
TYPERR   JSB  =ERROR           !
         BYT  33D              ! DATA TYPE MISMATCH
!
         JMP  RDRTN1           !
!
NXDATA   POBD R34,+R36         ! NEXT DATA TOKEN
         CMB  R34,=16          !
         JNZ  NXRTN            ! JIF NOT END
         JSB  =DASRC           ! GET NEXT DATA STMT
         JEN  NXDATA           ! FOUND ONE
!
DATEXP   JSB  =ERROR+          !
         BYT  34D              ! DATA EXPIRED
!
! R30 = PCR
! R32 = RETURN ADDRESS
!
FNDRTN   STM  R32,R10          !
         JSB  =SETTR1          !
         STMD R30,=PCR         ! STORE PCR
         CMM  R30,R10          ! BEGIN LINE
         JNZ  GNXTL            ! JIF NO
         GTO GORTN             ! GO DO IT
!
INIPGM   SAD                   ! initialize program
         BIN                   !
         LDMD R34,=FWCURR      ! get ptr to start of pgm
         LDMD R36,X34,P.LEN    ! get length of pgm
         JNZ  INPRTN           ! jif non-0, already INITIALIZED
         LDMD R36,=NXTMEM      ! get end of pgm
         SBM  R36,R34          ! calc len of pgm
         STMD R36,X34,P.LEN    ! store back into pgm header
INPRTN   PAD                   !
GNXTL    RTN                   !
!
! *******************************************************************
! STRING CONCATENATION
! *******************************************************************
         BYT  10               !
         BYT  53               !
CONCA.   BIN                   ! CONCATENATE TWO STRINGS
         POMD R70,-R12         ! L1/P1/L2/P2
         LDM  R36,R74          ! STR2 LEN
         LDM  R56,R70          ! STR1 LEN
         ADM  R56,R36          ! STR1 + STR2
         JPS  NOTRUN           ! JIF <= 32767
         LDM  R56,=377,177     ! SET TO 32767
NOTRUN   JSB  =RSMEM-          !
         JEN  MSRTN            ! JIF MEM OVFLO
         PUMD R56,+R12         ! NEW LEN
         SBM  R56,R70          ! TOTAL - STR1
         PUMD R26,+R12         ! NEW STR PTR
         LDM  R36,R72          ! STR 1 PTR
         LDM  R2,R70           !
         JZR  MS2              ! JIF STR1 NULL
         JSB  =MSLOP           !
MS2      TSM  R56              !
         JZR  MSRTN            ! JIF MOVE COMPLETE
         STM  R56,R2           !
         LDM  R36,R76          !
MSLOP    POBD R67,+R36         !
         PUBD R67,+R26         !
         DCM  R2               !
         JNZ  MSLOP            ! JIF NOT DONE
MSRTN    RTN                   !
!
! *******************************************************************
! RESULT
! *******************************************************************
RESUL.   LDMD R40,=RESULT      ! GET MOST RECENT RESULT
         PUMD R40,+R12         !
         JSB  =ONER            ! MAKE SURE IT'S IN REAL# FORMAT
         LDM  R56,=21,0        ! RESERVE 21 BYTES OF RAM (MAX)
         JSB  =RSMEM-          !
         STM  R26,R30          !
         JSB  =CVNUM           ! FORMAT THE NUMBER AS ASCII
         LDM  R36,R54          ! BYTE COUNT
         JSB  =HLFLIN          ! OUT TO CRT
         JSB  =RELMEM          ! NOW RELEASE MEM
         CLE                   !
         RTN                   !
!
! *******************************************************************
! 'CHAIN' RUNTIME
! *******************************************************************
         BYT  241              !
CHAIN.   JSB  =SETTR1          ! CHAIN TO ANOTHER PROGRAM
! WE MAY HAVE TO REPORT CHANGE IN FWCURR
! GETNAM DOES BIN
         JSB  =GETNAM          !
         LDMD R56,=FWPRGM      !
         STMD R56,=FWCURR      !
         JSB  =CALTAP          ! GO LOAD IT
CHAIN+   CMB  R17,=300         ! ERRORS?
         JCY  CHNRTN           ! EXIT IF ERRORS
         PUBD R16,+R6          ! SAVE STATE
         CLB  R16              ! SET STATE=IDLE
         JSB  =ALLOC           ! GO ALLOCATE
         STMD R12,=TOS         ! STORE TOS
         POBD R16,-R6          ! RESTORE STATE
         JEN  CHNRTN           ! EXIT IF ERRORS
         LDMD R36,=FWPRGM      !
         LDBD R34,X36,P.TYPE   ! GET TYPE
         JEV  MAIN             ! JIF MAIN
!
         JSB  =ERROR+          !
         BYT  31D              ! ILLEGAL CHAIN
!
MAIN     LDMD R56,X36,P.COM    ! LEN COMMON
         SBM  R36,R56          !
         CMMD R36,=FWUSER      !
         JZR  MAIN1            ! JIF COM SIZE EQUAL
!
         JSB  =ERROR+          !
         BYT  32D              !
!
MAIN1    JSB  =INIVAR          ! GO INIT VARIABLES
         LDBD R22,=TRCFL2      ! TRACE ALL FLAG
! WE COULD SKIP THIS CHECK
         JZR  MAIN1A           ! JIF NOT SET
         JSB  =TRVRBL          ! GO SET TRACE FLAGS
MAIN1A   LDB  R36,=7           !
         STBD R36,=ROMFL       ! TELL ROMS WHATS HAPPENING
         JSB  =ROMINI          !
         JSB  =RSETG-          ! RESET GO
! R36 = FWCURR FROM RSETG-
! R40 CLEARED BY RSETG-
         STBD R40,=CONTOK      ! MAKE CONT LEGAL
         LDMD R34,=FWBIN       !
         STMD R34,=NXTRTN      ! RESET NEXT RETURN PTR
         JSB  =ASIGN_          ! FIND ASSIGN BUFFER PTR
         STMD R22,=LAVAIL      ! TO LAVAIL
         STMD R22,=CALVRB      ! AND CALVRB
         JSB  =CUROPT          !
         ADM  R36,=P.GO        !
         STMD R36,=OLDPCR      ! FOR TRACE
         STMD R36,=PCR         ! PCR
         STM  R36,R10          !
         LDB  R16,=2           ! SET RUN
         ANM  R17,=376         ! CLEAR CALC COMPL
         ADM  R10,=3,0         !
CHNRTN   RTN                   !
!
! *******************************************************************
! ****  PRINTER DRIVERS ****
! *******************************************************************
!
! *******************************************************************
! COPY RUNTIME
! *******************************************************************
         BYT  241              ! COPY CRT TO PRINTER
COPY.    JSB  =CRTPOF          ! POWER DOWN CRT
         LDBD R30,=CRTWRS      ! GET LAST VALUE WRITTEN TO CRTSTS
         JNG  GRAPHIK          ! JIF GRAPHICS MODE (MS BIT SET)
         LDMD R36,=CRTRAM      ! GET LAST COPY OF CRTSAD
         LDB  R25,=16D         !
COPY+    JSB  =CHKSTS          ! WAIT FOR CRT NOT BUSY
         STMD R36,=CRTBAD      ! STORE ADDRESS OF NEXT CHAR TO FETCH
NXTALF   STM  R12,R26          ! COPY R12 STACK PTR (SCRATCH RAM)
         LDB  R24,=32D         ! GET 040=32 CHARS (ONE LINE)
WANT32   JSB  =INCHR-          ! READ THE NEXT CHAR
         PUBD R32,+R26         ! PUSH IT AT THE END OF R12 STACK
         DCB  R24              ! DEC CHAR COUNTER
         JNZ  WANT32           ! JIF NOT DONE
BLANK?   POBD R32,-R26         ! GET PREVIOUS CHARACTER
         CMB  R32,=40          ! SPACE?
         JNZ  NOBLNK           ! JIF NO, ITS END OF LINE
CM1226   CMM  R12,R26          ! REACHED START OF LINE?
         JNZ  BLANK?           ! JIF NO, SOMETHING TO PRINT
         JMP  SKIPIN           !
!
NOBLNK   CMB  R32,=15          ! IS END OF LINE CHAR A CR?
         JZR  CM1226           ! JIF YES, TREAT IT LIKE SPACE
         ICM  R26              ! PUT LAST CHAR BACK
SKIPIN   LDM  R36,R26          ! COPY END OF LINE PTR
         SBM  R36,R12          ! MINUS START OF LINE = LEN
         LDM  R26,R12          ! POINT TO START OF LINE AGAIN
         JSB  =PRDVR1          ! PRINT IT TO THE INTERNAL PRINTER
         JEN  JMPRTN           ! JIF ERROR, BAIL OUT
         DCB  R25              ! DEC LINE COUNTER
         JNZ  NXTALF           ! JIF NOT DONE
JMPRTN   JSB  =CHKSTS          ! WAIT FOR CRT TO BE NOT BUSY
         LDMD R36,=CRTBYT      ! GET LAST CRTBAD VALUE
         STMD R36,=CRTBAD      ! RESTORE IT TO CRT CONTROLLER
         JSB  =CRTPUP          ! POWER UP THE CRT
P^RTN    RTN                   ! DONE
! *******************************************************************
GRAPHIK  JSB  =GRINIT          ! SEND HOME IN ALPHA
         JEN  P^RTN            ! EXIT STILL IN ALPHA
         JSB  =GRHOME          ! SET TO GRAPHICS
         LDM  R45,=40,300,77   ! R45=040 (32) R46-7=37700 (ADDRESS OF BOTTOM-LEFT GRAPHICS)
SCANLO   LDM  R56,=30,300      ! R56=030 (24 BYTES HEIGHT OF CRT) R57=300 (192) # OF LINES OF GRAPHICS
         STMD R46,=CRTGBA      !
STILL0   JSB  =CHKSTS          ! LOOP TO SEE IF ENTIRE "LEADING" LINE IS BLANK
         STMD R46,=CRTBAD      !   IF SO, JUST DO A PAPER ADVANCE
         JSB  =INCHR-          !
         JNZ  DOLINE           ! JIF LINE NOT ENTIRELY BLANK
         SBM  R46,=100,0       ! SUB ONE GRAPHICS LINE'S WORTH OF ADDRESSES (KEEP CHECKING)
         DCB  R57              !
         JNZ  STILL0           !
         LDMD R46,=CRTGBA      ! ENTIRE LINE IS BLANK, MOVE OVER TO NEXT "LINE" (COLUMN)
         ICM  R46              !
         ICM  R46              !
         JSB  =PAPER+          ! DO A PAPER ADVANCE
         JMP  DNCNT            !
! *******************************************************************
! WHEN COPYING CRT GRAPHICS SCREEN TO THE BUILT-IN PRINTER, THE GRAPHICS
! ARE ROTATED 90 DEGREES.  SO THE FIRST "LINE" PRINTED ON THE
! PRINTER IS THE 8-BIT WIDE STRIP THAT RUNS DOWN THE LEFT
! SIDE OF THE CRT.
DOLINE   LDMD R46,=CRTGBA      !
         JSB  =GETRDY          ! MAKE SURE PRINTER IS READY
         JPS  GR.OUT           ! JIF OUT OF PAPER
! CHANGED 6/24/79
         LDB  R#,=10           !
         STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         STBD R#,=PRMLEN       ! 010 -> PRTCTL
NEXT8    LDB  R0,=70           ! SETUP FOR R* ACCESS TO R70
INROW.   JSB  =CHKSTS          ! WAIT FOR CRT NOT BUSY
         STMD R46,=CRTBAD      ! STORE NEXT BYTE ADDRESS TO CRT
         JSB  =INCHR-          ! GET BYTE FROM THERE
         STB  R32,R*           ! STORE INTO R70-R77
         SBM  R46,=100,0       ! MOVE UP A ROW ON THE CRT
         ICB  R0               ! MOVE TO NEXT REGISTER
         CMB  R0,=100          ! R70'S FILLED?
         JNZ  INROW.           ! JIF NO
         JSB  =GETRDY          ! WAIT FOR PRINTER READY FOR DATA
         STMD R70,=PRDATA      ! SEND 8 BYTES OF DATA
         DCB  R56              ! DEC BYTE HEIGHT OF CRT
         JNZ  NEXT8            ! JIF NOT DONE
         ADM  R46,=2,60        ! MOVE TO BOTTOM OF CRT AND RIGHT ONE BYTE
DNCNT    JSB  =GRHOME          ! WAIT FOR PRINTER TO DUMP THAT LINE OF GRAPHICS
         STBD R#,=GINTEN       ! ENABLE INTERRUPTS
         DCB  R45              ! DEC CRT WIDTH COUNTER
         JNZ  SCANLO           ! JIF NOT DONE
         JSB  =GETRDY          ! WAIT FOR PRINTER READY
         STBD R45,=PRSTS       ! 0 -> PRTSTS (EXIT GRAPHICS, POWER DOWN PRINTER)
PUP      JSB  =CRTPUP          ! POWER UP CRT
EXCHK    RTN                   !
! *******************************************************************
CHKPR    CLE                   ! CLEAR ERROR FLAGS
         JSB  =GETRDY          ! WAIT FOR PRINTER READY
         JNG  EXCHK            ! JIF NOT OUT OF PAPER
! CHANGED 6/24/79
GROUT    LDBD R#,=PRMODE       ! CLEAR "NEED PAPER ADVANCE" FLAG (I THINK)
         LRB  R#               !
         LLB  R#               !
         STBD R#,=PRMODE       ! SAVE BACK
         JSB  =MIDDLE          ! TRY TO ADVANCE PAPER
!
         JSB  =ERROR           ! ERROR
         BYT  20D              ! OUT OF PAPER
!
         CLE                   !
         ICE                   ! SET ERROR FLAG
PUPJMP   JMP  PUP              ! GO POWER UP CRT AND EXIT
!
GRHOME   JSB  =GETRDY          !
         LDB  R31,=300         ! SET "PRINTER PW-UP" AND "??GRAPHICS MODE??"
         STBD R31,=PRSTS       ! SET HOME IN GRAPHICS
         RTN                   !
!
GR.OUT   JSB  =GRHOME          ! SET HOME IN GRAPHICS
         JSB  =GROUT           ! SET TO ALPHA, CALL ERROR
         RTN                   !
! *******************************************************************
! **** PRINTER ALPHA DRIVER ****
! *******************************************************************
! R26 = PTR TO BUFFER TO PRINT
! R36 = LEN OF BUFFER
! *******************************************************************
PRDVR1   BIN                   ! OUTPUT A STRING TO THE INTERNAL PRINTER
         TSM  R36              ! ANY CHARS REMAINING TO PRINT?
         JZR  PAPER.           ! JIF NO, JUST ADVANCE THE PAPER
         CMM  R36,=2,0         ! AT LEAST 2 CHARS TO PRINT
         JCY  NOT^             ! JIF YES
         LDBD R32,R26          ! GET ONLY CHAR
         CMB  R32,=40          ! IS IT A SPACE
         JZR  PAPER.           ! JIF YES, BLANK LINE, JUST ADVANCE PAPER
NOT^     CLE                   ! PRE-CLEAR ERROR FLAG
         BIN                   ! MAKE SURE BIN
         LDBD R31,=CRTWRS      ! GET LAST WRITE TO CRTSTS
         STBD R31,=CRTON?      ! SAVE IT
         JRN  ITSOFF           ! JIF ALREADY WIPED-OUT AND POWERED DOWN
         JSB  =CRTPOF          ! ELSE POWER DOWN CRT
ITSOFF   LDBD R31,=PRMODE      ! GET ???
         JOD  PRLOOP           ! JIF LS BIT SET
         JSB  =GRINIT          ! DO INIT
         JEN  DVREX            !
PRLOOP   TSM  R36              ! ANY CHARS LEFT TO PRINT?
         JZR  DVREX            ! JIF NO
         JSB  =CHKPR           ! PRINT IT?
         JEN  DVREX            ! JIF ERROR
         STBD R36,=GINTDS      ! DISABLE INTERRUPTS (NO RESET)
         CMM  R36,=41,0        ! 32 (DEC) OR LESS CHARS TO PRINT?
         JNC  LEN<33           ! JIF YES, SEND THEM
         PUMD R36,+R6          ! SAVE REMAINING LEN
         LDB  R36,=40          ! LOAD LEN OF 32
         JSB  =SNDMSG          ! PRINT THOSE 32 CHARS
         POMD R36,-R6          ! RECOVER LEN
         SBM  R36,=40,0        ! SUBTRACT OFF THOSE 32 JUST PRINTED
         JMP  PRLOOP           ! LOOP TIL DONE
!
LEN<33   JSB  =SNDMSG          !
DVREX    LDBD R#,=CRTON?       !
         JRZ  PUPJMP           !
         RTN                   !
!
! *******************************************************************
! **** GRAPHICS INIT, SHIP BYTES
! *******************************************************************
GRINIT   JSB  =CHKPR           ! PRINTER BUSY?
         JEN  PRINIT           ! JIF NOT
         JSB  =HOMEA           ! SEND HOME IN ALPHA
         LDBD R#,=PRMODE       ! CHECK FOR GRAPHICS PON
         JOD  PRINIT           ! DONT PAPER^
         ICB  R#               !
         STBD R#,=PRMODE       ! SET POWER ON FLAG
PAPER+   JSB  =GETRDY          ! WAIT FOR PRINTER READY
         CLB  R#               ! 0 TO 177014 CAUSES A PAPER ADVANCE
         STBD R#,=PRMLEN       ! ADVANCE THE PAPER ONE LINE
         RTN                   !
! *******************************************************************
PAPER.   LDBD R30,=PRMODE      ! CHECK FOR POWER ON
         JOD  CHKMID           ! JIF NO, CHECK MIDDLE
         ICB  R30              !
         STBD R30,=PRMODE      ! SET NOT 1ST TIME
         JMP  MIDDLE           !
!
CHKMID   LDBD R#,=ML           ! GET LEN OF LAST MESSAGE PRINTED
         CMB  R#,=20           ! 16?
         JZR  PAPER+           ! JIF YES, IN MIDDLE
MIDDLE   JSB  =HOMEA           ! SEND HOME
         LDB  R40,=20          ! LEN OF 16
         STBD R40,=PRMLEN      ! TELL PRINTER HOW MANY CHARS COMING (MSG LEN)
         STBD R40,=ML          ! SAVE TO "LEN OF LAST MESSAGE"
         LLB  R40              ! DOUBLE LEN TO GET A 32 WHICH IS A BLANK
         STM  R40,R41          ! RIPPLE COPY THROUGH R40-R47
         STMD R40,=PRDATA      ! WRITE 8 SPACES
         STMD R40,=PRDATA      ! WRITE 8 MORE (TOTAL OF 16)
PRINIT   RTN                   !
! ----------------------------------
! R26 = PTR TO BUFFER TO PRINT
! R36 = LEN OF BUFFER
SNDMSG   LDBD R32,=ML          ! GET LEN OF LAST MSG PRINTED
         CMB  R32,R36          ! LESS THAN LEN WE'RE PRINTING THIS TIME?
         JCY  SEND             ! NEW SHORTER THAN OLD
         LLB  R32              ! ELSE x2 (WHICH WAY BEST?)
         CMB  R32,R36          ! STILL LESS THAN NEW LEN?
         JCY  SEND             ! JIF NO
         JSB  =HOMEA           ! SEND HOME FIRST
SEND     STBD R36,=PRMLEN      ! TELL PRINTER HOW MANY CHARS ARE COMING
         STBD R36,=ML          ! SAVE A COPY
         LDB  R36,=4           ! 4 CHUNKS OF 8 BYTES = 32
SNDMS+   POMD R40,+R26         ! GET EIGHT BYTES
         STMD R40,=PRDATA      ! SEND THEM TO THE PRINTER
         DCB  R36              ! DEC CHUNK COUNT
         JNZ  SNDMS+           ! JIF NOT DONE
         STBD R36,=GINTEN      ! ENABLE INTERRUPTS (ALLOW RESET)
         RTN                   ! DONE
!
! *******************************************************************
! **** LIST DRIVER ****
! *******************************************************************
LISTPR   POBD R0,+R26          !
         CMB  R0,=40           !
         JNZ  LISTPR           !
         LDB  R0,=43           ! SET DRP FOR LATER
         LDM  R56,R26          ! HOW FAR DID IT GO?
         SBM  R56,=INPBUF      !
         CMB  R56,=5           ! 5 MEANS LINE#>1000
         JZR  SBM26            !
         LDB  R56,=4           ! SET 56 TO 4
         ICB  R0               ! CHANGE DRP TO 44
SBM26    SBM  R26,R56          ! MOVE POINTER
         JSB  =NO.BLK          ! RESET TOTAL LENGTH
         DCM  R#               ! TRASH THE CR.
LISTP1   PUMD R36,+R6          ! SAVE LENGTH
         CMM  R36,=41,0        ! LESS THAN 33?
         JNC  SPIT             ! JIF YES
         LDM  R36,=40,0        ! SEND 32
SPIT     JSB  =NOT^            ! SEND 1 LINE
         LDMD R36,=LISTCT      ! DROP LIST BUSTER
         DCM  R36              !
         STMD R36,=LISTCT      !
         POMD R36,-R6          ! RESTORE TOTAL LENGTH
         JEN  LISTER           ! JIF ERRORS
         SBM  R36,=41,0        ! DONE?
         JNG  LSTRTN           ! JIF YES
         ICM  R36              ! BUMP TO 32 THAT LINE
         ADM  R36,R56          ! BUMP TOTAL LENGTH
         LDMD R*,=BLANKS       ! APPEND BLANKS
         PUMD R*,-R26          ! (IN FRONT)
         JMP  LISTP1           ! NEXT LINE
!
LSTRTN   LDMD R#,=LISTCT       ! DO PAPER^ AT 11"
         JZR  STDFLT           ! ALREADY ZERO, SET DEFAULT
         JPS  LISTER           ! JIF DONE
STDFLT   LDMD R#,=LDFLTR       ! RESET DEFAULT
         STMD R#,=LISTCT       !
         LDB  R#,=6            !
LSTBST   JSB  =PAPER.          !
         DCB  R36              !
         JNZ  LSTBST           !
LISTER   RTN                   !
!
! *******************************************************************
! **** PRINTER STATUS CHECK/HOME HEAD
! *******************************************************************
HOMEA    JSB  =GETRDY          ! GET RDY FLAG
         LDB  R#,=100          ! SEND HOME IN ALPHA
         STBD R#,=PRSTS        ! POWER UP PRINTER
         CLB  R#               !
         STBD R#,=ML           ! CLEAR ML FOR HOME
! FALL THROUGH TO GETRDY
GETRDY   DRP  R30              !
GETLUP   LDBD R#,=PRSTS        ! READY?
         JEV  GETLUP           ! EVEN IS NO
         RTN                   !
! *******************************************************************
! PRMODE IS 0 FOR POWER ON OR OUT OF PAPER
! *******************************************************************
! PRMODE BIT 1 IS USED FOR BPLOT TO DECIDE ON BLINKING THE CRT.
! BIT 7 IS USED TO THE TEST ROM.  OTHER BITS ARE AVAILABLE.  IT IS
! CLEARED FOR POWER ON AND RESET.
! ALPHA INIT IS:
!     POWER DOWN CRT
!     IF NOT PON, DONE
!     ELSE HOME IN ALPHA
!     PAPER ADVANCE
!     AND DONE.
! GRAPH INIT IT:
!     POWER DOWN CRT
!     HOME IN ALPHA
!     IF NOT PON, DONE
!     ELSE PAPER ADVANCE
!     AND DONE.
!   DONE...(THEN DGO TO GRAPHICS MODE).
! *******************************************************************
         BYT  241              !
PRALL.   CLB  R#               ! PRINT ALL
         ICB  R#               !
         STBD R#,=PRALLM       !
         RTN                   !
!
! *******************************************************************
! BACKWARD TRIG ROUTINES
! *******************************************************************
! ATN(X/Y)
! *******************************************************************
         BYT  40,55            !
ATN2.    CLM  R26              ! INITIALIZE FLAGS
         CLM  R22              ! SGN(ANS) REGISTER
         JSB  =TWOR            ! DEMAND TWO REALS FOR X AND Y
         JSB  =SEP15           ! SPLIT X AND Y
         TSM  R42              ! Y=0?
         JNZ  RTP50            ! JMP IF Y#0
         TSM  R52              ! X=0?
         JNZ  RTP52            ! JIF ANS#0
!
         JSB  =ERROR+          ! FATAL ERROR
         BYT  11D              !
!
RTP52    JSB  =TRC7            ! PI/2 TO R70
         STM  R70,R40          ! PI/2 TO R40
         STB  R33,R22          ! SGN(X)=SGN(ANS) TO R22
         GTO BRT54             ! GO CONVERT TO DEG,RAD,OR GRDS
!
RTP50    TSB  R32              ! Y>0?
         JRZ  RTP60            ! JMP IF Y>0
         LDB  R23,=11          ! SET S7=S10=9 STATUS TO GIVE
         STB  R23,R26          ! PI-T (2ND OR 3RD QUAD ANS)
         CLB  R32              ! SGN(Y)=0
RTP60    JSB  =DIV20           ! X/ABS(Y)
         JMP  BRT10            ! CONTINUE
!
! *******************************************************************
! ASN
! *******************************************************************
         BYT  20,55            !
ISIN     LDM  R26,=0C,99C      ! INV(SIN) ENTRY: SET STATUS
         JMP  BRT5             !
!
! *******************************************************************
! ACS
! *******************************************************************
         BYT  20,55            !
ICOS     LDM  R26,=9C,99C      ! INV(COS) ENTRY: SET STATUS
         JMP  BRT5             !
!
! *******************************************************************
! ATN
! *******************************************************************
         BYT  20,55            !
ITAN     LDM  R26,=0C,9C       ! INV(TAN) ENTRY: SET STATUS
BRT5     CLM  R22              ! CLR SGN(ANS) & ADD PI/2 STATUS
         JSB  =ONER            ! GET ARGUMENT X (FLOATING PT)
         JSB  =SEP10           ! SPLIT X
BRT10    TSB  R32              ! A<0?
         JRZ  BRT12            ! JMP IF A>=0
         NCB  R22              ! S4=9 FOR NEGATIVE ANSWER
         TSB  R27              ! WHICH FUNCTION? (TEST S13)
         JRZ  BRT12            ! JMP IF RTP
         TSB  R26              ! INV(SIN(),INV(COS), OR INV(TAN)?
         JRZ  BRT12            ! JMP IF INV(SIN) OR INV(COS)
         LLB  R26              ! SET S10=0 (SAYS FIND INV(SIN))
         NCB  R23              ! S7=9 FOR ADD PI/2
         CLB  R22              ! S4=0 FOR POS (+ ANS)
BRT12    TSB  R37              ! POSITIVE EXPONENT?
         JLZ  BRT70            ! JMP IF A=0 OR A>=1
         TSB  R27              ! WHICH FUNCTION? (TEST S6)
         JLZ  BRT30            ! JMP IF RTP OR INV(TAN)
         STM  R36,R24          ! SAVE EXP(A)
         PUMD R40,+R12         ! SAVE MANT(A)
         JSB  =BRTS35          ! SHIFT MANT; MOVE DEC TO LEFT
         CLM  R34              ! CLR EXP(1+A)
         STM  R40,R50          ! MOVE MANT(A)
         LRM  R57              ! PREPARE TO ADD 1
         ADB  R57,=10C         ! A+1
         TCM  R40              ! =1-A IF 0<A<1; =0 IF A=0
         JCY  BRT20            ! JMP IF A=0
         JSB  =SHF10           ! ELIMINATE LEAD ZEROS
         JSB  =MPY30           ! (1+A)(1-A) (=1-AA)
         DCM  R36              ! CORRECT DEC PT TO NORMAL LOC
         JSB  =SQR30           ! SQR(A-AA)
         LDM  R34,R24          ! GET EXP(A)
         POMD R50,-R12         ! GET MANT(A)
         JSB  =DIV20           ! A/SQR(1-AA)
         JMP  BRT22            ! CONTINUE
!
BRT72    TSB  R27              ! WHICH FUNCTION?
         JLZ  BRT76            ! JMP IF ITAN OR RTP
!
         JSB  =ERROR+          ! GO PROCESS ERROR
         BYT  11D              !
!
BRT76    JSB  =FTR53           ! GIVES 1/X
         NCB  R26              ! COMPLEMENT S10 STATUS
         JMP  BRT30            ! GO TO PSEUDO-DIVIDE
!
BRT70    TSM  R36              ! A=0, 1<=A<10, OR A>=10?
         JNZ  BRT72            ! JMP IF A>=10
         STM  R40,R50          ! MOVE MANT(A)
         JZR  BRT50            ! JMP IF A=0
         SBB  R57,=10C         ! A-1
         TSM  R50              ! A=1 OR 1<1<10?
         JNZ  BRT72            ! JMP IF 1<1<10
         TSB  R27              ! WHICH FUNCTION? (TEST S6)
         JLZ  BRT74            ! JMP IF INV(TAN) OR RTP
         NCB  R26              ! 9 TO 0 IF ICOS; 0 TO 9 IF ISIN
         CLM  R40              ! ICOS(1)=0; ISIN(1)=PI/2-0
         JMP  BRT50            ! GO DO PI/2 ADJUSTMENT
!
BRT74    LDMD R70,=DCON1       ! PI/4 TO R70(=ITAN(1))
         STM  R70,R40          ! PI/4 TO R40
         DCM  R36              ! EXP(PI/4)= -1
         JMP  BRT50            ! GO DO PI/2 ADJUSTMENT
!
BRT20    POMD R40,-R12         ! GET MANT(A)
         LDM  R36,R24          ! GET EXP(A)
BRT22    CLB  R32              ! CLR SGN
         CMB  R37,=120         ! TEST SIZE OF NUMBER
         JNC  BRT76            ! JMP IF 1<=NUMBER
BRT30    STM  R40,R50          ! MOVE MANT
         LDM  R34,R36          ! SAVE EXP
         ADM  R34,=7,0         ! NO DECADES-1 IN R34 (0-6)
         JNC  BRT50            ! SM. ANGLES: JMP IF EXP(A)<-7
         CLM  R70              ! CLEAR PQ AREA
         CLM  R40              ! PREPARE FOR CONSTANT 1
         ICB  R47              ! GENERATE CONSTANT 1
         LRM  R57              ! GENERATE LEAD 0 (BUFFER AREA)
BRT32    STM  R50,R60          ! SAVE Z
         SBM  R50,R40          ! Z=Z-X
         JNC  BRT34            ! JMP IF UNSUCCESSFUL SUBTRACT
         ICB  R70              ! TALLY 1 IN PQ
         STB  R36,R24          ! INIT SHIFT COUNTER TO -J
BRT36    LRM  R67              ! Z(10 TO -J) LAST TIME THRU
         LRM  R67              ! Z(10 TO -2J) LAST TIME THRU
         ICB  R24              ! INCREMENT SHIFT COUNTER
         JNZ  BRT36            ! LOOP TILL COUNTER=0
         ADM  R40,R60          ! X=X+Z(10 TO -2J)
         JMP  BRT32            ! CONTINUE
!
BRT50    JSB  =TRC7            ! PI/2 TO R70
         TSB  R26              ! SUB. T FROM PI/2? (TEST S10)
         JRZ  BRT52            ! JMP IF S10=0 (NO SUBTRACT)
         JSB  =BRTS40          ! T RT SHIFT TO ALIGN DEC PTS
         SBM  R40,R70          ! T-PI/2
         TCM  R40              ! T = PI/2 - T
         JSB  =SHF10           ! ELIMINATE LEAD ZEROS
BRT52    TSB  R23              ! ADD PI/2?
         JRZ  BRT54            ! JMP IF S7=0 (NO ADD)
         JSB  =BRTS40          ! SHIFT T RT TO ALIGN DECIMAL
         ADM  R40,R70          ! T=T+PI/2
BRT54    STM  R36,R34          ! MOVE EXP(T)
         LDBD R25,=DRG         ! GET DEG,RAD,GRD INDICATOR
         JPS  BRT60            ! JMP IF RAD
         ICM  R34              ! 10T
         ICM  R34              ! 100T
         CLM  R36              ! EXP(PI/2)=0
         STM  R40,R50          ! MOVE MANT(100T)
         LDM  R40,R70          ! PI/2 TO R40 FOR DIVIDE
         JSB  =DIV20           ! T GRD = 400 T RAD/2PI
         TSB  R25              ! DEG OR GRD MODE SET?
         JOD  BRT60            ! JMP IF GRD
         STM  R40,R50          ! COPY T GRD
         LRM  R57              ! .1T GRD
         SBM  R40,R50          ! T DEG = .9T GRD
BRT60    STB  R22,R32          ! GET SIGN ANS
         GTO SHRONF            ! SHIFT, ROUND, NFR, AND EXIT
!
BRT34    DCB  R36              ! DECREMENT -J (INCREMENT J)
         LLM  R70              ! INITIALIZE NEW PQ DIGIT TO 0
         LDM  R50,R60          ! GET Z
         LLM  R50              ! 10Z
         DCB  R34              ! DECREMENT PQ DECADE COUNTER
         JCY  BRT32            ! LOOP TILL ALL DECADES DONE
         CLM  R34              ! CLEAR EXP FOR DIVIDE
         CLE                   ! READY FOR DIV77
         JSB  =DIV77           ! Y/X=TAN(T)=T (Y=10TO-6,X=1)
         STM  R70,R50          ! PQ TO R50
         LDM  R30,=TBL3B       ! POINTER TO TRIG CONSTANTS
BRT40    POMD R70,-R30         ! GET NEXT TRIG CONSTANT
         LRM  R57              ! SHIFT RT NEXT PQ DIG; 0 TO E
         ICM  R36              ! INCREMENT DECADE COUNTER
         JMP  BRT42            ! JMP TO PSEUDO-MULTIPLY LOOP
!
BRT44    DCB  R50              ! DECREMENT PQ DIGIT
         ADM  R40,R70          ! ADD CONSTANT TO SUM
         JNC  BRT42            ! JIF NO CARRY
         ICE                   ! ELSE UP VALUE IN E
BRT42    TSB  R50              ! TEST CURRENT PQ DIGIT
         JRN  BRT44            ! JMP(LOOP) IF NOT YET=0
         ERM  R47              ! SHIFT ACCUMULATING RES RIGHT
         TSM  R50              ! ANY MORE NON-ZERO PQ DIGITS?
         JZR  BRT50            ! JMP(EXIT LOOP) IF R50=0
         JMP  BRT40            ! CONTINUE LOOP
!
BRTS30   LRM  R47              ! SHIFT MANTISSA RIGHT
BRTS35   ICM  R36              ! INCREMENT EXPONENT
BRTS40   TSB  R37              ! HAS EXPONENT REACHED 0 YET?
         JNG  BRTS30           ! JMP(LOOP) IF EXP NOT YET 0
         CLM  R36              ! CLEAR REGISTER
         RTN                   ! RETURN
!
! *******************************************************************
! 'TEST' KEY
! *******************************************************************
TEST.    JSB  =PWO             ! PWO TEST
         CMB  R17,=300         ! IF ERR, EXIT
         JCY  TEND             !
! *** GRAPHICS DISPLAY 1'S THEN 0'S ***
CTEST    JSB  =GRAPH.          ! SWITCH TO GRAPHICS
         CLB  R32              !
         JSB  =GRIN++          ! FILL GRAPHICS WITH 1
         LDB  R32,=377         !
         JSB  =GRIN++          ! FILL GRAPHICS WITH 0
! *** DISPLAY 128 ASCII CHARS + ROM CHECKSUM ***
         JSB  =ALPHA.          ! SWITCH TO ALPHA
         JSB  =BLK&SC          ! BLANK LINE AND SCROLL?
         LDMD R56,=CRTBYT      ! REM CRT BYTE ADDR
         LDB  R33,=200         ! START WITH ASCII CODE=0
CTEST1   STB  R#,R32           !
         JSB  =OUTCHR          ! DISPLAY ASCII CHARACTER
         ICB  R33              ! INCREMENT ASCII CODE
         JNC  CTEST1           ! REPEAT FOR 128 ASC CODES
         LDM  R26,=TSTBUF      ! GET ROM SUM FROM BUFFER
         LDM  R36,=2,0         ! BYTE COUNT=2
         JSB  =OUTSTR          ! DISPLAY ROM CHECKSUM
! *** PRINT 128 ASCII CHARS + ROM CHECKSUM ***
PTEST    LDM  R36,R56          ! GET BYTE ADDR
         LDB  R25,=5           ! NUMBER OF LINES=5
         JSB  =COPY+           ! COPY CRT TO PRT
         JSB  =STBEEP          ! BEEP
TEND     STBD R#,=GINTEN       ! ENABLE INTERRUPTS
         RTN                   !
!
! *******************************************************************
! PWO TEST
! *******************************************************************
PWO      BIN                   ! -
         STBD R#,=GINTDS       ! DISABLE INTERRUPTS
         CLM  R20              ! SET ERROR INDEX = 0
! *** RAM CHECKERBOARD TEST ***
         LDMD R60,=PRT         ! GET SOME HANDY DATA
RAM      LDM  R32,=0,200       ! GET RAM START ADDR
RAM1     LDMD R70,R32          ! SAVE PREV RAM CONTENTS
         PUMD R60,+R32         ! WRITE OUR HANDY DATA THERE
         POMD R50,-R32         ! READ IT BACK
         PUMD R70,+R32         ! RESTORE RAM CONTENTS
         XRM  R50,R60          ! GET BACK WHAT WE WROTE?
         JNZ  ERR              ! JIF NO, EXIT, INDEX=0
         CMMD R32,=LWAMEM      ! DONE?
         JNC  RAM1             ! LOOP TIL END OF RAM
         CLM  R32              ! ROM START ADDR = 0
         NCM  R60              ! INVERT R60 BITS
         JOD  RAM              ! JIF ONLY FIRST TIME THRU, TRY AGAIN WITH FLIPPED BITS
         STMD R60,=TSTBF0      ! SAVE FOR REFRESH CHECK LATER
! *** ROM CHECKSUM ***
ROM      ICM  R20              ! INDEX+1 (TOTAL=ADDR=0)
         JSB  =RSUM8K          ! CHECKSUM ALL 4 ROMS
         JNZ  ERR              ! JIF ERROR, EXIT, INDEX=1-4
         ADMD R56,R#           ! ADD CHECKSUM TO TOTAL
         STMD R56,=TSTBUF      ! STORE TOTAL IN BUFFER
         ICM  R32              ! GET ADDRESS OF NEXT ROM
         ICM  R32              !
         JNO  ROM              ! REPEAT TIL END OF ROMS
! *** READ 1 BYTE FROM PRT ROM ***
PRT      LDM  R44,=67,41,216,101 !
         STBD R44,=PRCHAR      ! SEND ASCII ADDRESS OF CHAR
         STBD R45,=PRSTS       ! SEND COL#, READ ROM COMMAND
         ANMD R47,=PRSTS       ! READ PRINTER STATUS
         CMB  R47,=101         ! CHECK PRT,DATA READY=1
         JNZ  ERR+1            ! IF ERR, EXIT, INDEX=5
         CMBD R46,=PRCHAR      ! READ PRINTER ROM, COMPARE
         JNZ  ERR+2            ! IF ERROR, EXIT, INDEX=6
! *** CHECK TAPE STATUS ***
         LDBD R46,=TAPSTS      ! READ TAPE STATUS
         JOD  TAPE             !
         JSB  =SET0S           ! INVALID DIRECTORY, CLR ASN.
TAPE     LDM  R20,=7,0         ! ERRL# = 7 (reason for selftest fail)
         LDBD R23,=TAPSTS      ! GET TAPE STATUS (TWICE TO MAKE SURE)
         ANM  R23,=246         ! CHECK STOP, GAP=1
         CMB  R23,=240         ! CHECK STALL, ILIM=0
         JNZ  ERR              ! IF ERR,EXIT,INDEX=7
! *** READ KEY STATUS ***
         LDBD R23,=KEYSTS      ! CHECK GLOBAL INT ENABLED
         JNG  ERR+1            ! IF ERROR, EXIT INDEX=8
! *** CHECK RAM REFRESH ***
RAMF     CMMD R60,=TSTBF0      ! DATA STILL THERE?
         JZR  PWOEND           ! JIF OK TO END
ERR+2    ICM  R20              ! SELFTEST ERROR# = 9
ERR+1    ICM  R20              ! SELFTEST ERROR# = 8
ERR      STMD R20,=ERLIN#      ! SAVE ERROR INDEX
         JSB  =STBEEP          ! BEEP ANYWAY, MAY NOT GET TO DISP
!
         JSB  =ERROR           !
         BYT  23D              ! ERROR 23 (decimal) SELF TEST
!
PWOEND   RTN                   !
!
! *******************************************************************
! READ ARRAY NUMERIC
! *******************************************************************
         BYT  44               !
R#ARAY   BIN                   ! READ AN ARRAY FROM A DATA FILE
         POMD R44,-R12         ! R44=ADDR; R46=NAME
         POMD R52,+R44         ! ARRAY LEN,ROW,COL
         PUMD R44,+R6          ! SAVE ADDR,NAME
         LDM  R36,R44          ! MOVE ADDRESS
         PUMD R36,+R12         ! PUSH TO STACK
         LDB  R36,R47          ! MOVE NAME
         LLB  R36              !
         TSB  R36              ! TRACE ON?
         JPS  TRACOF           ! JIF NO
         CLM  R63              ! 5 BYTES OF 377
         DCM  R63              !
         TSM  R56              ! 1 DIM?
         JNG  PUSHOD           ! R67 IS ODD IF 1 DIM
         ICB  R67              ! OTHERWISE EVEN
PUSHOD   PUMD R63,+R12         !
TRACOF   PUMD R46,+R12         ! PUSH NAME
         JSB  =LENCAL          ! CALC DATA LENGTH
         PUMD R36,+R6          ! SAVE DATA LENGTH
         LDM  R36,R52          ! ARAY LENGTH
         PUMD R36,+R6          ! SAVE IT
NXTELR   JSB  =READ#N          ! READ A NUMERIC
         POMD R40,-R6          !
         STM  R40,R30          !
         CMB  R17,=300         !
         JCY  CALOUT           ! ERRORS?
         SBM  R46,R44          ! DOWN COUNT LENGTH
         JZR  CALOUT           !
         ADM  R30,R44          ! NEXT ADDRESS
         STM  R30,R40          !
         PUMD R30,+R12         ! PUSH ADDRESS
         PUMD R40,+R6          ! ADDR,NAME,DLEN,ARAYLENGTH
         LDM  R46,R42          ! MOVE NAME
         ANM  R47,=277         ! TRACE OFF
         PUMD R46,+R12         ! PUSH NAME
         JMP  NXTELR           ! READ NEXT ELEMENT
!
LENCAL   LDM  R36,=10,0        ! DATUM LENGTH DEFAULT
         BCD                   !
         PUMD R46,+R6          ! SAVE NAME
         LRB  R46              !
         BIN                   !
         ANM  R46,=3,0         ! ISOLATE TYPE BITS
         JZR  CALDON           ! 0 IS REAL
         LRB  R36              ! 10->4
         DCB  R46              !
         JNZ  CALDON           ! 0 IS SHORT
         DCB  R36              ! 4->3 FOR INTEGER
CALDON   POMD R46,-R6          ! RESTORE NAME
CALOUT   RTN                   !
!
! *******************************************************************
! UNUSED BYTES
! *******************************************************************
         BSZ  13               !
! *******************************************************************
! ROM CHECKSUMS
! *******************************************************************
         BYT  150              ! END OF ROM (CHECKSUM & SUCH)
         BYT  166              !
         BYT  147              !
         BYT  343              !
         FIN
