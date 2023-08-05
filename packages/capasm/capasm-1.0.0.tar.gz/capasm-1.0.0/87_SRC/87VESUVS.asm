01000 ! ASTORE "87VESUVS
01100 ! ASSEMBLE "87VESUV
01200 ! REN 1000,10
01300          NAM  1,VESUV   
01400          DEF  RUNTIM  
01500          DEF  TOKS    
01600          DEF  PARSE   
01700          DEF  ERMSG   
01800          DEF  INIT    
01900 RUNTIM   BYT  0,0
02000          DEF  SETCH.  
02100          DEF  VESUV.  
02200 PARSE    BYT  0,0
02300          DEF  SETPAR  
02400          DEF  VESPAR  
02500          BYT  377,377
02600 TOKS     ASP  "SET CHARS"
02700          ASP  "VESUVIUS"
02800          BYT  377
02900 INIT     RTN  
03000 ERMSG    BYT  200
03100          BYT  200,200,200,200
03200          BYT  200,200,200,200
03300          ASP  "MUST BE ONE DIMENSIONAL ARRAY"
03400          ASP  "MUST BE AN INTEGER ARRAY"
03500          BYT  377
03600 ! ************************
03700 SETPAR   PUBD R43,+R6
03800          JSB  =SCAN    
03900          JSB  =FORMAR  
04000 ERR      POBD R55,-R6
04100          JEN  OK      
04200          JSB  =ERROR+  
04300          BYT  88D
04400 OK       LDM  R56,=1,371
04500          STMI R55,=PTR2-   
04600          RTN  
04700 ! ************************
04800 VESPAR   PUBD R43,+R6
04900          JSB  =SCAN    
05000          JSB  =STRREF  
05100          JEZ  ERR     
05200          CMB  R14,=54
05300          CLE  
05400          JNZ  ERR     
05500          JSB  =STREX+  
05600          JEZ  ERR     
05700          POBD R55,-R6
05800          JMP  OK      
05900 ! ************************
06000          BYT  241
06100 VESUV.   BIN  
06200 ! 
06300 ! 
06400 !  THE R12 STACK WILL HAVE
06500 ! 
06600 !    3 BYTES   ABS ADDDRESS OF NAME OF B
06700 !    1 BYTES   HEADER OF B$ VARIABL
06800 !    2 BYTES   MAX LEN OF STRING VARIABL
06900 !    3 BYTES   ABS ADDRESS OF FIRST BYTE OF STRIN
07000 !    2 BYTES   MAX LEN AVAILABLE TO STORE INT
07100 !    3 BYTES   ABS ADDRESS OF FIRST BYTE TO STORE INT
07200 !    2 BYTES   LEN OF STRING P
07300 !    3 BYTES   ADDRESS OF STRING P
07400 !  R12-----
07500 ! 
07600 !  THE SYNTAX FOR VESUVIUS
07700 ! 
07800 !   VESUVIUS B$,P
07900 ! 
08000 !  WHERE B$ HAS TO BE 
08100 !  STRING VARIABLE AND I
08200 !  THE I/O BUFFER, AND P
08300 !  IS A STRING EXPRESSIO
08400 !  AND IS THE STRING TO B
08500 !  PRINTED
08600 ! 
08700 ! 
08800          POMD R45,-R12
08900          STMD R45,=PTR2-   
09000          POMD R36,-R12
09100          JNZ  #NULL$  
09200          LDMD R12,=TOS     
09300          RTN  
09400 #NULL$   LDMD R45,=PTR1    
09500          PUMD R45,+R6
09600          POMD R45,-R12
09700          POMD R34,-R12
09800          POMD R45,-R12
09900          STMD R45,=PTR1    
10000          POMD R32,-R12
10100          LDM  R20,R36
10200          BCD  
10300          LLM  R20
10400          BIN  
10500          LLM  R20
10600          CMM  R20,R32
10700          JNC  OK3     
10800          JZR  OK3     
10900          JSB  =ERROR   
11000          BYT  56D
11100          LDM  R22,R32
11200          LRM  R23
11300          BCD  
11400          LRM  R23
11500          BIN  
11600          STM  R22,R36
11700          LDM  R20,R32
11800 OK3      STMI R20,=PTR1    
11900 LOOP     LDBI R32,=PTR2-   
12000          ANM  R32,=177,0
12100          LLM  R32
12200          BCD  
12300          LLM  R32
12400          BIN  
12500          ADM  R32,=CHARS   
12600          ADMD R32,=BINTAB  
12700          POMD R40,+R32
12800          STMI R40,=PTR1-   
12900          POMD R40,+R32
13000          STMI R40,=PTR1-   
13100          POMD R40,+R32
13200          STMI R40,=PTR1-   
13300          POMD R40,+R32
13400          STMI R40,=PTR1-   
13500          DCM  R36
13600          JNZ  LOOP    
13700          POMD R45,-R6
13800          STMD R45,=PTR1    
13900          RTN  
14000 ! ************************
14100 ! 
14200 !  R12 STACK WILL LOOK LIKE THIS
14300 ! 
14400 !    3 BYTES ADDRESS OF FIRST ELEMEN
14500 !    3 BYTES ADDRESS OF NAM
14600 !    1 BYTES HEADE
14700 !  R12----
14800 ! 
14900 ! 
15000          BYT  241
15100 SETCH.   BIN  
15200          POBD R46,-R12
15300          BCD  
15400          LRB  R46
15500          CMB  R46,=5           !  SIMPLE NUMBERIC INTEGER ARRAY?
15600          BIN  
15700          JZR  OK4     
15800          LDB  R46,=1
15900          STBD R46,=ERRBP#  
16000          JSB  =ERROR+  
16100          BYT  365
16200 OK4      POMD R45,-R12         !  GET RID OF NAME ADDRESS
16300          POMD R45,-R12         !  GET PTR TO MAX ROW
16400          STMD R45,=PTR2-       !  SET PTR
16500          LDMI R44,=PTR2        !  GET MAX ROW  & MAX COL/VECTOR FLAG
16600          LDM  R26,R44          !  COPY VECTOR FLAG
16700          CMM  R26,=377,377     !  ONE-DIM ARRAY ?
16800          JZR  OK5     
16900          LDB  R26,=1
17000          STBD R26,=ERRBP#  
17100          JSB  =ERROR+  
17200          BYT  366
17300 OK5      BSZ  0
17400          LDM  R#,R46
17500          LDM  R22,=CHARS   
17600          ADMD R22,=BINTAB  
17700          LDB  R0,=77           !  INDIRECT REGISTER PTR
17800 LOOP2    LDB  R44,=377
17900          LDMI R45,=PTR2-       !  GET NEXT NUMBER FROM ARRAY
18000          PUMD R40,+R12         !  PUSH TO STACK FOR CONVERSION
18100          JSB  =ONEB            !  GET FROM STACK AND CONVERT
18200          STB  R46,R*           !  SAVE IN APPROPRIATE REGISTER R70-R77
18300          DCB  R0               !  MOVE TO NEXT REGISTER
18400          CMB  R0,=67           !  DONE 8 OF THEM?
18500          JNZ  DCM26            !  JIF NO
18600          PUMD R70,+R22         !  ELSE PUSH THEM OUT
18700          LDB  R0,=77           !  RESET REGISTER PTR
18800 DCM26    DCM  R26
18900          JNZ  LOOP2   
19000          CMB  R0,=77           !  ANY LEFT OVER?
19100          JZR  SETRTN           !  JIF NO
19200          PUMD R70,+R22         !  ELSE PUSH THEM OUT
19300 SETRTN   RTN  
19400 !  **********************************************************************
19500 !  *                                                                     
19600 !  *                                                                     
19700 !  *                                                                     
19800 !  **********************************************************************
19900 CHARS    BSZ  4200D
20000 !  **********************************************************************
20100 !  *                                                                     
20200 !  *                                                                     
20300 !  *                                                                     
20400 !  **********************************************************************
20500 PTR2-    DAD  177715
20600 PTR2     DAD  177714
20700 ERRBP#   DAD  103371
20800 BINTAB   DAD  104070
20900 PTR1     DAD  177710
21000 PTR1-    DAD  177711
21100 TOS      DAD  101744
21200 ONEB     DAD  12153
21300 SCAN     DAD  21110
21400 STRREF   DAD  24056
21500 STREX+   DAD  23721
21600 ERROR    DAD  10224
21700 ERROR+   DAD  10220
21800 FETSVA   DAD  45305
21900 FORMAR   DAD  27034
22000          FIN  
