0002        NAM  REDZER
0007        DEF  RUNTIM
0008        DEF  TOKENS
0009        DEF  PARSE 
0010        DEF  ERMSG 
0011        DEF  INIT  
0013 RUNTIM BSZ  2
0014        DEF  RDIM.            !   REDIM     1
0015        DEF  OTHER            !   ZER       2
0016        DEF  MAT.             !    MAT       3
0017        DEF  DUMMY            !   DUMMY     4
0018        DEF  ZER.             !    ZER       5
0019        DEF  ZDIM1V           !  ZER(M)    6
0020        DEF  ZDIM2V           !  ZER(M,N)  7
0021        DEF  DUMMY=           !  DUMMY=    10
0022        DEF  RED1V            !   REDIM1V   11
0023        DEF  RED2V            !   REDIM2V   12
0025 PARSE  BSZ  2
0026        DEF  REDIM            !   REDIM     1
0027        DEF  ZER              !     ZER       2
0028        DEF  MAT              !     MAT       3
0029        BYT  377,377
0031 INIT   LDBD R32,=ROMFL 
0032        JZR  FLGSET
0033 INIOUT CMB  R#,=4
0034        JZR  RUNHIT
0035        CMB  R#,=5
0036        JNZ  CKCOM 
0037 FLGSET LDB  R33,=1
0038        JMP  FLGSTR
0039 CKCOM  CMB  R#,=7
0040        JNZ  INIRTN
0041        LDMD R36,=FWUSER
0042        CMMD R36,=FWPRGM
0043        JNZ  INIRTN
0044 RUNHIT LDMD R36,=BINTAB
0045        LDBD R36,X36,RDMFLG
0046        JZR  INIRTN
0047        JSB  =DALLOC
0048        JSB  =ALLOC 
0049        JSB  =INIVAR
0050        CLB  R36
0051        STBD R36,=CONTOK
0052        LDMD R36,=FWUSER
0053        LDMD R32,=FWPRGM
0054        CMM  R32,R36
0055        JZR  FLGCLR
0056        JSB  =INIVLP
0057 FLGCLR CLB  R33
0058 FLGSTR LDMD R36,=BINTAB
0059        STBD R33,X36,RDMFLG
0060 INIRTN RTN  
0062 TOKENS ASP  "REDIM"
0064        ASP  "ZER"
0066        ASP  "MAT"
0068        BYT  377              !               4
0070        ASP  "ZER"
0072        ASP  "ZER"            !   ZER()     6
0074        ASP  "ZER"            !   ZER(,)    7
0076        BYT  275              !     DUMMY=    10
0077        BYT  377
0079 M      EQU  315
0080 R      EQU  322
0081 T      EQU  324
0083 ZDMTOK EQU  5
0084 RDMTOK EQU  11
0085 EQUTOK EQU  10
0087 RDMFLG BSZ  1
0090        BYT  41
0092 DUMMY  BSZ  0
0093 OTHER  RTN  
0096        BYT  241
0098 RDIM.  BSZ  0
0099 MAT.   RTN  
0102        BYT  5,51
0104 DUMMY= RTN  
0106 MAT    LDB  R51,=371
0107        PUBD R51,+R12
0108        PUBD R51,+R12
0109        PUBD R43,+R12
0110        JSB  =SCAN  
0111        JSB  =NARREF
0112        CMB  R14,=EQUALS
0113        JNZ  ERR89 
0114        JSB  =SCAN  
0115        BIN  
0116        CMB  R43,=2
0117        JZR  ZER   
0118 ERR89  JSB  =ERROR 
0119        BYT  89D
0120        RTN  
0121 ZER    LDB  R32,=ZDMTOK
0122        PUBD R32,+R6
0123        JSB  =SCAN  
0124        CMB  R14,=OPEN  
0125        JNZ  PRM-  
0126        ICB  R32
0127        JSB  =SCAN  
0128        POBD R70,-R6
0129        LDMD R30,=BINTAB
0130        JSB  X30,SUBSCR
0131        JEZ  ERR89 
0132        LDB  R53,=371
0133        PUBD R53,+R12
0134        PUBD R53,+R12
0135        LDB  R53,=EQUTOK
0136        PUBD R53,+R12
0137        RTN  
0138 REDIM  LDB  R51,=371
0139        PUBD R51,+R12
0140        PUBD R51,+R12
0141        PUBD R43,+R12
0142 ALOOP  JSB  =SCAN  
0143        CMB  R14,=2
0144        JNZ  ERR89 
0145        JSB  =PUSH45
0146        LDB  R32,=RDMTOK
0147        LDMD R30,=BINTAB
0148        JSB  X30,SUBSCR
0149        JEZ  ERR89 
0150        CMB  R14,=COMMA 
0151        JZR  ALOOP 
0152        RTN  
0154 PRM-   LDB  R51,=371
0155        PUBD R51,+R12
0156        PUBD R51,+R12
0157        POBD R53,-R6
0158        PUBD R53,+R12
0159        LDB  R53,=EQUTOK
0160        PUBD R51,+R12
0161        PUBD R51,+R12
0162        PUBD R53,+R12
0163        RTN  
0165 SUBSCR PUBD R36,+R6
0166        JSB  =NUMVAL
0167        POBD R36,-R6
0168        JEZ  SUBRTN
0169        CMB  R14,=COMMA 
0170        JNZ  RTPAR 
0171        ICB  R32
0172        PUBD R36,+R6
0173        JSB  =NUMVA+
0174        POBD R36,-R6
0175        JEZ  SUBRTN
0176 RTPAR  CMB  R14,=CLOSE 
0177        CLE  
0178        JNZ  SUBRTN
0179        JSB  =SCAN  
0180        LDB  R51,=371
0181        PUBD R51,+R12
0182        PUBD R51,+R12
0183        PUBD R32,+R12
0184        CLE  
0185        ICE  
0186 SUBRTN RTN  
0189        BYT  20,55
0191 ZDIM1V LDMD R36,=BINTAB
0192        JSB  X36,DUP1V        ! DUP MAT ADDR PTR ON R12.
0193        JSB  X36,RD1V         ! REDIM TARGET ARRAY.
0194        JMP  ZER.             !    GO SET IT = ZERO.
0196        BYT  40,55
0198 ZDIM2V POMD R50,-R12         ! GET 1ST SUBSCRIPT.
0199        LDMD R36,=BINTAB
0200        JSB  X36,DUP1V 
0201        PUMD R50,+R12
0202        JSB  X36,RD2V  
0203        JMP  ZER.             !    GO SET IT = ZERO.
0205        BYT  0,55
0207 ZER.   POMD R20,-R12
0208        PUMD R20,+R12
0209        PUMD R20,+R12
0210        LDMD R36,=BINTAB
0211        JSB  X36,LOCSZ-
0212        CLE                   !         CLEAR FLAG.
0213        DCE                   !         FLAG SETTING FOR TARGET MATRIX.
0214        POMD R20,-R12
0215        LDMD R36,=BINTAB
0216        JSB  X36,REDIM.
0217        TSM  R36
0218        JZR  ZERTN            !   DONE IF NULL ARRAY.
0219        LDMD R36,=BINTAB
0220        JSB  X36,VECFLG
0221        CMB  R17,=300         !   FOR REDIM ERROR CHECK.
0222        JNC  ERROUT           !  JIF NO REDIM ERROR.
0223 ZERTN  RTN  
0224 ERROUT LDMD R76,=INCRC 
0225        LDB  R0,=70           !   WILL ALTER.
0226        SBB  R0,R76           !  REAL=60,SHORT=64,INT=65.
0227        CLM  R60              !     CONST=0.
0228        STM  R20,R36          ! STARTING ADDR TO R36.
0229        STM  R20,R72          ! ANOTHER COPY FOR CKTRC.
0230        JSB  =ZERO1-          ! PUSH OUT CONSTS (0'S OR 1'S).
0231        JMP  CKTRC 
0232 LOCSZ- CLE                   !         CLEAR FLAG.
0233        DCE                   !         FLAG SETTING FOR TARGET MATRIX.
0234        POMD R20,-R12
0235        LDMD R36,=BINTAB
0236        JSB  X36,RUDIM 
0237        BIN                   !         SET MODE.
0238 VECFLG LDBD R47,=TRCFLG
0239        ANM  R47,=360         ! CLEAR RT BITS.
0240        JEZ  FLGSTO           !  JIF TARGET MATRIX IS NOT A VECTOR.
0241        ICB  R47              !     TAG THIS AS A VECTOR.
0242 FLGSTO STBD R47,=TRCFLG
0243        RTN                   !         RETURN.
0245 DUP1V  POMD R40,-R12
0246        POMD R32,-R12
0247        PUMD R32,+R12
0248        PUMD R32,+R12
0249        PUMD R40,+R12
0250        RTN  
0251 CKTRC  LDBD R46,=TYPC  
0252        ARP  R72
0253        LDMD R36,=BINTAB
0254        JSB  X36,FETCH-
0255        DRP  R34
0256 STOV   BIN  
0257        PUMD R#,+R12
0258        ADMD R#,=INCRC 
0259        LDB  R56,=317
0260        LDBD R57,=TRCFLG
0261        JLZ  NOTRC 
0262        PUBD R56,+R12
0263        PUBD R56,+R12
0264        PUBD R56,+R12
0265        PUBD R56,+R12
0266        ANM  R57,=17
0267        STBD R57,=TRCFLG
0268        PUBD R57,+R12
0269        LDB  R57,=377
0270        JMP  CNAME 
0271 NOTRC  LDB  R57,=277
0272 CNAME  ANMD R56,=MTEMP 
0273        PUMD R0,+R6
0274        PUMD R2,+R6
0275        PUMD R14,+R6
0276        PUMD R70,+R6
0277        LDM  R70,R20
0278        PUMD R70,+R6
0279        LDM  R70,R30
0280        PUMD R70,+R6
0281        LDBD R77,=TYPC  
0282        ORB  R56,R77
0283        PUMD R56,+R12
0284        PUMD R40,+R12
0285        JSB  =STOSV 
0286        JMP  GETREG
0287 FETCH- LDM  R34,R#
0288 FETCH  PUMD R0,+R6
0289        PUMD R2,+R6
0290        PUMD R14,+R6
0291        PUMD R70,+R6
0292        LDM  R70,R20
0293        PUMD R70,+R6
0294        LDM  R70,R30
0295        PUMD R70,+R6
0296        JSB  =FETSVX
0297        BIN  
0298        STM  R60,R40
0299 GETREG POMD R70,-R6
0300        STM  R70,R30
0301        POMD R70,-R6
0302        STM  R70,R20
0303        POMD R70,-R6
0304        POMD R14,-R6
0305        POMD R2,-R6
0306        POMD R0,-R6
0307        RTN  
0310        BYT  32
0312 RED1V  LDMD R36,=BINTAB
0313        JSB  X36,RD1V  
0314        RTN  
0315 RD1V   CLM  R24              !           READY TO DECLARE A VECTOR.
0316        ICM  R24              !           THIS IS A VECTOR.
0317        JSB  =ONEB            !          BINARY INT TO R46.
0318        LDMD R36,=BINTAB
0319        JSB  X36,STOPT-
0320        LDMD R36,=BINTAB
0321        JSB  X36,R1VA         !      1V REDIM.
0322        JEZ  ER33R            !         JIF DIM MISMATCH.
0323 RDRTN  RTN  
0324 R1VA   DRP  R46
0325        JMP  R1V   
0326 R1VB   DRP  R56
0327 R1V    ADMD R#,=OPTBAS       !    ADJUST PRIOR TO REDIM.
0328        STM  R#,R22           !        MOVE ROW TO R22.
0329        CLE  
0330        DCE                   !               FLAG TYPE FOR REDIM.
0331        JPS  REDIM.           !        JIF OK.
0332 ER89R- POMD R36,-R6          !       ELIM RTN
0333 ER89R  POMD R36,-R6          !       ELIM RTN
0334        JSB  =ERROR 
0335        BYT  89D
0336        RTN  
0338        BYT  32
0340 RED2V  LDMD R36,=BINTAB
0341        JSB  X36,RD2V         !       2 VAR REDIM.
0342        RTN  
0343 RD2V   JSB  =TWOB            !          ROW,COL BIN INTS-R46,R56.
0344        LDM  R24,R46          !       COL TO R24.
0345        LDMD R36,=BINTAB
0346        JSB  X36,STOPT-       !    OPTBAS FOR CALC OR PROG VAR.
0347        ADMD R24,=OPTBAS      !   ADJUST COL PRIOR TO REDIM.
0348        JNG  ER89R            !         INVALID IF NEG.
0349        LDMD R36,=BINTAB
0350        JSB  X36,R1VB         !      DO THE REDIM.
0351        JEZ  RDRTN            !         JIF NO DIM MISMATCH.
0352 ER33R  POMD R36,-R6          !       ELIM ONE RTN
0353        JSB  =ERROR 
0354        BYT  246D
0355        RTN  
0391 RUDIM  CLM  R22
0392        DCM  R22
0393        CLM  R24
0394        JMP  REDIM.
0396        BYT  0,241
0398 REDIM. SAD  
0399        PUMD R70,+R6
0400        BIN  
0401        TSB  R16
0402        JOD  REDI1            !         JIF CALC
0403        ADMD R20,=FWCURR      !  MAKE ADDR ABSOLUTE
0404 REDI1  POMD R36,+R20         !     POP NAME
0405        JPS  NTREMO           !        JIF NOT REMOTE
0406        LDMD R20,R20
0407 NTREMO LDMD R30,=BINTAB
0408        JSB  X30,SETOPT
0409 RED3   LDMD R30,=BINTAB
0410        JSB  X30,ITSLOC       !    REDIMENSION
0411        JSB  =CUROPT          !       AND RESET OPTION BASE
0412        POMD R70,-R6          !      RESTORE R74 - R77
0413        PAD  
0414        RTN  
0415 STOPT- POMD R20,-R12         !      POINTER TO BA.
0416 SETOPT PUBD R16,+R6
0417        CMM  R20,R12
0418        JCY  CALCVB
0419        CLB  R16
0420 CALCVB JSB  =CUROPT
0421        POBD R16,-R6
0422        RTN  
0423 ITSLOC LDM  R76,=10,0
0424        STM  R36,R34          ! SAVE NAME IN CASE TARGET MATRIX.
0425        ANM  R36,=60,100
0426        LDB  R75,R36          ! MOVE TYPE.
0427        CMB  R75,=20          !  REAL TYPE?
0428        DRP  R76              !      SET ARP FOR LATER.
0429        JNC  ABCTST           !  JIF REAL, INCR AMT ALREADY SET.
0430        JZR  INTINC           !  JIF INT.
0431        LDB  R#,=4            !   INCREMENT AMT FOR SHORTS.
0432        JMP  ABCTST           !  C=A*B, SEE IF A,B, OR C.
0433 INTINC LDB  R#,=3            !   INCREMENT AMT FOR INTS.
0434 ABCTST JEN  BCTST            !   JIF NOT ARRAY A.
0435        STMD R75,=TYPA  
0436        JMP  DOLOC            !   GO DO REST OF ITSLOC.
0437 BCTST  DCE                   !         DECREMENT FLAG.
0438        JEN  CTYPE            !   JIF ARRAY C FLAGGED.
0439        STMD R75,=TYPB  
0440        JMP  DOLOC            !   GO DO REST OF ITSLOC.
0441 CTYPE  STMD R75,=TYPC  
0442        STBD R75,=DIMFLG
0443        STBD R37,=TRCFLG
0444        STMD R34,=MTEMP 
0445 DOLOC  LDM  R36,R22
0446        ORM  R36,R24
0447        JPS  REDIM1           !        JIF NOT RUDIM
0448        CLE  
0449        LDMD R36,=OPTBAS      !  RETURN OPT BASE IN 36
0450        DCM  R36
0451        TCM  R36
0452        POMD R56,+R20         !     ARRAY SIZE
0453        POMD R22,+R20         !     MAX ROW
0454        ADMD R#,=OPTBAS       !   ADJUST FOR OPT BASE
0455        POMD R24,+R20         !     MAX COL
0456        JPS  RED5  
0457        CLM  R24
0458        ICM  R24
0459        DCE  
0460        RTN  
0461 RED5   ADMD R#,=OPTBAS       !   ADJUST FOR OPT BASE
0462        RTN  
0463 RDER33 JSB  =ERROR 
0464        BYT  246D
0465        RTN                   !         ERROR EXIT
0466 REDIM1 POMD R36,+R20         !     ARRAY SIZE
0467        LDMD R34,=OPTBAS
0468        JZR  REDIM2           !        JIF OPTION BASE IS 1
0469        TSM  R22              !           TRYING TO REDIM TO NULL?
0470        JZR  RDIMER           !        ERROR IF YES & OPT BAS 0.
0471        TSM  R24              !           TRYING TO REDIM TO NULL?
0472        JZR  RDIMER           !        ERROR IF YES & OPT BAS 0.
0473 REDIM2 LDM  R76,R22
0474        SBM  R76,R34          !       ADJUST FOR OPT BASE
0475        STM  R76,R74          !       ROW
0476        LDM  R76,R24
0477        SBM  R76,R34          !       ADJUST FOR OPT BASE
0478        LDMD R64,R20          !      OLD ROW   COL
0479        CMM  R66,=377,377     !  VECTOR?
0480        JNZ  NTVC1            !         JIF NO
0481        CMM  R24,=1,0
0482        JNZ  NTVC1            !         JIF NOT N X 1
0483        LDM  R76,R66
0484 NTVC1  XRM  R64,R74
0485        XRM  R66,R64
0486        ANM  R66,=000,200     ! OR BOTH POS
0487        JNZ  RDER33           !       JIF NO
0488        JSB  =CALCSZ          !       GO CALC ARRAY SIZE
0489        CLE  
0490        CMM  R36,R56          !       MAX SIZE - NEW SIZE
0491        JNG  RDIMER           !        JIF TOO BIG
0492 REDEX  LDM  R36,R56
0493        TSM  R76
0494        JPS  REDEX1           !        JIF NOT VECTOR
0495        CLM  R24
0496        ICM  R24
0497        DCE  
0498 REDEX1 PUMD R74,+R20         !     NEW ROW/COL
0499        LDMD R76,=BINTAB
0500        CLB  R75
0501        ICB  R75
0502        STBD R75,X76,RDMFLG
0503        RTN  
0504 RDIMER JSB  =ERROR 
0505        BYT  242D
0506        RTN                   !         ERROR EXIT.
0508 ERMSG  BYT  200              !                       0
0509        BYT  200              !                       1
0510        BYT  200              !                       2
0511        BYT  200              !                       3
0512        BYT  200              !                       4
0513        BYT  200              !                       5
0514        BYT  200              !                       6
0515        BYT  200              !                       7
0516        BYT  200              !                       8
0517        ASC  6,# DIMS
0518        BYT  240
0519        BYT  200              !                       10
0520        BYT  200              !                       11
0521        BYT  200              !                       12
0522        ASC  10,DIM SIZE
0523        BYT  240
0524        BYT  377              !           END OF TABLE
0525 TWOB   DAD  56176
0526 ROMFL  DAD  101231
0527 FWUSER DAD  100000
0528 FWPRGM DAD  100002
0529 FWCURR DAD  100004
0530 BINTAB DAD  101233
0531 ERROR  DAD  6615
0532 NUMVA+ DAD  12407
0533 NUMVAL DAD  12412
0534 NARREF DAD  13402
0535 ONEB   DAD  56113
0536 PUSH45 DAD  14266
0537 SCAN   DAD  11262
0538 STOSV  DAD  45254
0539 DALLOC DAD  42414
0540 ALLOC  DAD  40034
0541 INIVAR DAD  43670
0542 CONTOK DAD  100024
0543 INIVLP DAD  43715
0544 EQUALS DAD  65
0545 OPEN   DAD  50
0546 COMMA  DAD  54
0547 CLOSE  DAD  51
0548 ZERO1- DAD  44137
0549 TRCFLG DAD  101157
0550 INCRC  DAD  101155
0551 MTEMP  DAD  101126
0552 FETSVX DAD  44540
0553 OPTBAS DAD  100164
0554 CUROPT DAD  44500
0555 TYPA   DAD  101120
0556 TYPB   DAD  101123
0557 TYPC   DAD  101154
0558 DIMFLG DAD  101173
0559 CALCSZ DAD  43557
0560        FIN  
