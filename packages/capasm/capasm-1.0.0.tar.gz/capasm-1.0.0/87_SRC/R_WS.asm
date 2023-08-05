01000 ! ***********************************************************************
01010 ! *                                                                      
01020 ! *          READ/WRITE SECTOR BINARY PROGRAM FOR HP-87                  
01030 ! *                                                                      
01040 ! ***********************************************************************
01050 ! *                                                                      
01060 ! *    syntax:                                                           
01070 ! *                                                                      
01080 ! *      RSECTOR <string var>,<numeric exp>,<string exp>                 
01090 ! *                 (sink)     (sector #)     (msus)                     
01100 ! *                                                                      
01110 ! *      WSECTOR <string exp>,<numeric exp>,<string exp>                 
01120 ! *                (source)    (sector #)     (msus)                     
01130 ! *                                                                      
01140 ! ***********************************************************************
01150 ! *                                                                      
01160 ! *  This Binary Program calls three routines in the Mass Storage Rom.   
01170 ! *                                                                      
01180 ! *  DCDFIL                                                              
01190 ! *                                                                      
01200 ! *     Decodes a file name and/or an MSUS, storing the file name in     
01210 ! *     FNAM and FNAM+5 and storing the MSUS in ACTMSU.                  
01220 ! *                                                                      
01230 ! *     INPUT CONDITIONS:                                                
01240 ! *                                                                      
01250 ! *        SAVER6 must contain the address to be loaded into R6-7 by     
01260 ! *        the Mass Storage Rom in case of error before executing a RTN. 
01270 ! *                                                                      
01280 ! *        The length (2 bytes) and address (3 bytes) of the string      
01290 ! *        which represents the file name and/or MSUS must be on the     
01300 ! *        R12 (operating) stack.                                        
01310 ! *                                                                      
01320 ! *        R14-5 must contain the contents of RAM location MSBASE.       
01330 ! *                                                                      
01340 ! *        The RAM location pointed to by the contents of the RAM        
01350 ! *        location MSBASE must contain the contents of R12-13 at entry. 
01360 ! *                                                                      
01370 ! *        R40 must contain a flag specifying what you want DCDFIL to    
01380 ! *        accept:                                                       
01390 ! *                   0 = at least a file name or an MSUS                
01400 ! *                   1 = filename only (no MSUS allowed)                
01410 ! *                   2 = MSUS only (no file name allowed)               
01420 ! *                                                                      
01430 ! *     OUTPUT CONDITIONS                                                
01440 ! *                                                                      
01450 ! *        Assume all registers and PTR2 to be undefined.                
01460 ! *                                                                      
01470 ! *  GETSEC                                                              
01480 ! *                                                                      
01490 ! *     Reads one sector (256 bytes) from the disc into a memory location
01500 ! *     pointed to by PTR2.                                              
01510 ! *                                                                      
01520 ! *     INPUT CONDITIONS                                                 
01530 ! *                                                                      
01540 ! *        SAVER6 must contain the address to be loaded into R6-7 by     
01550 ! *        the Mass Storage Rom in case of error before executing a RTN. 
01560 ! *                                                                      
01570 ! *        R14-5 must contain the contents of RAM location MSBASE.       
01580 ! *                                                                      
01590 ! *        The RAM location pointed to by the contents of the RAM        
01600 ! *        location MSBASE must contain the contents of R12-13 at entry. 
01610 ! *                                                                      
01620 ! *        R32-3 must contain the sector number to be read as a Binary #.
01630 ! *                                                                      
01640 ! *                                                                      
01650 ! *                                                                      
01660 ! *             1) The first word of the 256 bytes of memory             
01670 ! *          OR                                                          
01680 ! *             2) One byte past the last byte of the memory             
01690 ! *                                                                      
01700 ! *          Which it has to be depends on whether you want the first    
01710 ! *          byte of the sector to be at the lowest (1) or highest (2)   
01720 ! *          address. Whichever is chosen two things must be set up      
01730 ! *          to coincide with that choice: FILTYP and DFLAG.             
01740 ! *          If DFLAG=0 then (1) must be used; if DFLAG#0 and FILTYP=10  
01750 ! *          then (1) must be used; If DFLAG#0 and FILTYP#10 then (2)    
01760 ! *          must be used.                                               
01770 ! *                                                                      
01780 ! *        DFLAG and FILTYP must be set according to PTR2.               
01790 ! *                                                                      
01800 ! *     OUTPUT CONDITIONS                                                
01810 ! *                                                                      
01820 ! *        The selected sector will be in memory at the location pointed 
01830 ! *        to by PTR2 at entry. Consider all registers and PTR2 to be    
01840 ! *        undefined.                                                    
01850 ! *                                                                      
01860 ! *  PUTSEC                                                              
01870 ! *                                                                      
01880 ! *     Writes 256 bytes of memory out to a given sector on disk.        
01890 ! *                                                                      
01900 ! *     INPUT CONDITIONS                                                 
01910 ! *                                                                      
01920 ! *     Same as for GETSEC.                                              
01930 ! *                                                                      
01940 ! *     OUTPUT CONDITIONS                                                
01950 ! *                                                                      
01960 ! *     Same as for GETSEC.                                              
01970 ! *                                                                      
01980 ! ***********************************************************************
01990          NAM  37,R/WSEC        !  BINARY PROGRAM # = 37 OCTAL
02000          DEF  RUNTIM  
02010          DEF  TOKS    
02020          DEF  PARSE   
02030          DEF  ERMSG   
02040          DEF  INIT    
02050 RUNTIM   BYT  0,0
02060          DEF  READ.            !  RUNTIME ADDRESS FOR 'RSECTOR'
02070          DEF  WRITE.           !  RUNTIME ADDRESS FOR 'WSECTOR'
02080          DEF  REV.             !  RUNTIME ADDRESS FOR REV DATE
02090 PARSE    BYT  0,0
02100          DEF  RPARSE           !  PARSE ADDRESS FOR 'RSECTOR'
02110          DEF  WPARSE           !  PARSE ADDRESS FOR 'WSECTOR'
02120 !                                  THERE'S NO NEED FOR A ENTRY IN THE PARS
02130 !                                  TABLE FOR REV DATE SINCE IT'S A FUNCTIO
02140 !                                  AND THERE'S NO KEYWORDS AFTER IT
02150 ERMSG    BYT  377,377          !  TERMINATE RELOCATION OF ADDRESSES
02160 TOKS     ASP  "RSECTOR"        !  KEYWORD # 1
02170          ASP  "WSECTOR"        !  KEYWORD # 2
02180 !        ASP  ""             !  KEYWORD CONTROL H CONTROL P
02185          BYT  10,220           !  KEYWORD CONTROL H CONTROL P
02190          BYT  377              !  TERMINATE KEYWORD TABLE
02200 INIT     RTN                   !  NO INITIALIZATION
02210 ! ********************************************************************
02220 RPARSE   PUBD R43,+R6          !  SAVE INCOMING TOKEN #
02230          JSB  =SCAN            !  GET THE NEXT TOKEN IN THE INPUT STREAM
02240          JSB  =STRREF          !  GET A STRING VARIABLE REFERENCE(STORE $)
02250 COMPAR   JEN  OK               !  JIF GOT IT ELSE
02260 ERR      POBD R43,-R6          !     CLEAN UP R6 (RETURN) STACK AND
02270          JSB  =ERROR+          !        REPORT ERROR
02280          BYT  88D              !           # 88 (BAD STATEMENT)
02290 OK       CMB  R14,=54          !  CHECK TO SEE IF A COMMA IS NEXT
02300          JNZ  ERR              !  JIF NO, ERROR
02310          JSB  =NUMVA+          !  ELSE SCAN & GET NUMERIC EXPR (SECTOR #)
02320          JEZ  ERR              !  JIF NOT THERE TO ERROR
02330          CMB  R14,=54          !  CHECK TO SEE IF A COMMA IS NEXT
02340          JNZ  ERR              !  JIF NO, ERROR
02350          JSB  =STREX+          !  GET A STRING EXPRESSION (MSUS $)
02360          JEZ  ERR              !  JIF NOT THERE TO ERROR
02370          LDM  R56,=37,371      !  LOAD BP # AND SYSTEM BP TOKEN
02380          POBD R55,-R6          !  RECOVER INCOMING TOKEN #
02390          STMI R55,=PTR2-       !  STORE IT ALL OUT TO PARSE STACK
02400          RTN                   !  DONE
02410 ! ********************************************************************
02420 WPARSE   PUBD R43,+R6          !  SAVE INCOMING TOKEN #
02430          JSB  =STREX+          !  GET A STRING EXPRESSION (THE $ TO WRITE)
02440          JMP  COMPAR           !  JMP TO COMMON PARSE FINISH
02450 ! ********************************************************************
02460          BYT  241              !  ATTRIBUTE, STATEMENT LEGAL AFTER THEN
02470 READ.    BIN                   !  FOR ADDRESS MATH
02480          CLB  R40              !  GET A 0
02490          STBD R40,=FILTYP      !  SET FILTYP TO 0
02500          LDB  R40,=2           !  GET A 2
02510          STBD R40,=DFLAG       !  SET DIRECTION FLAG TO NON-ZERO
02520          LDM  R20,R6           !  GET A COPY OF STACK POINTER
02530          ADM  R20,=7,0         !  ADD SEVEN
02540          STMD R20,=SAVER6      !  STORE FOR MASS STORAGE ROM ERROR EXIT
02550          LDMD R14,=MSBASE      !  GET MS ROM BASE IN R14
02560          STMD R12,R14          !  STORE STACK POINTER TO RAM
02570          JSB  =ROMJSB          !  CALL MS ROM
02580          DEF  DCDFIL           !  DECODE THE MASS STORAGE UNIT SPECIFIER
02590          VAL  MSROM#           !  320
02600          JSB  =ONEB            !  GET THE SECTOR # OFF STACK AS BINARY #
02610          STM  R46,R32          !  COPY IT INTO R32-3 FOR 'GETSEC'
02620          LDM  R75,=LSTBUF      !  GET ADDRESS OF LAST BYTE OF BUFFER + 1
02630          BYT  0                !  (NEED A 3-BYTE ADDRESS FOR PTR)
02640          STMD R75,=PTR2-       !  SET PTR2 FOR 'GETSEC'
02650          JSB  =ROMJSB          !  CALL MS ROM
02660          DEF  GETSEC           !  READ THE SECTOR TO PTR2-
02670          VAL  MSROM#           !  320
02680          CLB  R40              !  GET A 0
02690          STBD R40,=DFLAG       !  CLEAR DIRECTION FLAG
02700          CMB  R17,=300         !  CHECK FOR ANY ERRORS
02710          JCY  READRTN          !  JIF ERROR, DON'T STORE TO $
02720          LDM  R66,=0,1         !  LENGTH SHOULD BE 256
02730          PUMD R66,+R12         !  PUSH TO OPERATING STACK
02740          LDM  R65,=LSTBUF      !  ADDRESS OF HIGHEST BYTE +1
02750          BYT  0                !  (3-BYTE ADDRESS AGAIN)
02760          PUMD R65,+R12         !  PUSH TO OPERATING STACK
02770          JSB  =STOST           !  HAVE THE SYSTEM STORE IT INOT THE $
02780 READRTN  RTN                   !  DONE
02790 ! ********************************************************************
02800          BYT  241              !  ATTRIBUTE, STATEMENT LEGAL AFTER THEN
02810 WRITE.   BIN                   !  FOR ADDRESS MATH
02820          CLB  R40              !  GET A 0
02830          STBD R40,=FILTYP      !  SET FILE TYPE TO 0
02840          LDB  R40,=2           !  GET A 2
02850          STBD R40,=DFLAG       !  SET DIRECTION FLAG TO NON-ZERO
02860          LDM  R20,R6           !  GET A COPY OF THE RETURN STACK POINTER
02870          ADM  R20,=7,0         !  ADD SEVEN FOR ROMJSB RETURN ETC.
02880          STMD R20,=SAVER6      !  SET FOR MS ROM ERROR EXIT
02890          LDMD R14,=MSBASE      !  GET MS ROMs RAM BASE ADDRESS
02900          STMD R12,R14          !  STORE R12 STACK POINTER INTO RAM
02910          JSB  =ROMJSB          !  CALL MS ROM
02920          DEF  DCDFIL           !  DECODE THE MSUS
02930          VAL  MSROM#           !  320
02940          JSB  =ONEB            !  GET THE SECTOR # OFF THE STACK
02950          STM  R46,R32          !  SET IN R32-3 FOR 'PUTSEC'
02960          POMD R65,-R12         !  GET ADDRESS OF $ TO BE WRITTEN
02970          STMD R65,=PTR2-       !  SET PTR2 POINTING TO IT
02980          POMD R46,-R12         !  THROW AWAY THE LENGTH, WE'RE GOINT TO
02990 !                                   WRITE 256 WHETHER THE STRINGS THAT LON
03000 !                                   OR NOT
03010          JSB  =ROMJSB          !  CALL MS ROM
03020          DEF  PUTSEC           !  WRITE THE $ TO THE SECTOR
03030          VAL  MSROM#           !  320
03040          CLB  R40
03050          STBD R40,=DFLAG       !  CLEAR DIRECTION FLAG
03060          RTN                   !  DONE
03070 ! ********************************************************************
03080          BYT  0,56             !  ATTRIBUTES,STRING FUNCTION, 0 PARAMETERS
03090 REV.     BIN                   !  FOR ADDRESS MATH
03100          LDM  R43,=14,0        !  LENGTH OF STRING
03110          DEF  DATE             !    AND ADDRESS
03120          BYT  0                !  3-BYTE ADDRESS
03130          ADMD R45,=BINTAB      !  MAKE IT AN ABSOLUTE ADDRESS
03140          PUMD R43,+R12         !  PUSH ON OPERATING STACK
03150          RTN  
03160          ASC  "1891,92 TPES"   !  THE DATE: SEPT 29,1981
03170 DATE     BSZ  0                !  TO GET THE RIGHT ADDRESS
03180 ! ********************************************************************
03190 BINTAB   DAD  104070           ! 
03200 DCDFIL   DAD  61371            ! 
03210 DFLAG    DAD  104224           ! 
03220 ERROR+   DAD  10220            ! 
03230 FILTYP   DAD  101671           ! 
03240 GETSEC   DAD  77126            ! 
03250 LSTBUF   DAD  103200           ! 
03260 MSBASE   DAD  103412           ! 
03270 MSROM#   DAD  320              ! 
03280 NUMVA+   DAD  22403            ! 
03290 ONEB     DAD  12153            ! 
03300 PTR2-    DAD  177715           ! 
03310 PUTSEC   DAD  77040            !  LABEL DEFINITIONS
03320 RECB+1   DAD  102601           ! 
03330 RECBUF   DAD  102600           ! 
03340 ROMJSB   DAD  6223             ! 
03350 SAVER6   DAD  104066           ! 
03360 SCAN     DAD  21110            ! 
03370 STOST    DAD  46472            ! 
03380 STREX+   DAD  23721            ! 
03390 STRREF   DAD  24056            ! 
03400          FIN                   !  TERMINATE ASSEMBLY
