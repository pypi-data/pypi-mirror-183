       ABS  
       ORG 06000H
       TITLE 'krdir'
*  __________________________________________________________________
* |KRDIR 134 06/24/82 - 7/ 9/1982 1:36PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@      @@@@@@@@@@  @@@@@@@@     ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@    @@@@@@@@@@  @@@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@    @@@       @@      @@     @@@   ||
* ||   @@  @@@     @@      @@  @@      @@      @@      @@      @@   ||
* ||   @@ @@@      @@     @@   @@      @@      @@      @@     @@    ||
* ||   @@@@@       @@@@@@@     @@      @@      @@      @@@@@@@      ||
* ||   @@@@@       @@@@@@@     @@      @@      @@      @@@@@@@      ||
* ||   @@ @@@      @@    @@@   @@      @@      @@      @@    @@@    ||
* ||   @@  @@@     @@     @@@  @@      @@      @@      @@     @@@   ||
* ||   @@   @@@    @@      @@  @@    @@@       @@      @@      @@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@    @@@@@@@@@@  @@      @@   ||
* ||   @@     @@@  @@      @@  @@@@@@      @@@@@@@@@@  @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1336>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
         DEF  RMHEAD           ; ROM marker: 1CE3
         DEF  FILDRV           ; RMDR.LOC - location of file
         DEF  LEN8K            ; RMDR.SIZ - size of file
         VAL  TYTOK?           ; RMDR.TYP - type of file
         VAL  TYNSYS           ; RMDR.TNM - name of type
         DATA  300,240,251,232 ; RMDR.DAT - Date of creation
         DATA  "melrom  "      ; RMDR.NAM - name of file
         DEF  ZRO              ; RMDR.ESZ - size of file (0 for ROMs)
       TITLE 'krhdr'
*
*  __________________________________________________________________
* |KRHDR 222 06/24/82 - 7/ 9/1982 1:36PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@      @@@@@@@@     ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@    @@@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@      @@  @@    @@@   @@     @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@      @@  @@      @@  @@     @@    ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@@  @@      @@  @@@@@@@      ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@@  @@      @@  @@@@@@@      ||
* ||   @@ @@@      @@    @@@   @@      @@  @@      @@  @@    @@@    ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@  @@     @@@   ||
* ||   @@   @@@    @@      @@  @@      @@  @@    @@@   @@      @@   ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@    @@      @@   ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@      @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1366>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FILDRV   DEF  MELROM           ; RM.ID - ROM id#
         DEF  RUNTIM           ; RM.RUN - pointer to RUNTIM table
         DEF  ASCII            ; RM.ASC - pointer to ASCII TOKEN table
         DEF  PARTAB           ; RM.PAR - pointer to PARSE table
         DEF  ERMSG            ; RM.ERR - pointer to ERRMSG table
         DEF  FILNIT           ; RM.INI - pointer to INIT routine
RUNTIM   DEF  RETURN           
         DEF  TRFRM.
         DEF  PACK.
         DEF  INIT.
         DEF  TIME$.           
         DEF  DATE$.           
         DEF  TIME.
         DEF  DATE.
         DEF  ATN2.            
         DEF  ICOS.
         DEF  ITAN.
         DEF  ISIN.
         DEF  REM10.           
         DEF  MOD10.
         DEF  RND10.           
ASCII    DATA  `TRANSFORM`      
         DATA  `PACK`           
         DATA  `INITIALIZE`     
         DATA  `TIME$`          
         DATA  `DATE$`          
         DATA  `TIME`           
         DATA  `DATE`           
         DATA  `ANGLE`          
         DATA  `ACOS`           
         DATA  `ATN`            
         DATA  `ASIN`           
         DATA  `RMD`            
         DATA  `MOD`            
         DATA  `RND`            
         DATA  377              
PARTAB   DEF  RETURN
         DEF  TRNSLP           
         DEF  ASPACK           
         DEF  ASINIT           

GTFMEM   JSB  =EVIL            
           DEF S22-77
         JSB  =RESCON
           VAL FNBLEN
         STM  R26,R20          
RETURN   RTN                   

FILNIT   CMB  R0,=V.FILE
         RNE
         CLE                   
         JSB  =GTFMEM          
         REN
         PUMD R24,+R20         
         PUMD R26,+R20         
         PUMD R34,+R20         
         PUMD R36,+R20         
         PUMD R40,+R20         
         PUMD R50,+R20         
         PUMD R60,+R20         
         PUMD R70,+R20         
FILINI2  JSB  =EVIL            
           DEF S20-77
         JSB  =FLSBON
         SBM  R20,=(FLSTOP).2
         STM  R20,R24          

HDDISP   LDBD R2,=TOKEN        
         JSB  =LOOKUP          
           DEF FILTAB
         REN
         JSB  X0,ZRO           
         RTN                   
*
FILTAB
         VAL PURGTK
         DEF FLPURG

         VAL RENATK
         DEF FLRENA

         VAL CATTK
         DEF FLCAT

         VAL COPYTK
         DEF FLCOPY
      
         DATA 0
       TITLE 'krca2'
*
* ********************************************************************
* ********************************************************************
FLCAT    LDMD R64,X24,FLDEV
         JSB  =VFHI+           
         LDMD R40,X24,FNBR60
         CMMD R40,=BLANKS      
         IFZR
           JSB  =VFDIR
           JEN  krca2_9
           JSB  =FLCATA
         ELSE
           JSB  =FLCAF+
           JEN  krca2_9
           JSB  =FLCAT1
         ENDIF
krca2_9  JSB  =VFBYE
         RTN                   

FLCATA   CLM  R26              
         STMD R26,X36,(VF.2DE)+(VF.CST)-(VF.CDE)
         LDM  R26,=CATHED
         JSB  =VFMSG
         JSB  =VFEOD?
         RZR
         JSB  =FLDOWN
         JSB  =VFEOD?
         RZR
FLGUT    REN
         JSB  =FLDENT
         REN
         JSB  =VF1T02
         JSB  =SIGNIF          
         DRP  !2
         JSB  =LOOKUP          
           DEF FLTAB
         JEN  CLESUB
         JSB  =DEQUE           
         JSB  X0,ZRO           
         JMP  FLGUT
CLESUB   CLE                   
         RTN                   

FL.DN    JSB  =VFNXE+          
         JSB  =VFEOD?
         IFZR
           JSB  =FLUENT
         ENDIF
         RTN                   

FL.SDN   JSB  =VFNXE+          
         JSB  =VFEOD?
         JNZ  FL.SDN
         JSB  =FLUENT
         RTN                   

FL.UP
FLUENT   JSB  =VFGLOC
         DRP  !46
         ARP  !56
         CMM  R46,R56
         JNZ  krca2_1
         TSB  R45              
         RZR
krca2_1  LDMD R45,X36,VF.CDL
         SBM  R45,=32D,0,0      
         STMD R45,X36,VF.CDL
         LDMD R55,X36,VF.LOC
         DCM  R56              
         CMM  R46,R56          
         IFEQ
           JSB  =VFRWSB
         ELSE
           JSB  =VFRWSK          
         ENDIF
         REN
         JSB  =VFNXD-
         REN
         JSB  =VFMFP?
         JZR  FLUENT
         RTN                   

FLDENT   JSB  =FLDOWN
         REN
         JSB  =VFEOD?
         IFZR
           JSB  =FLUENT
           REN
         ENDIF
         JSB  =VFUTL+          
         LDMD R20,X36,VF.CST
         LDMD R22,X36,(VF.2DE)+(VF.CST)-(VF.CDE)
         CMM  R22,R20          
         RZR
         JSB  =FLCAT1
         JSB  =VFRVDE
         RTN                   

krca2_0  JSB  =VFNXE+          
FLDOWN   JSB  =VFEOD?
         RZR
         JSB  =VFMFP?
         JZR  krca2_0
         RTN                   

FLTAB    VAL  UPKEY
         DEF  FL.UP
         VAL  DOWNKY
         DEF  FL.DN
         VAL  (SHIFT)+(UPKEY)
         DEF  VFDIR
         VAL  (SHIFT)+(DOWNKY)
         DEF  FL.SDN
         DATA 0

FLCAT1   JSB  =VFRVDE           
         JSB  =VFRDE
         LDM  R30,R36          
         ADM  R30,=(VF.RDE).2
         LDM  R26,=((TMPMM2)+1).2
         PUMD R36,+R6          
         PUMD R20,+R6          
         JSB  =CATBUF          
         PUBD R36,-R26         
         POMD R20,-R6          
         POMD R36,-R6          
         LDMD R46,X36,(VF.CDE)+8D
         STMD R46,X26,9D
         CMB  R20,=' '
         IFNE
           LDMD R42,X26,(13D).2
           LDB  R47,R20          
           STMD R43,X26,13D
         ENDIF
         JSB  =VFMSG
         RTN                   
       TITLE 'krprg'
*
*  __________________________________________________________________
* |KRPRG 372 06/24/82 - 7/ 9/1982 1:38PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@     @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@     @@@  @@     @@   @@           ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@@@@@@     @@           ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@     @@   @@@@@   ||
* ||   @@ @@@      @@    @@@   @@          @@    @@@   @@   @@@@@   ||
* ||   @@  @@@     @@     @@@  @@          @@     @@@  @@      @@   ||
* ||   @@   @@@    @@      @@  @@          @@      @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@  @@          @@      @@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@  @@          @@      @@     @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820908.1330>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FLPURG   LDMD R64,X24,FLDEV
         JSB  =VFHI+           
         LDMD R40,X24,FLNAM
         JSB  =FLCAF+
         JEN  krprg_9
         JSB  =FLPUR-
krprg_9  JSB  =VFBYE
         RTN                   

FLPUR-   CLM  R46              
         STMD R46,X36,VF.FTY
         JSB  =VFDECL
         RTN                   
       TITLE 'krcop'
*
*  __________________________________________________________________
* |KRCOP 86 06/24/82 - 7/ 9/1982 1:39PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@       @@@@       @@@@@@    @@@@@@@@     ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@    @@@@@@@@   @@@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@@    @@@  @@     @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@          @@      @@  @@     @@@   ||
* ||   @@@@@       @@@@@@@     @@          @@      @@  @@@@@@@@@    ||
* ||   @@@@@       @@@@@@@     @@          @@      @@  @@@@@@@@     ||
* ||   @@ @@@      @@    @@@   @@          @@      @@  @@           ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@  @@           ||
* ||   @@   @@@    @@      @@  @@@    @@@  @@@    @@@  @@           ||
* ||   @@    @@@   @@      @@   @@@@@@@@    @@@@@@@@   @@           ||
* ||   @@     @@@  @@      @@     @@@@       @@@@@@    @@           ||
* ||                                                                ||
* ||                  Last edited on <820908.1357>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FLCOPY   CLB  R30              
         LDMD R70,X24,FLNAM1
         LDMD R54,X24,FLDEV1
         IFZR
           LDMD R20,X24,FLDIR1
           LDMD R70,X20,DR.NAM
         ENDIF
         LDMD R40,X24,FLNAM0
         LDMD R64,R24          
         IFZR
           LDMD R20,X24,FLDIR0
           LDMD R40,X20,DR.NAM
         ENDIF
         CMM  R40,R70          
         IFEQ
           ICB  R30              
         ENDIF
         STBD R30,X24,FLSFLG
         TSB  R64              
         IFZR
           JSB  =FLSTOR
         ELSE
           TSB  R54              
           IFZR
             JSB  =FLLOAD
           ELSE
             CMM  R54,R64           
             IFEQ
               JSB  =FLTTOT          
             ELSE
               JSB  =FLFTOF
             ENDIF
           ENDIF
         ENDIF
         RTN                   

FLLOAD   JSB  =VFHI            
         JEN  JEN7FA
         JSB  =FLG0FE
         JEN  JEN7F
         JSB  =FLVFO?
         JEN  JEN7F
         JSB  =VFRDE           
         JSB  =VFROO?          
         IFNZ
           JSB  =ERR1            
           DATA 68D
           JEN  JEN7F
         ENDIF
         LDMD R74,X36,((VF.RDE)+(DR.DAT)).2
         JSB  =VFSKFL
JEN7F    JEN  JEN7FA
         JSB  =VFLIF?
         IFZR
           LDMD R46,X36,VF.CLN
           TSB  R47              
           IFNZ
             JSB  =ERR1            
             DATA 16D
             JEN  JEN7FA
           ENDIF
           CLB  R45              
           STM  R45,R32          
           LDM  R20,=TYLIF1      
           STMD R20,X36,((VF.RDE)+(DR.TYP)).2
         ELSE
*          NLC     ; ???
           LDM  R44,=(DRENSZ).2
           BSS  2D
           LDM  R46,R36          
           ADM  R46,=(VF.RDE).2
           JSB  =VFRWRD          
JEN7FA     JEN  krcop_6
           LDMD R32,X36,((VF.RDE)+(DR.SIZ)).2
         ENDIF
         LDMD R30,X24,FLDIR1
         JSB  =FLSAM?
         IFZR
           JSB  =JSBCRT          
           LDM  R74,R44          
         ENDIF
         STMD R74,X30,DR.DAT
         STM  R30,R46          
         LDMD R30,R30          
         JSB  =ALLDC           
         JEN  krcop_6
         STM  R46,R30          
         LDMD R46,R30          
         STM  R32,R44          
         JSB  =VFRWRD          
krcop_6  IFEN
           LDMD R30,X24,FLDIR1
           LDMD R40,X30,DR.NAM
           JSB  =FPURGE          
           STE
         ELSE
           LDMD R20,X36,((VF.RDE)+(DR.TYP)).2
           STMD R20,X30,DR.TYP
         ENDIF
         JSB  =VFTERM          
         RTN                   

FLSTOR   DRP  !64
         LDM  R64,R54           
         JSB  =VFHI+           
         JSB  =FLGET1
         JSB  =FLFIN+
         IFZR
           JSB  =FLPUR-
           JEN  krcop_9
         ENDIF
         LDMD R30,X24,FLDIR0
         CLB  R20              
         JSB  =FLNEW           
         JEN  krcop_7
         CLB  R45              
         LDM  R46,R66          
         JSB  =VFRWSK          
         JEN  krcop_7
         JSB  =VFLAD
         JEN  krcop_7
         JSB  =VFWREC
         JEN  krcop_7
         JSB  =VFRLF?
         IFNZ
           CLM  R44              
*          NLC
           LDM  R44,=(DRENSZ).2
           BSS  2D
           LDM  R46,R30          
           JSB  =VFWR            
           JEN  krcop_7
         ENDIF
         LDMD R56,X30,DR.SIZ
         STM  R56,R44          
         LDMD R46,R30          
         JSB  =VFWR            
         JEN  krcop_7
         JSB  =VFADCL
         JEN  krcop_7
         JSB  =VFBSY           
         IFEN
krcop_7    JSB  =FLPUR!
           STE
         ENDIF
krcop_9  JSB  =VFTERM          
         RTN                   

FLPUR!   LDBD R57,=KEYHIT      
         PUBD R57,+R6          
         CLB  R57              
         STBD R57,=KEYHIT      
         ICB  R57              
         STBD R57,X36,VF.FLG
         JSB  =FLGET1
         JSB  =FLFIN+
         JNZ  krcop_8
         JEN  krcop_8
         JSB  =FLPUR-
krcop_8  POBD R2,-R6           
         STBD R2,=KEYHIT       
         RTN                   
       TITLE 'krco2'
*
*  __________________________________________________________________
* |KRCO2 83 06/24/82 - 7/ 9/1982 1:41PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@       @@@@       @@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@    @@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@@    @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@          @@   ||
* ||   @@ @@@      @@     @@   @@          @@      @@         @@@   ||
* ||   @@@@@       @@@@@@@     @@          @@      @@        @@@    ||
* ||   @@@@@       @@@@@@@     @@          @@      @@      @@@      ||
* ||   @@ @@@      @@    @@@   @@          @@      @@    @@@        ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@   @@@         ||
* ||   @@   @@@    @@      @@  @@@    @@@  @@@    @@@  @@@          ||
* ||   @@    @@@   @@      @@   @@@@@@@@    @@@@@@@@   @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@     @@@@       @@@@@@    @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1357>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FLTTOT   JSB  =VFHI+           
         JSB  =FLGTFN
         JEN  krco2_9
         JSB  =FLG0FE
         JEN  krco2_9
         JSB  =FLVFO?
         JEN  krco2_9
         JSB  =VF1TO2
         LDB  R20,=0FFH
         JSB  =FLNEW           
         JEN  krco2_71
         LDMD R54,X36,((VF.2DE)+(VF.CST)-(VF.CDE)).2
         LDMD R56,X36,((VF.2DE)+(VF.CLN)-(VF.CDE)).2
         STM  R54,R62          
         JSB  =VFMOVE
         JEZ  krco2_9
krco2_71 JSB  =FLPUR!
         STE
krco2_9  JSB  =VFTERM          
         RTN                   

