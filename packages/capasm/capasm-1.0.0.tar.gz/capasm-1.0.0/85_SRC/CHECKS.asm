0010 ! ***********************************************************************
0020 ! *                                                                      
0030 ! *          FILE CHECKSUM     BINARY PROGRAM FOR HP-87                  
0040 ! *                                                                      
0050 ! ***********************************************************************
0060 ! *                                                                      
0070 ! *    syntax:                                                           
0080 ! *                                                                      
0090 ! *      CHECKSUM(<string exp>)                                          
0100 ! *                file name                                             
0110 ! ***********************************************************************
0120 ! *                                                                      
0130 ! *  This Binary Program calls three routines in the Mass Storage Rom.   
0140 ! *                                                                      
0150 ! *                                                                      
0160 ! *  GETSEC                                                              
0170 ! *                                                                      
0180 ! *     Reads one sector (256 bytes) from the disc into a memory location
0190 ! *     pointed to by R30-31.                                            
0200 ! *                                                                      
0210 ! *     INPUT CONDITIONS                                                 
0220 ! *                                                                      
0230 ! *        SAVER6 must contain the address to be loaded into R6-7 by     
0240 ! *        the Mass Storage Rom in case of error before executing a RTN. 
0250 ! *                                                                      
0260 ! *        R14-5 must contain the contents of RAM location MSBASE.       
0270 ! *                                                                      
0280 ! *        The RAM location pointed to by the contents of the RAM        
0290 ! *        location MSBASE must contain the contents of R12-13 at entry. 
0300 ! *                                                                      
0310 ! *        R32-3 must contain the sector number to be read as a Binary #.
0320 ! *                                                                      
0330 ! *                                                                      
0340 ! *                                                                      
0480 ! *                                                                      
0490 ! *     OUTPUT CONDITIONS                                                
0500 ! *                                                                      
0510 ! *        The selected sector will be in memory at the location pointed 
0520 ! *        to by PTR2 at entry. Consider all registers and PTR2 to be    
0530 ! *        undefined.                                                    
0540 ! *  TAPDS+                                                              
0550 ! *  DIRSCN                                                              
0560 ! ***********************************************************************
0570        NAM  CHECK 
0580        DEF  RUNTIM
0590        DEF  TOKS  
0600        DEF  PARSE 
0610        DEF  ERMSG 
0620        DEF  INIT  
0630 RUNTIM BYT  0,0
0640        DEF  CHECK.           !  RUNTIME ADDRESS FOR 'CHECKSUM'
0650        DEF  REV.             !  RUNTIME ADDRESS FOR REV DATE
0660 PARSE  BYT  0,0
0670 !                                  THERE'S NO NEED FOR A ENTRY IN THE PARS
0680 !                                  TABLE FOR REV DATE SINCE IT'S A FUNCTIO
0690 !                                  AND THERE'S NO KEYWORDS AFTER IT
0700        BYT  377,377          !  TERMINATE RELOCATION OF ADDRESSES
0710 ERMSG  BYT  200,200,200,200,200,200,200,200,200
0720        ASP  "BAD DIRECTORY ENTRY FOR THAT FILE NAME"
0721        ASC  "SORRY, BUT THIS BINARY PROGRAM WILL ONLY PERFORM CHECKSUMS OF FILES"
0722        ASP  " THAT EXIST ON A DISKETTE."
0730        BYT  377
0740 TOKS   ASP  "CHECKSUM"       !  KEYWORD # 1
0750        ASP  ""             !  KEYWORD CONTROL H CONTROL P
0760        BYT  377              !  TERMINATE KEYWORD TABLE
0770 INIT   RTN                   !  NO INITIALIZATION
0780 ! ********************************************************************
0790        BYT  30,55            !  ATTRIBUTES, 1 $ PARAMETER,NUM. FUNCTION
0800 CHECK. BIN                   !  FOR ADDRESS MATH
0810        LDMD R14,=BINTAB
0820        JSB  X14,SETR6 
0830        JSB  =ROMJSB
0840        DEF  TAPDS-
0850        VAL  MSROM#
0851        JEZ  DIROK 
0852        JSB  =ERROR+
0853        BYT  365
0860 DIROK  JSB  =ROMJSB
0870        DEF  DIRSCN
0880        VAL  MSROM#
0890        JEZ  OK    
0900        JSB  =ERROR+
0910        BYT  67D
0920 !  DIRSCN RETURNS R36-7 POINTING TO NAME IN DIRECTOR
0930 OK     LDMD R14,=BINTAB
0940        LDMD R26,X36,D.ORG 
0950        STB  R26,R0
0960        LDB  R26,R27
0970        STB  R0,R27
0980        STMD R26,X14,F.ORG 
0990        LDMD R26,X36,D.EXTS
1000        STB  R26,R0
1010        LDB  R26,R27
1020        STB  R0,R27
1030        STMD R26,X14,F.EXTS
1040        LDMD R26,X36,D.EXTB
1050        STMD R26,X14,F.EXTB
1060        CLM  R44
1070 LOOP   LDMD R14,=BINTAB
1080        STMD R44,X14,CHKSUM
1090        LDMD R32,X14,F.ORG 
1100        ICM  R32
1110        STMD R32,X14,F.ORG 
1120        DCM  R32
1130        LDMD R26,X14,F.EXTS
1140        DCM  R26
1150        JCY  OKSEC 
1180        JSB  =ERROR+
1190        BYT  366              !  BAD DIRECTORY FOR THAT FILE
1200 OKSEC  STMD R26,X14,F.EXTS
1210        JSB  X14,RSECTR
1220        BIN  
1230        CMB  R17,=300
1240        JCY  EREXIT
1250        LDMD R14,=BINTAB
1260        LDMD R22,X14,F.EXTB
1270        LDM  R24,=RECBUF
1280        LDMD R44,X14,CHKSUM
1290        CLM  R32
1300 ADDLOP POMD R30,+R24
1310        DCM  R22
1320        JNC  DONE  
1330        DCM  R22
1340        JCY  ADD   
1350        CLB  R30
1360        ADM  R44,R30
1370        JMP  DONE  
1380 ADD    ADM  R44,R30
1390        TSM  R22
1400        JZR  DONE  
1410        CMM  R24,=LSTBUF
1420        JNC  ADDLOP
1430        STMD R22,X14,F.EXTB
1440        JMP  LOOP  
1450 DONE   LDM  R36,R44
1460        ADM  R36,R46
1470        JSB  =CONBIN
1480        PUMD R40,+R12
1490 EREXIT RTN  
1500 ! ********************************************************************
1550 RSECTR JSB  X14,SETR6 
1580        LDM  R30,=RECBUF
1590        JSB  =ROMJSB
1600        DEF  GETSEC
1610        VAL  MSROM#
1640        RTN  
1650 ! ********************************************************************
1660 SETR6  LDM  R20,R6
1670        ADM  R20,=5,0
1680        STMD R20,=SAVER6
1690        LDMD R14,=MSBASE
1700        STMD R12,R14
1710        RTN  
1720 ! ********************************************************************
1730 ! ********************************************************************
1740        BYT  0,56             !  ATTRIBUTES,STRING FUNCTION, 0 PARAMETERS
1750 REV.   BIN                   !  FOR ADDRESS MATH
1760        LDM  R44,=47D,0
1770        DEF  DATE             !    AND ADDRESS
1790        ADMD R46,=BINTAB
1800        PUMD R44,+R12
1810        RTN  
1820 DATE   ASC  "(c) 1981 Hewlett-Packard Co.    Revision 110.14"
1840 ! ********************************************************************
1850 ! 
1860 F.EXTB BSZ  2
1870 F.EXTS BSZ  2
1880 F.ORG  BSZ  2
1890 CHKSUM BSZ  4
1900 D.EXTB EQU  34
1910 D.EXTS EQU  22
1920 D.ORG  EQU  16
1930 ! 
1940 BINTAB DAD  101233
1950 CONBIN DAD  3572
1970 DIRSCN DAD  63143
1990 ERROR+ DAD  6611
2000 FILTYP DAD  101034
2010 GETSEC DAD  77253
2020 LSTBUF DAD  102400
2030 MSBASE DAD  102540
2040 MSROM# DAD  320              ! 
2050 NUMVA+ DAD  12407
2060 ONEB   DAD  56113
2080 RECBUF DAD  102000
2090 ROMJSB DAD  4776
2100 SAVER6 DAD  101174
2110 SCAN   DAD  11262
2120 STOST  DAD  45603
2130 STREX+ DAD  13623
2140 STRREF DAD  13753
2150 TAPDS- DAD  70740
2160        FIN                   !  TERMINATE ASSEMBLY
