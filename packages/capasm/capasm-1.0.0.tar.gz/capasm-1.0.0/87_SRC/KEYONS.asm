00010          NAM  23,KEYON   
00020          DEF  RUNTIM  
00030          DEF  ASCIIS  
00040          DEF  PARSE   
00050          DEF  ERMSG   
00060 RUNTIM   DEF  INIT    
00070          DEF  KEYON.  
00080          DEF  KEYOF.  
00090 PARSE    DEF  REV.    
00100          DEF  KONPRS  
00110          DEF  KOFPRS  
00120          BYT  377,377
00130 ! *************************
00140 ASCIIS   ASP  "KEY ON"
00150          ASP  "KEY OFF"
00160 !        ASP  ""
00165          BYT  10,220
00170          BYT  377
00180 ! *************************
00190 ERMSG    BYT  200
00200          BYT  200,200,200,200
00210          BYT  200,200,200,200
00220          ASP  "BAD 'KEY ON' FORMAT"
00230          ASP  "SYSTEM HOOK IN USE"
00240          BYT  377
00250 INIT     BIN  
00260          LDMD R22,=BINTAB  
00270          LDBD R36,=ROMFL   
00280          DCB  R36
00290          JNZ  SCRAT?  
00300 RESET    LDBD R46,=CHIDLE  
00310          CMB  R46,=236
00320          JZR  RSET    
00321          LDBD R46,=ERRORS  
00322          JNZ  INIRTN  
00323          LDB  R46,=23
00324          STBD R46,=ERRBP#  
00330          JSB  =ERROR+  
00340          BYT  365
00350 RSET     LDM  R24,=KEYCHK  
00360          ADM  R24,R22
00370          STM  R24,R45
00380          LDB  R47,=236
00390          LDB  R44,=316
00400          STMD R44,=CHIDLE  
00410          JMP  RUNIN   
00420 SCRAT?   DCB  R#
00430          JNZ  LODBIN  
00440 SCRAT    LDM  R44,=236
00450          RTN  
00460          RTN  
00470          RTN  
00480          STMD R44,=CHIDLE  
00490 INIRTN   RTN  
00500 LODBIN   DCB  R#
00510          JZR  RESET   
00520          DCB  R#
00530 RUNINI   JNZ  LOAD    
00540 RUNIN    JSB  X22,OFF     
00550          RTN  
00560 LOAD     DCB  R#
00570          JZR  SCRAT   
00580          DCB  R#
00590          DCB  R#
00600          JZR  RUNIN   
00610          RTN  
00620 ! *************************
00630 KEYCHK   BIN  
00640          TSB  R16
00650          JOD  KOUT+   
00660          JZR  KOUT+   
00670          CMB  R16,=4
00680          JZR  KOUT+   
00690          LDMD R22,=BINTAB  
00700          LDMD R55,X22,KYTAB   
00710          JZR  KOUT+   
00720          LDMD R45,=ONFLAG  
00730          JNZ  KOUT+   
00740          LDBD R32,=KEYHIT  
00750          STB  R32,R34
00760          ANM  R32,=37,0
00770          ADM  R32,R22
00780          LDBD R26,X32,STORE   
00790          CLB  R27
00800          ICB  R27
00810          BCD  
00820          LRB  R34
00830          BIN  
00840          LRB  R34
00850          JZR  DONNE   
00860 TEST     LLB  R27
00870          DCB  R34
00880          JNZ  TEST    
00890 DONNE    ANM  R27,R26
00900          JZR  KOUT+   
00910          JSB  =SETTR1  
00920          LDMD R45,=PTR1    
00930          STMD R45,=ONFLAG  
00940          STMD R55,=PTR1    
00950          CLB  R37
00960          LDBD R36,=KEYHIT  
00970          JSB  =CONBIN  
00980          LDMD R55,X22,ADRESS  
00990          PUMD R55,+R12
01000          LDMD R54,X22,NAME    
01010          PUMD R54,+R12
01020          PUMD R40,+R12
01030          JSB  =STOSV   
01040          LDB  R16,=7
01050          JSB  =EOJ2    
01060          POMD R30,-R6
01070          POMD R30,-R6
01080          CLE  
01090 KOUT+    BIN  
01100          RTN  
01110 ! ***********************
01120 KONPRS   PUBD R43,+R6
01130          JSB  =SCAN    
01140          CLE  
01150          JSB  =REFNUM  
01160          CMB  R14,=COMMA   
01170          JNZ  NO-$    
01180          JSB  =STREX+  
01190          JEZ  ERR82   
01200 NO-$     LDM  R56,=23,371
01210          POBD R55,-R6
01220          STMI R55,=PTR2-   
01230          CMB  R47,=210
01240          JNZ  ERR89   
01250          JSB  =GOTOSU  
01260          RTN  
01270 ! ***********************
01280 KOFPRS   PUBD R43,+R6
01290          JSB  =STREX+  
01300          LDM  R56,=23,371
01310          POBD R55,-R6
01320          STMI R55,=PTR2-   
01330          RTN  
01340 ERR82    POBD R57,-R6
01350          JSB  =ERROR+  
01360          BYT  366
01370 ERR89    JSB  =ERROR+  
01380          BYT  131
01390 ! ************************
01400          BYT  241
01410 KEYON.   BIN  
01420          CLM  R26
01430          LDMD R22,=BINTAB  
01440          LDMD R34,=TOS     
01450          ADM  R34,=7,0
01460          SBM  R34,R12
01470          JZR  KYON1   
01480          POMD R45,-R12
01490          STMD R45,=PTR2    
01500          POMD R26,-R12
01510 KYON1    LDMD R55,=PTR1    
01520          STMD R55,X22,KYTAB   
01530          LDMI R74,=PTR1-   
01540          POMD R64,-R12
01550          STMD R64,X22,NAME    
01560          POMD R65,-R12
01570          STMD R65,X22,ADRESS  
01580          TSM  R26
01590          JZR  RRTN    
01600 AGAIN    JSB  X22,POPEE   
01610          ORB  R36,R37
01620          STBD R36,X30,STORE   
01630          DCM  R26
01640          JNZ  AGAIN   
01650 RRTN     RTN  
01660 ! ************************
01670 POPEE    LDBI R30,=PTR2-   
01680          STB  R30,R34
01690          ANM  R30,=37,0
01700          ADM  R30,R22
01710          LDBD R36,X30,STORE   
01720          CLB  R37
01730          ICB  R37
01740          BCD  
01750          LRB  R34
01760          BIN  
01770          LRB  R34
01780          JZR  DUNN    
01790 TST      LLB  R37
01800          DCB  R34
01810          JNZ  TST     
01820 DUNN     RTN  
01830 ! ************************
01840          BYT  241
01850 KEYOF.   BIN  
01860          LDMD R22,=BINTAB  
01870          CMMD R12,=TOS     
01880          JNZ  KYOFF1  
01890 OFF      LDB  R27,=5
01900          CLM  R60
01910 STM      STMD R60,X22,STORE   
01920          ADM  R22,=10,0
01930          DCB  R27
01940          JNZ  STM     
01950          STMD R66,X22,STORE   
01960          RTN  
01970 KYOFF1   POMD R45,-R12
01980          STMD R45,=PTR2    
01990          POMD R26,-R12
02000          JZR  RRTN    
02010 AGIN     JSB  X22,POPEE   
02020          NCB  R37
02030          ANM  R37,R36
02040          STBD R37,X30,STORE   
02050          DCM  R26
02060          JNZ  AGIN    
02070          RTN  
02080 ! ***********************
02090 STORE    BSZ  40
02100 ADRESS   BSZ  3
02110 NAME     BSZ  4
02120 KYTAB    BSZ  3
02130 ! ***********************
02140          BYT  0,56
02150 REV.     LDM  R36,=14,0
02160          BIN  
02170          PUMD R36,+R12
02180          LDMD R36,=BINTAB  
02190          ADM  R36,=DATE    
02200          STM  R36,R45
02210          CLB  R47
02220          PUMD R45,+R12
02230          RTN  
02240          ASC  "1891 ,6 YLUJ"
02250 DATE     BSZ  0
02260 ! ************************
02270 ERROR+   DAD  10220
02275 ERRORS   DAD  100123
02276 ERRBP#   DAD  103371
02280 SCAN     DAD  21110
02290 ROMFL    DAD  104065
02300 CHIDLE   DAD  103670
02310 KEYHIT   DAD  101142
02320 ONFLAG   DAD  100065
02330 EOJ2     DAD  14525
02340 SETTR1   DAD  2633
02350 BINTAB   DAD  104070
02360 STREX+   DAD  23721
02370 CONBIN   DAD  4401
02380 STOSV    DAD  46057
02390 GOTOSU   DAD  30317
02400 COMMA    EQU  54
02410 TOS      DAD  101744
02420 REFNUM   DAD  27530
02430 PTR1     DAD  177710
02440 PTR1-    DAD  177711
02450 PTR2     DAD  177714
02460 PTR2-    DAD  177715
02470          FIN  