FLSWCH   JSB  =VFBYE
         LDMD R0,X24,FNBSW
         STMD R36,X24,FNBSW
         LDM  R36,R0           
         RTN                   

FLFTOF   JSB  =VFHI+           
         JSB  =FLSWCH
         CLB  R64              
         ICB  R64              
         STBD R64,=HANDLD      
         LDMD R64,X24,FLDEV1
         JSB  =VFHI            
         JEN  FLSWCH
         JSB  =FLGTFN
         JEN  JEN7F2
         JSB  =FLSWCH
         JEN  JEN7F2
         LDMD R64,X24,FLDEV0
         JSB  =VFHI            
         JEN  JEN7F2
         JSB  =FLG0F+          
         JEN  JEN7F2
         IFNZ
           JSB  =ERR1            
           DATA 62D
           JMP krco2_7
         ENDIF
         JSB  =FLVF0?
         JEN  krco2_7
         DRP  R34              
         JSB  =VFCDEP
         LDM  R32,=(32D).2
         JSB  =FLSWCH
JEN7F2   JEN  krco2_7
         LDM  R30,R36          
         ADM  R30,=(VF.2DE).2
         JSB  =COPY            
         LDB  R20,=0FFH
         JSB  =FLNEW           
         JEN  krco2_6
         CLB  R45              
         LDM  R46,R66          
         JSB  =VFRWSK          
         JEN  krco2_6
         JSB  =FLSWCH
         JEN  krco2_5
         JSB  =VFSKFL
         JEN  krco2_5
         JSB  =VFRREC
         JEN  krco2_5
         JSB  =FLSWCH
         JEN  krco2_6
         JSB  =VFLAD
         JEN  krco2_6
         JSB  =VFDDL2
         JEN  krco2_6
         JSB  =FLR36
         JSB  =VFTAD
         JEN  krco2_5
         LDB  R20,=0FFH
         LDMD R46,X36,VF.CLN
         CLB  R45              
         JSB  =VFWACH
         JEN  krco2_5
         JSB  =FLSWCH
         JEN  krco2_6
         JSB  =VFADCL
         JEN  krco2_6
         JSB  =VFTERM          
         JEN  krco2_7
         JSB  =FLSWCH
         JSB  =VFTERM          
         RTN                   

krco2_5  JSB  =FLSWCH
krco2_6  JSB  =FLPUR!
krco2_7  JSB  =VFBYE
         RTN                   
       TITLE 'krren'
*
*  __________________________________________________________________
* |KRREN 451 06/24/82 - 7/9/1982 1:41PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@@@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@@  @@      @@   ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@          @@@     @@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@@@    @@   ||
* ||   @@ @@@      @@     @@   @@     @@   @@          @@ @@   @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@     @@@@@@@@@   @@  @@  @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@     @@@@@@@@@   @@  @@  @@   ||
* ||   @@ @@@      @@    @@@   @@    @@@   @@          @@   @@ @@   ||
* ||   @@  @@@     @@     @@@  @@     @@@  @@          @@    @@@@   ||
* ||   @@   @@@    @@      @@  @@      @@  @@          @@     @@@   ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@  @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
LFRENA   LDMD R64,X24,FLDEV0
         JNZ  krren_1
         LDMD R64,X24,FLDEV1
krren_1  JSB  =VFHI+           
         JSB  =FLGTFN
         JEN  krren_2
         JSB  =FLG0FE
         JEN  krren_2
         JSB  =FLGET1
         JSB  =VFRENA
         JSB  =VFDECL
krren_2  JSB  =VFBYE
         RTN                   
       TITLE 'krpak'
PACKTK EQU  2
*
*  __________________________________________________________________
* |KRPAK 316 06/24/82 - 7/ 9/1982 1:45PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@      @@@@@@    @@     @@@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@   @@    @@@    ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@@    @@@  @@   @@@     ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@  @@@      ||
* ||   @@ @@@      @@     @@   @@     @@@  @@      @@  @@ @@@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@@@@@@@@@  @@@@@        ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@@@@  @@@@@        ||
* ||   @@ @@@      @@    @@@   @@          @@      @@  @@ @@@       ||
* ||   @@  @@@     @@     @@@  @@          @@      @@  @@  @@@      ||
* ||   @@   @@@    @@      @@  @@          @@      @@  @@   @@@     ||
* ||   @@    @@@   @@      @@  @@          @@      @@  @@    @@@    ||
* ||   @@     @@@  @@      @@  @@          @@      @@  @@     @@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1357>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
ASPACK   JSB  =SYSJSB          
           DEF  GETSTP
*        NLC
         LDM  R54,=
           VAL  EROMTK
           DEF  MELROM
           VAL  PACKTK
         PUMD R54,+R12         
         RTN                   

         DATA  241
PACK.    JSB  =FLSBON
         JSB  =FLSTAK
         JEN  krpak_1
         JSB  =VFHI            
         IFEN
krpak_1    LDBD R2,=KEYHIT       
           CMB  R2,=ATTNKY
           REQ
           JSBN  =ERR1+           
           DATA  63D
         ENDIF
         JSB  =PAK0
         JEN  PAKBAD             
         JSB  =PAK1
         JEN  PAKBAD             
         JSB  =PAK2
         JEN  PAKBAD             
         JSB  =PAK3
         JEN  PAKBAD             
         JSB  =VFADDR
         JEN  PAKBAD             
         JSB  =VFBSY           
         JEZ  krpak_9
PAKBAD   JSB  =ERR1            
         DATA 97D
krpak_9  JSB  =VFTERM          
         RTN                   

PAK0     JSB  =VFDIR+          
         LDM  R56,=256D
         JSB  =RSMEM-          
         REN
         STM  R26,R30          
         ADM  R26,=256D
         DRP  R34              
         JSB  =VFCDEP
         ARP  !36
         LDM  R32,=(32D).2
         LDMD R40,X36,VF.CDL
krpak_0  JSB  =VFEOD?
         IFZR
           SBM  R26,=256D
           JSB  =VFLED?
            JZR  krpak_11
           LDMD R46,X36,(VF.CDL)+1
           CMM  R46,R41          
           IFNE
krpak_11     LDM  R45,R40          
             JSB  =VFRWO+          
             STM  R26,R46          
             LDM  R26,=256D
             STM  R26,R44          
             CLM  R26              
             DCM  R26              
             STMD R26,X36,VF.FTY
             JSB  =COPY            
             JSB  =VFWOOP          
           ENDIF
           RTN                   
         ENDIF
         JSB  =VFMFP?
         IFNZ
           JSB  =COPY            
           ADM  R30,=(32D).2
           CMM  R30,R26          
           IFEQ
             LDMD R65,X36,VF.CDL
             ADM  R65,=32D,0,0      
             LDM  R45,R40          
             JSB  =VFRWO+          
             ICM  R41              
             LDM  R2,=256D
             STM  R2,R44           
             SBM  R30,R2           
             STM  R30,R46          
             JSB  =VFWOOP          
             REN
             LDM  R45,R65          
             JSB  =VFRWK+          
           ENDIF
         ENDIF
         JSB  =VFNXDE
         JEZ  krpak_0
         RTN

PAK1     JSB  =VFDIR+          
         JSB  =RESCON          
         DATA  6
         REN
         LDM  R24,R26          
         ADM  R24,=(6d).2
         LDMD R20,X36,VF.DL
         LDMD R66,X36,VF.BIG
         ADM  R66,R20          
krpak_12  JSB  =VFEOD?
         IFZR
           CLM  R62              
           PUMD R62,+R26         
           RTN                   
         ENDIF
         JSB  =VFRVDE
         LDMD R42,X36,VF.CST
         LDM  R44,R46          
         STM  R66,R46          
         ADM  R66,R44          
         PUMD R42,+R26         
         JSB  =VFNXE+          
         JSB  =RESCON          
         DATA  6
         JEZ  krpak_12
         RTN                   

PAK2     JSB  =VFDIR+          
         STM  R24,R26          
krpak_01 LDB  R45,=14D          
         LOOP
           JSB  =VFRWSB
           REN
           JSB  =VFLAD+          
           POMD R62,-R26         
           IFZR
             JSB  =PAK2A
             RTN                   
           ENDIF
           CLB  R57              
           JSB  =DDLRP+          
           STB  R67,R57          
           JSB  =DATRP+          
           STB  R66,R57          
           JSB  =DATRP+          
           ADB  R45,=32D
           CMB  R45,=14D         
         WHNE
         JSB  =PAK2A
         JEZ  krpak_01
         RTN                   

PAK2A    LDMD R45,X36,VF.LOC
         CLB  R45              
         DCM  R46              
         JSB  =VFRWU0
         REN
         JSB  =VFRREC
         RTN                   

PAK3     LDM  R26,R24          
         LOOP
           JSB  =VFBSY+          
           POMD R62,-R26         
           RZR
           JSB  =VFMOVE
         WHEZ
         RTN                   
       TITLE 'krin2'
*
*  __________________________________________________________________
* |KXIN2 227 06/24/82 - 7/ 9/1982 1:45PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@  @@      @@     @@@@      ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@      @@   @@@@@@@@    ||
* ||   @@   @@@    @@@    @@@      @@      @@@     @@  @@@    @@@   ||
* ||   @@  @@@      @@@  @@@       @@      @@@@    @@          @@   ||
* ||   @@ @@@         @@@@         @@      @@ @@   @@         @@@   ||
* ||   @@@@@           @@          @@      @@  @@  @@        @@@    ||
* ||   @@@@@           @@          @@      @@  @@  @@      @@@      ||
* ||   @@ @@@         @@@@         @@      @@   @@ @@    @@@        ||
* ||   @@  @@@      @@@  @@@       @@      @@    @@@@   @@@         ||
* ||   @@   @@@    @@@    @@@      @@      @@     @@@  @@@          ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1355>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
INITTK   EQU  03H
ASINIT   JSB  =SYSJSB          
           DEF  GETSTP
         CMB  R14,=COMMA         
         JNE  krin2_2
         JSB  =SYSJSB          
           DEF  NUMVA+
         IFEZ
           JSB  =ERROR+          
           DATA 91D
         ENDIF
krin2_2  LDM  R54,=
           VAL EROMTK
           DEF MELROM
           VAL INITTK
         PUMD R54,+R12         
         RTN                   

         DATA  241
INIT.    JSB  =FLSBON
         JSB  =ONR12?          
         CMB  R2,=12D           
         IFEQ
           JSB  =ONEB            
         ELSE
           LDM  R76,=(128D).2
         ENDIF
         JSB  =FLSTAK
         JEN  krin2_1
         JSB  =VFGET
         JEN  krin2_1
         JSB  =VFMM?
         IFEN
krin2_1    LDBD R2,=KEYHIT       
           CMB  R2,=ATTNKY
           REQ
           JSBN  =ERR1+           
           DATA 63D
         ENDIF
         JSB  =CLRCOD
         JSB  =UNTUNL
         JEN  krin2_9
         JSB  =VFSTAT
         JEN  krin2_9             
         JSB  =INISIZ
         JEN  krin2_9             
         JSB  =INICHK
         JEN  krin2_9             
         JSB  =VFLAD
         JEN  krin2_9             
         LDB  R57,=5D           
         JSB  =DDLREP          
         JEN  krin2_9             
         JSB  =VFBSY           
krin2_9  JEN  krin2_91             
         CLM  R45              
         JSB  =VFRWSK          
         JEN  krin2_91             
         LDM  R20,=0,16D
         JSB  =VFDUDE
         JEN  krin2_91             
         CLM  R45              
         JSB  =VFRWSK          
         JEN  krin2_91             
**
         LDM  R34,=(FILATT).2
         LDM  R32,=(36D).2
         DRP  R30
         JSB  =VFCDEP

         JSB  =COPY
         ADM  R32,R30
         STMD R76,X30,18D
         LDM  R20,R2
         JSB  =REVBYT

         LDM  R46,=(12D).2
         STM  R46,R44
         SBM  R46,R32
         TCM  R46
         LDB  R57,=6D
         JSB  =DDT67
         JEN  krin2_91


         JSB  =JSBCRT          
         JSB  =VFTIME          
         JSB  =VFCD46
         ADB  R44,=10D
         JSB  =VFRWWR
         REN
         JSB  =VFCLCH
krin2_91 JSB  =VFBYE
         RTN                   

FILATT   DATA 80H,0
         DATA '      '
         DATA 0,0,0,2
         DATA 10H,0
         DATA 0,0
         DATA 0,0,0,0
         DATA 0,1,0,0
         DATA 0,0,0,2
         DATA 0,0,0,1
         DATA 0,0,1,0

ETO_     EQU 0100000010100101B

DDT67    JSB =DDTREP
         REN
         LDM  R56,=SDA
         JSB  =RDYSD+
         CMM  R56,=ETO_
         IFNE
           CLB  R20
           JSB  =VFWAC2
         ENDIF
         RTN
GAP002   NOP
         NOP

INISIZ   LDB  R57,=7D
         JSB  =VFCD46
         SBM  R46,=((VF.CDE)-(VF.MED)).2
         PUMD R46,+R6
         SBB  R44,=30D
         LDM  R20,=1,0FFH
         STMD R20,R46
         JSB  =DDT67
         POMD R20,-R6
         JSB  =REVBYT
         RTN

INICHK   LDM  R30,R76
         JZR  krin2_11
         JNG  krin2_11

         ADM  R30,=(7).2
         LRM  R31
         LRM  R31
         LRM  R31
         ADM  R76,R30
         ICM  R76
         LDMD R32,X36,VF.MED
         CMM  R32,R76
         IFNC
krin2_11   JSBN  =ERR1+
           DATA  11D
         ELSE
           STM  R30,R76
         ENDIF
         RTN                   
       TITLE 'krxit'
*
*  __________________________________________________________________
* |KRXIT 597 06/24/82 - 7/ 9/1982 1:49PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@@    @@@      @@          @@       ||
* ||   @@  @@@     @@      @@   @@@  @@@       @@          @@       ||
* ||   @@ @@@      @@     @@      @@@@         @@          @@       ||
* ||   @@@@@       @@@@@@@         @@          @@          @@       ||
* ||   @@@@@       @@@@@@@         @@          @@          @@       ||
* ||   @@ @@@      @@    @@@      @@@@         @@          @@       ||
* ||   @@  @@@     @@     @@@   @@@  @@@       @@          @@       ||
* ||   @@   @@@    @@      @@  @@@    @@@      @@          @@       ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@      @@       ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@      @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1357>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFRWK+   JSB  =VFRWSK          
         JMP  EXIT             
VFLAD+   JSB  =LADREP          
         JMP  EXIT             
VFHI+    JSB  =VFHI            
         JMP  EXIT             
VFDIR+   JSB  =VFDIR
         JMP  EXIT             
DDLRP+   JSB  =DDLREP          
         JMP  EXIT             
DATRP+   JSB  =DATREP          
         JMP  EXIT             
RDYSD+   JSB  =RDYSND          
         JMP  EXIT             
VFBSY+   JSB  =VFBSY           
         JMP  EXIT             
VFNXE+   JSB  =VFNXDE
         JMP  EXIT             
VFLTY+   JSB  =VFLTBY          
         JMP  EXIT             
VFRWO+   JSB  =VFRWSO
         JMP  EXIT             
VFTAD+   JSB  =TADREP          
         JMP  EXIT             
VFUTL+   JSB  =UNTUNL
EXIT     REZ
         POMD R2,-R6           
         RTN                   
       TITLE 'krfl0'
*
*  __________________________________________________________________
* |KRFLO 188 06/24/82 - 7/ 9/1982 1:53PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@@@  @@            @@@@@@     ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@           @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@          @@          @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@          @@          @@      @@   ||
* ||   @@ @@@      @@     @@   @@          @@          @@      @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@          @@      @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@          @@      @@   ||
* ||   @@ @@@      @@    @@@   @@          @@          @@      @@   ||
* ||   @@  @@@     @@     @@@  @@          @@          @@      @@   ||
* ||   @@   @@@    @@      @@  @@          @@          @@@    @@@   ||
* ||   @@    @@@   @@      @@  @@          @@@@@@@@@@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@  @@          @@@@@@@@@@    @@@@@@     ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FLGOF+   LDMD R40,X24,FLNAM0
FLFIN+   STM  R40,R70          
         JSB  =VFDIR+          
krflo_1  JSB  =VFEOD?
         IFZR
           TSM  R6               
           RTN                   
         ENDIF
         JSB  =VFMFP?
         IFNZ
           LDMD R50,X36,VF.CDE
           CMM  R50,R70          
           RZR
         ENDIF
         JSB  =VFNXE+          
         JMP  krflo_1

FLGOFE   JSB  =FLGOF+          
RENERR   REN
         RZR
         JSBN  =ERR1+           
         DATA  62D

FLCRF+   JSB  =FLFIN+
         JMP  RENERR

FLGET1   LDMD R74,X24,FLPWD1
         LDMD R40,X24,FLNAM1
         RTN                   

