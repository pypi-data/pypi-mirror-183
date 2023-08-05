01000 !  (c) COPYRIGHT HEWLETT-PACKARD CO., 1981.  ALL RIGHTS ARE RESERVED
01010 !  FORMS - HP87 FORM BINARY (This is the real Mc Coy turkey.
01020 !  RELEASE:  006.02     LAST EDIT:  08/07/81      REVISED BY:  Pau
01030 !  -----------------------------------------------------------------------
01040 ! 
01050 ! 
01060 ! 
01070 ! 
01080 ! 
01090          GLO  FORMGLOBAL
01100          NAM  20,FORM          ! 
01110          DEF  RUNTIM           ! 
01120          DEF  TOKS             ! 
01130          DEF  BASIC            ! 
01140          DEF  ERROR            ! 
01150          DEF  INIT             ! 
01160 RUNTIM   BYT  0,0              ! 
01170          DEF  GET.             ! 
01180          DEF  GET.             ! 
01190          DEF  INP.    
01200          DEF  DEL.             ! 
01210          DEF  DEL.             ! 
01220          DEF  FENTER$.
01230          DEF  FENTERN.
01240          DEF  ???.    
01250          DEF  MSG.             ! 
01260          DEF  AN$.    
01270          DEF  REV.             ! 
01280          DEF  FART.            ! 
01290          DEF  FART.            ! 
01300          DEF  FEND.            ! 
01310          DEF  FEND.            ! 
01320          DEF  WIND.            ! 
01330          DEF  WIND.            ! 
01340          DEF  NAME.   
01350          DEF  FPOS.   
01360          DEF  FLEN.   
01370          DEF  TFNUM.  
01380          DEF  FIELDS. 
01390 BASIC    BYT  0,0              ! 
01400          DEF  GET#             ! 
01410          DEF  GET#+            ! 
01420          DEF  DEL#    
01430          DEF  DEL#             ! 
01440          DEF  DEL#+            ! 
01450          DEF  FENTER# 
01460          DEF  FENTER# 
01470          DEF  MSG#    
01480          DEF  MSG#             ! 
01490          BYT  377,377          ! 
01500 TOKS     ASP  "GET FORM"       ! 
01510          ASP  "GF"             ! 
01520          ASP  "FINPUT"
01530          ASP  "DELETE FORM"    ! 
01540          ASP  "DF"             ! 
01550          ASP  "FENTER"
01560          ASP  "FENTER"
01570          ASP  "QUESTION"
01580          ASP  "MESSAGE"        ! 
01590          ASP  "ANSWER$"
01600          ASP  ""             ! 
01610          ASP  "FORM START"     ! 
01620          ASP  "FS"             ! 
01630          ASP  "FORM END"       ! 
01640          ASP  "FE"             ! 
01650          ASP  "WINDOW"         ! 
01660          ASP  "WI"             ! 
01670          ASP  "FNAME$"         ! 
01680          ASP  "FPOS"
01690          ASP  "FLEN"
01700          ASP  "TFNUM"
01710          ASP  "FIELDS"
01720          BYT  377              ! 
01730 ERROR    BSZ  0                ! 
01740          BYT  377              ! 
01750 !       ------------------
01760 ! 
01770 GET#+    BIN  
01780          DCB  R43
01790 GET#     PUBD R43,+R6          ! 
01800          JSB  =STREX+          ! 
01810          JEZ  ERROR!           ! 
01820          JSB  =DMNDCR          ! 
01830 THER+    POBD R55,-R6          ! 
01840 THERE    LDM  R56,=20,371      ! 
01850          STMI R55,=PTR2-       ! 
01860          RTN  
01870 INIT     BIN  
01880          LDBD R22,=ROMFL   
01890          CMB  R22,=2
01900          JZR  RTNRTN  
01910          CMB  R22,=5
01920          JZR  RTNRTN  
01930          LDMD R22,=BINTAB  
01940          CLB  R36
01950          STBD R36,X22,ANSFLG  
01960          DRP  R74
01970          BYT  251
01980          ASC  "FORM"
01990          STMD R#,=F.CAT   
02000          RTN  
02010 ! 
02020 RTNRTN   LDB  R34,=236
02030          STBD R34,=KYIDLE  
02040          JSB  =CLEAR.  
02050          RTN  
02060 !  _______________________________________________________
02070 ! 
02080 ! 
02090 DEL#+    BIN  
02100          DCB  R43
02110 DEL#     LDM  R56,=20,371      ! 
02120          STMI R56,=PTR2-       ! 
02130          STBI R43,=PTR2-   
02140          JSB  =SCAN            ! 
02150          JSB  =DMNDCR          ! 
02160          RTN                   ! 
02170 !       ------------------
02180 ! 
02190 MSG#     PUBD R43,+R6          ! 
02200          JSB  =STREX+          ! 
02210          JEZ  ERROR!           ! 
02220          JSB  =GETCMA          ! 
02230          JSB  =NUMVAL          ! 
02240          JEZ  ERROR!           ! 
02250          JMP  THER+            ! 
02260 ! 
02270 !       ------------------
02280 ! 
02290 ERROR!   POBD R43,-R6          ! 
02300          JSB  =ERROR+          ! 
02310          BYT  88D              ! 
02320          LDB  R47,R43          ! 
02330          JMP  THERE            ! 
02340 ! 
02350 !       ------------------
02360 ! 
02370 FENTER#  PUBD R43,+R6
02380          JSB  =SCAN    
02390          JSB  =STRREF  
02400          JEN  OK$     
02410          JSB  =REFNUM  
02420          JEN  OKN     
02430          JSB  =ERROR+  
02440          BYT  88D
02450 OK$      POBD R55,-R6
02460 OK       LDM  R56,=20,371
02470          STMI R55,=PTR2-   
02480          RTN  
02490 OKN      POBD R55,-R6
02500          ICB  R55
02510          JMP  OK      
02520 ! 
02530 !       ------------------
02540 ! 
02550 !  ====================
02560 !  REVISION DATE RUNTIM
02570 !  ====================
02580 ! 
02590          BYT  0,56             ! 
02600 REV.     BIN                   ! 
02610          LDM  R43,=8D,0        ! 
02620          DEF  DATE             ! 
02630          BYT  0
02640          ADMD R45,=BINTAB      ! 
02650          PUMD R43,+R12         ! 
02660          RTN                   ! 
02670          ASC  "18/40/80"
02680 DATE     BSZ  0
02690 ! 
02700 COLONE   LDMD R34,=CRTBYT  
02710          JSB  =COLUMN  
02720          SBM  R34,R66
02730          RTN  
02740 ! 
02750 ! 
02760 !  -------------------------------------------------------
02770 !  Form Name Runtim
02780 !  ----------------
02790 ! 
02800          BYT  0,56
02810 NAME.    BIN  
02820          LDM  R43,=30D,0
02830          DEF  FNAME   
02840          BYT  0
02850          ADMD R45,=BINTAB  
02860          PUMD R43,+R12
02870          RTN  
02880 ! 
02890 ! 
02900 ! 
02910 !  =======================
02920 !  GET FORM RUNTIME ROUTIN
02930 !  =======================
02940 ! 
02950          BYT  241              ! 
02960 GET.     BIN                   ! 
02970          JSB  =ALPHA           ! 
02980 !       __________________________________________________
02990          LDMD R14,=BINTAB      ! 
03000 !       __________________________________________________
03010          LDB  R56,=FRMTYP      !  Establish File Type FORM
03020          STBD R56,=FILTYP      ! 
03030 !       __________________________________________________
03040          JSB  =ROMJSB          ! 
03050          DEF  MSIN             ! 
03060          VAL  MSROM#           ! 
03070 !       __________________________________________________
03080          LDM  R20,R6           ! 
03090          ADM  R20,=7,0         !  Give MS ROM a Quick Escape
03100          STMD R20,=SAVER6      ! 
03110 !       __________________________________________________
03120          JSB  =ROMJSB          ! 
03130          DEF  TAPDS-           !  Set MSUS & Get The File Name
03140          VAL  MSROM#           ! 
03150 !       __________________________________________________
03160 NORTN    BIN                   ! 
03170          LDMD R14,=BINTAB      !  Squish CALVRB
03180 !       __________________________________________________
03190          JSB  X14,LODLOP  
03200 !       __________________________________________________
03210          LDMD R14,=BINTAB  
03220          LDM  R26,=FORM        !  Get Address Of Form In RAM.
03230          ADM  R26,R14
03240          CMB  R17,=300         !  Check for Load Errors
03250          JNC  PAGE?            !  Don't Display If Errors Exist
03260          JSB  =CRTUNW  
03270          RTN  
03280 PAGE?    LDBD R77,X14,PAGMOD  
03290          JNZ  PAG24   
03300          JSB  =PAGES1  
03310          JMP  DISP    
03320 PAG24    JSB  =PAGES2  
03330 !       __________________________________________________
03340 DISP     LDMD R36,X14,EFORM   
03350          JSB  =CRTWPO  
03360          TSM  R36              ! 
03370          JNZ  GO!!             ! 
03380          JSB  =CRTUNW  
03390          RTN  
03400 !       __________________________________________________
03410 GO!!     BIN                   ! 
03420          PUMD R36,+R6
03430          LDBD R34,X14,FSTART  
03440          JZR  GO!!-   
03450          LDB  R35,=4
03460          LDBD R34,=CRTSTS  
03470          ORB  R34,R35
03480          STBD R34,=CRTSTS  
03490 ! 
03500 GO!!-    CLM  R34
03510          JSB  =SAD1    
03520          JSB  =BYTCRT  
03530          LDM  R36,=PAGSIZ  
03540          LDB  R32,=15
03550          JSB  =L7      
03560          JSB  =DECUR2  
03570          CLM  R32
03580 !         JSB =CHKSTS            ! Get Beg. Form Screen Addr
03590 !         STMD R32,=CRTBAD       ! (Addr. of Curr Cursor Pos
03600          STMD R32,X14,BFORM    ! 
03610 !       __________________________________________________
03620          POMD R36,-R6
03630          LDM  R34,R36          !  Length Of Form (in Chars)
03640          ADM  R34,R32          !  Add Form Start Addr.
03650          DCM  R34              ! 
03660          STMD R34,X14,EFORM    !  Save End Form Screen Addr.
03670 !       __________________________________________________
03680          JSB  =BYTCRT  
03690          JSB  X14,COLONE  
03700          ADM  R34,=LINSIZ      ! 
03710          STMD R34,X14,WINDOW   ! 
03720          CLM  R32              !  Get In Alpha and Set First Page
03730          JSB  =BYTCRT          ! 
03740 !       __________________________________________________
03750 !       __________________________________________________
03760 LUPE     POBD R32,+R26         !  Pop 1 Character From Form
03770          JSB  =CHKSTS          ! 
03780          STBD R32,=CRTDAT      !  Display To Screen Mem.
03790          DCM  R36              ! 
03800          JNZ  LUPE             !  Continue Until Complete Form
03810 !       __________________________________________________
03820          LDMD R36,X14,WINDOW   !  Get CRT Addr. of Window
03830          JSB  =BYTCRT          !  Set Cursor to it.
03840 !       __________________________________________________
03850          CLM  R34
03860 RTN      JSB  =CRTUNW          !  Turn On CRT.  (Hello There!!)
03870          BSZ  0
03880 ! 
03890 !  ****               ***
03900 !  **** GET FORM EXIT ***
03910 !  ****               ***
03920          RTN                   ! 
03930 MSG      ASC  "NO TAPE TURKEY!"
03940 !       __________________________________________________
03950 ! 
03960 !  -----------------------
03970 !  LOAD IN FOR
03980 !  -----------------------
03990 ! 
04000 LODLOP   LDMD R75,=NXTDAT  
04010          PUMD R75,+R6
04020          LDMD R75,=NXTMEM  
04030          PUMD R75,+R6
04040          LDMD R75,=LSTDAT  
04050          PUMD R75,+R6
04060          LDM  R75,=FSTART  
04070          BYT  0
04080          ADMD R75,=BINTAB  
04090          STMD R75,=LSTDAT  
04100          LDM  R75,=EFORM+  
04110          BYT  0
04120          ADMD R75,=BINTAB  
04130          STMD R75,=NXTDAT  
04140          LDMD R20,=NXTMEM  
04150          PUMD R12,+R6
04160          LDMD R65,=PTR1    
04170          PUMD R65,+R6
04180          JSB  =ROMJSB  
04190          DEF  MSIN    
04200          VAL  MSROM#  
04210          JSB  =ROMJSB  
04220          DEF  LOADB$  
04230          VAL  MSROM#  
04240          LDMD R14,=BINTAB  
04250          BIN  
04260          POMD R75,-R6
04270          STMD R75,=PTR1    
04280          POMD R12,-R6
04290          POMD R75,-R6
04300          STMD R75,=LSTDAT  
04310          POMD R75,-R6
04320          STMD R75,=NXTMEM  
04330          POMD R75,-R6
04340          STMD R75,=NXTDAT  
04350          RTN  
04360 ! 
04370 ! 
04380 !       __________________________________________________
04390 ! 
04400 !  -----------------------
04410 !  DELETE FORM RUNTIME ROU
04420 !  -----------------------
04430 ! 
04440          BYT  241              ! 
04450 DEL.     BIN                   ! 
04460          JSB  =DECUR2          ! 
04470          LDMD R14,=BINTAB      ! 
04480          LDMD R34,X14,BFORM    ! 
04490          JSB  =BYTCRT          ! 
04500          LDMD R36,X14,EFORM    ! 
04510          SBM  R36,R34          ! 
04520          LDB  R32,=CR          ! 
04530          ICM  R36              ! 
04540 CLR      JSB  =CHKSTS          ! 
04550          STBD R32,=CRTDAT      ! 
04560          DCM  R36              ! 
04570          JNZ  CLR              ! 
04580          LDMD R34,=CRTBYT      ! 
04590          JSB  =BYTCRT          ! 
04600          LDMD R34,=CRTRAM      ! 
04610          JSB  =SAD1            ! 
04620          CLM  R#               ! 
04630          STMD R#,X14,WINDOW    ! 
04640          STMD R#,X14,BFORM     ! 
04650          STMD R#,X14,EFORM   
04660          STBD R#,X14,NUMFLD  
04670          STBD R#,X14,IFPTR   
04680          STBD R#,X14,TFPTR   
04690          LDBD R34,X14,FSTART  
04700          JZR  BLACK   
04710          LDB  R35,=4
04720          LDBD R34,=CRTSTS  
04730          XRB  R34,R35
04740          STBD R34,=CRTSTS  
04750 BLACK    JSB  =CURS    
04760          RTN  
04770 ! 
04780 !  -----------------------
04790 !  MESSAGE RUNTIME ROUTIN
04800 !  -----------------------
04810 ! 
04820          BYT  241
04830 ???.     BIN  
04840          CLB  R00
04850          ICB  R00
04860          JMP  MSG!    
04870          BYT  241              ! 
04880 MSG.     BIN                   ! 
04890          CLB  R00
04900 MSG!     BSZ  0
04910          LDMD R14,=BINTAB      ! 
04920          JSB  =ONEB            ! 
04930          POMD R45,-R12         ! 
04940          STMD R45,=PTR2        ! 
04950          POMD R36,-R12         ! 
04960          LDM  R56,=LINSIZ  
04970          LDMD R34,X14,WINDOW   ! 
04980          JNZ  DOWN+   
04990 REGOUT   LDM  R76,R36
05000          LDM  R30,=INPBUF  
05010          JSB  =DCSLOP  
05020          JSB  =DECUR2  
05030          LDM  R26,=INPBUF  
05040          JSB  =OUTSTR  
05050          RTN  
05060 DOWN+    TSM  R76
05070          JZR  OUT              ! 
05080          ANM  R76,=3,0
05090          JPS  DOWN    
05100          TCM  R76
05110 DOWN     DCM  R76              ! 
05120          JZR  OUT              ! 
05130          ADM  R34,=LINSIZ      ! 
05140          JMP  DOWN             ! 
05150 OUT      STM  R34,R56          ! 
05160          JSB  =BYTCRT          ! 
05170          JSB  =BLKLIN          ! 
05180          LDM  R34,R56          ! 
05190          JSB  =BYTCRT          ! 
05200          STM  R36,R76          ! 
05210          ADM  R76,R34          ! 
05220          TSM  R36              ! 
05230          JZR  DONE             ! 
05240 SPIT     LDBI R32,=PTR2-       ! 
05250          JSB  =CHKSTS          ! 
05260          STBD R32,=CRTDAT      ! 
05270          DCM  R36              ! 
05280          JNZ  SPIT             ! 
05290 DONE     LDM  R34,R76          ! 
05300          TSB  R0
05310          JZR  SETME   
05320          ADM  R34,=LINSIZ  
05330          JSB  =BYTCRT  
05340          JSB  X14,COLONE  
05350          JSB  =BYTCRT  
05360 SETME    DRP  R34
05370          JSB  =BYTCRT  
05380          RTN                   ! 
05390 ! 
05400 ! 
05410 !  =======================
05420 !  INPUT SUBROUTIN
05430 !  =======================
05440 ! 
05450 INPUT.   LDMD R75,=PTR1    
05460          STMD R75,=SAVPC   
05470          STMD R12,=INPTOS  
05480          LDM  R22,=INPBUF  
05490          STMD R22,=INPTR   
05500          LDB  R16,=4
05510          JSB  =SET240  
05520          RTN  
05530 ! 
05540 ! 
05550 !  ---------------------------------------------------------------
05560 !  Form Parameter Function
05570 !  -----------------------
05580 ! 
05590 ! 
05600 ! 
05610          BYT  0,55             ! 
05620 FART.    BIN                   ! 
05630          LDMD R14,=BINTAB      ! 
05640          LDMD R36,X14,BFORM    ! 
05650          JMP  SHIP             ! 
05660 ! 
05670          BYT  0,55             ! 
05680 FEND.    BIN                   ! 
05690          LDMD R14,=BINTAB      ! 
05700          LDMD R36,X14,EFORM    ! 
05710          JMP  SHIP             ! 
05720 ! 
05730          BYT  0,55             ! 
05740 WIND.    BIN                   ! 
05750          LDMD R14,=BINTAB      ! 
05760          LDMD R36,X14,WINDOW   ! 
05770 SHIP     JSB  =CONBIN          ! 
05780          PUMD R40,+R12         ! 
05790          RTN  
05800 ! 
05810          BYT  20,55
05820 FLEN.    BIN  
05830          LDMD R14,=BINTAB  
05840          JSB  =ONEB    
05850          LLM  R46
05860          ADM  R14,=LENGTH  
05870          ADM  R14,R46
05880          LDMD R36,R14
05890          JMP  SHIP    
05900 ! 
05910          BYT  20,55
05920 FPOS.    BIN  
05930          LDMD R14,=BINTAB  
05940          JSB  =ONEB    
05950          LLM  R46
05960          ADM  R14,=FIELD   
05970          ADM  R14,R46
05980          LDMD R36,R14
05990          JMP  SHIP    
06000 ! 
06010          BYT  0,55
06020 TFNUM.   BIN  
06030          LDMD R14,=BINTAB  
06040          LDMD R36,X14,TFPTR   
06050          JMP  SHIP    
06060 ! 
06070          BYT  0,55
06080 FIELDS.  BIN  
06090          LDMD R14,=BINTAB  
06100          LDBD R36,X14,NUMFLD  
06110          CLB  R37
06120          JMP  SHIP    
06130 ! 
06140 ! 
06150 !  _______________________________________________________
06160 ! 
06170 ! 
06180 ANSR.    JSB  =CURS    
06190          ICB  R20
06200          STBD R20,X14,ANSFLG  
06210          LDMI R75,=PTR1+   
06220          JSB  X14,INPUT.  
06230          RTN  
06240 !  _______________________________________________________
06250          BYT  0,56
06260 AN$.     BIN  
06270          CMB  R16,=2
06280          JZR  RUNOK   
06290          JSB  =ERROR+  
06300          BYT  88D
06310 RUNOK    LDMD R14,=BINTAB  
06320          LDBD R20,X14,ANSFLG  
06330          JZR  ANSR.   
06340          LDMD R12,=INPTOS  
06350          CLB  R20
06360          STBD R20,X14,ANSFLG  
06370          LDMD R32,=INPTR   
06380          STM  R32,R14
06390          CLM  R36
06400 CHRCNT   POBD R35,+R32
06410          CMB  R35,=15
06420          JZR  ENDOF$  
06430          ICM  R36
06440          JMP  CHRCNT  
06450 !  _______________________________________________________
06460 ENDOF$   TSM  R36
06470          JZR  FINI    
06480          POBD R25,-R32
06490 !  _______________________________________________________
06500 POPBLK   POBD R25,-R32
06510          CMB  R25,=40
06520          JNZ  FINI    
06530          DCM  R36
06540          JNZ  POPBLK  
06550 !  _______________________________________________________
06560 FINI     PUMD R36,+R12
06570          ICM  R32
06580          STM  R32,R55
06590          CLB  R57
06600 FINLOP   CMM  R14,R32
06610          JCY  FINRTN  
06620          LDBD R20,R14
06630          POBD R21,-R32
06640          PUBD R21,+R14
06650          STBD R20,R32
06660          JMP  FINLOP  
06670 FINRTN   PUMD R55,+R12
06680          JSB  =DECUR2  
06690          RTN  
06700 ! 
06710 !  --------------------------------------------------------------
06720 !  KYIDLE SERVICE ROUTIN
06730 !  ---------------------
06740 ! 
06750 ! 
06760 KEYIN    BIN  
06770          PUMD R75,+R6
06780          LDBD R75,=SVCWRD  
06790          JEV  NEWKEY  
06800          POMD R75,-R6
06810          RTN  
06820 NEWKEY   CLM  R75
06830          LDBD R76,=KEYSTS  
06840          ANM  R76,=10,0
06850          LDB  R75,R76
06860          LDMD R76,=BINTAB  
06870          STBD R75,X76,SHIFT   
06880          POMD R75,-R6
06890          RTN  
06900 ! 
06910 !  --------------------------------------------------------------
06920 !  FORM INPUT ROUTIN
06930 !  ---------------------
06940 ! 
06950          BYT  241
06960 INP.     BIN  
06970          JSB  =DECUR2  
06980          LDMD R14,=BINTAB  
06990          LDM  R34,=KEYIN   
07000          ADMD R34,=BINTAB  
07010          LDB  R74,=316
07020          STM  R34,R75
07030          LDB  R77,=236
07040          STMD R74,=KYIDLE  
07050          LDMD R26,X14,TFPTR   
07060          LLM  R26
07070          ADM  R26,R14
07080          LDMD R36,X26,FIELD   
07090          JSB  =BYTCRT  
07100 !         JSB =EOJ
07110 KEYLO+   JSB  =CURS    
07120          LDBD R0,=EDMOD2  
07130          JZR  COOLIT  
07140          JSB  =LTCUR.  
07150          JSB  =CURS    
07160          JSB  =RTCUR.  
07170 COOLIT   JSB  =COUNTK  
07180          CLB  R64
07190          CLM  R56
07200 KEYLOP   DCM  R56
07210          JPS  NORMAL  
07220          LDM  R56,=0,25
07230          NCB  R64
07240          JZR  ON      
07250          JSB  =DECUR2  
07260          JMP  NORMAL  
07270 ON       JSB  =CURS    
07280          LDBD R0,=EDMOD2  
07290          JZR  NORMAL  
07300          JSB  =LTCUR.  
07310          JSB  =CURS    
07320          JSB  =RTCUR.  
07330 NORMAL   LDBD R32,=SVCWRD  
07340          JEV  KEYLOP  
07350          JSB  =DECUR2  
07360          CLM  R32
07370          LDBD R32,=KEYHIT  
07380          JPS  ECOCHR  
07390          CMB  R32,=232
07400          JZR  RETURN  
07410          JSB  X14,KEYTEST 
07420          JMP  KEYLO+  
07430 ! 
07440 RETURN   JSB  =EOJ2    
07450          LDMD R26,X14,TFPTR   
07460          LDBD R66,X14,NUMFLD  
07470          CLB  R67
07480          CMM  R26,R66
07490          JCY  NOMORE  
07500          ICM  R26
07510          STMD R26,X14,TFPTR   
07520 NOMORE   RTN  
07530 ! 
07540 ECOCHR   JSB  X14,ECHO    
07550          JMP  KEYLO+  
07560 ! 
07570 ! 
07580 KEYTEST  BIN  
07590          CMB  R32,=244
07600          JNZ  NONE    
07610          JSB  =DNCUR.  
07620 !         JSB X14,OFFIN
07630          RTN  
07640 NONE     JSB  =STBEEP  
07650          RTN  
07660 ! 
07670 ! 
07680 ECHO     BIN  
07690          LDMD R14,=BINTAB  
07700          LDMD R66,=CRTBYT  
07710          ADM  R66,R14
07720          LDBD R66,X66,FORM    
07730          CMB  R66,=240
07740          JNZ  OUTFIELD
07750          LDB  R33,=200
07760          XRB  R32,R33
07770          JSB  =CHKSTS  
07780          STBD R32,=CRTDAT  
07790          JSB  =RTCUR.  
07800          RTN  
07810 ! 
07820 OUTFIELD JSB  =STBEEP  
07830          RTN  
07840 ! 
07850 !  -------------------------------------------------------
07860 !  FORM ENTER ROUTIN
07870 !  -------------------
07880 ! 
07890          BYT  241
07900 FENTER$. BIN  
07910          LDMD R14,=BINTAB  
07920          JSB  X14,GETFIELD
07930          JSB  =STOST   
07940          RTN  
07950 ! 
07960          BYT  241
07970 FENTERN. BIN  
07980          LDMD R14,=BINTAB  
07990          JSB  X14,GETFIELD
08000          JSB  =VAL.    
08010          JSB  =STOSV   
08020          RTN  
08030 ! 
08040 GETFIELD LDMD R26,X14,IFPTR   
08050          LDBD R34,X14,NUMFLD  
08060          CLB  R35
08070          CMM  R26,R34
08080          JNC  OKFLD   
08090          CLM  R36
08100          JMP  DONFLD  
08110 OKFLD    LLM  R26
08120          ADM  R26,R14
08130          LDMD R34,X26,FIELD   
08140          JSB  =BYTCRT  
08150          LDMD R36,X26,LENGTH  
08160          STM  R36,R76
08170          LDM  R22,=INPBUF  
08180          ADM  R22,=240,0
08190          LDB  R33,=200
08200 ENT+     JSB  =INCHR   
08210          XRB  R32,R33
08220          PUBD R32,-R22
08230          DCM  R76
08240          JNZ  ENT+    
08250          CLM  R34
08260          JSB  =BYTCRT  
08270          LDMD R26,X14,IFPTR   
08280          ICM  R26
08290          STMD R26,X14,IFPTR   
08300 DONFLD   PUMD R36,+R12
08310          LDM  R45,=INPBUF  
08320          BYT  0
08330          CLB  R40
08340          ADM  R45,=240,0,0
08350          PUMD R45,+R12
08360          RTN  
08370 ! 
08380 ! 
08390 ! 
08400 !  _______________________________________________________
08410 ! 
08420 ! 
08430 ! 
08440 SHIFT    BSZ  1
08450 ST240+   DAD  21067
08460 BFORM    BSZ  2                ! 
08470 ANSFLG   BSZ  1
08480 SAVNXT   BSZ  2                ! 
08490 LINSIZ   EQU  120              ! 
08500 PAGSIZ   EQU  3600             ! 
08510 HOLD12   BSZ  2                ! 
08520 WINDOW   BSZ  2                ! 
08530 ENDMEM   BSZ  2                ! 
08540 TFPTR    BSZ  2
08550 IFPTR    BSZ  2
08560 FSTART   BSZ  30               ! 
08570 FNAME    BSZ  0
08580 PAGMOD   BSZ  1                ! 
08590 NUMFLD   BSZ  1                ! 
08600 FIELD    BSZ  400
08610 LENGTH   BSZ  400
08620 FORM     BSZ  3600
08630 EFORM    BSZ  2
08640 EFORM+   FIN                   ! 
08650 !  GOODB
