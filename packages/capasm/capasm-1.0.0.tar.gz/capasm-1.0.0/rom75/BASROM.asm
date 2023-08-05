       ABS       
       ORG 0E000H
       TITLE 'krtok'
FNCAL.   ADDR 056CCH
*SKIPR    ADDR 0FEEAH                ; disable if assemble whole file
GO12N    ADDR 012DCH
G$012N   ADDR 012C6H
GO1N$    ADDR 012B9H
GO1N     ADDR 12D7H
G1OR2N   ADDR 012F3H
G$!012   ADDR 012D0H
GO1$     ADDR 01250H
GO1$/*   ADDR 05B87H
GOTO4N   ADDR 012E1H
*  __________________________________________________________________
* |KXTOK 509 09/27/82 - 12/14/1982                                   |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@    @@@@@@    @@     @@@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@   @@@@@@@@   @@    @@@    ||
* ||   @@   @@@    @@@    @@@      @@      @@@    @@@  @@   @@@     ||
* ||   @@  @@@      @@@  @@@       @@      @@      @@  @@  @@@      ||
* ||   @@ @@@         @@@@         @@      @@      @@  @@ @@@       ||
* ||   @@@@@           @@          @@      @@      @@  @@@@@        ||
* ||   @@@@@           @@          @@      @@      @@  @@@@@        ||
* ||   @@ @@@         @@@@         @@      @@      @@  @@ @@@       ||
* ||   @@  @@@      @@@  @@@       @@      @@      @@  @@  @@@      ||
* ||   @@   @@@    @@@    @@@      @@      @@@    @@@  @@   @@@     ||
* ||   @@    @@@   @@      @@      @@       @@@@@@@@   @@    @@@    ||
* ||   @@     @@@  @@      @@      @@        @@@@@@    @@     @@@   ||
* ||                                                                ||
* ||                  Last edited on <821208.1557>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
TOPROM   DEF  RMHEAD           ; ROM marker: 1CE3
* ** rom directory
BASLOC   DEF  RMSTRT           ; RMDR.LOC - location of file
         DEF  LEN8K            ; RMDR.SIZ - size of file
         VAL  TYTOK?           ; RMDR.TYP - type of file
         VAL  TYNSYS           ; RMDR.TNM - name of type
         DATA 0B8H,0B3H,0CAH,098H  ; RMDR.DAT - Date of creation
         DATA "basic   "       ; RMDR.NAM - name of file
         DEF  ZRO              ; RMDR.ESZ - size of file (0 for ROMs)
RMSTRT   DEF  BASROM           ; RM.ID - ROM id#
         DEF  BTAB.R           ; RM.RUN - pointer to RUNTIM table
         DEF  ASCIIS           ; RM.ASC - pointer to ASCII TOKEN table
         DEF  BASICS           ; RM.PAR - pointer to PARSE table
         DEF  NULERT           ; RM.ERR - pointer to ERRMSG table
         DEF  RETURN           ; RM.INI - pointer to INIT routine
BTAB.R   DEF  ERRORX
         DEF  FTSVL            
         DEF  SVADR            
         DEF  FTSTL            
         DEF  ICONST           
         DEF  SCONST           
         DEF  SCONST           
         DEF  STOST            
         DEF  STOSV            
         DEF  AVADR1           
         DEF  AVADR2           
         DEF  AVVAL1           
         DEF  AVVAL2           
         DEF  ERRORX
*
         DEF  GORTN            
         DEF  ERRORX
         DEF  INVRTN
         DEF  FTADR            
         DEF  SVADR+           
         DEF  FTSTLS           
         DEF  STOSVM           
         DEF  STOSTM           
         DEF  FNCAL.           
         DEF  FNCAL$           
         DEF  JTRUE#           
         DEF  ITAIL.           
         DEF  INTCON           
         DEF  JFALSR           
         DEF  JMPREL
         DEF  SUBST1           
         DEF  SUBST2           
         DEF  EJMP#            
         DEF  ERRORX
         DEF  ERRORX
         DEF  P#ARAY
         DEF  ERRORX
         DEF  R#ARAY
         DEF  ERRORX
         DEF  CONCA.           
         DEF  PRSEM.            
         DEF  ERRORX           
         DEF  ERRORX           
         DEF  MPYROI           
         DEF  ADDROI           
         DEF  ERRORX
         DEF  SUBROI           
         DEF  ERRORX
         DEF  DIV2             
         DEF  YTX5             
         DEF  UNEQ$.           
         DEF  LEQ$.            
         DEF  GEQ$.            
         DEF  UNEQ$.           
         DEF  EQ$.             
         DEF  GR$.             
         DEF  LT$.             
         DEF  CHSROI           
         DEF  UNEQ.            
         DEF  LEQ.             
         DEF  GEQ.             
         DEF  UNEQ.            
         DEF  EQ.              
         DEF  GR.              
         DEF  LT.              
         DEF  ATSIGN
         DEF  ONERR.
         DEF  OFFER.
         DEF  DEFKY.           
         DEF  FNLET.           
         DEF  AUTO.
         DEF  CATAL.           
         DEF  LSTIO.           
         DEF  CAT$.            
         DEF  DSPIS.           
         DEF  CAT.             
         DEF  LIST.            
         DEF  NAME.            
         DEF  DELAY.
         DEF  MERGE.           
         DEF  CALL.            
         DEF  READ#.
         DEF  FETK.            
         DEF  WIDTH.
         DEF  POP.
         DEF  RUN.             
         DEF  SKIPR
         DEF  DISP.
         DEF  FETCH.           
         DEF  PWIDT.
         DEF  DEFAL.
         DEF  JMPLN#
         DEF  JMPSUB
         DEF  PRIN#.
         DEF  MRGIN.           
         DEF  REST#.           
         DEF  INPUT.           
         DEF  ASSIN.           
         DEF  FNLET.           
         DEF  NOP.
         DEF  STAND.
         DEF  TMRON.           
         DEF  TMROF.           
         DEF  ON.
         DEF  BYE.             
         DEF  WAIT.
         DEF  CRDWPR
         DEF  PRINS.           
         DEF  PRINT.
         DEF  PLIST.           
         DEF  RNDIZ.           
         DEF  READ.
         DEF  REST.            
         DEF  REST0.
         DEF  RETRN.
         DEF  CRDUPR
         DEF  EDIT.            
         DEF  OFFIO.           
         DEF  STOP.            
         DEF  PUT.             
         DEF  TRFLO.           
         DEF  TROFF.           
         DEF  TRVAR.           
         DEF  EOL.             
         DEF  CLRVA.           
         DEF  COPY.            
         DEF  PURGE.           
         DEF  RENAM.           
         DEF  SKIPI
         DEF  SKIPS
         DEF  DELET.           
         DEF  RMERR.           
         DEF  SKIP!
         DEF  OPTIO.
         DEF  FNRTN.           
         DEF  SKIPEM
         DEF  SKPDEF
         DEF  SKIPD
         DEF  RENUM.           
         DEF  END.             
         DEF  SKIP!
         DEF  FOR.
         DEF  ERRORT
         DEF  SKIPIT           
         DEF  NEXT.
         DEF  BEEP.
         DEF  ERRORT
         DEF  CONFIG           
         DEF  CLOOP.           
         DEF  CONTI.           
         DEF  CLDEV.           
         DEF  SCONST           
         DEF  TEXT.            
         DEF  BASIC.           
         DEF  LIF1.            
         DEF  RESUL.
         DEF  NOP2.
*
         DEF  INVPOP
         DEF  TMRCLR           
         DEF  OR.              
         DEF  TO.
         DEF  ULIN#.
         DEF  READS.
         DEF  PRLINE
         DEF  PRSTR.           
         DEF  PRSTR.           
         DEF  SEMI#.
         DEF  COMA#.
         DEF  PR#END
BASICS   DEF  ONTOK.           
         DEF  OFTOK.           
         DEF  IP5              
         DEF  EPS10            
         DEF  FP5              
         DEF  CEIL10           
         DEF  MAX10            
         DEF  FNRET.           
         DEF  SQR5             
         DEF  MIN10            
         DEF  MEM.
         DEF  ABS5             
         DEF  ROM:GO           
         DEF  SVADCK           
         DEF  SVADCK           
         DEF  SGN5             
         DEF  KEY$.
         DEF  COT10            
         DEF  CSEC10           
         DEF  APPT.            
         DEF  EXP5             
         DEF  INT5             
         DEF  LOGT5            
         DEF  LN5              
         DEF  VER.             
         DEF  SEC10            
         DEF  CHR$.
         DEF  VAL$.
         DEF  LEN.
         DEF  NUM.
         DEF  VAL.
         DEF  INF10            
         DEF  READN.
         DEF  PI10             
         DEF  UPC$.
         DEF  USING.
         DEF  ERRORX
         DEF  TAB.
         DEF  STEP.
         DEF  EXOR.            
         DEF  NOT.             
*
         DEF  INTDIV           
         DEF  ERNUM.
         DEF  ERRL.
         DEF  CARD.            
         DEF  AND.             
         DEF  KEYS.            
         DEF  ERRORX
         DEF  SIN10            
         DEF  COS10            
         DEF  TAN10            
         DEF  NOP2.
         DEF  RESTN.
         DEF  INPUN.           
         DEF  ERRORX
         DEF  ERRORX
         DEF  INTDIV           
         DEF  POS.
         DEF  DEG10            
         DEF  RAD10.           
         DEF  INT5             
         DEF  INPU$.           
         DEF  ERRORX
         DEF  PRNUM.           
         DEF  PRNUM.           
*
         DEF  ONERRO           
         DEF  P1ANC!           
         DEF  DEFKEY           
         DEF  FNLET            
         DEF  GO12N
         DEF  PUSH1A           
         DEF  PUSH1A           
         DEF  ERRORX
         DEF  G1$OR*           
         DEF  PUSH1F           
         DEF  G$012N
         DEF  GET1$            
         DEF  GET1N            
         DEF  G$!012           
         DEF  GET1$            
         DEF  READ#            
         DEF  GET1$            
         DEF  GET1N            
         DEF  P1ANC!           
         DEF  GO1N$            
         DEF  TYPSTM           
         DEF  PRINT            
         DEF  GO1N$            
         DEF  GET1N            
         DEF  ON/OFF           
         DEF  GOTOPR           
         DEF  GOTOSU           
         DEF  PRINT#           
         DEF  GET1N            
         DEF  G1OR2N           
         DEF  INPUT            
         DEF  ASSIGN           
         DEF  FNLET            
         DEF  LET              
         DEF  ON/OFF           
         DEF  ONTMR            
         DEF  OFFTMR           
         DEF  ON               
         DEF  PUSH1A           
         DEF  GET1N            
         DEF  PUSH1A           
         DEF  G1$OR*           
         DEF  PRINT            
         DEF  G$012N           
         DEF  TRY1N            
         DEF  READ             
         DEF  PUSH1A           
         DEF  RESTOR           
         DEF  P1ANC!           
         DEF  PUSH1A           
*
         DEF  EDIT             
         DEF  PUSH1A           
         DEF  P1ANC!           
         DEF  GET1$            
         DEF  PUSH1A           
         DEF  PUSH1A           
         DEF  PUSH1A           
         DEF  GO1$             
         DEF  PUSH1A           
         DEF  FLTOFL           
         DEF  PUSH1F           
         DEF  FLTOFL           
         DEF  TYPSTM           
         DEF  TYPSTM           
         DEF  GO12N            
         DEF  ERRORX
         DEF  REM              
         DEF  OPTION           
         DEF  FNEND            
         DEF  DATA             
         DEF  DEF              
         DEF  DIM              
         DEF  GOTO4N           
         DEF  P1ANC!           
         DEF  REM              
         DEF  FOR              
         DEF  IF               
         DEF  REM              
         DEF  NEXT             
         DEF  BEEP             
         DEF  ILET             
         DEF  GO1$/*           
         DEF  PUSH1A           
         DEF  GO1N             
         DEF  GET1$            

         DATA 344
ERRORT
         DATA 44
ERRORX   JSB  =ERROR+          
         DATA 15D

TO?I     JSB  =ON?I
         REZ
         PUMD R40,+R6          
         JSB  =ON?I
         POMD R#,-R6           
         ICE                   
         RTN                   

ON?I     STE
         JMP  ON?IR

ON?R     CLE                   
ON?IR    BIN                   
         LDM  R2,R12           
         SBMD R2,=TOS          
         SBM  R2,=(EIGHT).2
         BCD                   
         JNG  NON?IR
         IFEZ
           JSB  =ONER            
         ELSE
           JSB  =ONEI            
         ENDIF
         STE                   
         DRP  R50              
         RTN                   

NON?IR   CLM  R40              
         CLE                   
         RTN                   

         DATA 11
JFALSR   JSB  =ONEROI          
         DRP  R45              
         IFEZ
           DRP R40
         ENDIF
         TSM  R#
         JZR  JMPREL
         POMD R36,+R10         
         RTN                   

         DATA 26
JMPREL   BIN                   
         ADMD R10,R10          
         RTN                   

         DATA 42
ATSIGN   LDMD R12,=TOS         
         GTO RELMEM            

         DATA 341
ONERR.   BIN                   
         LDMD R20,=FWVARS      
         LDM  R22,R10          
         SBMD R22,=RNFILE      
         STMD R22,X20,E.EREX
         LDMD R22,=PCR         
         SBMD R22,=RNFILE      
         STMD R22,X20,E.ERPC
END.ON   LDMD R10,=PCR         
         JSB  =SKPLN#          
         GTO GORTN             

         DATA 241
OFFER.   BIN                   
         LDMD R20,=FWVARS      
         CLM  R22              
         STMD R22,X20,E.EREX
         STMD R22,X20,E.ERPC
         RTN                   

         DATA 241
AUTO.    JSB  =TO?I
         LDM  R32,=(10C).2
         LDMD R30,=CURLN#      
         IFEN
           LDM  R30,R45          
           DCE                   
           IFEN
             LDM  R32,R55          
             IFZR
               JSB  =ERROR+          
               DATA 89D
             ENDIF
           ENDIF
           BCD                   
           SBM  R30,R32          
         ENDIF
         STMD R30,=CURLN#      
         STMD R32,=AUTOI       
         RTN                   

         DATA 241
DELAY.   JSB  =ONE7PR
         RNG
         DRP  !53
         STMD R53,=DELAY        
         RTN                   

         DATA 241
DEFAL.   POBD R40,-R12         
         STBD R40,=DEFAUL      
         RTN                   

         DATA 241
NOP.     RTN                   

         DATA 241
WAIT.    JSB  =ONE7PR
         RNG
         DRP !53
         STM  R53,R43           
         CLB  R40              
WCKJSB   JSB  =MELJSB          
           DEF WAITCK
         RTN                   

ONE7PR   JSB  =MELJSB          
           DEF ONE7+B
         TSM  R46              
         DRP  R53              
         IFNZ
           CLM  R53              
           DCM  R53              
         ELSE
           LDM  R53,R41          
         ENDIF
         TSB  R17              
         DRP  R53              
         RTN                   

         DATA 241
DISP.    LDB  R40,=1           
         LDM  R52,=(DISPTR).2
         DEF  DSFLAG
         DEF  DISPLN
         JMP  DOCOM

         DATA 241
PRINT.   LDB  R40,=2           
         LDM  R52,=(PRTPTR).2
         DEF  PRFLAG
         DEF  PRNTLN

DOCOM    DRP  !52
         STMD R52,=P_PTR       
         CLB  R50              
         STBD R50,=USING?      
         ICB  R50              
         STBI R50,=P_FLAG      
         STBD R40,=ROUTE       
         JSB  =CLRTMT          
         RTN                   

         DATA 315
OPTIO.   POMD R64,+R10          
         RTN                   

         DATA 312
SKPDEF   BIN
         ICM  R10              
         ICM  R10              
         POMD R10,+R10         
         ADMD R10,=RNFILE      
         RTN                   

         DATA 241
WIDTH.   JSB  =WIDSUB
         STBD R#,=DISPLN       
         RTN                   

         DATA 241
PWIDT.   JSB  =WIDSUB
         STBD R#,=PRNTLN       
         RTN                   

WIDSUB   BIN                   
         POMD R40,-R12         
         CMM  R40,=99C,40C,99C,99C,99C,99C,99C,99C
         IFEQ
           CLB  R40              
           RTN                   
         ENDIF
         PUMD R40,+R12         
         JSB  =ONEB            
         TSB  R47              
         DRP  R46              
         IFNZ
           LDB  R46,=255D
         ENDIF
         TSB  R46              
         IFZR
           ICB  R46              
         ENDIF
         RTN                   

         DATA 41
USING.   DRP  R76              
         JSB  =GETAD#          
         ARP  !12
         POMD R2,-R12           
         STM  R2,R74           

USEXIT   STM  R74,R70          
         STMD R70,=IMSLEN      
         LDB  R77,=177         
         STBD R77,=USING?      
         RTN                   

         DATA 1,51
NOP2.    RTN                   

         DATA 27
ULIN#.   BIN                   
         POMD R36,+R10         
         ADMD R36,=RNFILE      
         POMD R63,+R36         
         CLM  R74              
         POBD R74,+R36         
         CMB  R66,=216         
         IFNE
           JSBN  =ERROR+          
           DATA 53D
         ENDIF
         LDM  R76,R36         
         JMP  USEXIT

         DATA 35
PRLINE   BIN                   
         LDBD R22,=USING?      
         IFNZ
           PUMD R10,+R6          
           LDMD R10,=IMCADR      
           LDMD R30,=IMCLEN      
           LDMD R36,=IMSADR      
           CMM  R36,R10          
           IFEQ
             LDBI R22,=P_FLAG      
             JZR PRLN2-
           ENDIF
           JSB  =SCANLX
PRLN2-     POMD R10,-R6          
         ENDIF
         JSB  =LINEND
         RTN                   
       TITLE 'krkad'
*  __________________________________________________________________
* |IVKAD 248 05/10/82 - 5/13/1982 3:44PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@  @@     @@@    @@@@@@    @@@@@@       ||
* ||   @@@@@@@@@@  @@      @@  @@    @@@    @@@@@@@@   @@@@@@@@     ||
* ||       @@      @@      @@  @@   @@@    @@@    @@@  @@    @@@    ||
* ||       @@      @@      @@  @@  @@@     @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@ @@@      @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@@@@       @@@@@@@@@@  @@      @@   ||
* ||       @@       @@    @@   @@@@@       @@@@@@@@@@  @@      @@   ||
* ||       @@        @@  @@    @@ @@@      @@      @@  @@      @@   ||
* ||       @@         @@@@     @@  @@@     @@      @@  @@      @@   ||
* ||       @@         @@@@     @@   @@@    @@      @@  @@    @@@    ||
* ||   @@@@@@@@@@      @@      @@    @@@   @@      @@  @@@@@@@@     ||
* ||   @@@@@@@@@@      @@      @@     @@@  @@      @@  @@@@@@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1333>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
KYADDR   PUMD R76,+R6          
         PUMD R20,+R6          
         LDB  R20,R40          
         JSB  =TOBCD2          
         STM  R20,R76          
         JSB  =KYOPEN          
         IFEZ
           JSB  =FSEEK           
         ENDIF
         POMD R20,-R6          
         POMD R76,-R6          
         RTN                   
       TITLE 'krmod'
*  __________________________________________________________________
* |IVMOD 291 05/10/82 - 5/13/1982 3:51PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@  @@      @@    @@@@@@    @@@@@@       ||
* ||   @@@@@@@@@@  @@      @@  @@@    @@@   @@@@@@@@   @@@@@@@@     ||
* ||       @@      @@      @@  @@@@  @@@@  @@@    @@@  @@    @@@    ||
* ||       @@      @@      @@  @@@@@@@@@@  @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@  @@  @@  @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@  @@  @@  @@      @@  @@      @@   ||
* ||       @@       @@    @@   @@      @@  @@      @@  @@      @@   ||
* ||       @@        @@  @@    @@      @@  @@      @@  @@      @@   ||
* ||       @@         @@@@     @@      @@  @@      @@  @@      @@   ||
* ||       @@         @@@@     @@      @@  @@@    @@@  @@    @@@    ||
* ||   @@@@@@@@@@      @@      @@      @@   @@@@@@@@   @@@@@@@@     ||
* ||   @@@@@@@@@@      @@      @@      @@    @@@@@@    @@@@@@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1333>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
MODEKY   LDM  R30,=EXEC        
MODELP   JSB  =MODE?
         DRP  R30              
         IFEN
           LDM  R30,R0           
         ENDIF
         PUMD R30,+R6          
         JSB  X30,ZRO          
         LDBD R2,=LETSEE       
         IFNZ
           JSB  =EOLND           
           JSB  =UNSEE
         ENDIF
         POMD R30,-R6          
         JMP  MODELP
KEYTAB   VAL APPTKY
         DEF APPTMD

         VAL TIMEKY
         DEF TIMEMD

         VAL  EDITKY
         DEF  EXEC

         VAL NAPKEY
         DEF ZZZZZZ

         VAL BYEKEY
         DEF ZZZZZZ

         VAL APNOTE
         DEF ANOTE

         VAL APCMND
         DEF ACMND
         
         DATA 0
         
MODE?    JSB  =PWROK?          
         DRP  R25              
         IFEN
           LDB  R25,=NAPKEY
         ENDIF
         DRP  !25
         JSB  =LOOKUP          
         DEF  KEYTAB
         IFEZ
           ICE                   
           RTN                   
         ENDIF
         CLE                   
         RTN                   
       TITLE 'krtxt'
FETSET ADDR 1DC3H
*  __________________________________________________________________
* |KXTXT 525 09/27/82 - 2/ 3/1983 7:54AM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@      @@  @@@@@@@@@@   ||
* ||   @@   @@@    @@@    @@@      @@      @@@    @@@      @@       ||
* ||   @@  @@@      @@@  @@@       @@       @@@  @@@       @@       ||
* ||   @@ @@@         @@@@         @@         @@@@         @@       ||
* ||   @@@@@           @@          @@          @@          @@       ||
* ||   @@@@@           @@          @@          @@          @@       ||
* ||   @@ @@@         @@@@         @@         @@@@         @@       ||
* ||   @@  @@@      @@@  @@@       @@       @@@  @@@       @@       ||
* ||   @@   @@@    @@@    @@@      @@      @@@    @@@      @@       ||
* ||   @@    @@@   @@      @@      @@      @@      @@      @@       ||
* ||   @@     @@@  @@      @@      @@      @@      @@      @@       ||
* ||                                                                ||
* ||                  Last edited on <830203.0751>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
         DATA  241
ASSIN.   BIN
         LDM  R22,=TYBASC
         JSB  =ONR12?
         STB  R#,R14
         CMB  R#,=12D
         IFNE
           POMD R22,-R12
         ENDIF
         JSB  =GETADR
         ARP  !12
         POMD R2,-R12
         POMD R70,-R12
         PUMD R2,+R12
         JSB  =PUTREL
         ARP  !12
         PUMD R70,+R12
         JSB  =GET#AN
         REZ
         JSB  =STAR?
         JZR  IFSTAR
         ADM  R12,=(4).2
         JSB  =GETNAM
         REN
         TSM  R54
         IFNZ
           GTO HAND
         ENDIF
         JSB  =FOPEN
         STM  R20,R76
         IFEN
           LDM  R20,R22
           JSB  =FCRNUL
           REN
         ELSE
           LDBD R0,X30,DR.TNM
           CMB  R0,R23
           IFNE
             CMB  R14,=12D
             IFEQ
               CMB  R0,=TYNTEX
               JEQ  krtxt_1
             ENDIF
             JSBN  =ERROR+
             DATA 68D
           ENDIF
         ENDIF
krtxt_1  STM  R40,R60
         JSB  =IO?
         JSB  =IOOPEN
         RTN

IFSTAR   CMB  R14,=12D
         IFNE
           JSBN =ERROR+
           DATA  89D
         ENDIF
         LDM  R76,R20
         LDMD R40,=IOFILE
         JSB  =FDELLN
         RTN

GAPa02   NOP
         NOP

         DATA 241
REST#.   LDB  R24,=0EH
         LDB  R14,=(TYRUN?)|(TYLIN?)
         JSB  =CLRPR#
         JMP  READ#+

         DATA 241
PRIN#.   JSB  =SETPR#
         STBD R#,=PRNT#1
         LDB  R14,=(TYRUN?)|(TYLIN?)|(TYEDT?)|(TYRAM?)
         JMP  READ#-

         DATA 241
READ#.   LDB  R14,=(TYRUN?)|(TYLIN?)|(TYLST?)|(TYCOP?)
         JSB  =CLRPR#
READ#-   LDB  R24,=0FH
READ#+   JSB  =ONR12?
         TSB  R#
         JLZ  krtxt_2

         JSB  =GET#LN
         REZ
         STM  R#,R24

krtxt_2  JSB  =GET#AN
         REZ
         STM  R#,R76
         JSB  =FILE#?
         JEZ  SETFIL1
         RTN

GAPb02   NOP
         NOP

DATTK.   EQU  206
         DATA 241
RESTO.   LDB  R24,=0EH
         JMP  READ.+

         DATA 227
RESTN.   BIN
         DRP  !20
         POMD R20,+R10
         ADMD R20,=RNFILE
         POMD R24,+R20
         JMP  READ.+

gapa01   NOP
         DATA 241
READ.    LDB  R24,=0FH
READ.+   BIN
         JSB  =CLRPR#
         LDB  R14,=(TYRUN?)|(TYLIN?)
         JSB  =IO?
         LDMD R40,=RNNAME
         STMD R40,X36,(NAME#).2
         CLM  R76

SETFIL1  STBD R14,=ACCESS
         STMD R76,=FILNUM
         STMD R36,=A#IO
         JSB  =FILAD?
         REN
         JSB  =DOSAFE
         REN

setlin   CMB  R24,=0EH
         IFEQ
           ICB  R24
           CLM  R0
           JMP  update
         ENDIF
         CMB  R#,=0FH
         IFEQ
           LDBD R0,=PRNT#?
           JZR  SETNUM
           LDBD R0,X34,DATA#
           JZR  SETNUM
           LDMD R0,X34,LINE#
           JSB  =TOBIG?
           REN
         ENDIF
update   STMD R#,X34,LINE#
         CLB  R#
         STBD R#,X34,DATA#

SETNUM   STBD R24,=RANDOM
         LDMD R76,X34,LINE#
         JSB  =FSEEK
         CMB  R24,=0FH
         JNE  krtxt_3
         IFEN
           JSB  =CHKEND
           JNZ  krtxt_4
           TSM  R76
           IFZR
             ICM  R76
           ENDIF
           JMP  PRINT?
         ENDIF
         JSB  =VALID?
         JEZ  krtxt_5
         JMP  krtxt_4
krtxt_3  JEZ  GOTLIN
PRINT?   LDBD R2,=PRNT#?
         JNZ  BUILD
JSBE34   JSBN  =ERR1+
         DATA 34D

BUILD    LDM  R30,R36
         PUMD R34,+R6
         JSB  =BILDIT
         POMD R34,-R6
         REN
GOTLIN   JSB  =VALID?
         JEN  JSBE34

krtxt_4  JSB  =DATOK?
         JEN  ADD1?
DATNUM
krtxt_5  JSB  =LINE36
         DRP  !36
         STM  R36,R30
         LDBD R2,=TEXT?
         IFNZ
           ICM  R30
           ICM  R30
           LDBD R2,=PRNT#?
           RZR
           CLM  R2
           LDBD R2,R30
           ADM  R2,R30
           STM  R2,R30
           RTN
         ENDIF
         ADM  R30,=(4).2
         LDBD R20,X34,DATA#
krtxt_6  DCB  R20
         RNG
         POBD R32,+R30
         CMB  R32,=0EH
         IFEQ
NEXTLN     JSB  =GETDAT
           REZ
           DCE
           IFEZ
ADD1?        LDBD R2,=PRNT#?
             JZR  JSBE34
             DRP  R76
             JSB  =TOBIG?
             REN
             LDM  R30,R36
             JSB  =BILDIT
             REN
             JSB  =DATOK?
           ENDIF
           RTN
         ENDIF
         CMB  R#,=1AH
         IFEQ
           ADM  R30,=(3).2
           JMP  krtxt_6
         ENDIF
         DRP  !32
         CMB  R32,=96H
         IFEQ
krtxt_7    DRP  !32
           CLM  R32
           POBD R32,+R30
           ADM  R32,R30
           STM  R32,R30
           JMP  krtxt_6
         ENDIF
         DRP  !32
         CMB  R32,=5H
         JZR  krtxt_7
         CMB  R32,=6H
         JZR  krtxt_7
         CMB  R32,=4H
         IFEQ
           ADM  R30,=(8H).2
           JMP  krtxt_6
         ENDIF
         JSB  =HANDI
         VAL  V.UNKD
         DATA 33D
         STE
         RTN

TOBIG?   CLE
         BCD
         CMM  R#,=9999H
         IFEQ
           JSBN =ERR1+
           DATA 90D
         ENDIF
         ICM  R#
         BIN
         RTN

gapa05   NOP
         NOP
         NOP
         NOP
         NOP

         DATA 44
readn.   CLB  R56
         JMP  readdt

         DATA 44
reads.   CLB  R56
         DCB  R56

readdt   JSB  =RSETUP
         TSB  R56

         IFZR
           JSB  =TRAPTX
           REN
         ENDIF

         PUMD R10,+R6
NXDATA   LDM  R10,R30
         JSB  =DATA+1
         LDBD R2,=TEXT?
         IFNZ
           CMB  R34,=1
           JNE krtxt_8
GOTSTR     JSB  =SCONST
           JMP  POP&ST
         ENDIF
         POBD R34,+R10
         CMB  R34,=16
         IFEQ
krtxt_8    JSB  =GETDAT
           JEZ  NXDATA
           POMD R10,-R6
           JSBN  =ERROR+
           DATA  34D
         ENDIF
         CMB  R34,=4
         IFNZ
           CMB  R#,=32
           IFNZ
             TSB  R56
             JNZ  GOTSTR
             POMD R10,-R6
             JSBN  =ERROR+
             DATA 33D
           ENDIF
           JSB  =INTCON
         ELSE
           JSB  =ICONST
         ENDIF

         TSB  R56
         IFNZ
           JSB  =VAL$.
POP&ST     POMD R10,-R6
           REN
           JSB  =STOST
           RTN
         ENDIF
         POMD R10,-R6
         JSB  =STOSV
         RTN

         DATA  35
PR#END   JSB  =PSETUP
PR#ERR   LDBD R2,=PRNT#1
         JZR  krtxt_9
CLRLIN   LDMD R30,=A#LINE
         CLM  R32
         LDBD R32,X30,LEN#
         ADM  R32,=(3).2
         JSB  =DELETE
krtxt_9  CLB  R2
         STBD R2,=PRNT#1
         RTN

SETPR#   LDB  R2,=1
         JMP  krtxt_10

CLRPR#   CLB  R2

krtxt_10 DRP  !2
         STBD R2,=PRNT#?
         RTN
gapb01   NOP

         DATA 41
PRSEM.   RTN

PRSEM    LDBD R0,=PRNT#1
         RZR
PRSEM+   JSB  =CLRLIN
         LDMD R76,X34,LINE#
         JSB  =BILDIT
         ADM  R30,=(4).2
         LDM  R26,=(2).2
         LDBD R2,=TEXT?
         IFNZ
           DCM  R30
           DCM  R30
           CLM  R26
         ENDIF
         RTN

BILDIT   LDB  R63,=1
         STBD R63,=NEW?
         LDMD R63,=(EMTDAT)-2
         STM  R76,R63
         LDM  R32,=(5).2
         LDBD R2,=TEXT?
         IFNZ
           CLB  R65
           DCM  R32
           DCM  R32
         ENDIF
         STMD R63,=TMPMM2
INSRT    LDM  R34,=TMPMM2
         JSB  =INSERT
         RTN

         DATA 36
SEMI#.
COMA#.
PR#VAL   JSB  =PSET#1
         REN
         JMP  prtxt_11
P#VAL+   JSB  =PSETUP
prtxt_11
         ICM  R36
         ICM  R36
         CLM  R20
         LDBD R20,R36
         STM  R20,R26
         JSB  =ONR12?
         REZ
         CMB  R#,=STRSIZ
         JNZ  krtxt_12
         JSB  =PRSEM
         JSB  =GETADR
         ARP  !12
         POMD R32,-R12
         LDBD R0,=TEXT?
         IFNZ
           TSB  R33
           IFNZ
             LDM  R32,=(0FFH).2
             JSB  =WARN4
           ENDIF
           ADM  R26,R32
           TSB  R27
           JNZ  NEWLIN1
           ICM  R30
           JSB  =INSERT
           JMP  FINISH
         ENDIF
         ICM  R32
         ICM  R32
         CMM  R32,=(0FEH).2
         IFPS
           LDM  R32,=(0FDH).2
           JSB  =WARN4
         ENDIF
         ADM  R26,R32
         TSB  R27
         JNZ  NEWLIN1
         DCM  R34
         DCM  R34
         JSB  =INSERT
         REN
         DCM  R32
         DCM  R32
         STB  R32,R33
         LDB  R32,=PRITOK
         STMD R32,R30
         JMP  FINISH

krtxt_12 POMD R40,-R#
         JSB  =TRAPTX
         REN
         JSB  =PRSEM
         CMB  R44,=0FFH
         DRP  R32
         IFEQ
           LDM  R32,=(4).2
           LDB  R44,=1AH
         ELSE
           LDM  R32,=(9D).2
           STMD R40,=(TMPMM2)+1
           LDB  R47,=4H
         ENDIF
         STMD R#,=TMPMM2
         ADM  R26,R32
         TSB  R27
         IFNZ
NEWLIN1    ADM  R12,R2
           JSB  =NEXTLN
           IFEN
             JSBN  =ERR1+
             DATA 28D
           ENDIF
           JSB  =PRSEM+
           GTO P#VAL+
         ENDIF
         JSB  =INSRT
FINISH   REN
         STBD R26,R36
         CLB  R#
         STBD R#,=NEW?
DATA+1   LDMD R30,=A#IO
         LDBD R34,X30,DATA#
         ICB  R34
         STBD R34,R2
         RTN

WARN4    JSB  =WARN
         DATA 42D
         LDM  R2,=(FOUR).2
         RTN

         DATA 36
P#ARAY   JSB  =PSET#1
         REN

         JSB  =TRAPTX
         REN
         JSB  =FETSET

         STMD R36,=KLUDGE
         PUMD R46,+R6
         LDMD R72,R34
         JSB  =LENCAL
         LDMD R34,=KLUDGE
         PUMD R36,+R6
         PUMD R56,+R6

NXTELP   JSB  =FETNUM
         TSB  R17
         IFNG
           JSB  =PR#ERR
           POMD R62,-R6
           RTN
         ENDIF
         PUMD R60,+R12
         JSB  =P#VAL+
         POMD R52,-R6
         STM  R52,R32
         TSB  R17
         RNG
         JSB  =ATTN?
         REN
         SBM  R36,R34
         RZR
         LDM  R46,R32
         LDM  R52,R32
         PUMD R52,+R6
         ADMD R34,=KLUDGE
         STMD R34,=KLUDGE
         JMP  NXTELP

         DATA 44
R#ARAY   JSB  =RSETUP
         JSB  =TRAPTX
         REN
         JSB  =FETSET
         PUMD R36,+R6
         PUMD R36,+R12
         LDBD R0,X10,(-4).2
         CLM  R73
         DCM  R73
         LDB  R77,=ARY2TK
         SBB  R77,R0
         PUMD R73,+R12
         PUMD R46,+R12
         PUMD R46,+R6
         LDMD R72,R34
         JSB  =LENCAL
         PUMD R36,+R6
         PUMD R56,+R6
         LDBD R56,=TRFLAG
NXTEL-   PUBD R#,+R#
         JSB  =READN.
         POBD R2,-R6
         STBD R2,=TRFLAG
         POMD R50,-R6
         STM  R50,R30
         TSB  R17
         RNG
         SBM  R36,R34
         RZR
         ADM  R30,R34
         PUMD R30,+R12
         PUMD R73,+R12
         PUMD R32,+R12
         LDM  R50,R30
         PUMD R50,+R6
         CLB  R50
         STBD R50,=TRFLAG
         DRP  R2
         JMP  NXTEL-

TYPTAB   DATA 10,3,4
LENCAL   PUMD R46,+R6
         ANM  R46,=60,0
         STBD R46,=DIMFLG
         LRB  R46
         LRB  R46
         LRB  R46
         LRB  R46
         CLM  R36
         LDBD R36,X46,TYPTAB
         POMD R46,-R6
         CLM  R0
         LLB  R73
         ELM  R0
         STMD R0,=OPTBAS
         JSB  =CALCSZ
         RTN

GETDAT   BIN
         CLE
         LDBD R36,=RANDOM
         CMB  R36,=0FH
         JNE  E=2
         LDMD R36,=A#LINE
krtxt_13 LDMD R76,R36
         JSB  =SKPLN
DATOK?   CLE
         JSB  =CHKEND
         JZR  E=1
         JSB  =VALID?
         JEN  krtxt_13

         LDMD R34,=A#IO
         LDMD R30,R36
         STMD R30,X34,LINE#
         CLB  R30
         STBD R30,X34,DATA#
         LDM  R30,R36
         ADM  R30,=(4).2
         LDBD R2,=TEXT?
         IFNZ
           DCM  R30
           DCM  R30
         ENDIF
LINE36   STMD R36,=A#LINE
         RTN

E=2      ICE
E=1      ICE
         RTN

IO?      LDMD R40,=IOFILE
         JSB  =FLOPEN
         REZ
         JSBN  =ERR1+
         DATA  15D

GET#LN   JSB  =ONEI
         STE
         TSB  R47
         JNZ  BADUN
         LDM  R20,R45
         RTN

GET#AN   JSB  =GET#LN
         RNZ

BADUN    JSBN  =ERROR+
         DATA 89D

RESTUP   LDBD R14,=ACCESS
         JSB  =CLRPR#
         JMP  ALWAYS
PSETUP   LDB  R14,=(TYRUN?)|(TYLIN?)|(TYEDT?)|(TYRAM?)
         JSB  =SETPR#
ALWAYS   BIN
         LDMD R76,=FILNUM
         JSB  =FILE#?
         JEN  BACK2
         JSB  =FILAD?
         JEN  BACK2
         LDMD R76,X34,LINE#
         JSB  =FSEEK
         IFEN
           JSB  =ERR1
           DATA 32D
           JMP  BACK2
         ENDIF
         JSB  =DATNUM
         REZ
BACK2    DCM  R6
         DCM  R6
         RTN

FILAD?   LDBD R21,X36,TYPE#
         IFNZ
HAND       JSB  =HANDI
           VAL  V.ASN#
           DATA 63D
           STE
           RTN
         ENDIF
         CLB  R2
         STBD R2,=TEXT?
         STM  R36,R34
         LDMD R40,X34,NAME#
         JSB  =FOPAC?
         IFEN
           JSBN  =ERR1+
           DATA  62D
         ENDIF
         IFNZ
           LDBD R0,X30,DR.TNM
           CMB  R0,=TYNTEX
           JNE  BADACC
           ANM  R14,=
           VAL  NOT#6
           DATA 0FFH
           ANM  R15,R14
           CMM  R15,R14
           IFNE
BADACC       JSB  =HANDI
             VAL  V.ACC#
             DATA 65D
             STE
             RTN
           ENDIF
           LDB  R2,=1
           STBD R2,=TEXT?
         ENDIF
         JSB  =MOVEUP
         RTN

PSET#1   JSB  =PSETUP

DOSAFE   LDBD R2,=PRNT#?
         RZR
         CMMD R40,=RNNAME
         IFEQ
           JSBN  =ERR1+
           DATA  51D
         ENDIF
         JSB  =SAFE!
         JSB  =ANYER?
         RTN

VALID?   CLE
         LDBD R2,=TEXT?
         IFZR
           LDMD R64,R36
           CMB  R67,=DATTK.
           IFNE
             ICE
           ENDIF
         ENDIF
         RTN

TRAPTX   CLE
         LDBD R0,=TEXT?
         RZR
         LDBD R0,=NEW?
         IFNZ
           JSB  =CLRLIN
         ENDIF
         JMP BADACC

FILE#?   JSB  =IO?
         JSB  =FSEEK
         REZ
         JSBN  =ERR1+
         DATA  45D

EMTDAT   DATA  2
         DATA  086H
         DATA  0EH
       TITLE 'krpil'
*  __________________________________________________________________
* |MJPIL                                                             |
* |==================================================================|
* ||                                                                ||
* ||   @@      @@    @@@@@@@@  @@@@@@@@    @@@@@@@@@@  @@           ||
* ||   @@@    @@@    @@@@@@@@  @@@@@@@@@   @@@@@@@@@@  @@           ||
* ||   @@@@  @@@@        @@    @@     @@@      @@      @@           ||
* ||   @@@@@@@@@@        @@    @@      @@      @@      @@           ||
* ||   @@  @@  @@        @@    @@     @@@      @@      @@           ||
* ||   @@  @@  @@        @@    @@@@@@@@@       @@      @@           ||
* ||   @@      @@        @@    @@@@@@@@        @@      @@           ||
* ||   @@      @@        @@    @@              @@      @@           ||
* ||   @@      @@  @@    @@    @@              @@      @@           ||
* ||   @@      @@  @@@  @@@    @@              @@      @@           ||
* ||   @@      @@   @@@@@@     @@          @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@      @@    @@@@      @@          @@@@@@@@@@  @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820813.1414>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
         DATA 241              
EOL.     JSB  =ONR12?          
         JEZ  ELINIT
         JSB  =GETADR          
         ARP  !12
         POMD R2,-R12          
         CMM  R2,=(4).2
         IFCY
           JSBN  =ERROR+          
           DATA  42D
         ENDIF
         STBD R#,=EOLLEN       
         LDMD R55,R34          
         JMP ELSTOR

C.INIT   LDM  R54,=1,12D,4,31D   
         STMD R54,=PLSTAT      
ELINIT   LDM  R54,=13D,10D,377,2 
ELSTOR   STMD R#,=EOL         
         RTN                   

         DATA 241
STAND.   BIN                   
         POBD R#,-R12         
STAND-   TSB  R#              
         IFZR
S.OFF      LDM  R70,=
A.ZERO     DATA 0,0,68H,043H,0,055H,023H,0 
         ELSE
S.ON       LDBD R2,=STAND?       
           LDM  R70,=0FFH,0FFH,0B7H,0D3H,018H,0,0,0
         ENDIF
STAND+   STMD R#,=STAND?      
         JEV  PILOF!
         TSB  R2               
         ROD

PILON    LDBD R2,=PILR2
         LDB  R2,=1            
         STBD R2,=PILR0
         CLB  R2               
         STBD R2,=PILR0
         LDBD R3,=PILADR       
         CMB  R3,=37           
         JNC  krpil_1
         CLB  R3               
krpil_1  STMD R2,=PILR3
         RTN                   

PILOF!   LDB  R2,=1            
         STBD R2,=PILR0
         STBD R2,=PILR7
         RTN                   

IDYSND   LDB  R55,=140         
         JMP  SNDFRM
UNTSND   LDB  R57,=UNT_
CMDSND   LDB  R56,=200         
RDYSND   LDB  R55,=120         

SNDFRM   PUMD R74,+R6          
         LDBD R74,=STAND?      
         IFEV
           JSB  =PILON!
         ENDIF
TRYIT    JSB  =STOP?           
         IFEN
           LDBD R#,=NDATTN       
           JZR  NOSEND
         ENDIF
         LDBD R77,=PLSTAT      
         IFNG
           JSB  =HANDI0          
           VAL  V.LOOP
           IFEN
NOSEND       ICE                   
             ICE                   
             CLB  R55              
             JMP  SNDEND
           ENDIF
           TSB  R77              
           JZR  MORE?
         ENDIF
         IFOD
           JSB  =CLRTMT          
           IFOD
             JSB  =ERR1            
             DATA 60D
             JMP  NOSEND
           ENDIF
           JSB  =TSTIDY
           JZR  DOTIME
         ENDIF
         CLE                   
         LDBD R#,=PILR2
         STMD R55,=PILR0
ORAV+    LDM  R75,=0,0C0H,0     
ORAV?    LDBD R56,=PILR1
         JOD  ORAV=1
         JSB  =STOP?           
         IFEN
           TSB  R76              
           IFZR
             JSB  =TSTIDY
             JZR  DOTIME
             STE
             JMP  E+2
           ENDIF
         ENDIF
         DCM  R75              
         JNZ  ORAV?
         TSB  R74              
         JNG  ORAV+
DOTIME   JSB  =LPOFF           
         CLE                   
E+2      ICE                   
         ICE                   
PILEND   JSB  =PILTRP          

SNDEND   TSB  R74              
         IFEV
           JSB  =PILOF!
         ENDIF
         POMD R74,-R6          
         TSB  R55              
         RTN                   

ORAV=1   DRP  !56
         LDMD R56,=PILR1
         STB  R56,R3           
         JSB  =SRQR?
         JEN  PILEND
MORE?    LDBD R3,=FAST!        
         JZR  PILEND
         DCM  R36              
         JNG  PILEND
         LDM  R55,=140,0,0     
         POBD R57,+R30         
         GTO  TRYIT

TSTIDY   LDM  R75,=140,0C0H,0   
         STMD R75,=PILR0
         LDM  R76,=(300H).2        
krpil_2  LDBD R3,=PILR1
         JOD  SRQR?
         DCM  R76              
         JNZ  krpil_2
         RTN                   

SRQR?    CLE                   
         ANM  R3,=0AH
         JZR  FIXDRP
         ICE                   
         ANM  R3,=BIT#1
         JNZ  FIXDRP
         JSB  =HANDI0          
         VAL  V.SRQR
         CLE                   
FIXDRP   TSM  R76              
         RTN                   

UNLSND   LDB  R57,=UNL_
         JSB  =CMDSND
         JMP  krpil_3

UNLRP?   JSB  =LPOFF           
         ANM  R#,=((BIT#5)|(BIT#4)).1
         CMB  R#,=BIT#4
         RNE
UNLREP   LDB  R57,=UNL_
         JSB  =CMDREP
krpil_3  RZR
CL.ACT   LDBD R3,=PLSTAT       
         ANM  R3,=((NOT#3)&(NOT#1)).1
         STBD R3,=PLSTAT       
         TSB  R55              
         RTN                   

UNTREP   LDB  R57,=UNT_
         JMP  CMDREP
VFTAD
TADREP   LDBD R57,X36,DADDR
         ADB  R57,=TAD_
         JMP  CMDREP

VFLAD
LADREP   LDBD R57,X36,DADDR
         ADB  R57,=LAD_

CMDREP   JSB  =CMDSND
         JMP  ERR?

DATREP   CLB  R56              
         LDB  R55,=140         
         JSB  =SNDFRM
ERR?     REZ
         JSB  =PILREP          
         TSB  R55              
         RTN                   
       TITLE 'krfor'
*  __________________________________________________________________
* |KXFOR 199 08/31/82 - 9/ 9/1982 4:26PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@    @@@@@@    @@@@@@@@     ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@   @@@@@@@@   @@@@@@@@@    ||
* ||   @@   @@@    @@@    @@@  @@          @@@    @@@  @@     @@@   ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@      @@   ||
* ||   @@ @@@         @@@@     @@          @@      @@  @@     @@    ||
* ||   @@@@@           @@      @@@@@@@@@   @@      @@  @@@@@@@      ||
* ||   @@@@@           @@      @@@@@@@@@   @@      @@  @@@@@@@      ||
* ||   @@ @@@         @@@@     @@          @@      @@  @@    @@@    ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@     @@@   ||
* ||   @@   @@@    @@@    @@@  @@          @@@    @@@  @@      @@   ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@   @@      @@   ||
* ||   @@     @@@  @@      @@  @@            @@@@@@    @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <820909.1624>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
         DATA  7                
JTRUE#   JSB  =ONEROI          
         DRP  R45              
         IFEZ
           DRP R40
         ENDIF
         TSM  R#             
         JNZ  NEWLIN
         POMD R36,+R10         
         RTN                   

         DATA 210
JMPSUB   BIN                   
         LDM  R36,R10          
         ICM  R36              
         ICM  R36              
ONSUB    LDM  R34,=8000H
         JSB  =SUBSTF
         REN

         DATA 210
JMPLN#   DATA 25
EJMP#
NEWLIN
         POMD R36,+R10         
         BIN                   
         ADMD R36,=RNFILE      
         STM  R36,R10          
         JSB  =TRJUMP          
         GTO GORTN             

SUBSTF   LDMD R32,=FWVARS      
         LDBD R22,X32,E.GCNT
         ICB  R22              
         JCY  ERGSB
         LDM  R56,=(GOSBSZ).2
         JSB  =GETMEM
         JEN  ERGSB
         STBD R22,R2           
         LDMD R22,=NXTRTN      
         PUMD R34,+R22         
         LDMD R0,=PCR          
         SBMD R0,=RNFILE       
         PUMD R0,+R22          
         SBMD R36,=RNFILE      
         PUMD R36,+R22         
         CLE                   
         RTN                   

ERGSB    JSBN  =ERR1+           
         DATA 49D

GETMEM   CLE                   
         LDM  R40,R30          
         LDMD R32,=NXTRTN      
         SBMD R32,=LAVAIL      
         LDMD R26,=LAVAIL      
         STM  R26,R34          
         SBM  R26,R56          
         SBMD R26,=LEEWAY      
         CMMD R26,=TOS         
         IFNC
           JSBN  =ERR1+           
           DATA  16D
         ENDIF

         ADMD R#,=LEEWAY       
         STMD R#,=LAVAIL       
         STM  R#,R30           
         JSB  =COPY            
         LDMD R30,=NXTRTN      
         SBM  R30,R56          
         STMD R30,=NXTRTN      
         STM  R40,R30          
         RTN                   

         DATA 230
ON.      JSB  =ONEI            
         DCM  R45              
         JNG  INVAL
         ICM  R45              
         LDBD R56,R10          
ONLP1    POMD R65,+R10         
         CMB  R65,R56          
         JNZ  INVAL
         DCM  R45              
         JNZ  ONLP1
         LDM  R36,R10          
         PUMD R65,-R10         
ONLP2    DRP  !65
         POMD R65,+R36         
         CMB  R65,R56          
         JZR  ONLP2
         PUMD R65,-R36         
         POBD R65,+R10         
         CMB  R65,=GOSTOK
         IFEQ
           BIN                   
           GTO ONSUB
         ENDIF
         GTO  NEWLIN
INVAL    JSB  =ERROR+          
         DATA 11D

         DATA  44
INVRTN   JSB  =ATSIGN
         JMP  RETRN.

         DATA 241
RETRN.   JSB  =INVPOP
         REN

FNDRTN   ADMD R32,=RNFILE      
         STM  R32,R10          
         ADMD R30,=RNFILE      
         JSB  =TRJUMP          
         RTN                   

         DATA 241
POP.     STE
         JMP  POP

         DATA 44
INVPOP   CLE                   
POP      BIN                   
         LDMD R36,=FWVARS      
         LDBD R34,X36,E.GCNT
         DCB  R34              
         JNC  POPERR
         STBD R34,R2           
         LDMD R34,=NXTRTN      
         POMD R76,+R34         
         IFNG
           ANM  R76,=7FFFH        
           IFNZ
             LDMD R36,X36,E.EREX
             IFNZ
               STMD R76,R2           
             ENDIF
           ENDIF
         ELSE
           JSB  =TMRDNE          
         ENDIF
         POMD R30,+R34         
         POMD R32,+R34         
REMGSB
         LDM  R56,=(0-(GOSBSZ)).2
         JSB  =GETMEM
         CLE                   
         RTN                   

POPERR   REN
         JSBN  =ERR1+           
         DATA  50D

         DATA  341
FOR.     BIN                   
         LDMD R65,R10          
         JSB  =GETFC
         LDMD R26,=LAVAIL      
         STM  R26,R2           
         STB  R20,R0           
         LOOP
           LDMD R36,R26          
           DCB  R0               
           JNG  NOMORE
           ADM  R26,=(FORSZ).2
           CMM  R36,R66          
         WHNZ
         LDM  R34,R2           
         STM  R34,R30          
         ADM  R30,=(FORSZ).2
         LDM  R32,R26          
         SBM  R32,R2           
         SBM  R32,=(FORSZ).2
         ADM  R2,=(FORSZ).2
         STMD R2,=LAVAIL       
         JSB  =COPY            
         DCB  R20              
         LDMD R30,=FWVARS      

NOMORE   ICB  R20              
         IFNC
           LDM  R56,=(FORSZ).2
           STE
           JSB  =RSMEM=          
           REN
           STBD R20,X30,E.FCNT
           PUMD R66,+R26         
           CLM  R50              
           PUMD R50,+R26         
           LDM  R54,=0FFH,1,0,0   
           PUMD R50,+R26         
           RTN                   
         ENDIF
         JSBN  =ERROR+          
         DATA  48D

GETFC    LDMD R30,=FWVARS      
         LDBD R20,X30,E.FCNT
         RTN                   

         DATA 341
NEXT.    BIN                   
         JSB  =GETFC
         JZR  NXERR
         POMD R46,-R12         
         DRP  R30              
         JSB  =GETAD#          
         LDMD R26,=LAVAIL      
         POMD R66,+R26         
         JSB  =FETSVA          
         STM  R30,R36          
         CMM  R34,R36          
         JNZ  NXTST
         JSB  =CKLOOP
         JEN  EXNXT

         BIN                   
         POMD R32,+R26         
         POMD R10,+R26         
         ADMD R10,=RNFILE      
         ADMD R32,=RNFILE      
         JSB  =TRJUMP          
         JSB  =SPY             
         RTN                   

NXTST
         DRP  R36              
         JSB  =PUTADR          
         ARP  !12
         PUMD R46,+R12         
         JSB  =EXNXT
         JMP  NEXT.

NXERR    JSBN  =ERROR+          
         DATA  47D

EXNXT    BIN                   
         JSB  =GETFC
         RZR
         DCB  R#               
         STBD R#,X30,E.FCNT
         LDMD R36,=LAVAIL      
         ADM  R36,=(FORSZ).2
         STMD R36,=LAVAIL      
         RTN                   

         DATA  41
TO.      JSB  =GTFOR
         POMD R#,-R12          
         PUMD R#,+R26          
         LDBD R0,R10           
         JSB  =CREOL?          
         REN
         JMP  CKDON

GTFOR    JSB  =RELMEM          
         LDMD R26,=LAVAIL      
         BIN                   
         POMD R66,+R26         
         JSB  =FETSVA          
         DRP  R50              
         RTN                   

         DATA 41
STEP.    JSB  =GTFOR
         POMD R#,+R26          
         POMD R60,-R12         
         STMD R60,R26          

CKDON    POMD R70,+R26         
         LDMD R36,=PCR         
         SBMD R36,=RNFILE      
         PUMD R36,+R26         
         ADMD R36,=RNFILE      
         SBMD R10,=RNFILE      
         PUMD R10,+R26         
         ADMD R10,=RNFILE      
         SBM  R26,=(12D).2
         JSB  =FNUM            
         BCD                   
         LDM  R40,R60          
         JSB  =CKDONE
         REZ
         BIN                   
         LDMD R26,=LAVAIL      
         POMD R30,+R26         
         LDM  R24,R10          
         LDMD R66,=PCR         
SKPLOP
         POBD R36,+R24         
         CMB  R36,=16          
         JNZ  TSTNXT
         LDMD R36,=PCR         
         JSB  =SKPLN#          
         CMM  R#,R24           
         JNZ  SKPLOP

         JSB  =NXTLIN          
         JEZ  ENDPGM
         JMP  SKPLOP

TSTNXT   CMB  R36,=NXTTOK
         JNZ  SKPLOP
         POMD R75,-R24         
         PUMD R75,+R24         
         CMM  R30,R75          
         JNZ  SKPLOP
         LDMD R76,=PCR         
         STMD R66,=PCR         
         LDM  R10,R24          
         DRP  R76              
         JSB  =TRJUMP          
         JSB  =EXNXT
         BCD                   
         RTN                   

ENDPGM   STMD R66,=PCR         
         JSBN  =ERROR+          
         DATA 46D

MATH2    CLE                   
         CMB  R44,=INTFLG
         JNC  ROI
         CMB  R54,=INTFLG
         RCY

ROI      CLE                   
         PUMD R40,+R12         
         PUMD R50,+R12         
         DCE                   
         RTN                   

CKLOOP   POMD R70,+R26         
         PUMD R70,+R12         
         PUMD R34,+R12         
         PUMD R46,+R12         
         JSB  =FNUM            
         BCD                   
         LDM  R40,R60          
         LDMD R50,R26          
         JSB  =MATH2
         JEZ  ADRR
ADDRR    JSB  =ADD9            
         POMD R40,-R12         
         JMP  ADDR1

ADRR     STM  R45,R75          
         ADM  R45,R55          
         JLZ  ADDR1
         CMB  R47,=90C
         JLZ  ADDR1
         LDM  R45,R75          
         JSB  =ROI
         JMP  ADDRR

ADDR1    POMD R56,-R12         
         STM  R56,R76          
         LDBD R57,=TRFLAG      
         ANM  R56,=30H,1
         IFNZ
           PUMD R76,+R12         
           PUMD R40,+R12         
           PUMD R40,+R6          
           PUMD R26,+R6          
           JSB  =STOSV           
           POMD R26,-R6          
           POMD R40,-R6          
         ELSE
           POMD R36,-R12         
           STMD R40,R36          
         ENDIF
         POMD R50,-R12         

CKDONE   JSB  =MATH2
         JEZ  SUBR
         JSB  =SUBROI          
         POMD R40,-R12         
         JMP  NEXT1

SUBR     STM  R45,R75          
         TCM  R55              
         ADM  R45,R55          
         JLZ  NEXT1
         CMB  R47,=90C
         JLZ  NEXT1
         LDM  R45,R75          
         JSB  =ROI
         JSB  =ADD9            
         POMD R40,-R12         

NEXT1    POMD R50,+R26         
         BCD                   
         LLB  R41              
         LDB  R0,=42           
         CMB  R44,=INTFLG
         JNC  TSTR1
         LDB  R0,=45           
         CLB  R41              
         TSB  R47              
         JLZ  TSTR1
         DCB  R41              
TSTR1
         LLB  R51              
         CMB  R54,=INTFLG
         DRP  R51              
         IFCY
           CLB  R51              
           TSB  R57              
           DRP  R51              
           IFLN
             DCB  R51              
           ENDIF
         ENDIF
         CLE                   
         XRB  R51,R41          
         RNG
         TSM  R*               
         RZR
         ICE                   
         RTN                   
       TITLE 'krlc'
*  __________________________________________________________________
* |KRLC' 256 07/14/82 - 7/19/1982 10:13PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@             @@@@         @@       ||
* ||   @@    @@@   @@@@@@@@@   @@           @@@@@@@@       @@       ||
* ||   @@   @@@    @@     @@@  @@          @@@    @@@      @@       ||
* ||   @@  @@@     @@      @@  @@          @@      @@      @@       ||
* ||   @@ @@@      @@     @@   @@          @@                       ||
* ||   @@@@@       @@@@@@@     @@          @@                       ||
* ||   @@@@@       @@@@@@@     @@          @@                       ||
* ||   @@ @@@      @@    @@@   @@          @@                       ||
* ||   @@  @@@     @@     @@@  @@          @@      @@               ||
* ||   @@   @@@    @@      @@  @@          @@@    @@@               ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@   @@@@@@@@                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@     @@@@                  ||
* ||                                                                ||
* ||                  Last edited on <820813.1411>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
CLRLCD   JSB  =SET             
         VAL  BLANK
         DEF  LCDBUF
         DEF  (LCDBUF)+95D
         JSB  =LCDRST
         LDM  R0,=0,' '
         JSB  =TOLCD
         JSB  =ANNUNS          

CURSE?   LDBD R2,=CURSOR       
         JZR  DECURS           

CURSE    LDB  R2,=TRUE
         STBD R2,=CURSOR       
         SAD                   
         BIN                   
         PUMD R20,+R6          
         JSB  =INWIND
         JSB  =WINDOW
         DRP  !20
         SBBD R20,=MINMIN       
         TCB  R20               
         LDBD R2,=I/RFLG       
         IFZR
           ADB  R20,=BIT#7
         ENDIF
         LDB  R21,R20          
         JSB  =TOLCD
         POMD R20,-R6          
         PAD                   
         RTN                   

DECURS   CLB  R3               
         STBD R3,=CURSOR       
         ICB  R3               
         JMP  TOLCD

WINDOW   LDMD R20,=LCDPTR      
         SBMD R20,=LCDWIN      
         CMMD R20,=SIZSIZ      
         RTN                   

INWIND   JSB  =WINDOW
         RLO
         DRP  !20
         LDMD R20,=LCDPTR       
         SBMD R20,=SIZSIZ       
         ICM  R20               
         STMD R20,=LCDWIN       
         JMP  PUTWN_

IO.ON    CLB  R2               
         STBD R2,=LCDOFF       
PUTWN_   GTO PUTWIN            

IO.OFF   LDB  R2,=TRUE
         STBD R2,=LCDOFF       
         RTN                   

DOSEE    LDB  R2,=TRUE
         JMP  krlc_1

UNSEE    CLB  R2               
krlc_1   STBD R#,=LETSEE       
         RTN                   

LCDRDY   DRP  R2
         LOOP
           LDBD  R#,=LCD
         WHOD
         RTN                   

TOLCD    SAD                   
         JSB  =LCDRDY
         PAD                   
         STMD R#,=LCD
         RTN                   

LCDRST   LDM  R2,=LCDBUF       
         STMD R2,=LCDPTR       
         STMD R2,=LCDWIN       
         RTN                   

ADDR     LDB  R#,='C'
         STBD R#,=CREST        
         RTN                   
       TITLE 'krfs'
*  __________________________________________________________________
* |KRFS 206 04/02/82 - 4/20/1982                                     |
* |==================================================================|
* ||                                                                ||
* ||         @@     @@@  @@@@@@@@    @@@@@@@@@@    @@@@@@           ||
* ||         @@    @@@   @@@@@@@@@   @@@@@@@@@@   @@@@@@@@          ||
* ||         @@   @@@    @@     @@@  @@          @@@    @@@         ||
* ||         @@  @@@     @@      @@  @@          @@      @@         ||
* ||         @@ @@@      @@     @@   @@          @@@                ||
* ||         @@@@@       @@@@@@@     @@@@@@@@@    @@@@@@@           ||
* ||         @@@@@       @@@@@@@     @@@@@@@@@     @@@@@@@          ||
* ||         @@ @@@      @@    @@@   @@                 @@@         ||
* ||         @@  @@@     @@     @@@  @@          @@      @@         ||
* ||         @@   @@@    @@      @@  @@          @@@     @@         ||
* ||         @@    @@@   @@      @@  @@           @@@@@@@@          ||
* ||         @@     @@@  @@      @@  @@            @@@@@@           ||
* ||                                                                ||
* ||                  Last edited on <820908.1331>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
SCANN    BIN                   
         CLM  R54              
         LDBD R46,=USING?      
         IFZR
           CLM  R70              
           LDB  R70,=2           
           RTN                   
         ENDIF
         JSB  =SCANL
         CLM  R66              
         CLM  R70              
         DCB  R71              
         CLM  R54              
         JEN  SCANL1
         JMP  FMTER2
         LOOP
           JSB  =GETREP
SCANL1     JSB  =FCHAR+
           LLM  R36              
           LDMD R36,X36,TYTAB
           JSB  X36,ZRO          
           TSB  R17              
         WHPS
         RTN                   
TYTAB    DEF  IMERR?
         DEF  STRNG
         DEF  ZEE
         DEF  STARR
         DEF  DEE
         DEF  RADX
         DEF  RADXR
         DEF  SIGNF
         DEF  SIGNF
         DEF  SEP
         DEF  SEPS
         DEF  EEE
         DEF  KAA
         DEF  IMERR?


ZEE      LDB  R32,=4           
         TSB  R71              
         JNG  SFILL
         CMB  R71,R32          
         JEQ  SFILL1            
         DCM  R44              
         JNZ  FMTER2             
         ICM  R44              
         CMB  R20,=PERIOD
         JZR  DCFILL           
         CMB  R20,='R'
         JZR  DCFILL             
         JSB  =CKSEP
         JEZ  FMTER2             
         JSB  =DCFILL
         GTO  DONE?
DCFILL   DCB  R71              
         JMP  SFILL1             
SFILL    LDB  R#,R32          
SFILL1   TSB  R72              
         JNZ  FMTER2             
         BCD                   
         ADM  R76,R44          
CHRAD    ADM  R54,R44          
         RTN                   

STARR    LDB  R32,=3           
STAR1    TSB  R71              
         JNG  SFILL
         CMB  R71,R32          
         JZR  SFILL1             
FMTER2   JMP  FMTERR

DEE      LDB  R32,=1           
         TSB  R72              
         JZR  STAR1
         BCD                   
         ADM  R74,R44          
         JMP  CHRAD

RADXR    LDB  R14,=COMMA
RADX     TSB  R72              
         JNZ  FMTERR             
         LDB  R72,R14          
CREP1    BCD                   
         DCM  R44              
         JNZ  FMTERR             
         ICM  R44              
         JMP  CHRAD             

SIGNF    TSB  R70              
         JNZ  FMTERR             
         TSM  R54              
         JNZ  FMTERR             
         CMB  R14,='S'
         DRP  R70              
         IFNE
           ICB  R70              
         ENDIF
         ICB  R70              
         JMP  CREP1

SEPS     JSB  =SEP1
         TCM  R34              
         JMP  SEP2
SEP      JSB  =SEP1
SEP2     PUMD R34,+R12         
         ICM  R66              
         TSM  R76              
         JZR  FMTERR             
         JMP  CREP1
SEP1     PUMD R54,+R6          
         JSB  =ARDON
         LDM  R34,R54          
         POMD R54,-R6          
         BIN                   
         RTN                   

STRNG    TSB  R73              
         JNZ  FMTERR             
         DCB  R73              
         JMP  CHRAD             

EEE      TSB  R73              
         JNZ  FMTERR             
         ICB  R73              
         BCD                   
         DCM  R44              
         JNZ  FMTERR             
         LDB  R44,=5           
         JMP  CHRAD             

KAA      DCB  R70              
         BCD                   
         TSM  R54              
         JNZ  FMTERR             
         DCM  R44              
         JNZ  FMTERR             
         RTN                   

IMERR?   JSB  =CKSEP
         JEZ  CKCLO
         DCM  R44              
         JZR  DONE?
FMTERR   JSBN  =ERROR+          
         DATA 52D

CKCLO    CMB  R20,=CLOSE
         JZR  CLSFND
         LDM  R2,=(TWO).2
         JSB  =IMERR           
         TSM  R2               
         IFPS
           JSB  =ERROR
           DATA 52D
         ENDIF
CKCLOR   DCM  R6               
         DCM  R6               
         RTN                   

CLSFND   DCM  R10              
         ICM  R30              
DONE?    STMD R30,=IMCLEN      
         STMD R10,=IMCADR      
         JSB  =ARDON
         JMP  CKCLOR

LTABL    DATA 'X"()/',"'"
LTABLN   EQU  ($-(LTABL)+1).1

SCANL    LDMD R10,=IMCADR      
         STM  R10,R36          
         LDMD R30,=IMCLEN      
SCANLX   BIN                   
         STMD R36,=IMWADR      
SCNGLO   JSB  =GCHAR#
         JEZ  SCANLS
SCANLR   JSB  =WTEST
         JSB  =GETREP
         LDM  R34,=LTABL
         LDM  R24,=(LTABLN).2
         JSB  =FCHAR
         JEN  PROCHR
SCANLS   JSB  =WTEST
         JSB  =CKSEP
         JEZ  SCLRT+
         JSB  =WTEST
         JMP  SCNGLO

SCLRT+   CLM  R2               
         JSB  =IMERR           
         TSM  R2               
         JNG  SCANLR
         ICE                   
         RTN                   

FMTER4   JMP  FMTERR             

WTEST    CLE                   
         BIN                   
         TSM  R30              
         RPS
         LDMD R2,=IMWADR       
         CMMD R2,=IMSADR       
         RNE
         JMP  CKCLOR
PROCHR   LLM  R36              
         LDMD R36,X36,LJTAB
         JSB  X36,ZRO          
         TSB  R17              
         JPS  SCANLR
         RTN                   
LJTAB    DEF  FMTERR
         DEF  EX
         DEF  QLIT
         DEF  LTBRAC
         DEF  RTBRAC
         DEF  SENDCR
         DEF  QLIT

RTBRAC   LDBD R65,=USING?      
         JPS  FMTER4
         PUMD R52,+R6          
         POMD R52,-R12         
         BCD                   
         DCM  R56              
         BIN                   
         JNZ  RSET
         DCB  R65              
RTBREX   STBD R#,=USING?      
RTBRX1   POMD R52,-R6          
         RTN                   
RSET     PUMD R52,+R12         
         LDM  R30,R54          
         LDM  R10,R52          
         JSB  =GCHAR#
         JMP  RTBRX1

LTBRAC   PUMD R52,+R6          
         DCM  R10              
         STM  R10,R52          
         ICM  R10              
         LDM  R54,R30          
         ICM  R54              
         LDM  R56,R44          
         PUMD R52,+R12         
         CMMD R12,=LAVAIL      
         JCY  LTBOUT
         LDBD R65,=USING?      
         ICB  R65              
         JNZ  RTBREX

LTBOUT   POMD R52,-R6          
FMTER3   JMP  FMTER4

QLIT     LDM  R26,R10          
         DCM  R26              
QLCON    CMB  R20,R14          
         JZR  QMOV
         JSB  =GCHAR-
         JEZ  FMTER3
         JMP  QLCON

QMOV     LDM  R22,R10          
         SBM  R22,R26          
         DCM  R22              
         STM  R22,R54          
         CLM  R56              
         JSB  =GCHAR#
SPECOT   LDM  R36,R54          
         PUMD R20,+R6          
         LDB  R20,=1           
         JSB  =PRNFMT          
         POMD R20,-R6          
         RTN                   

EX       LDM  R55,R44          
         LDB  R54,=377         
         PUMD R50,+R12         
         JSB  =ONEB            
         CLM  R54              
         STM  R46,R54          
         CLM  R76              
         JSB  =RESFIL          
         REN
         JMP  SPECOT

SENDCR
         LOOP
           JSB  =LINEND
           BCD                   
           DCM  R44              
         WHNZ
         RTN                   

CTABL    DATA "AZ*D.RSMCPEK"
CTABLN   EQU  ($-(CTABL)+1).1
FCHAR+   LDM  R34,=CTABL
         LDM  R24,=(CTABLN).2
FCHAR    BIN                   
         CLE                   
         CLM  R36              
         TSM  R30              
         RNG
         STB  R20,R14          
         CMB  R20,=COMMA
         REQ
         JSB  =IDCHAR
         REZ
         JSB  =GCHAR-
         JEZ  FCRT1
         CMB  R14,='('
         REQ
         CMB  R14,=')'          
         REQ
*        DRP  ?14
         JSB  =QUIP?           
         REQ
         CMB  R20,=BLANK
         IFEQ
TSTRP      JSB  =GCHAR#
           JEZ  FCRT1
         ENDIF
         CMB  R14,R20          
         RNE
         BCD                   
         ICM  R44              
         TSM  R46              
         IFNZ
           DCM  R44              
         ENDIF
         JMP  TSTRP

FCRT1    ICE                   
         BIN                   
         RTN                   

GETREP   CLM  R44              
GLOP     BCD                   
         JSB  =DIGIT           
         JEZ  GLOPT
         TSB  R45              
         IFLZ
           ERB  R20              
           ELM  R44              
         ENDIF
         JSB  =GCHAR#
         JMP  GLOP

GLOPT    TSM  R44              
         IFZR
           ICM  R44              
         ENDIF
         BIN                   
         RTN                   

IDCHAR   CLE                   
         CLM  R36              
         LOOP
           ICM  R36              
           CMM  R36,R24          
           REQ
           POBD R32,+R34         
           CMB  R32,R14          
         WHNE
         ICE                   
         RTN                   

GCHAR#   LOOP
           JSB  =GCHAR-
           REZ
           CMB  R#,=BLANK
         WHEQ
         RTN                   

GCHAR-   BIN                   
         CLE                   
         DCM  R30              
         RNG
         POBD R20,+R10         
         JSB  =ALFA#           
         JMP  RTNE=1

CKSEP    BIN                   
         TSM  R30              
         JPS  CKRST
         LDMD R30,=IMSLEN      
         LDMD R10,=IMSADR      
RTNE=1
CKINC    STE
         RTN                   

CKRTN    CLM  R2               
         ICM  R2               
         JSB  =IMERR           
         TSM  R2               
         JNG  CKINC
         CLE                   
         RTN                   

CKRST    CMB  R20,=COMMA
         JZR  CKINC
         CMB  R20,=SLASH
         JNZ  CKRTN
         DCM  R10              
         ICM  R30              
         JMP  CKINC
       TITLE 'krff'
*  __________________________________________________________________
* |KRFF 178 04/02/82 - 4/20/1982                                     |
* |==================================================================|
* ||                                                                ||
* ||         @@     @@@  @@@@@@@@    @@@@@@@@@@  @@@@@@@@@@         ||
* ||         @@    @@@   @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@@         ||
* ||         @@   @@@    @@     @@@  @@          @@                 ||
* ||         @@  @@@     @@      @@  @@          @@                 ||
* ||         @@ @@@      @@     @@   @@          @@                 ||
* ||         @@@@@       @@@@@@@     @@@@@@@@@   @@@@@@@@@          ||
* ||         @@@@@       @@@@@@@     @@@@@@@@@   @@@@@@@@@          ||
* ||         @@ @@@      @@    @@@   @@          @@                 ||
* ||         @@  @@@     @@     @@@  @@          @@                 ||
* ||         @@   @@@    @@      @@  @@          @@                 ||
* ||         @@    @@@   @@      @@  @@          @@                 ||
* ||         @@     @@@  @@      @@  @@          @@                 ||
* ||                                                                ||
* ||                  Last edited on <820908.1331>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
CVNUM    LDB  R70,=377         
         STM  R30,R26          
         JSB  =ARITH

FORMN+   LDM  R56,R54          
         JSB  =BLKFIL          
         CLM  R66              
FORMN
         BCD                   
         PUMD R54,+R6          
         PUMD R24,+R6          
         PUMD R66,+R6          
         JSB  =SEP10           
         JSB  =ROUND           
         TSB  R73              
         IFZR
           JSB  =INFR4           
           LDM  R36,R34          
         ENDIF
         LDM  R30,R26          
         POMD R66,-R6          
         JSB  =OUTC/P
         JSB  =SIGNN
         JSB  =LDIGIT
         JSB  =RADIX
         JSB  =RDIGIT
         JSB  =EFORM           
         POMD R24,-R6          
         BIN                   
         POMD R54,-R6          
         CLM  R74              
         LDB  R74,R2           
         SBM  R54,R74          
         RTN                   

ARITH    LDB  R71,=4           
         CLM  R72              
         LDB  R72,=PERIOD
         LDM  R36,R40          
         STM  R36,R34          
         BCD                   
         LRB  R37              
         LDM  R62,R42          
         JNZ  TSEXP
         ICM  R76              
         JMP  INT?
TSEXP    CMB  R37,=5           
         JPS  NGEXP
         CMM  R36,=12C,0
         JPS  NR3
         LDB  R76,R36          
         ICM  R76              
NR12     JSB  =CHRRT
INT?     LDM  R36,R74          
         IFZR
           CLB  R72              
         ENDIF
SETCNT   LDM  R56,R74          
         ADM  R56,R76          
         TSB  R70              
         JNG  INCS?
         JNZ  INCS
INCS?    TSB  R41              
         JRZ  NOINCS
INCS     ICM  R56              
NOINCS   TSB  R72              
         IFNZ
           ICM  R56              
         ENDIF
         TSB  R73              
         IFNZ
           ADM  R56,=5,0
         ENDIF
         STM  R56,R54          
         CLM  R56              
ARDON    PUMD R70,+R6          
         PUMD R66,+R6          
         CLM  R60              
         LDB  R60,=7           
         LDM  R64,R54          
         JSB  =CONINT          
         CLM  R54              
         STM  R76,R54          
         POMD R66,-R6          
         POMD R70,-R6          
         RTN                   
NR3      LDM  R62,R42          
         ICM  R76              
         JSB  =CHRRT
         LDB  R73,=2           
         JMP  SETCNT
NGEXP    NCM  R36              
         ANM  R37,=17          
         TSM  R36              
NVAGN    JZR  NR12
         LRM  R67              
         TSB  R61              
         JLN  NR3
         DCM  R36              
         JMP  NVAGN
CHRRT    LDM  R34,=12C,0
         SBM  R34,R76          
         JZR  CHRTEX
SHFAGN   TSB  R62              
         JRN  CHRTEX
         LRM  R67              
         DCM  R34              
         JNZ  SHFAGN
CHRTEX   STM  R34,R74          
         RTN                   

OUTC/P   TSM  R66              
         RZR
         BIN                   
         LOOP
           LDB  R34,=COMMA
           POMD R24,-R12         
           IFNG
             TCM  R24              
             LDB  R34,=PERIOD
           ENDIF
           ADM  R24,R26          
           PUBD R34,+R24         
           DCM  R66              
         WHNZ
         BCD                   
         RTN                   

LDIGIT   TSB  R73              
         DRP  R50              
         IFNZ
           LDM  R50,R40          
         ENDIF
         TSM  R50              
         IFNZ
           IFLZ
             LOOP
               LLM  R#             
             WHLZ
           ENDIF
         ENDIF
         LDM  R34,R76          
         TSB  R73              
         DRP  R36              
         IFNZ
           SBM  R36,R76          
           JMP  OUTE
         ENDIF
         STM  R36,R24          
         DRP  R34              
         IFLZ
           SBM  R34,R24          
           DCM  R34              
         ENDIF
         TSM  R34              
         JNG  OVFLO
         JZR  SETFIL
         JSB  =FILL
         TSM  R72              
         JZR  LDEXIT
         LDBD R23,R30          
         CMB  R23,=' '         
         IFNZ
           CMB  R22,=60          
           IFZR
             LDB  R22,R23          
           ENDIF
           PUBD R22,+R30         
         ENDIF
SETFIL   CMB  R71,=2           
         IFNC
           JSB  =SIGNFF
         ENDIF
         LDB  R71,=4           
         LDM  R34,R36          
         JLN  LDEXIT
         CMM  R34,=12C,0
         JPS  OUTMO
OUTE     ICM  R#              
         TSM  R34              
         JZR  LDEXIT
         JLN  OVFLO
         JSB  =OUTDIG
         JMP  LDEXIT
OUTMO    LDM  R#,=12C,0          
         JSB  =OUTDIG
         LDM  R34,R36          
         ICM  R34              
         SBM  R34,=12C,0
         JSB  =FILL
LDEXIT   TSB  R73              
         RNZ
         LDM  R50,R40          
         RTN                   

OVFLO    CLM  R73              
         JSBN  =ERROR+          
         DATA  2

OUTDIG   LOOP
           LLM  R50              
           CLB  R22              
           ELB  R22              
           BIN                   
           ADB  R22,='0'
           BCD                   
           JSB  =OUT1
         WHNZ
         RTN                   

FILL     LDB  R22,=BLANK
         CMB  R71,=2           
         IFPS
           LDB  R22,='*'
           CMB  R71,=4           
           IFPS
             LDB  R22,='0'
           ENDIF
         ENDIF
         LOOP
           DCM  R76              
           IFZR
             TSB  R71              
             IFEV
               LDB  R22,='0'       
             ENDIF
           ENDIF
           JSB  =OUT1
         WHNZ
         RTN                   

OUT1     LDB  R0,=22           
         LDBD R23,R30          
         CMB  R23,=BLANK
         JZR  OUT1X
         ICM  R34              
         BIN                   
         CMB  R22,=BLANK
         IFNE
           CMB  R22,=STAR
           IFNE
             LDB  R0,=23           
           ENDIF
         ENDIF
         BCD                   
         JSB  =OUT1X
         JMP  OUT1
OUT1X    PUBD R*,+R30          
         DCM  R34              
         RTN                   

SIGNFF   JSB  =SIGNX
         POMD R24,-R30         
         BIN                   
         CMM  R30,R26          
         IFCY
           CMB  R24,='0'
           IFEQ
             STB  R25,R24          
             LDB  R25,='0'
           ENDIF
         ENDIF
         PUMD R24,+R30         
         CMM  R76,=2,0
         IFCY
           LDB  R24,=BLANK
           CMBD R24,R30          
           IFNE
             POBD R25,-R30         
             PUMD R24,+R30         
           ENDIF
         ENDIF
         BCD                   
         RTN                   

SIGNN    TSB  R32              
         IFRN
           TSB  R70              
           IFZR
             DCM  R76              
           ENDIF
         ENDIF
         TSB  R73              
         JNZ  SIGNX
         TSB  R71              
         JNG  SIGNX
         CMB  R71,=2           
         RNC
SIGNX    LDB  R34,=MINUS
         TSB  R32              
         IFRZ
           LDB  R34,=PLUS
           BIN                   
           DCB  R70              
           BCD                   
           RNG
           IFNZ
             LDB  R34,=BLANK
           ENDIF
         ENDIF
         PUBD R34,+R30         
         RTN                   

RADIX    TSB  R72              
         IFNZ
           PUBD R72,+R30         
         ENDIF
         RTN                   

RDIGIT   LDB  R71,=4           
         LDM  R76,R74          
         RZR
         TSB  R73              
         JNZ  RDLP1
         LDM  R34,R36          
         JLZ  RDLP1
         NCM  R34              
         CMM  R34,R76          
         IFCY
           LDM  R34,R76          
         ENDIF
         TSM  R34              
         IFNZ
           JSB  =FILL
         ENDIF
RDLP1    LDM  R34,R76          
         IFNZ
           JSB  =OUTDIG
         ENDIF
         RTN                   
       TITLE 'krvr4'
*  __________________________________________________________________
* |KXVR4 NA                                                          |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@      @@  @@@@@@@@          @@     ||
* ||   @@    @@@   @@      @@  @@      @@  @@@@@@@@@        @@@     ||
* ||   @@   @@@    @@@    @@@  @@      @@  @@     @@@      @@@@     ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@      @@     @@@@@     ||
* ||   @@ @@@         @@@@      @@    @@   @@     @@     @@@ @@     ||
* ||   @@@@@           @@       @@    @@   @@@@@@@      @@@  @@     ||
* ||   @@@@@           @@       @@    @@   @@@@@@@     @@@   @@     ||
* ||   @@ @@@         @@@@       @@  @@    @@    @@@   @@@@@@@@@@   ||
* ||   @@  @@@      @@@  @@@      @@@@     @@     @@@  @@@@@@@@@@   ||
* ||   @@   @@@    @@@    @@@     @@@@     @@      @@        @@     ||
* ||   @@    @@@   @@      @@      @@      @@      @@        @@     ||
* ||   @@     @@@  @@      @@      @@      @@      @@        @@     ||
* ||                                                                ||
* ||                                                                ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* Version code for BASROM: 'd'
* ********************************************************************
VERMN4   DATA  'd'              
       TITLE 'krsum'
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

* ********************************************************************
* CHECKSUM for BASROM
* ********************************************************************
         DATA   036H             
       TITLE 'krcrd'
CRDRD    EQU 7H
CRDWR    EQU 6H
WRPTCT   EQU 0FFH
WRPWSZ   EQU 2H
WRPRSZ   EQU 5H
FLHDSZ   EQU 23H
HPHDSZ   EQU 8H
CRDSIZ   EQU 28AH
CRDERR   EQU  70H
CRDLO    EQU  20H
CRDSTP   EQU  0FBH
CRDEOJ   EQU  7FH
CRDON    EQU 200H
CRDOFF   EQU 0H
ENABL    EQU 2H
RWEND    EQU  0F4H
S20-67   EQU  0D810H
*  __________________________________________________________________
* |KRCRD 91 06/24/82 - 7/12/1982 4:57PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@       @@@@     @@@@@@@@    @@@@@@       ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@   @@@@@@@@@   @@@@@@@@     ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@     @@@  @@    @@@    ||
* ||   @@  @@@     @@      @@  @@      @@  @@      @@  @@      @@   ||
* ||   @@ @@@      @@     @@   @@          @@     @@   @@      @@   ||
* ||   @@@@@       @@@@@@@     @@          @@@@@@@     @@      @@   ||
* ||   @@@@@       @@@@@@@     @@          @@@@@@@     @@      @@   ||
* ||   @@ @@@      @@    @@@   @@          @@    @@@   @@      @@   ||
* ||   @@  @@@     @@     @@@  @@      @@  @@     @@@  @@      @@   ||
* ||   @@   @@@    @@      @@  @@@    @@@  @@      @@  @@    @@@    ||
* ||   @@    @@@   @@      @@   @@@@@@@@   @@      @@  @@@@@@@@     ||
* ||   @@     @@@  @@      @@     @@@@     @@      @@  @@@@@@       ||
* ||                                                                ||
* ||    Finished on 06/01/82  Raan  Last edited on <820908.1342>    ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
HPHDVL   DATA  'HPCV'           
         DEF  (CRDSIZ)+50D
         DEF  ZRO              
MSG1     DATA 21D
         DATA ' card:  Align & [RTN]'
MSG1.L   DATA 9D
         DATA 'Copy from'
MSG1.S   DATA 7D
         DATA 'Copy to'
MSG1.P   DATA 7D
         DATA 'Protect'
MSG1.U   DATA 9D
         DATA 'Unprotect'
MSG1.X   DATA 7D
         DATA 'Catalog'
MSG1.V   DATA 6D
         DATA 'Verify'
MSG1A    DATA 13D
         DATA 'Pull card ...'
MSG2     DATA 7D
         DATA 30D
         DATA 'Track '
MSG2A    DATA 20D
         DATA ' done; insert track '
MSG3     DATA 25D
         DATA 8D
         DATA ' (track '
MSG3A    DATA 4D
         DATA ' of '
MSG4     DATA 16D
         DATA ' track(s) needed'

         DATA 241
CRDUPR   DRP  !20
         CLM  R20               
         LDM  R32,=MSG1.U
         JMP  WRPCNT
         
         DATA 241
CRDWPR   DRP  !20
         LDM  R20,=(WRPTCT).2
         LDM  R32,=MSG1.P

WRPCNT   STMD R20,=WRTPRO      
         JSB  =STRTUP
WRPTRY   STMD R4,=RTNSVE       
         LDM  R26,R32          
         JSB  =STRTCD
         LDM  R20,=(WRPWSZ).2
         LDM  R22,=WRTPRO      
         JSB  =WRITCR
         JSB  =INTENA
         JSBN  =ENDIT

         DATA 241
CRDEXM   JSB  =STRTUP
EXMTRY   STMD R4,=RTNSVE       
         LDM  R26,=MSG1.X
         JSB  =GOCARD
         JSB  =READCR
         JSB  =HEDSUM
         CMBD R47,=HDCKSM      
         IFNZ
            GTO GENERR
         ENDIF
         JSB  =INTENA
         JSB  =FRMCHK
         JSB  =EXMMSG
         LDM  R30,=TRKSZE      
         JSB  =CATLIN          
         JSB  =SIGNIF          

         JSBN  =ENDIT

CRDCPY   CMB  R34,='C'
         JLO  LOADIT
         JEQ  STORE
PRIVTE
         LDM  R30,R56          
         JSB  =MKEPRV
         JSB  =STORE
         STMD R30,X56,DR.TYP
         RTN                   

LOADIT   JSB  =LOAD
         CMB  R24,='P'
         RNE
         LDBD R30,=ABTFLG      
         RNZ
         LDM  R30,R66          

MKEPRV   LDMD R0,X30,DR.TYP
         STM  R0,R30           
         CLE                   
         CMM  R0,=TYBASC       
         IFNE
           JSB  =WARN            
           DATA 68D
         ELSE
           ANM  R0,=(0FF00H+0FFH-(TYPRI?)).2
           STMD R0,R2            
         ENDIF
         RTN                   

STORE    JSB  =STRTUP
         LDM  R74,R70          
         LDMD R30,R56          
         LDB  R70,=1           
         CLB  R71              
         JSB  =HEDBLD
         JSB  =SZEMSG
         LDMD R40,X56,DR.NAM
         CMM  R40,R60          
         IFNZ
           JSB  =SYSJSB          
           DEF  CRTMDT
           STMD R44,=TMEDTE      
         ENDIF
WRTRY    STMD R4,=RTNSVE       
         STBD R70,=FLHEAD      
         LDMD R14,=FLHEAD      
         CMB  R14,R15          
         IFZR
           LDMD R14,=LSTTRK      
         ELSE
           LDMD R14,=FULTRK      
         ENDIF
         STMD R14,=TRKSZE      
         LDM  R22,R30          
         JSB  =DTACLC
         JSB  =DTASUM
         STMD R46,=CHKSUM      
         CMB  R70,R71          
         IFNE
           STB  R70,R71          
           LDM  R14,R32          
           ADMD R14,=TRKSZE      
           LDMD R2,=PRTNXT       
           STMD R2,=PRT1ST       
           ADM  R32,R2           
           LOOP
             JSB  =SKPLN#          
             DRP  !32
             CMM  R32,R14           
           WHNC
           SBM  R32,R14           
           STMD R32,=PRTNXT       
           LDM  R32,R22           
         ENDIF
         JSB  =HEDSUM
         STBD R47,=HDCKSM      
         LDM  R26,=MSG1.S
         JSB  =GOCARD
         LDMD R14,=WRTPRO      
         IFNZ
           LDB  R36,=19D
           JMP  STRABT
         ENDIF
         JSB  =WRITCR
         LDMD R20,=TRKSZE      
         LDM  R22,R32          
         JSB  =WRITCR
         JSB  =INTENA
         LDBD R14,=CRDSTS      
         IFOD
           JSB  =VERIFY
           IFEN
             LDB  R36,=21D          
STRABT       GTO  ABORT
           ENDIF
           JSB  =INTENA
         ENDIF
         LDMD R14,=FLHEAD      
         CMB  R14,R15          
         IFCY
           JSBN  =ENDIT
         ENDIF
         ICB  R70              
         CLE                   
         JSB  =TRKMSG
         GTO WRTRY

LOAD     JSB  =STRTUP
         LDB  R73,R33          
         STM  R66,R60          
         LDMD R30,R60          
         JSB  =ALCALL          
         IFEN
           GTO ABTHRD
         ENDIF
         LDB  R40,=1           
         LDM  R14,=TMRBUF      
         ICM  R14              
         LOOP
           PUBD R40,+R14         
           CMM  R14,=SUBPNT      
         WHNC
         CLB  R70              
RDTRY    STMD R4,=RTNSVE       
         LDM  R26,=MSG1.L
         JSB  =GOCARD
         JSB  =READCR
         JSB  =CHKHED
         LDM  R22,R30          
         JSB  =DTACLC
         JSB  =READCR
         JSB  =CHKEND1          
         JSB  =INTENA
         LDMD R14,=FLHEAD      
         CMB  R15,R70          
         IFNC
           JSB  =CRTFLE
           JSBN  =ENDIT
         ENDIF
         STE
         JSB  =TRKMSG
         JMP  RDTRY

VERIFY   LDMD R34,=SUBPNT      
         STMD R6,=SUBPNT       
VFYTRY   STMD R4,=RTNSVE       
         LDM  R26,=MSG1.V
         JSB  =GOCARD
         LDM  R22,=TMPMM2      
         JSB  =READCR
         CLE                   
         JSB  =VYHDSM
         CMBD R47,=HDCKSM      
         JNZ  VFYFAL
         LDMD R20,=(TMPMM2)+3
         JSB  =RDVFY
         CLE                   
         CMMD R46,=CHKSUM      
         IFNZ
VFYFAL     ICE                   
         ENDIF
VFYDNE   STMD R34,=SUBPNT      
         LDM  R14,=WRTRY
         STMD R14,=RTNSVE      
         RTN                   

GOCARD   JSB  =STRTCD
         LDM  R20,=(WRPRSZ).2
         LDM  R22,=WRTPRO      
         JSB  =READCR
         LDM  R20,=(FLHDSZ).2
         LDM  R22,=SUBFRM      
         RTN                   

STRTCD   CLB  R14              
         STBD R14,=ABTFLG      
         JSB  =HLFOUT          
         LDM  R26,=MSG1
         JSB  =MSSOUT          
         LOOP
           JSB  =SIGNIF          
           CMB  R2,=ATTNKY
           JZR  ABTHRD
           CMB  R2,=NAPKEY
           JZR  ABTHRD
           JSB  =DEQUE           
           CMB  R2,=CR
         WHNZ
         LDMD R43,=DELAY       
         PUMD R43,+R6          
         CLM  R43              
         STMD R43,=DELAY       
         LDM  R26,=MSG1A
         JSB  =MSSOUT          
         JSB  =UNSEE
         POMD R43,-R6          
         STMD R43,=DELAY       
         JSB  =INTDSA
         LDM  R20,=(HPHDSZ).2
         LDM  R22,=HPHEAD      
         JSB  =READCR
         JSB  =PWROK?          
         JEN  ABTHRD
         LDMD R40,=HPHEAD      
         CMMD R40,=HPHDVL      
         JMP  DOINTC

FRMCHK   CLM  R40              
         LDBD R47,=SUBFRM      

DOINTC   JSB  =HPINTC          
         RZR

FRMERR   LDB  R36,=22D         
ABRTIT   GTO  ABORT

ABTHRD   LDB  R14,=1           
         STBD R14,=ABTFLG      
         JMP  GENERR

READIT   LDB  R15,=CRDRD
         STE
         JMP  RDWRIT

WRITIT   LDB  R15,=CRDWR
         CLE                   

RDWRIT   DCM  R20              
         STM  R20,R24          
         ADM  R20,R22          
         DCM  R24              
         IFEZ
           ADM  R24,=(6D).2
         ENDIF
         ADM  R24,R22          
         CLB  R14              
         RTN                   

READCR   JSB  =READIT
         JMP  RDWRCR

WRITCR   JSB  =WRITIT

RDWRCR   JSB  =GETBYT
         JMP  GORDWR

ERRS     ANM  R15,=CRDERR
         CMB  R15,=CRDLO
         IFNZ
           IFCY
GENERR       LDB  R36,=23D
             LDMD R14,=RTNSVE      
             CMM  R14,=VFYTRY
             JNZ  ABRTIT
             JSB  =VFYDNE
             LDB  R36,=21D          
             JMP  ABRTIT
           ENDIF
           LDB  R36,=24D
           JMP  ABRTIT
         ENDIF
         LDB  R36,=25D
         JMP  ABRTIT

NXTBYT   CMM  R24,R22          
         IFNC
           ANM  R15,=CRDSTP
         ENDIF
GETBYT   STMD R14,=CRDRDR
         LOOP
           DCM  R65              
           JNG  GENERR
           LDMD R14,=CRDRDR
         WHPS
         LDMD R14,=CRDRDR
         CLM  R65              
         LDB  R66,=4H          
         ANM  R15,=CRDEOJ
         LDB  R3,=RWEND
         ANM  R3,R15           
         IFEZ
           RRZ
         ENDIF
         JLN  ERRS
         RTN                   

RWREAL   IFEN
           PUBD R14,+R22         
         ELSE
           POBD R14,+R22         
         ENDIF
         LOOP
           TSB  R3               
           RRZ
           JSB  =NXTBYT
GORDWR     CMM  R20,R22          
           JCY  RWREAL
           ICM  R22              
           CLB  R14              
         WHMP

RDVFY    JSB  =READIT
         CLM  R46              
         JSB  =GETBYT
         JMP  VFCNT-

         LOOP
           JSB  =NXTBYT
VFCNT-     ICM  R22              
           CLM  R20              
           LDB  R20,R14          
           TSB  R3               
           IFRN
             JSB  =NXTBYT
             ICM  R22              
             LDB  R21,R14          
           ENDIF
           ADM  R46,R20          
           IFCY
             ICM  R46              
           ENDIF
           TSB  R3               
         WHRN
         RTN                   

NUMOUT   JSB  =TOBCD2          
         JSB  =TOASC2          
         CMB  R20,='0'
         IFZR
           LDB  R20,=' '
         ENDIF
         PUMD R20,+R22         
         RTN                   

STRTUP   POMD R14,-R6          
         JSB  =EVIL            
           DEF S20-67
         STMD R6,=SUBPNT       
         LDB  R2,=1            
         STBD R2,=NOCHEK       
         PUMD R14,+R6          
         RTN                   

ENDIT    POMD R14,-R6          
         JSB  =BLEBUF          
         CLB  R2               
         STBD R2,=NOCHEK       
         RTN                   

INTDSA   LDM  R14,=CRDON
         STMD R14,=CRDRDR
         STBD R14,=KEYSTS
         STBD R14,=IOINTC
         JSB  =CMPDSA          
         CLM  R65              
         LDB  R67,=2H          
         RTN                   

INTENA   LDM  R14,=(CRDOFF).2
         STMD R14,=CRDRDR
         LDB  R14,=ENABL           
         STBD R14,=KEYSTS
         LDBD R14,=PILINT      
         STBD R14,=IOINTC
         JSB  =CMPENA          
         RTN                   

DTACLC   LDMD R20,=TRKSZE      
         LDBD R14,=FLHEAD      
         LDMD R32,=FULTRK      
         LOOP
           DCB  R14              
           JZR  DTAEND
           ADM  R22,R32          
         WHMP

DTAEND   STM  R22,R32          
         RTN                   

CRTFLE   LDMD R14,=FILTYP      
         STMD R14,X60,DR.TYP
         LDMD R40,X60,DR.NAM
         LDMD R50,=FILNME      
         CMM  R50,R40          
         IFZR
           LDMD R54,=TMEDTE      
           STMD R54,X60,DR.DAT
         ENDIF
         ADMD R30,=FILSZE      
         LDMD R32,X60,DR.SIZ
         SBMD R32,=FILSZE      
         JSB  =DELETE          
         RTN                   

VYHDSM   LDM  R14,=TMPMM2      
         JMP  CPHDSM
HEDSUM   LDM  R14,=SUBFRM      

CPHDSM   LDM  R0,=(34D).2
         JSB  =SUMIT
         ADB  R47,R46          
         RTN                   

CHKHED   JSB  =HEDSUM
         CMBD R47,=HDCKSM      
         JNZ  SUMERR
         JSB  =FRMCHK           
         TSB  R70              
         IFZR
           CMMD R50,=BLANKS      
           IFNZ
             CMMD R50,=FILNME      
             IFNZ
               LDB  R36,=26D
               JMP  CHKABS
             ENDIF
           ENDIF
           CMMD R74,=PASWRD      
           IFNZ
             LDB  R20,=66D
             JMP  CHKERR
           ENDIF
           CMMD R32,=FILSZE      
           IFNC
             LDB  R20,=16D
             JMP  CHKERR
           ENDIF
           ICB  R73              
           IFNZ
             DCB  R73              
             CMBD R73,=(FILTYP)+1
             JZR  GETCHK
             LDB  R20,=68D
CHKERR       JSB  =ERRORR          
             GTO  ABTHRD
           ENDIF
           DCB  R#               
GETCHK     LDMD R34,=FLECHK      
         ENDIF
         CMMD R34,=FLECHK      
         RZR
         LDB  R36,=20D          
CHKABS   GTO  ABORT


CHKEND1  JSB  =DTASUM
         CMMD R46,=CHKSUM      
         IFNZ
SUMERR     GTO  GENERR
         ENDIF
         CLM  R14              
         LDBD R14,=FLHEAD      
         CLB  R40              
         STBD R40,X14,TRKTBL
         CLM  R14              
         LOOP
           ICM  R14              
           LDBD R40,X14,TRKTBL
         WHZR
         LDB  R70,R14          
         RTN                   

DTASUM   LDMD R0,=TRKSZE       
         LDM  R14,R32          
SUMIT    ADM  R0,R14           
SUMIT+   CLM  R46              
SUMIT-   LOOP
           POMD R2,+R14          
           CMM  R0,R14           
           IFNC
             CLB  R3               
           ENDIF
           ADM  R46,R2           
           IFCY
             ICM  R46              
           ENDIF
           CMM  R14,R0           
         WHNC
         RTN                   

HEDBLD   LDMD R40,X56,DR.SIZ
         STMD R40,=FILSZE      
         LDM  R34,R40          
         STM  R34,R0           
         STMD R60,=FILNME      
         STMD R74,=PASWRD      
         CLM  R43              
         STBD R43,=SUBFRM      
         LDM  R46,=(PCBLEN).2
         STMD R43,=PRTSTS      
         LDMD R14,R56          
         JSB  =SUMIT
         LDM  R0,=(DRENSZ).2
         LDM  R14,R56          
         ICM  R14              
         ICM  R14              
         JSB  =SUMIT-
         STMD R46,=FLECHK      
         CLM  R14              
         LOOP
           ICB  R15              
           SBMD R34,=FULTRK      
           JZR  krcrd_1
         WHCY
krcrd_1  DRP  !34
         ADMD R34,=FULTRK      
         STMD R34,=LSTTRK      
         STMD R14,=FLHEAD      
         RTN                   

SZEMSG   LDM  R22,=TMPMM2      
         LDB  R14,=18D
         PUBD R14,+R22         
         LDBD R20,=(FLHEAD)+1
         JSB  =NUMOUT
         DRP  !20
         LDM  R20,=MSG4
         JSB  =MVBYTS
         JMP  FINMSG

EXMMSG   LDM  R20,=MSG3
         LDM  R22,=TMPMM2      
         POBD R25,+R20         
         PUBD R25,+R22         
         LDMD R40,=FILNME      
         PUMD R40,+R22         
         JSB  =MVBYTS          
         LDBD R20,=FLHEAD      
         JSB  =NUMOUT
         DRP  !20
         LDM  R20,=MSG3A
         JSB  =MVBYTS
         LDBD R20,=(FLHEAD)+1
         JSB  =NUMOUT
         LDB  R25,=')'          
         PUBD R25,+R22         

FINMSG   LDM  R26,=TMPMM2      
         JSB  =EROUT-          
         RTN                   

TRKMSG   JSB  =HANDI0          
           VAL  V.CARD
         LDM  R20,=MSG2
         JSB  =MOVEIT          
         LDBD R20,=FLHEAD      
         JSB  =NUMOUT
         DRP  !20
         LDM  R20,=MSG2A
         JSB  =MVBYTS
         LDB  R20,R70          
         JSB  =NUMOUT
         JMP  FINMSG

ABORT    LDMD R6,=SUBPNT       
         JSB  =INTENA
         LDMD R14,=RTNSVE      
         LDBD R2,=ABTFLG       
         IFZR
           PUMD R14,+R6          
           CLB  R37              
           JSB  =WARN.R          
           RTN                   
         ENDIF
         CMM  R14,=RDTRY
         IFZR
           LDMD R40,X60,DR.NAM
           JSB  =FPURGE          
         ENDIF
         JSB  =ENDIT
       TITLE 'krfun'
*  __________________________________________________________________
* |KXFUN 213 09/27/82 - 12/13/1982 2:06PM                            |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@@@  @@      @@  @@      @@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@@@  @@      @@  @@      @@   ||
* ||   @@   @@@    @@@    @@@  @@          @@      @@  @@@     @@   ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@@@    @@   ||
* ||   @@ @@@         @@@@     @@          @@      @@  @@ @@   @@   ||
* ||   @@@@@           @@      @@@@@@@@@   @@      @@  @@  @@  @@   ||
* ||   @@@@@           @@      @@@@@@@@@   @@      @@  @@  @@  @@   ||
* ||   @@ @@@         @@@@     @@          @@      @@  @@   @@ @@   ||
* ||   @@  @@@      @@@  @@@   @@          @@      @@  @@    @@@@   ||
* ||   @@   @@@    @@@    @@@  @@          @@@    @@@  @@     @@@   ||
* ||   @@    @@@   @@      @@  @@           @@@@@@@@   @@      @@   ||
* ||   @@     @@@  @@      @@  @@            @@@@@@    @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <821213.1404>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
         DATA  0,56             
VER.     JSB   =MELJSB
           DEF VERB
         RTN
         DATA  241
MRGIN.   JSB  =SYSJSB
           DEF MARGN.
         RTN

FXRENU   BIN
         DRP  !76
         SBMD R76,=RNFILE
         JSB  =PTRALO
         ADMD R76,=RNFILE
         BCD
         RTN
gap013   nop
         nop
         nop
         nop
         nop
         nop
         nop
         nop
         nop
         nop
         nop
         nop

VERSUB   LDBD  R#,=VERMN3
         PUBD  R#,+R#
         RTN
RESPUT
         JSB  =RSMEM-          
         REN
         PUMD R56,+R12         
         PUMD R26,+R12         
         RTN                   

         DATA  7,53
CONCA.   JSB  =SETUP$          
         LDM  R70,R32          
         LDM  R76,R72          
         STM  R30,R72          

CONCA-   LDM  R56,R70          
         ADM  R56,R74          
         IFNG
           LDM  R56,=7FFFH       
         ENDIF
         JSB  =RESPUT
         REN
         STM  R70,R32          
         LDM  R30,R26          
         JSB  =COPY            
         ADM  R30,R32          
         STM  R74,R32          
         JSB  =COPY            
         RTN                   

         DATA 0,56
KEY$     BIN                   
         JSB  =KEY?            
         IFEZ
NULL       CLM  R44              
           PUMD R44,+R12         
           RTN                   
         ENDIF
         JSB  =ATTN?           
         JEN  NULL
         JSB  =DEQUE           
         STB  R2,R46           
         JMP  STR1CH

         DATA 20,56
CHR$.    JSB  =ONEB            
STR1CH   CLM  R56              
         ICM  R56              
         JSB  =RESPUT
         REN
         STBD R46,R26          
         RTN                   

         DATA  20,56
VAL$.    JSB  =ONER            
         BIN                   
         JSB  =RESCON          
         DATA 32D
         REN
         PUMD R26,+R6          
         STM  R26,R30          
         JSB  =CVNUM           
         BIN                   
         POMD R26,-R6          
         SBM  R30,R26          
         PUMD R30,+R12         
         PUMD R26,+R12         
         RTN                   

         DATA  0,55
ERRL.
         LDMD R44,=(ERLIN#)-1
         LDB  R44,=0FFH
         CLB  R47              
         CMB  R46,=0A9H
         IFHS
           LDB  R46,=99C
         ENDIF
         JMP  PUSH40

         DATA 30,55
LEN.     POMD R36,-R12         
         POMD R36,-R12         
         JMP  PUINTG

         DATA  0,55
MEM.     BIN                   
         LDMD R36,=LAVAIL      
         SBMD R36,=TOS         
         SBMD R36,=LEEWAY      
         JMP  PUINTG

         DATA  30,55
NUM.     DRP  R24              
         JSB  =GETAD#          
         CLM  R36              
         LDBD R36,R24          
         POMD R24,-R12         
         IFZR
           CLM  R36              
         ENDIF
PUINTG   JSB  =CONBIN          
PUSH40   PUMD R40,+R12         
         RTN                   

         DATA 0,55
RESUL.   LDMD R40,=RESULT      
         JMP  PUSH40

         DATA  30,55
VAL.     DRP  R24              
         JSB  =GETAD#          
         ARP  !12
         POMD R30,-R12          
         ADM  R30,R24          
         LDBD R32,R30          
         LDB  R33,=CR
         STBD R33,R30          
         LDM  R34,R10          
         LDM  R10,R24          
         CLM  R36              
         JSB  =GCHAR           
SCANVL
         LOOP
           JSB  =SYSJSB          
             DEF SCAN
           CMB  R14,=PLUS
         WHEQ
         CMB  R14,=MINUS
         IFEQ
           ICB  R36              
           JMP SCANVL
         ENDIF
         CMB  R14,=32          
         JZR  INTVAL
         CMB  R14,=4           
         JZR  VALDUN
         JSB  =ERROR           
         DATA 89D
         JMP  RESTOV

INTVAL   LDM  R75,R44          
         JSB  =I#PUSH          
VALDUN   TSB  R36              
         IFOD
           BCD                   
           JSB  =CHSROI          
         ENDIF
RESTOV   STM  R34,R10          
         STBD R32,R30          
         RTN                   

         DATA 0,55
ERNUM.   CLM  R36              
         LDBD R36,=ERNUM#      
         JMP  PUINTG

         DATA 52,55
POS.     JSB  =SETUP$          
         JSB  =POSRUN
         JMP  PUINTG

POSRUN   TSM  R36              
         JZR  NOTFND
         SBM  R32,R36          
         JNC  NOTFND
         DCM  R36              
         STM  R34,R26          
         STM  R30,R0           
FNDMAT
         POBD R50,+R30         
         CMBD R50,R34          
         JNZ  LOOKON
         STM  R30,R2           
         ICM  R34              
         STM  R36,R56          
         JSB  =CMPSTR          
         JZR  FOUND
         LDM  R34,R26          
         LDM  R30,R2           
LOOKON   DCM  R32              
         JCY  FNDMAT

NOTFND   CLM  R36              
         RTN                   
FOUND    LDM  R36,R2           
         SBM  R36,R0           
         RTN                   

         DATA 20,45
TAB.     JSB  =ONEB            
         DCM  R46              
         IFNG
           JSB  =WARN            
           DATA 54D
           CLM  R46              
         ENDIF
         CLM  R2               
         LDBI R2,=LINELN       
         IFNZ
           LOOP
             SBM  R46,R2           
           WHPS
           ADM  R46,R2           
         ENDIF
         LDBI R2,=P_PTR        
         CMM  R46,R2           
         IFNC
           JSB  =LINEND
           CLM  R2               
         ENDIF
         SBM  R46,R2           
         IFNG
           CLM  R46              
         ENDIF
         STM  R46,R56          
         JSB  =RESPUT
         REN
         JSB  =BLKFIL          
         RTN                   

         DATA 30,56
UPC$.    DRP  R36              
         JSB  =GETAD#          
         ARP  !12
         POMD R56,-R12          
         JSB  =RESPUT
         REN

UPLOOP   DCM  R56              
         RNC
         POBD R20,+R36         
         JSB  =ALFA#           
         PUBD R#,+R26          
         JMP  UPLOOP
       TITLE 'krprn'
ZONELN EQU 21D
*  __________________________________________________________________
* |KXPRN 373 09/27/82 - 12/16/1982                                   |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@      @@  @@@@@@@@    @@@@@@@@    @@      @@   ||
* ||   @@    @@@   @@      @@  @@@@@@@@@   @@@@@@@@@   @@      @@   ||
* ||   @@   @@@    @@@    @@@  @@     @@@  @@     @@@  @@@     @@   ||
* ||   @@  @@@      @@@  @@@   @@      @@  @@      @@  @@@@    @@   ||
* ||   @@ @@@         @@@@     @@     @@@  @@     @@   @@ @@   @@   ||
* ||   @@@@@           @@      @@@@@@@@@   @@@@@@@     @@  @@  @@   ||
* ||   @@@@@           @@      @@@@@@@@    @@@@@@@     @@  @@  @@   ||
* ||   @@ @@@         @@@@     @@          @@    @@@   @@   @@ @@   ||
* ||   @@  @@@      @@@  @@@   @@          @@     @@@  @@    @@@@   ||
* ||   @@   @@@    @@@    @@@  @@          @@      @@  @@     @@@   ||
* ||   @@    @@@   @@      @@  @@          @@      @@  @@      @@   ||
* ||   @@     @@@  @@      @@  @@          @@      @@  @@      @@   ||
* ||                                                                ||
* ||                  Last edited on <821216.1528>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
PRNFMT   
         
         LDMI R22,=P_PTR       
         CLM  R34
         LDBI R34,=LINELN
         IFNZ
           TSM  R22
           IFNZ
             LDM  R2,R36           
             ADM  R2,R22           
             CMM  R34,R2           
             IFNC
               LDBD R2,=USING?       
               IFZR
                 JSB  =LINEND
               ENDIF
             ENDIF
           ENDIF
         ENDIF
         PUBD R32,+R6          
         LOOP
           DCM  R36              
           JNC  CPYEND
           JSB  =TSTEOL
           POBD R32,+R26         
           JSB  =OUT
           ICM  R22              
         WHMP
CPYEND   POBD R32,-R6          
         TSB  R20              
         JOD  PRNTEX
         LDM  R36,R22          
         LOOP
           DRP  !36
           SBM  R36,=(ZONELN).2
         WHPS
         TCM  R36              
         TSM  R34              
         IFNZ
           SBM  R34,R22          
           CMM  R34,R36          
           IFLO
             JSB  =LINEND
             CLM  R36              
           ENDIF
         ENDIF
         LOOP
           DCM  R36              
           JNC  PRNTEX
           LDB  R32,=BLANK
           JSB  =OUT
           ICM  R22              
         WHMP
PRNTEX   STMI R22,=P_PTR       
         RTN                   

TSTEOL   TSB  R34
         RZR  
         CMB  R22,R34           
         RNC

LINEND   CLM  R22              
         STMI R22,=P_PTR       
         LDBD R2,=ROUTE        
         DCB  R2               
         IFZR
           GTO OUTEOL            
         ENDIF
         DCB  R2               
         IFZR
           GTO PR.EOL            
         ENDIF
         JSB  =HANDI0          
           VAL V.ENDL
         RTN                   

OUT      LDBD R2,=ROUTE        
         DCB  R2               
         IFZR
           GTO OUTCHR            
         ENDIF
         DCB  R2               
         IFZR
           GTO PRNTCH            
         ENDIF
         JSB  =HANDI0          
           VAL V.CHAR
         RTN                   
       TITLE 'krput'
*  __________________________________________________________________
* |RHPUT 448 04/02/82 - 4/20/1982 9:34PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@    @@      @@  @@@@@@@@    @@      @@  @@@@@@@@@@   ||
* ||   @@@@@@@@@   @@      @@  @@@@@@@@@   @@      @@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@     @@@  @@      @@      @@       ||
* ||   @@      @@  @@      @@  @@      @@  @@      @@      @@       ||
* ||   @@     @@   @@      @@  @@     @@@  @@      @@      @@       ||
* ||   @@@@@@@     @@@@@@@@@@  @@@@@@@@@   @@      @@      @@       ||
* ||   @@@@@@@     @@@@@@@@@@  @@@@@@@@    @@      @@      @@       ||
* ||   @@    @@@   @@      @@  @@          @@      @@      @@       ||
* ||   @@     @@@  @@      @@  @@          @@      @@      @@       ||
* ||   @@      @@  @@      @@  @@          @@@    @@@      @@       ||
* ||   @@      @@  @@      @@  @@           @@@@@@@@       @@       ||
* ||   @@      @@  @@      @@  @@            @@@@@@        @@       ||
* ||                                                                ||
* ||                  Last edited on <820908.1346>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
PUTBIN   JSB  =CONBIN          
         CLM  R66              
         CLM  R70              
         LDB  R76,=5           
         CLM  R55              
         LDB  R54,R76          
         LDM  R30,R26          
         JSB  =FORMN+
         BIN                   
         RTN                   
       TITLE 'krset'
*  __________________________________________________________________
* |KRSET 478 07/14/82 - 7/19/1982 4:11PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@      @@@@@@    @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@    @@@@@@@@   @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@@    @@@  @@              @@       ||
* ||   @@  @@@     @@      @@  @@      @@  @@              @@       ||
* ||   @@ @@@      @@     @@   @@@         @@              @@       ||
* ||   @@@@@       @@@@@@@      @@@@@@@    @@@@@@@@@       @@       ||
* ||   @@@@@       @@@@@@@       @@@@@@@   @@@@@@@@@       @@       ||
* ||   @@ @@@      @@    @@@          @@@  @@              @@       ||
* ||   @@  @@@     @@     @@@  @@      @@  @@              @@       ||
* ||   @@   @@@    @@      @@  @@@     @@  @@              @@       ||
* ||   @@    @@@   @@      @@   @@@@@@@@   @@@@@@@@@@      @@       ||
* ||   @@     @@@  @@      @@    @@@@@@    @@@@@@@@@@      @@       ||
* ||                                                                ||
* ||                  Last edited on <820813.1425>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
SET      POMD R2,-R6           
         PUMD R43,+R6          
         POMD R43,+R2          
         ARP  R44
         LOOP
           PUBD R43,+R#         
           CMM  R46,R#          
         WHHS
         POMD R43,-R6          
         PUMD R2,+R6           
         RTN                   
       TITLE 'krbee'
*  __________________________________________________________________
* |KRBEE 58 06/24/82 - 7/12/1982 4:53PM                              |
* |==================================================================|
* ||                                                                ||
* ||   @@     @@@  @@@@@@@@    @@@@@@@@    @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@    @@@   @@@@@@@@@   @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@   @@@    @@     @@@  @@     @@@  @@          @@           ||
* ||   @@  @@@     @@      @@  @@      @@  @@          @@           ||
* ||   @@ @@@      @@     @@   @@     @@@  @@          @@           ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@@@   @@@@@@@@@    ||
* ||   @@@@@       @@@@@@@     @@@@@@@@    @@@@@@@@@   @@@@@@@@@    ||
* ||   @@ @@@      @@    @@@   @@     @@@  @@          @@           ||
* ||   @@  @@@     @@     @@@  @@      @@  @@          @@           ||
* ||   @@   @@@    @@      @@  @@     @@@  @@          @@           ||
* ||   @@    @@@   @@      @@  @@@@@@@@@   @@@@@@@@@@  @@@@@@@@@@   ||
* ||   @@     @@@  @@      @@  @@@@@@@@    @@@@@@@@@@  @@@@@@@@@@   ||
* ||                                                                ||
* ||    Finished on 12/16/81  Raan  Last edited on <820908.1346>    ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
BEEPP    JSB  =GETPA?          
         JSB  =SXX3            
         TSB  R34              
         IFZR
           JSB  =EOL14?          
           IFEN
             POBD R36,-R12         
             JSB  =ONOFF2          
           ENDIF
         ENDIF
         RTN                   
STBEEP
         JSB  =MELJSB          
           DEF STBEP_
         RTN

         DATA 241
BEEP.    JSB  =MELJSB          
           DEF  BEEP._           
         RTN                   

BEEPER   JSB  =MELJSB          
           DEF  BEEPR_           
         RTN                   
       TITLE 'krdcl'
*  __________________________________________________________________
* |IVDCL 114 05/10/82 - 5/13/1982 2:56PM                             |
* |==================================================================|
* ||                                                                ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@         @@@@     @@           ||
* ||   @@@@@@@@@@  @@      @@  @@@@@@@@     @@@@@@@@   @@           ||
* ||       @@      @@      @@  @@    @@@   @@@    @@@  @@           ||
* ||       @@      @@      @@  @@      @@  @@      @@  @@           ||
* ||       @@       @@    @@   @@      @@  @@          @@           ||
* ||       @@       @@    @@   @@      @@  @@          @@           ||
* ||       @@       @@    @@   @@      @@  @@          @@           ||
* ||       @@        @@  @@    @@      @@  @@          @@           ||
* ||       @@         @@@@     @@      @@  @@      @@  @@           ||
* ||       @@         @@@@     @@    @@@   @@@    @@@  @@           ||
* ||   @@@@@@@@@@      @@      @@@@@@@@     @@@@@@@@   @@@@@@@@@@   ||
* ||   @@@@@@@@@@      @@      @@@@@@         @@@@     @@@@@@@@@@   ||
* ||                                                                ||
* ||                  Last edited on <820908.1352>                  ||
* |==================================================================|
* |__________________________________________________________________|

* ********************************************************************
* ********************************************************************
         DATA  323              
SKIPI    JMP  SKIPIT           

* break
         DATA  322              
SKIPS    JMP  SKIPIT           

         DATA  241              
SKIP!    JMP  SKIPIT           

         DATA  320              
SKIPEM   JMP  SKIPIT           

         DATA  321              
SKIPD
SKIPR    JMP  SKIPIT           

         DATA  341              
SKIPIT   LDMD R36,=PCR         
         JSB  =SKPLN           
         STM  R#,R10           
         GTO GORTN             

         BSS 0FFFFH-($)+1
*        BSZ  6                
*        BSZ  400              ! I/O SPACE - UNUSED ROM
       END