FLGETFN  JSB  =FLGET1
         PUMD R40,+R6          
         PUMD R74,+R6          
         JSB  =FLFIN+
         IFZR
           JSB  =ERR1            
           DATA 64D
         ENDIF
         POMD R74,-R6          
         POMD R40,-R6          
         RTN                   

FLSTAK   DRP  R26              
         JSB  =GETAD#          
         ARP  !12
         POMD R36,-R12         
         DCM  R36              
         JNG  krflo_2
         POBD R31,+R26         
         CMB  R31,=':'
         JNE  krflo_2
         LDB  R31,=4           
         JSB  =GETFST          
         REN
         TSB  R20              
         IFNZ
           CMB  R20,=' '
           IFNZ
krflo_2      STE
           ENDIF
         ENDIF
         LDMD R64,R34          
         RTN                   

FLVFO?   JSB  =VFRVDE
         JSB  =VFLIF?
         RZR
         JSB  =VFROO?          
         IFNZ
           JSBN =ERR1+
           DATA 65D
         ENDIF
         LDMD R54,X36,VF.CMP
         RZR
         CMMD R54,=BLANKS      
         RZR
         JSB  =FLVFO+
         IFNZ
           JSB  =ERR1
           DATA  66D
         ENDIF
         RTN                   

FLSBON   BIN                   
         POMD R22,-R6          
         LDBD R2,=STAND?       
         PUBD R2,+R6           
         CLB  R3               
         DCB  R3               
         JSB  =STAND+          
         DRP  !2
         LDM  R2,=(FLSBOF).2
         PUMD R2,+R6          
         PUMD R22,+R6          
         RTN                   

FLSBOF   LDBD R2,=STAND?       
         POBD R3,-R6           
         JSB  =STAND+          
         RTN                   
       TITLE 'krfl1'
*
*  __________________________________________________________________
* |KRFL1 192 06/24/82 - 7/ 9/1982 1:51PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@@@  @@              @@       ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@             @@@       ||
* ||   @@   @@@    @@     @@@  @@          @@            @@@@       ||
* ||   @@  @@@     @@      @@  @@          @@           @@@@@       ||
* ||   @@ @@@      @@     @@   @@          @@              @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@              @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@              @@       ||
* ||   @@ @@@      @@    @@@   @@          @@              @@       ||
* ||   @@  @@@     @@     @@@  @@          @@              @@       ||
* ||   @@   @@@    @@      @@  @@          @@              @@       ||
* ||   @@    @@@   @@      @@  @@          @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@          @@@@@@@@@@  @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1357>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
FLNEW    STBD R20,X36,VF.TTT
         CLM  R60              
         JSB  =VFDIR+          
         JSB  =VFRVDE
         LDMD R63,X36,VF.CDL
         LDMD R32,X36,VF.BIG
         LDMD R66,X36,VF.DL
         ADM  R66,R32          

FLNLUP   JSB  =VFEOD?
         IFZR
           LDMD R46,X36,VF.MED
           ICM  R46              
           JSB  =FLFIT?
           JNC  MEDFUL
           JSB  =FLNWDE
           REN
           TSB  R60              
           IFNZ
             LDM  R45,R63          
           ELSE
             JSB  =VFPED?
             IFZR
MEDFUL         JSBN  =ERR1+           
               DATA 95D
             ELSE
               LDMD R45,X36,VF.CDL
             ENDIF
           ENDIF
           JSB  =VFWRD1
           REN
           LDMD R45,X36,VF.LOC
           STMD R45,X36,VF.CDL
           JSB  =VFPED?
           RZR
           LDM  R20,=0FFH,1
           JSB  =VFDUDE
           RTN                   
         ENDIF
         JSB  =VFMFP?
         IFZR
           TSB  R60              
           IFZR
             LDMD R45,X36,VF.CDL
             STM  R45,R63          
           ENDIF
           JSB  =VFNXE+          
           JSB  =VFRVDE
           ICB  R60              
           IFZR
             DCB  R60              
           ENDIF
         ELSE
           TSB  R60              
           IFZR
             JSB  =FLNEW1
             JSB  =VFNXE+          
             JSB  =VFRVDE
           ELSE
             LDMD R46,X36,(VF.CST)
             JSB  =FLFIT?
             IFCY
               JSB  =FLNWDE
               REN
               LDM  R45,R63          
               JSB  =VFWRD1
               REN
               JSB  =VFCLCH
               RTN                   
             ELSE
               JSB  =FLNEW1
             ENDIF
           ENDIF
         ENDIF
         GTO  FLNLUP

FLFIT?   LDBD R20,X36,VF.TTT
         IFZR
           JSB  =VFSECT
         ELSE
           LDMD R20,X36,(VF.2DE)+(VF.CLN)-(VF.CDE)
         ENDIF
         SBM  R46,R66          
         CMM  R46,R20          
         RTN                   

FLNEW1   LDMD R42,X36,VF.CST
         ADM  R46,R42          
         STM  R46,R66          
         CLB  R60              
         RTN                   

FLNWDE   CLM  R54              
         STMD R54,X36,VF.CMP
         LDM  R56,R66          
         LDBD R20,X36,VF.TTT
         IFNZ
           LDM  R34,R36          
           ADM  R34,=(VF.2DE).2
           DRP  R30              
           JSB  =VFCDCO
           STMD R54,X36,(VF.CST)-2
           JSB  =FLNWD1
           JSB  =FLSAM?
           JNZ  krfl1_9
           LDM  R32,R36          
           ADM  R32,=(VF.CTC).2
           JMP  krfl1_7
         ENDIF
         STMD R54,X36,(VF.CST)-2
         JSB  =VFSECT
         LDM  R56,R20          
         STMD R54,X36,(VF.CLN)-2
         JSB  =VFTRNL
         REN
         JSB  =FLNWD1
         LDM  R32,R36          
         ADM  R32,=(VF.CTC).2
         JSB  =FLSAM?
         IFNZ
           LDMD R44,X30,DR.DAT
         ELSE
krfl1_7    JSB  =JSBCRT          
         ENDIF
         JSB  =VFTIME          
         LDM  R20,=80H,01H
         PUMD R20,+R32         
krfl1_9  JSB  =VFRVDE
         RTN                   

FLNWD1   JSB  =FLGET1
         JSB  =VFRENA
         JSB  =VFLIF?
         JZR  NOPW
         JSB  =VFROO?          
         IFNZ
NOPW       CMMD R74,=BLANKS      
           IFNE
             JSB  =VFUTL+          
             JSB  =WARN            
             DATA 66D
             JSB  =VFUTL+          
           ENDIF
         ELSE
           STMD R74,X36,VF.CMP
         ENDIF
         RTN                   

FLSAM?   LDBD R20,X24,FLSFLG
         RTN                   
       TITLE 'krvf0'
*
*  __________________________________________________________________
* |KXVF0 562 09/27/82 - 12/ 9/1982 1:15PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@     @@@@      ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@   @@@@@@@@    ||
* ||   @@   @@@    @@@    @@@  @@      @@  @@          @@      @@   ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@          @@     @@@   ||
* ||   @@ @@@         @@@@      @@    @@   @@          @@    @@@@   ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@   @@ @@   ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@  @@  @@   ||
* ||   @@ @@@         @@@@       @@  @@    @@          @@ @@   @@   ||
* ||   @@  @@@      @@@  @@@      @@@@     @@          @@@@    @@   ||
* ||   @@   @@@    @@@    @@@     @@@@     @@          @@@     @@   ||
* ||   @@    @@@   @@      @@      @@      @@           @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@             @@@@      ||
* ||                                                                ||
* ||                  Last edited on <821209.1314>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFHI     JSB  =VFGET            
         REN
         JSB  =VFMM?            
         JEN  krvf0_9
         LDBD R20,X36,VF.COD
         CMB  R20,='R'
         JNZ  GETHDR
         JSB  =VFBSY           
         CMM  R57,=00010111B
         JEN  krvf0_9
         IFZR
GETHDR     JSB  =VFFBHI            
           JSB  =BLEBUF          
           JEN  krvf0_9
         ENDIF
         JSB  =VFADDR
         JSB  =VFBYE
         RTN                   

krvf0_9  JSB  =CLRCOD
         JSB  =VFBYE            
STERTN   STE
         RTN                   
VFGET    LDM  R32,=(2D).2
         CMMD R66,=BLANKS      
         IFNE
           ICM  R32              
           CMB  R67,=' '
           IFNE
             ICM  R32              
           ENDIF
           LDM  R34,=TMPMM2      
           STMD R64,R34          
         ELSE
           LDM  R66,R64          
         ENDIF
         JSB  =SYSJSB          
           DEF GETPAD
         REN
         LDBD R20,X36,SETUP
         JOD  NOTMM
         CLB  R20              
         STBD R20,=HANDLD      
         LDBD R20,X36,LEN#
         LDM  R32,=(EXTLEN).2
         SBB  R32,R20          
         RZR
         RNC
         LDM  R30,R36          
         JSB  =SKPLN#          
         JSB  =ALLDC           
         REN
         LDB  R20,=EXTLEN
         STBD R20,X36,LEN#
CLRCOD   CLB  R20              
         STBD R20,X36,VF.COD
         RTN                   
VFMM?    JSB  =UNTUNL
         REN
         JSB  =VFTAD+          
         LDM  R56,=SAI
         JSB  =RDYSD+          
         LDB  R45,=10D         
         STM  R56,R46          
         ANM  R56,=0E0H,0FFH
         CMM  R56,=SAI
         IFEQ
           JSB  =ERROR           
           DATA 56D
           JMP  krvf0_8
         ENDIF
         LOOP
           JSB  =DATSND
           JEN  BADDEV
           CMM  R56,=ETO
           JZR  krvf0_2
           DCB  R45              
         WHNZ
         JMP  BADDEV
GAP003
krvf0_2  NOP
         NOP
         CMB  R47,=16D         
         IFNE
NOTMM      JSB  =ERR1            
           DATA 92D
         ENDIF
         REZ
BADDEV   JSB  =ERROR           
         DATA  57D
krvf0_8  JSB  =VFBYE            
         STE
         RTN                   

VFFBHI   JSB  =UNTUNL
         JEN  LPDN
         JSB  =LADREP          
         IFEN
LPDN       JSB  =VFBYE            
           STE
           RTN                   
         ENDIF
         CLM  R45              
         DCM  R45              
         STMD R45,X36,VF.FLG
         ICM  R45              
         JSB  =VFRWSK          
         JEN  LPDN
         CLM  R44              
         LDB  R44,=(40D).2
         LDM  R46,=TMPMEM
         JSB  =VFRWRD          
JMPLPD   JEN  LPDN
         LDM  R32,R36          
         ADM  R32,=(VF.DL).2
         LDMD R44,=((TMPMEM)+8D).2
         JSB  =REVPSH
         DRP  !44
         LDMD R44,=((TMPMEM)+16D).2
         JSB  =REVPSH

         JSB  =INISIZ
         JEN  JMPLPD
         LDMD R46,=(TMPMEM).2
         CMM  R46,=80H,00H
         JZR  krvf0_1
         LDMD R46,X36,VF.DL
         CMM  R46,=(2D).2
         JZR  krvf0_1
         JSB  =ERR1
         DATA 96D
         JMP  JMPLPD
krvf0_1  LDB  R20,='R'
         STBD R20,X36,VF.COD
         RTN

VERB     BIN
         LDM  R56,=(SIX).2
         JSB  =RESPUT
         REN

         LDBD R2,=VERMN0
         PUBD R2,+R26
         LDBD R2,=VERMN1
         PUBD R2,+R26
         LDBD R2,=VERMN2
         PUBD R2,+R26
         JSB  =SYSJSB
           DEF VERSUB
         DRP  !2
         ARP  !26
         LDBD R2,=VERMN4
         PUBD R2,+R26
         LDBD R2,=VERMN5
         PUBD R2,+R26
         RTN

FIX65    BIN
         CMB  R55,=ONES
         BCD
         RZR
         STB  R55,R65
         STB  R55,R75
         JSB  =SYSJSB
           DEF MINMM
         RTN
GAP004   NOP
         NOP

VFADR
         JSB  =VFTAD+          
         LDM  R20,=((VF.LOC)+3).2
         ADM  R20,R36          
         LDB  R57,=3D          
         JSB  =DDTREP
         REN
         LDM  R56,=SDA
         JSB  =RDYSD+          
         LOOP
           CMM  R56,=ETO
           REQ
           PUBD R57,-R20         
           JSB  =DATSND
           REN
         WHMP
       TITLE 'krvfs'
*
*  __________________________________________________________________
* |KRVFS 587 06/24/82 - 7/ 9/1982 1:57PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@    @@@@@@     ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@   @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@      @@  @@          @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@      @@   ||
* ||   @@ @@@      @@     @@    @@    @@   @@          @@@          ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@    @@@@@@@     ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@     @@@@@@@    ||
* ||   @@ @@@      @@    @@@     @@  @@    @@                 @@@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@          @@      @@   ||
* ||   @@   @@@    @@      @@     @@@@     @@          @@@     @@   ||
* ||   @@    @@@   @@      @@      @@      @@           @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@            @@@@@@     ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFRWSK   JSB  =VFRWO+          
         JSB  =VFLTY+          
         JSB  =VFRWSB
         RTN                   
         JSB  =VFLAD+          
         LDB  R56,=VFSEEK
         STBD R56,X36,VF.RSW
         LDBD R56,X36,VF.FLG
         JNZ  krvfs_0
         LDMD R56,X36,((VF.LOC)+1).2
         CMM  R56,R46          
         RZR
krvfs_0  CLB  R57              
         STBD R57,X36,VF.FLG
         LDB  R57,=4           
         JSB  =DDLRP+          
         STB  R47,R57          
         JSB  =DATRP+          
         STB  R46,R57          
         JSB  =DATREP          
         RTN                   

VFRWSB   JSB  =VFLAD+          
         LDB  R57,=3           
         JSB  =DDLRP+          
         STB  R45,R57          
         JSB  =DATRP+          
         JSB  =VFADDR
         RTN                   
       TITLE 'krvfr'
*
*  __________________________________________________________________
* |KXVFR                                                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@     ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@@    ||
* ||   @@   @@@    @@@    @@@  @@      @@  @@          @@     @@@   ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@          @@      @@   ||
* ||   @@ @@@         @@@@      @@    @@   @@          @@     @@    ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@@@@@@      ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@@@@@@      ||
* ||   @@ @@@         @@@@       @@  @@    @@          @@    @@@    ||
* ||   @@  @@@      @@@  @@@      @@@@     @@          @@     @@@   ||
* ||   @@   @@@    @@@    @@@     @@@@     @@          @@      @@   ||
* ||   @@    @@@   @@      @@      @@      @@          @@      @@   ||
* ||   @@     @@@  @@      @@      @@      @@          @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1353>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFRWRD   JSB  =VFBSY+          
         LDBD R57,X36,VF.RSW
         DCB  R57              
         JZR  RDMODE
         LDB  R57,=VFREAD          
         STBD R57,R2           
         JSB  =VFRREC
         REN
         LDBD R50,X36,VF.LOC
         TSB  R50              
         IFNZ
           JSB  =VFLAD+          
           LDB  R57,=3           
           JSB  =DDLRP+          
           LDB  R57,R50          
           JSB  =DATRP+          
           JSB  =VFTAD+          
         ENDIF
RDMODE   CLB  R20              
         JSB  =VFWACH
         REN
         JSB  =VFBSY+          
         JSB  =VFADDR
         RTN                   

VFWACH   CLB  R57              
         JSB  =DDTREP
         REN
         LDM  R56,=SDA
         JSB  =RDYSD+          
VFWAC2
krvfr_0  TSB  R20              
         IFZR
           PUMD R57,+R46         
           LDM  R2,R44           
           DCM  R2               
           STM  R2,R44           
         ELSE
           DCM  R45              
         ENDIF
         JZR  krvfr_3
         JSB  =DATSND
         CMM  R56,=ETO
         IFEQ
           JSB  =UNTUNL
           JSB  =VFBSY+          
           JMP  krvfr_4
         ENDIF
         JEZ  krvfr_0
         RTN                   
krvfr_3  PUMD R56,+R6          
         LDM  R56,=NRD
         JSB  =RDYSND          
         POMD R56,-R6          
         REN
         JSB  =DATSND
         REN
         CMM  R56,=ETO
         REQ
krvfr_4  JSB  =ERR1+           
         DATA 57D

VFRREC   JSB  =VFTAD+          
         LDB  R57,=2           
         JSB  =DDTREP
         RTN                   
       TITLE 'krvfw'
*
*  __________________________________________________________________
* |KRVFW 592 06/24/82 - 7/ 9/1982 1:59PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@   @@@    @@     @@@  @@      @@  @@          @@      @@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@      @@   ||
* ||   @@ @@@      @@     @@    @@    @@   @@          @@      @@   ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@   @@      @@   ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@   @@  @@  @@   ||
* ||   @@ @@@      @@    @@@     @@  @@    @@          @@  @@  @@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@          @@@@@@@@@@   ||
* ||   @@   @@@    @@      @@     @@@@     @@          @@@@  @@@@   ||
* ||   @@    @@@   @@      @@      @@      @@          @@@    @@@   ||
* ||   @@     @@@  @@      @@      @@      @@          @@      @@   ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFWOOP   JSB  =VFLTY+          
         JSB  =VFWREC
         JMP  krvfw_1
