10 !***************************
20 !* RECT/POLAR CONVERSIONS  *
30 !*     ROM VERSION         *
40 !* (c) Hewlett-Packard Co. *
50 !*          1980           *
60 !***************************
70        ABS ROM 60000
80        BYT 100
90        BYT 277
100        DEF RUNTIM
110        DEF ASCIIS
120        DEF PARSE 
130        DEF ERMSG 
140        DEF INIT  
150 !**********************************************************************
160 PARSE  BYT 0,0
170        DEF RTPP  
180        DEF RTPP  
190        DEF UNLODP
200 RUNTIM BYT 0,0
210        DEF RTP.  
220        DEF PTR.  
230        DEF SCRB. 
240        DEF REV.  
250 !*********************************************************************
260 ASCIIS ASP "POLAR"
270        ASP "RECTANGULAR"
280        ASP "SCRATCHBIN"
290        ASP "REV DATE"
300        BYT 377
310 !*********************************************************************
320 UNLODP LDM R46,=370,100
330        PUMD R46,+R12
340        PUMD R43,+R12
350        JSB =ROMJSB
360        DEF SCAN  
370        BYT 0
380        RTN 
390 !*********************************************************************
400 RTPP   PUBD R43,+R6
410        JSB =ROMJSB
420        DEF SCAN  
430        BYT 0
440        JSB =ROMJSB
450        DEF REFNUM
460        BYT 0
470        JEZ ERR   
480        JSB =ROMJSB
490        DEF GETCMA
500        BYT 0
510        JSB =ROMJSB
520        DEF REFNUM
530        BYT 0
540        JEZ ERR   
550        JSB =ROMJSB
560        DEF GETCMA
570        BYT 0
580        JSB =ROMJSB
590        DEF NUMVAL
600        BYT 0
610        JEZ ERR   
620        JSB =ROMJSB
630        DEF GETCMA
640        BYT 0
650        JSB =ROMJSB
660        DEF NUMVAL
670        BYT 0
680        JEZ ERR   
690        POBD R47,-R6
700        LDB R46,=100
710        LDB R45,=371
720        PUMD R45,+R12
730        JMP GTOROM
740 !*********************************************************************
750 ERR    POBD R47,-R6
760        JSB =ERROR 
770        BYT 81D
780 GTOROM GTO ROMRTN
790 !*********************************************************************
800 ERMSG  BSZ 0
810        BYT 377
820 !*********************************************************************
830 INIT   BSZ 0
840        BIN 
850        LDBD R34,=ROMFL 
860        JNZ INIRTN
870        LDMD R34,=FWUSER
880        STMD R34,=UNBAS1
890        ADM R34,=20,0
900        STMD R34,=FWUSER
910        JSB =ROMJSB
920        DEF SCRAT+
930        BYT 0
940 INIRTN RTN 
950 !*********************************************************************
960 XVAL   EQU 0
970 RVAL   EQU 0
980 YVAL   EQU 10
990 AVAL   EQU 10
1000 !*********************************************************************
1010        BYT 241
1020 RTP.   JSB =ONER  
1030        LDMD R22,=UNBAS1
1040        STMD R40,X22,YVAL  
1050        JSB =ONER  
1060        STMD R40,X22,XVAL  
1070        PUMD R40,+R12
1080        PUMD R40,+R12
1090        JSB =MPYROI
1100        LDMD R40,X22,YVAL  
1110        PUMD R40,+R12
1120        PUMD R40,+R12
1130        JSB =MPYROI
1140        JSB =ADDROI
1150        JSB =SQR5  
1160        POMD R40,-R12
1170        PUMD R40,+R6
1180        LDMD R40,X22,YVAL  
1190        PUMD R40,+R12
1200        LDMD R40,X22,XVAL  
1210        PUMD R40,+R12
1220        JSB =ATN2. 
1230        JSB =STOSV 
1240        POMD R40,-R6
1250        PUMD R40,+R12
1260        JSB =STOSV 
1270        RTN 
1280 !*********************************************************************
1290        BYT 241
1300 PTR.   JSB =ONER  
1310        LDMD R22,=UNBAS1
1320        STMD R40,X22,AVAL  
1330        JSB =ONER  
1340        STMD R40,X22,RVAL  
1350        LDMD R40,X22,AVAL  
1360        PUMD R40,+R12
1370        JSB =COS10 
1380        LDMD R22,=UNBAS1
1390        LDMD R40,X22,RVAL  
1400        PUMD R40,+R12
1410        JSB =MPYROI
1420        POMD R40,-R12
1430        PUMD R40,+R6
1440        LDMD R40,X22,AVAL  
1450        PUMD R40,+R12
1460        JSB =SIN10 
1470        LDMD R22,=UNBAS1
1480        LDMD R50,X22,RVAL  
1490        PUMD R50,+R12
1500        JSB =MPYROI
1510        JSB =STOSV 
1520        POMD R40,-R6
1530        PUMD R40,+R12
1540        JSB =STOSV 
1550        RTN 
1560 !*********************************************************************
1570        BYT 241
1580 SCRB.  STBD R#,=GINTDS
1590        LDMD R24,=UNBAS1
1600        DCM R24
1610        LDMD R26,=LWAMEM
1620        STM R26,R22
1630        SBM R22,R24
1640        LDB R20,=4
1650        LDM R32,=LAVAIL
1660 UNLD1  LDMD R36,R32
1670        ADM R36,R22
1680        PUMD R36,+R32
1690        DCB R20
1700        JNZ UNLD1 
1710        LDMD R36,R32
1720        CMMD R36,=LWAMEM
1730        JZR UNLD2 
1740        ADM R36,R22
1750        STMD R36,R32
1760 UNLD2  CLM R#
1770        STMD R#,=BINTAB
1780        JSB =MOVDN 
1790        STBD R#,=GINTEN
1800        RTN 
1810 !*********************************************************************
1820        BYT 0,56
1830 REV.   LDM R44,=8D,0
1840        DEF DATE  
1850        PUMD R44,+R12
1860        RTN 
1870 DATE   ASC "05/05/80"
1880 !*********************************************************************
1890 COS10  DAD 53556
1900 MPYROI DAD 52722
1910 ADDROI DAD 52150
1920 SIN10  DAD 53546
1930 SQR5   DAD 52442
1940 ATN2.  DAD 76455
1950 ONER   DAD 56215
1960 ERROR  DAD 06615
1970 NUMVAL DAD 12412
1980 GETCMA DAD 13414
1990 REFNUM DAD 17025
2000 SCAN   DAD 11262
2010 STOSV  DAD 45254
2020 BINTAB DAD 101233
2030 GINTDS DAD 177401
2040 LWAMEM DAD 100022
2050 LAVAIL DAD 100010
2060 MOVDN  DAD 37324
2070 GINTEN DAD 177400
2080 ROMJSB DAD 4776
2090 FWUSER DAD 100000
2100 UNBAS1 DAD 102554
2110 ROMRTN DAD 4762
2120 SCRAT+ DAD 4344
2130 ROMFL  DAD 101231
2140        FIN 
