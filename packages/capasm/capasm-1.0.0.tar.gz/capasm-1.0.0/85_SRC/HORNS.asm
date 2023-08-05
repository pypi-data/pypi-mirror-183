1000        NAM  HORN  
1010        DEF  RUNTIM
1020        DEF  TOKS  
1030        DEF  PARSE 
1040        DEF  ERMSG 
1050        DEF  INIT  
1060 ! ************************
1070 RUNTIM BSZ  2
1080        DEF  HORN. 
1090 ! ************************
1100 PARSE  BSZ  2
1110        DEF  HORPAR
1120 ERMSG  BYT  377,377
1130 ! ************************
1140 TOKS   ASP  "HORN"
1150        BYT  377
1160 ! ************************
1170 INIT   RTN  
1180 ! ************************
1190 ! * SYNTAX FOR HORN IS:   
1200 ! *  HORN P,S,D,N         
1210 ! *    where:             
1220 ! *     P=start period    
1230 ! *       (length of one  
1240 ! *        cycle of wave) 
1250 ! *     S=step amount     
1260 ! *       (delta period)  
1270 ! *     D=duration of a   
1280 ! *       single step in  
1290 ! *       milliseconds    
1300 ! *     N=number of steps 
1310 ! ************************
1320 HORPAR PUBD R43,+R6          ! SAVE TOKEN #
1330        LDB  R14,=371         ! LOAD BIN PGM TOKEN TOKEN
1340        JSB  =GET4N           ! GET FOUR PARAMETERS
1350        JEN  OK               ! JIF GOT ALL FOUR PARAMETERS
1360        POBD R57,-R6          ! CLEAN UP R6 (RETURN) STACK
1370        JSB  =ERROR+          ! REPORT ERROR
1380        BYT  88D              ! BAD STATEMENT
1390 OK     POBD R57,-R6          ! RECOVER TOKEN #
1400        PUMD R56,+R12         ! PUSH GARBAGE BYTE & TOKEN #
1410        RTN                   ! DONE
1420 ! ************************
1430 ! * R56-7 = FREQUENCY     
1440 ! * R46-7 = FREQUENCY STEP
1450 ! * R36-7 = NUMBER STEPS  
1460 ! ************************
1470        BYT  241
1480 HORN.  JSB  =ONEB            ! GET NUMBER OF STEPS AS A TWO-BYTE SIGNED VALUE
1490        PUMD R46,+R6          ! SAVE FOR LATER
1500        POMD R40,-R12         ! GET TIMER VALUE OFF OF R12 STACK
1510        CLM  R50              ! FOR TIMER #
1520        LDB  R57,=30C         ! MAKE R50-7 A FLOATING POINT 3
1530        PUMD R50,+R12         ! PUSH TIMER # ON R12 STACK
1540        PUMD R40,+R12         ! PUSH TIME VALUE ON R12 STACK
1550        PUBD R16,+R6          ! SAVE R16 CONTENTS
1560        LDB  R16,=2           ! FAKE RUN MODE FOR ONTIMER
1570        JSB  =ONTIM.          ! START TIMER # 3
1580        SBM  R10,=3,0         ! RESTORE R10 (ONTIM. SKIPS GOTO/GOSUB LINE #)
1590        POBD R16,-R6          ! RESTORE R16
1600        JSB  =TWOB            ! GET STEP AMOUNT AND FREQUENCY VALUES
1610        POMD R36,-R6          ! RECOVER # OF STEPS
1620        LDM  R30,=40,0        ! LOAD CONTSTANTS FOR TURNING SPEADKER ON/OFF
1630 HO     STBD R31,=KEYSTS      ! TURN SPEAKER OFF
1640        LDM  R34,R56          ! GET A COPY OF WAVEFORM PERIOD
1650 TIM1   DCM  R#               ! DECREMENT COUNT
1660        JCY  TIM1             ! LOOP TILL NEGATIVE
1670        STBD R30,=KEYSTS      ! TURN SPEAKER ON
1680        LDBD R35,=SVCWRD      ! GET SERVICE WORD
1690        JOD  ABORT            ! JIF KEY WAS HIT
1700        LDB  R34,=6           ! DELAY TO KEEP BEEP ON FOR MINIMUM TIME
1710 KILTIM DCB  R#               ! DECREMENT COUNTER
1720        JCY  KILTIM           ! LOOP IF NOT DONE
1730        STB  R35,R33          ! SAVE A COPY IN CASE WE NEED TO CLEAR BIT
1740        ANM  R35,=20          ! MASK FOR TIMER # 3 INTERRUPT BIT
1750        JZR  HO               ! LOOP IF NOT YET STEP TIME
1760        ANM  R33,=357         ! CLEAR TIMER # 3 INTERRUPT BIT
1770        STBD R33,=SVCWRD      ! RESET SERVICE WORD
1780        ADM  R56,R46          ! CHANGE FREQUENCY BY STEP AMOUNT
1790        DCM  R36              ! DECREMENT STEP COUNT
1800        JNZ  HO               ! LOOP IF NOT DONE
1810 ABORT  STBD R31,=KEYSTS      ! TURN SPEAKER OFF
1820        CLM  R40              ! FABRICATE TIMER # FOR OFF TIMER
1830        LDB  R47,=30C         ! MAKE IT A FLOATING POINT 3
1840        PUMD R40,+R12         ! PUSH TIMER # TO STACK
1850        JSB  =OFTIM.          ! TURN TIMER # 3 OFF
1860        RTN                   ! DONE
1870 ! ************************
1880 ONTIM. DAD  66041            ! -
1890 OFTIM. DAD  66211            ! -
1900 ONEB   DAD  56113            ! -
1910 KEYSTS DAD  177402           ! -  DEFINE ABSOLUTE ADDRESSES
1920 SVCWRD DAD  100151           ! -
1930 TWOB   DAD  56176            ! -
1940 GET4N  DAD  14414            ! -
1950 ERROR+ DAD  6611             ! -
1960        FIN                   ! -           THE END