VFRWWR   JSB  =VFLTY+          
         JSB  =VFWRBK
krvfw_1  REN
         JSB  =VFWR            
         REN
         JSB  =VFADDR
         REN
         JSB  =VFLTBY          
         RTN                   

VFWR     LOOP
           POBD R57,+R46         
           JSB  =DATRP+          
           LDM  R2,R44           
           DCM  R2               
           STM  R2,R44           
         WHNZ
         RTN                   

VFWREC   LDBD R57,=VFWRTE
         STBD R57,X36,VF.RSW
VFDDL2   LDB  R57,=2           
         JMP  VFDDL

VFWRBK   LDBD R57,X36,VF.RSW
         RZR
         IFPS
           PUMD R45,+R6          
           LDMD R45,X36,VF.LOC
           DCM  R46              
           JSB  =VFRWSK          
           POMD R45,-R6          
           REN
         ENDIF
         LDB  R57,=VFWRTE
         STBD R57,X36,VF.RSW
         LDB  R57,=6           
         JMP  VFDDL

VFADCL   JSB  =VFADDR
         REN
         LDMD R55,X36,VF.LOC
         TSB  R55              
         RZR
         JSB  =VFLAD+          
VFWRCL   LDB  R57,=8D
VFDDL    JSB  =DDLREP          
         RTN                   
       TITLE 'krvfb'
*
*  __________________________________________________________________
* |KXVFB 582 06/24/82 - 7/ 9/1982 2:00PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@     ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@@    ||
* ||   @@   @@@    @@@    @@@  @@      @@  @@          @@     @@@   ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@          @@      @@   ||
* ||   @@ @@@         @@@@      @@    @@   @@          @@     @@@   ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@@@@@@@     ||
* ||   @@@@@           @@       @@    @@   @@@@@@@@@   @@@@@@@@     ||
* ||   @@ @@@         @@@@       @@  @@    @@          @@     @@@   ||
* ||   @@  @@@      @@@  @@@      @@@@     @@          @@      @@   ||
* ||   @@   @@@    @@@    @@@     @@@@     @@          @@     @@@   ||
* ||   @@    @@@   @@      @@      @@      @@          @@@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@          @@@@@@@@     ||
* ||                                                                ||
* ||                  Last edited on <820908.1353>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFLTBY   JSB  =VFBSY+          
         JSB  =LADREP          
         RTN                   
VFBSY    JSB  =VFSTAT
         REN
         JSB  =VFERR
         RTN                   
VFSTAT   JSB  =VFTAD+          
krvfb_1  LDM  R56,=SST
         JSB  =RDYSD+          
         ANM  R56,=0E0H,0FFH
         CMM  R56,=SST
         IFEQ
           JSBN =ERR1+
           DATA 56D
         ENDIF
         DRP  !56
         PUMD R56,+R6
         LDB  R50,=10D
         LOOP
           JSB  =DATSND
           JEN  krvfb_3
           CMM  R56,=ETO
           JEQ  krvfb_3
           DCB  R50              
         WHNZ
         ICE                   
krvfb_3  POMD R56,-R6          
         REN
         STM  R56,R2           
         ANM  R3,=BIT#5
         JNZ  krvfb_1
         RTN                   

VFERR    TSB  R57              
         RZR
         CMB  R57,=00010111B
         REQ
         LDM  R30,=(ERRTAB).2
         LOOP
           POMD R20,+R30         
           CMB  R21,R57          
           IFEQ
             CLB  R21              
           ENDIF
           TSB  R21              
         WHNZ
         JSB  =ERRORR          
         STE                   
         RTN                   

ERRTAB   DATA 96D
         DATA 00010001B

         DATA 96D
         DATA 00010010B

         DATA 96D
         DATA 00010011B

         DATA 94D
         DATA 00010100B

         DATA 96D
         DATA 00011000B

         DATA 96D
         DATA 00011001B

         DATA 96D
         DATA 00011010B

         DATA 93D
         DATA 00000000B
       TITLE 'krvfu'
*
*  __________________________________________________________________
* |KRVFU 590 6/24/82 - 7/ 9/1982 2:07PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@   @@@    @@     @@@  @@      @@  @@          @@      @@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@      @@   ||
* ||   @@ @@@      @@     @@    @@    @@   @@          @@      @@   ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@   @@      @@   ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@   @@      @@   ||
* ||   @@ @@@      @@    @@@     @@  @@    @@          @@      @@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@          @@      @@   ||
* ||   @@   @@@    @@      @@     @@@@     @@          @@@    @@@   ||
* ||   @@    @@@   @@      @@      @@      @@           @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@            @@@@@@     ||
* ||                                                                ||
* ||                  Last edited on <820908.1331>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFRCEX   JSB  =VFRREC
         REN
         JSB  =VFEXCH
         RTN                   
VFRWU0   JSB  =VFRWK+          
         JSB  =VFWBU0
         RTN                   
VFCDEP   LDM  R#,R36           
         ADM  R#,=(VF.CDE).2
         ARP  !36
         RTN                   
VFCD46   LDM  R44,=32D,0,0,0    
         DRP  R46              
         JSB  =VFCDEP
         RTN                   
         JSB  =VFCDEP
         LDM  R32,=(32D).2
         JSB  =COPY            
         RTN                   
       TITLE 'krvf1'
*
*  __________________________________________________________________
* |KRVF1 567 06/24/82 - 7/ 9/1982 2:08PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@      @@       ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@     @@@       ||
* ||   @@   @@@    @@     @@@  @@      @@  @@            @@@@       ||
* ||   @@  @@@     @@      @@  @@      @@  @@           @@@@@       ||
* ||   @@ @@@      @@     @@    @@    @@   @@              @@       ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@       @@       ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@       @@       ||
* ||   @@ @@@      @@    @@@     @@  @@    @@              @@       ||
* ||   @@  @@@     @@     @@@     @@@@     @@              @@       ||
* ||   @@   @@@    @@      @@     @@@@     @@              @@       ||
* ||   @@    @@@   @@      @@      @@      @@          @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@      @@      @@          @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1358>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFTERM   JEN  VFBYE
         JSB  =VFLAD+          
         LDB  R57,=7D          
         JSB  =DDLREP          
VFBYE    LDB  R2,=1            
         STBD R2,=NDATTN       
         JSB  =UNTUNL
         CLB  R2               
         STBD R2,=NDATTN       
         RTN                   

VFDIR    LDMD R46,X36,VF.DL
         CLB  R45              
         STMD R45,X36,VF.CDL
         JSB  =VFRWSK          
         REN
         JMP  VFNXD-

VFNXDE   LDMD R45,X36,VF.CDL
         ADM  R45,=32D,0,0      
         STMD R45,R2           
VFNXD-   JSB  =VFCD46
         JSB  =VFRWRD          
         RTN                   

VFDECL   JSB  =VFWRDE
         REN
         JSB  =VFCLCH
         RTN                   

VFWRDE   LDMD R45,X36,VF.CDL
VFWRD1   JSB  =VFRWK+          
VFWRD-   JSB  =VFCD46
         JSB  =VFRWWR          
         RTN                   

VFEOD?   JSB  =VFLED?
         RZR
VFPED?   JSB  =VFGLOC
         DRP  !46
         ARP  !56
         SBM  R46,R56            
         LDMD R56,X36,VF.BIG
         CMM  R46,R56          
         RTN                   

VFLED?   JSB  =VFPED?
         IFZR
           TSM  R6               
         ELSE
           LDMD R46,X36,VF.FTY
           ICM  R46              
         ENDIF
         RTN                   

VFGLOC   LDMD R56,X36,VF.DL
         LDMD R45,X36,VF.CDL
         DRP  R46              
         ARP  R56              
         RTN                   

VFMFP?   LDMD R20,X36,(VF.CDE)+10D
         RTN                   

VFRENA   STMD R40,X36,VF.CDE
         LDM  R46,='  '
         STMD R46,X36,(VF.CDE)+8D
         RTN                   

VFMOVE   CMM  R66,R62          
         REQ
krvf1_1  CLB  R45              
         LDM  R46,R62          
         JSB  =VFRWK+          
         JSB  =VFRCEX          
         REN
         JSB  =VFRCEX          
         REN
         LDM  R46,R62          
         ICM  R46              
         ICM  R46              
         STM  R46,R62          
         STM  R66,R46          
         ICM  R66              
         ICM  R66              
         CLB  R45              
         JSB  =VFRWU0
         REN
         LDM  R2,R64           
         DCM  R2               
         STM  R2,R64           
         RZR
         JSB  =VFEXCH
         REN
         JSB  =VFWBU0
         REN
         LDM  R2,R64           
         DCM  R2               
         STM  R2,R64           
         JNZ  krvf1_1
         RTN                   

VFEXCH   JSB  =VFLAD+          
         LDB  R57,=10D
         JSB  =DDLREP          
         RTN                   

VFWBU0   JSB  =VFLAD+          
         JSB  =VFDDL2
         REN
         JSB  =VFWRCL
         RTN                   
       TITLE 'krvf2'
*
*  __________________________________________________________________
* |KRVF2 573 06/24/82 - 7/ 9/1982 2:08PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@     @@@@      ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@   @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@      @@  @@          @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@                  @@   ||
* ||   @@ @@@      @@     @@    @@    @@   @@                 @@@   ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@         @@@    ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@       @@@      ||
* ||   @@ @@@      @@    @@@     @@  @@    @@            @@@        ||
* ||   @@  @@@     @@     @@@     @@@@     @@           @@@         ||
* ||   @@   @@@    @@      @@     @@@@     @@          @@@          ||
* ||   @@    @@@   @@      @@      @@      @@          @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@      @@      @@          @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1336>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFROO?   LDMD R20,X36,VF.FTY
         LDM  R56,=(VFTRTB).2      
         LOOP
           POMD R45,+R56         
           JZR  krvf2_1
           CMM  R46,R20          
         WHNE
         STB  R45,R21          
         CLB  R45              
         RTN                   

krvf2_1  JSB  =HANDI0          
         VAL  V.RFTY
         CLB  R2               
         IFEN
           ICB  R2               
         ENDIF
         CLE                   
         RTN                   

VFLIF?   LDMD R20,X36,VF.FTY
         DCM  R20              
         RTN                   

VFRLF?   LDMD R22,X30,DR.TYP
         CMM  R22,=TYLIF1      
         RTN                   

VFRVDE   LDM  R20,R36          
         ADM  R20,=(VF.FTY).2
         JSB  =REVBYT          
         DRP  !20
         ADM  R20,=((VF.CST)-(VF.FTY)).2
         JSB  =REVBYT          
         DRP  !20
         ADM  R20,=((VF.CLN)-(VF.CST)).2           
         JSB  =REVBYT          
         RTN                   

VFMWG    JSB  =UNTUNL
         JSB  =MSSOUT          
         JSB  =UNTUNL
         RTN                   

VFSKFL   CLB  R45              
         LDMD R46,X36,VF.CST
         JSB  =VFRWSK          
         RTN                   

VFDUDE   DRP  R26              
         JSB  =VFCDEP
         STB  R20,R40          
         LDM  R41,R40          
         PUMD R40,+R26         
         PUMD R40,+R26         
         PUMD R40,+R26         
         PUMD R40,+R26         
         LOOP
           PUBD R21,+R6          
           JSB  =VFWRD-
           POBD R21,-R6          
           REN
           DCB  R21              
         WHNZ
         JSB  =VFCLCH
         RTN                   

VFTRNL   CLE                   
         LDBD R21,X30,DR.TNM   
         LDM  R56,=(VFTRTB).2     
         LOOP
           POMD R45,+R56         
           JZR  XPLUS
           CMB  R45,R21          
         WHNE
         JMP  krvf2_11
XPLUS    JSB  =HANDI           
         VAL  V.LFTY
         DATA  68D
krvf2_11 STMD R46,X36,VF.FTY
         RTN                   
VFTRTB   
         VAL  TYNLI1
LABL0    ADDR  1D
         DEF  LABL0

         VAL  TYNBAS
LABL1    EQU  -20000+210
         DEF  LABL1

         VAL  TYNLEX
LABL2    EQU  -20000+211
         DEF  LABL2

         VAL  TYNSYS
LABL9    EQU  -20000+121
         DEF  LABL9

         VAL  TYNTEX
LABL10   EQU  -20000+122
         DEF  LABL10

         VAL  TYNAPP
LABL11   EQU  -20000+123
         DEF  LABL11
         BSS  3D
   
       TITLE 'krvr5'
*
*  __________________________________________________________________
* |KRVR5 NA                                                          |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@    @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@   @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@      @@  @@     @@@  @@           ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@           ||
* ||   @@ @@@      @@     @@    @@    @@   @@     @@   @@           ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@     @@@@@@@@     ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@     @@@@@@@@@@   ||
* ||   @@ @@@      @@    @@@     @@  @@    @@    @@@          @@@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@     @@@  @@      @@   ||
* ||   @@   @@@    @@      @@     @@@@     @@      @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@      @@      @@      @@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@      @@    @@@@@@     ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* MELROM VERSION CODE ('a')
* ********************************************************************
         DATA  'd'              
       TITLE 'krsum'
*
*  __________________________________________________________________
* |KRSUM NA                                                          |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@      @@@@@@    @@      @@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@   @@      @@  @@@    @@@   ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@      @@  @@@@  @@@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@@@@@@@@@   ||
* ||   @@ @@@      @@     @@   @@@         @@      @@  @@  @@  @@   ||
* ||   @@@@@       @@@@@@@      @@@@@@@    @@      @@  @@  @@  @@   ||
* ||   @@@@@       @@@@@@@       @@@@@@@   @@      @@  @@      @@   ||
* ||   @@ @@@      @@    @@@          @@@  @@      @@  @@      @@   ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@  @@      @@   ||
* ||   @@   @@@    @@      @@  @@@     @@  @@@    @@@  @@      @@   ||
* ||   @@    @@@   @@      @@   @@@@@@@@    @@@@@@@@   @@      @@   ||
* ||   @@     @@@  @@      @@    @@@@@@      @@@@@@    @@      @@   ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* MELROM CHECKSUM BYTE
* ********************************************************************
*        DATA  037H
         DATA  1AH  ; checksum for single source file
       TITLE 'krvf3'
*
*  __________________________________________________________________
* |KRVF3 578 06/24/82 - 7/ 9/1982 2:10PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@     @@@@  @   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@   @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@      @@  @@          @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@      @@   ||
* ||   @@ @@@      @@     @@    @@    @@   @@                @@@    ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@      @@@@      ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@        @@@@    ||
* ||   @@ @@@      @@    @@@     @@  @@    @@                  @@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@                  @@   ||
* ||   @@   @@@    @@      @@     @@@@     @@                  @@   ||
* ||   @@    @@@   @@      @@      @@      @@           @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@             @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFTIME   LDM  R43,R44          
         CLB  R47              
         LDM  R50,R20          
         PUMD R50,+R6          
         JSB  =SYSJSB          
         ARP  R60              
         DRP  R51              
         POMD R50,-R6          
         STM  R50,R20          
         PUBD R45,+R32         
         PUBD R44,+R32         
         PUBD R43,+R32         
         PUBD R42,+R32         
         PUBD R41,+R32         
         PUBD R40,+R32         
         RTN                   
       TITLE 'krvf4'
*
*  __________________________________________________________________
* |KRVF4 579 06/24/82 - 7/ 9/1982 2:10PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@        @@     ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@       @@@     ||
* ||   @@   @@@    @@     @@@  @@      @@  @@              @@@@     ||
* ||   @@  @@@     @@      @@  @@      @@  @@             @@@@@     ||
* ||   @@ @@@      @@     @@    @@    @@   @@            @@@ @@     ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@    @@@  @@     ||
* ||   @@@@@       @@@@@@@      @@    @@   @@@@@@@@@   @@@   @@     ||
* ||   @@ @@@      @@    @@@     @@  @@    @@          @@@@@@@@@@   ||
* ||   @@  @@@     @@     @@@     @@@@     @@          @@@@@@@@@@   ||
* ||   @@   @@@    @@      @@     @@@@     @@                @@     ||
* ||   @@    @@@   @@      @@      @@      @@                @@     ||
* ||   @@     @@@  @@      @@      @@      @@                @@     ||
* ||                                                                ||
* ||                  Last edited on <820908.1358>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
VFRDE    LDMD R40,X36,VF.CDE
         STMD R40,X36,(VF.RDE)+(DR.NAM)
         CLM  R46              
         LDM  R2,R36           
         ADM  R2,=(VF.CTC).2
         POBD R45,+R2          
         POBD R44,+R2          
         POBD R43,+R2          
         POBD R42,+R2          
         POBD R41,+R2          
         POBD R40,+R2          
         TSM  R40              
         IFNZ
           PUMD R24,+R6          
           JSB  =SYSJSB          
             DEF ENCLOK
           POMD R24,-R6          
           LDM  R54,R43          
           STM  R54,R44          
         ENDIF
         STMD R44,X36,(VF.RDE)+(DR.DAT)
         JSB  =VFROO?          
         IFZR
           LDB  R20,=((TYPUR?)+(TYCOP?)).2
         ELSE
           LDM  R20,=
              DATA ((TYPUR?)+(TYCOP?)).1
              DATA (TYN??).1
         ENDIF
         STMD R20,X36,(VF.RDE)+(DR.TYP)
         LDB  R20,=' '
         CLM  R40              
         LDMD R46,X36,VF.CLN
         CMM  R45,=(10000D).3
         IFHS
           JSB  =TENRIT
           LDB  R20,='K'
           CMM  R45,=(1000D).3
           IFHS
             JSB  =TENRIT
             LDB  R20,='M'
           ENDIF
         ENDIF
         LDM  R56,R45          
         STMD R56,X36,(VF.RDE)+(DR.SIZ)
         RTN                   

