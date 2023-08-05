       ABS 
       ORG 06000H
       TITLE 'kralt'
*  __________________________________________________________________
* |RYALT 46 04/02/82 - 4/20/1982 8:42PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@    @@      @@    @@@@@@    @@          @@@@@@@@@@   ||
* ||   @@@@@@@@@   @@      @@   @@@@@@@@   @@          @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@@    @@@  @@              @@       ||
* ||   @@      @@  @@@    @@@  @@      @@  @@              @@       ||
* ||   @@     @@    @@@  @@@   @@      @@  @@              @@       ||
* ||   @@@@@@@        @@@@     @@@@@@@@@@  @@              @@       ||
* ||   @@@@@@@         @@      @@@@@@@@@@  @@              @@       ||
* ||   @@    @@@       @@      @@      @@  @@              @@       ||
* ||   @@     @@@      @@      @@      @@  @@              @@       ||
* ||   @@      @@      @@      @@      @@  @@              @@       ||
* ||   @@      @@      @@      @@      @@  @@@@@@@@@@      @@       ||
* ||   @@      @@      @@      @@      @@  @@@@@@@@@@      @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1345>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
MYROM#   EQU  1
         DEF  RMHEAD           ; ROM marker: 1CE3
         DEF  RMSTRT           ; RMDR.LOC - location of file
         DATA 8K               ; RMDR.SIZ - size of file
         VAL  TYTOK?           ; RMDR.TYP - type of file
         VAL  TYNSYS           ; RMDR.TNM - name of type
         DATA 0H,0EAH,0A8H,099H ; RMDR.DAT - Date of creation
         DATA "altrom1 "       ; RMDR.NAM - name of file
         DEF  ZRO              ; RMDR.ESZ - size of file (0 for ROMs)

RMSTRT   DEF  MYROM#           ; RM.ID - ROM id#
         DEF  RUNALT           ; RM.RUN - pointer to RUNTIM table
         DEF  ASCALT           ; RM.ASC - pointer to ASCII TOKEN table
         DEF  PARALT           ; RM.PAR - pointer to PARSE table
         DEF  ERRALT           ; RM.ERR - pointer to ERRMSG table
         DEF  INIALT           ; RM.INI - pointer to INIT routine
INIALT   RTN                   ;

RUNALT   DEF  ERRORX           ;
         DEF  ALARM.           ;
         DEF  LOCK.            ;
         DEF  DEG.             ;
         DEF  RAD.             ;

PARALT   DEF  ERRORX           ;
         DEF  ON/OFF           ;
         DEF  GET1$            ;
         DEF  PUSH1A           ;
         DEF  PUSH1A           ;

ASCALT   DATA  `ALARM`          ;
         DATA  `LOCK`           ;
         DATA  `OPTION ANGLE DEGREES` ;
         DATA  `OPTION ANGLE RADIANS` ;

ERRALT   DATA 0FFH
       TITLE 'krasc'
*
*  __________________________________________________________________
* |KRASC 51 04/02/82 - 4/20/1982 8:43PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@      @@@@@@      @@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@    @@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@@    @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@      @@  @@@         @@           ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@@   @@@@@@@    @@           ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@@    @@@@@@@   @@           ||
* ||   @@ @@@      @@    @@@   @@      @@         @@@  @@           ||
* ||   @@  @@@     @@     @@@  @@      @@  @@      @@  @@      @@   ||
* ||   @@   @@@    @@      @@  @@      @@  @@@     @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@  @@      @@   @@@@@@@@    @@@@@@@@    ||
* ||   @@     @@@  @@      @@  @@      @@    @@@@@@       @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820908.1348>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
DUMMY    EQU  200

