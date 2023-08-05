0020        NAM  CHARIO
0040        DEF  RUNTIM
0060        DEF  TOKS  
0080        DEF  PARSES
0100        DEF  ERMSG 
0120        DEF  INIT  
0140 RUNTIM BSZ  2
0160        DEF  TRACK.
0180        DEF  UNLOD.
0200        DEF  .   
0220 PARSES BSZ  2
0240        DEF  TPARSE
0260        DEF  UPARSE
0280 ERMSG  BYT  377,377
0300 TOKS   ASP  "TRACK"
0320        ASP  "SCRATCHBIN"
0340        ASP  ""
0360        BYT  377
0380 INIT   RTN  
0400 ! *************************
0420 TPARSE PUBD R43,+R6
0440        JSB  =NUMVA+
0460        JEN  OK    
0480 ERR    JSB  =ERROR+
0500        BYT  88D
0520 OK     JSB  =GETCMA
0540        CMB  R14,=1
0560        JNZ  ERR   
0580        ADB  R14,=20
0600        JSB  =PUSH45
0620        JSB  =GETCMA
0640        CMB  R14,=1
0660        JNZ  ERR   
0680        ADB  R14,=20
0700        JSB  =PUSH45
0720        JSB  =GETCMA
0740        CMB  R14,=1
0760        JNZ  ERR   
0780        ADB  R14,=20
0800        JSB  =PUSH45
0820 DONE   POBD R57,-R6
0840        LDB  R55,=371
0860        PUMD R55,+R12
0880        RTN  
0900 ! *************************
0920 UPARSE PUBD R43,+R6
0940        JSB  =SCAN  
0960        JMP  DONE  
0980 ! *************************
1000 GERROR JSB  =ERROR+
1020        BYT  81D
1040 ! *************************
1060        BYT  241
1080 TRACK. LDMD R14,=BINTAB
1100        JSB  =GRAPH.
1120        POMD R40,-R12
1140        POMD R64,-R12
1160        POMD R50,-R12
1180        JZR  GERROR
1200        PUMD R64,+R12
1220        PUMD R40,+R12
1240        JSB  X14,SETUP2
1260        PUMD R34,+R6
1280        PUMD R22,+R6
1300        JSB  X14,PLOT  
1320        POMD R22,-R6
1340        POMD R34,-R6
1360 ! ************************
1380 ! * ENTER 6 BYTES FROM    
1400 ! *  THE TABLET           
1420 ! ************************
1440 TLOOP  LDB  R70,=6
1460        JSB  X14,GET#S 
1480        PUMD R34,+R6
1500        PUMD R22,+R6
1520        ANM  R32,=204,0
1540 ! ************************
1560 ! * CHECK STATUS FOR PEN  
1580 ! *  PRESS                
1600 ! ************************
1620        JNZ  BITSET
1640        LDMD R14,=BINTAB
1660        JSB  X14,MAP   
1680        CMBD R36,=YMAP  
1700        JNZ  MOVED 
1720        CMBD R76,=XMAP  
1740        JNZ  MOVED 
1760 GTO    POMD R22,-R6
1780        POMD R34,-R6
1800        BIN  
1820        LDMD R14,=BINTAB
1840        JMP  TLOOP 
1860 ! ************************
1880 ! * THE PEN HAS MOVED, SO 
1881 ! * MOVE THE CURSOR.      
1900 ! ************************
1920 MOVED  PUBD R36,+R6
1940        PUBD R76,+R6
1960        JSB  X14,PLOT  
1980        POBD R36,-R6
2000        POBD R37,-R6
2020        STMD R36,=XMAP  
2040        JSB  X14,PLOT  
2060        JMP  GTO   
2061 ! ************************
2062 ! * PEN HAS BEEN PRESSED  
2080 ! ************************
2100 BITSET LDMD R14,=BINTAB
2120        TSB  R32
2140        JNG  MENU  
2160        JSB  X14,OUTXY 
2180        CLM  R40
2200        PUMD R40,+R12
2220        JSB  =STOSV 
2240        JMP  BITFIN
2241 ! ************************
2242 ! * PEN WAS ON A MENU.    
2260 ! ************************
2280 MENU   CLM  R40
2300        PUMD R40,+R12
2320        JSB  =STOSV 
2340        POMD R22,-R6
2360        POMD R34,-R6
2380        LDMD R14,=BINTAB
2400        JSB  X14,GETMEN
2420        PUMD R34,+R6
2440        PUMD R22,+R6
2460        JSB  X14,FINMEN
2480        CLM  R40
2500        LDB  R47,=10C
2520        PUMD R40,+R12
2540        JSB  =STOSV 
2560 BITFIN POMD R22,-R6
2580        POMD R34,-R6
2600        LDMD R14,=BINTAB
2620        JSB  X14,FINISH
2640        JSB  X14,PLOT  
2660        RTN  
2661 ! ************************
2662 ! * OUTPUTS OR ERASES THE 
2663 ! * CURSOR, DEPENDING ON  
2664 ! * WHETHER A CURSOR WAS  
2665 ! * ALREADY THERE OR NOT. 
2680 ! ************************
2700 PLOT   LDMD R14,=BINTAB
2720        LDM  R20,=CURSES
2740        ADM  R20,R14
2760        LDBD R22,=XMAP  
2780        ANM  R22,=3,0
2800        LDM  R34,R22
2820        LLM  R34
2840        LLM  R34
2860        ADM  R34,R22
2880        ADM  R34,R20
2900        LDM  R22,=5,0
2920        LDM  R44,=1,0,1,0
2940        LDMD R56,=XMAP  
2960        PUMD R56,+R6
2980        JSB  =BPLOT+
3000        POMD R56,-R6
3020        STMD R56,=XMAP  
3040        RTN  
3041 ! ************************
3042 ! * DIVIDES X OR Y BY 48  
3043 ! * FOR SCALING TO ABOUT  
3044 ! * 192 X 256.            
3060 ! ************************
3080 DIV48  CLM  R46
3100        XRB  R36,R37
3120        XRB  R37,R36
3140        XRB  R36,R37
3160        TSM  R36
3180        JPS  POSIT 
3200        CLM  R36
3220 POSIT  BCD  
3240        LRM  R37
3260        BIN  
3280 NOTD   ICM  R46
3300        SBM  R36,=3,0
3320        JPS  NOTD  
3340        LDM  R36,R46
3360        RTN  
3361 ! ************************
3362 ! * READS BYTES FROM THE  
3363 ! * CHARIOT. COUNT TO BE  
3364 ! * READ IS IN R70 AT ENTR
3380 ! ************************
3400 GET#S  PUBD R70,+R6
3420        LDB  R46,=ENTCMD
3440        JSB  =ROMJSB
3460        DEF  CMDCED
3480        BYT  360
3500        LDM  R26,=INPBUF
3520        POBD R70,-R6
3540        CLM  R56
3560 LOP10- LDBD R30,R22
3580        JOD  LOP10+
3600        DCM  R56
3620        JNZ  LOP10-
3640        JMP  HERROR
3660 LOP10+ LDBD R32,R34
3680        PUBD R32,+R26
3700        DCB  R70
3720        JZR  LOP-11
3740        STBD R32,R34
3760        JMP  LOP10-
3780 LOP-11 LDB  R30,=4
3800        STBD R30,R22
3820 LOP-1+ LDBD R30,R22
3840        LRB  R30
3860        JOD  LOP-1+
3880        CLB  R30
3900        STBD R30,R22
3920        LDMD R14,=BINTAB
3940        RTN  
3960 ! ************************
3980 HERROR POMD R36,-R6
4000        JSB  =ERROR+
4020        BYT  81D
4021 ! ************************
4022 ! ** THIS ROUTINE INITS  *
4023 ! ** CHARIOT TO TALK AND *
4024 ! ** CAPRICORN TO LISTEN.*
4040 ! ************************
4060 SETUP  LDMD R60,X14,S.C.  
4080        STMD R60,=SCTEMP
4100 ! ************************
4120 ! * PROCESS ADDRESS       
4140 ! ************************
4160        JSB  =ROMJSB
4180        DEF  PRADDR
4200        BYT  360
4220        CMB  R17,=300
4240        JCY  HERROR
4260        LDB  R21,R46
4280        CLM  R22
4300        LDB  R22,R56
4320 ! ************************
4340 ! *  SET UP ADDRESS       
4360 ! ************************
4380        JSB  =ROMJSB
4400        DEF  SETSC-
4420        BYT  360
4440        ADB  R21,=100
4460        TSB  R21
4480        JNG  HERROR
4500 ! ************************
4520 ! * UNLISTEN; UNTALK      
4540 ! ************************
4560        JSB  =ROMJSB
4580        DEF  LLINIT
4600        BYT  360
4620 ! ************************
4640 ! * CAPRICORN LISTEN      
4660 ! ************************
4680        LDB  R46,=MLA   
4700        JSB  =ROMJSB
4720        DEF  CMDOUT
4740        BYT  360
4760 ! ************************
4780 ! * TABLET TALK           
4800 ! ************************
4820        JSB  =ROMJSB
4840        DEF  LADTAD
4860        BYT  360
4880        LDMD R14,=BINTAB
4900        RTN  
4901 ! ************************
4902 ! ************************
4903 ! ** SETS UP SELECT CODE *
4904 ! ** AND CALLS SETUP FOR *
4905 ! ** UNLISTEN/UNTALK STUFF
4906 ! ************************
4920 ! ************************
4940 SETUP2 PUMD R50,+R12
4960        JSB  =ONER  
4980        STMD R40,=SCTEMP
5000        STMD R40,X14,S.C.  
5020        JSB  =ROMJSB
5040        DEF  ROMRES
5060        BYT  360
5080        LDM  R42,=104,106,73,123,107,73
5100 ! ************************
5120 ! * OUTPUT DF;SG;         
5140 ! ************************
5160        PUMD R42,+R30
5180        LDM  R36,=6,0
5200        STMD R36,=DATLEN
5220        JSB  =ROMJSB
5240        DEF  LOADSC
5260        BYT  360
5280        LDMD R14,=BINTAB
5300        JSB  X14,SETUP 
5320        RTN  
5321 ! ************************
5322 ! * GETS CHARIOT'S NUMBERS
5323 ! * FROM THE INPUT BUFFER 
5324 ! * AND MAPS THEM ONTO THE
5325 ! * 192 X 256 SCALE SCREEN
5340 ! ************************
5360 MAP    LDMD R36,=INPBUF
5380        LDMD R14,=BINTAB
5400        JSB  X14,DIV48 
5420        CMM  R36,=254D,0
5440        JNC  <256  
5460        LDM  R36,=253D,0
5480 <256   STM  R36,R76
5500        LDMD R36,=INP+2 
5520        JSB  X14,DIV48 
5540        CMM  R36,=192D,0
5560        JNC  <192  
5580        LDM  R36,=191D,0
5600 <192   LDM  R46,=190D,0
5620        SBM  R46,R36
5640        JPS  >0    
5660        CLM  R46
5680 >0     STM  R46,R36
5700        RTN  
5701 ! ************************
5702 ! * STORES X AND Y INTO   
5703 ! * VARIABLE AREAS IN PREP
5704 ! * FOR RETURNING TO THE  
5705 ! * SYSTEM.               
5710 ! ************************
5720 OUTXY  LDM  R36,=191D,0
5740        SBBD R36,=YMAP  
5760        SBB  R36,=2
5780        JSB  =CONBIN
5800        BIN  
5820        STMD R40,=PLTMP2
5840        CLM  R36
5860        LDBD R36,=XMAP  
5880        ICM  R36
5900        ICM  R36
5920        JSB  =CONBIN
5940        BIN  
5960        STMD R40,=PLTMP1
5980        JSB  =ROMJSB
6000        DEF  NOPENT
6020        BYT  360
6040        LDMD R14,=BINTAB
6060        RTN  
6061 ! ************************
6062 ! * GETS THE MENU # FROM  
6063 ! * CHARIOT.              
6080 GETMEN LDMD R40,X14,S.C.  
6100        STMD R40,=SCTEMP
6120        JSB  =ROMJSB
6140        DEF  ROMRES
6160        BYT  360
6180        LDM  R45,=122,123,73
6200        PUMD R45,+R30
6220        LDM  R36,=3,0
6240        STMD R36,=DATLEN
6260        JSB  =ROMJSB
6280        DEF  LOADSC
6300        BYT  360
6320        LDMD R14,=BINTAB
6340        JSB  X14,SETUP 
6360        LDB  R70,=2
6380        JSB  X14,GET#S 
6400        RTN  
6401 ! ************************
6402 ! * TAKES THE MENU # FROM 
6403 ! * TRANSLATES IT INTO THE
6404 ! * INTERNAL CAPRICORN    
6405 ! * NUMBER FORMAT AND     
6406 ! * STUFFS IT IN THE      
6407 ! * VARIABLE SPACE.       
6420 ! ************************
6440 FINMEN CLM  R36
6460        LDMD R46,=INPBUF
6480        SBB  R46,=60
6500        SBB  R47,=60
6520        CMB  R47,=335
6540        JZR  ONEDIG
6560        LDB  R46,=10D
6580        ADB  R46,R47
6600 ONEDIG LDB  R36,R46
6620        JSB  =CONBIN
6640        PUMD R40,+R12
6660        JSB  =STOSV 
6680        RTN  
6681 ! ************************
6682 ! * SENDS A DIGITIZE CLEAR
6683 ! * TO CHARIOT.           
6700 ! ************************
6720 FINISH JSB  =ROMJSB
6740        DEF  ROMRES
6760        BYT  360
6780        LDM  R45,=104,103,73
6800 ! ************************
6820 ! * OUTPUT DC;            
6840 ! ************************
6860        PUMD R45,+R30
6880        LDM  R36,=3,0
6900        STMD R36,=DATLEN
6920        JSB  =ROMJSB
6940        DEF  LOADSC
6960        BYT  360
6980        LDMD R14,=BINTAB
7000        RTN  
7001 ! ************************
7002 ! * DATA FOR THE GRAPHICS 
7003 ! * CURSOR.               
7020 ! ************************
7040 CURSES BYT  40,40,370,40,40
7060        BYT  20,20,174,20,20
7080        BYT  10,10,76,10,10
7100        BYT  4,4,37,4,4
7101 ! ************************
7102 ! * THE CONTROL HP FUNCTIO
7103 ! * WHICH RETURNS THE REV 
7104 ! * DATE OF THIS VERSION  
7105 ! * OF THE BINARY.        
7120 ! ************************
7140        BYT  0,56
7160 .    BIN  
7180        LDM  R44,=12D,0
7200        DEF  DATE  
7220        ADMD R46,=BINTAB
7240        PUMD R44,+R12
7260        RTN  
7280 DATE   ASC  "JUNE 12,1980"
7281 ! ************************
7282 ! * THE SCRATCHBIN COMMAND
7300 ! ************************
7320        BYT  241
7340 UNLOD. STBD R#,=GINTDS
7360        LDMD R24,=BINTAB
7380        STM  R24,R22
7400        DCM  R24
7420        LDMD R26,=LWAMEM
7440        STM  R26,R22
7460        SBM  R22,R24
7480        LDB  R20,=4
7500        LDM  R32,=LAVAIL
7520 UNLD1  LDMD R36,R32
7540        ADM  R36,R22
7560        PUMD R36,+R32
7580        DCB  R20
7600        JNZ  UNLD1 
7620        LDMD R36,R32
7640        CMMD R36,=LWAMEM
7660        JZR  UNLD2 
7680        ADM  R36,R22
7700        STMD R36,R32
7720 UNLD2  CLM  R#
7740        STMD R#,=BINTAB
7760        LDM  R#,R12
7780        LDM  R41,=316
7800        DEF  MOVDN 
7820        STBD R#,=GINTEN
7840        RTN  
7860        STMD R41,R36
7880        DCM  R36
7900        LDM  R4,R36
7901 ! ************************
7902 ! * STORAGE FOR CHARIOT'S 
7903 ! * SELECT CODE.          
7920 ! ************************
7940 S.C.   BSZ  10
7960 ! ************************
7980 BINTAB DAD  101233
8000 GINTDS DAD  177401
8020 GINTEN DAD  177400
8040 LWAMEM DAD  100022
8060 LAVAIL DAD  100010
8080 MOVDN  DAD  37324
8100 OUTSTR DAD  35052
8120 PRDRV1 DAD  75767
8140 SCAN   DAD  11262
8160 ONER   DAD  56215
8180 ROMJSB DAD  4776
8200 DATLEN DAD  101223
8220 ERROR+ DAD  6611
8240 INPBUF DAD  100310
8260 INP+2  DAD  100312
8280 GRAPH. DAD  36147
8300 ROMRES DAD  74111
8320 LOADSC DAD  76123
8340 PRADDR DAD  62266
8360 SCTEMP DAD  101110
8380 SETSC- DAD  76752
8400 LLINIT DAD  76260
8420 MLA    EQU  106
8440 CMDOUT DAD  76111
8460 LADTAD DAD  76331
8480 ENTCMD EQU  24
8500 CMDCED DAD  76515
8520 BPLOT+ DAD  34405
8540 MOVE.  DAD  64400
8560 DRAW.  DAD  64435
8580 DIV10  DAD  51644
8600 NUMVA+ DAD  12407
8620 GETCMA DAD  13414
8640 XMAP   DAD  100262
8660 YMAP   DAD  100263
8680 PLTMP1 DAD  101740
8700 PLTMP2 DAD  101750
8720 NOPENT DAD  71355
8740 CONBIN DAD  3572
8760 PUSH45 DAD  14266
8780 STOSV  DAD  45254
8800        FIN  