VF1TO2   LDM  R30,R36          
         ADM  R30,=(VF.2DE).2
         DRP  R34              
         JSB  =VFCDCO
         RTN                   

VFSECT   LDMD R20,X30,DR.SIZ
         JSB  =VFRLF?
         IFNZ
           ADM  R20,=(DRENSZ).2
         ENDIF
         TSB  R20              
         IFNZ
           ICB  R21              
         ENDIF
         STB  R21,R20          
         CLB  R21              
         RTN                   
       TITLE 'krpin'
*
*  __________________________________________________________________
* |KRPIN 367 06/24/82 - 7/ 9/1982 2:10PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@@@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@@  @@      @@   ||
* ||   @@   @@@    @@     @@@  @@     @@@      @@      @@@     @@   ||
* ||   @@  @@@     @@      @@  @@      @@      @@      @@@@    @@   ||
* ||   @@ @@@      @@     @@   @@     @@@      @@      @@ @@   @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@       @@      @@  @@  @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@@        @@      @@  @@  @@   ||
* ||   @@ @@@      @@    @@@   @@              @@      @@   @@ @@   ||
* ||   @@  @@@     @@     @@@  @@              @@      @@    @@@@   ||
* ||   @@   @@@    @@      @@  @@              @@      @@     @@@   ||
* ||   @@    @@@   @@      @@  @@          @@@@@@@@@@  @@      @@   ||
* ||   @@     @@@  @@      @@  @@          @@@@@@@@@@  @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
DDLREP   ADB  R57,=DDL_
         JMP  CMDJMP
DDTREP   ADB  R57,=DDT_
CMDJMP   JSB  =CMDREP          
         RTN                   

DATSND   CLB  R56              
DATSND-  LDB  R55,=120         
         JSB  =SNDFRM          
         ANM  R56,=0FFE0H
         REZ
         DCE                   
         IFEN
           LDBD R2,=KEYHIT       
           CMB  R2,=ATTNKY
           IFNZ
             ICE                   
             JSB  =PILREP          
           ENDIF
         ENDIF
         RTN                   

UNTUNL   JSB  =UNTREP          
         JSB  =UNLREP          
         RTN                   
       TITLE 'krfut'
*
*  __________________________________________________________________
* |KRFUT 220 06/24/82 - 7/ 9/1982 2:10PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@          @@      @@      @@       ||
* ||   @@  @@@     @@      @@  @@          @@      @@      @@       ||
* ||   @@ @@@      @@     @@   @@          @@      @@      @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@      @@      @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@   @@      @@      @@       ||
* ||   @@ @@@      @@    @@@   @@          @@      @@      @@       ||
* ||   @@  @@@     @@     @@@  @@          @@      @@      @@       ||
* ||   @@   @@@    @@      @@  @@          @@@    @@@      @@       ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@       @@       ||
* ||   @@     @@@  @@      @@  @@            @@@@@@        @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1332>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
JSBCRT   JSB  =SYSJSB          
           DEF CRTMDT
         RTN                   
*
REVBYT   LDMD R2,R20           
         PUBD R3,+R20          
         STBD R2,R20           
         DCM  R20              
         RTN                   
*
REVPSH   PUBD R47,+R32         
         PUBD R46,+R32         
         PUBD R45,+R32         
         PUBD R44,+R32         
         RTN                   
*
TENRIT   ADM  R45,=512D,0
         LDB  R2,=10D           
         LOOP
           LRM  R47              
           DCB  R2               
         WHNZ
         RTN                   
       TITLE 'krtfm'
LINLEN EQU 0FEH
EOL    ADDR 0C7CH
*
*  __________________________________________________________________
* |GCTFM 484 06/24/82 - 7/14/1982 8:02AM                             |
* |==================================================================|
* ||                                                                ||
* ||      @@@@        @@@@     @@@@@@@@@@  @@@@@@@@@@  @@      @@   ||
* ||    @@@@@@@@    @@@@@@@@   @@@@@@@@@@  @@@@@@@@@@  @@@    @@@   ||
* ||   @@@    @@@  @@@    @@@      @@      @@          @@@@  @@@@   ||
* ||   @@      @@  @@      @@      @@      @@          @@@@@@@@@@   ||
* ||   @@          @@              @@      @@          @@  @@  @@   ||
* ||   @@          @@              @@      @@@@@@@@@   @@  @@  @@   ||
* ||   @@   @@@@@  @@              @@      @@@@@@@@@   @@      @@   ||
* ||   @@   @@@@@  @@              @@      @@          @@      @@   ||
* ||   @@      @@  @@      @@      @@      @@          @@      @@   ||
* ||   @@@    @@@  @@@    @@@      @@      @@          @@      @@   ||
* ||    @@@@@@@@    @@@@@@@@       @@      @@          @@      @@   ||
* ||      @@@@        @@@@         @@      @@          @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1416>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
TRNSLP   JSB  =SYSJSB          
           DEF STREX+
         CMB  R14,=INTOTK
         JNE  TERROR
         JSB  =SFSCAN          
         CMB  R47,=46          
         JEQ  KDONE

TERROR   JSBN  =ERROR+          
         DATA  78D

KDONE    PUBD R14,+R12         
         LDB  R14,=INTOTK
         PUBD R14,+R12         
         LDM  R44,=
           VAL EROMTK
           DEF MELROM
           VAL TRFTOK
         PUMD R44,+R12         
         JSB  =SFSCAN          
         RTN                   

CONAS-   JSB  =MYSTPR
         ADM  R26,=(PCBLEN).2
         SBMD R10,=RNFILE      
         PUMD R10,+R6          
         PUBD R16,+R6          
         CLB  R16              
         JSB  =BLIMP           
LBL2     LDM  R30,R26          
         JSB  =SKPLN#          
         POMD R22,+R26         
         CMMD R22,=ENLIN#
         JEQ  NEWNAM
         LDB  R22,=CR
         JSB  =MALLOC
         POBD R32,+R26         
         ICB  R32              
         PUBD R32,+R6          
         PUMD R26,+R6          
         STM  R26,R10          
         JSB  =INIPR-          
         DRP  !12
         PUMD R12,+R6           
         DCM  R12               
         STMD R12,=STSIZE       
         ICM  R12               
         PUMD R30,+R6          
         JSB  =SYSJSB          
           DEF PARSIT
         JSB  =EOL             
         JSB  =ANYER?          
         POMD R26,-R6          
         STMD R26,=KLUDGE      
         JEN  TROUBL
         POMD R26,-R6          
         POMD R30,-R6          
         LDM  R32,R12          
         SBM  R32,R26          
         TSB  R33              
         JNZ  krtfm_1
         JSB  =ALLDC           
         JEN  WHY??
         DRP  !30
         DCM  R30              
         PUBD R32,+R30         
         ADM  R26,R32          
         JSB  =PUTCHR
         DRP  !32
         POBD R32,-R6           
         JSB  =DELETE          
         LDMD R26,=KLUDGE      
LBL3     LDMD R12,=TOS         
         JMP  LBL2

NEWNAM   CMM  R22,=ENDLIN      
         JEQ  FINUP
         JSB  =PCR.
         DRP  !2
         LDBD R2,=MISSNG       
         JZR  MEMER2
         JSBN  =ERR1+           
         DATA  18D

krtfm_1  JSB  =TYER1+
WHY??    POBD R2,-R6           
         JSB  =PCR.
         DCM  R30              
         JSB  =SETL30
         LDMD R30,=KLUDGE      
         DCM  R30              
         LDBD R32,R30          
         CMB  R32,=CR
         JNE  WHY??+
         CLM  R32              
         ICM  R32              
         JSB  =DELETE          
WHY??+   JSB  =BAS_AS
         LDBD R#,=ORIGIN       
         RZR
         JSB  =BASLI-
         RTN                   

TROUBL   JSB  =CLRERR          
         POMD R12,-R6          
         POMD R30,-R6          
         LDM  R32,=(FOUR).2
         JSB  =ROOM?           
         JEN  WHY??
         CLB  R22              
         ICB  R22              
         STBD R22,=PARERR      
         POBD R22,-R6          
         STB  R22,R34          
         ADB  R22,=FOUR
         PUBD R22,-R30         
         POBD R22,+R30         
         JSB  =ALLDC           
         LDMD R26,=KLUDGE      
         DCM  R26              
         LDM  R44,=
           VAL BANGTK
           DATA 6
           DATA 0
           DATA 3FH

         LDB  R46,R34          
         STMD R44,R30          
         LDB  R44,=0EH
         PUBD R44,+R26         
         JMP  LBL3

FINUP    JSB  =MYSTPR
         DRP  !2
         LDM  R2,=TYBASC
         JSB  =EDITFI
         JSB  =PCR.
         LDBD R#,=PARERR       
         RZR
         JSBN  =ERROR+          
         DATA  78D

MEMER2   JSB  =ERR1+           
         DATA 16D

CLIF     LDM  R32,=((PCBLEN)+3).2
         JSB  =ROOM!           
         JEN  krtfm_0
         JSB  =MBLIM-
         JSB  =MYSTPR
         ARP  !30
         POMD R32,-R30         
         ADM  R32,R26          
         LDM  R24,R26          
         JMP  NEWSKR

TRASHR   POBD R23,+R24         
         POBD R22,+R24         
         CMM  R22,=(LINLEN).2
         IFCY
krtfm_0    CLE                   
           RTN                   
         ENDIF

         LDB  R2,=4            
         LOOP
           POBD R20,+R24         
           JSB  =DIGIT           
           IFEZ
             ICE                   
             RTN                   
           ENDIF
           DCB  R2               
         WHNZ
         POMD R44,-R24         
         TSB  R22              
         IFOD
           ICB  R#              
         ENDIF
         ADM  R24,R22          
         CMM  R24,R32          
         IFEQ
           ARP  !32
           LDM  R30,R32          
           LDM  R32,=(TWO).2
           JSB  =ALLDC           
           LDM  R22,=0FFH,0FFH
           STMD R22,R30          
           JMP  NOTRSH
         ENDIF

NEWSKR   LDMD R22,R24          
         CMM  R22,=0FFH,0FFH
         JNE  TRASHR
         ICM  R24              
         ICM  R24              
         STM  R24,R30          
         SBM  R32,R24          
         JSB  =DELETE          

NOTRSH   JSB  =MYSET2
         JSB  =ALLDC           
         CLM  R43              
         PUMD R43,+R30         
         PUMD R43,+R30         
         LDM  R26,R30          

CLIF+    LDMD R34,R26          
         CMMD R34,=ENLIN#
         REQ
         POBD R35,+R26         
         POBD R34,+R26         
         CMM  R34,=0FFH,0FFH
         JEQ  LIFEND
         TSB  R34              
         IFOD
           LDM  R30,R26          
           ADM  R30,R34          
           CLM  R32              
           ICM  R32              
           JSB  =DELETE          
           DRP  !30
           LDM  R30,R26           
           DCM  R30               
           DCM  R30               
         ENDIF
         SBB  R34,=FOUR          
         JSB  =ASTBCD
         LDM  R32,=3,0
         JSB  =DELETE          
         DRP  !30
         STM  R30,R26           
         PUMD R22,+R26         
         PUBD R34,+R26         
         ADM  R26,R34          
         STM  R26,R30          
         JMP  CLIF+

LIFEND   LDM  R32,=(THREE).2
         ARP  !26
         LDM  R30,R26          
         JSB  =ALLOC           
         DRP  !30
         PUMD R30,-R26          
         LDM  R30,=ENDLIN
         PUMD  R30,+R26
         LDB  R30,=2            
         PUBD R30,+R26          
         LDM  R30,=8AH,0EH
         PUMD R30,+R26          
         JSB  =MYSTPR
         DRP  !2
         ARP  !30
         LDM  R2,=TYTEXT
         PUMD R2,+R30          
         CLE                   
         ICE                   
         CLB  R2              
         RTN                   

BAS_AS   JSB  =MYSTPR
         ADM  R26,=(PCBLEN).2
         STM  R26,R24          
LBL4     LDMD R22,R24          
         CMMD R22,=ENLIN#
         JEQ  END-
         POMD R45,+R24         
         LDM  R67,=7EH
         JSB  =RECON!
         JEN  LBL4
         PUMD R24,+R6          
         LDM  R30,=INPBUF      
         PUBD R17,+R6          
         CLB  R17              
         JSB  =SYSJSB          
         DEF  DECOM
         IFNG
           DRP !17
           STBD R17,=MISSNG      
           POBD R17,-R6          
           CLB  R17              
           POMD R30,-R6          
           JMP  OUTR
         ENDIF
         DRP  !17
         POBD R17,-R6          
         STMD R24,=KLUDGE      
         LDM  R34,=INPBUF      
         POMD R26,-R6          
         LOOP
           POBD R36,+R34         
           CMB  R36,=20H
         WHNE
         PUBD R36,-R34         
         SBM  R30,R34          
         STM  R30,R32          
         LDM  R30,R26          
         JSB  =ALLDC           
         IFEN
OUTR       DRP  !30
           DCM  R30              
           JSB  =SETL30
           JSB  =CLRERR          
           GTO CONAS-
         ENDIF
         DRP !30
         DCM  R30               
         LDBD R20,R30          
         PUBD R32,+R30         
         LDBD R26,=DCOVFL      
         ARP  R34              
         IFNZ
           LDB  R26,='?'
           STBD R26,R34          
         ENDIF
         LDM  R26,R34          
         JSB  =PUTCHR
         DRP !32
         LDB  R32,R20           
         JSB  =DELETE          

         JSB  =BLIMP           
         LDMD R24,=KLUDGE      
         JMP  LBL4

END-     CMM  R22,=ENDLIN      
         JNE  MEMERR           

ENDIT    JSB  =MYSTPR
         DRP  !2
         LDM  R2,=TYTEXT
         JSB  =EDITFI
         CLE                   
         RTN                   

TYPLIF   DRP  !2
         CMM  R2,=TYLIF1
         JNE  BADTYP           
         JSB  =CLIF
         IFEZ
TYER1+     JSBN  =ERR1+           
           DATA  67D
         ENDIF
         CLE                   
         DRP  !2
         TSB  R2               
         JZR  HRE
         JSBN  =ERR1+           
         DATA  88D

HRE      DRP  !2
         ICB  R2
         STBD R2,=ORIGIN      
         RTN                   

MEMERR   JSBN  =ERROR+          
         DATA  16D

BADNAM   JSBN  =ERROR+          
         DATA  63D

BADTYP   JSBN  =ERR1+           
         DATA  68D

         DATA  241
TRFRM.   CLB  R20              
         STBD R20,=MISSNG      
         STBD R20,=ORIGIN      
         STBD R20,=PARERR      
         POMD R20,-R12         
         JSB  =MYGETN
         JEN  BADNAM
         CMM  R20,R2           
         REQ
         DRP  !20
         CMM  R20,=TYTEXT      
         IFEQ
           CMM  R2,=TYBASC       
           IFEQ
THERE        JSB  =MBLIMP
             REN
             GTO BAS_AS
           ENDIF
           JSB  =TYPLIF
           RTN                   
         ENDIF
         DRP  !20
         CMM  R20,=TYBASC
         IFEQ
           CMM  R2,=TYTEXT
           IFEQ
THERE1       JSB  =MBLIMP
             REN
HHERE        GTO CONAS-
           ENDIF
           JSB  =TYPLIF
           REN
           JSB  =MBLIMP
           JEN  BASLI-
           JMP  HHERE
         ENDIF
         DRP  !20
         CMM  R20,=TYLIF1
         JNE  BADTYP
         CMMD R40,=DFNAME      
         JEQ  BADNAM
         CLB  R71              
         CMM  R2,=TYTEXT       
         JEQ  BASLIF
         CMM  R2,=TYBASC       
         JNE  BADTYP           
         JSB  =THERE
         REN

BASLI-   ICB  R71              

BASLIF   JSB  =MYSET2
         JSB  =DELETE          
         JMP  IVIDEA
