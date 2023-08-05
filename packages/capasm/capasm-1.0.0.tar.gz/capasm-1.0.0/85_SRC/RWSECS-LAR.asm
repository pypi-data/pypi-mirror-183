0020        NAM  RWSEC            !  9/19/81 L.W
0030        DEF  RUNTIM
0040        DEF  ASCIIS
0050        DEF  PARSE 
0060        DEF  ERMSG 
0070        DEF  INIT  
0080 PARSE  BYT  0,0
0090        DEF  RSECT,
0100        DEF  WSECT,
0110 RUNTIM BYT  0,0
0120        DEF  RSECT.
0130        DEF  WSECT.
0140        BYT  377,377
0150 ASCIIS ASP  "READSECTOR"
0160        ASP  "WRITESECTOR"
0170        BYT  377
0180 ERMSG  BYT  200,200,200,200,200,200,200,200,200
0190        ASP  "NO M.S. ROM!"
0200        ASP  "STRING TOO SHORT!"
0210        BYT  377
0220 INIT   LDBD R34,=ROMFL 
0230        CMB  R34,=3           !  LOADBIN?
0240        JZR  MSROM?
0250        RTN  
0260 MSROM? LDM  R34,=ROMTAB
0270 NXTROM POMD R36,+R34
0280        CMB  R36,=377         !  END OF TABLE?
0290        JZR  MSERR 
0300        CMB  R36,=MSROM#
0310        JNZ  NXTROM
0320        RTN                   !  M.S. ROM IS IN
0330 MSERR  JSB  =ERROR+          !  "NO M.S. ROM!"
0340        BYT  366
0350 !  READSECTOR <sector#> , <string variable> , <error flag
0360 !  the string variable must be >= 256 chars lon
0370 !  reads a sector from the disk to the string variable
0380 !  if an error occurs in the read, the error flag will be a 1, else it will be a 0
0390 !  WRITESECTOR <sector#> , <string expression> , <error flag
0400 !  the string expression must be >= 256 chars lon
0410 !  for both, the error flag must be a real 
0420 !  writes a sector from the string expression to the disk
0430 !  if an error occurs in the write, the error flag will be a 1, else it will be a 0
0440 RSECT, PUBD R43,+R6
0450        JSB  =NUMVA+
0460        JSB  =GETCMA
0470        JSB  =STRREF
0480        JSB  =GETCMA
0490        JSB  =REFNUM
0500 DONPAR POBD R47,-R6
0510        LDB  R45,=371
0520        PUMD R45,+R12
0530        RTN  
0540 WSECT, PUBD R43,+R6
0550        JSB  =NUMVA+
0560        JSB  =GETCMA
0570        JSB  =STREXP
0580        JSB  =GETCMA
0590        JSB  =REFNUM
0600        JMP  DONPAR
0610        BYT  241
0620 RSECT. BIN  
0630        POMD R44,-R12         !  GET ERROR FLAG VARIABLE
0640        PUMD R44,+R6          !  SAVE FOR LATER
0650        POMD R30,-R12         !  START ADDRESS
0660        POMD R34,-R12         !  LENGTH
0670        POMD R32,-R12         !  BASE ADDRESS ( THROWN AWAY )
0680        CMM  R34,=0,1         !  256 BYTES LONG OR MORE?
0690        JNC  TOOSM            !  JIF NO
0700        JSB  =ONEB            !  GET SECTOR #
0710        LDM  R32,R46          !  PUT IN RIGHT REGISTER
0720        LDMD R0,=BINTAB
0730        JSB  X0,INITMS        !  SET UP FOR M.S. ROM CALL
0740        JSB  =ROMJSB
0750        DEF  GETSEC           !  GET A SECTOR
0760        VAL  MSROM#
0770 SECCOM CLM  R40              !  0 FOR LATER => NO ERROR
0780        CMB  R17,=300         !  ANY ERRORS?
0790        JNC  MSSUCC           !  JIF OK
0800        ANM  R17,=37          !  CLEAR ERRORS
0810        STBD R40,=ERRORS
0820        STBD R40,=ERRROM
0830        LDB  R47,=20          !  1=> ERROR
0840 MSSUCC POMD R34,-R6          !  GET NAME BLOCK ( THROW AWAY )
0850        POMD R34,-R6          !  GET ADDRESS
0860        STMD R40,R34          !  PUT FLAG IN LOCATION
0870        RTN  
0880 TOOSM  POMD R40,-R12         !  CLEAN OFF STACKS
0890        POMD R44,-R6
0900        JSB  =ERROR+          !  "STRING TOO SHORT!"
0910        BYT  365
0920        BYT  241
0930 WSECT. BIN  
0940        POMD R44,-R12         !  GET ERROR FLAG VARIABLE
0950        PUMD R44,+R6          !  SAVE FOR LATER
0960        POMD R30,-R12         !  GET START ADDRESS
0970        POMD R34,-R12         !  LENGTH
0980        CMM  R34,=0,1         !  256 BYTES LONG OR MORE ?
0990        JNC  TOOSM            !  JIF NO
1000        JSB  =ONEB            !  GET SECTOR #
1010        LDM  R32,R46          !  PUT IN RIGHT REGISTER
1020        LDMD R0,=BINTAB
1030        JSB  X0,INITMS        !  SETUP FOR M.S. ROM CALL
1040        JSB  =ROMJSB
1050        DEF  PUTSEC           !  WRITE A SECTOR
1060        VAL  MSROM#
1070        JMP  SECCOM
1080 INITMS LDMD R14,=MSBASE      !  INIT FOR M.S. ROM
1090        LDM  R34,=GINTEN
1100        STMD R34,=TINTEN
1110        CLB  R34
1120        STBD R34,=SCRTYP
1130        LDM  R34,R6           !  GET STACK POINTER
1140        ADM  R34,=5,0         !  POINT TO WHERE RETURN ADDR WILL BE AFTER ROMJSB
1150        STMD R34,=SAVER6
1160        RTN  
1170 ROMFL  DAD  101231
1180 ROMTAB DAD  101235
1190 MSROM# EQU  320
1200 ERROR+ DAD  6611
1210 NUMVA+ DAD  12407
1220 GETCMA DAD  13414
1230 STRREF DAD  13753
1240 REFNUM DAD  17025
1250 STREXP DAD  13626
1260 GETSEC DAD  77253
1270 PUTSEC DAD  77163
1280 ONEB   DAD  56113
1290 GINTEN DAD  177400
1300 TINTEN DAD  101071
1310 SAVER6 DAD  101174
1320 MSBASE DAD  102540
1330 SCRTYP DAD  101120
1340 BINTAB DAD  101233
1350 ROMJSB DAD  4776
1360 ERRORS DAD  100070
1370 ERRROM DAD  100065
1380        FIN  