ASCIIS   DATA DUMMY            
         DATA  `&`              
         DATA  `;`              
         DATA  `(`              
         DATA  `)`              
         DATA  `*`              
         DATA  `+`              
         DATA  `,`              
         DATA  `-`              
         DATA  `.`              
         DATA  `/`              
         DATA  `^`              
         DATA  `#`              
         DATA  `<=`             
         DATA  `>=`             
         DATA  `<>`             
         DATA  `=`              
         DATA  `>`              
         DATA  `<`              
         DATA  `-`              
         DATA  `#`              
         DATA  `<=`             
         DATA  `>=`             
         DATA  `<>`             
         DATA  `=`              
         DATA  `>`              
         DATA  `<`              
         DATA  `@`              
         DATA  `ON ERROR`       
         DATA  `OFF ERROR`      
         DATA  `DEF KEY`        
         DATA  `FN`             
         DATA  `AUTO`           
         DATA  `CAT ALL`        
         DATA  `LIST IO`        
         DATA  `CAT$`           
         DATA  `DISPLAY IS`     
         DATA  `CAT`            
         DATA  `LIST`           
         DATA  `NAME`           
         DATA  `DELAY`          
         DATA  `MERGE`          
         DATA  `CALL`           
         DATA  `READ #`         
         DATA  `FETCH KEY`      
         DATA  `WIDTH`          
         DATA  `POP`            
         DATA  `RUN`            
         DATA  `REAL`           
         DATA  `DISP`           
         DATA  `FETCH`          
         DATA  `PWIDTH`         
         DATA  `DEFAULT`        
         DATA  `GOTO`           
         DATA  `GOSUB`          
         DATA  `PRINT #`        
         DATA  `MARGIN`         
         DATA  `RESTORE #`      
         DATA  `INPUT`          
         DATA  `ASSIGN #`       
         DATA  `LET FN`         
         DATA  `LET`            
         DATA  `STANDBY`        
         DATA  `ON TIMER #`     
         DATA  `OFF TIMER #`    
         DATA  `ON`             
         DATA  `BYE`            
         DATA  `WAIT`           
         DATA  `PROTECT`        
         DATA  `PRINTER IS`     
         DATA  `PRINT`          
         DATA  `PLIST`          
         DATA  `RANDOMIZE`      
         DATA  `READ`           
         DATA  `RESTORE IO`     
         DATA  `RESTORE`        
         DATA  `RETURN`         
         DATA  `UNPROTECT`      
         DATA  `EDIT`           
         DATA  `OFF IO`         
         DATA  `STOP`           
         DATA  `PUT`            
         DATA  `TRACE FLOW`     
         DATA  `TRACE OFF`      
         DATA  `TRACE VARS`     
         DATA  `ENDLINE`        
         DATA  `CLEAR VARS`     
         DATA  `COPY`           
         DATA  `PURGE`          
         DATA  `RENAME`         
         DATA  `INTEGER`        
         DATA  `SHORT`          
         DATA  `DELETE`         
         DATA  `ROM missing`    
         DATA  `REM`            
         DATA  `OPTION BASE`    
         DATA  `END DEF`        
         DATA  `DATA`           
         DATA  `DEF FN`         
         DATA  `DIM`            
         DATA  `RENUMBER`       
         DATA  `END`            
         DATA  `!`              
         DATA  `FOR`            
         DATA  `IF`             
         DATA  `IMAGE`          
         DATA  `NEXT`           
         DATA  `BEEP`           
         DATA  DUMMY              
         DATA  `ASSIGN IO`      
         DATA  `CLEAR LOOP`     
         DATA  `CONT`           
         DATA  `CLEAR`          
         DATA  ^'^             
         DATA  `TEXT`           
         DATA  `BASIC`          
         DATA  `LIF1`           
         DATA  `RES`            
         DATA  ` INTO `         
         DATA  DUMMY              
         DATA  DUMMY            
         DATA  ` OR `           
         DATA  `TO`             
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  `ON`             
         DATA  `OFF`            
         DATA  `IP`             
         DATA  `EPS`            
         DATA  `FP`             
         DATA  `CEIL`           
         DATA  `MAX`            
         DATA  DUMMY              
         DATA  `SQR`            
         DATA  `MIN`            
         DATA  `MEM`            
         DATA  `ABS`            
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  `SGN`            
         DATA  `KEY$`           
         DATA  `COT`            
         DATA  `CSC`            
         DATA  `APPT`           
         DATA  `EXP`            
         DATA  `INT`            
         DATA  `LOG10`          
         DATA  `LOG`            
         DATA  `VER$`           
         DATA  `SEC`            
         DATA  `CHR$`           
         DATA  `STR$`           
         DATA  `LEN`            
         DATA  `NUM`            
         DATA  `VAL`            
         DATA  `INF`            
         DATA  DUMMY              
         DATA  `PI`             
         DATA  `UPRC$`          
         DATA  `USING`          
         DATA  `THEN`           
         DATA  `TAB`            
         DATA  `STEP`           
         DATA  ` EXOR `         
         DATA  `NOT `           
         DATA  ` DIV `          
         DATA  `ERRN`           
         DATA  `ERRL`           
         DATA  `CARD`           
         DATA  ` AND `          
         DATA  `KEYS`           
         DATA  `ELSE`           
         DATA  `SIN`            
         DATA  `COS`            
         DATA  `TAN`            
         DATA  ` TO `           
         DATA  DUMMY              
         DATA  DUMMY              
         DATA  `[`              
         DATA  `]`              
         DATA  `\`              
         DATA  `POS`            
         DATA  `DEG`            
         DATA  `RAD`            
         DATA  `FLOOR`          
         DATA  0FFH
       TITLE 'krps2'
*
*  __________________________________________________________________
* |KRPS2 390 07/19/82 - 8/12/1982 4:18PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@      @@@@@@       @@@@      ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@@    @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@          @@   ||
* ||   @@ @@@      @@     @@   @@     @@@  @@@                @@@   ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@    @@@@@@@          @@@    ||
* ||   @@@@@       @@@@@@@     @@@@@@@@      @@@@@@@       @@@      ||
* ||   @@ @@@      @@    @@@   @@                 @@@    @@@        ||
* ||   @@  @@@     @@     @@@  @@          @@      @@   @@@         ||
* ||   @@   @@@    @@      @@  @@          @@@     @@  @@@          ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@   @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@            @@@@@@    @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1331>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
APINFO   LDM  R20,=(INFOTM).2
         JSB  =GETLNX
         LDM  R36,=7,0
         LDMD R42,R32          
         JSB  =DCCLOK
         LDB  R20,R45          
         JSB  =TOASC2          
         STMD R20,=INP+5       
         LDB  R20,R46          
         JSB  =TOASC2          
         STMD R20,=INP+3       
         LDMD R20,X32,SIX
         TSB  R20              
         JPS  krps2_8
         LDB  R36,=32D
         LDB  R20,R21          
         JZR  krps2_4
         BCD                   
         LRB  R20              
         BIN                   
         JSB  =FXDAY
         ANM  R21,=0FH
         JZR  krps2_3
         ADB  R21,='0'
         CMB  R21,='8'
         DRP  !21
         JNC  krps2_2
         JNZ  krps2_1
         DCB  R21              
krps2_1  DRP  !21
         SBB  R21,=12D          
krps2_2  DRP  !21
         STB  R21,R47          
krps2_3  STMD R45,=INP+29      
krps2_4  LDBD R20,X32,EIGHT
         JZR  krps2_5
         JSB  =TOASC2          
         STMD R20,=INP+15      
krps2_5  LDMD R45,X32,NINE
         LDM  R26,=DAYSEC      
         JSB  =TIMDIV
         JZR  krps2_6
         DRP  !20
         STMD R20,=INP+18       
krps2_6  LDM  R26,=(HRSEC).2
         JSB  =TIMDIV
         JZR  krps2_7
         DRP  !20
         STMD R#,=INP+21       
krps2_7  LDM  R26,=(MNSEC).2
         JSB  =TIMDIV
         JZR  krps2_8
         DRP  !20
         STMD R#,=INP+24       
krps2_8  LDM  R26,=INPBUF      
         JSB  =OUTSTR          
         JSB  =LETBD           
         RTN                   

APTDEL   LDB  R27,=BIT#5
         STBD R27,X32,SIX
         LDM  R20,R32          
         JSB  =APTACK
         STM  R20,R32          
APDEL_   PUMD R30,+R6          
         LDM  R30,R32          
         CLM  R32              
         LDBD R32,R30          
         LLB  R32              
         LRB  R32              
         SBM  R34,R32          
         JSB  =DELETE          
         STM  R30,R32          
         POMD R30,-R6          
         JSB  =STALRM
         RTN                   

APTDSP   JSB  =HANDI0          
         VAL V.AFMT
         JSB  =APTGET
         JSB  =FXAPPT
         LDM  R20,=INPBUF      
         STM  R20,R22          
         RTN                   

APTERR
         JSB  =ERRORR          
         LDM  R73,=32D,TMPLAT,INPBUF
         JSB  =KOPY            
         LDB  R24,=41H
         STBD R24,=PSIOST      
         LDBD R24,=APTSIZ      
         LDM  R20,=INPBUF      
         STM  R20,R22          
         ICE                   
         RTN                   

APTFND   LDMD R43,=INP+1       
APFND_   CLE                   
         CLM  R32              
         STM  R32,R25          
         LDM  R32,R30          

krps2_11 ADM  R32,R25          
         CMM  R32,R34          
         RZR
         LDMD R52,R32          
         LDBD R25,R32          
         ANM  R25,=NOT#7
         CMM  R53,R43          
         JNC  krps2_11
         RNZ
         ICE                   
         RTN                   

APTGET   LDMD R70,=BLANKS      
         STMD R70,=INP+26      
         LDM  R76,=INPBUF      
         STM  R32,R74          
         LDBD R73,R74          
         LLB  R73              
         LRB  R73              
         JSB  =KOPY            
         RTN                   

APTINS   LDM  R42,R30          
         STM  R32,R30          
         LDBD R32,=INPBUF      
         ANM  R32,=7FH,0
         LDM  R34,=INPBUF      
         JSB  =INSERT          
         STM  R32,R2           
         STM  R42,R30          
         REN
         ADM  R34,R2           
         JSB  =STALRM
         CLE                   
         RTN                   

APTR+    JSB  =APSTAT
         CMM  R32,R34          
         JZR  APTR-
         ADM  R32,R2           
         CMM  R32,R34          
         RNZ

APTR-    LDM  R20,R30          
         CMM  R20,R32          
         RZR
krps2_21 DRP !20
         STM  R20,R22          
         CLM  R20              
         LDBD R20,R22          
         LLB  R20              
         LRB  R20              
         ADM  R20,R22          
         CMM  R20,R32          
         JNC  krps2_21
         STM  R22,R32          
         RTN                   

GETLNX   LDM  R22,=INPBUF      
krps2_31 POBD R24,+R20         
         PUBD R24,+R22         
         JNZ  krps2_31
         POMD R44,+R20         
         POMD R53,+R20         
         STM  R53,R20          
         RTN                   

RSTBUF   LDM  R73,=40D,PSTEMP,INPBUF
         JMP  krps2_41

SAVBUF   LDM  R73,=40D,INPBUF,PSTEMP
krps2_41 JSB  =KOPY            
         RTN                   

TIMDIV   LDB  R20,=ONES
krps2_51 ICB  R20              
         CMB  R20,=99D
         JZR  krps2_52
         SBMD R45,R26          
         JCY  krps2_51
         ADMD R45,R26          
krps2_52 JSB  =TOBCD2          
         JSB  =TOASC2          
         CMM  R20,='00'
         RTN                   

TTMPLT   LDM  R20,=(TIMTPT).2
         JMP  krps2_71
ATMPLT   LDM  R20,=APPTTM
krps2_71 JSB  =GETLNX
         LDBD R27,=PSSTAT      
         ELB  R27              
         ELB  R27              
         ELB  R27              
         JNC  krps2_72
         LDM  R52,='Dy\Mo\'
         STMD R52,=INP+4       
krps2_72 ELB  R27              
         JNC  krps2_73
         LDM  R56,='**'
         STMD R56,R20          
krps2_73 LDM  R20,=INPBUF      
         RTN                   

APMSKE   DATA ((FILL0)+4).1
         DATA 00010010B,01001001B,00100110B
         DATA 01100000B

APMSKY   DATA ((FILL0)+4).1
         DATA 00010010B,01111001B,00100110B
         DATA 01100000B

RPTMSK   DATA ((FILL1)-3).1
         DATA 11111001B,00100100B,11100011B

STMMSK   DATA ((FILL1)-4).1
         DATA 11110010B,01000010B,01001001B
         DATA 00111111B

TIMMSK   DATA ((FILL1)-4).1
         DATA 11111111B,11111111B,11111111B
         DATA 11100000B

YRMASK   DATA ((FILL1)-2).1
         DATA 11111110B,00011111B


APPTTM   DATA 'Day Mo/Dy/Yr Hr:Mn AM #1N !Note'
         DATA 0H
         DEF  AINCHK
         DEF  APMSKE
         DEF  INP+19
         DEF  INPBUF
         DATA 31D

TIMTPT   DATA 'Set Mo/Dy/Year Hr:Mn:Sc AM'
         DATA 0H
         DEF  TINCHK
         DEF  STMMSK
         DEF  INP+24
         DEF  INP+4
         DATA 26D

YEARTM   DATA ' Year? YYYY'
         DATA 0H
         DEF  YINCHK
         DEF  YRMASK
         DEF  INPBUF
         DEF  INP+7
         DATA 11D

INFOTM   DATA 'Yr=     | '
REPTTM   DATA 'Rept=Mo+Dy+Hr+Mn | DOW'
         DATA 0H
         DEF  RINCHK
         DEF  RPTMSK
         DEF  INPBUF
         DEF  INP+5
         DATA 22D

HRSEC    DATA (3600D).3
MNSEC    DATA (60D).3
       TITLE 'krps1'
*
*  __________________________________________________________________
* |KRPS1 376 06/24/82 - 7/13/1982 12:14PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@      @@@@@@        @@       ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@      @@@       ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@@    @@@    @@@@       ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@   @@@@@       ||
* ||   @@ @@@      @@     @@   @@     @@@  @@@             @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@    @@@@@@@        @@       ||
* ||   @@@@@       @@@@@@@     @@@@@@@@      @@@@@@@       @@       ||
* ||   @@ @@@      @@    @@@   @@                 @@@      @@       ||
* ||   @@  @@@     @@     @@@  @@          @@      @@      @@       ||
* ||   @@   @@@    @@      @@  @@          @@@     @@      @@       ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@   @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@            @@@@@@    @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1336>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
APPTMD   JSB  =ACREAT          
         JEZ  krps1_1
         LDB  R25,=EDITKY
         JSBN  =ERROR+          
         DATA 16D

krps1_1  CLM  R2               
         STBD R2,=((PSTEMP)+10D).2
krps1_2  ADM  R32,R2           
         CMM  R32,R34          
         JZR  krps1_3
         JSB  =APSTAT
         JCY  krps1_2
         LDBD R2,=PSSTAT       
         JPS  krps1_3
         LDB  R3,=BIT#7
krps1_3  STBD R3,=PSIOST       

APPT00   JSB  =HANDI0          
          VAL V.APT0
         LDBD R37,=PSIOST      
         DCB  R37              
         STBD R37,=PSIOST      
         JEV  krps1_11
         ICB  R37              
         ANM  R37,=BIT#7
         STBD R37,=PSIOST      

         JSB  =BLIMP           
         JSB  =ATMPLT
         TSB  R37              
         JPS  krps1_11
         JSB  =APTDSP

krps1_11 LDM  R44,=(AINCHK).2,(APMSKE).2
         LDBD R27,=PSSTAT      
         ANM  R27,=BIT#6
         JNZ  krps1_12
         LDM  R46,=APMSKY

krps1_12 JSB  =GETTEM          
         JSB  =ANN.E-          
         LDM  R73,=32D,(INPBUF).2,(TMPLAT).2
         JSB  =KOPY            
         STBD R24,R76          
         DRP  R25              
         JSB  =LOOKUP          
          DEF APTKYS
         IFEN
           CLM  R2               
         ENDIF
         STM  R2,R66           
         JSB  =HANDI0          
          VAL V.AKEY
         TSM  R66              
         JZR  APEXIT
         STM  R66,R4           

APTKYS   DATA CR
         DATA (APPT01).2
         DATA ATTNKY
         DATA (APPT05).2
         DATA UPKEY
         DATA (APPT10).2
         DATA DOWNKY
         DATA (APPT20).2
         DATA CLRKEY
         DATA (APPT40).2
         DATA RUNKEY
         DATA (APPT50).2
         DATA ((APPTKY)+(SHIFT)).1
         DATA (APPT60).2
         DATA ((UPKEY)+(SHIFT)).1
         DATA (APPT70).2
         DATA ((DOWNKY)+(SHIFT)).1
         DATA (APPT80).2
         DATA ((DELKEY)+(SHIFT)).1
         DATA (APPT90).2
         DATA 0H

APEXIT   JSB  =HANDI0          
          VAL V.ARTN
         JSB  =BLEBUF          
         CMM  R30,R34          
         RNZ
         LDMD R40,=APFILE      
         JSB  =FPURGE          
         RTN                   

APPT01   LDBD R27,=PSIOST      
         ANM  R27,=BIT#6
         JZR  APLOOP

APPT02   JSB  =APTCHK          
         JEN  APLOOP 
         JSB  =APTFND
         JSB  =DUPCHK
         LDB  R37,=71D
         JEN  krps1_21

         JSB  =APTINS
         JEZ  STATLP
         LDB  R37,=16D
krps1_21 JSB  =NUNPCK
         LDB  R20,R37          
         JSB  =APTERR
         JMP  APLOOP

APPT05   LDBD R27,=PSIOST      
         ANM  R27,=0C0H
         ADB  R27,=BIT#7
         JNZ  APPT40
         JSB  =APTACK
         JMP  APLOOP

APPT10   JSB  =APTR-
         JMP  STATLP

APPT20   JSB  =APTR+

STATLP   CMM  R32,R34          
         DRP  R3               
         IFNC
           LDB  R3,=BIT#7
         ELSE
           CLB  R3               
         ENDIF
krps1_31 STBD R3,=PSIOST       
APLOOP   GTO APPT00

APPT40   CLB  R2               
         STBD R2,=PSIOST       
         JMP  APLOOP

APPT50   JSB  =APEXIT
         JSB  =APPROC
         LDB  R36,=APPTKY
         REZ
         STB  R36,R25          
         RTN                   

APPT60   LDBD R3,=PSIOST       
         JPS  STATLP
         ANM  R3,=BIT#6
         JNZ  STATLP
         JSB  =APINFO          
         JMP  STATLP

APPT70   LDM  R32,R30          
         JMP  STATLP

APPT80   LDM  R32,R34          
         JSB  =APTR-
         JMP  STATLP

APPT90   LDBD R27,=PSIOST      
         JPS  APLOOP
         PUBD R27,+R6          
         JSB  =APTDEL
         POBD R3,-R6           
         ANM  R3,=BIT#6
         JZR  STATLP
         GTO APPT02

TIMEMD   JSB  =BLIMP           
         JSB  =TCKTGL
         JSB  =TICK
krps1_41 LDB  R24,=27D          
krps1_42 LDM  R20,=INPBUF      
         LDM  R22,=INP+27      
         LDM  R44,=(TINCHK).2,(TIMMSK).2
         JSB  =GETTEM          
         JZR  krps1_41
         IFPS
           JSB  =TMECMD
           JMP krps1_42
         ENDIF

krps1_43 JSB  =TCKTGL
         CLM  R40              
         LDB  R40,=21D          
         JSB  =CMPENT          
         JSB  =CMPCHK          
         RTN                   

CSTRIG   JSB  =HANDI0          
          VAL V.CLOK

CKTRIG   LDBD R2,=PSSTAT       
         REV
         CLB  R20              
         JSB  =STDATE
         LDM  R40,R50          
         JSB  =FXTIME
         STMD R45,=INP+23      
         LDB  R45,=':'          
         LDB  R20,R50          
         JSB  =TOASC2          
         STM  R20,R46          
         LDB  R20,R56          
         JSB  =TOASC2          
         LDMD R22,=INP+10      
         STMD R40,=INP+15      
         LDM  R44,R20          
         STMD R44,=INP+10      
         LDMD R36,=INPTR       
         SBM  R36,=INPBUF      
         JSB  =UPDISP
         RTN                   

AINCHK   LDMD R46,=INPTR       
         CMB  R40,=(SHIFT)+(DELKEY)
         JNZ  krps1_53
         ICE                   
krps1_53 DRP  !40
         CMB  R40,=LEFTKY
         JZR  krps1_54
         CMB  R40,=BS
         JNZ  krps1_55
         JSB  =krps1_57
krps1_54 CMM  R46,=INP+27      
         RNZ
         LDB  R40,=LEFT!
krps1_55 DRP  !40
         CMB  R40,=CR
         RZR
         CMB  R40,=DELKEY
         JZR  krps1_57
         TSB  R40              
         RNG
         CMM  R46,=INP+26      
         JNZ  krps1_57
         CMB  R40,='!'
         JZR  krps1_57
         CMB  R40,='>'
         JZR  krps1_57
         LDB  R40,=RGHTKY
         RTN                   

krps1_57 LDBD R3,=PSIOST       
         ANM  R3,=NOT#6
         ADB  R3,=BIT#6
         STBD R3,=PSIOST       
         RTN                   

RINCHK   BSS 0
TINCHK   BSS 0
YINCHK   BSS 0

         CMB  R40,=I/RKEY
         JNZ  krps1_61
         LDB  R40,=NOPKEY
krps1_61 DRP  !40
         RTN                   

UPDISP   JSB  =CURSE-          
         JSB  =OUT1CH          
          VAL CR
         LDM  R26,=INPBUF      
         JSB  =HLFLIN          
         JSB  =CURSE+          
         RTN                   

STDATE   LDM  R26,=DAYSEC      
         JSB  =GETCLK
         JMP  krps1_72
krps1_71 ADMD R43,R26          
krps1_72 DCB  R20              
         JPS  krps1_71

         JSB  =DCDAY
         PUBD R27,+R6          
         JSB  =DCCLOK
         STM  R40,R50          
         LDM  R65,R43          
         STM  R65,R45          
         JSB  =FXDATE
         STMD R40,=INP+4       
         POBD R20,-R6          
         JSB  =FXDAY
         STMD R45,=INPBUF      
         RTN                   

TICK     LDMD R40,=RTCSB         
         ANM  R40,=0,0,0C0H,0FFH,0FFH,0FFH,0,0
         JZR  TICK
         LDB  R40,=21D
         LDMD R20,=TMBASE      
         TCM  R20              
         ANM  R20,=0FFH,3FH
         ADM  R20,R41          
         STM  R20,R41          
         JSB  =CMPENT          
         RTN                   
       TITLE 'krps3'
*
*  __________________________________________________________________
* |KRPS3 402 09/27/82 - 12/ 9/1982 1:05PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@      @@@@@@       @@@@  @   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@    @@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@@    @@@  @@@    @@@   ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@     @@@  @@@               @@@    ||
* ||   @@@@@       @@@@@@@     @@@@@@@@@    @@@@@@@       @@@@      ||
* ||   @@@@@       @@@@@@@     @@@@@@@@      @@@@@@@        @@@@    ||
* ||   @@ @@@      @@    @@@   @@                 @@@          @@   ||
* ||   @@  @@@     @@     @@@  @@          @@      @@          @@   ||
* ||   @@   @@@    @@      @@  @@          @@@     @@          @@   ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@    @@@@@@@@    ||
* ||   @@     @@@  @@      @@  @@            @@@@@@       @@@@      ||
* ||                                                                ||
* ||                  Last edited on <821209.1302>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
APTCHK   LDM  R20,=INPBUF      
         LDB  R27,=21D
krps3_1  LDBD R23,R20          
         ANM  R23,=NOT#7
         PUBD R23,+R20         
         DCB  R27              
         JNZ  krps3_1
         LDMD R45,=INPBUF      
         JSB  =DAYCHK
         JEZ  krps3_2
         LDB  R20,=73D
         JMP  SAVBYT

krps3_2  STBD R47,=INP+1       
         LDMD R40,=INP+4       
         JSB  =DATCHK
         JEZ  krps3_3
         LDB  R20,=74D         
         JSB  =APTERR            
         LDM  R22,=INP+4       
         RTN                   

krps3_3  STMD R44,=INP+6       
         LDMD R40,=INP+13      
         JSB  =TIMCHK
         JEZ  krps3_4
         LDB  R20,=75D
         JSB  =APTERR            
         LDM  R22,=INP+13      
         RTN                   

krps3_4  STMD R45,=INP+3       
         JSB  =GETTD
         LDMD R50,=INP+3       
         CLB  R57              
         LDBD R21,=INP+1       
         JSB  =FINDTD
         JEZ  krps3_5
         LDB  R20,=72D

SAVBYT   JSB  =APTERR            
         RTN                   

krps3_5  STMD R43,=INP+1       
         LDMD R46,=INP+23      
         JSB  =ALMCHK          
         JEZ  krps3_7
         LDB  R20,=77D
krps3_6  JSB  =APTERR            
         LDM  R22,=INP+23      
         RTN                   

krps3_7  LDM  R76,=INP+6       
         PUBD R47,+R76         
         JPS  krps3_8
         JSB  =RPTINP
         STMD R43,=INP+7       
         LDM  R76,=INP+12      
         JEZ  krps3_8
         LDB  R20,=76D
         JMP  krps3_6

krps3_8  LDBD R73,=APTSIZ      
         CMB  R73,=31D
         JNZ  krps3_9
         LDMD R43,=INP+26      
         CMM  R43,='!Note'
         JNZ  krps3_9
         LDB  R73,=26D

krps3_9  LDM  R20,=INP+26      
         STM  R20,R74          
         SBB  R73,=26D
         JZR  krps3_0
         JSB  =KOPY            
krps3_0  SBM  R76,=INPBUF      
         STBD R76,=INPBUF      
         RTN                   

DCCLOK   LDM  R26,=DAYSEC      
         LDM  R20,=04FCH        
krps3_11 ADB  R20,=4           
         SBM  R43,=200,131,140,360,2 
         JPS  krps3_11
krps3_12 DRP  !43
         STM  R43,R53          
         DCB  R21              
         JNZ  krps3_13
         ADMD R43,R26          
krps3_13 ADM  R43,=0,302,27,274,0 
         JNG  krps3_12
         ADB  R20,R21          
         TSB  R21              
         JZR  krps3_14
         LDB  R21,=ONES
krps3_14 DRP  !21
         ADB  R21,=26D
         LDM  R22,=104D,0
krps3_15 LDM  R43,R53          
         SBB  R22,=4           
         DCB  R21              
         JNZ  krps3_16
         SBMD R53,R26          
krps3_16 ADM  R53,=200,37,206,7,0 
         JNG  krps3_15
         TSB  R21              
         JZR  krps3_17
         LDB  R21,=ONES
krps3_17 DRP  !21
         ADB  R21,=5           
krps3_18 DCB  R22              
         DCB  R21              
         JNZ  krps3_19
         ICB  R23              
         ADMD R43,R26          
krps3_19 ADM  R43,=200,63,341,1,0 
         JNG  krps3_18
         CLB  R21              
         STM  R43,R53          
         SBM  R43,=200,336,50,0,0 
         JNG  krps3_22
         STM  R43,R53          
         ICB  R21              
         TSB  R23              
         JZR  krps3_10
         SBMD R43,R26          
krps3_10 SBM  R43,=0,352,44,0,0 
         JNG  krps3_22
         STM  R43,R53          
         CLB  R21              
         SBM  R43,=200,265,311,0,0 
         JNG  krps3_21
         STM  R43,R53          
         LDB  R21,=5           
krps3_21 ADB  R21,=2           
         STM  R53,R43          
         SBM  R53,=200,153,120,0,0 
         JPS  krps3_21
         STM  R43,R53          
         SBM  R43,=200,336,50,0,0 
         JNG  krps3_22
         STM  R43,R53          
         ICB  R21              
krps3_22 ICB  R21              
         CLB  R23              
krps3_23 ICB  R23              
         STM  R53,R43          
         SBMD R53,R26          
         JPS  krps3_23
         LDM  R24,=377,377
krps3_24 ICB  R24              
         STM  R43,R53          
         SBM  R43,=20,16,0,0,0 
         JPS  krps3_24
krps3_25 ICB  R25              
         STM  R53,R43          
         SBM  R53,=74,0,0,0,0  
         JPS  krps3_25
         STB  R43,R40          
         STB  R25,R41          
         STB  R24,R42          
         STB  R23,R43          
         STB  R21,R44          
         STB  R22,R45          
         STB  R20,R46          
         CLB  R47              
         JSB  =TOBCD8          
         RTN                   

ENCLOC   PUMD R20,+R6          
         JSB  =TOBIN8          
         STM  R40,R20          
         CLM  R40              
         LDB  R40,=4           
         LDM  R0,=DAYSEC       
krps3_31 ADM  R43,=200,131,140,360,2 
         SBB  R26,=4           
         JPS  krps3_31
krps3_32 SBM  R43,=0,302,27,274,0 
         DCB  R40              
         JNZ  krps3_33
         SBMD R43,R0           
krps3_33 ICB  R26              
         JNZ  krps3_32
         TSB  R25              
         JZR  krps3_37
         TSB  R40              
         JZR  krps3_34
         SBMD R43,R0           
krps3_34 ADM  R43,=200,37,206,7,0 
         SBB  R25,=4           
         JPS  krps3_34
         LDB  R40,=4           
krps3_35 SBM  R43,=200,63,341,1,0 
         DCB  R40              
         JNZ  krps3_36
         SBMD R43,R0           
krps3_36 ICB  R25              
         JNZ  krps3_35
krps3_37 DCB  R24              
         JZR  krps3_42
         ADM  R43,=200,336,50,0,0 
         DCB  R24              
         JZR  krps3_42
         ADM  R43,=0,352,44,0,0 
         TSB  R40              
         JNZ  krps3_38
         ADMD R43,R0           
krps3_38 CMB  R24,=6           
         JNC  krps3_39
         SBB  R24,=5           
         ADM  R43,=200,265,311,0,0 
krps3_39 CMB  R24,=3           
         JNC  krps3_30
         SBB  R24,=2           
         ADM  R43,=200,153,120,0,0 
         JMP  krps3_39
krps3_30 DCB  R24              
         JZR  krps3_42
         ADM  R43,=200,336,50,0,0 
         JMP  krps3_42
krps3_41 ADMD R43,R0           
krps3_42 DCB  R23              
         JNZ  krps3_41
         JMP  krps3_44         
krps3_43 ADM  R43,=20,16,0,0,0 
krps3_44 DCB  R22              
         JPS  krps3_43
         JMP  krps3_46
krps3_45 ADM  R43,=74,0,0,0,0  
krps3_46 DCB  R21              
         JPS  krps3_45
         ADB  R43,R20          
         JNC  krps3_47
         ICM  R44              
krps3_47 POMD R20,-R6          
         RTN                   

FINDTD   BCD                   
         LDM  R70,=
MAXSAT   DATA 0,59C,23C,31C,12C,99C,99C,0
         STM  R40,R60          
         LDBD R3,=PSSTAT       
         ANM  R3,=BIT#6
         JNZ  krps3_51
         LDM  R2,R65           
         ICM  R2               
         JCY  krps3_56
         STM  R2,R75           
         JMP  krps3_56
krps3_51 LDB  R2,R66           
         ADB  R2,=4            
         JCY  krps3_52
         STB  R2,R76           
krps3_52 CMM  R55,=377,377,0   
         JZR  krps3_56
         JSB  =MINYY

FNDTD_   BIN
         CMB  R56,=ONES
         BCD
         JZR  krps3_54
         STB  R56,R66          
         STB  R56,R76          
         JMP  krps3_54

CENT+    ICB  R66              
         JCY  NOMTCH
         CMB  R76,R66          
         JCY  krps3_53

NOMTCH   BIN                   
         CLE                   
         ICE                   
         RTN                   

krps3_53 JSB  =MINYY

krps3_54 JSB  =MELJSB
          DEF FIX65
         JMP krps3_56

YEAR+    ICB  R65              
         JCY  CENT+
         CMB  R75,R65          
         JNC  CENT+
krps3_55 JSB  =MINMM
krps3_56 LDB  R47,R64          
         CMB  R54,=ONES         
         JZR  krps3_58
         STB  R54,R64          
         STB  R54,R74          
         CMB  R54,R47          
         JNC  YEAR+
         JZR  krps3_58
         JMP  krps3_57

MONTH+   ICB  R64              
         CMB  R74,R64          
         JNC  YEAR+
         LDB  R73,=31C
krps3_57 JSB  =MINDD
krps3_58 LDB  R47,R63          
         CMB  R53,=ONES
         JZR  krps3_50
         STB  R53,R63          
         STB  R53,R73          
         CMB  R53,R47          
         JNC  MONTH+
         JZR  krps3_50
         JMP  krps3_59

DAY+     ICB  R63              
         CMB  R73,R63          
         JNC  MONTH+
krps3_59 JSB  =MINHH
krps3_50 JSB  =DAYOK
         JEN  MONTH+
         LDB  R47,R62          
         CMB  R52,=ONES
         JZR  krps3_62
         STB  R52,R62          
         STB  R52,R72          
         CMB  R52,R47          
         JNC  DAY+
         JZR  krps3_62
         JMP  krps3_61

HOUR+    ICB  R62              
         CMB  R72,R62          
         JNC  DAY+
krps3_61 JSB  =MINMN
krps3_62 LDB  R47,R61          
         CMB  R51,=ONES
         JZR  krps3_63
         STB  R51,R61          
         STB  R51,R71          
         CMB  R51,R47          
         JNC  HOUR+
         JZR  krps3_63
         CLB  R60              
krps3_63 TSB  R60              
         JZR  krps3_64
         CLB  R60              
         ICB  R61              
         CMB  R71,R61          
         JNC  HOUR+
krps3_64 LDM  R40,R60          
         BIN                   
         JSB  =ENCLOK
         TSB  R21              
         JZR  krps3_67
         JSB  =DCDAY
         BCD                   
         CLM  R22              
         LDB  R22,R21          
         LLM  R22              
         TSB  R22              
         JNG  krps3_68
         JZR  krps3_66
         LDB  R26,R63          
         DCB  R26              
         CLB  R25              
krps3_65 ICB  R25              
         SBB  R26,=7C          
         JPS  krps3_65
         LLB  R25              
         CMB  R25,R22          
         JNZ  DAY+
krps3_66 CMB  R23,R27          
         JNZ  DAY+
         BIN                   
krps3_67 CLE                   
         RTN                   
krps3_68 BIN                   
         SBB  R22,=200         
         JZR  krps3_69
         LDB  R22,=7           
krps3_69 ADM  R43,=0,214,12,0,0 
         SBB  R27,R23          
         JNZ  krps3_60
         ADB  R22,R22          
krps3_60 JPS  krps3_71
         ADB  R27,=7           
krps3_71 ICB  R27              
         ADB  R27,R22          
         LDM  R24,=DAYSEC      
krps3_72 SBMD R43,R24          
         DCB  R27              
         JNZ  krps3_72
         TSM  R43              
         JNG  krps3_73
         CMM  R43,=200,275,150,171,111 
         JNC  krps3_67
krps3_73 CLE                   
         ICE                   
         RTN                   
GAP002   NOP
         NOP

FXAPPT   JSB  =NUNPCK
         LDBD R47,=INP+6       
         JSB  =FXALRM
         LDM  R53,=' ','#',0,0,' '
         STM  R46,R55          
         STMD R53,=INP+21      
         JSB  =GETCLK
         STM  R43,R53          
         LDMD R43,=INP+1       
         JSB  =DCDAY
         TCM  R53              
         ADM  R53,R43          
         JPS  krps3_81
         TCM  R53              
         ADB  R27,=100         
krps3_81 SBM  R53,=200,215,66,272,0 
         JNG  krps3_82
         ADB  R27,=200         
krps3_82 STBD R27,=INP+1       
         JSB  =DCCLOK
         STMD R43,=INP+3       
         JSB  =FXTIME
         STMD R40,=INP+13      
         LDMD R45,=INP+3       
         JSB  =FXDATE
         STMD R40,=INP+4       
         LDB  R40,=' '
         STBD R40,=INP+3       
         STBD R40,=INP+12      
         LDBD R20,=INP+1       
         JSB  =FXDAY
         LDBD R24,=INPBUF      
         STMD R45,=INPBUF      
         LLB  R20              
         JNC  krps3_83
         LDM  R2,='**'
         STMD R2,=INP+10       
krps3_83 LLB  R20              
         RNC
         LDM  R20,=INPBUF      
         LDB  R27,=21D
krps3_84 LDBD R26,R20          
         ADB  R26,=200         
         PUBD R26,+R20         
         DCB  R27              
         JNZ  krps3_84
         RTN                   
       TITLE 'krps4'
*
*  __________________________________________________________________
* |KXPS4 416 08/31/82 - 9/ 2/1982 6:59AM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@      @@@@@@          @@     ||
* ||   @@    @@@   @@      @@  @@@@@@@@@    @@@@@@@@        @@@     ||
* ||   @@   @@@    @@@    @@@  @@     @@@  @@@    @@@      @@@@     ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@      @@     @@@@@     ||
* ||   @@ @@@         @@@@     @@     @@@  @@@           @@@ @@     ||
* ||   @@@@@           @@      @@@@@@@@@    @@@@@@@     @@@  @@     ||
* ||   @@@@@           @@      @@@@@@@@      @@@@@@@   @@@   @@     ||
* ||   @@ @@@         @@@@     @@                 @@@  @@@@@@@@@@   ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@@@@@@@@@   ||
* ||   @@   @@@    @@@    @@@  @@          @@@     @@        @@     ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@         @@     ||
* ||   @@     @@@  @@      @@  @@            @@@@@@          @@     ||
* ||                                                                ||
* ||                  Last edited on <820902.0656>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
ALMCHK   LDM  R21,R46          
         CMB  R21,=' '
         JNZ  krps4_1
         LDB  R21,='1'
krps4_1  LDB  R20,='0'
         JSB  =NUMCHK          
         CMB  R47,=' '
         JZR  krps4_2
         ANM  R47,=337         
         CMB  R47,='N'
         JZR  krps4_2
         ADB  R21,=BIT#6
         ADB  R21,=BIT#6
         CMB  R47,='R'
         JZR  krps4_2
         ADB  R21,=BIT#6
         CMB  R47,='A'
         JZR  krps4_2
         ICE                   
krps4_2  STB  R21,R47          
         RTN                   

DATCHK   LDBD R3,=PSSTAT       
         ANM  R3,=BIT#6
         JNZ  krps4_11
         LDM  R46,='Yr'
krps4_11 LDM  R20,R43          
         STM  R20,R42          
         LDM  R20,='YY'
         STM  R20,R44          
         CMM  R46,='**'
         JNZ  DATCK_
         JSB  =FXYEAR
DATCK_   STM  R40,R20          
         LDBD R47,=PSSTAT      
         ANM  R47,=BIT#5
         JNZ  krps4_12
         LDM  R20,R42          
         LDM  R22,R40          
krps4_12 LDM  R0,='Dy'
         JSB  =FLDCHK            
         JEN  DATERR             
         STB  R20,R44          
         LDM  R20,R24          
         LDM  R0,='YY'
         JSB  =FLDCHK            
         JEN  DATERR             
         STB  R20,R47          
         LDM  R20,R26          
         LDM  R0,='Yr'
         JSB  =FLDCHK            
         JEN  DATERR             
         STB  R20,R46          
         LDM  R20,R22          
         LDM  R0,='Mo'
         JSB  =FLDCHK            
         JEN  DATERR             
         STB  R20,R45          
         ICE                   
         CMB  R45,=ONES
         JZR  krps4_13
         TSB  R45              
         JZR  DATERR             
         CMB  R45,=13C
         JCY  DATERR             
krps4_13 TSB  R44              
         JZR  DATERR             
         CMB  R44,=ONES
         JZR  DATRTN             
         CMB  R44,=29C
         JZR  krps4_14
         ICB  R20              
         LDBD R20,X20,DTAB-1   
         CMB  R20,R44          
         JCY  DATRTN             
         RTN                   

krps4_14 CMB  R45,=2           
         JNZ  DATRTN             
         LDB  R65,R46          
         CMB  R65,=ONES
         JZR  DATRTN             
         LDB  R66,R47          
         CMB  R66,=ONES
         JNZ  krps4_15
         CLB  R66              
krps4_15 JSB  =LEAPYR
         JEZ  DATERR             
DATRTN   CLE                   
DATERR   RTN                   

DAYCHK   CLE                   
         CMM  R45,='Day'
         JZR  krps4_21
         CMMD R45,=BLANKS      
         JNZ  krps4_22
krps4_21 DRP  !45
         CLM  R45              
         RTN                   

krps4_22 LDM  R55,=337,337,337 
         ANM  R55,R45          
         STM  R55,R20          
         LDM  R55,=160,(DAYTB1).2
krps4_23 CMMD R20,R56          
         JZR  krps4_24
         SBM  R55,=20,3,0      
         TSB  R55              
         JNZ  krps4_23
         JMP  DAYERR
krps4_24 LDB  R21,R55          
         ADM  R56,=2,0
         CMBD R22,R56          
         JZR  DAYRTN             
         CMB  R47,=BLANK
         JZR  DAYRTN             
         ADB  R21,=8D          
         CMB  R47,='+'
         JZR  DAYRTN             
         ICB  R21              
         CMB  R47,='-'
         JZR  DAYRTN             
         SBB  R21,=9D
         SBB  R47,='0'
         JNG  DAYERR
         JZR  DAYERR
         CMB  R47,=6           
         JNC  krps4_25
DAYERR   ICE                   
krps4_25 ORB  R21,R47          
DAYRTN   LDM  R47,R21          
         RTN                   

DAYTAB   DATA 'SAT'
         DATA 'SUN'
         DATA 'MON'
         DATA 'TUE'
         DATA 'WED'
         DATA 'THU'
DAYTB1   DATA 'FRI'

DAYOK    CLM  R0               
         LDB  R0,R64           
         LDBD R0,X0,DTAB0      
         CMB  R64,=2           
         JNZ  krps4_3x
         JSB  =LEAPYR
         JEN  krps4_3x
         DCB  R0               
krps4_3x CLE                   
         CMB  R0,R63           
         RCY
         ICE                   
         RTN                   

DCDAY    PUMD R43,+R6          
krps4_31 DRP  !43
         SBM  R43,=0,250,332,150,5 
         JPS  krps4_31
krps4_32 DRP  !43
         ADM  R43,=0,14,353,142,0 
         JNG  krps4_32
krps4_33 DRP  !43
         SBM  R43,=0,312,20,7,0 
         JPS  krps4_33
krps4_34 DRP  !43
         ADM  R43,=0,63,201,0,0 
         JNG  krps4_34
krps4_35 DRP  !43
         SBM  R43,=200,72,11,0,0 
         JPS  krps4_35
         LDB  R27,=8D
krps4_36 DCB  R27              
         ADM  R43,=200,121,1,0,0 
         JNG  krps4_36
         POMD R43,-R6          
         RTN                   

DUPCHK   CLE                   
         CLM  R2               
krps4_41 ADM  R32,R2           
         CMM  R32,R34          
         RZR
         STM  R32,R22          
         POBD R26,+R22         
         LDM  R20,=INPBUF      
         POBD R27,+R20         
         ANM  R26,=177,177
         STB  R26,R2           
         POMD R43,+R20         
         POMD R53,+R22         
         CMM  R53,R43          
         RNZ
         CMB  R27,R26          
         JNZ  krps4_41
         SBB  R27,=6           
         POBD R25,+R20         
         POBD R24,+R22         
         ANM  R24,=317,317
         JMP  krps4_43
krps4_42 POBD R25,+R20         
         POBD R24,+R22         
krps4_43 DRP  !24
         CMB  R24,R25          
         JNZ  krps4_41
         DCB  R27              
         JNZ  krps4_42
         ICE                   
         RTN                   

FLDCHK   CLE                   
         CMM  R20,R0           
         JZR  krps4_0
         CMM  R20,='  '
         JZR  krps4_0
         JSB  =NUMCHK          
         STB  R21,R20          
         CLB  R21              
         RTN                   
krps4_0  DRP  !20 
         CLM  R20              
         DCB  R20              
         RTN                   

FXALRM   LDM  R0,R46           
         ANM  R47,=17          
         STB  R47,R46          
         ADB  R46,='0'
         ANM  R0,=0,300
         ELM  R0               
         ELM  R0               
         ELM  R0               
         LDBD R47,X0,ALMTAB
         RTN                   
ALMTAB   DATA 'NDRA'

FXDATE   STB  R45,R20          
         LDB  R45,='/'
         STB  R45,R42          
         JSB  =TOASC2          
         STM  R20,R22          
         STM  R20,R43          
         LDB  R20,R46          
         JSB  =TOASC2          
         STM  R20,R40          
         LDBD R27,=PSSTAT      
         ANM  R27,=BIT#5
         JZR  krps4_ft
         STM  R20,R43          
         STM  R22,R40          
         LDB  R42,='\'
         STB  R42,R45          
krps4_ft LDM  R20,R47          
         JSB  =TOASC2          
         STM  R20,R46          
         RTN                   

FXDAY    LDM  R26,=((DAYTAB)-3).2
krps4_fd ADM  R26,=3,0
         DCB  R20              
         JRN  krps4_fd
         LDMD R45,R26          
         RTN                   

FXTIME   LDB  R20,R41          
         JSB  =TOASC2          
         STM  R20,R43          
         LDB  R20,R42          
         LDM  R45,=' **'
         LDBD R23,=PSSTAT      
         ANM  R23,=BIT#4
         JNZ  krps4_52
         LDM  R46,='AM'
         CMB  R20,=12C
         JNC  krps4_51
         BCD                   
         SBB  R20,=12C
         BIN                   
         LDB  R46,='P'
krps4_51 TSB  R20              
         JNZ  krps4_52
         LDB  R20,=12C
krps4_52 JSB  =TOASC2          
         STM  R20,R40          
         LDB  R42,=':'
         RTN                   

FXYEAR   JSB  =SAVBUF
krps4_61 LDM  R20,=YEARTM
         JSB  =GETLNX
         JSB  =GETTEM          
         JZR  krps4_61
         JNG  krps4_62
         LDMD R44,=INP+7       
         CMB  R47,='Y'
         JNZ  krps4_63
         LDB  R47,='r'         
         JMP  krps4_63
krps4_62 LDB  R44,='X'
krps4_63 JSB  =RSTBUF
         RTN                   

LEAPYR   CLE                   
         LDB  R27,R65          
         JNZ  krps4_71
         LDB  R27,R66          
krps4_71 DRP  !27
         ANM  R27,=13H
         JLZ  krps4_72
         SBB  R27,=12H
krps4_72 RNZ
         ICE                   
         RTN                   

MINYY    CLB  R65              
MINMM    LDB  R64,=1           
MINDD    LDB  R63,=1           
MINHH    CLB  R62              
MINMN    CLB  R61              
         CLB  R60              
         RTN                   

NUNPCK   CLM  R73              
         LDBD R73,=INP+6       
         ADB  R73,=BIT#7
         JNC  krps4_81
         LDB  R74,=5           
krps4_81 LDBD R21,=INPBUF      
         ANM  R21,=7FH
         ADB  R21,=19D
         SBB  R21,R74          
         STBD R21,=INPBUF      
         SBB  R21,=26D
         STB  R21,R73          
         STB  R21,R76          
         ADB  R74,R21          
         ADM  R74,=(INP+7).2,(INP+26).2
         JMP  krps4_83

krps4_82 POBD R72,-R74         
         PUBD R72,-R76         
krps4_83 DCB  R73              
         JPS  krps4_82
         RTN                   

RPTADJ   LDB  R50,=16D
RPTAJ_   LDMD R43,X32,ONE
         JSB  =DCCLOK
         LDB  R43,=1           
         ANM  R46,=37,0
         STM  R40,R70          
         JSB  =ENCLOK
         STM  R40,R60          
         LDM  R40,R70          
         LDBD R44,X32,EIGHT

         BCD                   
krps4_91 ICM  R45              
         SBB  R44,=12C
         JCY  krps4_91
         ADB  R44,R74          
         JZR  krps4_92
         JCY  krps4_93
krps4_92 DRP  !44
         ADB  R44,=12C
         DCM  R45              
krps4_93 BIN                   
         JSB  =ENCLOK
         SBM  R43,R63          
         LDMD R53,X32,NINE
         CLM  R56              
         ADM  R53,R43          
         LDMD R43,X32,ONE
         ADM  R43,R53          
krps4_94 LDM  R53,=177,275,150,171,111 
         CMM  R43,R53          
         JNC  krps4_95
         LDM  R43,R53          
         JMP  krps4_90
krps4_95 DRP  !43
         STM  R43,R63          
         JSB  =DCCLOK
         BCD                   
         LDB  R21,R43          
         DCB  R21              
         CLB  R20              
krps4_96 DRP  !20
         ADM  R20,=1,93C
         JCY  krps4_96
         LDM  R43,R63          
         BIN                   
         JSB  =DCDAY
         BCD                   
         LLB  R27              
         BIN                   
         LDBD R21,X32,SEVEN
         JZR  krps4_90
         SBB  R21,R27          
         JLZ  krps4_97
         ADMD R43,=DAYSEC      
         JMP  krps4_94
krps4_97 JRZ  krps4_99
         CMB  R21,=8C
         JZR  krps4_99
         JCY  krps4_98
         CMB  R21,R20          
         JZR  krps4_99
         ADM  R43,=200,72,11,0,0 
         JMP  krps4_94
krps4_98 SBM  R43,=200,72,11,0,0 
krps4_99 LDMD R53,X32,ONE
         CMM  R53,R43          
         JNG  krps4_90
         ADM  R43,=200,72,11,0,0 
         JMP  krps4_99
krps4_90 PUMD R34,+R6          
         PUMD R30,+R6          
         PUMD R32,+R6          
         JSB  =APFND_
         POMD R34,-R6          
         STM  R32,R30          
         LDBD R32,R34          
         ANM  R32,=177,0
         STB  R32,R42          
         STMD R42,R34          
         JSB  =MOVE            
         STM  R30,R32          
         POMD R30,-R6          
         POMD R34,-R6          
         JSB  =GETCLK
         LDMD R53,X32,ONE
         CMM  R53,R43          
         JCY  krps4_c2
         DCB  R50              
         JNZ  krps4_c1
         JSB  =GETTD
         CLB  R40              
         JSB  =ENCLOK
         STMD R43,X32,ONE
krps4_c1 GTO RPTAJ_
krps4_c2 LDBD R27,X32,SIX
         ANM  R27,=NOT#5
         STBD R27,X32,SIX
         JSB  =STALRM
         RTN                   

RPTINP   JSB  =SAVBUF
krps4_a1 LDM  R20,=REPTTM
         JSB  =GETLNX
         JSB  =GETTEM          
         JZR  krps4_a1
         CLE                   
         DCE                   
         JNG  RPTRTN
RPTPRS   CLM  R43              
         LDMD R45,=INP+19      
         CMM  R45,='DOW'
         JZR  krps4_a2
         JSB  =DAYCHK
         JEN  RPTRTN
         STB  R47,R43          
krps4_a2 LDMD R20,=INP+5       
         CMM  R20,='Mo'
         JZR  krps4_a3
         CMM  R20,='  '
         JZR  krps4_a3
         JSB  =NUMCHK          
         JEN  RPTRTN
         STB  R21,R44          
krps4_a3 CLM  R45              
         CLB  R22              
         LDMD R20,=INP+8       
         CMM  R20,='Dy'
         JZR  krps4_a5
         CMM  R20,='  '
         JZR  krps4_a5
         JSB  =NUMCHK          
         JEZ  krps4_a4
RPTRTN   JSB  =RSTBUF
         RTN                   

krps4_a4 STB  R21,R20          
         JSB  =TOBIN2          
         CLB  R21              
         LLM  R20              
         LLM  R20              
         LLM  R20              
         STM  R20,R45          
         LLM  R20              
         ADM  R45,R20          
krps4_a5 LDMD R20,=INP+11      
         CMM  R20,='Hr'
         JZR  krps4_a6
         CMM  R20,='  '
         JZR  krps4_a6
         JSB  =NUMCHK          
         JEN  RPTRTN
         STB  R21,R20          
         JSB  =TOBIN2          
         CLB  R21              
         ADM  R45,R20          
krps4_a6 JSB  =MULT60
         LDMD R20,=INP+14      
         CMM  R20,='Mn'
         JZR  krps4_a7
         CMM  R20,='  '
         JZR  krps4_a7
         JSB  =NUMCHK          
         JEN  RPTRTN             
         STB  R21,R20          
         JSB  =TOBIN2          
         CLM  R55              
         LDB  R55,R20          
         ADM  R45,R55          
krps4_a7 JSB  =MULT60
         TSM  R43              
         JNZ  RPTRTN             
         ICE                   
         JMP  RPTRTN             
TIMCHK   CLE                   
         STM  R40,R20          
         CLM  R45              
         DCM  R45              
         CMM  R20,='  '
         JZR  krps4_b1
         CMM  R20,='Hr'
         JZR  krps4_b1
         JSB  =NUMCHK          
         JEN  TIMRTN             
         CMB  R21,=24C
         JCY  TIMERR             
         STB  R21,R47          
krps4_b1 LDM  R20,R23          
         CMM  R20,='  '
         JZR  krps4_b2
         CMM  R20,='Mn'
         JZR  krps4_b2
         JSB  =NUMCHK          
         JEN  TIMRTN             
         CMB  R21,=60C
         JCY  TIMERR             
         STM  R20,R45          
krps4_b2 CMM  R26,='  '
         RZR
         CMM  R26,='**'
         RZR
         SBB  R47,=12C
         JZR  krps4_b3
         JPS  TIMERR             
         ADB  R47,=12C
         JNZ  krps4_b3
TIMERR   ICE                   
TIMRTN   RTN                   

krps4_b3 ANM  R26,=337,337
         CMM  R26,='AM'
         RZR
         CMM  R26,='PM'
         JNZ  TIMERR             
         TSB  R47              
         JNG  TIMERR             
         BCD                   
         ADB  R47,=12C
         BIN                   
         RTN                   
       TITLE 'krvr3'
*
*  __________________________________________________________________
* |KXVR3 NA                                                          |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@       @@@@  @   ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@    @@@@@@@@    ||
* ||   @@   @@@    @@@    @@@  @@      @@  @@     @@@  @@@    @@@   ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@         @@@@      @@    @@   @@     @@         @@@    ||
* ||   @@@@@           @@       @@    @@   @@@@@@@        @@@@      ||
* ||   @@@@@           @@       @@    @@   @@@@@@@          @@@@    ||
* ||   @@ @@@         @@@@       @@  @@    @@    @@@           @@   ||
* ||   @@  @@@      @@@  @@@      @@@@     @@     @@@          @@   ||
* ||   @@   @@@    @@@    @@@     @@@@     @@      @@          @@   ||
* ||   @@    @@@   @@      @@      @@      @@      @@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@      @@     @@@@      ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* VERSION LETTER FOR THIS ROM ('d')
* ********************************************************************
         DATA 'd'
       TITLE 'krsum'
*
*  __________________________________________________________________
* |KRSUM                                                             |
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
* CHECKSUM FOR THIS ROM
* ********************************************************************
*        DATA 0C5H
         DATA 32H  ; checksum for single file
       TITLE 'krps5'
S27-57 EQU 0E717H
*
*  __________________________________________________________________
* |KXPS5 433 07/19/82 - 8/ 6/1982 4:48PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@      @@@@@@    @@@@@@@@@@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@@    @@@@@@@@   @@@@@@@@@@   ||
* ||   @@   @@@    @@@    @@@  @@     @@@  @@@    @@@  @@           ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@      @@  @@           ||
* ||   @@ @@@         @@@@     @@     @@@  @@@         @@           ||
* ||   @@@@@           @@      @@@@@@@@@    @@@@@@@    @@@@@@@@     ||
* ||   @@@@@           @@      @@@@@@@@      @@@@@@@   @@@@@@@@@@   ||
* ||   @@ @@@         @@@@     @@                 @@@         @@@   ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@      @@   ||
* ||   @@   @@@    @@@    @@@  @@          @@@     @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@    @@@@@@@@    ||
* ||   @@     @@@  @@      @@  @@            @@@@@@      @@@@@@     ||
* ||                                                                ||
* ||                  Last edited on <820813.1431>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
ACREAT   JSB  =AOPEN
         REZ
         LDM  R20,=TYAPPT      
         JSB  =FCREAT          
         REN
         JMP  APPTRS

AOPEN    LDMD R40,=APFILE      
AOPEN_   JSB  =FOPEN           
         REN

APPTRS   LDMD R44,R30          
         STM  R44,R32          
         ADM  R34,R32          
         LDM  R30,R32          
         RTN                   

ALBEEP   ANM  R27,=17          
         RZR
         DCB  R27              
         LLB  R27              
         CMB  R27,=10D          
         JZR  krps5_4
         JNC  krps5_1
         SBB  R27,=10D          
         STMD R27,=CNALRM
         LDMD R40,=RTCSB         
         ADMD R41,=CMAJST      
         CLM  R46              
         JSB  =STCCMP
         JMP  ALBEEP

krps5_1  CLM  R20              
         LDB  R20,R27          
         LDMD R22,X20,ALRMTB
         POBD R27,+R22         
         LDM  R24,R22          
         JMP  krps5_3
krps5_2  CLM  R42              
         ARP  !22
         POBD R44,+R22         
         JSB  =BEEPER          
krps5_3  CLM  R20              
         POBD R20,+R22         
         JNZ  krps5_2
         STM  R24,R22          
         DCB  R27              
         JNZ  krps5_3
         RTN                   

krps5_4  LDB  R3,=1            
         LDM  R20,=0,8D
krps5_5  DRP  !20
         STB  R20,R22          
         LDBD R2,=CMPSB        
         XRB  R2,R3            
         STBD R2,=CMPSB        
krps5_6  DCB  R22              
         JNZ  krps5_6
         JSB  =STOP?           
         REN
         DCM  R20              
         JNZ  krps5_5
         RTN                   

ALRMTB   DEF ALARM1
         DEF ALARM2
         DEF ALARM3
         DEF ALARM4
         DEF ALARM5

ALARM1   DATA 1,3,6,0
ALARM2   DATA 1,64D,128D,0
ALARM3   DATA 4,25D,32D,50D,32D,0
ALARM4   DATA 32D,10D,8D,255D,0,0
ALARM5   DATA 1,50D,64D,12D,128D,0

APPROC   JSB  =HANDI0          
          VAL V.APRC
         JSB  =APTRIG
         JSB  =AOPEN
         CLM  R2               
         JEZ  krps5_12
krps5_11 STE
         RTN                   

krps5_12 ADM  R32,R2           
         CMM  R32,R34          
         JCY  krps5_11
         JSB  =APSTAT
         ANM  R27,=BIT#4
         JZR  krps5_12
         JSB  =PRNOTE
         PUBD R25,+R6          
         LDBD R27,X32,SIX
         JNG  krps5_13
         CMB  R27,=BIT#6
         JNC  krps5_13
         JSB  =APTDEL
         JMP  krps5_14

krps5_13 ANM  R27,=NOT#4
         STBD R27,X32,SIX
krps5_14 POBD R25,-R6          
         JZR  APPROC
         CLE                   
         RTN                   

APSTAT   CLE                   
         LDBD R27,X32,SIX
         LDB  R3,R27           
         ANM  R3,=BIT#5
         JZR  krps5_21
         ICE                   
krps5_21 CLB  R3               
         LDBD R2,R32           
         DRP  !2
         RPS
         ADB  R2,=BIT#7
         DRP  !2
         RTN                   

APTACK   JSB  =HANDI0          
          VAL V.AACK
         JSB  =APSTAT
         DRP  !2
         RCY
         REZ
         ADB  R2,=BIT#7
         STBD R2,R32           
         TSB  R27              
         JPS  krps5_31
         JSB  =RPTADJ
krps5_31 CLM  R2               
         PUMD R32,+R6          
         LDM  R32,R30          
krps5_32 ADM  R32,R2           
         CMM  R32,R34          
         JZR  krps5_33
         JSB  =APSTAT
         DRP  !2
         JCY  krps5_32
         JEZ  krps5_32
         POMD R2,-R6           
         RTN                   

krps5_33 CLB  R32              
         STBD R32,=PSIOST      
         LDBD R32,=PSSTAT      
         JPS  krps5_34
         ADB  R32,=BIT#7
krps5_34 STBD R32,=PSSTAT      
         JSB  =ANN.A-          
         POMD R32,-R6          
         RTN                   

APTMRG   LDMD R40,=APFIL0      
         LDB  R14,=TYCOP?
         JSB  =FOPAC?          
         REN
         JNZ  krps5_43
         LDBD R20,X30,DR.TNM   
         CMB  R20,=TYNAPP
         JZR  krps5_41
         JSB  =ERROR           
          DATA 68D
         JMP  krps5_43
krps5_41 LDMD R50,=APFILE      
         JSB  =FRENAM          
         REZ
krps5_42 LDMD R40,=APFIL0      
         JSB  =AOPEN_
         CMM  R30,R34          
         JZR  krps5_43
         JSB  =APTGET
         JSB  =APDEL_
         JSB  =AOPEN
         JSB  =APTFND
         JSB  =DUPCHK
         JEN  krps5_42
         JSB  =APTINS
         JSB  =ATTN?           
         JEZ  krps5_42
krps5_43 LDMD R40,=APFIL0      
         JSB  =FPURGE          
         JSB  =BLIMP           
         RTN                   

APTRIG   JSB  =HANDI0          
          VAL V.ATRG
         JSB  =STOP?           
         REN
         JSB  =AONOF?
         ROD
         JSB  =NXTAPT
         JEN  krps5_53
         JSB  =GETCLK
         DRP  !42
         LDBD R42,R32           
         CMMD R42,R32           
         JNC  krps5_53
         LDB  R0,=60           
         ORB  R0,R27           
         STBD R0,X32,SIX
         JSB  =ANN.A+          
         LDBD R2,=PSSTAT       
         JNG  krps5_51
         ADB  R2,=BIT#7
         STBD R2,=PSSTAT       

krps5_51 ADB  R27,=BIT#6
         ADB  R27,=BIT#6
         JNC  krps5_52
         LDBD R26,=PSIOST      
         PUMD R26,+R6          
         JSB  =APTACK
         POMD R26,-R6          
         STBD R26,=PSIOST      
krps5_52 JSB  =ALBEEP
         JMP  APTRIG

krps5_53
STALRM   JSB  =AONOF?
         ROD
         JSB  =EVIL            
          DEF S27-57
         JSB  =NXTAPT
         REN
         ICM  R32              
         CLM  R40              
         LDMD R43,R32          
         LRM  R47              
         LRM  R47              
         SBMD R41,=TMBASE      
         JCY  STACMP
         CLM  R41              
         ICM  R41              
STACMP   LDB  R40,=7D          
         JSB  =CMPENT          
         RTN                   

AONOF?   LDBD R0,=PSSTAT       
         LRB  R0               
         LRB  R0               
         RTN                   

         DATA 241
ALARM.   BIN                   
         POBD R3,-R12          
         DCB  R3               
         LDBD R2,=PSSTAT       
         ANM  R2,=NOT#2,BIT#2
         ORB  R2,R3            
         STBD R2,=PSSTAT       
         JSB  =STALRM

OFALRM   CLM  R40              
         JMP  STACMP

CNTRIG   LDBD R27,=CNALRM      
         JZR  krps5_61
         JSB  =ALBEEP
         RTN                   

krps5_61 CLM  R40              
STCCMP   LDB  R40,=14D
         JSB  =CMPENT          
         RTN                   

GETCLK   LDMD R40,=RTCSB         
         CLM  R46              
         ADMD R41,=TMBASE      
         STM  R41,R61
         LLM  R42              
         LLM  R42              
         CLB  R42              
         DRP  !42
         RTN                   

GETTD    JSB  =GETCLK
         JSB  =DCCLOK
         RTN                   

MULT60   STM  R45,R55          
         BCD                   
         LLM  R45              
         BIN                   
         SBM  R45,R55          
         LLM  R45              
         LLM  R45              
         RTN                   

NXTAPT   JSB  =AOPEN
         REN
         ICE                   
         CLM  R2               
krps5_71 ADM  R32,R2           
         CMM  R32,R34          
         RZR
         JSB  =APSTAT
         JEN  krps5_71
         RTN                   

PRNOTE   JSB  =APTDSP
         CLB  R25              
         SBB  R24,=26D
         RZR
         STB  R24,R73          
         STM  R20,R22          
         LDM  R20,=INP+26      
         LDM  R74,R20          
         JSB  =KOPY            
         LDB  R25,=CR
         STBD R25,R76          
         LDB  R25,=APNOTE
         LDBD R2,=INPBUF       
         CMB  R2,='!'
         RZR
         LDB  R2,=BLANK
         STBD R2,=INPBUF       
         LDB  R25,=APCMND
         RTN                   
       TITLE 'krtmc'
S20-27 EQU 0F810H
S50-67 EQU 0F028H

*
*  __________________________________________________________________
* |KXTMC                                                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@  @@      @@     @@@@      ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@@    @@@   @@@@@@@@    ||
* ||   @@   @@@    @@@    @@@      @@      @@@@  @@@@  @@@    @@@   ||
* ||   @@  @@@      @@@  @@@       @@      @@@@@@@@@@  @@      @@   ||
* ||   @@ @@@         @@@@         @@      @@  @@  @@  @@           ||
* ||   @@@@@           @@          @@      @@  @@  @@  @@           ||
* ||   @@@@@           @@          @@      @@      @@  @@           ||
* ||   @@ @@@         @@@@         @@      @@      @@  @@           ||
* ||   @@  @@@      @@@  @@@       @@      @@      @@  @@      @@   ||
* ||   @@   @@@    @@@    @@@      @@      @@      @@  @@@    @@@   ||
* ||   @@    @@@   @@      @@      @@      @@      @@   @@@@@@@@    ||
* ||   @@     @@@  @@      @@      @@      @@      @@     @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820921.1421>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
STSMSG   DATA  32D               
         DATA  "Date: MDY, ~Time: AM, Appt: YEAR" 
STSPRT   DATA ((FILL1)-4).1
         DATA 11111100B,11111111B,11001111B,11110000B
ADJTMP   DATA 24D
         DATA 'Adjust (N)  + Hr+Mn+Sc.t'
ADJPRT   DATA ((FILL1)-3).1
         DATA 11111111B,01110100B,10010010B
CMDTBL   DATA 'EXACT'
         DEF  EXACT
         DATA 'ADJST'
         DEF  ADJUST
         DATA 'SET  '
         DEF  TMESET
         DATA 'STATS'
         DEF  STATUS
         DATA 'RESET'
TBLEND   DEF  RESET

CRTMDT   SAD
         JSB  =CRTMD_
         PAD
         RTN                   

CRTMD_   JSB  =EVIL
          DEF  S20-27
         JSB  =EVIL
          DEF  S50-67

         JSB  =GETTD
         CLB  R46
         JSB  =ENCLOK
         LDM  R54,R43          
         STM  R54,R44          
         RTN
GAP001   NOP

DTECNV   LDM  R60,R20          
         PUMD R60,+R6          
         LDM  R43,R44          
         CLB  R47              
         JSB  =DCCLOK            
         LDM  R65,R43          
         LDBD R64,=PSSTAT      
         LDB  R63,=20          
         ORB  R63,R64          
         STBD R63,=PSSTAT      
         JSB  =FXTIME            
         LDM  R72,R40          
         STBD R64,=PSSTAT      
         STM  R65,R45          
         JSB  =FXDATE
         POMD R60,-R6          
         STM  R60,R20          
         BIN                   
         RTN                   

TMECMD   CLB  R25              
         ADM  R24,=INPBUF      
         LDMD R43,=BLANKS      
         STMD R43,R24          
         LDMD R43,=INP+27      
         JSB  =UPRCSE
         IFNZ
           LDM  R20,=CMDTBL
           LOOP
             POMD R51,+R20         
             CMM  R43,R51          
             JZR  TBSEND
             CMM  R20,=TBLEND
           WHNC
           JSB  =HANDI           
             DATA V.TMCX,78D
           LDB  R24,=32D          
           JMP  TMCEND

TBSEND     JSB  =TCKTGL
           JSB  X56,ZRO          
           JSB  =TCKTGL
         ENDIF
         LDB  R24,=27D
         JSB  =BLIMP           

TMCEND   STBD R#,=GINTDS       
         LDB  R30,=C/SFLG
         LDBD R31,=CMPFLG      
         ORB  R31,R30          
         STBD R31,=CMPFLG      
         LDB  R2,=80H
         JSB  =SVCSET          
         RTN                   

TCKTGL   LDB  R30,=DSPTGL
         LDBD R31,=PSSTAT      
         XRB  R31,R30          
         STBD R31,=PSSTAT      
         RTN                   

STATUS   LDM  R20,=STSMSG      
         LDM  R22,=INPBUF      
         JSB  =MVBYTS          
         LDBD R3,=PSSTAT       
         STB  R3,R31           
         ELB  R3               
         ELB  R3               
         IFCY
           LDM  R44,='EXTD'
           STMD R44,=INP+28      
         ENDIF
         ELB  R3               
         IFCY
           LDM  R46,='DM'
           STMD R46,=INP+6       
         ENDIF
         ELB  R3               
         IFCY
           LDM  R46,='**'
           STMD R46,=INP+18      
         ENDIF
         ELB  R3               
         ELB  R3               
         ELB  R3               
         IFCY
           LDB  R47,='*'
           STBD R47,=INP+11      
         ENDIF
         LDM  R24,=(32D).2
         LDM  R22,=INP+6       

STSINP   LDM  R20,=INPBUF      
         LDM  R44,=(TINCHK).2,(STSPRT).2
         JSB  =GETTEM          
         JZR  STATUS
         RNG
         LDB  R30,=(EXTON).2
         LDM  R22,=INP+28      
         LDMD R44,R22          
         JSB  =UPRCSE
         IFNZ
           CMM  R44,='YEAR'
           IFZR
             ANM  R31,=(EXTOFF).1
           ELSE
             CMM  R44,='EXTD'
             JNZ  INPERR
             ORB  R31,R30
           ENDIF
         ENDIF
         LRB  R30              
         LDM  R22,=INP+6       
         LDMD R46,R22          
         JSB  =UPRCSE
         IFNZ
           CMM  R46,='MD'
           IFZR
             ANM  R31,=DMYOFF
           ELSE
             CMM  R46,='DM'
             JNZ  INPERR
             ORB  R31,R30          
           ENDIF
         ENDIF

         LRB  R30              
         LDM  R22,=INP+18      
         LDMD R46,R22          
         JSB  =UPRCSE
         IFNZ
           CMM  R46,='AM'
           JZR  SETAM
           CMM  R46,='PM'
           IFZR
SETAM        ANM  R31,=(H24OFF).1
           ELSE
             CMM  R46,='**'
             IFZR
               ORB  R31,R30          
             ELSE
INPERR         JSB  =ERROR           
                DATA 89D
               GTO STSINP
             ENDIF
           ENDIF
         ENDIF
         STBD R31,=PSSTAT      
         RTN                   

TMESET   JSB  =TTMPLT
INPTME   LDM  R44,=(TINCHK).2,(STMMSK).2
         JSB  =GETTEM          
         JZR  TMESET
         RNG
         PUBD R24,+R6          
         LDMD R70,=RTC         
         CLM  R76              
         PUMD R71,+R6          
         ADMD R71,=TMBASE      
         LLM  R71              
         LLM  R71              
         CLB  R71              
         CLB  R72              
         ICM  R73              
         LDMD R40,=INP+4       
         LDM  R42,R43          
         LDMD R44,=INP+10      
         CMM  R44,='Year'
         IFZR
           LDM  R44,='YYYr'
         ENDIF
         JSB  =DATCK_
         JEN  SETERR
         CLM  R60              
         STM  R44,R63          
         LDMD R40,=INP+15      
         LDMD R46,=INP+24      
         JSB  =TIMCHK
         JEN  SETERR
         STM  R45,R60          
         LDM  R41,R71          
         JSB  =DCCLOK            
         STB  R40,R32          
         STM  R60,R50          
         LDM  R60,R40          
         LDM  R0,=56,6
         LOOP
           CMB  R*,=DEFALT
           IFZR
             ARP  R*
             ADB  R0,=10           
             STB  R*,R#            
             SBB  R0,=10           
           ENDIF
           SBM  R0,=1,1
         WHPS
         CLM  R20              
         CLM  R60              
         ICB  R63              
         ICB  R64              
         LDMD R70,=MAXDAT
         JSB  =FNDTD_
         JEN  SETERR             
         LDMD R20,=INP+21      
         CMM  R20,='Sc'
         JZR  DEFASC
         CMMD R20,=BLANKS      
         IFZR
DEFASC     LDB  R21,R32          
         ELSE
           JSB  =NUMCHK          
           JEN  SETERR             
           CMB  R21,=60C
           IFCY
SETERR       POMD R51,-R6          
             JSB  =ERROR           
              DATA 89D
             LDM  R20,=INPBUF      
             LDM  R22,=INP+4       
             POBD R24,-R6          
             GTO INPTME
           ENDIF
         ENDIF
         STB  R21,R20           
         JSB  =TOBIN2          
         CLM  R53              
         LDB  R53,R20          
         ADM  R43,R53          
         CLM  R65              
         STM  R65,R40          
         LRM  R47              
         LRM  R47              
         POMD R51,-R6          
         SBM  R41,R51          
         LDMD R51,=TMBASE      
         STMD R41,=TMBASE      
         SBM  R41,R51          
         LDB  R21,='N'
         JSB  =MKEADJ
         POBD R24,-R6          
         RTN                   

EXACT    LDMD R50,=RTC         
         CLM  R56              
         LDMD R41,=TMBASE      
         SBMD R41,=TMEADJ      
         ADM  R41,R51          
         LDBD R31,=PSSTAT      
         ANM  R31,=DXOFF
         ADB  R31,=XCTON
         LDMD R61,=TMEXCT      
         STMD R41,=TMEXCT      
         SBM  R41,R61          
         JNG  XCTERR
         LDMD R51,=TMEERR      
         IFZR
           CLM  R61              
         ELSE
           SBM  R41,R51          
           JNG  XCTERR
           TSM  R51              
           IFNG
             TCM  R51              
             ADB  R31,=DECON
           ENDIF
           CLM  R61              
           ICB  R61              
           CLM  R71              
           BCD                   
           LLM  R41              
           LLM  R41              
           LLM  R41              
           BIN                   
           JMP  SZEFND
           LOOP
             LLM  R51              
             LLM  R61              
             JCY  XCTERR
SZEFND       CMM  R51,R41          
           WHNC

           LOOP
             CMM  R41,R51          
             IFCY
               SBM  R41,R51          
               ADM  R71,R61          
             ENDIF
             LRM  R57              
             LRM  R67              
             TSM  R61              
           WHNZ
     
           LDM  R61,R71          
           IFZR
XCTERR       JSB  =WARN            
             DATA 70D
             RTN                   
           ENDIF
         ENDIF

         JSB  =SETCMP
         STBD R31,=PSSTAT      
         RTN                   

ADJUST   LDM  R20,=ADJTMP
         LDM  R22,=INPBUF      
         JSB  =MVBYTS          
         LDM  R22,=INP+12      
ADJINP   LDM  R20,=INPBUF      
         LDB  R24,=24D
         LDM  R44,=(TINCHK).2,(ADJPRT).2
         JSB  =GETTEM          
         JZR  ADJUST
         RNG
         CLM  R40              
         LDM  R22,=INP+14      
         LDMD R20,R22          
         CMM  R20,='Hr'
         IFNZ
           CMMD R20,=BLANKS      
           IFNZ
             JSB  =NUMCHK          
             JEN  ADJERR             
             STB  R21,R42          
           ENDIF
         ENDIF
         LDM  R22,=INP+17      
         LDMD R20,R22          
         CMM  R20,='Mn'
         IFNZ
           CMMD R20,=BLANKS      
           IFNZ
             JSB  =NUMCHK          
             JEN  ADJERR             
             STB  R21,R41          
           ENDIF
         ENDIF
         LDB  R43,=1           
         LDB  R44,=1           
         JSB  =ENCLOK
         LDM  R22,=INP+20      
         LDMD R20,R22          
         CMM  R20,='Sc'
         IFNZ
           CMMD R20,=BLANKS      
           IFNZ
             JSB  =NUMCHK          
             IFEN
ADJERR         JSB  =ERROR           
               DATA 89D
               JMP  ADJINP
             ENDIF
             STB  R21,R20          
             JSB  =TOBIN2          
             CLM  R53              
             STB  R20,R53          
             ADM  R43,R53          
           ENDIF
         ENDIF
 
         LRM  R47              
         LRM  R47              
         LDM  R22,=INP+23      
         LDBD R21,R22          
         CMB  R21,='t'
         IFNZ
           CMB  R21,=' '
           IFNZ
             LDB  R20,='0'
             JSB  =NUMCHK          
             JEN  ADJERR             
             STB  R21,R20          
             JSB  =TOBIN2          
             LOOP
               DCB  R20              
               JNG  GETSGN
               ADM  R41,=66H,6H,0,0,0,0,0 
             WHMP
           ENDIF
         ENDIF

GETSGN   LDM  R22,=INP+12      
         LDBD R20,R22          
         CMB  R20,='+'
         IFNZ
           CMB  R20,='-'          
           JNZ  ADJERR             
           TCM  R41              
         ENDIF

         LDM  R22,=INP+8       
         LDBD R21,R22          
         ANM  R21,=NOT#5
         CMB  R21,='N'
         IFNZ
           CMB  R21,='A'
           JNZ  ADJERR             
         ENDIF
         LDMD R51,=TMBASE      
         ADM  R51,R41          
         IFNG
           CLM  R51              
         ENDIF
         STMD R51,=TMBASE      

MKEADJ   JSB  =ERRADJ
         JSB  =STALRM
         JSB  =TICK
         RTN                   

STRTME   CLM  R62              
         LDB  R62,=CLRCLK
         STMD R62,=RTC         
         JMP  CLRRST

RESET    LDBD R67,=PSSTAT      
         ANM  R67,=XCTOFF
         STBD R67,=PSSTAT      

CLRRST   CLM  R61              
         STMD R61,=TMEXCT      
         STMD R61,=TMEERR      
         STMD R61,=TMEADJ      

SETCMP   CLM  R71              
         LDB  R72,=ADJLIM
         STM  R61,R41          
         IFNZ
           CMM  R61,R71          
           IFNC
             LDM  R41,R71          
           ENDIF
         ENDIF
         LDB  R40,=CT.ADJ
         JSB  =CMPENT          
         RTN                   

ERRADJ   LDBD R31,=PSSTAT      
         ANM  R31,=XCTFLG
         JZR  CLRRST
         STM  R41,R61          
         CMB  R21,='N'
         IFZR
           CLM  R61              
           TSM  R41              
           IFNG
             TCM  R41              
             CLB  R31              
           ENDIF
           LDM  R50,=0,0,0,0,0,0,20H,1CH 
           LDB  R34,=28D
SPRTLP     LOOP
             DCB  R#
             LRM  R57              
             CMM  R41,R51          
             IFCY
               SBM  R41,R51          
               ADM  R61,R51          
               TSB  R34              
               JPS  SPRTLP
               SBM  R41,R51          
               ADM  R61,R51          
             ENDIF
             TSB  R34              
           WHPS
           TSB  R31              

           IFZR
             TCM  R41              
             TCM  R61              
           ENDIF
           ADMD R41,=TMEERR      
           STMD R41,=TMEERR      
         ENDIF
         ADMD R61,=TMEADJ      
         STMD R61,=TMEADJ      
         RTN                   

UPRCSE   SAD                   
         LDMD R70,=BLANKS      
         PAD                   
         SAD                   
         STM  R#,R70           

         LOOP
           CMB  R70,=' '
           JNZ  NOBLNK
           BCD                   
           LRM  R77              
           LRM  R77              
           BIN                   
         WHMP

NOBLNK   LDM  R0,=70,370
         JSB  =UPRC*           
         PAD                   
         LDM  R#,R70           
         CLE                   
         RTN                   
       TITLE 'krloc'
*
*  __________________________________________________________________
* |KRLOK 268 06/24/82 - 7/ 9/1982 8:51AM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@            @@@@@@    @@     @@@   ||
* ||   @@    @@@   @@@@@@@@@   @@           @@@@@@@@   @@    @@@    ||
* ||   @@   @@@    @@     @@@  @@          @@@    @@@  @@   @@@     ||
* ||   @@  @@@     @@      @@  @@          @@      @@  @@  @@@      ||
* ||   @@ @@@      @@     @@   @@          @@      @@  @@ @@@       ||
* ||   @@@@@       @@@@@@@     @@          @@      @@  @@@@@        ||
* ||   @@@@@       @@@@@@@     @@          @@      @@  @@@@@        ||
* ||   @@ @@@      @@    @@@   @@          @@      @@  @@ @@@       ||
* ||   @@  @@@     @@     @@@  @@          @@      @@  @@  @@@      ||
* ||   @@   @@@    @@      @@  @@          @@@    @@@  @@   @@@     ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@   @@@@@@@@   @@    @@@    ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@    @@@@@@    @@     @@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1356>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
PROMPT   DATA 10D              
         DATA "password? "     
         DATA 241              
LOCK.    DRP  R0               
         JSB  =GETAD#          
         LDMD R60,R0           
         POMD R0,-R12          
         JSB  =CLGRBG
         STMD R60,=LOKPSW      
         JSB  =BLIMP           
         RTN                   

         LDMD R70,=LOKPSW      
         RZR
         LDM  R26,=PROMPT      
         JSB  =HLFOUT          
         JSB  =GET.IN          
         CMB  R25,=CR
         IFEQ
           LDB  R25,=EDITKY
         ENDIF
         LDMD R60,=INPBUF      
         LDB  R0,R24           
         JSB  =CLGRBG
         CMM  R60,R70          
         RTN                   

CLGRBG   CMB  R0,=8D
         IFNC
           ADB  R0,=60           
           CLM  R*               
         ENDIF
         RTN                   
       TITLE 'krang'
*
*  __________________________________________________________________
* |IVANG 48 05/10/82 - 5/13/1982 2:53PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@    @@@@@@    @@      @@     @@@@      ||
* ||   @@@@@@@@@@  @@      @@   @@@@@@@@   @@      @@   @@@@@@@@    ||
* ||       @@      @@      @@  @@@    @@@  @@@     @@  @@@    @@@   ||
* ||       @@      @@      @@  @@      @@  @@@@    @@  @@      @@   ||
* ||       @@       @@    @@   @@      @@  @@ @@   @@  @@           ||
* ||       @@       @@    @@   @@@@@@@@@@  @@  @@  @@  @@           ||
* ||       @@       @@    @@   @@@@@@@@@@  @@  @@  @@  @@   @@@@@   ||
* ||       @@        @@  @@    @@      @@  @@   @@ @@  @@   @@@@@   ||
* ||       @@         @@@@     @@      @@  @@    @@@@  @@      @@   ||
* ||       @@         @@@@     @@      @@  @@     @@@  @@@    @@@   ||
* ||   @@@@@@@@@@      @@      @@      @@  @@      @@   @@@@@@@@    ||
* ||   @@@@@@@@@@      @@      @@      @@  @@      @@     @@@@      ||
* ||                                                                ||
* ||                  Last edited on <820908.1333>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
         DATA  241              
DEG.     LDB  R#,=90C
         DRP  R77

         DATA  241
RAD.     CLB  R#              
         STBD R20,=DRG         
         RTN                   
       TITLE 'krini'
*
*  __________________________________________________________________
* |IVINI 232 05/10/82 - 5/13/1982 3:33PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||       @@      @@      @@      @@      @@@     @@      @@       ||
* ||       @@      @@      @@      @@      @@@@    @@      @@       ||
* ||       @@       @@    @@       @@      @@ @@   @@      @@       ||
* ||       @@       @@    @@       @@      @@  @@  @@      @@       ||
* ||       @@       @@    @@       @@      @@  @@  @@      @@       ||
* ||       @@        @@  @@        @@      @@   @@ @@      @@       ||
* ||       @@         @@@@         @@      @@    @@@@      @@       ||
* ||       @@         @@@@         @@      @@     @@@      @@       ||
* ||   @@@@@@@@@@      @@      @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@@@@@@@@@      @@      @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1352>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
CLRINT   JSB  =SET             
         VAL  RTN              
         DEF  INTBGN           
         DEF  (INTEND)-1
         RTN                   

START?   LDBD R3,=PSSB         
         ANM  R3,=BIT#2
         IFNZ
           LDMD R70,=TMPMM2      
           STM  R70,R6           
           STM  R14,R16          
           RTN                   
         ENDIF

START    LDB  R6,=31H
         STBD R6,=PSSB         
         LDM  R6,=STACK        
         CLM  R40              
         STM  R40,R10          
SYSINI   BIN                   
         JSB  =BOUND           
         LDM  R36,=R6LIM1      
         LDM  R56,R34          
         JSB  =Z36.56          
         STMD R34,=LWAMEM      
         CLB  R34              
         STBD R34,=CMPSB       
         JSB  =ROMSET          
         JSB  =STRTME
         JSB  =CMPSET          
         JSB  =CMPENA          
         LDB  R2,=1            
         STBD R2,=CRDSTS       
         STBD R2,=BEEPOK       
         STBD R2,=DEFAUL       
         ICB  R2               
         STBD R2,=KEYSTS       
         LDM  R2,=CRDSIZ       
         STMD R2,=FULTRK       

TONY     EQU  32D

         LDB  R2,=TONY
         STBD R2,=DISPLN       
         STBD R2,=PRNTLN       
         JSB  =CLRINT          
         LDM  R2,=RETURN       
         STMD R2,=INPCHK       
         STBD R2,=DEAD         
         LDM  R2,=(91D).2
         STMD R2,=RMARG        
         LDM  R44,=80D,49D,32D,0 
         STMD R44,=MINMIN      
         JSB  =NULOLD          
         JSB  =LCDRST
         CLM  R43              
         STMD R43,=CRDRDR      
         LDB  R44,=20H
         STMD R43,=DELAY       
         JSB  =C.INIT          
         JSB  =INITGL
         JSB  =RNDINI          
         JSB  =S.OFF           
         JSB  =B.INIT          
         JSB  =UPSET           
         JSB  =FLINIT          
         JSB  =HANDI0          
         VAL  V.COLD
         JSB  =TMESET
         JSB  =SETCAL          
         LDM  R20,=TYBASC      
         LDMD R40,=DFNAME      
         JSB  =SETED           
         JSB  =SETRN           
         LDMD R40,=IOFILE      
         JSB  =MAKEIT          
         CLM  R60              
         CLM  R76              
         JSB  =IOOPEN          
         LDM  R2,=4H,0FFH
         JSB  =SETPSB          
         LDB  R25,=TIMEKY
         GTO MODEKY            
       TITLE 'kred'
S41-47 EQU 0F921H
S40-47 EQU 0F820H
S30-31 EQU 0FE18H
S20-25 EQU 0FA10H
*
*  __________________________________________________________________
* |KXED 144 09/27/82 - 11/ 3/1982 1:20PM                             |
* |==================================================================|
* ||                                                                ||
* ||         @@     @@@  @@      @@  @@@@@@@@@@  @@@@@@             ||
* ||         @@    @@@   @@      @@  @@@@@@@@@@  @@@@@@@@           ||
* ||         @@   @@@    @@@    @@@  @@          @@    @@@          ||
* ||         @@  @@@      @@@  @@@   @@          @@      @@         ||
* ||         @@ @@@         @@@@     @@          @@      @@         ||
* ||         @@@@@           @@      @@@@@@@@@   @@      @@         ||
* ||         @@@@@           @@      @@@@@@@@@   @@      @@         ||
* ||         @@ @@@         @@@@     @@          @@      @@         ||
* ||         @@  @@@      @@@  @@@   @@          @@      @@         ||
* ||         @@   @@@    @@@    @@@  @@          @@    @@@          ||
* ||         @@    @@@   @@      @@  @@@@@@@@@@  @@@@@@@@           ||
* ||         @@     @@@  @@      @@  @@@@@@@@@@  @@@@@@             ||
* ||                                                                ||
* ||                  Last edited on <821103.1318>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
CHEDIT   JSB  =EVIL            
         DEF  S41-47
         CLE                   
         LDMD R46,=INPCHK      
         JSB  X46,ZRO          
         JEN  ISTERM
         JSB  =HANDI0          
         VAL  V.CHED
         JSB  =LIT?            
         JNG  NORMAL           
         JSB  =TYPAID
         RNZ
CHED__   JSB  =LIT?            
         JOD  NORMAL
         JSB  =SPECKY
         REZ
         JSB  =TERMKY
         IFEN
           TSB  R40              
           IFPS
NORMAL       JSB  =PUTCHR
           ENDIF
           CLE                   
           RTN                   
         ENDIF
ISTERM   JSB  =KEYTRM          

         LDB  R47,=CR
         STBD R47,=CRSPOT      
         JSB  =SHELD?
         DRP  !2
         IFEN
           LDMD R2,=LASTCH       
           ICM  R2               
           STBD R47,R2           
         ENDIF
         JSB  =I/ROFF
         JSB  =EOLND           
         JSB  =UNSEE           
         STE
         RTN                   

CHED_    JSB  =EVIL            
         DEF  S40-47
         JMP  CHED__

TYPAID   PUMD R36,+R6
         PUMD R30,+R6
         PUMD R20,+R6
         LDB  R20,R40
         CMB  R20,=NAPKEY
         IFEQ
           JSB  =PWROK?
           JEN  FAIL
         ENDIF

         JSB  =TOBCD2          
         JSB  =KYOPEN          
         JEN  FAIL
         PUMD R76,+R6          
         LDM  R76,R20          
         JSB  =FSEEK           
         POMD R76,-R6          
         JEN  FAIL
         POMD R44,+R36         
         TSB  R46              
         JZR  SUCESS

LOOP     DCB  R46              
         JZR  kred_1
         POBD R40,+R36         
         JSB  =CHED_
         JEN  SUCESS
         JMP  LOOP

kred_1   CMB  R47,=';'
         JZR  SUCESS
         LDB  R40,=CR
         JSB  =CHED_

SUCESS   LDB  R2,=1            
         JMP  EXIT
FAIL     CLB  R2               
EXIT     POMD R20,-R6          
         POMD R30,-R6          
         POMD R36,-R6          
         TSB  R2               
         RTN                   

PUTCHR   LDM  R2,=((INPBUF)-1).2     
         ADMD R2,=RMARG        
         CMMD R2,=INPTR        
         IFEQ
           JSB  =STBEEP          
         ENDIF
         LDBD R46,=I/RFLG      
         JNZ  INSPUT
         LDMD R46,=LCDPTR      
         CMM  R46,=((LCDBUF)+95D).2
         JCY  NOGOOD

         LDMD R46,=INPTR       
         CMM  R46,=((INPBUF)+95D).2
         JCY  NOGOOD

         CMMD R46,=LASTCH      
         IFHS
           STMD R46,=LASTCH      
         ENDIF
         PUBD R40,+R46         
         STMD R46,=INPTR       
         JSB  =OUTC40          
         JSB  =RHTBND
         DRP  !2
         CMMD R2,=INPTR        
         IFLO
           JSB  =LEFT1
         ENDIF
         JMP GTORSL

NOGOOD   GTO STBEEP            

INSPUT   JSB  =EVIL            
         DEF  S30-31
         LDMD R30,=LASTCH
         JSB  =NXTWAL
         DRP  !2
         CMMD R2,=LASTCH       
         IFHS
           ICM  R30              
         ENDIF
         STM  R#,R46          
         JSB  =RHTBND
         DRP  !2
         DCM  R2               
         DCM  R2               
         CMM  R2,R46           
         JNC  NOGOOD
         STMD R46,=LASTCH      
         LDMD R46,=INPTR       
         ICM  R46              
         STMD R46,=INPTR       
         DCM  R46              
         STB  R40,R41          
kred_2   LDBD R2,R46           
         PUBD R41,+R46         
         LDB  R41,R2           
         CMMD R46,=LASTCH      
         JLO  kred_2
         JEQ  kred_2

         JSB  =OUTC40          
         STMD R30,=LASTCH      
GTORSL   GTO  RSLIP

SPECKY   CMB  R40,=CLRKEY
         IFEQ
           JSB  =SHELD?
           IFEZ
             ICE                   
             RTN                   
           ENDIF
         ENDIF
         DRP  R40              
         JSB  =LOOKUP          
         DEF SPECTB
         REN
         JSB  X0,ZRO           
         CLE                   
         RTN                   

SPECTB   VAL ((UPKEY)+(CNTL)).1
         DEF MOVEUP
         VAL ((DOWNKY)+(CNTL)).1
         DEF MOVEDN
         VAL LEFT!
         DEF LEFT1
         VAL LEFTKY
         DEF LA
         VAL ((LEFTKY)+(SHIFT)).1
         DEF SHLA
         VAL ((LEFTKY)+(CNTL)).1
         DEF BAKSEG
         VAL RGHTKY
         DEF RA
         VAL ((RGHTKY)+(SHIFT)).1
         DEF SHRA
         VAL ((RGHTKY)+(CNTL)).1
         DEF FWDSEG
         VAL I/RKEY
         DEF I/R
         VAL ((FTCHKY)+(SHIFT)).1
         DEF SHFET
         VAL ((FTCHKY)+(CNTL)).1
         DEF EDITIN
         VAL DELKEY
         DEF DEL
         VAL ((DELKEY)+(SHIFT)).1
         DEF SHDEL
         VAL CLRKEY
         DEF CLR
         VAL LOCKKY
         DEF LOCK
         VAL ((LOCKKY)+(SHIFT)).1
         DEF LOCK
         VAL ((LOCKKY)+(CNTL)).1
         DEF LOCK
         VAL BS
         DEF BACKSP
         VAL TABKEY
         DEF TAB
         VAL ((TABKEY)+(SHIFT)).1
         DEF UNTAB
         VAL LITKEY
         DEF SETJS
         VAL BEEPKY
         DEF STBEEP
         DATA 0

TERMKY   DRP  R40              
         JSB  =SEARCH          
         DEF  TERMTB
         RTN                   

TERMTB   VAL ATTNKY
         VAL TIMEKY
         VAL ((TIMEKY)+(SHIFT)).1
         VAL APPTKY
         VAL ((APPTKY)+(SHIFT)).1
         VAL EDITKY
         VAL UPKEY
         VAL ((UPKEY)+(SHIFT)).1
         VAL DOWNKY
         VAL ((DOWNKY)+(SHIFT)).1
         VAL CLRKEY
         VAL FTCHKY
         VAL CR
         VAL RUNKEY
         VAL STEPKY
         VAL NAPKEY
         VAL BYEKEY
         DATA 0

LOCK     SBB  R40,=214         
         TSB  R40              
         ELB  R40              
         ELB  R40              
         ELB  R40              
         ELB  R40              
         STBD R40,=CAPLOK      
         RTN                   

EDITIN
         JSB  =SHELD?
         REZ
         
         JSB  =EVIL            
         DEF  S20-25

         LDM  R20,=INPBUF
         LDMD R22,=INPTR       
         LDMD R24,=LASTCH      
         CMMD R24,=OLDLST      
         IFLO
           LDMD R24,=OLDLST      
         ENDIF
         ICM  R24              
         SBM  R24,R20          
         RZR
         JSB  =I/ROFF
         JSB  =KEYTRM          
         JSB  =EOLND           
         JSB  =SETLIN          
         RTN                   
GAP03C   NOP
         NOP

I/R      LDBD R#,=I/RFLG       
         NCB  R#               
         JMP  SETI/R

I/ROFF   CLB  R2               
SETI/R   STBD R#,=I/RFLG       
         IFZR
           JSB  =OUTESC          
           DATA 'R'
         ELSE
           JSB  =OUTESC          
           DATA 'Q'
         ENDIF
         JSB  =CURSE?          
         RTN                   

CLR      JSB  =SHLA
         JSB  =OUTESC          
         DATA 'J'
         JSB  =ANN.E-          
         LDM  R2,=INPBUF       
         STMD R2,=INPTR        
         DCM  R2               
         STMD R2,=LASTCH       
         JMP  I/ROFF

BACKSP   LDMD R2,=INPTR        
         PUMD R2,+R6           
         JSB  =LA
         DRP  !2
         POMD R2,-R6           
         CLE                   
         CMMD R2,=INPTR        
         REQ
         LDBD R40,=I/RFLG      
         JNZ  DEL
         LDB  R40,=BLANK
         JSB  =PUTCHR
         JSB  =LA
         DRP  !2
         LDMD R2,=INPTR        
         CMMD R2,=LASTCH       
         IFEQ
           DCM  R2               
           STMD R2,=LASTCH       
         ENDIF
         JMP  RTN_E1

DEL      LDMD  R44,=LASTCH      
         JSB  =NXTWAL
         DRP  !2
         CMM  R2,R44           
         IFHS
           LDM  R2,R44           
           DCM  R2               
           STM  R2,R44           
           ICM  R2               
         ENDIF
         CLE                   
         CMMD R2,=INPTR        
         RLO
         LDMD R46,=INPTR       

DELLUP   CMM  R2,R46           
         IFHS
           POBD R40,+R46         
           LDBD R40,R46          
           PUBD R40,-R46         
           POBD R40,+R46         
           JMP  DELLUP
         ENDIF
         LDB  R2,=BLANK
         PUBD R2,-R46         
         STMD R46,=LASTCH      
         JSB  =OUTESC          
         DATA 'P'
         LDM  R2,R44           
         STMD R2,=LASTCH       
RTN_E1   STE                   
         RTN                   

UNTAB    JSB  =LFTBND
         DRP !2
         CMMD R2,=INPTR        
         RHS
         JSB  =LEFT1
         JSB  =LSLIP
GOLEFT   DRP !2
         LDMD R2,=INPTR        
         CMM  R2,=INPBUF       
         REQ
         DCM  R2               
         JSB  =R2OK?
         REZ
         JSB  =LEFT1
         JMP  GOLEFT

TAB      JSB  =NXTWAL
         REN
         LOOP
           DRP !2
           ICM  R2               
           CMM  R2,=((INPBUF)+96D).2
           RHS
           JSB =R2OK?
         WHEZ

GOTAB    JSB  =LEGAL?
         IFEZ
           GTO RSLIP
         ENDIF
         JSB  =RIGHT1
         JMP  GOTAB

FWDSEG   LDBD R41,=SIZSIZ      
         LOOP
           JSB  =RA
           REZ
           DCB  R41              
         WHNZ
         RTN                   

BAKSEG   JSB  =IO.OFF          
         LDBD R41,=SIZSIZ      
         LOOP
           JSB  =LA
           JEZ  kred_3
           DCB  R41              
         WHNZ
kred_3   GTO IO.ON             

SETJS    LDB  R#,=FF
         STBD R#,=JUSTSO
         RTN

LA       JSB  =LFTBND
         DRP  !2
         CLE                   
         CMMD R2,=INPTR        
         IFLO
           JSB  =LEFT1
           JSB  =LSLIP
           ICE                   
           RTN                   
         ENDIF
         LDMD R2,=LCDWIN       
         CMM  R2,=((LCDBUF)+1).2
         RLO
         DCM  R2               
         STMD R2,=LCDWIN       
         JSB  =PUTWIN          
         JMP  RTN.E1

LEFT1    JSB  =OUT1CH          
         DATA BS
         LDMD R2,=INPTR        
         DCM  R2               
         JMP  STORIN
GAP01A   NOP

RA       CLE                   
         LDMD R2,=INPTR        
         DCM  R2               
         CMMD R2,=LASTCH       
         RHS
         JSB  =RHTBND
         DRP  !2
         CLE                   
         CMMD R2,=INPTR        
         REQ
         JSB  =RIGHT1
         JSB  =RSLIP
RTN.E1   STE
         DRP  R2
         RTN                   

RIGHT1   JSB  =OUTESC          
         DATA 'C'
         LDMD R2,=INPTR        
         ICM  R2               
STORIN   CMM  R#,=INPBUF       
         IFLO
           LDM  R#,=INPBUF       
         ENDIF
         CMM  R#,=((INPBUF)+(BUFLEN)).2
         IFHS
           LDM  R#,=((INPBUF)+(BUFLEN)-1).2
         ENDIF
         STMD R#,=INPTR        
         RTN                   

RSLIP    JSB  =LEGAL?
         REN
         JSB  =RIGHT1
         JMP  RSLIP

LSLIP    JSB  =LEGAL?
         REN
         JSB  =LEFT1
         JMP  LSLIP

MOVEUP   JSB  =OUTESC          
         DATA 'S'
         RTN                   

MOVEDN   JSB  =OUTESC          
         DATA 'T'
         RTN                   

RHTBND   LDM  R2,=((INPBUF)+(BUFLEN)-1).2
kred_4   JSB  =R2OK?
         DRP  !2
         JEN  PHASE2
         CMM  R2,=INPBUF       
         REQ
         DCM  R2               
         JMP  kred_4
PHASE2   DRP  !2
         CMM  R2,=((INPBUF)+1).2
         RLO
         LDMD R0,=INPTR        
         SBMD R0,=LCDPTR       
         ADM  R0,=((LCDBUF)+96D).2
         CMM  R0,R2            
         IFLO
           STM  R0,R2            
         ENDIF
         DRP  R2
         RTN                   

LFTBND   LDM  R2,=INPBUF       
kred_5   JSB  =R2OK?
         DRP  !2
         REN
         CMM  R2,=((INPBUF)+(BUFLEN)-1).2
         REQ
         ICM  R2               
         JMP  kred_5

LEGAL?   LDMD R2,=INPTR        
R2OK?    PUMD R2,+R6           
         PUMD R30,+R6          
         LDM  R30,R2           
         SBM  R30,=INPBUF      
         LDM  R0,R30           
         ANM  R0,=111B,0
         LRM  R30              
         LRM  R30              
         LRM  R30              
         LDBD R30,X30,SHIELD   
kred_11  TSM  R0               
         JZR  kred_12
         DCM  R0               
         LLB  R30              
         JMP  kred_11
kred_12  CLE                   
         TSB  R30              
         IFPS
           ICE                   
         ENDIF
         POMD R30,-R6          
         POMD R2,-R6           
         RTN                   
GAP2B    NOP
         NOP

SHELD?   LDM  R2,=INPBUF       
         JMP  CRUISE

NXTWAL   LDMD R2,=INPTR        

CRUISE   LOOP
           JSB  =R2OK?
           JEZ  AWALL
           DRP  !2
           CMM  R2,=((INPBUF)+(BUFLEN)-1).2
           RHS
           ICM  R2               
         WHMP

AWALL    DRP  !2
         DCM  R2               
         RTN                   

SHDEL    JSB  =NXTWAL
         JEZ  kred_21
         JSB  =OUTESC          
         DATA 'J'
         LDMD R2,=INPTR        
         DCM  R2               
         STMD R2,=LASTCH       
         RTN                   

kred_21  JSB  =IO.OFF          
         LDMD R44,=LCDPTR      
         PUMD R44,+R6          
         LDBD R43,=I/RFLG      
         CLB  R2               
         JSB  =SETI/R
         LDMD R2,=INPTR        
         STM  R2,R41           
         LOOP
           LDMD R46,=INPTR       
           CMMD R46,=LASTCH      
           IFNE
             JHS  BCK.UP
           ENDIF
           LDB  R40,=BLANK
           JSB  =CHEDIT          
           CMMD R46,=INPTR       
         WHNE

BCK.UP   
         LDM  R46,R41          
kred_22  CMMD R46,=INPTR       
         JZR  kred_23
         LDB  R40,=LEFTKY
         JSB  =CHEDIT          
         JMP  kred_22

kred_23  DRP  R43              
         JSB  =SETI/R
         POMD R44,-R6          
         STMD R44,=LCDPTR      
         JMP  IO.ON_

SHLA     JSB  =IO.OFF          
         LOOP
           JSB  =LA
         WHEN
         JSB  =DECURS          
         JSB  =IO.ON           
         JSB  =LETBD           
         RTN                   

SHRA     JSB  =IO.OFF          
         LOOP
           JSB  =RA
         WHEN
IO.ON_   GTO  IO.ON

GAP02D   NOP
         NOP

         VAL  PGMRSW
MARGN.
         JSB  =ONEB            
         STMD R46,=RMARG       
         RTN                   

SHFET    LDM  R46,=ERRBUF      
         STM  R46,R44          
         LDBD R46,=MINMIN      
         LOOP
           POBD R47,+R44         
           DRP  R46              
           JSB  =TOLCD           
           DRP  !46
           DCB  R46               
           CMBD R46,=MAXMAX       
         WHCY
         JSB  =ANNUNS          
         LDBD R40,=CURSOR      
         JSB  =DECURS          
         JSB  =LETGO
         STBD R40,=CURSOR      
         GTO PUTWIN            
       TITLE 'krmpy'
*
*  __________________________________________________________________
* |KRMPY 292 07/19/82 - 7/27/1982 5:59PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@      @@  @@@@@@@@    @@      @@   ||
* ||   @@    @@@   @@@@@@@@@   @@@    @@@  @@@@@@@@@   @@      @@   ||
* ||   @@   @@@    @@     @@@  @@@@  @@@@  @@     @@@  @@      @@   ||
* ||   @@  @@@     @@      @@  @@@@@@@@@@  @@      @@  @@@    @@@   ||
* ||   @@ @@@      @@     @@   @@  @@  @@  @@     @@@   @@@  @@@    ||
* ||   @@@@@       @@@@@@@     @@  @@  @@  @@@@@@@@@      @@@@      ||
* ||   @@@@@       @@@@@@@     @@      @@  @@@@@@@@        @@       ||
* ||   @@ @@@      @@    @@@   @@      @@  @@              @@       ||
* ||   @@  @@@     @@     @@@  @@      @@  @@              @@       ||
* ||   @@   @@@    @@      @@  @@      @@  @@              @@       ||
* ||   @@    @@@   @@      @@  @@      @@  @@              @@       ||
* ||   @@     @@@  @@      @@  @@      @@  @@              @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1334>                  ||
* |==================================================================|
* |__________________________________________________________________|
*
* ********************************************************************
* ********************************************************************
MPYR_    IFEZ
           GTO MPY30             
         ENDIF
         CLB  R0               
         TSB  R57              
         JPS  SGN2
         TCM  R55              
         ICB  R0               
SGN2     TSB  R47              
         JPS  SGN3
         TCM  R45              
         ICB  R0               
SGN3     CMM  R45,R55          
         JCY  NOFLIP
         JSB  =UT210           
NOFLIP   CLM  R70              
         STM  R45,R70          
         CLM  R40              
         STM  R55,R50          
         JZR  POS
         CLM  R53              
MYLOP    LRM  R52              
         DRP  R40              
         ARP  R70              
         JMP  TSTEZ
ADLOOP   ADM  R#,R#
         DCE                   
TSTEZ    JEN  ADLOOP
         LLM  R70              
         TSM  R50              
         JNZ  MYLOP
         CLM  R70              
         LDB  R72,=10C
         CMM  R42,R72          
         JCY  OOPS
         LDM  R45,R40          
         TSB  R0               
         JEV  POS
         TCM  R45              
POS      LDB  R44,=377         
         RTN                   
OOPS     CLB  R32              
         TSB  R0               
         JEV  OOPS1
         NCB  R32              
OOPS1    GTO INFR9             
         BSS 7FFFH-($)+1
       END