OLOOP    LDM  R32,=(FOUR).2
         JSB  =ROOM?           
         IFEN
           POMD R2,+R30          
           JSB  =SETL30
           JSB  =ER16+
           RTN                   
         ENDIF
         LDM  R36,R26          
         JSB  =SKPLN           
         STMD R#,=KLUDGE       
         DCM  R32              
         JSB  =ALLDC           
         POMD R45,+R30         
         CLB  R32              
         LDB  R33,R47          
         ADB  R33,=4           
         PUMD R32,+R26         
         LDB  R20,R46          
         JSB  =TOASC2          
         PUMD R#,+R26          
         LDB  R#,R45           
         JSB  =TOASC2          
         PUMD R#,+R26          
         LDMD R30,=KLUDGE      
         TSB  R33              
         IFOD
           JSB  =MALLOC
         ENDIF

IVIDEA   LDMD R22,R30          
         CMM  R22,=ENDLIN      
         JZR  CLERUP
         LDM  R26,R30          
         JMP  OLOOP

CLERUP   LDM  R32,=0FFH,0FFH
         PUMD R32,+R30         
         LDM  R32,R30          
         JSB  =MYSTPR
         ARP  !30
         STM  R32,R30           
         SBM  R32,R26          
         TCB  R32              
         CLB  R33              
         JSB  =ALLDC           

         IFEN
           POMD R20,-R30         
           LDM  R20,=ENDLIN      
           PUMD R20,+R30         
           STMD R20,=ENLIN#
           JSB  =ER16+
           RTN                   
         ENDIF
         ADM  R#,R32           
         LDB  R32,=THREE
         JSB  =DELETE          

         JSB  =MYSTPR
         LDM  R#,=TYLIF1
         JSB  =EDITFI
         RTN                   
       TITLE 'krutl'
*
*  __________________________________________________________________
* |GCUTL 545 06/24/82 - 7/14/1982 8:04AM                             |
* |==================================================================|
* ||                                                                ||
* ||      @@@@        @@@@     @@      @@  @@@@@@@@@@  @@           ||
* ||    @@@@@@@@    @@@@@@@@   @@      @@  @@@@@@@@@@  @@           ||
* ||   @@@    @@@  @@@    @@@  @@      @@      @@      @@           ||
* ||   @@      @@  @@      @@  @@      @@      @@      @@           ||
* ||   @@          @@          @@      @@      @@      @@           ||
* ||   @@          @@          @@      @@      @@      @@           ||
* ||   @@   @@@@@  @@          @@      @@      @@      @@           ||
* ||   @@   @@@@@  @@          @@      @@      @@      @@           ||
* ||   @@      @@  @@      @@  @@      @@      @@      @@           ||
* ||   @@@    @@@  @@@    @@@  @@@    @@@      @@      @@           ||
* ||    @@@@@@@@    @@@@@@@@    @@@@@@@@       @@      @@@@@@@@@@   ||
* ||      @@@@        @@@@       @@@@@@        @@      @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
MYSTPR   LDMD R40,=PRNAME      
         JMP  LB1

MYGETN   JSB  =FLORD           
         REN
         JSB  =SYSJSB          
           DEF SAFE!

LB1      JSB  =SETPR           
         ADM  R30,=DR.TYP
         LDMD R2,R30           
         RTN                   

ASTBCD   POMD R20,+R26         
         JSB  =NUMCHK          
         STB  R21,R23          
         POMD R20,+R26         
         JSB  =NUMCHK          
         STB  R21,R22          
         RTN                   

MBLIMP
         JSB  =RESCON          
           DATA 255D
         REN
MBLIM-   JSB  =BLIMP
         LDM  R2,=ENDLIN       
         STMD R2,=ENLIN#
         RTN                   

PUTCHR   LOOP
           POBD R36,+R26         
           PUBD R36,+R30         
           DCB  R32              
         WHNZ
         RTN                   

SETL30   POMD R2,-R30          
         STMD R2,=ENLIN#
         JSB  =RELMEM          
         RTN                   

PCR.     POMD R2,-R6           
         POBD R16,-R6          
         POMD R10,-R6          
         ADMD R10,=RNFILE      
         PUMD R2,+R6           
         RTN                   

ER16+    JSB  =NOTRSH
         TSB  R71              
         JZR  NXT
         JSB  =THERE1
         JSB  =CLRERR          

NXT      JSBN  =ERROR+          
         DATA 16D

RECON!   CLE                   
         ARP  !24
         LDMD R54,R24          
         CLB  R56              
         CMM  R54,=BANGTK,6,0,3FH
         RNE
         LDM  R30,R24          
         LDM  R32,=(FOUR).2
         JSB  =DELETE          
         SBB  R47,=FIVE
         PUBD R47,-R30         
         STB  R47,R32          
         ADM  R30,R32          
         ICM  R30              
         LDB  R32,=ONE           
         JSB  =DELETE          
         DRP  !30
         STM  R30,R24           
         STM  R30,R26           
         ICE                   
         RTN                   

EDITFI   ARP  !30
         STMD R#,R30           
         CMMD R40,=EDNAME      
         IFEQ
           LDMD R20,R30          
           CMM  R20,=TYLIF1      
           IFEQ
             LDM  R20,=TYTEXT      
             LDMD R40,=DFNAME      
             TSB  R71              
             IFNZ
               LDM  R20,=TYBASC      
             ENDIF
             JSB  =SETED           
             JSB  =SYSJSB          
               DEF CATLIN
             RTN                   
           ENDIF
           JSB  =SETED           
         ENDIF
         JSB  =RELMEM          
         RTN                   

MALLOC   CLM  R32              
         ICM  R32              
         JSB  =ALLDC           
         REN
         PUBD R22,+R30         
         RTN                   

MYSET2   JSB  =MYSTPR
         ARP  !30
         STM  R26,R30           
         LDM  R32,=(PCBLEN).2
         RTN                   
       TITLE 'krtrg'
*
*  __________________________________________________________________
* |KRTRG 523 04/30/82 - 5/ 5/1982 9:43AM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@@@  @@@@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@      @@      @@     @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@      @@      @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@       @@      @@     @@   @@           ||
* ||   @@@@@       @@@@@@@         @@      @@@@@@@     @@           ||
* ||   @@@@@       @@@@@@@         @@      @@@@@@@     @@   @@@@@   ||
* ||   @@ @@@      @@    @@@       @@      @@    @@@   @@   @@@@@   ||
* ||   @@  @@@     @@     @@@      @@      @@     @@@  @@      @@   ||
* ||   @@   @@@    @@      @@      @@      @@      @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@      @@      @@      @@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@      @@     @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820908.1349>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
         DATA 40,55
ATN2.    CLM  R26              
         CLM  R22              
         JSB  =TWOR            
         JSB  =UT210           
         JSB  =SEP15           
ATN2.+   TSM  R40              
         JNZ  RTP50
         TSM  R50              
         JNZ  RTP52
         CLM  R40              
         PUMD R40,+R12         
         RTN                   

RTP52    JSB  =TRC7            
         STM  R70,R40          
         STB  R33,R22          
         GTO  BRT54
RTP50    TSB  R32              
         JRZ  RTP60
         LDB  R23,=9C
         STB  R23,R26          
         CLB  R32              
RTP60    JSB  =DIV20           
         JMP  BRT10
  
         DATA 20,55
ISIN.    LDM  R26,=0C,99C
         JMP  BRT5

         DATA 20,55
ICOS.    LDM  R26,=9C,99C
         JMP  BRT5

         DATA 20,55
ITAN.    LDM  R26,=0C,9C

BRT5     CLM  R22              
         JSB  =ONER            
         JSB  =SEP10           

BRT10    TSB  R32              
         JRZ  BRT12
         NCB  R22              
         TSB  R27              
         JRZ  BRT12
         TSB  R26              
         JRZ  BRT12
         LLB  R26              
         NCB  R23              
         CLB  R22              
BRT12    TSB  R37              
         JLZ  BRT70
         TSB  R27              
         JLZ  BRT30
         STM  R36,R24          
         PUMD R40,+R12         
         JSB  =BRT835          
         CLM  R34              
         STM  R40,R50          
         LRM  R57              
         ADB  R57,=10C
         TCM  R40              
         JCY  BRT20
         JSB  =SHF10           
         JSB  =MPY30           
         DCM  R36              
         JSB  =SQR30           
         LDM  R34,R24          
         POMD R50,-R12         
         JSB  =DIV20           
         JMP  BRT22
BRT72    TSB  R27              
         JLZ  BRT76
         JSBN  =ERROR+          
         DATA 11D
BRT76    JSB  =FTR53           
         NCB  R26              
         JMP  BRT30

BRT70    TSM  R36              
         JNZ  BRT72
         STM  R40,R50          
         JZR  BRT50
         SBB  R57,=10C
         TSM  R50              
         JNZ  BRT72
         TSB  R27              
         JLZ  BRT74
         NCB  R26              
         CLM  R40              
         JMP  BRT50
BRT74    LDMD R70,=DCON1       
         STM  R70,R40          
         DCM  R36              
         JMP  BRT50
BRT20    POMD R40,-R12         
         LDM  R36,R24          
BRT22    CLB  R32              
         CMB  R37,=50C
         JNC  BRT76
BRT30    STM  R40,R50          
         LDM  R34,R36          
         ADM  R34,=7C,0C
         JNC  BRT50
         CLM  R70              
         CLM  R40              
         ICB  R47              
         LRM  R57              
BRT32    STM  R50,R60          
         SBM  R50,R40          
         JNC  BRT34
         ICB  R70              
         STB  R36,R24          
BRT36    LRM  R67              
         LRM  R67              
         ICB  R24              
         JNZ  BRT36
         ADM  R40,R60          
         JMP  BRT32
BRT50    JSB  =TRC7            
         TSB  R26              
         JRZ  BRT52
         JSB  =BRT840          
         SBM  R40,R70          
         TCM  R40              
         JSB  =SHF10           
BRT52    TSB  R23              
         JRZ  BRT54
         JSB  =BRT840          
         ADM  R40,R70          
BRT54    STM  R36,R34          
         LDBD R25,=DRG         
         JPS  BRT60
         ICM  R34              
         ICM  R34              
         CLM  R36              
         STM  R40,R50          
         JSB  =DEGCNV          
BRT60    STB  R22,R32          
         GTO SHRONF            

BRT34    DCB  R36              
         LLM  R70              
         LDM  R50,R60          
         LLM  R50              
         DCB  R34              
         JCY  BRT32
         CLM  R34              
         CLE                   
         JSB  =DIV77           
         STM  R70,R50          
         LDM  R30,=(TBL3B).2
BRT40    POMD R70,-R30         
         LRM  R57              
         ICM  R36              
         JMP  BRT42

BRT44    DCB  R50              
         ADM  R40,R70          
         JNC  BRT42
         ICE                   
BRT42    TSB  R50              
         JRN  BRT44
         ERM  R47              
         TSM  R50              
         JZR  BRT50
         JMP  BRT40
       TITLE 'krwak'
*
*  __________________________________________________________________
* |KRWAK 595 07/14/82 - 7/20/1982 1:51PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@    @@@@@@    @@     @@@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@   @@@@@@@@   @@    @@@    ||
* ||   @@   @@@    @@     @@@  @@      @@  @@@    @@@  @@   @@@     ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@  @@@      ||
* ||   @@ @@@      @@     @@   @@      @@  @@      @@  @@ @@@       ||
* ||   @@@@@       @@@@@@@     @@      @@  @@@@@@@@@@  @@@@@        ||
* ||   @@@@@       @@@@@@@     @@  @@  @@  @@@@@@@@@@  @@@@@        ||
* ||   @@ @@@      @@    @@@   @@  @@  @@  @@      @@  @@ @@@       ||
* ||   @@  @@@     @@     @@@  @@@@@@@@@@  @@      @@  @@  @@@      ||
* ||   @@   @@@    @@      @@  @@@@  @@@@  @@      @@  @@   @@@     ||
* ||   @@    @@@   @@      @@  @@@    @@@  @@      @@  @@    @@@    ||
* ||   @@     @@@  @@      @@  @@      @@  @@      @@  @@     @@@   ||
* ||                                                                ||
* ||                  Last edited on <820813.1429>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
WAKEUP   JSB  =CLROFF          
         PUMD R53,+R6          
         LDB  R53,=3           
         LDB  R54,=32D          
AGAIN    LDM  R56,=300,0
         JSB  =IDYSND          
         IFEN
           IFNZ
             BCD                   
             ERB  R53              
             BIN                   
             DCB  R54              
             IFNZ
               JSB  =STBEEP          
               JMP  AGAIN
             ENDIF
           ENDIF
           BCD                   
           ELB  R53              
           BIN                   
           JSB  =PILREP          
           JMP  OUT
         ENDIF
         LDB  R57,=AAU_
         JSB  =CMDREP          
         JZR  OUT
         LDB  R55,=37          
         STBD R55,=PILADR      
         STBD R55,=PILR4       
         JEN  REP
         JSB  =ASPSND
         IFEN
           DCE                   
           IFEZ
             LDM  R2,R56           
             ANM  R2,=0E0H,0E0H
             CMM  R2,=0A0H,080H
             JNE  krwak_1
             ANM  R57,=1FH
             CMB  R57,=1FH
             IFEQ
               JSB  =ASPSND
               IFEZ
                 LDB  R57,=1FH
                 JMP  krwak_2
               ENDIF
               DCE                   
               IFEZ
                 JSB  =ERR1            
                 DATA 61D
                 JMP  NOGOOD
               ENDIF
               JMP  krwak_1
             ENDIF
krwak_2      CLB  R2               
             STBD R2,=PILADR       
             STBD R2,=PILR4        
             DCB  R57              
             JPS  FIXDEV
           ENDIF
krwak_1    ICE                   
REP        JSB  =PILREP          
         ENDIF
NOGOOD   CLB  R57              
FIXDEV   DRP  !57
         STBD R57,=DEVCNT      
OUT      LDB  R2,R55           
         POMD R53,-R6          
         TSB  R2               
         RTN                   

ASPSND   LDM  R56,=ASP_1_
         JSB  =RDYSND          
         LDB  R55,=1           
         RTN                   
       TITLE 'krmo2'
*
*  __________________________________________________________________
* |KRMO2                                                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@    @@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@   @@@    @@@   @@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@@@  @@@@  @@@    @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@@@@@@@@@  @@      @@          @@   ||
* ||   @@ @@@      @@     @@   @@  @@  @@  @@      @@         @@@   ||
* ||   @@@@@       @@@@@@@     @@  @@  @@  @@      @@        @@@    ||
* ||   @@@@@       @@@@@@@     @@      @@  @@      @@      @@@      ||
* ||   @@ @@@      @@    @@@   @@      @@  @@      @@    @@@        ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@   @@@         ||
* ||   @@   @@@    @@      @@  @@      @@  @@@    @@@  @@@          ||
* ||   @@    @@@   @@      @@  @@      @@   @@@@@@@@   @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@      @@    @@@@@@    @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
         DATA  40,55            
REM10.   CLB  R2               
         JMP  MOD20

         DATA 40,55
MOD10.   CLB  R2               
         ICB  R2               
MOD20    JSB  =TWOR            
         JSB  =UT210           
         TSM  R52              
         JNZ  MOD35
MOD30    PUMD R40,+R12         
         RTN                   

MOD40    GTO NFR               
MOD50    LRM  R47              
         LRM  R57              
MOD60    SBM  R40,R50          
         JCY  MOD60
         ADM  R40,R50          
         LLM  R40              
         DCM  R30              
         JPS  MOD60
         LDM  R36,R34          
         TSB  R2               
         JZR  MOD70
         CMB  R33,R32          
         JRZ  MOD70
         STB  R33,R32          
         TSM  R40              
         JZR  MOD70
         LLM  R50              
         SBM  R50,R40          
         STM  R50,R40          
MOD70    JSB  =SHRONF          
         RTN                   

MOD35    TSM  R40              
         JZR  MOD30
         JSB  =SEP15           
         LDM  R30,R36          
         SBM  R30,R34          
         JPS  MOD50
         TSB  R2               
         JZR  MOD40
         CMB  R32,R33          
         JRZ  MOD40
         JSB  =ADD15           
         RTN                   
       TITLE 'krriz'
*
*  __________________________________________________________________
* |KRRIZ 545 07/19/82 - 7/29/1982 2:36PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@     @@@      @@             @@@   ||
* ||   @@  @@@     @@      @@  @@      @@      @@            @@@    ||
* ||   @@ @@@      @@     @@   @@     @@       @@           @@@     ||
* ||   @@@@@       @@@@@@@     @@@@@@@         @@          @@@      ||
* ||   @@@@@       @@@@@@@     @@@@@@@         @@         @@@       ||
* ||   @@ @@@      @@    @@@   @@    @@@       @@        @@@        ||
* ||   @@  @@@     @@     @@@  @@     @@@      @@       @@@         ||
* ||   @@   @@@    @@      @@  @@      @@      @@      @@@          ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@@@  @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
RNDIZ    JSB  =ON?R            
         JEN  CFP
