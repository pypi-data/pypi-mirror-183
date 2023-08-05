0010        NAM  GFSORT
0020        DEF  RUNTIM
0030        DEF  TOKS  
0040        DEF  PARSE 
0050        DEF  ERMSG 
0060        DEF  INIT  
0070 RUNTIM BYT  0,0
0080        DEF  R1    
0090        DEF  R2    
0100 PARSE  BYT  0,0
0110        DEF  P1    
0120        DEF  P1    
0130        BYT  377,377
0140 TOKS   ASP  "SORT"
0150        ASP  "UPCSORT"
0160        BYT  377,377
0170 ERMSG  BYT  260,261,262,263,264,265,266,267,270,271,272
0180        ASP  "Element length = 0"
0190        ASP  "Element length > length of string"
0200        ASP  "Last column > size of element"
0210        ASP  "First column > last column"
0220        ASP  "First column = 0"
0230        BYT  377
0240 INIT   LDMD R56,=BINTAB
0250        STMD R56,=FWBIN 
0260        RTN  
0270 P1     LDB  R14,=371
0280        PUMD R40,+R6
0290        LDB  R35,=3
0300        JSB  =GETPA$
0310        POMD R70,-R6
0320        PUBD R73,+R12
0330        PUBD R73,+R12
0340        RTN  
0350        BYT  241
0360 R1     CLB  R14
0370        JMP  L1    
0380        BYT  241
0390 R2     CLB  R14
0400        ICB  R14
0410 L1     PUBD R#,+R6
0420        JSB  =TWOB  
0430        PUMD R46,+R6
0440        PUMD R56,+R6
0450        JSB  =ONEB  
0460        POMD R30,-R12
0470        POMD R32,-R12
0480        POMD R20,-R6
0490        POMD R22,-R6
0500        POBD R14,-R6
0510        CLE  
0520        JZR  L2    
0530        ICE  
0540 L2     LDM  R24,R46
0550        JZR  L3    
0560        CMM  R32,R24
0570        JNC  L4    
0580        CMM  R24,R22
0590        JNC  L5    
0600        DCM  R20
0610        JNC  L6    
0620        SBM  R22,R20
0630        JNC  L7    
0640        JZR  L7    
0650        ADM  R32,R30
0660        SBM  R32,R24
0670        SBM  R32,R24
0680        STM  R32,R26
0690        LDM  R70,R20
0700        LDM  R60,R30
0710        JMP  L8    
0720 L3     JSB  =ERROR+
0730        BYT  364
0740 L4     JSB  =ERROR+
0750        BYT  363
0760 L5     JSB  =ERROR+
0770        BYT  362
0780 L7     JSB  =ERROR+
0790        BYT  361
0800 L6     JSB  =ERROR+
0810        BYT  360
0820 L8     CLB  R66
0830        LDM  R22,R60
0840        STM  R22,R64
0850 L16    CMM  R26,R22
0860        JNC  L9    
0870        ADM  R22,R70
0880        STM  R22,R24
0890        ADM  R24,R74
0900        LDM  R32,R72
0910 L15    POBD R37,+R24
0920        POBD R36,+R22
0930        JEZ  L10   
0940        CMB  R37,=141
0950        JNC  L11   
0960        CMB  R37,=173
0970        JCY  L11   
0980        SBB  R37,=40
0990 L11    CMB  R36,=141
1000        JNC  L10   
1010        CMB  R36,=173
1020        JCY  L10   
1030        SBB  R36,=40
1040 L10    CMB  R36,R37
1050        JNC  L12   
1060        JZR  L13   
1070        LDB  R66,=1
1080        LDM  R20,R64
1090        LDM  R22,R64
1100        ADM  R22,R74
1110        LDM  R24,R74
1120 L14    LDBD R30,R20
1130        LDBD R31,R22
1140        PUBD R31,+R20
1150        PUBD R30,+R22
1160        DCM  R24
1170        JNZ  L14   
1180        JMP  L12   
1190 L13    DCB  R32
1200        JNZ  L15   
1210 L12    LDM  R22,R64
1220        ADM  R22,R74
1230        STM  R22,R64
1240        JMP  L16   
1250 L9     TSB  R66
1260        JNZ  L8    
1270        RTN  
1280 BINTAB DAD  101233
1290 FWBIN  DAD  100020
1300 ONEB   DAD  56113
1310 TWOB   DAD  56176
1320 ERROR+ DAD  6611
1330 GETPA$ DAD  14326
1340        FIN  
