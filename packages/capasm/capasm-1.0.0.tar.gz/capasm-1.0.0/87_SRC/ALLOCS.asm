01000 ! ASTORE "ALLOCS
01100 ! ASSEMBLE "ALLOC
01200 ! REN 1000,10
01300          NAM  76,ALLO    
01400          DEF  RUNTIM  
01500          DEF  TOKS    
01600          DEF  PARSE   
01700          DEF  ERMSG   
01800          DEF  INIT    
01900 RUNTIM   BSZ  2
02000          DEF  ALLOC.  
02100 PARSE    BSZ  2
02200          DEF  ALLOC@  
02300 ERMSG    BYT  377,377
02400 TOKS     ASP  "ALLOCATE"
02500          BYT  377
02600 INIT     RTN  
02700 !  **********************************************************************
02800 !  *                                                                     
02900 !  *                                                                     
03000 !  *                                                                     
03100 !  **********************************************************************
03200 ALLOC@   LDM  R56,=76,371      !  SYSTEM TOKEN AND BPGM #
03300          LDB  R55,R43          !  GET TOKEN#
03400          STMI R55,=PTR2-       !  PUSH OUT
03500          JSB  =SCAN            !  GET NEXT TOKEN
03600          RTN                   !  DONE
03700 !  **********************************************************************
03800 !  *                                                                     
03900 !  *                                                                     
04000 !  *                                                                     
04100 !  **********************************************************************
04200          BYT  241
04300 ALLOC.   BIN  
04400          LDMD R55,=PTR1        !  GET PC
04500          PUMD R55,+R6          !  SAVE IT
04600          LDMD R55,=PCR         !  GET PCR
04700          PUMD R55,+R6          !  SAVE IT
04800          PUMD R16,+R6          !  SAVE CSTAT & XCOM
04900          JSB  =INIT.           !  INITIALIZE THE PROGRAM
05000          LDM  R20,R16          !  COPY CSTAT & XCOM
05100          POMD R16,-R6          !  RECOVER CSTAT & XCOM
05200          ORB  R17,R21          !  OR IN ERROR STUFF
05300          CMB  R17,=300         !  ANY ERRORS?
05400          JCY  ALLOCRTN         !  JIF YES
05500          ANM  R17,=37          !  TRASH IMMEDIATE BREAK
05600 ALLOCRTN POMD R55,-R6          !  RECOVER PCR
05700          STMD R55,=PCR         !  RESTORE IT
05800          POMD R55,-R6          !  RECOVER PC
05900          STMD R55,=PTR1        !  RESTORE IT
06000          RTN                   !  DONE
06100 !  **********************************************************************
06200 !  *                                                                     
06300 !  *                                                                     
06400 !  *                                                                     
06500 !  **********************************************************************
06600 SCAN     DAD  21110
06700 PTR1     DAD  177710
06800 PTR2-    DAD  177715
06900 PCR      DAD  101115
07000 INIT.    DAD  1241
07100          FIN  