RNTIME   LDMD R45,=RTC         
         TSB  R47              
         JZR  RNTIME
         STM  R46,R36          
         JSB  =CONBIN          
         BCD                   
CFP      JSB  =SEP10           
         TSM  R40              
         JZR  RSET20
RSET9    ICM  R36              
         JPS  RSET10
         LRM  R47              
         JNZ  RSET9
RSET10   STB  R36,R41          
         LDB  R40,=10C
RSET20   STMD R#,=X_K-1_      
         RTN                   
       TITLE 'krytx'
*
*  __________________________________________________________________
* |KRYTX 599 07/19/82 - 7/27/1982 5:57PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@      @@  @@@@@@@@@@  @@      @@   ||
* ||   @@   @@@    @@     @@@  @@      @@      @@      @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@@    @@@      @@       @@@  @@@    ||
* ||   @@ @@@      @@     @@    @@@  @@@       @@         @@@@      ||
* ||   @@@@@       @@@@@@@        @@@@         @@          @@       ||
* ||   @@@@@       @@@@@@@         @@          @@          @@       ||
* ||   @@ @@@      @@    @@@       @@          @@         @@@@      ||
* ||   @@  @@@     @@     @@@      @@          @@       @@@  @@@    ||
* ||   @@   @@@    @@      @@      @@          @@      @@@    @@@   ||
* ||   @@    @@@   @@      @@      @@          @@      @@      @@   ||
* ||   @@     @@@  @@      @@      @@          @@      @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
YTX5_    JSB  =TWOR            
         JSB  =UT210           
         STMD R50,=TEMP2       
         JSB  =SEP15           
         TSM  R42              
         JZR  YTX12
         TSB  R32              
         JRZ  YTX14
         TSB  R35              
         JLN  YTX16
         JMP  YTX18
YTX20    TSM  R34              
         JZR  YTX16
         DCM  R34              
YTX18    LLM  R52              
         JNZ  YTX20
         TSM  R34              
         JNZ  YTX14
         ELB  R57              
         JOD  YTX22
YTX14    CLB  R32              
YTX22    STB  R32,R22          
         JSB  =LN30            
         LDMD R50,=TEMP2       
         JSB  =SEP20           
         JSB  =MPY30           
         JSB  =EXP20           
         LDB  R32,R22          
         GTO CSEC11            

YTX12    TSM  R52              
         JNZ  YTX26
         JSB  =ERROR           
         DATA 6D
         LDB  R47,=10C
SGN6
NFR2     PUMD R40,+R12         
         RTN                   

YTX26    TSB  R33              
         JRZ  SGN6
         JSB  =ERROR           
         DATA 5D
         GTO INF10             

*
YTX16    JSBN  =ERROR+          
         DATA  9D               
*
*  __________________________________________________________________
* |KRRND 455 07/19/82 - 7/27/1982 5:57PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@      @@  @@@@@@       ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@      @@  @@@@@@@@     ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@@     @@  @@    @@@    ||
* ||   @@  @@@     @@      @@  @@      @@  @@@@    @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@     @@   @@ @@   @@  @@      @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@     @@  @@  @@  @@      @@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@     @@  @@  @@  @@      @@   ||
* ||   @@ @@@      @@    @@@   @@    @@@   @@   @@ @@  @@      @@   ||
* ||   @@  @@@     @@     @@@  @@     @@@  @@    @@@@  @@      @@   ||
* ||   @@   @@@    @@      @@  @@      @@  @@     @@@  @@    @@@    ||
* ||   @@    @@@   @@      @@  @@      @@  @@      @@  @@@@@@@@     ||
* ||   @@     @@@  @@      @@  @@      @@  @@      @@  @@@@@@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
         DATA  0,55             
RND10.   CLB  R47              
         CLM  R50              
         LDMD R70,=X_K-1_      
         LRM  R77              
         LDM  R60,=67C,84C,92C,30C,11C,85C,02C,00C
         LDM  R36,=15C,0C
         ARP  R70              
         LOOP
           LRM  R67              
           DRP  R50              
           JMP  RND31
           LOOP
             DCE                   
             ADM  R#,R#          
RND31      WHEN
           LRM  R57              
           ERM  R47              
           DCB  R36              
         WHNZ
         STMD R40,=X_K-1_      
         DCM  R36              
         JSB  =SHF10           
         LLB  R37              
         STM  R36,R40          
         PUMD R40,+R12         
         RTN                   
       TITLE 'kris'
*
*  __________________________________________________________________
* |MJIS 247 07/14/82 - 7/20/1982                                     |
* |==================================================================|
* ||                                                                ||
* ||         @@      @@    @@@@@@@@  @@@@@@@@@@    @@@@@@           ||
* ||         @@@    @@@    @@@@@@@@  @@@@@@@@@@   @@@@@@@@          ||
* ||         @@@@  @@@@        @@        @@      @@@    @@@         ||
* ||         @@@@@@@@@@        @@        @@      @@      @@         ||
* ||         @@  @@  @@        @@        @@      @@@                ||
* ||         @@  @@  @@        @@        @@       @@@@@@@           ||
* ||         @@      @@        @@        @@        @@@@@@@          ||
* ||         @@      @@        @@        @@             @@@         ||
* ||         @@      @@  @@    @@        @@      @@      @@         ||
* ||         @@      @@  @@@  @@@        @@      @@@     @@         ||
* ||         @@      @@   @@@@@@     @@@@@@@@@@   @@@@@@@@          ||
* ||         @@      @@    @@@@      @@@@@@@@@@    @@@@@@           ||
* ||                                                                ||
* ||                  Last edited on <820813.1411>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
DEVOK    BIN                   
         JSB  =STAR?           
         JZR  CLOSIT
         JSB  =GET#2+          
         REN
         PUMD R36,+R6          
         JSB  =CLOSIT
         POMD R36,-R6          
         REN
SETBIT   LDBD R33,X36,SETUP
         ORB  R33,R77          
         STBD R33,R2           
         JSB  =GET#2+          
         JEZ  SETBIT
         LDB  R2,R75           
         JMP  CHANG+

CLOSIT   JSB  =UNLREP          
         REN
         JSB  =THERE!          
kris_2   LDMD R33,X36,SETUP
         ANM  R33,R76          
         STMD R33,R2           
         JSB  =SKPCHK          
         JNZ  kris_2
         DRP !2
         CLB  R2               
CHANG+   LDBD R3,=PLSTAT       
         ANM  R3,R74           
         JSB  =SETIT           
         JSB  =CHANGE          
         RTN                   
*
*  __________________________________________________________________
* |IVERR 158 05/10/82 - 5/13/1982 3:28PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@@@@@  @@@@@@@@    @@@@@@@@     ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@@@@@  @@@@@@@@@   @@@@@@@@@    ||
* ||       @@      @@      @@  @@          @@     @@@  @@     @@@   ||
* ||       @@      @@      @@  @@          @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@          @@     @@   @@     @@    ||
* ||       @@       @@    @@   @@@@@@@@@   @@@@@@@     @@@@@@@      ||
* ||       @@       @@    @@   @@@@@@@@@   @@@@@@@     @@@@@@@      ||
* ||       @@        @@  @@    @@          @@    @@@   @@    @@@    ||
* ||       @@         @@@@     @@          @@     @@@  @@     @@@   ||
* ||       @@         @@@@     @@          @@      @@  @@      @@   ||
* ||   @@@@@@@@@@      @@      @@@@@@@@@@  @@      @@  @@      @@   ||
* ||   @@@@@@@@@@      @@      @@@@@@@@@@  @@      @@  @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1330>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
CALL     EQU  0
CALB     EQU  1
GOTO     EQU  2

ERMSG    DATA  1                
* nessage 1: num too small"
         DATA  CALB,109D,`small`

* message 2: num too large"
         DATA  CALB,109D,`large`

* message 3: "COT pr CSC inf"
         DATA 'COT',CALB,135D,'CS',GOTO,124D

* message 4: "TAN or SEC inf"
         DATA "TAN",CALB,135D,'SE',GOTO,124D

* message 5: "0^neg"
         DATA `0^neg`

* message 6: "0^0"
         DATA `0^0`

* message 7: "no value"
         DATA CALB,121D,`value`

* message 8: "/zero"
         DATA `/zero`

* message 9: "neg^non-integer"
         DATA `neg^non-integer`

* message 10: "SQR(neg number)"
         DATA "SQR",GOTO,99D

* message 11: "arg out of range"
         DATA `arg out of range`

* message 12: "LOG(0)
         DATA `LOG(0)`

* message 13: "LOG(neg number)
         DATA 'LOG', GOTO, 99D

* message 14: "Low batteries"
         DATA `Low batteries`

* message 15: "system error"
         DATA 'syst',GOTO,110D

* message 16: "not enough memory"
         DATA CALB, 136D,`enough memory`

* message 17: "RAM is invalid"
         DATA 'RAM is ', GOTO, 113D

* message 18: "ROM missing"
         DATA 'ROM ', GOTO, 116D

* message 19: "write protected"
         DATA CALL,125D, ' prot', GOTO, 126D

* message 20: "not this file"
         DATA CALB, 136D, 'this ', GOTO, 137D

* message 21: "verify failed"
         DATA `verify failed`

* message 22: "unknown card"
         DATA `unknown card`

* message 23: "bad read/write"
         DATA CALB, 139D, "read/", GOTO, 125D

* message 24: "pulled too fast"
         DATA CALB, 100D,`fast`

* message 25: "pulled too slow"
         DATA CALB, 100D,`slow`

* message 26: "wrong name"
         DATA CALB, 117D, GOTO, 120D

* message 27: "invalid subscript"
         DATA CALB, 112D, `subscript`

* message 28: "record overflow"
         DATA 'record',GOTO,106D

* message 29: "ON ERROR overflow"
         DATA 'ON ERROR', GOTO, 106D

* message 30: "OPTION BASE"
         DATA `OPTION BASE`

* message 31: "CONT before RUN"
         DATA `CONT before RUN`

* message 32: "missing line"
         DATA CALB, 105D, GOTO 138D

* message 33: "data type"
         DATA CALL,132D,'a',GOTO,127D

* message 34: "no data"
         DATA CALB,121D,CALL,132D,`a`

* message 35: "DIM exist var"
         DATA `DIM exist var`

* message 36: "invalid DIM"
         DATA CALB,112D,`DIM`

* message 37: "duplicate FN"
         DATA CALB,102D,`FN`

* message 38: "no END DEF"
         DATA CALB,121D,`END DEF`

* message 39: "FN missing"
         DATA "FN ",GOTO,116D

* message 40: "FN parameter"
         DATA "FN",GOTO,103D

* message 41: "FN calls itself"
         DATA `FN calls itself`

* message 42: "string too long"
         DATA CALL,118D,GOTO,101D

* message 43: "numeric input"
         DATA "numeric ",GOTO,128D

* message 44: "too many inputs"
         DATA CALB,107D,CALL,128D,`s`

* message 45: "missing ASSIGN#"
         DATA CALB,105D,CALL,119D,`#`

* message 46: "missing NEXT"
         DATA CALB,105D,`NEXT`

* message 47: "no matching FOR"
         DATA CALB,121D,CALL,129D,`ing FOR`

* message 48: "FOR overflow"
         DATA "FOR",GOTO,106D

* message 49: "GOSUB overflow"
         DATA CALL,130D,GOTO,106D

* message 50: "RETURN w/o GOSUB"
         DATA "RETURN w/o ",GOTO,130D

* message 51: "PRINT# to runfile"
         DATA "PRINT# to run",GOTO,137D

* message 52: "invalid IMAGE"
         DATA CALB,112D,`IMAGE`

* message 53: "invalud USING"
         DATA CALB,112D,`USING`

* message 54: "invalid TAB"
         DATA CALB 112D,`TAB`

* message 55: "ASSIGN IO needed"
         DATA CALL,119D,GOTO,104D

* message 56: "no loop response"
         DATA CALB,121D,CALB,131D,`response`

* message 57: "bad transmission"
         DATA CALB,139D,'trans',CALL,133D,`on`

* message 58: "loop timeout"
         DATA CALB,131D,`timeout`

* message 59: "too many names"
         DATA CALB,107D,CALL,120D,`s`

* message 60: "RESTORE IO needed"
         DATA "RESTORE",GOTO,104D

* message 61: ">31 devices"
         DATA `>31 devices`

* message 62: "file not found"
         DATA CALL,137D,` not found`

* message 63: "invalid filespec"
         DATA CALB,112D,CALL,137D,`spec`

* message 64: "duplicate name"
         DATA CALB,102D,GOTO,120D

* message 65: "access restricted"
         DATA `access restricted`

* message 66: "invalid password"
         DATA CALB,112D,`password`

* message 67: "line too long"
         DATA CALL,138D,GOTO,101D

* message 68: "wrong file type"
         DATA CALB,117D,CALL,137D,GOTO,127D

* message 69: "workfile name?"
         DATA 'work',CALL,137D,' ',CALL,120D,`?`

* message 70: "time adjust bad"
         DATA `time adjust bad`

* message 71: "duplicate APPT"
         DATA CALB,102D,`APPT`

* message 72: "day/date mismatch"
         DATA 'day/',CALL,132D,'e mis',GOTO,129D

* message 73: "bad day field"
         DATA CALB,139D,'day',GOTO,122D

* message 74: "bad date field"
         DATA CALB,139D,CALL,132D,'e',GOTO,122D

* message 75: "bad time field"
         DATA CALB,139D,'time',GOTO,122D

* message 76: "bad rep field"
         DATA CALB,139D,'rep',GOTO,122D

* message 77: "bad alarm spec"
         DATA CALB,139D,`alarm spec`

* message 78: "syntax"
         DATA `syntax`

* message 79: "; expected"
         DATA ';',GOTO,108D

* message 80: ") expected"
         DATA ")",GOTO,108D

* message 81: "comma expected"
         DATA "comma",GOTO,108D

* message 82: "string expected"
         DATA CALL,118D,GOTO,108D

* message 83: "missing TO"
         DATA CALB,105D,`TO`

* message 84: "extra characters"
         DATA `extra characters`

* message 85: "expr too big"
         DATA "expr",CALL,111D,` big`

* message 86: "illegal context"
         DATA `illegal context`

* message 87: "bad expression"
         DATA CALB,139D,`expression`

* message 88: "bad statement"
         DATA CALB,139D,`statement`

* message 89: "bad parameter"
         DATA 'bad',GOTO,103D

* message 90: "bad line number"
         DATA CALB,139D,CALL,138D,GOTO,115D

* message 91: "missing parameter"
         DATA CALL,116D,GOTO,103D

* message 92: "dev not mass mem"
         DATA 'dev ',CALB,136D,CALL,114D,`em`

* message 93: "mass mem error"
         DATA CALL,114D,GOTO,110D

* message 94: "no medium"
         DATA CALB,121D,GOTO,123D

* message 95: "medium full"
         DATA CALL,123D,` full`

* message 96: "invalid medium"
         DATA CALB,112D,GOTO,123D

* message 97: "invalid pack"
         DATA CALB,112D,`pack`
 
         DATA 0FFH

* macro 99
         DATA "(neg",CALL,115D,`)`

* macro 100
         DATA "pulled",GOTO,111D

* magro 101
         DATA CALL,111D,` long`

* macro 102
         DATA `duplicate`

* marco 103
         DATA ` parameter`

* macro 104
         DATA ` IO needed`

* macro 105
         DATA GOTO,116D

* macro 106
         DATA ` overflow`

* macro 107
         DATA `too many`

* macro 108
         DATA ' exp',GOTO,126D

* macro 109
         DATA 'num',GOTO,111D

* macro 110
         DATA `em error`

* macro 111
         DATA ` too`

* macro 112
         DATA GOTO,113D

* macro 113
         DATA `invalid`

* macro 114
         DATA `mass m`

* macro 115
         DATA ` number`

* macro 116
         DATA CALL,133D,`ng`

* macro 117
         DATA `wrong`

* macro 118
         DATA `string`

* macro 119
         DATA `ASSIGN`

* macro 120
         DATA `name`

* macro 121
         DATA `no`

* macro 122
         DATA ` field`

* macro 123
         DATA `medium`

* macro 124
         DATA `C inf`

* macro 125
         DATA `write`

* macro 126
         DATA `ected`

* macro 127
         DATA ` type`

* macro 128
         DATA `input`

* macro 129
         DATA `match`

* macro 130
         DATA `GOSUB`

* macro 131
         DATA `loop`

* macro 132
         DATA `dat`

* macro 133
         DATA `missi`

* message 134: "?"
         DATA `?`

* macro 135:
         DATA ` or`

* macro 136:
         DATA `not`

* macro 137:
         DATA `file`

* macro 138:
         DATA `line`

* macro 139:
         DATA `bad`
       TITLE 'krt_d'
