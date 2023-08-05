1 !****************************
2 !*     GCURS BINARY         *
3 !* (c) Hewlett-Packard Co.  *
4 !*          1980            *
5 !****************************
10        NAM GCURS 
20        DEF RUNTIM
30        DEF TOKS  
40        DEF PARSES
50        DEF ERMSG 
60        DEF INIT  
70 RUNTIM BSZ 2
80        DEF GCOFF.
90        DEF GCURX.
100        DEF GCURY.
110        DEF GCURS.
120        DEF REV.  
130 PARSES BSZ 2
140        DEF GCOFFP
150        BSZ 2
160        BSZ 2
170        DEF GCPAR 
180 ERMSG  BYT 377,377
190 TOKS   ASP "GCURSOR OFF"
200        ASP "GCURSOR X"
210        ASP "GCURSOR Y"
220        ASP "GCURSOR"
230        ASP "REV DATE"
240        BYT 377
250 !*******************************************************************
260 INIT   BIN 
280        LDBD R34,=ROMFL 
290        CMB R34,=2
300        JNZ LOAD? 
310 SCRAT! LDM R44,=236,236,236, 236
320        STMD R44,=CHIDLE
330        RTN 
340 LOAD?  CMB R#,=5
350        JZR SCRAT!
360 RTN    RTN 
370 !*******************************************************************
380 LEFT   LDMD R40,X14,STEP  
390        JMP COMLEF
400 RIGHT  LDMD R40,X14,STEP  
410        JMP COMRIT
420 KEY    LDMD R14,=BINTAB
430        BIN 
440        CMB R16,=2
450        JNZ RTN   
460        LDMD R22,=KEYHIT
470        CMB R22,=211
480        JZR FRIGHT
490        CMB R22,=223
500        JZR FLEFT 
510        CMB R22,=245
520        JZR FUP   
530        CMB R22,=242
540        JZR DOWN  
550        CMB R22,=234
560        JZR LEFT  
570        CMB R22,=235
580        JZR RIGHT 
590        CMB R22,=241
600        JZR UP    
610        CMB R22,=254
620        JZR FDOWN 
630        RTN 
640 DOWN   LDMD R40,X14,STEP  
650        JMP COMDOW
660 UP     LDMD R40,X14,STEP  
670        JMP COMUP 
680 FRIGHT LDMD R40,X14,FSTEP 
690 COMRIT PUMD R#,+R12
700        LDMD R50,X14,CURS-X
710        PUMD R50,+R12
720        JSB =ADDROI
730 COM-X  LDMD R40,X14,CURS-Y
740        PUMD R40,+R12
750        JMP COMKEY
760 FLEFT  LDMD R40,X14,FSTEP 
770 COMLEF LDMD R50,X14,CURS-X
780        PUMD R50,+R12
790        PUMD R40,+R12
800        JSB =SUBROI
810        JMP COM-X 
820 FUP    LDMD R40,X14,FSTEP 
830 COMUP  LDMD R50,X14,CURS-X
840        PUMD R50,+R12
850        PUMD R40,+R12
860        LDMD R40,X14,CURS-Y
870        PUMD R40,+R12
880        JSB =ADDROI
890        JMP COMKEY
900 FDOWN  LDMD R40,X14,FSTEP 
910 COMDOW LDMD R50,X14,CURS-X
920        PUMD R50,+R12
930        LDMD R50,X14,CURS-Y
940        PUMD R50,+R12
950        PUMD R40,+R12
960        JSB =SUBROI
970 COMKEY JSB X14,PLOT  
980        CLM R50
990        POMD R40,-R12
1000        PUMD R40,+R12
1010        JSB =COMFLT
1020        POMD R40,-R12
1030        JEN TEST-X
1040        PUMD R40,+R12
1050        LDM R50,=2,0,0,0,0,0,20C,19C
1060        JSB =COMFLT
1070        POMD R40,-R12
1080        JEZ TEST-X
1090        STMD R40,X14,CURS-Y
1100 TEST-X CLM R50
1110        POMD R40,-R12
1120        PUMD R40,+R12
1130        JSB =COMFLT
1140        POMD R40,-R12
1150        JEN MOVCUR
1160        PUMD R40,+R12
1170        LDM R50,=2,0,0,0,0,0,60C,25C
1180        JSB =COMFLT
1190        BIN 
1200        POMD R40,-R12
1210        JEZ MOVCUR
1220        STMD R40,X14,CURS-X
1230 MOVCUR JSB X14,PLOT  
1240        CLE 
1250        JSB =EOJ2  
1260        LDBD R31,X14,KEYCON
1270 LOOPKE LDBD R30,=KEYSTS
1280        LRB R30
1290        JEV EOJ   
1300        LDBD R30,=CRTSTS
1310        LRB R30
1320        JEV LOOPKE
1330 LOOPK2 LDBD R30,=KEYSTS
1340        LRB R30
1350        JEV EOJ   
1360        LDBD R30,=SVCWRD
1370        JOD EOJ   
1380        LDBD R30,=CRTSTS
1390        LRB R30
1400        JOD LOOPK2
1410        DCB R31
1420        JNZ LOOPKE
1430        LDB R31,=KYRPT2
1440        STBD R31,X14,KEYCON
1450        LDM R20,=KEY   
1460        ADM R20,R14
1470        DCM R20
1480        LDM R4,R20
1490 EOJ    LDB R31,=KYRPT1
1500        STBD R31,X14,KEYCON
1510        POMD R44,-R6
1520        CLE 
1530        RTN 
1540 !******************************************************************
1550 GCPAR  PUBD R43,+R6
1560        JSB =NUMVA+
1570        JEN OK    
1580 ERR    JSB =ERROR+
1590        BYT 81D
1600 OK     JSB =GETCMA
1610        JSB =NUMVAL
1620        JEZ ERR   
1630        CMB R14,=54
1640        JNZ DONE  
1650        JSB =NUMVA+
1660        JEZ ERR   
1670        JSB =GETCMA
1680        JSB =NUMVAL
1690        JEZ ERR   
1700 DONE   POBD R47,-R6
1710        LDB R45,=371
1720        PUMD R45,+R12
1730        RTN 
1740 GCOFFP PUBD R43,+R6
1750        JSB =SCAN  
1760        JMP DONE  
1770 !******************************************************************
1780        BYT 241
1790 GCOFF. LDMD R14,=BINTAB
1800        JSB X14,SCRAT!
1810        JSB X14,PLOT  
1820        RTN 
1830 !******************************************************************
1840        BYT 0,55
1850 GCURX. LDMD R14,=BINTAB
1860        LDMD R50,X14,CURS-X
1870 GPUSH  PUMD R50,+R12
1880        RTN 
1890 !******************************************************************
1900        BYT 0,55
1910 GCURY. LDMD R14,=BINTAB
1920        LDMD R50,X14,CURS-Y
1930        JMP GPUSH 
1940 !******************************************************************
1950        BYT 241
1960 GCURS. BIN 
1970        LDMD R14,=BINTAB
1980        LDM R40,=0,0,0,0,0,0,0,10C
1990        STMD R40,X14,STEP  
2000        LDB R47,=40C
2010        STMD R40,X14,FSTEP 
2020        LDM R20,R12
2030        SBM R20,=40,0
2040        CMMD R20,=TOS   
2050        JNZ NOSTEP
2060        JSB =ONER  
2070        BIN 
2080        STMD R#,X14,FSTEP 
2090        JSB =ONER  
2100        BIN 
2110        STMD R#,X14,STEP  
2120 NOSTEP JSB =ONER  
2130        BIN 
2140        STMD R#,X14,CURS-Y
2150        JSB =ONER  
2160        BIN 
2170        STMD R#,X14,CURS-X
2180        JSB X14,PLOT  
2190        LDM R46,=KEY   
2200        ADM R46,R14
2210        STM R46,R45
2220        LDB R47,=236
2230        LDB R44,=316
2240        STMD R44,=CHIDLE
2250        RTN 
2260 !******************************************************************
2270 PLOT   JSB X14,GCURX.
2280        JSB X14,GCURY.
2290        LDM R20,=ROMTAB
2300 NXTROM POMD R24,+R20
2310        CMB R24,=377
2320        JZR SYSTEM
2330        CMB R24,=PPROM#
2340        JNZ NXTROM
2350        JSB =ROMJSB
2360        DEF PMOVE.
2370        VAL PPROM#
2380        LDMD R14,=BINTAB
2390        JMP PLOT++
2400 SYSTEM JSB =MOVE. 
2410 PLOT++ LDM R20,=CURSES
2420        ADM R20,R14
2430        LDBD R22,=XMAP  
2440        ANM R22,=3,0
2450        LDM R34,R22
2460        LLM R34
2470        LLM R34
2480        ADM R34,R22
2490        ADM R34,R20
2500        LDM R22,=5,0
2510        LDM R44,=1,0,1,0
2520        JSB =BPLOT+
2530        RTN 
2540 !******************************************************************
2550 CURSES BYT 360,300,240,220,10
2560        BYT 170,140,120,110,4
2570        BYT 74,60,50,44,2
2580        BYT 36,30,24,22,1
2590 KEYCON BSZ 1
2600 CURS-X BSZ 10
2610 CURS-Y BSZ 10
2620 FSTEP  BSZ 10
2630 STEP   BSZ 10
2640 !******************************************************************
2650        BYT 0,56
2660 REV.   BIN 
2670        LDM R44,=11D,0
2680        DEF DATE  
2690        ADMD R46,=BINTAB
2700        PUMD R44,+R12
2710        RTN 
2720 DATE   ASC "AUG 14,1980"
2730 BPLOT+ DAD 34405
2740 MOVE.  DAD 31703
2750 PMOVE. DAD 64400
2760 ROMJSB DAD 4776
2770 PPROM# EQU 360
2780 ROMTAB DAD 101235
2790 KYRPT2 EQU 1
2800 KYRPT1 EQU 30
2810 CRTSTS DAD 177406
2820 KEYSTS DAD 177402
2830 CHIDLE DAD 102416
2840 ROMFL  DAD 101231
2850 KEYHIT DAD 100671
2860 EOJ2   DAD 34772
2870 ADDROI DAD 52150
2880 SUBROI DAD 52127
2890 BINTAB DAD 101233
2900 NUMVAL DAD 12412
2910 NUMVA+ DAD 12407
2920 SCAN   DAD 11262
2930 GETCMA DAD 13414
2940 SVCWRD DAD 100151
2950 TOS    DAD 101132
2960 ERROR+ DAD 6611
2970 ONER   DAD 56215
2980 XMAP   DAD 100262
2990 COMFLT DAD 32621
3000        FIN 
