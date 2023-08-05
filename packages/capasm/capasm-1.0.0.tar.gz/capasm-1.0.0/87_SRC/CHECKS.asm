00010 ! ***********************************************************************
00020 ! *                                                                      
00030 ! *          FILE CHECKSUM     BINARY PROGRAM FOR HP-87                  
00040 ! *                                                                      
00050 ! ***********************************************************************
00060 ! *                                                                      
00070 ! *    syntax:                                                           
00080 ! *                                                                      
00090 ! *      CHECKSUM(<string exp>)                                          
00100 ! *                file name                                             
00110 ! ***********************************************************************
00120 ! *                                                                      
00130 ! *  This Binary Program calls three routines in the Mass Storage Rom.   
00140 ! *                                                                      
00150 ! *                                                                      
00160 ! *  GETSEC                                                              
00170 ! *                                                                      
00180 ! *     Reads one sector (256 bytes) from the disc into a memory location
00190 ! *     pointed to by PTR2.                                              
00200 ! *                                                                      
00210 ! *     INPUT CONDITIONS                                                 
00220 ! *                                                                      
00230 ! *        SAVER6 must contain the address to be loaded into R6-7 by     
00240 ! *        the Mass Storage Rom in case of error before executing a RTN. 
00250 ! *                                                                      
00260 ! *        R14-5 must contain the contents of RAM location MSBASE.       
00270 ! *                                                                      
00280 ! *        The RAM location pointed to by the contents of the RAM        
00290 ! *        location MSBASE must contain the contents of R12-13 at entry. 
00300 ! *                                                                      
00310 ! *        R32-3 must contain the sector number to be read as a Binary #.
00320 ! *                                                                      
00330 ! *                                                                      
00340 ! *                                                                      
00350 ! *             1) The first word of the 256 bytes of memory             
00360 ! *          OR                                                          
00370 ! *             2) One byte past the last byte of the memory             
00380 ! *                                                                      
00390 ! *          Which it has to be depends on whether you want the first    
00400 ! *          byte of the sector to be at the lowest (1) or highest (2)   
00410 ! *          address. Whichever is chosen two things must be set up      
00420 ! *          to coincide with that choice: FILTYP and DFLAG.             
00430 ! *          If DFLAG=0 then (1) must be used; if DFLAG#0 and FILTYP=10  
00440 ! *          then (1) must be used; If DFLAG#0 and FILTYP#10 then (2)    
00450 ! *          must be used.                                               
00460 ! *                                                                      
00470 ! *        DFLAG and FILTYP must be set according to PTR2.               
00480 ! *                                                                      
00490 ! *     OUTPUT CONDITIONS                                                
00500 ! *                                                                      
00510 ! *        The selected sector will be in memory at the location pointed 
00520 ! *        to by PTR2 at entry. Consider all registers and PTR2 to be    
00530 ! *        undefined.                                                    
00540 ! *  TAPDS+                                                              
00550 ! *  DIRSCN                                                              
00560 ! ***********************************************************************
00570          NAM  40,CHECK         !  BINARY PROGRAM # = 40 OCTAL
00580          DEF  RUNTIM  
00590          DEF  TOKS    
00600          DEF  PARSE   
00610          DEF  ERMSG   
00620          DEF  INIT    
00630 RUNTIM   BYT  0,0
00640          DEF  CHECK.           !  RUNTIME ADDRESS FOR 'CHECKSUM'
00650          DEF  REV.             !  RUNTIME ADDRESS FOR REV DATE
00660 PARSE    BYT  0,0
00670 !                                  THERE'S NO NEED FOR A ENTRY IN THE PARS
00680 !                                  TABLE FOR REV DATE SINCE IT'S A FUNCTIO
00690 !                                  AND THERE'S NO KEYWORDS AFTER IT
00700          BYT  377,377          !  TERMINATE RELOCATION OF ADDRESSES
00710 ERMSG    BYT  200,200,200,200,200,200,200,200,200
00720          ASP  "BAD DIRECTORY ENTRY FOR THAT FILE NAME"
00730          BYT  377
00740 TOKS     ASP  "CHECKSUM"       !  KEYWORD # 1
00750 !        ASP  ""             !  KEYWORD CONTROL H CONTROL P
00755          BYT  10,220           !  KEYWORD CONTROL H CONTROL P
00760          BYT  377              !  TERMINATE KEYWORD TABLE
00770 INIT     RTN                   !  NO INITIALIZATION
00780 ! ********************************************************************
00790          BYT  30,55            !  ATTRIBUTES, 1 $ PARAMETER,NUM. FUNCTION
00800 CHECK.   BIN                   !  FOR ADDRESS MATH
00810          LDMD R14,=BINTAB  
00820          JSB  X14,SETR6   
00830          JSB  =ROMJSB  
00840          DEF  TAPDS+  
00850          VAL  MSROM#  
00860          JSB  =ROMJSB  
00870          DEF  DIRSCN  
00880          VAL  MSROM#  
00890          JEZ  OK      
00900          JSB  =ERROR+  
00910          BYT  67D
00920 !  DIRSCN RETURNS R36-7 POINTING TO NAME IN DIRECTOR
00930 OK       LDMD R14,=BINTAB  
00940          LDMD R26,X36,D.ORG   
00950          STB  R26,R0
00960          LDB  R26,R27
00970          STB  R0,R27
00980          STMD R26,X14,F.ORG   
00990          LDMD R26,X36,D.EXTS   !  WRONG!!!!!!
01000          STB  R26,R0           ! 
01010          LDB  R26,R27          ! 
01020          STB  R0,R27           ! 
01030          STMD R26,X14,F.EXTS   ! 
01040          LDMD R26,X36,D.EXTB  
01050          STMD R26,X14,F.EXTB  
01060          CLM  R44
01070 LOOP     LDMD R14,=BINTAB  
01080          STMD R44,X14,CHKSUM  
01090          LDMD R32,X14,F.ORG   
01100          ICM  R32
01110          STMD R32,X14,F.ORG   
01120          DCM  R32
01130          LDMD R26,X14,F.EXTS  
01140          DCM  R26
01150          JCY  OKSEC   
01160          LDB  R26,=40
01170          STBD R26,=ERRBP#  
01180          JSB  =ERROR+  
01190          BYT  366              !  BAD DIRECTORY FOR THAT FILE
01200 OKSEC    STMD R26,X14,F.EXTS  
01210          JSB  X14,RSECTR  
01220          BIN  
01230          CMB  R17,=300
01240          JCY  EREXIT  
01250          LDMD R14,=BINTAB  
01260          LDMD R22,X14,F.EXTB   !  WRONG !!!!!!!!!!!
01270          LDM  R24,=LSTBUF  
01280          LDMD R44,X14,CHKSUM  
01290          CLM  R32
01300 ADDLOP   POMD R30,-R24
01310          DCM  R22              !  WRONG!!!!!
01320          JNC  DONE    
01330          DCM  R22              !  WRONG !!!!!
01340          JCY  ADD     
01350          CLB  R30
01360          ADM  R44,R30
01370          JMP  DONE    
01380 ADD      ADM  R44,R30
01390          TSM  R22              !  WRONG !!!!!!
01400          JZR  DONE    
01410          CMM  R24,=RECBUF  
01420          JNZ  ADDLOP  
01430          STMD R22,X14,F.EXTB   !  WRONG !!!!!!!
01440          JMP  LOOP    
01450 DONE     LDM  R36,R44
01460          ADM  R36,R46
01470          JSB  =CONBIN  
01480          PUMD R40,+R12
01490 EREXIT   RTN  
01500 ! ********************************************************************
01510 RSECTR   CLB  R40
01520          STBD R40,=FILTYP  
01530          ICB  R40
01540          STBD R40,=DFLAG   
01550          JSB  X14,SETR6   
01560          LDM  R75,=LSTBUF  
01570          BYT  0
01580          STMD R75,=PTR2-   
01590          JSB  =ROMJSB  
01600          DEF  GETSEC  
01610          VAL  MSROM#  
01620          CLB  R40
01630          STBD R40,=DFLAG   
01640          RTN  
01650 ! ********************************************************************
01660 SETR6    LDM  R20,R6
01670          ADM  R20,=5,0
01680          STMD R20,=SAVER6  
01690          LDMD R14,=MSBASE  
01700          STMD R12,R14
01710          RTN  
01720 ! ********************************************************************
01730 ! ********************************************************************
01740          BYT  0,56             !  ATTRIBUTES,STRING FUNCTION, 0 PARAMETERS
01750 REV.     BIN                   !  FOR ADDRESS MATH
01760          LDM  R43,=14,0        !  LENGTH OF STRING
01770          DEF  DATE             !    AND ADDRESS
01780          BYT  0                !  3-BYTE ADDRESS
01790          ADMD R45,=BINTAB      !  MAKE IT AN ABSOLUTE ADDRESS
01800          PUMD R43,+R12         !  PUSH ON OPERATING STACK
01810          RTN  
01820          ASC  "1891,92 TPES"   !  THE DATE: SEPT 29,1981
01830 DATE     BSZ  0                !  TO GET THE RIGHT ADDRESS
01840 ! ********************************************************************
01850 ! 
01860 F.EXTB   BSZ  3
01870 F.EXTS   BSZ  2
01880 F.ORG    BSZ  2
01890 CHKSUM   BSZ  4
01900 D.EXTB   EQU  34
01910 D.EXTS   EQU  22
01920 D.ORG    EQU  16
01930 ! 
01940 BINTAB   DAD  104070           ! 
01950 CONBIN   DAD  4401
01960 DFLAG    DAD  104224           ! 
01970 DIRSCN   DAD  63162
01980 ERRBP#   DAD  103371
01990 ERROR+   DAD  10220            ! 
02000 FILTYP   DAD  101671           ! 
02010 GETSEC   DAD  77126            ! 
02020 LSTBUF   DAD  103200           ! 
02030 MSBASE   DAD  103412           ! 
02040 MSROM#   DAD  320              ! 
02050 NUMVA+   DAD  22403            ! 
02060 ONEB     DAD  12153            ! 
02070 PTR2-    DAD  177715           ! 
02080 RECBUF   DAD  102600           ! 
02090 ROMJSB   DAD  6223             ! 
02100 SAVER6   DAD  104066           ! 
02110 SCAN     DAD  21110            ! 
02120 STOST    DAD  46472            ! 
02130 STREX+   DAD  23721            ! 
02140 STRREF   DAD  24056            ! 
02150 TAPDS+   DAD  70726
02160          FIN                   !  TERMINATE ASSEMBLY