*
*  __________________________________________________________________
* |KXT&D 481 07/19/82 - 8/ 6/1982 4:42PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@   @@@@@      @@@@@@       ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@@@@@@     @@@@@@@@     ||
* ||   @@   @@@    @@@    @@@      @@      @@    @@    @@    @@@    ||
* ||   @@  @@@      @@@  @@@       @@       @@  @@     @@      @@   ||
* ||   @@ @@@         @@@@         @@        @@@@      @@      @@   ||
* ||   @@@@@           @@          @@         @@       @@      @@   ||
* ||   @@@@@           @@          @@        @@@@      @@      @@   ||
* ||   @@ @@@         @@@@         @@       @@  @@ @@  @@      @@   ||
* ||   @@  @@@      @@@  @@@       @@      @@    @@@@  @@      @@   ||
* ||   @@   @@@    @@@    @@@      @@      @@  @@@@@   @@    @@@    ||
* ||   @@    @@@   @@      @@      @@      @@@@@@  @@  @@@@@@@@     ||
* ||   @@     @@@  @@      @@      @@       @@@    @@  @@@@@@       ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
MARCH    EQU  3D
STRLEN   EQU  8D

         DATA  0,56             
TIME$.   LDB  R30,=':'
         JMP  TMEDTE           
*
         DATA  0,56             
DATE$.   LDB  R30,='/'
TMEDTE   LDM  R56,=(STRLEN).2
         JSB  =RESPUT          
         REN
         STM  R26,R36          
         BIN                   
         JSB  =TDGET
         CMB  R30,=':'
         IFNE
           STM  R43,R40          
         ENDIF
         LDB  R20,R42          
         JSB  =TOASC2          
         STM  R20,R60          
         LDB  R20,R41          
         JSB  =TOASC2          
         STM  R20,R63          
         LDB  R20,R40          
         JSB  =TOASC2          
         STM  R20,R66          
         STB  R30,R62          
         STB  R30,R65          
         STMD R60,R36          
         RTN                   

         DATA 0,55
DATE.    BIN                   
         JSB  =TDGET
         CLM  R22              
         LDB  R22,R44          
         CLM  R50              
         LDB  R50,R43          
         BCD                   
         LOOP
           DCM  R22              
           JZR  LPYR?
           CLM  R60              
           LDBD R20,X22,DTAB0    
           STB  R20,R60          
           ADM  R50,R60          
         WHMP

LPYR?    CMB  R44,=MARCH          
         IFCY
           STM  R45,R65          
           JSB  =SYSJSB          
           DEF  LEAPYR
           IFEZ
             DCM  R50              
           ENDIF
         ENDIF
         CLM  R60              
         LDB  R60,R45          
         LLM  R60              
         LLM  R60              
         LLM  R60              
         ADM  R50,R60          
         CLM  R44              
         LDM  R45,R50          

PSHINT   BIN                   
         NCB  R44              
         PUMD R40,+R12         
         RTN                   

         DATA 0,55
TIME.    BIN                   
         JSB  =TDGET
         BCD                   
         CLM  R43              
         LDB  R45,R42          
         JSB  =MULT60
         CLB  R42              
         ADM  R45,R41          
         JSB  =MULT60
         CLB  R41              
         ADM  R45,R40          
         JSB  =PSHINT
         LDM  R36,R61
         ANM  R36,=3FFFH

         JSB  =CONBIN          
         STM  R40,R50          
         LDMD R40,=TMEFAC      
         JSB  =DIV10           
         JSB  =ADDROI          

         DRP  !40
         ARP  !12
         POMD R40,-R12         
         ADB  R40,=3           
         CLB  R41
         PUMD R40,+R12         
         JSB  =IP5             
         JSB  =ONER            
         SBB  R40,=3           
        
         IFNC
           LDB  R41,=90C
         ENDIF
         JSB  =ABS5-
         RTN                   
GAP001   NOP

MULT60   DRP  !45
         LLM  R45              
         ADM  R45,R45          
         STM  R45,R55          
         ADM  R45,R55          
         ADM  R45,R55          
         RTN                   

TDGET    JSB  =SYSJSB          
          DEF GETTD
         RTN                   
       TITLE 'krbe_'
*
*  __________________________________________________________________
* |KRBE' 55 06/24/82 - 7/12/1982 4:54PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@@@      @@       ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@@      @@       ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@              @@       ||
* ||   @@  @@@     @@      @@  @@      @@  @@              @@       ||
* ||   @@ @@@      @@     @@   @@     @@@  @@                       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@@@                ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@@@                ||
* ||   @@ @@@      @@    @@@   @@     @@@  @@                       ||
* ||   @@  @@@     @@     @@@  @@      @@  @@                       ||
* ||   @@   @@@    @@      @@  @@     @@@  @@                       ||
* ||   @@    @@@   @@      @@  @@@@@@@@@   @@@@@@@@@@               ||
* ||   @@     @@@  @@      @@  @@@@@@@@    @@@@@@@@@@               ||
* ||                                                                ||
* ||   Finished on: 12/16/81  Raan  Last edited on <820908.1345>    ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
STBEP_   SAD                   
         BIN                   
         PUMD R20,+R6          
         LDM  R20,=(BEEPFQ).2
         PUMD R42,+R6          
         CLM  R42              
         LDB  R44,=(BEEPLN).2
         JSB  =BEEPR_
         POMD R42,-R6          
         POMD R20,-R6          
         PAD                   
         RTN                   

BEEP._   JSB  =ONR12?          
         JEZ  STBEP_           
         ARP  !12
         DRP  !02
         DCB  R02               
         IFZR
           POBD R2,-R12           
           STBD R2,=BEEPOK       
           RTN                   
         ENDIF
         SBM  R2,=(7D).2
         IFZR
           CLM  R53              
           LDB  R54,=(BEEPLN).2
           JMP  GOBEEP
         ENDIF

         JSB  =ONE7PR          
GOBEEP   PUMD R53,+R6          
         JSB  =ONEI            
         TSB  R47              
         DRP  R45              
         IFLN
           CLM  R45              
         ENDIF
         TSM  R45              
         IFZR
           ICM  R45              
         ENDIF
         LDM  R64,=0FFH,00C,83C,02C
         PUMD R60,+R12         
         PUMD R40,+R12         
         JSB  =INTDIV          
         JSB  =ONEB            
         SBM  R46,=(16D).2
         IFNG
           CLM  R46              
         ENDIF
         STM  R#,R20          
         POMD R43,-R6          
         CLB  R42              
         TSB  R17              
         RNG

BEEPR_   LDBD R2,=BEEPOK       
         RZR
         JSB  =SETWDB
         LDB  R0,=(1).2            
         LOOP
           JSB  =STOP?           
           JEN  BEEPDN
           LDBD R2,=CMPSB        
           XRB  R2,R0            
           STBD R2,=CMPSB        
           LDM  R2,R20           
           LOOP
             DCM  R#               
           WHCY
           LDMD R43,=WDBRIC      
           CMMD R42,=RTC         
         WHCY

BEEPDN   LDB  R3,=0FEH
         ANMD R3,=CMPSB        
         STMD R3,=CMPSB        
         RTN                   
       TITLE 'krti_'
MAXEXP EQU 16C
NEGEXP EQU 500C
NAMEXP EQU 11C
*
*  __________________________________________________________________
* |KRTI' 491 06/24/82 - 7/12/1982 4:59PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@@@  @@@@@@@@@@      @@       ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@@      @@       ||
* ||   @@   @@@    @@     @@@      @@          @@          @@       ||
* ||   @@  @@@     @@      @@      @@          @@          @@       ||
* ||   @@ @@@      @@     @@       @@          @@                   ||
* ||   @@@@@       @@@@@@@         @@          @@                   ||
* ||   @@@@@       @@@@@@@         @@          @@                   ||
* ||   @@ @@@      @@    @@@       @@          @@                   ||
* ||   @@  @@@     @@     @@@      @@          @@                   ||
* ||   @@   @@@    @@      @@      @@          @@                   ||
* ||   @@    @@@   @@      @@      @@      @@@@@@@@@@               ||
* ||   @@     @@@  @@      @@      @@      @@@@@@@@@@               ||
* ||                                                                ||
* ||                  Last edited on <820908.1342>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
ONE7+B   LDMD R40,=TMEFAC      
         PUMD R40,+R12         
         JSB  =MPYROI          
         POMD R40,-R12         
         LDM  R20,R40          
         CLM  R50              
         STM  R42,R50          
         BCD                   
         LRB  R21              
         IFEZ
           CMM  R20,=(NEGEXP).2
           IFNC
             CMM  R20,=(MAXEXP).2
             IFNC
               CLB  R40
               SBM  R20,=(NAMEXP).2
               IFNG
                 ICB  R40              
                 TCM  R20              
               ENDIF

               LOOP
                 DCM  R20              
                 JNG  BCDBIN
                 TSB  R40              
                 IFNZ
                   LRM  R57              
                 ELSE
                   LLM  R50              
                 ENDIF
               WHMP

BCDBIN         LLM  R50              
               LLM  R50              
               CLM  R41              
               LDB  R2,=13D           
               BIN                   

               LOOP
                 LLM  R41              
                 STM  R41,R61          
                 LLM  R41              
                 LLM  R41              
                 ADM  R41,R61          
                 BCD                   
                 LLM  R51              
                 CLM  R61              
                 ELM  R61              
                 BIN                   
                 ADM  R41,R61          
                 DCB  R2               
               WHPS
               RTN                   
             ENDIF
             CLM  R41              
             NCM  R41              
             BIN                   
             RTN                   

           ENDIF
         ENDIF
         CLM  R41              
         BIN                   
         RTN                   

SETWDB   CLB  R42              
         ADMD R42,=RTC         
         IFCY
           CLM  R43              
           DCM  R43              
         ENDIF
         STMD R43,=WDBRIC      
         RTN                   

WAITCK   JSB  =SETWDB
         LOOP
           JSB  =STOP?           
           REN
           TSB  R40              
           IFNZ
             JSB  =KEY?            
             REN
           ENDIF
           LDMD R43,=WDBRIC      
           CMMD R42,=RTC         
         WHCY
         RTN                   
       TITLE 'krcts'
*
*  __________________________________________________________________
* |RHCT$ 104 04/02/82 - 4/20/1982 10:13PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@    @@      @@     @@@@     @@@@@@@@@@      @@       ||
* ||   @@@@@@@@@   @@      @@   @@@@@@@@   @@@@@@@@@@   @@@@@@@     ||
* ||   @@     @@@  @@      @@  @@@    @@@      @@      @@@@@@@@@@   ||
* ||   @@      @@  @@      @@  @@      @@      @@      @@  @@  @@   ||
* ||   @@     @@   @@      @@  @@              @@      @@  @@       ||
* ||   @@@@@@@     @@@@@@@@@@  @@              @@       @@@@@@@     ||
* ||   @@@@@@@     @@@@@@@@@@  @@              @@        @@@@@@@    ||
* ||   @@    @@@   @@      @@  @@              @@          @@  @@   ||
* ||   @@     @@@  @@      @@  @@      @@      @@      @@  @@  @@   ||
* ||   @@      @@  @@      @@  @@@    @@@      @@      @@@@@@@@@    ||
* ||   @@      @@  @@      @@   @@@@@@@@       @@        @@@@@@     ||
* ||   @@      @@  @@      @@     @@@@         @@          @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1349>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************

CAT$     JSB  =ONEB            
         LDM  R56,=(CATLEN).2
         JSB  =RESPUT          
         REN
         BIN                   
         LDM  R32,R46          
         IFNG
           LDMD R40,=RNNAME      
           CMB  R16,=RUNSTS
           JEQ  ALMOST
           LDMD R66,=FWVARS      
           LDMD R0,X66,E.PREV
           SBM  R66,R0           
           LDMD R40,X66,E.MOM
           LDBD R0,X66,E.STAT
           CMB  R0,=RUNSTS
           JNZ  NULL
ALMOST
           JSB  =GOPEN           
           LDM  R34,R30          
           LDM  R32,=(DRENSZ).2
           LDM  R30,=TMRBUF      
           JSB  =ROMCPY          
           JMP  DONE
         ENDIF
         IFZR
           LDMD R40,=EDNAME      
           JMP  ALMOST
         ENDIF
         LDM  R30,=((DIRECT)-(DRENSZ)).2
         CLM  R34              
         LOOP
           JSB  =DNENT           
           JEN  NULL
           ICM  R34              
           CMM  R34,R32          
         WHNC
         JMP  DONE

NULL     CLM  R54              
         PUMD R54,-R12         
         POMD R54,+R12         

DONE     JSB  =CATBUF          
         RTN                   

CATALL
         BIN                   
         LDM  R30,=((DIRECT)-(DRENSZ)).2
         JSB  =DNENT           
         LDM  R26,=CATHED
         JSB  =MSSOUT          

CATGUT
         JSB  =CATLIN          
CWAIT
         JSB  =SIGNIF          
         DRP  !2
         JSB  =LOOKUP          
         DEF  CATTAB
         REN
         JSB  =DEQUE           
         STM  R2,R4            

CATTAB   VAL  UPKEY
         DEF  CAT.UP
         VAL  DOWNKY
         DEF  CAT.DN
         VAL  (SHIFT)+(UPKEY)
         DEF  CATSUP
         VAL  (SHIFT)+(DOWNKY)
         DEF  CATSDN
         VAL  EDITKY
         DEF  CATEDT
         DATA 0

CAT.DN   DRP !2
         JSB  =DNENT           
         JEN  CWAIT
         JMP  CATGUT

CATSDN   LOOP
           JSB  =DNENT           
         WHEZ
         JMP  CATGUT

CAT.UP   JSB  =UPENT           
         JEN  CWAIT
         JMP  CATGUT

CATSUP   LOOP
           JSB  =UPENT           
         WHEZ
TOCATG   JMP  CATGUT

CATEDT
         CLM  R50              
         DCM  R50              
         LDMD R20,X30,DR.TYP
         LDMD R40,X30,DR.NAM
         CMB  R40,='a'
         IFCY
           STM  R20,R50          
         ENDIF
         JSB  =EDITIT          
         REZ
         CLM  R36              
         LDBD R36,=ERRORS      
         JSB  =CLRERR          
         JSB  =WARN.R          
         JMP  TOCATG
       TITLE 'krbuf'
*
*  __________________________________________________________________
* |RHBUF 61 04/02/82 - 4/20/1982 10:13PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@    @@      @@  @@@@@@@@    @@      @@  @@@@@@@@@@   ||
* ||   @@@@@@@@@   @@      @@  @@@@@@@@@   @@      @@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@     @@@  @@      @@  @@           ||
* ||   @@      @@  @@      @@  @@      @@  @@      @@  @@           ||
* ||   @@     @@   @@      @@  @@     @@@  @@      @@  @@           ||
* ||   @@@@@@@     @@@@@@@@@@  @@@@@@@@    @@      @@  @@@@@@@@@    ||
* ||   @@@@@@@     @@@@@@@@@@  @@@@@@@@    @@      @@  @@@@@@@@@    ||
* ||   @@    @@@   @@      @@  @@     @@@  @@      @@  @@           ||
* ||   @@     @@@  @@      @@  @@      @@  @@      @@  @@           ||
* ||   @@      @@  @@      @@  @@     @@@  @@@    @@@  @@           ||
* ||   @@      @@  @@      @@  @@@@@@@@@    @@@@@@@@   @@           ||
* ||   @@      @@  @@      @@  @@@@@@@@      @@@@@@    @@           ||
* ||                                                                ||
* ||                  Last edited on <820908.1331>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
CATTMP   LDM  R26,=TMPMM2      
CATBUF   LDB  R23,=BLANK
         LDMD R40,R30          
         LDMD R50,X30,(DR.NAM).2
         PUMD R50,+R26         
         PUBD R23,+R26         
         PUBD R23,+R26         
         LDM  R36,R44          
         LDB  R36,R23          
         LDB  R3,R44           
         ANM  R3,=TYPRI?
         DRP  R36              
         IFEQ
           LDB  R36,='P'
         ENDIF
         PUMD R36,+R26         
         PUMD R30,+R6          
         LDM  R36,R42          
         LDM  R3,R44           
         ANM  R3,=TYLIN?
         IFNZ
           CMM  R36,=((PCBLEN)+(ENDSIZ)).2
           IFEQ
             CLM  R36              
           ENDIF
         ENDIF
         JSB  =PUTBIN          
         STM  R30,R26          
         PUMD R23,+R26         
         POMD R30,-R6          
         LDMD R44,X30,DR.DAT
         JSB  =SYSJSB          
         DEF  DTECNV
         PUMD R72,+R26         
         PUMD R40,+R26         
         LDM  R36,=(CATLEN).2
         SBM  R26,R36          
         RTN                   

*
         DATA  36               
         DATA  "  Name   Type Len  Time   Date" 
FLVFO+   LDMD  R74,X24,FLPWD0
         CMM   R74,R54
         RTN
       TITLE 'melfl'
       BSS  7FFFH-($)+1
       END
