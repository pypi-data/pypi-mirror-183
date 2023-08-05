01000 !  (c) COPYRIGHT HEWLETT-PACKARD CO., 1981.  ALL RIGHTS ARE RESERVED
01010 !  CFORMS - HP87 FORM CREAT
01020 !  RELEASE:  006.02     LAST EDIT:  08/06/81      REVISED BY:  PAU
01030 !  ---------------------------------------------------------------------
01040 ! 
01050 ! 
01060 ! 
01070 ! 
01080 ! 
01090          GLO  FORMGLOBAL
01100          NAM  21,CFORM         ! 
01110          DEF  RUNTIM           ! 
01120          DEF  TOKS             ! 
01130          DEF  BASIC            ! 
01140          DEF  ERROR            ! 
01150          DEF  INIT             ! 
01160 RUNTIM   BYT  0,0              ! 
01170          DEF  CREAT.           ! 
01180          DEF  REV.    
01190 ! 
01200 BASIC    BYT  0,0              ! 
01210          DEF  CREAT#           ! 
01220          BYT  377,377          ! 
01230 TOKS     ASP  "CREATE"         ! 
01240          ASP  ""
01250          BYT  377              ! 
01260 ERROR    BSZ  0                ! 
01270          BYT  377
01280 INIT     LDBD R0,=ROMFL   
01290          CMB  R0,=1
01300          JZR  RTNRTN  
01310          DRP  R74
01320          BYT  251
01330          ASC  "FORM"
01340          STMD R#,=F.CAT   
01350 F.CAT    DAD  107504
01360          RTN  
01370 INITAL   LDM  R34,=KEYIN   
01380          ADMD R34,=BINTAB  
01390          LDB  R74,=316
01400          STM  R34,R75
01410          LDB  R77,=236
01420          STMD R74,=KYIDLE  
01430          RTN  
01440 RTNRTN   LDB  R34,=236
01450          STBD R34,=KYIDLE  
01460          JSB  =CLEAR.  
01470          RTN  
01480 ! 
01490 !  --------------------------------------------------------
01500 ! 
01510 CREAT#   PUBD R43,+R6
01520          JSB  =STREX+  
01530          JEZ  ERROR!  
01540          JSB  =DMNDCR  
01550 THER+    POBD R55,-R6
01560 THERE    LDM  R56,=21,371
01570          STMI R55,=PTR2-   
01580          RTN  
01590 ERROR!   POBD R43,-R6
01600          JSB  =ERROR+  
01610          BYT  88D
01620 ! 
01630 !  ---------------------------------------------------------
01640 !  Revision Date Runtim
01650 !  ---------------------
01660 ! 
01670          BYT  0,56
01680 REV.     BIN  
01690          LDM  R43,=8D,0
01700          DEF  DATE    
01710          BYT  0
01720          ADMD R45,=BINTAB  
01730          PUMD R43,+R12
01740          RTN  
01750          ASC  "18/72/70"
01760 DATE     BSZ  0
01770 ! 
01780 ! 
01790 ! 
01800 !  --------------------------------------------------------
01810 !  KYIDLE Service Routin
01820 !  ---------------------
01830 KEYIN    BIN  
01840          PUMD R75,+R6
01850          LDBD R75,=SVCWRD  
01860          JEV  NEWKEY  
01870          POMD R75,-R6
01880          RTN  
01890 NEWKEY   CLM  R75
01900          LDBD R76,=KEYSTS  
01910          ANM  R76,=10,0
01920          LDB  R75,R76
01930          LDMD R76,=BINTAB  
01940          STBD R75,X76,SHIFT   
01950          POMD R75,-R6
01960          RTN  
01970 !  --------------------------------------------------------
01980 !  Create Form Runtime Rou
01990 !  -----------------------
02000 ! 
02010          BYT  241
02020 CREAT.   BIN  
02030          LDMD R14,=BINTAB  
02040          POMD R45,-R12
02050          STMD R45,=PTR2    
02060          POMD R36,-R12
02070          STMD R36,X14,FNAMEL  
02080          LDM  R46,=FNAME   
02090          ADM  R46,R14
02100 GETNAM   LDBI R32,=PTR2-   
02110          PUBD R32,-R46
02120          DCM  R36
02130          JNZ  GETNAM  
02140 ! 
02150 ! 
02160          JSB  X14,INITAL  
02170          JSB  X14,CLEAR   
02180          JSB  X14,KBD     
02190          JSB  X14,RTNRTN  
02200          JSB  =EOJ2    
02210 ! 
02220          RTN  
02230 !                                     --------------------
02240 !                                     END OF CREATE RUNTIM
02250 !  --------------------------------------------------------
02260 !  Space Fill Routin
02270 !  --------------------
02280 SPILL    LDMD R14,=BINTAB      !  Puts Blanks In Form Buffer
02290          LDB  R23,=3           ! 
02300          LDM  R36,R76          !  R76 = Starting CRT Position
02310          ADM  R36,R14          !  R56 = Number of Blanks
02320          ADM  R36,=FORM        ! 
02330          PUMD R76,+R6          ! 
02340          JSB  =ZROMEM          !  NOTE: Does Not Paint The CRT
02350          POMD R76,-R6          ! 
02360          RTN                   ! 
02370 ! 
02380 !  ---------------------------------------------------------
02390 !  Column 1 Positionin
02400 !  ----------------------
02410 ! 
02420 COLONE   LDMD R26,=CRTBYT  
02430          JSB  =COLUMN  
02440          SBM  R26,R66
02450          RTN  
02460 ! 
02470 ! 
02480 !  --------------------------------------------------------
02490 !  Clear Screen Routin
02500 !  ----------------------
02510 ! 
02520 CLEAR    LDMD R14,=BINTAB      !  Clears Form and Blanks CRT
02530          JSB  =CRTWPO          ! 
02540          CLM  R34              ! 
02550          JSB  =SAD1            ! 
02560          CLM  R76              ! 
02570          JSB  =BYTCRT          ! 
02580          LDM  R56,=PAGETWO 
02590          ICM  R56
02600          JSB  X14,SPILL        ! 
02610          JSB  X14,PAINT        ! 
02620          JSB  =CRTUNW          ! 
02630          RTN                   ! 
02640 !  --------------------------------------------------------
02650 !  CRT Painting Routin
02660 !  -------------------
02670 PAINT    LDM  R36,=PAGE    
02680 PLINE    SBM  R36,R76
02690          ICM  R36
02700          LDM  R26,R76
02710          ADM  R26,R14
02720          ADM  R26,=FORM    
02730 PAINT+   POBD R32,+R26
02740          JSB  =CHKSTS  
02750          STBD R32,=CRTDAT  
02760          DCM  R36
02770          JNZ  PAINT+  
02780          LDBD R37,X14,LABON   
02790          JZR  PAINTRTN
02800          CLB  R37
02810          STBD R37,X14,LABON   
02820          JSB  X14,K226    
02830 PAINTRTN RTN  
02840 ! 
02850 !  --------------------------------------------------------
02860 !  Turn Off Insert Mod
02870 !  -------------------
02880 ! 
02890 OFFINS   CLB  R65
02900          STBD R65,=EDMOD2  
02910 ANYRTN   RTN  
02920 ! 
02930 ! 
02940 !  --------------------------------------------------------
02950 !  KBD INPUT SUBROUTIN
02960 !  -------------------
02970 ! 
02980 KBD      BIN  
02990          CLM  R76              ! 
03000          JSB  =BYTCRT  
03010          JSB  =EOJ2    
03020 KEYLO+   JSB  =CURS    
03030          LDBD R0,=EDMOD2  
03040          JZR  COOLIT  
03050          JSB  =LTCUR.  
03060          JSB  =CURS    
03070          JSB  =RTCUR.  
03080 COOLIT   JSB  =COUNTK          ! 
03090          CLB  R64
03100          CLM  R56
03110 KEYLOP   DCM  R56
03120          JPS  NORMAL  
03130          LDM  R56,=0,25
03140          NCB  R64
03150          JZR  ON      
03160          JSB  =DECUR2  
03170          JMP  NORMAL  
03180 ON       JSB  =CURS    
03190          LDBD R0,=EDMOD2  
03200          JZR  NORMAL  
03210          JSB  =LTCUR.  
03220          JSB  =CURS    
03230          JSB  =RTCUR.  
03240 NORMAL   LDBD R32,=SVCWRD  
03250          JEV  KEYLOP           ! 
03260          JSB  =DECUR2          ! 
03270          CLM  R32
03280          LDBD R32,=KEYHIT      !  Get Key Code
03290          JPS  ECOCHR  
03300          CMB  R32,=234         !  Check For Softkey 7 (EXIT)
03310          JNZ  NOEXIT  
03311          LDB  R23,=40
03312          LDBD R22,=CRTSTS  
03313          ORB  R22,R23
03314          XRB  R22,R23
03315          STBD R22,=CRTSTS  
03316          RTN  
03320 NOEXIT   JSB  X14,CTRL    
03330          JMP  KEYLO+  
03340 ECOCHR   JSB  X14,ECHO    
03350          JMP  KEYLO+  
03360 ! 
03370 !  --------------------------------------------------------
03380 !  CRT Echo Routin
03390 !  -------------------
03400 ECHO     LDBD R65,=EDMOD2  
03410          JZR  REPLAC  
03420          STB  R32,R70
03430          JSB  X14,COLONE  
03440          ADM  R26,=LINE        !  LETS TRY THIS *******************
03450          STM  R26,R36
03460          STM  R26,R24
03470          STM  R26,R22
03480          DCM  R24
03490          LDMD R66,=CRTBYT  
03500          SBM  R22,R66
03510          LDMD R66,=BINTAB  
03520          ADM  R66,=FORM    
03530          ADM  R24,R66
03540          ADM  R26,R66
03550          JSB  =MOVDN   
03560          LDMD R76,=CRTBYT  
03570          JSB  X14,PLINE   
03580          DRP  R76
03590          JSB  =BYTCRT  
03600          LDB  R32,R70
03610 ! 
03620 ! 
03630 REPLAC   JSB  =CHKSTS  
03640          STBD R32,=CRTDAT  
03650          LDMD R66,=CRTBYT  
03660          LDMD R56,X14,EFORM   
03670          CMM  R66,R56
03680          JNC  ECHO-   
03690          STMD R66,X14,EFORM   
03700 ECHO-    ADMD R66,=BINTAB  
03710          STBD R32,X66,FORM    
03720          JSB  =RTCUR.  
03730          RTN  
03740 ! 
03750 !  --------------------------------------------------------
03760 !  Control Func. Directo
03770 !  ---------------------
03780 ! 
03790 ! 
03800 ! 
03810 CTRL     LDMD R14,=BINTAB  
03820          SBM  R32,=200,0
03830          LLM  R32
03840          ADM  R32,R14
03850          LDMD R32,X32,KEYTAB  
03860          ADM  R32,R14
03870          JSB  X32,ZERO    
03880          RTN  
03890 ! 
03900 !  --------------------------------------------------------
03910 !  CONTROL KEY BRANCH TABL
03920 !  -----------------------
03930 ! 
03940 KEYTAB   DEF  SOFT-1           !  200 - Soft Key 1
03950          DEF  SOFT-2           !  201 - Soft Key 2
03960          DEF  SOFT-3           !  202 - Soft Key 3
03970          DEF  SOFT-4           !  203 - Soft Key 4
03980          DEF  SOFT-8           !  204 - Soft Key 8
03990          DEF  SOFT-9           !  205 - Soft Key 9
04000          DEF  SOFT-10          !  206 - Soft Key 10
04010          DEF  SOFT-11          !  207 - Soft Key 11
04020          DEF  K210             !  210 - Delete Character
04030          DEF  K211             !  211 - Clear Screen
04040          DEF  K212             !  212 -
04050          DEF  IGNORE           !  213 - Reset
04060          DEF  IGNORE           !  214 - Init
04070          DEF  IGNORE           !  215 - Run
04080          DEF  IGNORE           !  216 - Pause
04090          DEF  IGNORE           !  217 - Cont
04100          DEF  IGNORE           !  220 - Step
04110          DEF  IGNORE           !  221 - Roll Up
04120          DEF  IGNORE           !  222 - Test
04130          DEF  SOFT-14          !  223 - Soft Key 14
04140          DEF  IGNORE           !  224 - List
04150          DEF  IGNORE           !  225 - Plist
04160          DEF  K226             !  226 - Key Label
04170          DEF  IGNORE           !  227 -
04180          DEF  IGNORE           !  230 -
04190          DEF  K231             !  231 - Backspace
04200          DEF  K232             !  232 - Endline
04210          DEF  K233             !  233 - Fast Backspace
04220          DEF  SOFT-7           !  234 - Soft Key 7
04230          DEF  K235             !  235 - Clear Line
04240          DEF  K236             !  236 - Insert/Replace
04250          DEF  K237             !  237 - Left Cursor
04260          DEF  K240             !  240 - E
04270          DEF  SOFT-5           !  241 - Soft Key 5
04280          DEF  SOFT-6           !  242 - Soft Key 6
04290          DEF  K243             !  243 - Up Cursor
04300          DEF  K244             !  244 - Down Cursor
04310          DEF  SOFT-12          !  245 - Soft Key 12
04320          DEF  IGNORE           !  246 - Result
04330          DEF  IGNORE           !  247 -
04340          DEF  K250             !  250 - Alpha/Graphics
04350          DEF  IGNORE           !  251 - Roll Down
04360          DEF  K252             !  252 - Right Cursor
04370          DEF  IGNORE           !  253 -
04380          DEF  SOFT-13          !  254 - Soft Key 13
04390          DEF  IGNORE           !  255 - Trace/Normal
04400 !  --------------------------------------------------------
04410 ! 
04420 ! 
04430 !   =====================================================
04440 !  | CONTROL ROUTINE SECTION (CURSOR, FIELDS, STORE, ETC) 
04450 !   =====================================================
04460 ! 
04470 ! 
04480 ! 
04490 !  --------------------------------------------------------
04500 !  SOFTKEY DEFINITION
04510 !  ----------------------
04520 ! 
04530 SOFT-1   BIN                   !  Input/Output Field
04540          LDMD R14,=BINTAB  
04550          LDB  R32,=240
04560          JSB  X14,ECHO    
04570          RTN  
04580 ! 
04590 ! 
04600 ! 
04610 !  --------------------------------------------------------
04620 ! 
04630 SOFT-2   JSB  X14,KEY-02       !  Insert Line Routine
04640          RTN  
04650 ! 
04660 !  --------------------------------------------------------
04670 ! 
04680 SOFT-3   JSB  X14,KEY-03       !  Delete Line Routine
04690          RTN  
04700 ! 
04710 !  --------------------------------------------------------
04720 ! 
04730 ! 
04740 SOFT-4   BIN                   !  Page Size Toggle
04750          LDBD R37,=CRTSTS  
04760          ANM  R37,=10
04770          JZR  SIZE24  
04780          JSB  =PAGES1  
04790          JMP  SIZERTN 
04800 SIZE24   JSB  =PAGES2  
04810 SIZERTN  CLM  R76
04820          JSB  =BYTCRT  
04830          JSB  X14,PAINT   
04840          RTN  
04850 ! 
04860 !  --------------------------------------------------------
04870 ! 
04880 SOFT-5   JSB  X14,KEY-05       !  Store Form Routine
04890          RTN  
04900 ! 
04910 !  --------------------------------------------------------
04920 ! 
04930 SOFT-6   BIN                   !  INVERT THE SCREEN
04940          LDBD R22,=CRTSTS  
04950          LDB  R23,=40
04960          XRB  R23,R22
04970          STBD R23,=CRTSTS  
04980          LDBD R22,X14,FSTART  
04981          LDB  R23,=1
04982          XRB  R23,R22
04983          STBD R23,X14,FSTART  
04984          RTN  
04990 ! 
05000 !  --------------------------------------------------------
05010 ! 
05020 SOFT-7   RTN                   !  Keycode Trapped In Input Loop
05030 ! 
05040 !  --------------------------------------------------------
05050 ! 
05060 SOFT-8   RTN  
05070 ! 
05080 !  --------------------------------------------------------
05090 ! 
05100 SOFT-9   RTN  
05110 ! 
05120 !  --------------------------------------------------------
05130 ! 
05140 SOFT-10  RTN  
05150 ! 
05160 !  --------------------------------------------------------
05170 ! 
05180 SOFT-11  RTN  
05190 ! 
05200 !  --------------------------------------------------------
05210 ! 
05220 SOFT-12  RTN  
05230 ! 
05240 !  --------------------------------------------------------
05250 ! 
05260 SOFT-13  RTN  
05270 ! 
05280 !  --------------------------------------------------------
05290 ! 
05300 SOFT-14  RTN  
05310 ! 
05320 !  --------------------------------------------------------
05330 !  KEY CODE 21
05340 !  -------------------
05350 ! 
05360 K212     RTN  
05370 ! 
05380 !  --------------------------------------------------------
05390 !  Clear Screen Routin
05400 !  -------------------
05410 ! 
05420 K211     JSB  X14,CLEAR   
05430          JSB  X14,OFFINS  
05440          RTN  
05450 ! 
05460 !  --------------------------------------------------------
05470 K226     BIN  
05480          LDMD R14,=BINTAB  
05490          LDMD R36,=CRTBYT  
05500          STMD R36,X14,SAVCRT  
05510          LDM  R56,=260,004
05520          LDBD R37,=CRTSTS  
05530          ANM  R37,=10
05540          TSM  R37
05550          JZR  GOLAB   
05560          LDM  R56,=060,007
05570 GOLAB    DRP  R56
05580          JSB  =BYTCRT  
05590          LDBD R37,X14,LABON   
05600          JNZ  KLOFF   
05610          ICB  R37
05620          STBD R37,X14,LABON   
05630          LDM  R36,=120,0
05640          LDM  R26,=KEY$0   
05650          ADM  R26,R14
05660 KLON     POBD R32,+R26
05670          LDB  R33,=200
05680          XRB  R32,R33
05690          JSB  =CHKSTS  
05700          STBD R32,=CRTDAT  
05710          DCM  R36
05720          JNZ  KLON    
05730          JMP  RESTORE 
05740 KLOFF    LDMD R76,=CRTBYT  
05750          CLB  R37
05760          STBD R37,X14,LABON   
05770          LDM  R36,R76
05780          ADM  R36,=120,0
05790          JSB  X14,PLINE   
05800 RESTORE  LDMD R36,X14,SAVCRT  
05810          JSB  =BYTCRT  
05820          RTN  
05830 ! 
05840 KEY$0    ASP  " "
05850          ASP  " "
05860 KEY$1    ASP  "I/O  FIELD "
05870 KEY$2    ASP  " INS LINE  "
05880 KEY$3    ASP  " DEL LINE  "
05890 KEY$4    ASP  "PAGE  SIZE "
05900 KEY$5    ASP  "STORE FORM "
05910 KEY$6    ASP  "           "
05920 KEY$7    ASP  " END PROG  "
05930          ASP  " "
05940          ASP  " "
05950 ! 
05960 !  --------------------------------------------------------
05970 !  Backspace Key Routin
05980 !  --------------------
05990 ! 
06000 K231     JSB  =LTCUR.  
06010          RTN  
06020 ! 
06030 !  --------------------------------------------------------
06040 !  Endline Key Routin
06050 !  --------------------
06060 ! 
06070 K232     JSB  =DNCUR.  
06080          JSB  X14,COLONE  
06090          JSB  =BYTCRT  
06100          JSB  X14,OFFINS  
06110          RTN  
06120 ! 
06130 !  --------------------------------------------------------
06140 !  Shift Backspace Routin
06150 !  ----------------------
06160 ! 
06170 K233     JSB  =LTCUR.  
06180          RTN  
06190 ! 
06200 !  --------------------------------------------------------
06210 !  KEY CODE 23
06220 !  ----------------------
06230 ! 
06240 K235     RTN  
06250 ! 
06260 ! 
06270 !  --------------------------------------------------------
06280 !  Left Cursor Routin
06290 !  ----------------------
06300 ! 
06310 K237     JSB  =LTCUR.  
06320          RTN  
06330 ! 
06340 !  --------------------------------------------------------
06350 !  Right Cursor Routin
06360 !  ----------------------
06370 ! 
06380 K252     JSB  =RTCUR.  
06390          RTN  
06400 ! 
06410 !  --------------------------------------------------------
06420 !  Delete Line Routin
06430 !  -------------------
06440 ! 
06450 KEY-03   LDMD R14,=BINTAB  
06460          JSB  X14,COLONE  
06470          JSB  =BYTCRT  
06480          LDMD R66,=CRTBYT  
06490          LDM  R24,R66
06500          LDM  R26,R66
06510          ADM  R24,=LINESIZE
06520          LDM  R22,=PAGETWO 
06530          SBM  R22,R24
06540          ICM  R22
06550          LDM  R66,R14
06560          ADM  R66,=FORM    
06570          ADM  R24,R66
06580          ADM  R26,R66
06590          JSB  =MOVUP   
06600          LDMD R76,=CRTBYT  
06610          JSB  X14,PAINT   
06620          JSB  X14,OFFINS  
06630          RTN  
06640 ! 
06650 !  --------------------------------------------------------
06660 !  Insert Line Routin
06670 !  -------------------
06680 ! 
06690 KEY-02   LDMD R14,=BINTAB  
06700          JSB  X14,COLONE  
06710          JSB  =BYTCRT  
06720          LDMD R66,=CRTBYT  
06730          LDM  R22,=PAGETWO-
06740          LDM  R24,R22
06750          LDM  R26,R22
06760          SBM  R22,R66
06770          ICM  R22
06780          SBM  R24,=LINESIZE
06790          LDM  R66,R14
06800          ADM  R66,=FORM    
06810          ADM  R24,R66
06820          ADM  R26,R66
06830          JSB  =MOVDN   
06840          LDM  R56,=LINESIZE
06850          LDMD R76,=CRTBYT  
06860          JSB  X14,SPILL   
06870          LDMD R76,=CRTBYT  
06880          JSB  X14,PAINT   
06890          JSB  X14,OFFINS  
06900          RTN  
06910 ! 
06920 !  --------------------------------------------------------
06930 ! 
06940 K240     RTN  
06950 ! 
06960 !  --------------------------------------------------------
06970 !  Up Cursor Routin
06980 !  -------------------
06990 ! 
07000 K243     LDBD R77,X14,SHIFT   
07010          JNZ  HOME    
07020          JSB  =UPCUR.  
07030          JSB  X14,OFFINS  
07040          RTN  
07050 HOME     CLM  R76
07060          JSB  =BYTCRT  
07070          JSB  X14,OFFINS  
07080          RTN  
07090 ! 
07100 !  --------------------------------------------------------
07110 !  Down Cursor Routin
07120 !  -------------------
07130 ! 
07140 K244     JSB  =DNCUR.  
07150          JSB  X14,OFFINS  
07160          RTN  
07170 ! 
07180 !  --------------------------------------------------------
07190 !  Insert/Replace Toggl
07200 !  --------------------
07210 ! 
07220 K236     LDMD R14,=BINTAB  
07230          LDBD R65,=EDMOD2  
07240          NCB  R65
07250          STBD R65,=EDMOD2  
07260          RTN  
07270 ! 
07280 ! 
07290 !  --------------------------------------------------------
07300 !  Delete Character Routin
07310 !  -----------------------
07320 ! 
07330 K210     STB  R32,R70
07340          JSB  X14,COLONE  
07350          STM  R#,R22
07360          ADM  R22,=LINE    
07370          STM  R22,R36
07380          STM  R22,R56
07390          LDMD R26,=CRTBYT  
07400          STM  R26,R24
07410          ICM  R24
07420          SBM  R22,R26
07430          LDM  R66,R14
07440          ADM  R66,=FORM    
07450          ADM  R24,R66
07460          ADM  R26,R66
07470          JSB  =MOVUP   
07480          ADM  R56,=FORM    
07490          ADM  R56,R14
07500          LDB  R55,=40
07510          STBD R55,R56
07520          LDMD R76,=CRTBYT  
07530          JSB  X14,PLINE   
07540          DRP  R76
07550          JSB  =BYTCRT  
07560          LDB  R32,R70
07570          RTN  
07580 ! 
07590 !  --------------------------------------------------------
07600 ! 
07610 K250     RTN  
07620 ! 
07630 !  --------------------------------------------------------
07640 !  Store Form Routin
07650 !  -----------------
07660 ! 
07670 KEY-05   LDMD R14,=BINTAB  
07680          LDBD R37,=CRTSTS  
07690          ANM  R37,=10
07700          STBD R37,X14,PAGMOD  
07710          LDMD R36,X14,FNAMEL  
07720          LDM  R45,=FNAME   
07730          BYT  0
07740          ADMD R45,=BINTAB  
07750 !         ADM R45,R36            ! ADD NAME STR LENGTH TO ADDRESS PTR
07760 !         CLB R4
07770          PUMD R36,+R12
07780          PUMD R45,+R12
07790          JSB  =ROMJSB  
07800          DEF  MSIN    
07810          VAL  MSROM#  
07820          LDM  R26,R6
07830          ADM  R26,=7,0
07840          STMD R26,=SAVER6  
07850          JSB  =ROMJSB  
07860          DEF  TAPDS+  
07870          VAL  MSROM#  
07880          JEZ  STO-OK  
07890          LDB  R30,=MSROM#  
07900          STBD R30,=ERROM#  
07910          JSB  =ERROR+  
07920          BYT  126D
07930          RTN  
07940 STO-OK   LDB  R30,=FRMTYP  
07950          STBD R30,=FILTYP  
07960          LDMD R45,=NXTMEM  
07970          STMD R45,=STSIZE  
07980          LDM  R76,=PAGESIZE
07990          ADMD R76,=BINTAB  
08000          ADM  R76,=FORM    
08010 SIZLOP   POBD R32,-R76
08020          CMB  R32,=40
08030          JZR  SIZLOP  
08040          ICM  R76
08050          STM  R76,R56
08060          LDMD R14,=BINTAB  
08070          SBM  R56,R14
08080          SBM  R56,=FORM    
08090          STMD R56,X14,EFORM   
08100 ! 
08110 ! 
08120 !  --------------------------------------------------------
08130 !  Find Field
08140 !  -----------
08150 ! 
08160          LDM  R66,=FORM    
08170          ADMD R66,=BINTAB  
08180          CLM  R46              !  Field Counter
08190          CLM  R56              !  Screen Address Pointer
08200 ! 
08210 FINDIT   CMM  R66,R76          !  Make Sure You're Still On Form
08220          JCY  STORE   
08230          POBD R32,+R66         !  Get 1 Character
08240          CMB  R32,=240         !  Check For Inverse Space
08250          JNZ  FINDIT  
08260          LDM  R36,=FIELD   
08270          ADMD R36,=BINTAB  
08280          ADM  R36,R46
08290          LDM  R56,R66
08300          SBMD R56,=BINTAB  
08310          SBM  R56,=FORM    
08320          DCM  R56
08330          STMD R56,R36
08340 ! 
08350 !  ----------------------------------------------------------
08360 !  Get Size Of Fiel
08370 !  -------------------
08380 ! 
08390          CLM  R26              !  Field Length Counter
08400 INFLD    ICM  R26
08410          CMM  R66,R76          !  Make Sure We're Still On Form
08420          JCY  INFLD-  
08430          POBD R32,+R66
08440          CMB  R32,=240
08450          JZR  INFLD   
08460 ! 
08470 INFLD-   LDM  R36,=LENGTH  
08480          ADMD R36,=BINTAB  
08490          ADM  R36,R46
08500          STMD R26,R36
08510          ADM  R46,=2,0
08520          JMP  FINDIT  
08530 ! 
08540 STORE    LDM  R36,=NUMFLD  
08550          ADMD R36,=BINTAB  
08560          LDM  R30,R46
08570          LRM  R31
08580          STBD R30,R36
08590          LDM  R55,=FSTART  
08600          BYT  0
08610          ADMD R55,=BINTAB  
08620          LDM  R45,=EFORM+  
08630          BYT  0
08640          ADMD R45,=BINTAB  
08650          STMD R55,=LSTDAT  
08660          LDM  R55,R45
08670 ! 
08680          JSB  =ROMJSB  
08690          DEF  STORB%  
08700          VAL  MSROM#  
08710          LDMD R14,=BINTAB  
08720          CLM  R76
08730          JSB  =BYTCRT  
08740          JSB  X14,PAINT   
08750 STORTN   RTN  
08760 ! 
08770 !  --------------------------------------------------------
08780 ! 
08790 ! 
08800 !  --------------------------------------------------------
08810 !  Ignore Key Routin
08820 !  -------------------
08830 ! 
08840 IGNORE   RTN  
08850 ! 
08860 !                                   ----------------------
08870 !                                   END OF CONTROL ROUTINE
08880 !  -------------------------------------------------------
08890 ! 
08900 ! 
08910 ! 
08920 BFORM    BSZ  2
08930 FNAMEL   BSZ  2
08940 SHIFT    BSZ  1
08950 SAVCRT   BSZ  2
08960 LABON    BSZ  1
08970 !  --------------------------------------------------------
08980 !  Screen Size Dependen
08990 !  --------------------
09000 ! 
09010 ALPHA    EQU  7777             ! 
09020 PAGESIZE EQU  3600             ! 
09030 PAGE     EQU  3577
09040 PAGETWO  EQU  7377
09050 PAGETWO- EQU  7257
09060 LINESIZE EQU  120              ! 
09070 LINE     EQU  117
09080 BEGLIN   EQU  7700
09090 NUMLIN   EQU  20
09100 FSTART   BSZ  30
09110 FNAME    BSZ  0
09120 PAGMOD   BSZ  1
09130 NUMFLD   BSZ  1
09140 FIELD    BSZ  400
09150 LENGTH   BSZ  400
09160 FORM     BSZ  3600
09170 EFORM    BSZ  2
09180 !                                       ------------------
09190 !                                       END OF SCREEN EQU'
09200 !  --------------------------------------------------------
09210 EFORM+   BSZ  3600
09220          FIN                   ! 
