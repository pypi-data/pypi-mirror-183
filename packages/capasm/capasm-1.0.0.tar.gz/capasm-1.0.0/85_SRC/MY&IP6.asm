0010 !  MY&IP6-6TH PART IPBIN (NEW
0020 ! --------------------------------------------------
0030 ! KEYBOARD IS binary is merged here in its entirety..
0040 !       LS
0050 !        HED KEYBOARD IS BINAR
0060 ! *********************************************
0070 !             !                                
0080 !    BINARY TO PERFORM !                       
0090 !      KEYBOARD IS <input select code> !       
0100 !             !    [,<handshake exp>           
0110 !            !      ]                          
0120 !            !                                 
0130 !    Ole Anderson, July 1980 !                 
0135 !    LAST UPDATE : FEB 198
0140 !            !                                 
0150 ! *********************************************
0160 ! Description
0170 ! This binary feeds the system characters fro
0180 ! an incoming IO character stream (e.g. RS-232 or HP-IB
0190 ! when it is in calculator or program input modes
0200 ! This allows a remote IO device to have nearl
0210 ! total control over Capricorn. The exceptions are tha
0220 ! SCRATCH and LOAD are prohibited because they woul
0230 ! destroy the binary that enables the process
0240 ! 
0250 ! This binary assumes that the IO card has been se
0260 ! up to cause an interrupt when the RESET function i
0270 ! desired, from previous action (e.g. ENABLE INTR s;ex
0280 ! where exp means receipt of BREAK on RS-232). Whe
0290 ! this occurs the the binary does a RESET, afte
0300 ! its card is removed from the LOGON table (t
0310 ! prevent it from being reset and accidently breakin
0320 ! modem or other connection). After calling reset i
0330 ! is replaced in the LOGON table IOBITS
0340 ! This is for getting back into a good state if the machin
0350 ! hangs
0360 ! 
0370 ! The 2rd param is for potential handshaking
0380 !         0 means no handshake
0390 !         1 means XON/XOF (also known as DC3,DC1) fo
0400 !           full-duplex mode
0410 !  This works as follows
0420 !   XOFF=<control>S=chr$(19) is sent by th
0430 !       binary after ENTERs
0440 !   XON=<control>Q=chr$(17) is sent before 
0450 !      new ENTER is begun
0460 !  This allows the binary to say when it can accept inpu
0470 !  and when it is busy (e.g. parsing or running)
0480 ! 
0490 ! System input is returned to the keyboard wit
0500 ! either a LOAD/SCRATCH operation or 
0510 !  KEYBOARD IS 
0520 ! the latter leaving the binary intact
0530 ! 
0540 !        ASC 6,KEYBD !      BINARY NAM
0550 !        BYT 142 !          BINARY ID ..
0560 !        BSZ 17D !          SPACE FOR HEADE
0570 ! *********************************************
0580 !        BSZ 2 !            BINARY BASE ADDRES
0590 !        DEF RUNTIM
0600 !        DEF TOKEN
0610 !        DEF PARS
0620 !        DEF ERMS
0630 !        DEF INI
0640 ! *********************************************
0650 ! RUNTIM  BSZ 
0660 !        DEF KBDIS
0670 ! *********************************************
0680 ! PARSE   BSZ 
0690 !        DEF KBDI
0700 !        BYT 377,37
0710 ! *********************************************
0720 ! TOKENS ASC 11D,KEYBOARD I
0730 !      BYT 240 !     BLANK WITH PARIT
0740 !       BYT 377 !           END OF LIS
0750 ! *********************************************
0760 ! ERMSG  BYT 200 !           DUMM
0770 !       BYT 377 !           END OF LIS
0780 ! **********************************************
0790 ! HLPRTN  BSZ 
0800 ! TEST FOR BINARY DESTRUCTION
0810 ! (SCRATCH,LOAD destroy binary
0820 ! In these cases, cancel the idle hook
0830 !      LDBD R40,=ROMFL WHAT TYPE INIT
0840 !      CMB R40,=2 !  SCRATC
0850 !      JZR KILID
0860 !      CMB R40,=5 !  LOA
0870 !      JZR KILID
0880 !      RT
0890 ! ------------------------------------------------
0900 KILIDL BSZ  0                !     CANCEL IDLE HOOK
0910        LDB  R30,=236         ! !'RTN'
0920        STBD R30,=RMIDLE
0930 ! cancel ISR change
0940        STBD R#,=GINTEN       !     !!!
0950        LDM  R45,=262         ! !STBD R#,=GINTDS
0960        DEF  GINTEN
0970        STMD R45,=IRQIEN
0980        STBD R#,=GINTEN
0990        RTN  
1000 ! -------------------------------------------------
1010 !        HED PARSE ROUTINE
1020 KBDIS  BIN  
1030        LDMD R36,=BINTAB      !   GET BASE ADDRESS
1040        LDM  R70,R40          !        SAVE OUR TOKEN
1050        JSB  =NUMVA+          !  GET A NUM.EXP.
1060        JEZ  SYNTER
1070 ! 2ND PARAM
1075 COMMA  EQU  54
1080        CMB  R14,=COMMA 
1090        JNZ  PRSRTN
1100        JSB  =NUMVA+
1110        JEZ  SYNTER
1120 PRSRTN LDB  R52,=371         !       BINARY TOKEN
1130        PUBD R52,+R12
1140        PUBD R71,+R12
1150        PUBD R73,+R12
1160        RTN  
1170 ! ----------------------
1180 SYNTER JSB  =ERROR 
1190        BYT  92D              !       SYSTEM SYNTAX
1200        RTN  
1210 IOROM# EQU  300
1220 ! 
1230 KIDLE  JMP  KILIDL
1240 !       HED KEYBOARD I
1250 ! 
1260 ! Method used by this binary to perform char inpu
1270 ! is equivalent to doing the following
1280 !      ENTER S;B
1290 ! where B$ is the binary pseudo-string (as in BASIC)
1300 ! Since this BASIC statement parses t
1310 !      S <TAD.> <ENTER.> ; B$ <ENTER$.> <END_ENTER.
1320 ! this is done by pushing the binary buffer addr B
1330 ! and S on the param stack
1340 ! then calling the runtime routines to simulat
1350 ! BASIC
1360 ! This ENTER operation is performed once for each lin
1370 ! entered when the system desires one and the buffer i
1380 ! empty. Then a char at a time is passed to the syste
1390 ! until the buffer is empty, whereupon the NEWLIN flag is reset
1400 ! 
1410        BYT  241
1420 KBDIS. LDMD R20,=BINTAB
1430 ! STASH params for ENTER and restar
1440        BIN  
1450 ! how many params
1460        CLB  R46              !      DEFAULT HANDSK=0
1470        LDM  R30,R12
1480        SBMD R30,=TOS         !  COMPUTES BYTES OF PARAM
1490        CMB  R30,=8D          ! !1 # ?
1500        JZR  ONE#  
1510 ! MUST HAVE 2 NUMS
1520        JSB  =ONEB            !    R46:=REAL OFF R12
1530 ONE#   STBD R46,X20,HANDSH   !  HANDSHAKE PARAM
1540        POMD R40,-R12
1550        PUMD R40,+R12         !   FOR ONEB
1560        STMD R40,X20,SELCOD   !  SELECT CODE
1570        JSB  =ONEB            !    SEL COD IS BINARY
1580        DCM  R46              !      KEYBOARD IS 1 ?
1590        JZR  KILIDL           !   YES:WE'RE DONE
1600 ! MAKE IOBITS MASK FROM SEL.COD
1610        SBB  R46,=2           !   0>=R46<=7D
1620        LDB  R47,=1           !   2^0=1
1630 SCLOOP DCB  R46
1640        JNG  SCDONE
1650        LLB  R47
1660        JMP  SCLOOP
1670 SCDONE BSZ  0                !     R47=(SC-3)^2
1680        STBD R47,X20,SCMASK
1690 ! 
1700 ! EOL PROCESSING FOR RMIDLE
1710 NLINE  LDMD R20,=BINTAB
1720        CLB  R30
1730        STBD R30,X20,GIVTIM   !  RMIDLE BREATHER
1740 ! START WITH A NEW LINE
1750        ICB  R30
1760        STBD R30,X20,NEWLIN   !  START A NEW LINE
1770 ! INSERT IDLE HOOK
1780        LDM  R44,=316         ! IE 'JSB'
1790        DEF  NUKEY            !   =NUKEY
1800        RTN  
1810        LDMD R20,=BINTAB      !  CORRECT NUKEY ADDR
1820        ADM  R20,R45
1830        STM  R20,R45          !  NUKEY+BASE
1840        STMD R44,=RMIDLE      !  INSERT IDLE HOOK
1850 ! INSTALL NEW ISR
1860        LDM  R45,=316         ! !JSB
1870        DEF  MYISR 
1880        ADMD R46,=BINTAB
1890 ! R45:= JSB =MYIS
1900        STMD R45,=IRQIEN
1910 KEYRTN RTN  
1920 ! 
1930 OVER   JMP  KIDLE 
1940 !       HED ROM IDLE HOO
1950 ! THE IDLE HOOK:(UNTIL EOF) PASS 1 KEY AT A TIM
1960 !  TO CAPRICORN VIA KEYHIT, WHEN IT NEEDS ANOTHER
1970 NUKEY  BSZ  0                ! 
1980        LDMD R20,=SVCWRD      ! DONE WITH LAST KEY?
1990        JOD  KEYRTN           !   NOPE
2000 ! HP-85 MODES
2010 !  R16      MOD
2020 !  0        IDL
2030 !  4        INPU
2040 !  1        CALC EXECUTE INPU
2050 !  2        RU
2060 !  3,6      NOT USE
2070 !  5        INPUT EXECUTE INPU
2080 ! therefore accept keys in modes 0,4 else idle returns
2090        TSB  R16              !      = 0 ?
2100        JZR  KEYON            !    RUN MODE ACEPTS
2110        CMB  R16,=4           !   WAITING FOR INPUT?
2120        JNZ  KEYRTN           !   NOPE
2130 KEYON  LDMD R20,=BINTAB
2140 ! EOL PROCESSING
2150        LDBD R30,X20,GIVTIM   !  NEED BREATHER?
2160        JZR  TIMOK            !    NOPE
2170        CLB  R30
2180        STBD R30,X20,GIVTIM   !  JUST ONCE!
2190        RTN                   !         NOTHING THIS TIME
2200 TIMOK  BSZ  0
2210 ! END EOL PROCES
2220        JSB  X20,GETASC       !  R60:=CHAR ENTERED
2230        CMB  R17,=300         ! SYS ERRS RTN HERE
2240        JCY  OVER             !     EOF OR ERROR
2250 ! NOTE GETASC IS GUARANTEED TO RETURN A CHAR IN R6
2260        STBD R22,=GINTDS      ! PROTECT SVCWRD
2270        STBD R60,=KEYHIT      !  GIVE TO SYSTEM
2280        LDMD R22,=SVCWRD      !  FLAG KBD SRVC REQUEST
2290        ICB  R22
2300        STMD R22,=SVCWRD
2310        LDB  R22,=20          !  BIT 4
2320        ORB  R17,R22          !  REQUEST SERVICE
2330        STBD R#,=GINTEN
2340        RTN  
2350 !       HED GET CHAR FROM IO BUFFE
2360 GETASC BSZ  0                !       GET A CHAR OR ENDLINE
2370        LDMD R20,=BINTAB
2380        LDBD R30,X20,NEWLIN   !  NEW LINE?
2390        JNZ  ITSNEW           !   YES!
2400 ! GET A REAL KEY FROM BUFFE
2410 ! SET FLAG IF IT'S A <CR
2420        LDMD R26,X20,INPTR 
2430        POBD R60,+R26
2440        STMD R26,X20,INPTR 
2450 ! MAKE <CR> INTO <ENDLINE> AND FLAG NEW LINE
2455 CR     EQU  15
2460        CMB  R60,=CR          !  WAS ENTERED CHAR A <CR>?
2470        JNZ  GETRTN           !   NOPE
2480 ! IT'S A <CR>. DO THE XCHANG
2490        LDB  R60,=232         ! <CR> BECOMES <ENDLINE>
2500        LDB  R30,=1           !   NEED A CLEAR
2510        STBD R30,X20,NEWLIN   ! FLAG NEW LINE
2515        STBD R30,X20,GIVTIM
2520 GETRTN RTN  
2530 ! -------------------------------------------
2540 ITSNEW CMB  R30,=2
2550        JZR  NEWENT
2560 ! CLEAR IS SENT TO DISABLE SCREEN EDIT
2570        ICB  R30              !           R30:=2
2580        STBD R30,X20,NEWLIN   !  FLAG SH-BACKSP SENT
2590        LDB  R60,=146D        !     CLEAR
2600        RTN  
2610 ! --------------------------------------------
2620 NEWENT CLB  R30              !  ITS A NEW LINE TO ENTER
2630        STBD R30,X20,NEWLIN   !  CANCEL NEW LINE
2640 ! GIVE THE SYSTEM SOME TIME TO CHANGE STATE
2650        LDB  R30,=1
2660        STBD R30,X20,GIVTIM
2670 ! SET UP BUFFER PTR TO FRONT OF BUFFER
2680        LDM  R30,R20
2690        ADM  R30,=KBUFF+
2700        STMD R30,X20,INPTR 
2710 ! IF HANDSHAKE ENABLED THEN SEND XON TO PROMPT REMOTE USE
2720        LDBD R30,X20,HANDSH
2730        JZR  NOHAND           !   NO HANDSHAKE
2740 ! PROMPT WITH XON
2750        LDB  R30,=17D
2760        JSB  X20,OUT   
2770 ! DO THE ENTER S; B
2780 NOHAND BSZ  0                ! 
2790 ! PARAM THE SELECT COD
2800        STMD R12,=TOS         !  SIMULATE BASIC
2810        LDMD R40,X20,SELCOD
2820        PUMD R40,+R12
2830 ! DO THE IOROM RUNTIM
2840        JSB  =ROMJSB
2850        DEF  TAD.  
2860        VAL  IOROM#
2870        CMB  R17,=300
2880        JCY  GETRTN
2890        JSB  =ROMJSB
2900        DEF  EI_ENT
2910        VAL  IOROM#
2920        CMB  R17,=300
2930 GET!   JCY  GETRTN
2940 ! SAVE CCRADR FOR TERMINATING ENTER AFTER RESETIN
2950        LDMD R24,X22,CCRADR
2960        LDMD R22,=BINTAB
2970        STMD R24,X22,MYCCR 
2980 ! SIMULATE A BASIC STR REF
2990 ! "RELOCATE" IMAGE POINTER
3000 ! 10/15/80: remove image specifier from ENTER strin
3010 !      LDM R20,R2
3020 !      LDMD R40,X20,EIMAGE ! ENTE
3030 !      ADM R22,R4
3040 !      STM R22,R4
3050 !      STM R22,R4
3060 !      STMD R40,=IMSLE
3070        LDMD R20,=BINTAB
3080        LDM  R56,=KBUFF       !  STRING NAME
3090        ADM  R56,R20          !  ADJ FOR BINARY
3100        STM  R56,R52
3110        CLM  R54
3120        LDB  R55,=1           !   MAX LENGTH = 256
3130        LDMD R56,=BINTAB
3140        ADM  R56,=KBUFF+
3150        PUMD R52,+R12         !  PARAM IT
3160 ! DO A STRING ENTER; AWAIT TERM CONDITIO
3170        JSB  =ROMJSB
3180        DEF  STRENT
3190        VAL  IOROM#
3200        CMB  R17,=300
3210 GETJMP JCY  GET!  
3220        JSB  =ROMJSB
3230        DEF  EE_ENT
3240        VAL  IOROM#
3250        CMB  R17,=300
3260        JCY  GETJMP
3270 ! IF HANDSHAKE ENABLED SEND WAIT CHAR XOFF
3280        LDMD R20,=BINTAB
3290        LDBD R30,X20,HANDSH
3300        JZR  HANDNO           !   NO HANDSHAKE
3310 ! PAUSE INPUT WITH XOFF TO REMOTE CONSOL
3320 ! UNTIL RESUMED WITH NEXT XON
3330        LDB  R30,=19D
3340        JSB  X20,OUT   
3350 ! DO A <-LINE> TO CLEAR THE SCREE
3360 HANDNO BSZ  0
3370        LDB  R60,=160D        !  <-LINE> KEY TO START NEW LINES
3380        RTN                   !         WE'RE DONE
3390 ! 
3400 ! ---------------------------------------------
3410 ! ENTER AND OUTPUT IMAGES
3420 ! EIMAGE BYT 5,0 !    ENTER IMAGE LENGT
3430 !      DEF ENTPTR !  ADD
3440 !      BYT 5,
3450 !      DEF ENTPT
3460 ! ENTPTR ASC "#,#%K" !READ STRING WITH SINGLE <CR> TERM CHA
3470 OIMAGE BYT  3,0              !     OUTPUT IMAGE LENGTH
3480        DEF  OUTPTR
3490        BYT  3,0
3500        DEF  OUTPTR
3510 OUTPTR ASC  "#,A"            !   WRITE SINGLE CHAR NO EOL
3520 ! Note!!! these addresses require absolutizatio
3530 ! at runtime
3540 ! -----------------------------------------------
3550 OUT    BSZ  0
3560        STMD R30,X20,OUTCHR   ! SAVE IT
3570 ! OUTPUT A CHAR TO THE REMOTE CONSOLE (R30
3580 ! SIMULATE THE BASIC: OUTPUT S; A
3590 ! WHERE A$ IS THE CHAR IN R30
3600 ! THIS PARSES A
3610 !  <PUSH S><LAD.><OUT.><PUSH A$><COMMA$><PRLINE><EOUT.
3620        STMD R12,=TOS         !  FOR PARAM LENGTH
3630        LDMD R40,X20,SELCOD
3640        PUMD R40,+R12         !  PARAM FOR <LAD.>
3650        JSB  =ROMJSB
3660        DEF  LAD.  
3670        VAL  IOROM#
3680        JSB  =ROMJSB
3690        DEF  OUT.  
3700        VAL  IOROM#
3710 ! USE IMAGE "#,A", I.E. ONE CHAR WITHOUT <CR><LF
3720        LDB  R20,=177
3725 USING? DAD  100037
3730        STBD R20,=USING?      !  USE AN IMAGE
3740 ! RELOCATE THE IMAGE & STASH IT FOR SYSTE
3750 ! "RELOCATE" IMAGE POINTER
3760        LDMD R22,=BINTAB
3770        LDMD R40,X22,OIMAGE   !  OUTPUT
3780        ADM  R22,R46
3790        STM  R22,R46
3800        STM  R22,R42
3810        STMD R40,=IMSLEN
3820 ! PUSH THE STRING PARAM (LENGTH AND ADDR
3830        LDM  R30,=1,0         ! LENGTH =1
3840        PUMD R30,+R12
3850        LDMD R30,=BINTAB
3860        ADM  R30,=OUTCHR      !  COMPUTE ADDR
3870        PUMD R30,+R12
3880 ! PERFORM THE PRIN
3890        JSB  =COMMA$
3900        JSB  =PRLINE
3910        JSB  =ROMJSB
3920        DEF  EOUT. 
3930        VAL  IOROM#
3940 ! RESTORE BASE ADDR FOR BINAR
3950        LDMD R20,=BINTAB
3960        RTN  
3970 !       HED ISR ADDITIO
3980 MYISR  BSZ  0
3990 ! This binary program must take over the Input/Oupu
4000 ! ROM's Interrupt Service Routine to handle al
4010 ! i/o interrupts. It lets the I/O rom do its par
4020 ! then is called for a little extra checking. I
4030 ! the interrupting card is not the KEYBOARD IS car
4040 ! then nothing need be done and MYISR just returns
4050 ! If the interrupting card is the right one this mean
4060 ! the user is requiring a RESET to be performed
4070 ! Because the KEYBOARD IS card may not be reset i
4080 ! must be temporarily removed from the power-on tabl
4090 ! before the reset is done. Afterwards it is replaced
4100 ! Reset also cancels ROM-IDLE hook which passes char
4110 ! to the system so it must be re-established
4120 !      STBD R#,=GINTEN !!!FOR DEBU
4130 ! SAVE REG
4140        PUMD R20,+R6
4150        PUMD R22,+R6
4160 ! CK FOR INTR TO MY CAR
4170        LDMD R22,=IOBASE
4180        LDBD R23,X22,ONITAB   ! ON INTR TABLE
4190        LDMD R20,=BINTAB
4200        LDBD R21,X20,SCMASK   ! MY SELCOD MASK
4210        ANM  R23,R21          !  SEL CODE MATCH?
4220        JZR  NOINTR           !   NOPE: NO INTR TO MY CARD
4230 ! WE HAVE RECEIVED AN INTR TO THE KEYBOARD IS CARD
4240 ! REMOVE CARD FROM LOGIN TA
4245 IOBITS DAD  100667
4250        LDBD R23,=IOBITS
4260        LDM  R6,=STACK 
4270        PUBD R23,+R6          ! SAVE OLD IOBITS
4280        XRB  R23,R21
4290        STBD R23,=IOBITS
4300 ! NOW DO WHAT TYPING <RESET> DOE
4310        JSB  =RESET.
4320        POBD R30,-R6
4330        STBD R30,=IOBITS      ! RESTORE OLD IOBITS
4340 ! RE-ESTABLISH ROMIDLE & ISR HOOK
4350        LDMD R20,=BINTAB
4360        JSB  X20,NLINE        !       AND FLAG NEWLINE
4370 ! CLEAR THE OLD ENTER THAT WAS INTERRUPTED TO RESE
4380        LDMD R24,=BINTAB
4390        LDMD R24,X24,MYCCR    ! GET CCRADR
4400 ! READ IB (=CCR+1) TO ENABLE SETCE
4410        ICM  R24
4420        LDBD R22,R24
4430        DCM  R24              !         R24:=CCR AGAIN
4440        LDMD R22,=IOBASE
4450        JSB  =ROMJSB
4460        DEF  SETCED           !          CLEAR THE BUSY
4470        VAL  IOROM#
4480 ! RETURN TO EXEC LOO
4490        LDB  R30,=1
4500        STBD R30,=KEYCOD
4510        GTO  DOCUR.
4520 ! ----------------------------------------------
4530 NOINTR BSZ  0                !       NO INTR RECEIVED
4540 ! RESTORE REGS AND RETUR
4550        POMD R22,-R6
4560        POMD R20,-R6
4570        DCM  R6               !       REMOVE JSB TO MYISR
4580        DCM  R6
4590        STBD R#,=GINTEN       !  FROM HERE DUPLICATE IOROM ISR
4600        PAD  
4610 BADCLR RTN  
4620 ! 
4630 ! ----------------------------------------
4640 ! BINARY R/W VARIABLE
4650 NEWLIN BSZ  1                !       BEG OF LINE IF <> 0
4660 INPTR  BSZ  2                !       INPUT BUFFER PTR
4670 KBUFF  BYT  200,0,0,1,0,1,0,0 ! 8 BYTES BUFFER HEADER
4680 ! 1ST 2 BYTES NEEDED TO CANCEL TRACE FUNCTIO
4690 ! 2ND,3RD & 4TH 2-BYTERS ARE TOTAL, MAX & ACTUAL LENGTH
4700 ! (MAX MAY DIFFER FROM TOTAL IF IOBUFFER,ETC.
4710 KBUFF+ BSZ  256D             !     'KEY' BUFFER
4720 GIVTIM BSZ  1                !       RMIDLE NEEDS BREATHER FLAG
4730 SELCOD BSZ  8D               !      SELECT CODE PARAMETER
4740 HANDSH BSZ  8D               !      HANDSHAKE
4750 SCMASK BSZ  1
4760 MYCCR  BSZ  2
4770 OUTCHR BSZ  1                !       OUTPUT CHARACTER (HANDSHAKES)
4780 ! ------------------------------------------------
4790 ! I.O.ROM ADDRESSE
4800 CCRADR DAD  206
4810 SETCED DAD  63347
4820 TAD.   DAD  62511
4830 EI_ENT DAD  63161
4840 STRENT DAD  63375
4850 EE_ENT DAD  63233
4860 ONITAB DAD  200
4870 LAD.   DAD  62517
4880 OUT.   DAD  66523
4890 EOUT.  DAD  66643
4900 ! ------------------------------------------------
4910 ! SYSTEM ADDRESSES
4920 COMMA$ DAD  70634
4930 IRQIEN DAD  102502           !    THIS IS IRQ20 + 11
4940 ! THIS PNTS AT THE "STBD R#,=GINTEN" IN IOROMS IS
4950 IMSLEN DAD  101142           !    USING IMAGE
4960 RESET. DAD  4327
4970 DOCUR. DAD  67
4980        LNK  MY&IP7.asm
4990 !        un
5000 !  IRQIEN DAD 10250
