0001 !       HED ZER, REDIM BINAR
0002        ASC  6,ZEREDM NAME
0003 !        OCT 14
0004        BSZ  21
0005 ! 
0006 BASE   BSZ  2
0007        DEF  RUNTIM
0008        DEF  TOKENS
0009        DEF  PARSE 
0010        DEF  ERMSG 
0011        DEF  INIT  
0012 ! 
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
0024 ! 
0025 PARSE  BSZ  2
0026        DEF  REDIM            !   REDIM     1
0027        DEF  ZER              !     ZER       2
0028        DEF  MAT              !     MAT       3
0029 !        OCT 377,37
0030 ! 
0031 ! INIT   LDBD R32=ROMF
0032        JZR  FLGSET
0033 ! INIOUT CMB R#=
0034        JZR  RUNHIT
0035 !        CMB R#=
0036        JNZ  CKCOM 
0037 ! FLGSET LDB R33=
0038        JMP  FLGSTR
0039 ! CKCOM  CMB R#=
0040        JNZ  INIRTN
0041 !        LDMD R36=FWUSE
0042 !        CMMD R36=FWPRG
0043        JNZ  INIRTN
0044 ! RUNHIT LDMD R36=BINTA
0045        LDBD R36,X36,RDMFLG
0046        JZR  INIRTN
0047        JSB  =DALLOC
0048        JSB  =ALLOC 
0049        JSB  =INIVAR
0050        CLB  R36
0051 !        STBD R36=CONTO
0052 !        LDMD R36=FWUSE
0053 !        LDMD R32=FWPRG
0054        CMM  R32,R36
0055        JZR  FLGCLR
0056        JSB  =INIVLP
0057 FLGCLR CLB  R33
0058 ! FLGSTR LDMD R36=BINTA
0059        STBD R33,X36,RDMFLG
0060 INIRTN RTN  
0061 ! 
0062 TOKENS ASC  4,REDIM !REDIM     1 
0063        VAL  M     
0064        ASC  2,ZER !  ZER       2 
0065        VAL  R     
0066        ASC  2,MAT !  MAT       3 
0067        VAL  T     
0068 !        OCT 377 !              
0069 ! ******  PARSER QUITS SEARCHING HERE !****************
0070        ASC  2,ZER !  ZER       5 
0071        VAL  R     
0072        ASC  2,ZER !  ZER()     6 
0073        VAL  R     
0074        ASC  2,ZER !  ZER(,)    7 
0075        VAL  R     
0076 !        OCT 275 !    DUMMY=    1
0077 !        OCT 37
0078 ! 
0079 M      EQU  315
0080 R      EQU  322
0081 T      EQU  324
0082 ! 
0083 ZDMTOK EQU  5
0084 RDMTOK EQU  11
0085 EQUTOK EQU  10
0086 ! 
0087 RDMFLG BSZ  1
0088 ! 
0089 ! ****  OTHER ATTRIBUTES !***************************
0090 !        OCT 4
0091 ! ***************************************************
0092 DUMMY  BSZ  0
0093 OTHER  RTN  
0094 ! 
0095 ! ****  MAT ATTRIBUTES !******************************
0096 !        OCT 24
0097 ! ***************************************************
0098 RDIM.  BSZ  0
0099 MAT.   RTN  
0100 ! 
0101 ! ****  DUMMY= ATTRIBUTES !***************************
0102 !        OCT 5,5
0103 ! ****************************************************
0104 DUMMY= RTN  
0105 ! 
0106 ! MAT    LDB R51=37
0107 !        PUBD R51+R1
0108 !        PUBD R51+R1
0109 !        PUBD R43+R1
0110        JSB  =SCAN  
0111        JSB  =NARREF
0112 !        CMB R14=EQUAL
0113        JNZ  ERR89 
0114        JSB  =SCAN  
0115        BIN  
0116 !        CMB R43=
0117        JZR  ZER   
0118 ERR89  JSB  =ERROR 
0119 !        OCT 89
0120        RTN  
0121 ! ZER    LDB R32=ZDMTO
0122 !        PUBD R32+R
0123        JSB  =SCAN  
0124 !        CMB R14=OPE
0125        JNZ  PRM-  
0126        ICB  R32
0127        JSB  =SCAN  
0128 !        POBD R70-R
0129 !        LDMD R30=BINTA
0130        JSB  X30,SUBSCR
0131        JEZ  ERR89 
0132 !        LDB R53=37
0133 !        PUBD R53+R1
0134 !        PUBD R53+R1
0135 !        LDB R53=EQUTO
0136 !        PUBD R53+R1
0137        RTN  
0138 ! REDIM  LDB R51=37
0139 !        PUBD R51+R1
0140 !        PUBD R51+R1
0141 !        PUBD R43+R1
0142 ALOOP  JSB  =SCAN  
0143 !        CMB R14=
0144        JNZ  ERR89 
0145        JSB  =PUSH45
0146 !        LDB R32=RDMTO
0147 !        LDMD R30=BINTA
0148        JSB  X30,SUBSCR
0149        JEZ  ERR89 
0150 !        CMB R14=COMM
0151        JZR  ALOOP 
0152        RTN  
0153 ! 
0154 ! PRM-   LDB R51=37
0155 !        PUBD R51+R1
0156 !        PUBD R51+R1
0157 !        POBD R53-R
0158 !        PUBD R53+R1
0159 !        LDB R53=EQUTO
0160 !        PUBD R51+R1
0161 !        PUBD R51+R1
0162 !        PUBD R53+R1
0163        RTN  
0164 ! 
0165 ! SUBSCR PUBD R36+R
0166        JSB  =NUMVAL
0167 !        POBD R36-R
0168        JEZ  SUBRTN
0169 !        CMB R14=COMM
0170        JNZ  RTPAR 
0171        ICB  R32
0172 !        PUBD R36+R
0173        JSB  =NUMVA+
0174 !        POBD R36-R
0175        JEZ  SUBRTN
0176 ! RTPAR  CMB R14=CLOS
0177        CLE  
0178        JNZ  SUBRTN
0179        JSB  =SCAN  
0180 !        LDB R51=37
0181 !        PUBD R51+R1
0182 !        PUBD R51+R1
0183 !        PUBD R32+R1
0184        CLE  
0185        ICE  
0186 SUBRTN RTN  
0187 !     HED MAT A = ZER, ZER(), ZER(,
0188 ! ***  ZER(M) ATTRIBUTES TABLE !*****************
0189 !        OCT 20,5
0190 ! ***********************************************
0191 ! ZDIM1V LDMD R36=BINTA
0192 !        JSB X36,DUP1V DUP MAT ADDR PTR ON R12
0193 !        JSB X36,RD1V REDIM TARGET ARRAY
0194        JMP  ZER.             !    GO SET IT = ZERO.
0195 ! ***  ZER(M,N) ATTRIBUTES TABLE !***************
0196 !        OCT 40,5
0197 ! ***********************************************
0198 ! ZDIM2V POMD R50-R12 GET 1ST SUBSCRIPT
0199 !        LDMD R36=BINTA
0200 !        JSB X36,DUP1V DUP & RESTORE
0201 !        PUMD R50+R12 RESTORE 1ST SUBSCRIPT
0202 !        JSB X36,RD2V REDIM TARGET ARRAY
0203        JMP  ZER.             !    GO SET IT = ZERO.
0204 ! ***  ZER (MAT) ATTRIBUTES TABLE !**************
0205 !        OCT 0,5
0206 ! ***********************************************
0207 ! ZER.   POMD R20-R12 GET C OFFSET
0208 !        PUMD R20+R12 RESTORE FOR LOCSZ-
0209 !        PUMD R20+R12 ONE MORE COPY FOR RDIM
0210 !        LDMD R36=BINTA
0211 !        JSB X36,LOCSZ- GET M,N,BASE,INCRC,TYPC,BIN
0212        CLE                   !         CLEAR FLAG.
0213        DCE                   !         FLAG SETTING FOR TARGET MATRIX.
0214 !        POMD R20-R12 GET BASE POINTER
0215 !        LDMD R36=BINTA
0216 !        JSB X36,REDIM. REDIMENSION ARRAY
0217        TSM  R36
0218        JZR  ZERTN            !   DONE IF NULL ARRAY.
0219 !        LDMD R36=BINTA
0220 !        JSB X36,VECFLG SETUP TRCFLG FOR TRACE LATER
0221 !        CMB R17=300 !  FOR REDIM ERROR CHECK
0222        JNC  ERROUT           !  JIF NO REDIM ERROR.
0223 ZERTN  RTN  
0224 ! ERROUT LDMD R76=INCRC INCR AMT TO R76
0225 !        LDB R0=70 !  WILL ALTER
0226        SBB  R0,R76           !  REAL=60,SHORT=64,INT=65.
0227        CLM  R60              !     CONST=0.
0228        STM  R20,R36          ! STARTING ADDR TO R36.
0229        STM  R20,R72          ! ANOTHER COPY FOR CKTRC.
0230        JSB  =ZERO1-          ! PUSH OUT CONSTS (0'S OR 1'S).
0231        JMP  CKTRC 
0232 LOCSZ- CLE                   !         CLEAR FLAG.
0233        DCE                   !         FLAG SETTING FOR TARGET MATRIX.
0234 !        POMD R20-R12 GET PTR TO STARTING ADDRESS
0235 !        LDMD R36=BINTA
0236 !        JSB X36,RUDIM R22=R24=0 THEN REDIM
0237        BIN                   !         SET MODE.
0238 ! VECFLG LDBD R47=TRCFLG NEED TO TAG RT BIT IF A VEC
0239 !        ANM R47=360 !CLEAR RT BITS
0240        JEZ  FLGSTO           !  JIF TARGET MATRIX IS NOT A VECTOR.
0241        ICB  R47              !     TAG THIS AS A VECTOR.
0242 ! FLGSTO STBD R47=TRCFLG TRACE FLAG IS NOW UPDATED
0243        RTN                   !         RETURN.
0244 ! 
0245 ! DUP1V  POMD R40-R12 GET V1
0246 !        POMD R32-R12 GET MAT ADDR PTR
0247 !        PUMD R32+R12 RESTORE MAT ADDR PTR
0248 !        PUMD R32+R12 DUP MAT ADDR PTR
0249 !        PUMD R40+R12 RESTORE SUBSCRIPT
0250        RTN  
0251 ! CKTRC  LDBD R46=TYPC GET TYPE OF RESULT ARRAY
0252        ARP  R72
0253 !        LDMD R36=BINTA
0254 !        JSB X36,FETCH- GET C(1,1)
0255        DRP  R34              !      STORE IT WHERE IT CAME FROM.
0256 STOV   BIN                   !         SET MODE.
0257 !        PUMD R#+R1
0258 !        ADMD R#=INCR
0259 !        LDB R56=31
0260 !        LDBD R57=TRCFL
0261        JLZ  NOTRC 
0262 !        PUBD R56+R1
0263 !        PUBD R56+R1
0264 !        PUBD R56+R1
0265 !        PUBD R56+R1
0266 !        ANM R57=1
0267 !        STBD R57=TRCFL
0268 !        PUBD R57+R1
0269 !        LDB R57=37
0270        JMP  CNAME 
0271 ! NOTRC  LDB R57=27
0272 ! CNAME  ANMD R56=MTEM
0273 !        PUMD R0+R
0274 !        PUMD R2+R
0275 !        PUMD R14+R
0276 !        PUMD R70+R
0277        LDM  R70,R20
0278 !        PUMD R70+R
0279        LDM  R70,R30
0280 !        PUMD R70+R
0281 !        LDBD R77=TYP
0282        ORB  R56,R77
0283 !        PUMD R56+R1
0284 !        PUMD R40+R1
0285        JSB  =STOSV 
0286        JMP  GETREG
0287 FETCH- LDM  R34,R#
0288 ! FETCH  PUMD R0+R
0289 !        PUMD R2+R
0290 !        PUMD R14+R
0291 !        PUMD R70+R
0292        LDM  R70,R20
0293 !        PUMD R70+R
0294        LDM  R70,R30
0295 !        PUMD R70+R
0296        JSB  =FETSVX
0297        BIN  
0298        STM  R60,R40
0299 ! GETREG POMD R70-R
0300        STM  R70,R30
0301 !        POMD R70-R
0302        STM  R70,R20
0303 !        POMD R70-R
0304 !        POMD R14-R
0305 !        POMD R2-R
0306 !        POMD R0-R
0307        RTN  
0308 !   HED REDIMENSION ROUTINE
0309 ! ************ !REDIM 1 SUBSCRIPT ROUTINE  **********************
0310 !         OCT 3
0311 ! ***************************************************************
0312 ! RED1V  LDMD R36=BINTA
0313 !        JSB X36,RD1V REDIM 1V ARRA
0314        RTN  
0315 RD1V   CLM  R24              !           READY TO DECLARE A VECTOR.
0316        ICM  R24              !           THIS IS A VECTOR.
0317        JSB  =ONEB            !          BINARY INT TO R46.
0318 !        LDMD R36=BINTA
0319 !        JSB X36,STOPT- OPTBAS-CALC OR PROG VAR
0320 !        LDMD R36=BINTA
0321        JSB  X36,R1VA         !      1V REDIM.
0322        JEZ  ER33R            !         JIF DIM MISMATCH.
0323 RDRTN  RTN  
0324 R1VA   DRP  R46
0325        JMP  R1V   
0326 R1VB   DRP  R56
0327 ! R1V     ADMD R#=OPTBAS !   ADJUST PRIOR TO REDIM
0328        STM  R#,R22           !        MOVE ROW TO R22.
0329        CLE  
0330        DCE                   !               FLAG TYPE FOR REDIM.
0331        JPS  REDIM.           !        JIF OK.
0332 ! ER89R-  POMD R36-R6 !      ELIM RT
0333 ! ER89R   POMD R36-R6 !      ELIM RT
0334        JSB  =ERROR 
0335 !         OCT 89
0336        RTN  
0337 ! ************* REDIM 2 VAR ROUTINE !********************************
0338 !         OCT 3
0339 ! *******************************************************************
0340 ! RED2V  LDMD R36=BINTA
0341        JSB  X36,RD2V         !       2 VAR REDIM.
0342        RTN  
0343 RD2V   JSB  =TWOB            !          ROW,COL BIN INTS-R46,R56.
0344        LDM  R24,R46          !       COL TO R24.
0345 !        LDMD R36=BINTA
0346        JSB  X36,STOPT-       !    OPTBAS FOR CALC OR PROG VAR.
0347 !         ADMD R24=OPTBAS !  ADJUST COL PRIOR TO REDIM
0348        JNG  ER89R            !         INVALID IF NEG.
0349 !        LDMD R36=BINTA
0350        JSB  X36,R1VB         !      DO THE REDIM.
0351        JEZ  RDRTN            !         JIF NO DIM MISMATCH.
0352 ! ER33R   POMD R36-R6 !      ELIM ONE RT
0353        JSB  =ERROR 
0354 !         OCT 246
0355        RTN  
0356 ! 
0357 ! 
0358 !   SUBROUTINE REDI
0359 ! 
0360 !   THIS ROUTINE IS CALLED TO REDIMENSION A
0361 !   ARRAY OR TO RETURN THE CURRENT DIMENSIONS
0362 ! 
0363 !   INPU
0364 ! 
0365 !   R20   = ARRAY ADD
0366 !   R22   = MAX ROW OR ZER
0367 !   R24   = MAX COL OR ZER
0368 ! 
0369 !   OUTPUT
0370 ! 
0371 !   IF R22 = -1 & R24 = 0, THE CURRENT MAX RO
0372 !   & COL WILL BE RETURNED IN R22 & R24
0373 !   OPTION BASE WILL BE RETURNED IN 36
0374 !   E = 0 IF MATRIX ELSE E # 0 IF VECTOR
0375 ! 
0376 !   IF R22 & R24 ARE NON-NEG THE ARRAY WILL B
0377 !   REDIMENSIONED AND THE NEW ARRAY SIZ
0378 !   RETURNED IN R36
0379 !   R24=1,0 FOR VECTO
0380 ! 
0381 !   ALL  ROW & COL DIMENSIONS ARE REL TO OPTIO
0382 !   BASE 1
0383 ! 
0384 !   ENTRY REDIM. WILL USE THE OPTION BAS
0385 !   OF THE PROGRAM WITHIN WHICH THE ARRA
0386 !   RESIDES
0387 ! 
0388 !   ENTRY RUDIM WILL SET R22=-1, CLR R24, & REDIM
0389 ! 
0390 ! 
0391 RUDIM  CLM  R22
0392        DCM  R22
0393        CLM  R24
0394        JMP  REDIM.
0395 ! ***  TOKEN 157 ATTRIBUTE TABLE !****************
0396 !         OCT 0,24
0397 ! ************************************************
0398 REDIM. SAD  
0399        PUMD R70,+R6
0400        BIN  
0401        TSB  R16
0402        JOD  REDI1            !         JIF CALC
0403        ADMD R20,=FWCURR      !  MAKE ADDR ABSOLUTE
0404 REDI1  POMD R36,+R20         !     POP NAME
0405        JPS  NTREMO           !        JIF NOT REMOTE
0406        LDMD R20,R20
0407 ! NTREMO LDMD R30=BINTA
0408        JSB  X30,SETOPT
0409 ! RED3    LDMD R30=BINTA
0410        JSB  X30,ITSLOC       !    REDIMENSION
0411        JSB  =CUROPT          !       AND RESET OPTION BASE
0412        POMD R70,-R6          !      RESTORE R74 - R77
0413        PAD  
0414        RTN  
0415 ! STOPT-  POMD R20-R12 !     POINTER TO BA
0416 ! SETOPT  PUBD R16+R
0417        CMM  R20,R12
0418        JCY  CALCVB
0419        CLB  R16
0420 CALCVB JSB  =CUROPT
0421 !         POBD R16-R
0422        RTN  
0423 ! ITSLOC LDM R76=10,0 INCREMENT AMOUNT IF REAL
0424        STM  R36,R34          ! SAVE NAME IN CASE TARGET MATRIX.
0425 !        ANM R36=60,100 ISOLATE TYPE AND TRACE FLAG. 
0426        LDB  R75,R36          ! MOVE TYPE.
0427 !        CMB R75=20 ! REAL TYPE
0428        DRP  R76              !      SET ARP FOR LATER.
0429        JNC  ABCTST           !  JIF REAL, INCR AMT ALREADY SET.
0430        JZR  INTINC           !  JIF INT.
0431        LDB  R#,=4            !   INCREMENT AMT FOR SHORTS.
0432        JMP  ABCTST           !  C=A*B, SEE IF A,B, OR C.
0433 INTINC LDB  R#,=3            !   INCREMENT AMT FOR INTS.
0434 ABCTST JEN  BCTST            !   JIF NOT ARRAY A.
0435 !        STMD R75=TYPA SAVE TYPA AND INCRA
0436        JMP  DOLOC            !   GO DO REST OF ITSLOC.
0437 BCTST  DCE                   !         DECREMENT FLAG.
0438        JEN  CTYPE            !   JIF ARRAY C FLAGGED.
0439 !        STMD R75=TYPB SAVE TYPB AND INCRB
0440        JMP  DOLOC            !   GO DO REST OF ITSLOC.
0441 ! CTYPE  STMD R75=TYPC SAVE TYPC AND INCRC
0442 !        STBD R75=DIMFLG NEEDED FOR STOSV
0443 !        STBD R37=TRCFLG SAVE TRACE FLAG
0444 !        STMD R34=MTEMP SAVE TARGET NAME
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
0458 !         IC
0459        DCE  
0460        RTN  
0461 RED5   ADMD R#,=OPTBAS       !   ADJUST FOR OPT BASE
0462        RTN  
0463 RDER33 JSB  =ERROR 
0464 !        OCT 246
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
0496 !         IC
0497        DCE  
0498 REDEX1 PUMD R74,+R20         !     NEW ROW/COL
0499 !         LDMD R76=BINTA
0500        CLB  R75
0501        ICB  R75
0502        STBD R75,X76,RDMFLG
0503        RTN  
0504 RDIMER JSB  =ERROR 
0505 !         OCT 242
0506        RTN                   !         ERROR EXIT.
0507 !         HED MATH ERROR MESSAGE
0508 ! ERMSG   OCT 200 !                      
0509 !         OCT 200 !                      
0510 !         OCT 200 !                      
0511 !         OCT 200 !                      
0512 !         OCT 200 !                      
0513 !         OCT 200 !                      
0514 !         OCT 200 !                      
0515 !         OCT 200 !                      
0516 !         OCT 200 !                      
0517        ASC  6,# DIMS !                 9
0518 !         OCT 24
0519 !         OCT 200 !                      1
0520 !         OCT 200 !                      1
0521 !         OCT 200 !                      1
0522        ASC  10,DIM SIZE !              13 
0523 !         OCT 24
0524 !         OCT 377 !          END OF TABL
0525 !         LST FOR EN
0526 !         UN!L FOR FI
0527        FIN  
