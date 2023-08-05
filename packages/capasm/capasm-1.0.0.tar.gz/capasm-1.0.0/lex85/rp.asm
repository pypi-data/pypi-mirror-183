1 !****************************
2 !* RECT/POLAR CONVERSIONS   *
3 !* (c) Hewlett-Packard Co.  *
4 !*          1980            *
5 !****************************
10        NAM R&P   
20        DEF RUNTIM
30        DEF ASCIIS
40        DEF PARSE 
50        DEF ERMSG 
60        DEF INIT  
70 !**********************************************************************
80 PARSE  BYT 0,0
90        DEF RTPP  
100        DEF RTPP  
110        DEF UNLODP
120 RUNTIM BYT 0,0
130        DEF RTP.  
140        DEF PTR.  
150        DEF SCRB. 
160        DEF REV.  
170        BYT 377,377
180 !*********************************************************************
190 ASCIIS ASP "POLAR"
200        ASP "RECTANGULAR"
210        ASP "SCRATCHBIN"
220        ASP "REV DATE"
230        BYT 377
240 !*********************************************************************
250 UNLODP LDB R47,R43
260        LDB R45,=371
270        PUMD R45,+R12
280        JSB =SCAN  
290        RTN 
300 !*********************************************************************
310 RTPP   PUBD R43,+R6
320        JSB =SCAN  
330        JSB =REFNUM
340        JEZ ERR   
350        JSB =GETCMA
360        JSB =REFNUM
370        JEZ ERR   
380        JSB =GETCMA
390        JSB =NUMVAL
400        JEZ ERR   
410        JSB =GETCMA
420        JSB =NUMVAL
430        JEZ ERR   
440        POBD R47,-R6
450        LDB R45,=371
460        PUMD R45,+R12
470        RTN 
480 !*********************************************************************
490 ERR    POBD R47,-R6
500        JSB =ERROR+
510        BYT 81D
520 !*********************************************************************
530 ERMSG  BSZ 0
540        BYT 377
550 !*********************************************************************
560 INIT   BSZ 0
570        RTN 
580 !*********************************************************************
590 XVAL   BSZ 0
600 RVAL   BSZ 10
610 YVAL   BSZ 0
620 AVAL   BSZ 10
630 !*********************************************************************
640        BYT 241
650 RTP.   JSB =ONER  
660        LDMD R22,=BINTAB
670        STMD R40,X22,YVAL  
680        JSB =ONER  
690        STMD R40,X22,XVAL  
700        PUMD R40,+R12
710        PUMD R40,+R12
720        JSB =MPYROI
730        LDMD R40,X22,YVAL  
740        PUMD R40,+R12
750        PUMD R40,+R12
760        JSB =MPYROI
770        JSB =ADDROI
780        JSB =SQR5  
790        POMD R40,-R12
800        PUMD R40,+R6
810        LDMD R40,X22,YVAL  
820        PUMD R40,+R12
830        LDMD R40,X22,XVAL  
840        PUMD R40,+R12
850        JSB =ATN2. 
860        JSB =STOSV 
870        POMD R40,-R6
880        PUMD R40,+R12
890        JSB =STOSV 
900        RTN 
910 !*********************************************************************
920        BYT 241
930 PTR.   JSB =ONER  
940        LDMD R22,=BINTAB
950        STMD R40,X22,AVAL  
960        JSB =ONER  
970        STMD R40,X22,RVAL  
980        LDMD R40,X22,AVAL  
990        PUMD R40,+R12
1000        JSB =COS10 
1010        LDMD R22,=BINTAB
1020        LDMD R40,X22,RVAL  
1030        PUMD R40,+R12
1040        JSB =MPYROI
1050        POMD R40,-R12
1060        PUMD R40,+R6
1070        LDMD R40,X22,AVAL  
1080        PUMD R40,+R12
1090        JSB =SIN10 
1100        LDMD R22,=BINTAB
1110        LDMD R50,X22,RVAL  
1120        PUMD R50,+R12
1130        JSB =MPYROI
1140        JSB =STOSV 
1150        POMD R40,-R6
1160        PUMD R40,+R12
1170        JSB =STOSV 
1180        RTN 
1190 !*********************************************************************
1200        BYT 241
1210 SCRB.  STBD R#,=GINTDS
1220        LDMD R24,=BINTAB
1230        DCM R24
1240        LDMD R26,=LWAMEM
1250        STM R26,R22
1260        SBM R22,R24
1270        LDB R20,=4
1280        LDM R32,=LAVAIL
1290 UNLD1  LDMD R36,R32
1300        ADM R36,R22
1310        PUMD R36,+R32
1320        DCB R20
1330        JNZ UNLD1 
1340        LDMD R36,R32
1350        CMMD R36,=LWAMEM
1360        JZR UNLD2 
1370        ADM R36,R22
1380        STMD R36,R32
1390 UNLD2  CLM R#
1400        STMD R#,=BINTAB
1410        LDM R#,R12
1420        LDM R41,=316
1430        DEF MOVDN 
1440        STBD R#,=GINTEN
1450        RTN 
1460        STMD R41,R36
1470        DCM R36
1480        LDM R4,R36
1490 !*********************************************************************
1500        BYT 0,56
1510 REV.   LDM R44,=8D,0
1520        DEF DATE  
1530        ADMD R46,=BINTAB
1540        PUMD R44,+R12
1550        RTN 
1560 DATE   ASC "05/05/80"
1570 !*********************************************************************
1580 COS10  DAD 53556
1590 MPYROI DAD 52722
1600 ADDROI DAD 52150
1610 SIN10  DAD 53546
1620 SQR5   DAD 52442
1630 ATN2.  DAD 76455
1640 ONER   DAD 56215
1650 ERROR+ DAD 06611
1660 NUMVAL DAD 12412
1670 GETCMA DAD 13414
1680 REFNUM DAD 17025
1690 SCAN   DAD 11262
1700 STOSV  DAD 45254
1710 BINTAB DAD 101233
1720 GINTDS DAD 177401
1730 LWAMEM DAD 100022
1740 LAVAIL DAD 100010
1750 MOVDN  DAD 37324
1760 GINTEN DAD 177400
1770        FIN 
