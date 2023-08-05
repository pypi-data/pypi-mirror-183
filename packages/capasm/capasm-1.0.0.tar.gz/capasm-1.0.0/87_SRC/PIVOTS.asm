01000          LST  
01010          NAM  30,PIVOT   
01020          DEF  RUNTIM  
01030          DEF  TOKENS  
01040          DEF  BASIC   
01050          DEF  ERMSG   
01060          DEF  INIT    
01070 RUNTIM   BYT  0,0
01080          DEF  PIVOT.  
01090 BASIC    BYT  0,0
01100          DEF  PIVOTP  
01110          BYT  377,377
01120 TOKENS   ASP  "PIVOT"
01130 ERMSG    BYT  377
01140 ! ********************************************************************
01150 ! *  This Binary Program provides the BASIC statement:                
01160 ! *        PIVOT A(,),R,C,B,I                                         
01170 ! *  The PIVOT statement performs the same thing as the following     
01180 ! *  BASIC code:                                                      
01190 ! *                                                                   
01200 ! *    100 FOR I=W TO 1 STEP -1                                       
01210 ! *    110 IF I=R THEN                                                
01220 ! *    120 V=A(I,C)                                                   
01230 ! *    130 FOR J=B TO 1 STEP -1                                       
01240 ! *    140 IF J=C THEN                                                
01250 ! *    150 A(I,J)=A(I,J)-A(R,J)*V                                     
01260 ! *    160 IF ABS(A(I,J))<=.00001 THEN A(I,J)=0                       
01270 ! *    170 NEXT J                                                     
01280 ! *    180 A(I,C)=0                                                   
01290 ! *    190 NEXT I                                                     
01300 ! *                                                                   
01310 ! *********************************************************************
01320          BYT  241
01330 PIVOT.   JSB  =ONEB            !  GET LIMIT VALUE OF I (VALUE OF W)
01340          LDMD R14,=BINTAB      !  GET BASE ADDRESS
01350          LDM  R24,=I           !  GET ADDRESS OF TEMP AREA
01360          ADM  R24,R14          !  MAKE IT ABSOLUTE
01370          CLM  R50              !  8 BYTES OF ZEROES
01380          PUMD R50,+R24         !  LET'S PUSH OUT 40 DECIMAL BYTES
01390          PUMD R50,+R24         ! 
01400          PUMD R50,+R24         ! 
01410          PUMD R50,+R24         ! 
01420          PUMD R50,+R24         ! 
01430          STMD R46,X14,I        !  SAVE LIMIT VALUE OF I
01440          JSB  =ONEB            !  GET VALUE OF B
01450          STMD R46,X14,B        !  STORE IT AWAY
01460          JSB  =ONEB            !  GET VALUE OF C
01470          STMD R46,X14,C        !  SAVE IT AWAY
01480          JSB  =ONEB            !  GET VALUE OF R
01490          STMD R46,X14,R        !  SAVE IT AWAY
01500 ! 
01510 ! ********************************************************************
01520 ! *  AN ARRAY IN THE HP-87 IS STORED IN MEMORY IN THE FOLLOWING FORM: 
01530 ! *                                                                   
01540 ! *    |                |                                             
01550 ! *    |                |                                             
01560 ! *    |       .        |                                             
01570 ! *    |       .        |                                             
01580 ! *    |       .        |                                             
01590 ! *    |----------------|                                             
01600 ! *    |                |                                             
01610 ! *    |                |                                             
01620 ! *    |                |                                             
01630 ! *    |                |  ELEMENT ROW 0, COL 1 VALUE                 
01640 ! *    |                |                                             
01650 ! *    |                |                                             
01660 ! *    |                |                                             
01670 ! *    |                |                                             
01680 ! *    |----------------|                                             
01690 ! *    | 3-BYTE INTEGER |                                             
01700 ! *    | 4-BYTE SHORT   |                                             
01710 ! *    |      OR        |                                             
01720 ! *    | 8-BYTE REAL    |  ELEMENT ROW 0, COL 0 VALUE                 
01730 ! *    |   VALUE/ELEMENT|                                             
01740 ! *    |                |                                             
01750 ! *    |                |                                             
01760 ! *    |                |                                             
01770 ! *    |----------------|                                             
01780 ! *    | 2-BYTE MAX     | <------------------ BASE ADDRESS            
01790 ! *    |     COLUMN     |                                             
01800 ! *    |----------------|                                             
01810 ! *    | 2-BYTE MAX     |                                             
01820 ! *    |     ROW        |                                             
01830 ! *    |----------------|                                             
01840 ! *    | 3-BYTE TOTAL   |                                             
01850 ! *    |     SIZE       |                                             
01860 ! *    |                |                                             
01870 ! *    |----------------|                                             
01880 ! *    | 3-BYTE RELATIVE|                                             
01890 ! *    |    ADDRESS OF  |                                             
01900 ! *    |     NAME       |                                             
01910 ! *    |----------------|                                             
01920 ! *    | 1-BYTE HEADER  |                                             
01930 ! *    |----------------|                                             
01940 ! *                                                                   
01950 ! *  The PIVOT statement is parsed using the FORMAR routine. Therefore
01960 ! *   the operating stack (R12) will look like this at runtime:       
01970 ! *                                                                   
01980 ! *          ABSOLUTE BASE ADDRESS OF ARRAY       3-BYTES             
01990 ! *          ABSOLUTE ADDRESS OF NAME OF ARRAY    3-BYTES             
02000 ! *          HEADER OF ARRAY VARIABLE             1-BYTE              
02010 ! *          VALUE OF R                           8-BYTES             
02020 ! *          VALUE OF C                           8-BYTES             
02030 ! *          VALUE OF B                           8-BYTES             
02040 ! *          VALUE OF I (REALLY 'W')              8-BYTES             
02050 ! *   R12 --------->                                                  
02060 ! *                                                                   
02070 ! *********************************************************************
02080          POMD R44,-R12         !  THROW AWAY HEADER AND PTR TO NAME
02090          POMD R45,-R12         !  GET BASE ADDRESS OF ARRAY A(,)
02100          STMD R45,=PTR2        !  SET PTR
02110          STM  R45,R23          !  SAVE COPY IN R23-25
02120          LDMI R45,=PTR2        !  FETCH MAX COL VALUE
02130          CLB  R47              !  IT WAS ONLY A TWO-BYTE VALUE
02140          LLM  R45              !  x2
02150          LLM  R45              !  x4
02160          LLM  R45              !  x8
02170          STM  R45,R20          !  SAVE 8*(MAX COL) IN R20-22
02180          LDMD R45,X14,I        !  GET START VALUE OF I
02190 MAIN     LDMD R55,X#,R         !  GET VALUE OF R
02200          CMM  R55,R45          !  IF I=R THEN
02210          JZR  AJMP             !       NEXT I
02220          LDMD R55,X14,C        !  GET VALUE OF C
02230          JSB  X14,FETCH        !  CALCULATE ADDRESS OF A(I,C)
02240          LDMI R40,=PTR2-       !  GET VALUE OF A(I,C)
02250          STMD R40,X14,V        !  SAVE IN TEMP AREA
02260          STMD R65,X14,AI.C     !  SAVE ADDRESS OF A(I,C)
02270          LDMD R45,X14,I        !  GET CURRENT VALUE OF I
02280          LDMD R55,X14,B        !  GET VALUE OF B
02290          JSB  X14,FETCH        !  GET ADDRESS OF A(I,B)
02300          STMD R#,X14,AI.B      !  SAVE ADDRESS OF A(I,B)
02310          LDMD R45,X14,R        !  GET VALUE OF R
02320          JSB  X14,FETCH+       !  GET ADDRESS OF A(R,J)
02330          STMD R#,X14,AR.B      !  SAVE ADDRESS OF A(R,J)
02340          LDMD R26,X14,B        !  GET VALUE OF B
02350 LOOPJ    LDMD R36,X#,C         !  GET VALUE OF C
02360          CMM  R26,R36          !  IF J=C THEN
02370          JZR  BETA             !      NEXT J
02380          LDMD R52,X14,AI.B     !  GET ADDRESSES OF A(I,B) AND A(R,J)
02390          STMD R52,=PTR2        !  SET PTR TO A(I,B)
02400          LDMI R40,=PTR2-       !  GET VALUE OF A(I,B)
02410          PUMD R40,+R12         !  PUSH TO OPERATING STACK
02420          STMD R55,=PTR2        !  SET PTR TO A(R,J)
02430          LDMI R40,=PTR2-       !  GET VALUE OF A(R,J)
02440          PUMD R40,+R12         !  PUSH TO OPERATING STACK
02450          LDMD R40,X14,V        !  GET VALUE OF V FROM TEMP AREA
02460          PUMD R40,+R12         !  PUSH TO OPERATING STACK
02470          BCD                   !  FOR MATH ROUTINES
02480          JSB  =MPYROI          !  GET A(R,J)*V
02490          JSB  =SUBROI          !  GET A(I,J)-A(R,J)*V
02500          POMD R40,-R12         !  GET IT OFF THE STACK
02510          JZR  CLMR40           !  JIF THE RESULT IS 0
02520          BIN                   !  FOR COMPARE
02530          CMB  R44,=377         !  IS THE RESULT A TAGGED INTEGER?
02540          JNZ  NOTINT           !  JIF NO
02550          TSM  R45              !  IS THE RESULT 0
02560          JZR  CLMR40           !  JIF YES
02570          JMP  STORE            ! 
02580 AJMP     JMP  ALPHA            !  HOP, SKIP, AND A
02590 MJMP     JMP  MAIN             !                   JUMP
02600 NOTINT   BCD                   !  FOR SHIFTING
02610          LDM  R30,R40          !  GET THE EXPONENT
02620          LRB  R31              !  GET THE MOST SIGNIFICANT DIGIT
02630          CMB  R31,=5           !  IS IT A NEGATIVE EXPONENT?
02640          JNC  STORE            !  JIF NO
02650          CMM  R30,=94C,9C      !  IS THE VALUE LESS THAN .00001?
02660          JCY  STORE            !  JIF NO
02670 CLMR40   CLM  R40              !  MAKE IT ZERO
02680 STORE    BIN                   !  FOR BINARY MATH
02690          LDMD R14,=BINTAB      !  RELOAD BASE ADDRESS
02700          LDMD R75,X14,AI.B     !  GET ADDRESS OF A(I,J)
02710          STMD R75,=PTR2        !  SET PTR
02720          STMI R40,=PTR2-       !  STORE NEW VALUE OF A(I,J)
02730 BETA     DCM  R26              !  J=0 ?
02740          JZR  QUIT             !  JIF YES, DONE
02750          LDMD R42,X14,AI.B     !  ELSE GET ADDRESSES OF A(I,J) AND A(R,J)
02760          ADM  R42,=10,0,0,10,0,0 !  MOVE UP TO NEXT ONES
02770          STMD R42,X14,AI.B     !  RESTORE ADDRESSES
02780          JMP  LOOPJ            !  NEXT J
02790 QUIT     CLM  R40              !  VALUE OF ZERO
02800          LDMD R75,X14,AI.C     !  GET ADDRESS OF A(I,C)
02810          STMD R75,=PTR2        !  SET PTR
02820          STMI R40,=PTR2-       !  STORE VALUE OF 0 INTO A(I,C)
02830 ALPHA    LDMD R45,X14,I        !  GET CURRENT VALUE OF I
02840          DCM  R45              !  DECREMENT
02850          JZR  END              !  JIF I=0, DONE
02860          STMD R45,X14,I        !  ELSE STORE NEW VALUE OF I
02870          JMP  MJMP             !      AND NEXT I
02880 END      RTN                   !  DONE
02890 FETCH    DCM  R#               !  -1
02900          LLM  R#               !  x2
02910          LLM  R#               !  x4
02920          LLM  R#               !  x8
02930          TCM  R#               !  NEGATIVE
02940 FETCH+   LDM  R65,R55          !  GET COPY
02950 DCMR30   DCM  R45              !  IF I=1 THEN
02960          JZR  FETCHV           !     SKIP
02970          SBM  R65,R20          !   ELSE R65=(-8*(C-1))-(8*R*(I-1))
02980          JMP  DCMR30           !  LOOP FOR MULTIPLY
02990 FETCHV   ADM  R65,R23          !  R65-67=BASE-8*(C-1)-8*R*(I-1)
03000          STMD R65,=PTR2        !  SET PTR
03010 INIT     RTN                   !  DONE
03020 ! ********************************************************************
03030 ! *                                                                   
03040 ! *&k1S PIVOT PARSE ROUTINE&k2S 
03050 ! *                                                                   
03060 ! ********************************************************************
03070 PIVOTP   JSB  =SCAN            !  GET NEXT TOKEN
03080          JSB  =FORMAR          !  GET ARRAY REFERENCE
03090          JEZ  NOARRY           !  JIF NOT THERE
03100          JSB  =GET4N           !  GET 4 NUMERIC PARAMETERS
03110          LDBI R30,=PTR2+       !  GET RID OF EXTRA TOKEN PUSHED BY SYSTEM
03120          LDM  R55,=1,30,371    !  LOAD BPGM TOK#,BPGM#,SYS BPGM TOK
03130          STMI R55,=PTR2-       !  STORE OUT TO PARSED OUTPUT STREAM
03140 NOARRY   RTN                   !  DONE
03150 ! ********************************************************************
03160 ! *                                                                   
03170 ! *&k1S TEMPORARY RAM SPACE&k2S 
03180 ! *                                                                   
03190 ! ********************************************************************
03200 I        BYT  0,0,0            ! \
03210 B        BYT  0,0,0            !  \
03220 C        BYT  0,0,0            !   \
03230 R        BYT  0,0,0            !    \
03240 BASE     BYT  0,0,0            !     \
03250 COL      BYT  0,0,0            !      \  TEMPORARY VARIABLE VALUES
03260 AI.B     BYT  0,0,0            !      /  AND ADDRESSES STORAGE
03270 AR.B     BYT  0,0,0            !     /
03280 AI.C     BYT  0,0,0            !    /
03290 J        BYT  0,0,0            !   /
03300 V        BYT  0,0,0,0,0,0,0,0  !  /
03310          BYT  0,0              ! /
03320 ! ********************************************************************
03330 ! *                                                                   
03340 ! *&k1S  SYSTEM ADDRESSES  &k2S 
03350 ! *                                                                   
03360 ! ********************************************************************
03370 BINTAB   DAD  104070           ! 
03380 ONEB     DAD  12153            ! 
03390 PTR2     DAD  177714           ! 
03400 PTR2-    DAD  177715           ! 
03410 PTR2+    DAD  177716           !  SYSTEM DAD'S
03420 SCAN     DAD  21110            ! 
03430 MPYROI   DAD  53517            ! 
03440 SUBROI   DAD  52724            ! 
03450 GET4N    DAD  24635            ! 
03460 FORMAR   DAD  27034            ! 
03470          FIN  
