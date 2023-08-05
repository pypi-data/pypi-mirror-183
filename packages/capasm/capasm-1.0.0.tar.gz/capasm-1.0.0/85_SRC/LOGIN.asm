1000 ! !!!!!!!!!!!!!!!!!!!!!!!
1010 ! 
1020 !   TOOLING UTILITY BINAR
1030 !   This binary provides
1040 !     LOGIN a fn of no arg
1050 !           which returns 
1060 !           and logs in al
1070 !           IOPs on the fl
1080 !     PEEK(addr) a fn of 
1090 !           numarg whic
1100 !           returns the me
1110 !           contents of it
1120 !           addr ar
1130 !     POKE(val,addr) a f
1140 !           of 2 num arg
1150 !           which store
1160 !           arg 1 into add
1170 !           of arg 
1180 !     TSTATUS(s.c.,reg
1190 !           a fn of 2 nu
1200 !           args. Doe
1210 !           the IOROM STA
1220 !           but with tim
1230 !           out count
1240 ! ---------------------
1250 !      A.L.R. CVD 7-8
1260 ! ---------------------
1270        NAM  LOGIN 
1280 ! ---------------------
1290        DEF  RUNTIM
1300        DEF  ASCIIS
1310        DEF  PARSE 
1320        DEF  ERMSG 
1330        DEF  INIT  
1340 ! ---------------------
1350 PARSE  BYT  0,0
1360 ! ---------------------
1370 RUNTIM BYT  0,0
1380        DEF  LOGIN.
1390        DEF  PEEK. 
1400        DEF  POKE. 
1410        DEF  TOSTA.
1420        BYT  377,377
1430 ! ---------------------
1440 ASCIIS ASP  5,LOGIN
1450        ASP  4,PEEK
1460        ASP  4,POKE
1470        ASP  7,TSTATUS
1480        BYT  377
1490 ! ---------------------
1500 ERMSG  BYT  377
1510 ! ---------------------
1520 INIT   RTN  
1530 !       no initializatio
1540 !       for no
1550 ! ---------------------
1560        BYT  0,55
1570 LOGIN. BIN  
1580 !       set ROMFL to impl
1590 !       PWO, then transfe
1600 !       to IOROM IOP rese
1610 !       and login code
1620 !       (Be sure to ente
1630 !        IOROM below it
1640 !        ram steal!
1650 !       --- --
1660 !       Must save and res
1670 !       regs to protect sy
1680 !       reg from IOROM
1690        LDM  R70,R10
1700        PUMD R70,+R6
1710        LDM  R70,R20
1720        PUMD R70,+R6
1730        LDM  R70,R30
1740        PUMD R70,+R6
1750        PUMD R40,+R6
1760 !       --- RESET CARD
1770        LDB  R30,=200
1780        LDBD R31,=INTRSC      !  STOP IO INTERRUPTS
1790        LDM  R26,=120,377
1800 RSLOP- STBD R30,R26
1810        LDB  R31,=40
1820 WLOP+  DCB  R31
1830        JNZ  WLOP+ 
1840        PUBD R#,+R26
1850        ICM  R26
1860        CMB  R26,=140
1870        JNC  RSLOP-
1880 !       --- register
1890 !       --- saved,now logi
1900 !       --- 1st set ROMF
1910        CLB  R41
1920        STBD R41,=ROMFL 
1930 !       --- 2nd call IORO
1940        JSB  =ROMJSB
1950        DEF  IORINI
1960        BYT  300
1970 IORINI DAD  60737
1980 !       --- clean up b
1990 !       --- reg restor
2000        POMD R40,-R6
2010        POMD R70,-R6
2020        STM  R70,R30
2030        POMD R70,-R6
2040        STM  R70,R20
2050        POMD R70,-R6
2060        STM  R74,R14
2070        CLM  R70
2080        PUMD R70,+R12
2090        RTN  
2100 ! ---------------------
2110        BYT  20,55
2120 PEEK.  BIN  
2130 !  PEEK looks into HP-8
2140 !  memory.  The argument i
2150 !  the address whose valu
2160 !  in mem is to be returne
2170 !  First, get the arg an
2180 !  convert to a binary
2190 !  then get the mem valu
2200 !  and convert to BCD an
2210 !  leave on stack (ret it
2220 !       --- reg sav
2230        LDM  R70,R10
2240        PUMD R70,+R6
2250        LDM  R70,R20
2260        PUMD R70,+R6
2270 !       ---get arg and con
2280 !       ---to bin using
2290 !       --- ONEB(X-32k)+32
2300        JSB  =ONER  
2310        LDM  R50,R40
2320        LDM  R40,=4,0,0,0,0,200,166,62
2330 !       --- BCD 32
2340        JSB  =SUB10 
2350 !       --- get + conv in
2360        JSB  =ONEB  
2370 !       --- add back 32
2380        BIN  
2390        LDM  R46,=0,200
2400        ADM  R76,R46
2410        LDBD R36,R76
2420        CLB  R37
2430 !       --- convert to BC
2440        JSB  =CONBIN
2450        PUMD R40,+R12
2460 !       --- rest reg & RT
2470        POMD R70,-R6
2480        STM  R70,R20
2490        POMD R70,-R6
2500        STM  R74,R14
2510        RTN  
2520 ! ---------------------
2530        BYT  40,55
2540 POKE.  BIN  
2550 !  POKE is used to chang
2560 !  the value of a mem lo
2570 !  First get the addr an
2580 !  value to poke as binar
2590 !  values. Then store an
2600 !  return 0
2610        LDM  R70,R10
2620        PUMD R70,+R6
2630        LDM  R70,R20
2640        PUMD R70,+R6
2650 !       ^^^ save re
2660 !       ||
2670 !       --- and get arg
2680        JSB  =ONER  
2690        LDM  R50,R40
2700        LDM  R40,=4,0,0,0,0,200,166,62
2710        JSB  =SUB10 
2720        JSB  =ONEB  
2730        BIN  
2740        LDM  R46,=0,200
2750        ADM  R76,R46
2760        PUMD R76,+R6
2770        JSB  =ONEB  
2780 !       --- addr is in R3
2790 !       --- val is in R4
2800 !       --- store valu
2810        POMD R76,-R6
2820        STBD R46,R76
2830 ! +++++++++++++++++++++
2840 ! +NOTE:               
2850 ! +   VALUE STORE IS   
2860 ! +   MODULO 256       
2870 ! +++++++++++++++++++++
2880 !       --- rest re
2890        POMD R70,-R6
2900        STM  R70,R20
2910        POMD R70,-R6
2920        STM  R74,R14
2930 !       --- and return 
2940        CLM  R70
2950        PUMD R70,+R12
2960        RTN  
2970 ! ---------------------
2980 !   Time out STATU
2990 !     TSTATUS(sc,reg
3000 !  1. get sc and reg an
3010 !     convert to byte
3020 !  2. init for MSRO
3030 !  5. read IOP re
3040 !  6. convert to BCD + rt
3050 ! .....................
3060 !  7. If time-out then rt
3070 !     1024 (TO indicator
3080 ! ----------------------
3090        BYT  40,55
3100 TOSTA. BIN  
3110 ! 000000--- 0. save re
3120        LDM  R70,R10
3130        PUMD R70,+R6
3140        LDM  R70,R20
3150        PUMD R70,+R6
3160        LDM  R70,R30
3170        PUMD R70,+R6
3180 ! 111111--- 1. get sc + re
3190 !              as byte
3200        JSB  =ONEB  
3210        LDMD R36,=BINTAB
3220        STBD R46,X36,REGLOC
3230        JSB  =ONEB  
3240        LDMD R36,=BINTAB
3250        STBD R46,X36,SCLOC 
3260 ! 222222--- 2. init for M
3270        BIN  
3280        LDMD R14,=MSBASE
3290        LDM  R66,R14
3300        ADM  R66,=DATAB 
3310        LDMD R44,X14,ACTMSU
3320        LDM  R26,=120,377
3330        LDBD R45,X36,SCLOC 
3340        LDB  R46,=3
3350        SBB  R45,R46
3360        ADB  R26,R45
3370        ADB  R26,R45
3380        LDM  R76,R26
3390        ICM  R76
3400        STMD R76,=INCRA 
3410        CLM  R46
3420        STM  R46,R22
3430        LDM  R0,=300,10
3440        CLB  R52
3450 ! 444444--- 4. write IO
3460 !              reg pointe
3470        LDBD R46,X36,REGLOC
3480        STMD R6,X36,RTNADD
3490        LDB  R57,=1
3500        JSB  X36,DATAIN
3510 ! 666666--- 6. convert t
3520 !              BCD + rt
3530 ! **********************
3540 TST1   BIN  
3550        LDBD R36,R66
3560        CLB  R37
3570        JSB  =CONBIN
3580        PUMD R40,+R12
3590 ! 6.56.5--- 6.5 restore re
3600 GOBACK POMD R70,-R6
3610        STM  R70,R30
3620        POMD R70,-R6
3630        STM  R70,R20
3640        POMD R70,-R6
3650        STM  R74,R14
3660        RTN  
3670 ! ......................
3680 ! ......................
3690 CNTERR BSZ  0
3700 ! 777777--- 7. IOP timeou
3710 !              return 102
3720        LDMD R36,=BINTAB
3730        LDMD R6,X36,RTNADD
3740        LDM  R36,=0,4
3750        JSB  =CONBIN
3760        PUMD R40,+R12
3770        JMP  GOBACK
3780 ! ----utilities------
3790 !  These routines are fro
3800 ! the MSROM. Please refe
3810 ! to MSROM documentatio
3820 ! for explanation of thes
3830 ! utilities!!
3840 ! ......--------------
3850 DAT01  BIN  
3860        LDB  R57,=1
3870        JSB  X36,DATOUT
3880        RTN  
3890 ! ......--------------
3900 DATOUT BIN  
3910        JSB  X36,DATOU+
3920 LOP-04 BSZ  0
3930 ! *********************
3940        LDBD R46,X36,REGLOC
3950 ! *********************
3960        DCB  R57
3970        JZR  DONOUT
3980        JSB  X36,OCK   
3990        STBD R46,R76
4000        JMP  LOP-04
4010 DONOUT BSZ  0
4020        JSB  X36,OCK   
4030        LDB  R75,=4
4040        STBD R#,R26
4050        STBD R46,R76
4060        JSB  X36,OBFCK 
4070 OPLB++ BSZ  0
4080        CLB  R57
4090        STBD R57,R26
4100        RTN  
4110 ! ......-------------
4120 CNTER1 JMP  CNTERR
4130 ! ......-------------
4140 OCK    BSZ  0
4150        STM  R0,R34
4160 OCKLOP BSZ  0
4170        DCM  R34
4180        JZR  CNTERR
4190        LDBD R75,R26
4200        JNG  OCKLOP
4210        RTN  
4220 ! ......--------------
4230 OBFCK  BSZ  0
4240        STM  R0,R34
4250 OBFLOP BSZ  0
4260        JSB  X36,OCKLOP
4270        LRB  R75
4280        JOD  OBFLOP
4290        RTN  
4300 ! ......-------------
4310 DATOU+ BSZ  0
4320        JSB  X36,CMDHS 
4330        JSB  X36,OCK   
4340        CLB  R75
4350        STBD R75,R26
4360        LDM  R24,R66
4370        RTN  
4380 ! ......-------------
4390 CMDHS  BSZ  0
4400        JSB  X36,OBFCK 
4410        LDB  R75,=2
4420        STBD R75,R26
4430        STBD R46,R76
4440        RTN  
4450 ! ......--------------
4460 CNTOPS JMP  CNTER1
4470 ! ......--------------
4480 DATAIN BSZ  0
4490        JSB  X36,DATOU+
4500 LOP-10 BSZ  0
4510        JSB  X36,ICK   
4520        LDBD R75,R26
4530        LRB  R#
4540        LRB  R#
4550        JOD  DONIN 
4560        LDBD R46,R76
4570 ! *******************
4580        STBD R46,R24
4590 ! *******************
4600        DCB  R57
4610        JZR  STTCED
4620        STBD R46,R76
4630        JMP  LOP-10
4640 DONIN  BSZ  0
4650        LDBD R46,R76
4660 ! *******************
4670        STBD R46,R24
4680 ! *******************
4690        DCB  R57
4700        JMP  PT..1 
4710 STTCED BSZ  0
4720        LDB  R#,=4
4730        STBD R#,R26
4740 PT..1  BSZ  0
4750        LDM  R34,R0
4760 LOP-11 LDBD R75,R26
4770        DCM  R34
4780        JZR  CNTOPS
4790        LRB  R75
4800        JOD  LOP-11
4810        JMP  OPLB++
4820 ! ......------------
4830 ICK    BSZ  0
4840        STM  R0,R34
4850 ICKLOP BSZ  0
4860        DCM  R34
4870        JZR  CNTOPS
4880        LDBD R75,R26
4890        JEV  ICKLOP
4900        RTN  
4910 ! ......-------------
4920 ! ......-------------
4930 ! ......................
4940 RTNADD BYT  0,0
4950 SCLOC  BYT  0
4960 REGLOC BYT  0
4970 ! ---------------------
4980 !  TABLE OF EXTERNAL ADDR
4990 ! '''''''''''''''''''''
5000 ROMFL  DAD  101231
5010 ROMJSB DAD  4776
5020 CONINT DAD  44321
5030 CONBIN DAD  3572
5040 ONEB   DAD  56113
5050 ONER   DAD  56215
5060 SUB10  DAD  52137
5070 INTRSC DAD  177500
5080 DATAB  DAD  76
5090 ACTMSU DAD  135
5100 INCRA  DAD  101121
5110 SCRTYP DAD  101120
5120 SAVER6 DAD  101174
5130 GINTEN DAD  177400
5140 TINTEN DAD  101071
5150 MSBASE DAD  102540
5160 BINTAB DAD  101233
5170        FIN  
