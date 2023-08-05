1000 ! ________________________
1010 ! 
1020 !   BINARY CUSTODIAN BINAR
1030 ! 
1040 ! ------------------------
1050 !  This binary provide
1060 !  the support necessar
1070 !  to use multiple binaries
1080 !  Several restriction
1090 !  are made on the binarie
1100 !  allowed by this cust
1110 ! 
1120 !  1. The binaries mus
1130 !     NOT use hidden token
1140 !     (after 377 of asci
1150 !     table)
1160 ! 
1170 !  2. The binaries mus
1180 !     RTN allways afte
1190 !     any operation. (e.
1200 !     must use ERROR an
1210 !     RTN rather tha
1220 !     ERROR+ for errors
1230 ! 
1240 ! -----------------------
1250 !   ENTRY KEYWORDS PROVIDED
1260 ! 
1270 !   LOADBIN F
1280 !   BINCA
1290 !   KEYWORD
1300 ! 
1310 ! -------------------------
1320 FIRST  NAM  B-CUST
1330 ! -------------------------
1340        DEF  RUNTIM
1350        DEF  ASCIIS
1360        DEF  PARSE 
1370 myerr  DEF  ERMSG 
1380        DEF  INIT  
1390 ! -------------------------
1400 PARSE  BYT  0,0
1410        DEF  LOADP 
1420        DEF  CATP  
1430        DEF  KEYP  
1440 ! ---> some dummy parser
1450        DEF  P-DIST
1460        DEF  P-DIST
1470        DEF  P-DIST
1480        DEF  P-DIST
1490        DEF  P-DIST
1500        DEF  P-DIST
1510        DEF  P-DIST
1520        DEF  P-DIST
1530        DEF  P-DIST
1540        DEF  P-DIST
1550        DEF  P-DIST
1560        DEF  P-DIST
1570        DEF  P-DIST
1580        DEF  P-DIST
1590        DEF  P-DIST
1600        DEF  P-DIST
1610        DEF  P-DIST
1620        DEF  P-DIST
1630        DEF  P-DIST
1640        DEF  P-DIST
1650 ! -----------------------
1660 RUNTIM BYT  0,0
1670        DEF  LOAD. 
1680        DEF  CAT.  
1690        DEF  KEY.  
1700 ! ---> some run ptr
1710        DEF  Rdum1 
1720        DEF  Rdum2 
1730        DEF  Rdum3 
1740        DEF  Rdum4 
1750        DEF  Rdum5 
1760        DEF  Rdum6 
1770        DEF  Rdum7 
1780        DEF  Rdum8 
1790        DEF  Rdum9 
1800        DEF  Rdum10
1810        DEF  Rdum11
1820        DEF  Rdum12
1830        DEF  Rdum13
1840        DEF  Rdum14
1850        DEF  Rdum15
1860        DEF  Rdum16
1870        DEF  Rdum17
1880        DEF  Rdum18
1890        DEF  Rdum19
1900        DEF  Rdum20
1910 ! ------------------------
1920        BYT  377,377
1930 ! ------------------------
1940 ASCIIS BSZ  0
1950        ASP  "LOADBIN"
1960        ASP  "BINCAT"
1970        ASP  "KEYWORDS"
1980 ASCEND BYT  377
1990        BSZ  200
2000 EOASC  BSZ  1
2010        BYT  377
2020 ! _______________________
2030 !  dummy run routine are
2040        BSZ  2                !  CLASS AREA
2050 Rdum1  BSZ  0
2060        LDB  R43,=4
2070        LDMD R20,=BINTAB
2080        JSB  X20,R-DIST
2090 !       --
2100        BSZ  2
2110 Rdum2  BSZ  0
2120        LDB  R43,=5
2130        LDMD R20,=BINTAB
2140        JSB  X20,R-DIST
2150 !       --
2160        BSZ  2
2170 Rdum3  BSZ  0
2180        LDB  R43,=6
2190        LDMD R20,=BINTAB
2200        JSB  X20,R-DIST
2210 !       --
2220        BSZ  2
2230 Rdum4  BSZ  0
2240        LDB  R43,=7
2250        LDMD R20,=BINTAB
2260        JSB  X20,R-DIST
2270 !       --
2280        BSZ  2
2290 Rdum5  BSZ  0
2300        LDB  R43,=10
2310        LDMD R20,=BINTAB
2320        JSB  X20,R-DIST
2330 !       --
2340        BSZ  2
2350 Rdum6  BSZ  0
2360        LDB  R43,=11
2370        LDMD R20,=BINTAB
2380        JSB  X20,R-DIST
2390 !       --
2400        BSZ  2
2410 Rdum7  BSZ  0
2420        LDB  R43,=12
2430        LDMD R20,=BINTAB
2440        JSB  X20,R-DIST
2450 !       --
2460        BSZ  2
2470 Rdum8  BSZ  0
2480        LDB  R43,=13
2490        LDMD R20,=BINTAB
2500        JSB  X20,R-DIST
2510 !       --
2520        BSZ  2
2530 Rdum9  BSZ  0
2540        LDB  R43,=14
2550        LDMD R20,=BINTAB
2560        JSB  X20,R-DIST
2570 !       --
2580        BSZ  2
2590 Rdum10 BSZ  0
2600        LDB  R43,=15
2610        LDMD R20,=BINTAB
2620        JSB  X20,R-DIST
2630 !       --
2640        BSZ  2
2650 Rdum11 BSZ  0
2660        LDB  R43,=16
2670        LDMD R20,=BINTAB
2680        JSB  X20,R-DIST
2690 !       --
2700        BSZ  2
2710 Rdum12 BSZ  0
2720        LDB  R43,=17
2730        LDMD R20,=BINTAB
2740        JSB  X20,R-DIST
2750 !       --
2760        BSZ  2
2770 Rdum13 BSZ  0
2780        LDB  R43,=20
2790        LDMD R20,=BINTAB
2800        JSB  X20,R-DIST
2810 !       --
2820        BSZ  2
2830 Rdum14 BSZ  0
2840        LDB  R43,=21
2850        LDMD R20,=BINTAB
2860        JSB  X20,R-DIST
2870 !       --
2880        BSZ  2
2890 Rdum15 BSZ  0
2900        LDB  R43,=22
2910        LDMD R20,=BINTAB
2920        JSB  X20,R-DIST
2930 !       --
2940        BSZ  2
2950 Rdum16 BSZ  0
2960        LDB  R43,=23
2970        LDMD R20,=BINTAB
2980        JSB  X20,R-DIST
2990 !       --
3000        BSZ  2
3010 Rdum17 BSZ  0
3020        LDB  R43,=24
3030        LDMD R20,=BINTAB
3040        JSB  X20,R-DIST
3050 !       --
3060        BSZ  2
3070 Rdum18 BSZ  0
3080        LDB  R43,=25
3090        LDMD R20,=BINTAB
3100        JSB  X20,R-DIST
3110 !       --
3120        BSZ  2
3130 Rdum19 BSZ  0
3140        LDB  R43,=26
3150        LDMD R20,=BINTAB
3160        JSB  X20,R-DIST
3170 !       --
3180        BSZ  2
3190 Rdum20 BSZ  0
3200        LDB  R43,=27
3210        LDMD R20,=BINTAB
3220        JSB  X20,R-DIST
3230 !       --
3240 ! --------------
3250 ! ------------------------
3260 ! ========================
3270 ERMSG  BYT  200
3280        BYT  200
3290        BYT  200
3300        BYT  200
3310        BYT  200
3320        BYT  200
3330        BYT  200
3340        BYT  200
3350        BYT  200
3360        BYT  200
3370        BYT  200              !  DUMMY
3380        ASP  "TOO MANY BINARIES"
3390        ASP  "ASCII OVERFLOW"
3400        ASP  "TOO MANY KEYWORDS"
3410        BYT  377
3420 ! ------------------------
3430 INIT   BSZ  0
3440        BIN  
3450 !  initialize ascii pt
3460        LDBD R34,=ROMFL 
3470        CMB  R34,=3
3480        JNZ  BYE   
3490 !  go on if LOADBIN entr
3500        PUMD R46,+R6
3510        PUMD R56,+R6
3520        LDMD R56,=BINTAB
3530        LDM  R46,=nxt-bn
3540        STMD R46,X56,nxt-as   !  NEXT NAME FOR BIN NAME TABLE
3550        LDM  R46,=ASCEND
3560        STMD R46,X56,asc-pt   !  SAVE POINTER TO NEXT ASCII ENTRY AREA
3570        LDM  R46,R56
3580        STMD R46,X56,mybase
3590        LDM  R46,=mybase
3600        ICM  R46
3610        ICM  R46
3620        STMD R46,X56,bas-pt   !  SAVE POINTER TO NEXT BASE ADDRESS AREA
3630        LDM  R46,=tok-ls      !  TOKEN# LIST ADDRESS
3640        ICM  R46
3650        ICM  R46
3660        ADM  R46,R56
3670        STMD R46,X56,tok-pt
3680        LDM  R46,=32,0
3690        ADM  R46,R56
3700        LDMD R46,R46          !  BASE OF MY RUNTIME ADDRESS TABLE
3710        LDM  R66,=10,0
3720        ADM  R46,R66          !  SKIP 4 ENTRIES (0 plus my 3)
3730        STMD R46,X56,run-pt
3740 ! --------INIT num-b
3750        LDB  R77,=1
3760        STBD R77,X56,num-bn
3770 ! ---------SAVE MY errorAD
3780        LDMD R46,X56,myerr 
3790        STMD R46,X56,myeadd
3800        POMD R56,-R6
3810        POMD R46,-R6
3820        RTN  
3830 ! ---------
3840 BYE    BSZ  0
3850 !  IF ROMFL=13Oct THEN DIS
3860        CMB  R34,=13
3870        JZR  distit
3880 !  IF ROMFL<8 THEN DISTRI
3890        CMB  R34,=10
3900        JZR  TOKALC
3910        JPS  TOKALC
3920 distit PUMD R40,+R6
3930        LDMD R46,=BINTAB
3940 !  FOR R43=1 TO num-bn-
3950        LDB  R43,=1
3960        LDBD R42,X46,num-bn
3970 IN-LOP LDB  R73,R43
3980        CMB  R43,R42
3990        JZR  DON-IN
4000        STM  R46,R70
4010        JSB  X46,GETBAS
4020 !       get init add
4030        LDM  R66,=42,0
4040        ADM  R76,R66
4050        LDMD R76,R76          !  GET INIT ADDR
4060        PUMD R40,+R6
4070        JSB  X76,ZRO          !  DO INIT
4080        BIN  
4090        POMD R40,-R6
4100        ICB  R43
4110        STM  R46,R70          !  MY BASE ADDR
4120        JSB  X70,ck-err
4130        JEZ  IN-LOP
4140 ! -----------------
4150 DON-IN BSZ  0
4160        STMD R46,=BINTAB
4170        POMD R40,-R6
4180        RTN  
4190 ! -------------------
4200 !  area for ROMFL>
4210 !  I.E. ALLOCATE TOKE
4220 ! 
4230 TOKALC BSZ  0
4240        PUMD R40,+R6
4250        POMD R76,+R24
4260        PUMD R76,-R74
4270        LDMD R46,=BINTAB
4280        LDB  R73,R77
4290        STM  R46,R70
4300        JSB  X46,GETOWN
4310        JSB  X46,GETBAS       !  GET BASE ADDR OF OWNER
4320        LDM  R66,=42,0
4330        ADM  R76,R66
4340        LDMD R76,R76          !  GET INIT ADDRESS
4350        PUMD R46,+R6
4360        JSB  X76,ZRO          !  DO ALLOC
4370        POMD R46,-R6
4380        STM  R46,R70
4390        JSB  X70,ck-err
4400        STMD R46,=BINTAB
4410        POMD R40,-R6
4420        RTN  
4430 ! ---------------
4440 ! _______________________-
4450 STLAMT DAD  2000
4460 ! ========================
4470 ! ------------------------
4480 !   PARSE ROUTINE
4490 ! ------------------------
4500 LOADP  BSZ  0
4510 STOREP BSZ  0
4520        PUBD R43,+R6
4530        JSB  =STREX+
4540        POBD R43,-R6
4550        LDB  R37,=371
4560        PUBD R37,+R12
4570        PUBD R37,+R12
4580        PUBD R43,+R12
4590        RTN  
4600 ! ______________________
4610 CATP   BSZ  0
4620 KEYP   BSZ  0
4630        LDB  R37,=371
4640        PUBD R37,+R12
4650        PUBD R37,+R12
4660        PUBD R43,+R12
4670        JSB  =SCAN  
4680        RTN  
4690 ! _______________________
4700 ! =======================
4710 ! -----------------------
4720 !  RUNTIME ROUTINE
4730 ! -----------------------
4740 !       BYT 0,24
4750 ! TORE. BSZ 
4760 !       RT
4770 ! ----------------------
4780 !  BINCAT RUNTIM
4790        BYT  241
4800 CAT.   BSZ  0
4810        BIN  
4820        LDMD R76,=BINTAB
4830        ADM  R76,=bin-ls
4840        LDMD R56,=BINTAB
4850        JSB  X56,GET-CH
4860        RTN  
4870 ! ----------------------
4880 ! ----------------------
4890 !  KEYWORDS RUNTIM
4900        BYT  241
4910 KEY.   BSZ  0
4920        BIN  
4930        LDMD R76,=BINTAB
4940        ADM  R76,=ASCIIS
4950 ! --------------------
4960 !  DUMP LIST ENTR
4970 GET-CH BSZ  0
4980        POBD R67,+R76
4990        CMB  R67,=377
5000        JNZ  GO-ON 
5010        RTN  
5020 ! --------
5030 GO-ON  BSZ  0
5040        TSB  R67
5050        JNG  END-W 
5060        LDB  R32,R67
5070        JSB  =OUTCHR
5080        JMP  GET-CH
5090 ! --------
5100 END-W  BSZ  0
5110        LDB  R66,=177
5120        ANM  R67,R66
5130        LDB  R32,R67
5140        JSB  =OUTCHR
5150        CLM  R36
5160        JSB  =OUTSTR
5170        JMP  GET-CH
5180 ! ----------------------
5190 ! ++++++++++++++++++++++
5200 !  SYSTEM ENTRY POINT
5210 ! ----------------------
5220 ERROR+ DAD  6611
5230 ERRORS DAD  100070
5240 GET1$  DAD  14455
5250 SCAN   DAD  11262
5260 STREX+ DAD  13623
5270 BINTAB DAD  101233
5280 OUTSTR DAD  35052
5290 OUTCHR DAD  35114
5300 ROMFL  DAD  101231
5310 LWAMEM DAD  100022
5320 MSLDB. DAD  63604
5330 NXTMEM DAD  100006
5340 MOVUP  DAD  37365
5350 MOVDN  DAD  37324
5360 FWBIN  DAD  100020
5370 ROMJSB DAD  4776
5380 ! ++++++++++++++++++++++++++++++++++++++++++!!!!!!!!!!!!!!
5390 ! ----------------------
5400 MAXBIN EQU  10D
5410 MAXTOK EQU  20D
5420 ! ----------------
5430 num-bn BYT  1
5440 !  DATA ARE
5450 mybase BSZ  30
5460 bin-ls ASP  "B-CUST"
5470 nxt-bn BYT  377
5480        BSZ  100
5490 nxt-as BSZ  2
5500 asc-pt BSZ  2
5510 bas-pt BSZ  2
5520 myeadd BSZ  2
5530 run-pt BSZ  2
5540 old-as BSZ  2
5550 tok-pt BSZ  2
5560 tok-ls BYT  1,3
5570        BSZ  30
5580 ! ----------------------
5590 ! ++++++++++++++++++++++++++++++++++++++++++!!!!!!!!!!!!!!
5600 !  LOADBIN RUNTIM
5610        BYT  241
5620 LOAD.  BSZ  0
5630        BIN  
5640 !  get and save strin
5650        LDMD R20,=BINTAB
5660        LDMD R46,X20,myeadd   !  GET MY ERROR ADDRESS
5670        STMD R46,X20,myerr    !  PUT IN MY HEADER
5680        LDBD R77,X20,num-bn
5690        CMB  R77,=MAXBIN
5700        JNG  ok-rm 
5710        JSB  =ERROR+
5720        BYT  364
5730 !       ---
5740 ok-rm  BSZ  0
5750        LDM  R76,R20
5760        LDMD R66,X20,nxt-as
5770        STMD R66,X20,old-as
5780        ADM  R66,R20
5790        JSB  X20,MOVST 
5800        SBM  R66,R20
5810        STMD R66,X20,nxt-as
5820 ! -----------------------
5830 !  1. HIDE SELF BEFORE LOA
5840        LDMD R22,X20,mybase
5850        DCM  R22              !  BASE TO LOAD AGAINST
5860        LDMD R24,=LWAMEM
5870        STMD R22,=LWAMEM
5880        STMD R22,=FWBIN 
5890        CLM  R26
5900        STMD R26,=BINTAB
5910 ! ----------------------
5920 !  2. PERFORM LOA
5930        PUMD R20,+R6
5940        PUMD R24,+R6
5950        LDM  R70,R10
5960        PUMD R70,+R6
5970        JSB  =ROMJSB
5980        DEF  MSLDB.
5990        BYT  320
6000        POMD R70,-R6
6010        STM  R70,R10
6020        DCM  R12
6030        DCM  R12
6040        DCM  R12
6050        DCM  R12
6060        POMD R24,-R6
6070        POMD R20,-R6
6080        LDBD R30,=ERRORS
6090        JZR  noerrr           !  CONTINUE IF NO ERROR ON LOAD
6100        LDMD R66,X20,old-as
6110        LDB  R30,=377
6120        LDM  R76,R66
6130        ADM  R76,R20
6140        STBD R30,R76          !  RESET TO LAST ASCII ENTRY
6150        STMD R66,X20,nxt-as
6160        LDB  R77,=300
6170        ORB  R17,R77          !  TELL INTERPRETER IS ERROR
6180        STMD R24,=LWAMEM
6190        STMD R20,=BINTAB
6200        RTN  
6210 !       ---
6220 noerrr BSZ  0
6230 ! --------------------
6240 !  3. RESTORE ADDRESSE
6250        STMD R24,=LWAMEM
6260        LDMD R26,=BINTAB      !  GET NEW BINARY'S BASE ADDRESS
6270        STMD R20,=BINTAB
6280 ! ----------------------
6290 !  INCREMENT num-b
6300        LDBD R77,X20,num-bn
6310        ICB  R77
6320        STBD R77,X20,num-bn
6330 ! ----------------------
6340 !  5. save new base add
6350        LDMD R30,X20,bas-pt
6360        ADM  R30,R20          !  POINTER INTO BASE ADDRESS TABLE
6370        STMD R26,R30
6380        STMD R26,X20,mybase   !  NEW LOADING BASE
6390        LDMD R30,X20,bas-pt
6400        ICM  R30
6410        ICM  R30
6420        STMD R30,X20,bas-pt   !  STORE NEW POINTER TO NEXT BASE ADDRESS ENTRY
6430 ! _______________________
6440 !  6. move ASCII
6450 !       1st get ascii bas
6460        LDM  R56,=34,0        !  OFFSET TO ASCII ADDRESS IN BINARY
6470        ADM  R56,R26          !  ADD BIN BASE ADDR
6480        LDMD R36,R56          !  GET ASCII ADDRESS
6490        LDMD R32,X20,asc-pt
6500        ADM  R32,R20          !  POINTER TO MY ASCII TABLE TOP
6510        JSB  X20,MOV-AS
6520        DCM  R32
6530        SBM  R32,R20
6540        STMD R32,X20,asc-pt   !  NEW NEXT ASCII POINTER
6550 ! ----------------------
6560 !  6.1 init TOK #
6570        LDB  R50,R35
6580        LDMD R32,X20,tok-pt
6590        DCM  R32
6600        LDBD R34,R32
6610        ICM  R32
6620        ADB  R35,R34          !  LAST TOK NUMBER
6630        CMB  R35,=MAXTOK
6640        JNG  ok-tok
6650        JSB  =ERROR+
6660        BYT  362
6670 !       --
6680 ok-tok BSZ  0
6690        ICB  R34              !  FIRST TOK #
6700        PUMD R34,+R32
6710        STMD R32,X20,tok-pt   !  SET NEXT TOK# POINTER
6720 ! ----------------------
6730 !   move run classe
6740        LDMD R46,X20,run-pt   !  LOAD NEXT RUNTIME ROUTINE ADDRESS POINTER
6750        LDM  R30,=32,0
6760        ADM  R30,R26
6770        LDMD R30,R30
6780        ICM  R30
6790        ICM  R30              !  NEW BINARIES RUNTIME TABLE BASE
6800        LDB  R77,R50          !  NUMBER OF TOKENS
6810 !       -----
6820 LOP-RO JZR  D-RMOV
6830        POMD R32,+R30         !  GET RUNTIME ADDRESS
6840        DCM  R32
6850        DCM  R32
6860        LDMD R34,R32          !  CLASS BYTES
6870        POMD R66,+R46
6880        DCM  R66
6890        DCM  R66
6900        STMD R34,R66          !  STORE CLASS ABOVE MY RUNTIME ROUTINE
6910        DCB  R77
6920        JMP  LOP-RO
6930 ! -------------
6940 D-RMOV BSZ  0
6950        STMD R46,X20,run-pt   !  SAVE NEW NEXT RUNTIME ADDRESS POINTER
6960 ! ----------------------
6970 !  send them a 'ZZZ
6980 BYNOTE BSZ  0
6990 !       TSB R5
7000 ! P     JZR B
7010 !       LDB R32,=90
7020 !       JSB =OUTCH
7030 !       DCB R5
7040 !       JMP L
7050 ! Y     CLM R3
7060 !       JSB =OUTST
7070        RTN  
7080 ! ----------------------
7090 !  SUBROUTINE TO MOVE BYTE
7100 !  FROM R36+ TO R32+ UNTI
7110 !  A 377. COUNT # KEYWORD
7120 !  IN R35
7130 MOV-AS BSZ  0
7140        LDMD R30,=BINTAB
7150        ADM  R30,=EOASC 
7160        CLB  R35              !  CLEAR KEYWORD COUNT
7170 LOOPM  POBD R34,+R36         !  GET BYTE
7180        JPS  NOINC 
7190        ICB  R35
7200 NOINC  BSZ  0
7210        CMM  R32,R30
7220        JNG  ok-by 
7230        JSB  =ERROR+
7240        BYT  363
7250 ok-by  PUBD R34,+R32         !  STORE BYTE
7260        CMB  R34,=377
7270        JNZ  LOOPM 
7280        DCB  R35
7290        LDB  R50,R35
7300        RTN  
7310 ! _______________________
7320 !  MOVST utility routin
7330 !  move string from stac
7340 !  to area pointed to b
7350 !  R66. follow string wit
7360 !  240 and 377 (end of st
7370 !  and end of list
7380 MOVST  BSZ  0
7390        POMD R74,-R12         ! GET STRING LENGTH AND LOC
7400        PUMD R74,+R12         !  PUT BACK FOR LOADBIN
7410        LDM  R46,R74
7420 ! --------
7430 TSTCNT BSZ  0
7440        JZR  BAK   
7450        POBD R40,+R76         !  GET BYTE
7460        PUBD R40,+R66
7470        DCM  R46
7480        JMP  TSTCNT
7490 ! --------
7500 BAK    BSZ  0
7510 !  load blank with high bi
7520 !  set and a 37
7530        LDB  R40,=240
7540        PUBD R40,+R66
7550        LDB  R40,=377
7560        STBD R40,R66
7570        RTN  
7580 ! ----------------------
7590 !  MOVE A LIST OF ADDRESSE
7600 !  FROM R46+ TO R32+ USIN
7610 !  R35 AS A COUN
7620 ADDR-M TSB  R50
7630 LP-C   JZR  BA-CK 
7640        POMD R30,+R46
7650        PUMD R30,+R32
7660        DCB  R35
7670        JMP  LP-C  
7680 BA-CK  RTN  
7690 ! ------------
7700 ! ---------------------
7710 ! ======================
7720 !  Parse distributo
7730 ! 
7740 P-DIST BSZ  0
7750        BIN  
7760        PUMD R70,+R6
7770        PUMD R40,+R12
7780        LDMD R70,=BINTAB
7790 !       token# in R4
7800 !       get bin
7810        JSB  X70,GETOWN
7820 !       owner# in R7
7830 !       get base addr (R76
7840        JSB  X70,GETBAS
7850 !       also loads BINTA
7860        LDM  R66,=36,0
7870        ADM  R66,R76
7880        LDMD R66,R66
7890        LDB  R76,R43
7900        LLB  R76
7910        CLB  R77
7920        ADM  R76,R66
7930        LDMD R66,R76
7940        PUMD R70,+R6
7950        POMD R40,-R12
7960        JSB  X66,ZRO   
7970 ZRO    DAD  0
7980        POMD R70,-R6
7990        LDM  R76,R70
8000        JSB  X70,ck-err       !  SEE IF ERROR GENERATED
8010        STMD R76,=BINTAB
8020        POMD R70,-R6
8030        RTN  
8040 ! -----------
8050 ! -----------
8060 !  SUBROUTINE token# - R4
8070 !     find binary owner
8080 !      (--> R73
8090 !     relative tok# - R4
8100 GETOWN BSZ  0
8110        LDM  R66,=tok-ls
8120        ADM  R66,R70
8130        LDB  R73,=1
8140 !       --
8150 LOOP-F BSZ  0
8160        POMD R76,+R66
8170        CMB  R77,R43
8180        JPS  GOT-# 
8190        JZR  GOT-# 
8200        ICB  R73
8210        JMP  LOOP-F
8220 ! --------
8230 GOT-#  BSZ  0
8240        SBB  R43,R76
8250        ICB  R43
8260        RTN  
8270 ! --------
8280 ! --------
8290 !  SUBROUTINE TO get bas
8300 !   address of binary whos
8310 !   # is in r7
8320 !   (put base in R76 an
8330 !    BINTAB
8340 GETBAS BSZ  0
8350        LDM  R66,=mybase
8360        ADM  R66,R70
8370 !       --
8380 LOPB-> BSZ  0
8390        POMD R76,+R66
8400        DCB  R73
8410        JZR  GOTBAS
8420        JMP  LOPB->
8430 ! --------
8440 GOTBAS BSZ  0
8450        STMD R76,=BINTAB
8460        RTN  
8470 ! ---------------------
8480 ! ---------------------
8490 !  RUN DISTRIBUTO
8500 !   SUBROUTIN
8510 ! 
8520 R-DIST BSZ  0
8530        BIN  
8540        LDMD R70,=BINTAB
8550 !      token# in R4
8560 !      strip RA from dumm
8570        DCM  R6
8580        DCM  R6
8590 !      get bin
8600        JSB  X70,GETOWN
8610 !      owner# to R7
8620 !      get base address R7
8630        JSB  X70,GETBAS
8640 !      also loads BINTA
8650        LDM  R66,=32,0        !  RUNTIME ADDRESS OFFSET
8660        ADM  R66,R76
8670        LDMD R66,R66          !  BASE OF RUNTIME TABLE
8680        LDB  R76,R43
8690        LLB  R76
8700        CLB  R77
8710        ADM  R76,R66
8720        LDMD R66,R76          !  ADDRESS OF ACTUAL RUNTIME ROUTINE
8730        PUMD R70,+R6
8740        JSB  X66,ZRO   
8750        POMD R70,-R6
8760        JSB  X70,ck-err       !  SEE IF ERROR GENERATED
8770        LDM  R76,R70
8780        STMD R76,=BINTAB      !  RESTORE MY BASE ADDRESS
8790        RTN  
8800 ! -------------------
8810 !  SUBROUTINE ck-er
8820 !    see if error reporte
8830 !    if so set R17 bit
8840 !          load bin erms
8850 !          set E=
8860 !    else set E=
8870 !  (assume my base in R70
8880 !  (assume bin base i
8890 !   BINTAB
8900 ! 
8910 ck-err BSZ  0
8920        CLE  
8930        LDBD R60,=ERRORS
8940        JZR  n-bak 
8950 !       ---is error
8960        ICE                   !  set error flag
8970        LDMD R66,=BINTAB
8980        ADM  R66,=40,0        !  GET BI ERMG ADDR
8990        LDMD R66,R66
9000        STMD R66,X70,myerr    !  PUT HIS ERMSG ADDR IN MY HEADER
9010 n-bak  RTN  
9020 ! ======================
9030 ! ======================
9040        FIN  
