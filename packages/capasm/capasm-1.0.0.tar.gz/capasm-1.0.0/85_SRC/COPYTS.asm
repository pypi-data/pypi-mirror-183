0010        GLO  GLOBAL:T
0020 ! *********************************************
0030 !                                              
0040 !    MODIFIED BINARY TO PERFORM                
0050 !      D-->T VOLUME COPY !                     
0060 !             !                                
0070 !    Randy Salo    DEC 1980 !                  
0080 !             !                                
0090 ! *********************************************
0100        NAM  COPYT 
0110 ! *********************************************
0120        DEF  RUNTIM
0130        DEF  TOKENS
0140        DEF  PARSE 
0150        DEF  ERMSG 
0160        DEF  INIT  
0170 ! *********************************************
0180 RUNTIM BSZ  2
0190        DEF  DT.              !           1. VCOPYDD
0200        DEF  REV.  
0210 ! *********************************************
0220 PARSE  BSZ  2
0230 ! *********************************************
0240        DEF  DT               !            1.
0250 !  Syntax is COPYTAPE disk-msu
0260 ! NOTE
0270 ! COPYTAPE aborts when it finds either type 
0280 ! (blank-name) or Type 1 (store duplication
0290 ! security. It stops WHEN detected, i.e. when i
0300 ! directory and while reading first sector o
0310 ! PROG/BPGM files, resp
0320 ! *********************************************
0330 !  RELOCATE THESE.... NONE !                   
0340 ! *********************************************
0350        BYT  377,377
0360 ! *********************************************
0370 TOKENS ASP  "COPYTAPE"
0380        ASP  ""
0390        BYT  377              !            END OF LIST
0400        BYT  0,56
0410 REV.   BIN  
0420        LDM  R44,=10,0
0430        DEF  DATE  
0440        ADMD R46,=BINTAB
0450        PUMD R44,+R12
0460        RTN  
0470 DATE   ASC  "12/30/80"
0480 ! *********************************************
0490 ERMSG  BYT  200              !            DUMMY
0500 ! 37
0510        ASC  33D,I can only copy 42 files to tape!
0520        BYT  240
0530 ! 37
0540        ASC  34D,Your source device must be a disk!
0550        BYT  240
0560 ! 37
0570        ASC  33D,The tape's not big enough. Sorry! 
0580        BYT  240
0590 ! 37
0600        ASC  33D,Copying SECURED files is a NO-NO! 
0610        BYT  240
0620        BYT  377              !            END OF LIST
0630 ! **********************************************
0640 INIT   BSZ  0
0650 ! ISSUE HELP MSG AFTER LOADBIN
0660        LDBD R36,=ROMFL 
0670        CMB  R36,=3           !   LOADBIN?
0680        JNZ  HLPRTN
0690        LDM  R36,=39D,0       !    LENGTH
0700        LDMD R26,=BINTAB
0710        ADM  R26,=HELP        !     ADDR
0720        JSB  =DISP.           !        INIT DRIVER
0730        JSB  =DRV12.          !       OUTPUT HELP
0740 HLPRTN RTN  
0750 ! ----------------------------------------
0760 HELP   ASC  "Syntax is 'COPYTAPE <disk source msus>'"
0770 ! *********************************************
0780 DT     BIN  
0790        LDMD R36,=BINTAB      !   GET BASE ADDRESS
0800        LDM  R70,R40          !        SAVE OUR TOKEN
0810        JSB  X36,GETSTR       !    GET A STRING
0820        LDB  R52,=371         !       BINARY TOKEN
0830        PUBD R52,+R12
0840        PUBD R71,+R12
0850        PUBD R73,+R12
0860        RTN  
0870 ! ----------------------
0880 ! ----------------------
0890 COMMA  EQU  54
0900 GETCOM CMB  R14,=COMMA 
0910        JNZ  ERROO 
0920 NOERR  RTN  
0930 ! ----------------------
0940 ERROO  POMD R46,-R6          !  POP CALLING R.A.
0950        JSB  =ERROR 
0960        BYT  92D              !       SYSTEM SYNTAX
0970        JSB  =TAPEXT
0980        RTN  
0990 ! ----------------------
1000 GETSTR JSB  =STREX+
1010        JEN  NOERR 
1020        JMP  ERROO 
1030 ! ----------------------
1040 ! -----------------------------------------------
1050 BADMSU JSB  =ERROR 
1060        BYT  375              !           BADMSUS
1070 BADIO  JSB  =TAPEXT
1080        RTN  
1090 ! --------------------------------------------------
1100 MSINIT BSZ  0
1110        JSB  =ROMJSB
1120        DEF  MSIN+ 
1130        VAL  MSROM#
1140        RTN  
1150 ! ----------------------------------------------------
1160 MSROM# EQU  320
1170        BYT  0,241
1180 DT.    LDMD R20,=BINTAB
1190        JSB  X20,MSINIT
1200        LDB  R40,=2           !   MSUS ONLY
1210        JSB  =ROMJSB
1220        DEF  DCDFIL
1230        VAL  MSROM#
1240        CMB  R17,=300         ! ERRORS?
1250        JCY  IOBAD 
1260        TSM  R44              !      TAPE OR DISK?
1270        JZR  BADMSU           !   TAPE NOT ALLOWED
1280 ! VALID D-->T COPY REQUESTE
1290 ! FIRST TRANSLATE MULTI-SECTOR DISK DIR TO 2-REC TAPE DI
1300        STMD R44,X14,SRCMSU   ! FOR NXTFIL MSUS
1310        JSB  =ERAST.          !        FORMAT THE TAPE+EMPTY DIR
1320        CMB  R17,=300         !      TAPE ERRORS?
1330        JCY  IOBAD 
1340 ! OFF THE CR
1350        JSB  =TAPIN-
1360        STBD R#,=GINTEN
1370 ! DISK DIR TO TAPE DI
1380        LDM  R56,=DIRECT      !   TAPE 1ST DIR ENTRY
1390        CLB  R55              !           CURRENT FILE#
1400        LDMD R20,=BINTAB
1410        STMD R55,X20,DIRINF   ! TAPE DIR INFO
1420        JSB  X20,TDINIT       ! TAPE DIR INIT (ALL FILES NEXTAVAIL)
1430        JSB  X20,MSINIT       !   MS ROM
1440        JSB  =ROMJSB
1450        DEF  GETDIR           !        GET 1ST DISK DIR ENTRY
1460        VAL  MSROM#
1470        CMB  R17,=300
1480        JCY  IOBAD 
1490        JSB  =ROMJSB
1500        DEF  SKHOL+           !        SKIP EMPTY ENTRIES
1510        VAL  MSROM#
1520        CMB  R17,=300
1530        JCY  IOBAD 
1540        JEN  IOBAD            !  MEANS WE'RE DONE DIR END
1550 ONEFIL STMD R45,R14          !      SAVE DISK DIR PTRS
1560 ! FOR EACH ENTRY
1570 ! ---TAPE:::::DISK--
1580 !  D.TYPE := DISK TYPE (R30
1590 !  D.#R/F := FILE LENGTH FROM LDREC
1600 !  D.#B/R := D.B/R
1610 !  D.FIL# := 
1620 !  NAME   := NAME (6 CHARS
1630        LDMD R20,=BINTAB
1640        LDMD R55,X20,DIRINF   ! TAPE PTRS
1650        ICB  R55              !           FILE# : +1
1660        CMB  R55,=43D         !      END 2ND TAPE SEG?
1670        JNZ  NOT2ND
1680        JSB  =ERROR 
1690        BYT  376              !           TOO MANY DISK FILES FOR TAPE
1700 IOBAD  JSB  =TAPEXT
1710        RTN  
1720 BADSEC JSB  =ERROR 
1730        BYT  373              !      COPY NONO
1740        JMP  IOBAD 
1750 ONEFI! JMP  ONEFIL
1760 ! -------------------------------------------------------
1770 NOT2ND STBD R30,X56,D.TYPE   ! NEW TAPE TYPE
1780 ! CHECK FOR TYPE 3 (BLANK-NAME) SECURITY
1790        JOD  BADSEC
1800        CLB  R30
1810        STBD R30,X56,D.FIL#   ! NEW FILE #
1820        LDMD R42,R36          !      DISK NAME
1830        STMD R42,R56          !      TAPE NAME
1840        LDB  R42,=MSROM#
1850        STBD R42,=RSELEC
1860        DRP  R30
1870        JSB  =LDRECS          !       DISK LENGTH
1880        STMD R30,X56,D.#R/F   ! TAPE FILE LENGTH
1890        CLB  R#
1900        STBD R#,=RSELEC
1910        LDMD R30,X36,D.B/RC   ! DISK BYTES/LOG REC
1920        STMD R30,X56,D.#B/R   ! NEW TAPE BYTES/LOG REC
1930        ADM  R56,=12D,0       !    BUMP TAPE DIR PTR
1940        STMD R55,X20,DIRINF   ! NXT LOOP PASS
1950        CMB  R55,=21D         !      END 1ST TAPE DIR SEG?
1960        JNZ  NOTEND           !        NOT END SEG
1970 ! END 1ST TAPE DIR SEG: WRITE IT AND READ OPS SEG
1980        STMD R6,=SAVER6
1990        STBD R#,=GINTDS
2000        JSB  =FIND+W
2010        JSB  =REDOPS
2020        STBD R#,=GINTEN
2030        LDMD R20,=BINTAB
2040        JSB  X20,MSINIT       ! SAVER6,ETC
2050        LDMD R55,X20,DIRINF   ! RESET TAPE DIR PTR
2060        LDM  R56,=DIRECT
2070        STMD R55,X20,DIRINF
2080        JSB  X20,TDINIT       ! DIR INIT:ALL FILES NEXTAVAIL
2090 NOTEND JSB  =ROMJSB
2100        DEF  NXTFIL
2110        VAL  MSROM#
2120        CMB  R17,=300
2130 ERR2   JCY  IOBAD 
2140        JEZ  ONEFI!
2150 VCDONE BSZ  0                !             NO MORE DISK FILES
2160        STMD R6,=SAVER6
2170        STBD R#,=GINTDS
2180        JSB  =FIND+W          !        WRITE TAPE DIR
2190        STBD R#,=GINTEN
2200        CMB  R17,=300
2210        JCY  ERR2  
2220        LDMD R20,=BINTAB
2230        JSB  X20,MSINIT
2240 ! ----------------------------------------------------
2250 ! TAPE DIR COPIED/TRANSLATED! NOW COPY THE FILES
2260 ! Note: to make sure of fit put only 350d recs/track
2270 ! I.e. when cummulative rec count reaches 350 terminat
2280 ! that track, rewind, fix tape dir, then continu
2290 ! til 42 files reached or end of tape/disk
2300        CLM  R34
2310        STBD R34,=VALIDD      ! DIR NOW VALID
2320        ICM  R34
2330        STMD R34,=CURFIL
2340 ! MOVE TO FIRST TAPE FIL
2350        JSB  =ROMJSB
2360        DEF  GETDIR
2370        VAL  MSROM#
2380        CMB  R17,=300
2390        JCY  ERR2  
2400        CLM  R34
2410        STMD R34,X14,CUMREC   ! CUMRECS/TRAK:=0
2420        JSB  =ROMJSB
2430        DEF  SKHOL+
2440        VAL  MSROM#
2450        CMB  R17,=300
2460        JCY  ERR3  
2470        JEZ  NOTDUN
2480 ERR3   JSB  =TAPEXT
2490        RTN  
2500 NOTDUN BSZ  0
2510        CLB  R30
2520        STBD R30,X14,CPYSIZ   ! TRACK#
2530 NXFILE BSZ  0
2540        LDB  R30,=CAPRTY
2550        STBD R30,=FILTYP      !  FILTYP:=CAPRTY FOR IRG
2560        CLM  R30
2570        STMD R30,=CURREC      !  CURREC:=0
2580        STMD R45,R14          !      DISK DIR INFO
2590        LDB  R#,=MSROM#
2600        STBD R#,=RSELEC
2610        DRP  R30
2620        JSB  =LDRECS
2630        LDMD R20,=BINTAB
2640        STMD R30,X20,TRECS    ! TOTAL RECS TO COPY
2650        JSB  =LDFBEG
2660        CLB  R20
2670        STBD R20,=RSELEC
2680        PUMD R30,+R6          ! SAVE SEEK ADR FROM GETTYP
2690        JMP  AROUND
2700 NFILE2 JMP  NXFILE           ! TOO MANY JMPs!
2710 AROUND BSZ  0
2720 ! ---
2730 ! NOTE: for PROG,BPGM files bytes in last rec may no
2740 ! be 256, as for DATA files. This is determined here an
2750 ! stashed in binary RAM B/LREC for use by WRTREC
2760 ! which expects r22=byte count, r56=address of data
2770 ! See MSROM COPY
2780        LDM  R24,=0,1         ! 256 BYTES FOR DATA FILES
2790        CLB  R26              !      PROG/BPGM FILE TYPE
2800        JSB  =ROMJSB
2810        DEF  GETTYP
2820        VAL  MSROM#
2830        LDB  R31,R30
2840        ANM  R31,=P/BTYP      !      PROG OR BINARY
2850 P/BTYP EQU  50               !   CAPRTY or BPGMTY
2860        JZR  YESDAT           !           NEITHER
2870 ! WE HAVE A PROGRM OR BINARY: CK SECURIT
2880        ICB  R26              !      NOT DATA TYPE
2890 ! COMPUTE BYTES LAST PROG REC
2900        LDMD R76,X36,D.BYTS
2910        CLM  R45
2920        LDB  R45,R76
2930        JNZ  BYT1  
2940        ICB  R46
2950 BYT1   LDB  R47,R77
2960        TSB  R76
2970        JZR  BYT2  
2980        ICB  R47
2990 BYT2   STM  R45,R24
3000 YESDAT LDMD R20,=BINTAB
3010        STMD R24,X20,B/LREC
3020        STBD R26,X20,CKSEC    !  NEED CHECK PROG SECUR?
3030        POMD R30,-R6          ! RESTORE SEEK ADR
3040        JSB  =ROMJSB
3050        DEF  HLSEEK
3060        VAL  MSROM#
3070        CMB  R17,=300
3080        JCY  IOERR 
3090 ! --
3100 ! NOW WRITE A TAPE FILE CONTAINING recs SECTORS FROM DIS
3110        STMD R6,=SAVER6
3120        STBD R#,=GINTDS
3130        JSB  =FIND+ 
3140        STBD R#,=GINTEN
3150        JEZ  MARKOK
3160 JSB131 JSB  =ERROR 
3170        BYT  73D              !   FILE NOT FOUND
3180 IOERR  JSB  =TAPEXT
3190        RTN  
3200 ! ---------------------------------------------------------
3210 ! ---------------------------------------------------------
3220 MARKOK BSZ  0
3230        LDMD R20,=BINTAB
3240        JSB  X20,MSINIT
3250        JMP  ARND!!
3260 NFILE  JMP  NFILE2
3270 ARND!! BSZ  0
3280        JSB  =ROMJSB
3290        DEF  GETBU+
3300        VAL  MSROM#
3310        CMB  R17,=300
3320        JCY  IOERR 
3330        LDMD R20,=BINTAB
3340        JSB  X20,BYTES 
3350        STMD R6,=SAVER6
3360        LDB  R30,=REWRTP
3370        LDM  R36,=IFGLEN
3380 M.LOOP STMD R36,=GAPLEN
3390 REDO   LDMD R14,=MSBASE
3400        LDMD R32,X14,CUMREC
3410        ICM  R32
3420        STMD R32,X14,CUMREC   ! CUMREC: +1
3430        STBD R#,=GINTDS
3440        JSB  =WRTREC
3450        JEN  JSB131
3460        JSB  =WSLACK
3470        LDMD R36,=GAPLEN
3480        JSB  =IRG   
3490        STBD R#,=GINTEN
3500        LDMD R26,=CURREC
3510        LDMD R20,=BINTAB
3520        JMP  ARND??
3530 NPHILE JMP  NFILE 
3540 ARND?? BSZ  0
3550        LDMD R22,X20,TRECS 
3560        CMM  R22,R26          ! CURREC=FILE LENGTH?
3570        JNZ  MORFIL           !        MORE FILE TO WRITE
3580        STBD R#,=GINTDS
3590        JSB  =DO.F1           !        EOF HEADER
3600        JSB  =REWGA*          !       REWND TO BEG FILE
3610        STBD R#,=GINTEN
3620        LDMD R20,=BINTAB
3630        JSB  X20,MSINIT
3640        JSB  =ROMJSB
3650        DEF  NXTFIL           !   NEXT FILE IN DIR
3660        VAL  MSROM#
3670        CMB  R17,=300
3680        JCY  ERR1  
3690        JEN  ERR1             !     NO MORE DISK FILES
3700        JMP  NPHILE
3710 M.     JMP  M.LOOP
3720 REDO.  JMP  REDO  
3730 MORFIL BSZ  0
3740        JSB  X20,MSINIT
3750        JSB  =ROMJSB
3760        DEF  GETBU+
3770        VAL  MSROM#
3780        CMB  R17,=300
3790        JCY  ERR1  
3800        LDMD R20,=BINTAB
3810        JSB  X20,BYTES 
3820        STMD R6,=SAVER6
3830        LDB  R30,=MARK  
3840        LDM  R36,=IRGLEN
3850 ! CUM REC COUNT ON TAPE
3860        LDMD R32,X14,CUMREC
3870        CMM  R32,=TAPSIZ
3880 TAPSIZ DAD  290D             !    RECS PER TRAK
3890        JNG  M.    
3900 ! WE'RE AT END OF TRACK
3910        LDBD R30,X14,CPYSIZ   ! TRAK#
3920        JNZ  EOT#2            !         2ND EOTRAK!
3930        ICB  R30
3940        STBD R30,X14,CPYSIZ
3950        STMD R36,=GAPLEN
3960        STBD R#,=GINTDS
3970        JSB  =SETFL1
3980        STBD R#,=GINTEN
3990        LDMD R14,=MSBASE
4000        CLM  R30
4010        STMD R30,X14,CUMREC   ! ZERO CUM REC THIS TRACK
4020        JMP  REDO. 
4030 ! NOTE!!!!!
4040 ! no hole detection is performed: max tape length is assume
4050 ! to be 350 recs
4060 ! ------------------------------------------------------
4070 EOT#2  JSB  =ERROR 
4080        BYT  374              !           EO 2ND TRAK
4090 ERR1   JSB  =TAPEXT
4100        RTN  
4110 ! ------------------------------------------------------
4120 BYTES  BSZ  0
4130        LDM  R56,=RECBUF      ! DATA ADDRESS
4140        LDMD R30,X20,TRECS    ! RECS TO COPY
4150        LDMD R32,=CURREC      ! CURRENT REC
4160        ICM  R32
4170        CMM  R32,R30          !  CURREC IS LAST?
4180        JZR  LSTREC           !   JIF LAST REC
4190        LDM  R22,=0,1         ! 256 BYTES / NORMAL REC
4200        RTN  
4210 LSTREC LDMD R22,X20,B/LREC
4220        RTN  
4230 ! -------------------------------------------------------
4240 TDINIT BSZ  0
4250 ! INITIALIZE ALL FILES IN TAPE DIR TO NEXT-AVAIL SO THER
4260 !  WILL BE A LAST FILE IN CASE DIR STILL HAS SPACE IN IT
4270        LDB  R60,=21D         ! 21 FILES PER DIR REC
4280        LDB  R61,=200         ! NEXT-AVAIL BIT
4290 DLOOP  STBD R61,X56,D.TYPE   ! SET NEXT AVAIL
4300        ADM  R56,=12D,0       ! NEXT FILE ENTRY
4310        DCB  R60              !      FILE CNT
4320        JNZ  DLOOP            !    ANOTHER ENTRY
4330        RTN  
4340 ! --------------------------------------------------------
4350 ! BINARY VARIABLES
4360 B/LREC BSZ  2                ! BYTES LAST REC PROG/BPGM FILES
4370 TRECS  BSZ  2                !        TOTAL RECS TO COPY
4380 DIRINF BSZ  3                !       TAPE FILE #, DIRECTORY ADDR
4390 CKSEC  BSZ  1                !       SECURITY IF PROG/BPGM FILE
4400 ! -------------------------------------------------------
4410 ! MSROM ENTRY POINTS
4420 DCDFIL DAD  61361
4430 HLSEEK DAD  77310
4440 HLFMT  DAD  76021
4450 GETDIR DAD  63346
4460 SKHOL+ DAD  73004
4470 DSTMSU EQU  165
4480 SRCMSU EQU  161
4490 TOID   DAD  76620
4500 ACTMSU EQU  135
4510 PUTBU+ DAD  77267
4520 GETBU+ DAD  77257
4530 GETTYP DAD  61716
4540 D.BYTS EQU  34
4550 LDRECS DAD  63574
4560 LDFBEG DAD  63540
4570 CUMREC EQU  125
4580 NXTFIL DAD  72751
4590 CPYSIZ EQU  145
4600 D.B/RC EQU  36
4610 MSIN+  DAD  70261
4620 ! 
4630 ! SYSTEM TAPE ENTRY POINTS
4640 TAPIN- DAD  24455
4650 DO.F1  DAD  22310
4660 REWGA* DAD  20125
4670 SETFL1 DAD  22405
4680 EOTRAK DAD  22367
4690 FIND+  DAD  20075
4700 WRTREC DAD  23075
4710 WSLACK DAD  23331
4720 IRG    DAD  23470
4730 REWIND DAD  20070
4740 TAPEXT DAD  22000
4750 ERAST. DAD  25120
4760 DIRECT DAD  102600
4770 D.TYPE EQU  7
4780 D.FIL# EQU  6
4790 D.#R/F EQU  10
4800 D.#B/R EQU  12
4810 SAVER6 DAD  101174
4820 FIND+W DAD  22736
4830 REDOPS DAD  24511
4840 VALIDD DAD  100663
4850 CURFIL DAD  101274
4860 CURREC DAD  101276
4870 CAPRTY EQU  40
4880 FILTYP DAD  101034
4890 IFGLEN EQU  120
4900 GAPLEN DAD  100160
4910 MARK   EQU  116
4920 IRGLEN EQU  40
4930 REWRTP EQU  56
4940 RECBUF DAD  102000
4950        FIN  
