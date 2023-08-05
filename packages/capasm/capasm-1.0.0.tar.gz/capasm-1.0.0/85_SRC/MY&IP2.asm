0010 !  MY&IP2 - 2ND PART OF IPBI
0020 !        HED ONKBD RUNTIME COD
0030 ! 
0040 !       ON KBD !( GOTO / GOSUB 
0050 ! 
0060        BYT  241
0070 ONKBD. LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
0080        BIN  
0090        STMD R10,X22,KEYEOL   !   SAVE BASIC.PC TO GOTO/GOSUB
0100        ADM  R10,=3,0         !         SKIP OVER GOTO/GOSUB
0110        LDMD R46,X22,KBD_R    !    \   COMPUTE REAL ADDRESS
0120        STMD R46,X22,KBDADR   !   /   IN KEYBOARD LINK
0130        LDMD R46,X22,KEYRPT   !   GET REPEAT TIME
0140 HOLDLP LDMD R20,=KEYSTS      !      \  WAIT A WHILE
0150        LRB  R20              !               \     OR UNTIL THE
0160        JEV  NOHOLD           !              \    THE KEY IS LET UP
0170        TSM  R46
0180        JZR  HOLDDN           !              /
0190        DCM  R46              !               /
0200        JMP  HOLDLP           !            /
0210 HOLDDN LDM  R46,=377,2       !       \
0220        STMD R46,X22,KEYRPT   !   /  SET REPEAT COUNTER TO MEDIUM
0230        LDBD R26,X22,OLDKEY   !   LOG KEY INTO BUFFER
0240        STBD R#,=GINTDS       !       TURN OFF INTERRUPTS
0250        JSB  X22,LOGKEY
0260 NOHOLD STBD R#,=GINTDS       !       TURN OFF INTERRUPTS
0270        LDB  R46,=TRUE        !        \   ARM FOR EOL SERVICE
0280        STBD R46,X22,KEYSVC   !   /
0290        LDMD R46,X22,KBDCNT   !   \
0300        JZR  SETISR           !                IF SOME KEYCODES ARE IN BUFFER
0310        JSB  X22,LOGONK       !        /      THEN LOG EOL INTERRUPT
0320 SETISR LDMD R44,X22,NEWKEY   !   GET MY KEYBOARD LINK
0330        STMD R44,=KYIDLE      !      PUT INTO SYSTEM KEYBOARD LINK
0340        STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
0350        RTN  
0360 ! 
0370 !       OFF KB
0380 ! 
0390        BYT  241
0400 OFFK.  LDMD R22,=BINTAB      !      SET UP BASE ADDRESS
0410        CLM  R46              !              \ CLEAR OUT GOTO/GOSUB ENTRY
0420        STMD R46,X22,KEYEOL   !   /
0430        STMD R46,X22,KBDCNT   !   SET # CHARS IN BUFFER TO ZERO
0440        LDB  R46,=236         !         \ PUT A DUMMY RETURN INTO
0450        STBD R46,=KYIDLE      !      /    SYSTEM KEYBOARD LINK
0460        RTN  
0470 ! 
0480 !       KBD
0490 ! 
0500        BYT  0,56             !              STRING FUNCTION - NO PARAMETERS
0510 KBD$.  LDMD R22,=BINTAB      !      GET BASE ADDRESS
0520        BIN  
0530        LDMD R20,X22,K_CNV    !    \ GET KBD CONVERSION POINTER
0540        STM  R20,R70          !          /
0550        LDM  R56,=120,0       !       \ RESERVE 80 BYTES
0560        JSB  =RSMEM-          !           /
0570        JEN  CANT+            !             MAKE SURE THERE IS ENOUGH MEMORY
0580        STM  R26,R30          !          SAVE PTR TO RESERVED AREA
0590        STBD R#,=GINTDS       !       DISABLE INTERRUPTS
0600        LDMD R76,X22,KBDCNT   !   GET NUMBER OF CHARACTERS IN BUFFER
0610        STM  R76,R34          !          KEEP A COPY FOR STACK
0620        JZR  K_NOCH           !            IF THERE ARE NO CHARACTERS - DON'T COPY
0630        LDM  R36,=KBDSAV      !      \  GET A POINTER TO THE BUFFER
0640        ADM  R36,R22          !          /
0650 K_LOOP POBD R32,+R36         !         GET CHARACTER FROM BUFFER
0660        JSB  X22,CNVCHR       !        CONVERT CHARACTER
0670        PUBD R32,+R26         !         PUSH CHARACTER INTO RESERVED MEMORY
0680        DCM  R34              !              \  REPEAT UNTIL ALL CHARACTERS
0690        JNZ  K_LOOP           !            /     ARE COPIED
0700 K_NOCH PUMD R76,+R12         !         PUSH LENGTH
0710        PUMD R30,+R12         !         PUSH POINTER TO RESERVED MEMORY
0720        STMD R34,X22,KBDCNT   !   CLEAR THE NUMBER OF CHARACTERS
0730        STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
0740        RTN  
0750 ! 
0760 CANT+  JSB  =ERROR           !            GIVE 'OUT OF MEMORY' ERROR
0770        BYT  19D
0780 ! 
0790 !       FIN
0800 ! 
0810        BYT  30,55            !             NUMERIC FUNCTION - 1 STRING PARAMETER
0820 FIND.  LDMD R22,=BINTAB      !      GET BASE ADDRESS
0830        BIN  
0840        POMD R32,-R12         !         GET STRING ADDRESS
0850        POMD R34,-R12         !         GET STRING LENGTH
0860        JZR  F_NONE           !            IF NO CHARACTERS THEN QUIT
0870        CLM  R46              !              INITIALIZE POSITION INDICATOR
0880 FND_LP ICM  R46              !              INCREMENT POSITION INDICATOR
0890        POBD R20,+R32         !         GET CHARACTER
0900        JNG  F_FND            !             IF UPPER BIT SET - CONDITION FOUND
0910        DCM  R34              !              LENGTH=LENGTH-1
0920        JNZ  FND_LP           !            LOOP UNTIL LENGTH = 0
0930 F_NONE CLM  R46              !              IF CONDITION NOT FOUND - RETURN 0
0940 F_FND  JSB  X22,FNCRTN       !        RETURN THE VALUE
0950        RTN  
0960 ! 
0970 !       CONVERT KBD PAIRS ! <STRING VARIABLE
0980 ! 
0990        BYT  241
1000 KCNVP. CLM  R20              !              CLEAR INDEX INDICATION
1010        JMP  KC_COM
1020 ! 
1030 !       CONVERT KBD INDEX !  <STRING VARIABLE
1040 ! 
1050        BYT  241
1060 KCNVI. LDM  R20,=0,200       !      SET INDEX INDICATION
1070 KC_COM POMD R42,-R12         !         GET STRING INFORMATION
1080        DCM  R46              !          \ SET PTR TO CURRENT LENGTH
1090        DCM  R46              !          /
1100        ANM  R46,=377,177     !   MASK OUT ADDRESS BIT
1110 !                             WHICH IS RECONSTRUCTED IN CNVCH
1120        ORM  R46,R20          !         OR IN INDEX INDICATION
1130 STRCOM LDMD R22,=BINTAB      !      GET BASE ADDRESS
1140        STMD R46,X22,K_CNV    !    STORE KBD CONVERSTION PTR
1150        RTN  
1160 ! 
1170 !       CONVERT KB
1180 ! 
1190        BYT  241
1200 KCNV.  CLM  R46              ! CLEAR KBD CONVERSION PTR
1210        JMP  STRCOM
1220 !        HED SGCLEAR ( SELECTIVE GCLEAR 
1230 ! 
1240 !       SGCLEAR <XMIN>,<XMAX>,<YMIN>,<YMAX
1250 ! 
1260 P.ERR  LDB  R30,=0           !            \ PARAMETER ERROR ROUTINE
1270        JSB  =ERROR+          !           /
1280        BYT  89D
1290 ! 
1300        BYT  241
1310 SGCLR. LDMD R22,=BINTAB      !      GET BASE ADDRESS
1320        JSB  =GRAPH.          !           ENTER GRAPHICS MODE
1330        JSB  =ONEB            !             \
1340        STM  R46,R26          !               YMAX
1350        JNG  P.ERR            !             /
1360        JSB  =ONEB            !             \
1370        STM  R46,R24          !               YMIN
1380        JNG  P.ERR            !             /
1390        JSB  =ONEB            !             \
1400        STM  R46,R32          !               XMAX
1410        JNG  P.ERR            !             /
1420        JSB  =ONEB            !             \
1430        STM  R46,R30          !               XMIN
1440        JNG  P.ERR            !             /
1450 ! 
1460        BIN  
1470        LDBD R21,=PLOTSY      !      GET PEN INFORMATION
1480        NCM  R21              ! COM DATA
1490 ! 
1500        CMM  R32,R30          !           \   IF XMIN>XMAX THEN ERROR
1510        JNC  P.ERR            !             /
1520        CMM  R32,=0,1         !          \   IF XMAX>255  THEN ERROR
1530        JCY  P.ERR            !             /
1540        CMM  R26,R24          !           \   IF YMIN>YMAX THEN ERROR
1550        JNC  P.ERR            !             /
1560        CMM  R26,=300,0       !        \   IF YMAX>191  THEN ERROR
1570        JCY  P.ERR            !             /
1580 ! 
1590        LRM  R30              !               \   XMIN=XMIN/4
1600        LRM  R30              !               /
1610        LRM  R32              !               \   XMAX=XMAX/4
1620        LRM  R32              !               /
1630        ICM  R24              !               \   ADJUST Y ADDRESSES
1640        ICM  R26              !               /
1650 ! 
1660 SG.L.Y LDM  R46,=300,0       !        \   ADDRESS = ( ( 192
1670        SBM  R46,R24          !            \                - Y )
1680        LLM  R46              !                 \               * 64 )
1690        LLM  R46              !                  \
1700        BCD  
1710        LLM  R46              !                  /
1720        BIN                   !                     /
1730        ADM  R46,R30          !            /              + XMIN
1740        ADM  R46,=0,20        !         /               + 4096
1750 SGWAIT LDBD R20,=CRTSTS      !      \  WAIT FOR CRT NOT BUSY
1760        JNG  SGWAIT           !            /
1770        STMD R46,=CRTBAD      !      SET UP STARTING GRAPHICS ADDRESS
1780 ! 
1790        LDM  R34,R30          !           COUNTER = XMIN
1800 SG.L.X LDBD R20,=CRTSTS      !      \  WAIT FOR CRT NOT BUSY
1810        JNG  SG.L.X           !            /
1820        STBD R21,=CRTDAT      !      PUT DOTS INTO 4 BIT CELL
1830        ICM  R34
1840        ICM  R34              !               COUNTER = COUNTER + 1
1850        CMM  R34,R32          !           \  LOOP UNTIL COUNTER > XMAX
1860        JNC  SG.L.X           !            /
1870 ! 
1880        ICM  R24              !               Y = Y + 1
1890        CMM  R24,R26          !           \  LOOP UNTIL Y > YMAX
1900        JNC  SG.L.Y           !            /
1910 ! 
1920        RTN  
1930 !        HED KEYBOARD LINK & IS
1940 ! 
1950 !       NEW KEYBOARD LINK COD
1960 ! 
1970 NEWKEY BYT  316              !               \   JSB =KBDISR
1980 KBDADR DEF  KBDISR           !            /
1990        RTN  
2000 ! 
2010 !       KEYBOARD INTERRUPT SERVICE ROUTIN
2020 ! 
2030 KBDISR STBD R#,=GINTDS       !       DISABLE INTERRUPTS
2040        BIN  
2050        CMB  R16,=002         !         \   IF NOT IN RUN MODE
2060        JZR  KBD_GO           !             \     OR IN 'ON..GOTO-GOSUB'
2070        CMB  R16,=007         !                THEN GIVE UP
2080        JZR  KBD_GO           !             /     AND PASS KEY TO SYSTEM
2090        JMP  KBDE             !              /
2100 KBD_GO PUMD R2,+R6           !           \
2110        PUMD R40,+R6          !           \
2120        LDM  R40,R20          !        /  SAVE REGISTERS
2130        PUMD R40,+R6          !          /
2140        BCD  
2150        ELB  R47              !          \   SAVE E BECAUSE OF CALL
2160        BIN                   !                   /        TO ERROR
2170        CMM  R6,=R6LIM2       !    \   IF RETURN STACK OVERFLOW
2180        JNC  R6_OK            !              \     THEN GIVE ERROR 15
2190        JSB  =ERROR           !             /     ( SYSTEM ERROR )
2200        BYT  15D              !               /
2210 R6_OK  LDMD R22,=BINTAB      !      GET BASE ADDRESS
2220        LDM  R26,=377,57      !    \  INITIALIZE REPEAT TIME
2230        STMD R26,X22,KEYRPT   !   /
2240        LDBD R26,=KEYCOD      !      GET KEYCODE FROM KBD CHIP
2250        STBD R26,X22,OLDKEY   !   SAVE IT AWAY FOR AUTO REPEAT
2260        JSB  X22,LOGKEY       !        PUT THE KEY IN THE BUFFER
2270 STARTK LDBD R20,=KRPET1      !      \   RESET KBD SCANNET
2280        STBD R20,=KEYCNT      !      /
2290        LDB  R20,=1           !        \   RESTART SCANNER
2300        STBD R20,=KEYCOD      !      /
2310        LDM  R20,R6           !         \
2320        SBM  R20,=26,0        !        \  ADJUST RETURN STACK TO
2330        LDM  R26,=PADKBD      !      /     NOT DO SYSTEM PROCESSING
2340        STMD R26,R20          !          /      OF THE KEYBOARD
2350        BCD                   !                   \
2360        ERB  R47              !         /   RESTORE E
2370        POMD R40,-R6          !          \
2380        STM  R40,R20          !       \  RESTORE REGISTERS
2390        POMD R40,-R6          !           /
2400        POMD R2,-R6           !           /
2410 KBDE   STBD R#,=GINTEN       !       RE-ENABLE INTERRUPTS
2420        RTN  
2430        LNK  MY&IP3.asm
