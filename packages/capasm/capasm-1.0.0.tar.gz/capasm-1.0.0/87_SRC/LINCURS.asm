00010          NAM  27,LINCUR  
00020          DEF  RUNTIM  
00030          DEF  ASCIIS  
00040          DEF  PARSE   
00050          DEF  ERMSG   
00060          DEF  INIT    
00070 RUNTIM   BYT  0,0
00080          DEF  RTN.    
00090          DEF  RTN.    
00100          DEF  LINPT.  
00110          DEF  MOVCR.  
00120          DEF  RTN.    
00130          DEF  REV.    
00140          BYT  0,0
00150          DEF  LIN$.   
00160 PARSE    BYT  0,0
00170          DEF  ERR89   
00180          DEF  ERR89   
00190          DEF  LINPRS  
00200          DEF  CURPRS  
00210          DEF  ERR89   
00220          BYT  377,377
00230 ASCIIS   ASP  "***UNUSED***"
00240          ASP  "***UNUSED***"
00250          ASP  "LINPUT"
00260          ASP  "MOVE CURSOR"
00270          ASP  "***UNUSED***"
00280          ASP  ""
00290 ERMSG    BYT  377
00300          BYT  240
00310 ! ********************************************************************
00320 ERR89    JSB  =ERROR+  
00330          BYT  131
00340 ! ********************************************************************
00350 LINPRS   LDM  R55,=3,27,371
00360          STMI R55,=PTR2-   
00370          JSB  =SCAN    
00380          JSB  =STRREF  
00390          JEZ  ERR89   
00400          LDM  R55,=10,27,371
00410          STMI R55,=PTR2-   
00420 INIT     RTN  
00430 ! ********************************************************************
00440          BYT  241
00450 RTN.     RTN  
00460 ! ********************************************************************
00470 CURPRS   JSB  =GET2N   
00480          LDBI R55,=PTR2+   
00490          LDM  R56,=27,371
00500          STMI R55,=PTR2-   
00510          RTN  
00520 ! ********************************************************************
00530          BYT  241
00540 LINPT.   JSB  =INPUT.  
00550          RTN  
00560 ! ********************************************************************
00570          BYT  44
00580 LIN$.    BIN  
00590          LDMD R32,=INPTR   
00600          STM  R32,R14
00610          CLM  R36
00620 CHRCNT   POBD R35,+R32
00630          CMB  R35,=15
00640          JZR  ENDOF$  
00650          ICM  R36
00660          JMP  CHRCNT  
00670 ENDOF$   TSM  R36
00680          JZR  DONE    
00690          POBD R25,-R32
00700 POPBLK   POBD R25,-R32
00710          CMB  R25,=40
00720          JNZ  DONE+   
00730          DCM  R36
00740          JNZ  POPBLK  
00750 DONE+    ICM  R32
00760          STM  R32,R65
00770          CLB  R67
00780 DOLOOP   CMM  R14,R32
00790          JCY  DONE    
00800          LDBD R30,R14
00810          POBD R31,-R32
00820          STBD R30,R32
00830          PUBD R31,+R14
00840          JMP  DOLOOP  
00850 DONE     PUMD R36,+R12
00860          PUMD R65,+R12
00870          JSB  =STOST   
00880          RTN  
00890 ! ********************************************************************
00900          BYT  241
00910 MOVCR.   BIN  
00920          LDBD R30,=CRTSTS  
00930          JPS  GET     
00940          LLB  R30
00950          TSB  R30
00960          JNG  GET     
00970          JSB  =ALPHA.  
00980 GET      JSB  =DECUR2  
00990          JSB  =HMCURS  
01000          JSB  =TWOB    
01010 GET-Y    DCM  R46
01020          JNG  GET-X   
01030          JZR  GET-X   
01040          JSB  =DNCUR.  
01050          JMP  GET-Y   
01060 GET-X    DCM  R56
01070          JNG  DONE1   
01080          JZR  DONE1   
01090          JSB  =RTCUR.  
01100          JMP  GET-X   
01110 DONE1    JSB  =CURS    
01120          RTN  
01130 ! ********************************************************************
01140          BYT  0,56
01150 REV.     LDM  R36,=14,0
01160          BIN  
01170          PUMD R36,+R12
01180          LDMD R36,=BINTAB  
01190          ADM  R36,=DATE    
01200          STM  R36,R45
01210          CLB  R47
01220          PUMD R45,+R12
01230          RTN  
01240          ASC  "1891 ,8 SEPT"
01250 DATE     BSZ  0
01260 ! ********************************************************************
01270 ERROR+   DAD  10220
01280 PTR2-    DAD  177715
01290 PTR2+    DAD  177716
01300 SCAN     DAD  21110
01310 STRREF   DAD  24056
01320 GET2N    DAD  24630
01330 INPUT.   DAD  16314
01340 INPTR    DAD  101143
01350 STOST    DAD  46472
01360 ALPHA.   DAD  12413
01370 DECUR2   DAD  13467
01380 HMCURS   DAD  13661
01390 TWOB     DAD  56760
01400 DNCUR.   DAD  13607
01410 RTCUR.   DAD  13651
01420 CURS     DAD  14030
01430 BINTAB   DAD  104070
01440 CRTSTS   DAD  177702
01445 PTR1     DAD  177710
01450          FIN  
