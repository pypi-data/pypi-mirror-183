0260 ! ====================
0270 !   parse are
0280 ! -------------
0290 !    get one string ex
0300 CAT.P  BSZ  0
0310        PUBD R43,+R6
0320        JSB  =STREX+
0330        POBD R47,-R6
0340        LDB  R45,=371
0350        PUMD R45,+R12
0360        RTN  
0370 ! --------------------
0380 ! ++++++++++++++++++++
0390 ! --------------------
0400 !       set to send 32 byte
0410 DRIVE- BSZ  0
0420        LDM  R36,=31D,0
0430 DRIVER BSZ  0
0440        LDM  R26,R14
0450        JSB  =DISP. 
0460        JSB  =DRV12.
0470        LDMD R14,=MSBASE
0480        RTN  
0490 ! --------
0500 GETMSU LDM  R26,R12
0510        SBMD R26,=TOS   
0520        JZR  NOPAR 
0530        LDB  R40,=2
0540        JSB  =ROMJSB
0550        DEF  DECODE
0560        BYT  320
0570 DCD+   STMD R44,X14,ACTMSU
0580        RTN  
0590 ! --------
0600 NOPAR  BSZ  0
0610        LDMD R44,X14,DEFMSU
0620        JMP  DCD+  
0630 ! -----------------------
0640 TCAT   BSZ  0
0650        JSB  =TCAT. 
0660 CATDON RTN  
0670 ! -----------------------
0680 ! !!===================!!
0690        BYT  241
0700 CAT.   BSZ  0
0710        CLB  R40
0712        BIN  
0714        LDM  R30,R6
0720        DCM  R30
0722        DCM  R30
0724 !    RA now OK for erro
0726        LDM  R76,=ROMRTN
0728        PUMD R76,+R30
0730        STMD R30,=SAVER6
0732        LDM  R30,=GINTEN
0734        STMD R30,=TINTEN
0735        LDMD R14,=MSBASE
0736        CLB  R30
0738        STBD R30,=SCRTYP
0740        LDMD R0,=BINTAB
0750        JSB  X0,GETMSU
0760        LDBD R44,X14,ACTMSU
0770        JZR  TCAT  
0780 !       --
0790 !       MSROM initialize
0800 !       and MSUS decode
0810 !       tape vectored awa
0820 !       now get catalo
0830 ! DO A CATALOG OF DISC AD
0840 !  IN R45,46,4
0850 !       print volume labe
0860        JSB  =ROMJSB
0870        DEF  GETDIR
0880        BYT  320
0890        LDM  R26,R14
0900        LDM  R50,=76D
0910        ASC  "IFVOL: "
0920        PUMD R50,+R26
0930        LDMD R42,X14,SPECIF
0940 SPECIF DAD  70
0950        PUMD R42,+R26
0960        LDB  R42,=15          !  CR
0970        PUBD R42,+R26
0980 !       -----
0990 !       vol head and labe
1000 !       in buffer,  dum
1010        LDM  R36,=15D,0
1020        LDMD R0,=BINTAB
1030        JSB  X0,DRIVER
1040 !       -------
1050 !       vol head gone
1060 !       now dump cat hea
1070 ! 
1080 !       move cat head t
1090 !       MSROM ra
1100        LDMD R24,=BINTAB
1110        ADM  R24,=CATHED
1120        LDMD R26,=MSBASE
1130        LDM  R22,=31D,0
1140        JSB  =MOVUP 
1150 !       print the cathea
1160        LDMD R0,=BINTAB
1170        JSB  X0,DRIVE-
1180 !       restore R3
1190        LDM  R36,=RECBUF
1200 !  ----------------
1210 !   start of cat entr
1220 !   print loo
1230 CATLOP BSZ  0
1240        LDMD R26,=SVCWRD
1250        JOD  CATcom
1260        LDMD R26,=MSBASE
1270 !       print type, bytes
1280 !       logrec, #logrec
1290        LDMD R0,=BINTAB
1300        CLB  R77
1310        STBD R77,X0,ASCFLG
1320 !       ascii flag cleare
1330        JSB  X0,GETTYP
1340        LDBD R77,X0,ODDFLG
1350        JNZ  NameP 
1360        CLM  R56
1370        LDB  R56,R30
1380 !       type is in R56 no
1390        CMB  R56,=377
1400 !       last file?
1410        JZR  CATcom
1420 ! 
1430        LDMD R43,=BLANKS
1440        STM  R43,R63
1450        TSB  R56
1460 !       got blanks for nul
1470 !       file name, c
1480 !       secure
1490        JOD  BLDUN 
1500        JZR  NULL  
1510 NameP  LDMD R43,R36
1520 !       get the nam
1530        LDMD R63,X36,SEC1/2
1540 !       get second half na
1550        JMP  BLDUN 
1560 CATcom RTN  
1570 ! ================
1580 ! ===HELPER=======
1590 CATLO- JMP  CATLOP
1600 ! ===END HELP=====
1610 ! ================
1620 !  ------------
1630 NULL   BSZ  0
1640        LDB  R50,=100
1650        ORB  R56,R50
1660 !       set null bit fo
1670 !       type chec
1680 !       -----------
1690 BLDUN  BSZ  0
1700 !       name to prtbu
1710        PUMD R43,+R26
1720        PUMD R63,+R26
1730        LDBD R77,X0,ODDFLG
1740        JZR  NOTODD
1750        LDMD R30,X36,D.FTYP
1753        DCM  R26
1754        LDB  R36,R31
1755        LDB  R37,R30
1760        JSB  =CATCO-
1765        ADM  R26,=7,0
1770        LDM  R36,=RECBUF
1780        JMP  ODDDON
1790 ! ----------
1800 CATL-- JMP  CATLO-
1810 ! ----------
1820 NOTODD LDMD R42,=BLANKS
1830        LRB  R56
1840        LRB  R56
1850 !       shift file typ
1860        JEV  NOTEXT
1870        LDM  R56,=0,1
1880        STMD R56,X36,D.B/RC
1890        CLM  R56
1900        LDMD R0,=BINTAB
1910        LDBD R77,X0,ASCFLG
1920        CMB  R77,=1
1930        JNZ  NOASC 
1940        LDB  R56,=34
1950 NOASC  BSZ  0
1960 !       set catalog "****
1970 !       ----------
1980 NOTEXT BSZ  0
1990        JLN  DNSHFT
2000        LRB  R56
2010        LLB  R56
2020        LLB  R56
2030        JLZ  DNSHFT
2040        LDB  R56,=14
2050 !       ---------------
2060 DNSHFT BSZ  0
2070 !       get ASCII type nam
2080 !       from type tabl
2090        ADMD R56,=BINTAB
2100 !       R56 has type offse
2110 !       add ram base to i
2120 !       and get ASCII typ
2130        LDMD R44,X56,CATTAB
2140        CMM  R44,=116,125,114,114
2150        JZR  SKIP1 
2160        PUMD R42,+R26
2170 ODDDON PUMD R36,+R6
2180        LDMD R36,X36,D.B/RC
2190        JSB  =CATCO-
2200 !       convert num->ASCI
2210        POMD R36,-R6
2220        JSB  =ROMJSB
2230        DEF  LOGREC
2240        BYT  320
2250 !       compute logica
2260 !       record numbe
2270        LDM  R26,R30
2280        JSB  =CATCO-
2290 !       convert NUM->ASCI
2300        LDMD R0,=BINTAB
2310        JSB  X0,DRIVE-
2320 !       ----------
2330 !       get next entr
2340 SKIP1  JSB  =ROMJSB
2350        DEF  NXTENT
2360        BYT  320
2370        JEZ  CATL--
2380 !       ---------
2390        RTN  
2400 ! ____________________
2410 GETTYP BSZ  0
2420        CLB  R77
2430        STBD R77,X0,ODDFLG
2440 !    Convert two byt
2450 !  interchange disc typ
2460 !  to one byt
2470        LDMD R30,X36,D.FTYP
2480        STB  R31,R77
2490        LDB  R31,R30
2500        LDB  R30,R77
2510 !       bytes swappe
2520        TSM  R30
2530        JZR  GETLST
2540        CMM  R30,=377,377
2550        JZR  GETLST
2560        CMM  R30,=1,0
2570        JNZ  GETCAP
2580        LDB  R30,=4
2590        LDMD R0,=BINTAB
2600        LDB  R77,=1
2610        STBD R77,X0,ASCFLG
2620 GETLST TSB  R#
2630        RTN  
2640 !       --------
2650 GETCAP ADM  R30,=CVDOFF
2660 CVDOFF DAD  20000
2670        TSM  R30
2680        JNG  ALIEN 
2690        CMM  R30,=377,3
2700        JNG  OURS  
2710 ALIEN  BSZ  0
2720        LDMD R0,=BINTAB
2730        LDB  R77,=1
2740        STBD R77,X0,ODDFLG
2750 OURS   RTN  
2760 ! --------------------
2770 ! ====================
2780 ! --------------------
2790 CATHED ASC  "Name        Type  Bytes   Recs"
2800        BYT  15
2810 !           15 = <CR
2820 ! --------------------
2830 !  here is the ASCII typ
2840 !  tabl
2850 CATTAB BSZ  0
2860        ASC  "****"
2870        ASC  "BPGM"
2880        ASC  "DATA"
2890        ASC  "PROG"
2900        ASC  "NULL"
2910        ASC  "GRAF"
2920        ASC  "ASSM"
2930        ASC  "asci"
2940        ASC  "????"
2950 ! -------------------
2960 ASCFLG BYT  0
2970 ODDFLG BYT  0
2980 ! --------------
2990 MSCAT. DAD  61411
3000 TOS    DAD  101132
3020 TCAT.  DAD  25305
3030 ACTMSU DAD  135
3040 DEFMSU DAD  40
3050 DECODE DAD  70501
3060 GETDIR DAD  63346
3070 DISP.  DAD  70046
3080 DRV12. DAD  5462
3120 SCTEMP DAD  101110
3140 MOVUP  DAD  37365
3160 SVCWRD DAD  100151
3170 BLANKS DAD  26536
3180 SEC1/2 DAD  5
3190 D.B/RC DAD  36
3200 CATCO- DAD  25616
3210 LOGREC DAD  62031
3220 NXTENT DAD  63450
3230 D.FTYP DAD  12
3240 ! -------------
3250        FIN  
