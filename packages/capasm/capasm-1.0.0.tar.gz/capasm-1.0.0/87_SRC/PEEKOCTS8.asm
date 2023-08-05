00010          NAM  33,PEEK    
00020          DEF  RUNTIM  
00030          DEF  TOKS    
00040          DEF  PARSE   
00050          DEF  ERMSG   
00060          DEF  INIT    
00070 RUNTIM   BSZ  2
00080          DEF  POKE.   
00090          DEF  PEEK.   
00100          DEF  INVERT. 
00110 PARSE    BSZ  2
00120          DEF  POKPAR  
00130          BYT  0,0
00140          DEF  INVPAR  
00150 ERMSG    BYT  377,377
00160 TOKS     ASP  "POKE"
00170          ASP  "PEEK"
00180          ASP  "INVERT"
00190          BYT  377
00200 INIT     RTN  
00210 ! *******************************************************************
00220 POKPAR   PUBD R43,+R6
00230          JSB  =NUMVA+  
00240          JEN  OK      
00250 ERR      POBD R43,-R6
00260          JSB  =ERROR+  
00270          BYT  88D
00280 OK       CMB  R14,=54
00290          JNZ  ERR     
00300          JSB  =NUMVA+  
00310          JEZ  ERR     
00320          LDM  R56,=33,371
00330          POBD R55,-R6
00340          STMI R55,=PTR2-   
00350          RTN  
00360 ! *******************************************************************
00370 INVPAR   LDM  R56,=33,371
00380          LDB  R55,R43
00390          STMI R55,=PTR2-   
00400          JSB  =SCAN    
00410          RTN  
00420 ! *******************************************************************
00430          BYT  241
00440 POKE.    JSB  =ONEB            ! 12155
00450          PUBD R46,+R6
00460          JSB  =ONEX            ! 56700
00470          POBD R40,-R6
00480          STBD R40,R46
00490          RTN  
00500 ! ******************************************************************
00510          BYT  20,55
00520 PEEK.    JSB  =ONEX    
00530          CLM  R36
00540          LDBD R36,R46
00550          JSB  =CONBIN  
00560          PUMD R40,+R12
00570          RTN  
00580 ! *****************************************************************
00590          BYT  241
00600 INVERT.  LDBD R40,=CRTSTS  
00610          LDB  R37,=40
00620          XRB  R37,R40
00630          ANM  R37,=376
00640          STBD R37,=CRTSTS  
00650          RTN  
00660 ! *****************************************************************
00670 CONBIN   DAD  4401
00680 CRTSTS   DAD  177702
00690 ERROR+   DAD  10220
00700 NUMVA+   DAD  22403
00710 ONEB     DAD  12153
00720 ONEX     DAD  56673
00730 PTR2-    DAD  177715
00740 SCAN     DAD  21110
00750          FIN  
