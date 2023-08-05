0020        NAM  STRBIN
0040        DEF  RUNTIM
0060        DEF  ASCIIS
0080        DEF  PARSE 
0100        DEF  ERMSG 
0120        DEF  INIT  
0140 PARSE  BYT  0,0
0160        DEF  UNLDP 
0180 RUNTIM BYT  0,0
0200        DEF  UNLD. 
0220        DEF  UDL$. 
0240        DEF  LWC$. 
0260        DEF  RPT$. 
0280        DEF  REV$. 
0300        DEF  TRIM$.
0320        DEF  ROT$. 
0340        DEF  NOC.  
0360        DEF  SAR$. 
0380        DEF  .   
0400        BYT  377,377
0420 ASCIIS ASP  12,SCRATCHBIN
0440        ASP  4,UDL$
0460        ASP  4,LWC$
0480        ASP  4,RPT$
0500        ASP  4,REV$
0520        ASP  5,TRIM$
0540        ASP  4,ROT$
0560        ASP  3,NOC
0580        ASP  4,SAR$
0600        ASP  2,
0620 ERMSG  BYT  377
0640 UNLDP  LDB  R47,R43
0660        LDB  R45,=371
0680        PUMD R45,+R12
0700        JSB  =SCAN  
0720 INIT   RTN  
0740 ! *************************
0760 ! *                        
0780 ! *  UDL$(<string exp.>)   
0800 ! *      RETURN THE STRING 
0820 ! *      UNDERLINED.       
0840 ! *                        
0860 ! *************************
0880        BYT  30,56
0900 UDL$.  LDMD R22,=BINTAB
0920        JSB  X22,POPUSH
0940        LDB  R34,=200
0960 MOREU  DCM  R30
0980        JNC  DONE  
1000        POBD R20,+R36
1020        ORB  R20,R34
1040        PUBD R20,+R26
1060        JMP  MOREU 
1080 DONE   RTN  
1100 ! *************************
1120 ! *                        
1140 ! *  LWC$(<string exp.>)   
1160 ! *      RETURNS THE STRING
1180 ! *      AS LOWER CASE.    
1200 ! *                        
1220 ! *************************
1240        BYT  30,56
1260 LWC$.  LDMD R22,=BINTAB
1280        JSB  X22,POPUSH
1300 MOREL  DCM  R30
1320        JNC  DONE  
1340        POBD R20,+R36
1360        CMB  R20,=101
1380        JNG  NOCHNG
1400        CMB  R20,=133
1420        JPS  NOCHNG
1440        ADB  R20,=40
1460 NOCHNG PUBD R20,+R26
1480        JMP  MOREL 
1500 ! *************************
1520 ! *                        
1540 ! *  RPT$(<string exp.>,#) 
1560 ! *      RETURNS THE STRING
1580 ! *      THE # OF TIMES.   
1600 ! *                        
1620 ! *************************
1640        BYT  50,56
1660 RPT$.  JSB  =ONEB  
1680        POMD R30,-R12
1700        POMD R24,-R12
1720        CLM  R76
1740        TSM  R46
1760        JPS  COUNT 
1780        CLM  R46
1800 COUNT  DCM  R46
1820        JNC  GETMEM
1840        ADM  R76,R24
1860        JMP  COUNT 
1880 GETMEM LDM  R56,R76
1900        JSB  =RSMEM-
1920        PUMD R76,+R12
1940        PUMD R26,+R12
1960        DCM  R76
1980        JNG  DONE  
2000 SETPNT LDM  R32,R24
2020        LDM  R34,R30
2040 COPYRP DCM  R32
2060        JNG  SETPNT
2080        POBD R20,+R34
2100        PUBD R20,+R26
2120        DCM  R76
2140        JPS  COPYRP
2160        RTN  
2180 ! ************************
2200 ! *                       
2220 ! * REV$(<string exp.>)   
2240 ! *     RETURNS THE STRING
2260 ! *     IN REVERSE ORDER. 
2280 ! *                       
2300 ! ************************
2320        BYT  30,56
2340 REV$.  LDMD R22,=BINTAB
2360        JSB  X22,POPUSH
2380        ADM  R26,R30
2400 MOREV  DCM  R30
2420        JNC  DONE  
2440        POBD R20,+R36
2460        PUBD R20,-R26
2480        JMP  MOREV 
2500 ! ************************
2520 ! *                       
2540 ! * TRIM$(<string exp.>)  
2560 ! *     RETURN THE STRING 
2580 ! *     WITH ALL LEADING  
2600 ! *     AND TRAILING      
2620 ! *     BLANKS DELETED    
2640 ! *                       
2660 ! ************************
2680        BYT  30,56
2700 TRIM$. POMD R36,-R12
2720        POMD R30,-R12
2740        BIN  
2760        STM  R30,R32
2780        ADM  R30,R36
2800 MORETR DCM  R32
2820        POBD R20,-R30
2840        CMB  R20,=40
2860        JZR  MORETR
2880        ICM  R32
2900        LDM  R30,R36
2920 MORELE DCM  R32
2940        POBD R20,+R30
2960        CMB  R20,=40
2980        JZR  MORELE
3000        ICM  R32
3020        PUMD R32,+R12
3040        DCM  R30
3060        PUMD R30,+R12
3080 DONE5  RTN  
3100 ! ************************
3120 ! *                       
3140 ! * ROT$(<string exp.>,#) 
3160 ! *     RETURN THE STRING 
3180 ! *     ROTATED CIRCULAR  
3200 ! *     +/- THE #         
3220 ! *                       
3240 ! ************************
3260        BYT  50,56
3280 ROT$.  JSB  =ONEB  
3300        LDMD R22,=BINTAB
3320        JSB  X22,POPUSH
3340        TSM  R76
3360        JPS  MOD   
3380 STILL- ADM  R76,R30
3400        TSM  R76
3420        JNG  STILL-
3440 MOD    CMM  R30,R76
3460        JPS  STAROT
3480        SBM  R76,R30
3500        JMP  MOD   
3520 STAROT LDM  R32,R36
3540        SBM  R30,R76
3560        ADM  R32,R30
3580 COPYE  DCM  R76
3600        JNC  COPYB 
3620        POBD R20,+R32
3640        PUBD R20,+R26
3660        JMP  COPYE 
3680 COPYB  DCM  R30
3700        JNC  DONE1 
3720        POBD R20,+R36
3740        PUBD R20,+R26
3760        JMP  COPYB 
3780 DONE1  RTN  
3800 ! ************************
3820 ! *                       
3840 ! * NOC(<string exp.>,    
3860 ! *      <string exp.>)   
3880 ! *     RETURNS THE # OF  
3900 ! *     OCCURANCES        
3920 ! *                       
3940 ! ************************
3960        BYT  52,55
3980 NOC.   CLM  R14
4000        POMD R70,-R12
4020 MOREOC PUMD R#,+R12
4040        JSB  =POS.  
4060        POMD R60,-R12
4080        PUMD R70,+R12
4100        PUMD R60,+R12
4120        JSB  =ONEB  
4140        POMD R70,-R12
4160        TSM  R46
4180        JZR  DONOC 
4200        ICM  R14
4220        STM  R70,R20
4240        ADM  R22,R46
4260        ADM  R22,R24
4280        DCM  R22
4300        ICM  R20
4320        SBM  R20,R46
4340        SBM  R20,R24
4360        JNG  DONOC 
4380        LDM  R70,R20
4400        JMP  MOREOC
4420 DONOC  LDM  R36,R14
4440        JSB  =CONBIN
4460        PUMD R40,+R12
4480        RTN  
4500 ! ************************
4520 ! *                       
4540 ! * SAR$(<string exp.>,   
4560 ! *      <string exp.>,   
4580 ! *      <string exp.>)   
4600 ! *     RETURNS THE THE   
4620 ! *     STRING WITH Y$    
4640 ! *     REPLACED BY Z$    
4660 ! *                       
4680 ! ************************
4700        BYT  200,72,56
4720 SAR$.  POMD R44,-R12
4740        POMD R70,-R12
4760        PUMD R70,+R12
4780        PUMD R44,+R12
4800        PUMD R70,+R12
4820        LDMD R22,=BINTAB
4840        JSB  X22,NOC.  
4860        JSB  =ONEB  
4880        POMD R54,-R12
4900        POMD R40,-R12
4920        PUMD R40,+R12
4940        PUMD R54,+R12
4960        LDM  R14,R40
4980        LDM  R66,R54
5000        JSB  =INTMUL
5020        ADM  R14,R54
5040        LDM  R66,R44
5060        JSB  =INTMUL
5080        SBM  R14,R54
5100        STM  R14,R56
5120        PUMD R14,+R12
5140        JSB  =RSMEM-
5160        PUMD R26,+R12
5180        POMD R60,-R12
5200        POMD R70,-R12
5220 GO-ON  PUMD R60,+R12
5240        PUMD R70,+R12
5260        JSB  =POS.  
5280        POMD R60,-R12
5300        PUMD R70,+R12
5320        PUMD R60,+R12
5340        JSB  =ONEB  
5360        POMD R70,-R12
5380        POMD R60,-R12
5400        LDM  R34,R62
5420        LDM  R56,R60
5440        PUMD R46,+R12
5460        TSM  R46
5480        JZR  FINISH
5500 COPYX$ DCM  R46
5520        JZR  COPYZ$
5540        POBD R20,+R72
5560        PUBD R20,+R66
5580        JMP  COPYX$
5600 COPYZ$ DCM  R56
5620        JNC  RESET 
5640        POBD R20,+R34
5660        PUBD R20,+R66
5680        JMP  COPYZ$
5700 RESET  STM  R60,R20
5720        STM  R70,R30
5740        ADM  R32,R34
5760        POMD R46,-R12
5780        ICM  R30
5800        SBM  R30,R46
5820        SBM  R30,R34
5840        JNG  DONE2 
5860        LDM  R60,R20
5880        LDM  R70,R30
5900        JMP  GO-ON 
5920 FINISH POMD R46,-R12
5940        STM  R60,R20
5960        STM  R70,R30
5980 FINCOP DCM  R30
6000        JNC  DONE2 
6020        POBD R46,+R32
6040        PUBD R46,+R66
6060        JMP  FINCOP
6080 DONE2  LDM  R14,R64
6100        PUMD R14,+R12
6120        SBM  R66,R14
6140        PUMD R66,+R12
6160        RTN  
6180 POPUSH POMD R36,-R12
6200        POMD R30,-R12
6220        STM  R30,R56
6240        JSB  =RSMEM-
6260        PUMD R30,+R12
6280        PUMD R26,+R12
6300        BIN  
6320        RTN  
6340 ! ************************
6360 ! *                       
6380 ! *  - RETURNS REVISION 
6400 ! *      DATE.            
6420 ! *                       
6440 ! ************************
6460        BYT  0,56
6480 .    LDM  R44,=8D,0
6500        DEF  DATE  
6520        ADMD R46,=BINTAB
6540        PUMD R44,+R12
6560        RTN  
6580        BYT  241
6600 UNLD.  STBD R#,=GINTDS
6620        LDMD R24,=BINTAB
6640        DCM  R24
6660        LDMD R26,=LWAMEM
6680        STM  R26,R22
6700        SBM  R22,R24
6720        LDB  R20,=4
6740        LDM  R32,=LAVAIL
6760 UNLD1  LDMD R36,R32
6780        ADM  R36,R22
6800        PUMD R36,+R32
6820        DCB  R20
6840        JNZ  UNLD1 
6860        LDMD R36,R32
6880        CMMD R36,=LWAMEM
6900        JZR  UNLD2 
6920        ADM  R36,R22
6940        STMD R36,R32
6960 UNLD2  CLM  R#
6980        STMD R#,=BINTAB
7000        LDM  R#,R12
7020        LDM  R41,=316
7040        DEF  MOVDN 
7060        STBD R#,=GINTEN
7080        RTN  
7100        STMD R41,R36
7120        DCM  R36
7140        LDM  R4,R36
7160 DATE   ASC  "07/17/80"
7180 BINTAB DAD  101233
7200 POS.   DAD  03435
7220 ONEB   DAD  56113
7240 RSMEM- DAD  37453
7260 CONBIN DAD  03572
7280 INTMUL DAD  53076
7300 SCAN   DAD  11262
7320 GINTDS DAD  177401
7340 LWAMEM DAD  100022
7360 LAVAIL DAD  100010
7380 MOVDN  DAD  37324
7400 GINTEN DAD  177400
7420        FIN  
