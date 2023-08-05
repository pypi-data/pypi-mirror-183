         ABS
         ORG 60000
GETTYP   ADDR 61716
STRB-    ADDR 62661
DIRSCN   ADDR 63143             ; Scan the directory in MSROM
MSLDB.   ADDR 63604             ; LOADBIN runtime entry in MSROM
LOADBR   ADDR 63770
TYPOK2   ADDR 64157
MSCRE.   ADDR 65256
ASSIG.   ADDR 65571
MSPRT.   ADDR 66312
PR#$     ADDR 66762
RD#$     ADDR 67457
CKMSUS   ADDR 70235
MSIN     ADDR 70253
TAPDS-   ADDR 70740
ASTAR    ADDR 25016             ; addr in sytem ROM of a '*' (byte 052)
BEGWRI   ADDR 100710            ; first byte of what to write to a file
ENDWRI   ADDR 100712            ; last byte of what to write to a file
AIFFLG   ADDR 100714            ; conditional-asm flg, non-0 to assemble
ASTLIN   ADDR 100716            ; ptr to start of line we're assembling
ALBTBL   ADDR 100720            ; ptr to beginning of label table
ACODBA   ADDR 100722            ; ptr to end of LblTbl, start of code
ACODEN   ADDR 100724            ; ptr to end of code being assembled
ALAVAI   ADDR 100726            ; ptr to end of avail space for assemble
ABNLEN   ADDR 100730            ; length of ABPNAM (see below)
GNMLEN   ADDR 100732            ; len of GLOFNM
CURARP   ADDR 100736            ; curr ARP during assembly (377 if undef)
CURDRP   ADDR 100737            ; curr DRP during assembly (377 if undef)
ALODBP   ADDR 100740            ; dont-load-bpgm flag after ASSEMBLE
ABPNAM   ADDR 100746            ; targ filename for bpgm being assembled
GLOFNM   ADDR 100767            ; filename for included global file
ILNMAB   ADDR 101201            ; if set, illegal (MSbit=NAM LSbit=ABS)
ISGLO    ADDR 101202            ; =0 if this is a global file, else non-0
ISAROM   ADDR 101203            ; ABS ROM or not
GOODLI   ADDR 101204            ; non-0 at end of line ASSM line parse
LSTFLG   ADDR 101205            ; whether LST is on or off
AERCNT   ADDR 101206            ; error count during ASSEMBLE
ORGBAS   ADDR 101212            ; ORG base address
ABSBAS   ADDR 101214            ; base address for absolute code
RRSTK    ADDR 101306            ; stack for returning from ROMJSB to EXEC
END16K   ADDR 140000            ; end of RAM on 16K machine
SVCIO    ADDR 100143            ; 8-byte block ends with SVCWRD and IOSW
OUTBUF   EQU 0                 ; scratch buf for ASM ROM input/output
ROMPEK   EQU 40                ; buf for code to read byte from ROMs
MEMADR   EQU 50                ; mem dump addr (8-byte REAL/INT number)
MEMROM   EQU 60                ; ROM# from which to do a MEM dump
MEMLEN   EQU 61                ; length of a MEM dump
MEMPTR   EQU 63                ; address we're currently dumping from
MEMR6    EQU 65                ; place to save R6 during MEM statement
DBSAV1   EQU 67                ; system RAM save during bkp interrupt
DBSAV2   EQU 77                ; ditto
DBSAV3   EQU 107               ; ditto
DBSAV4   EQU 117               ; ditto
DBSAV5   EQU 127               ; ditto
DBSAV6   EQU 137               ; ditto
DB?1     EQU 147               ; don't think this is ever used!
DBS.C.   EQU 150               ; output select code for debugging output
TRCCNT   EQU 160               ; count from Trace command at breakpoint
DBBKP2   EQU 162               ; address BREAKPOINT #2 is set to
DBGWRS   EQU 164               ; last state written to DEBSTS
DBBKP1   EQU 165               ; address BREAKPOINT #1 is set to
EOLREM   EQU 167               ; 0 hides EOL remarks, non-0 shows them
ASMMOD   EQU 170               ; 0 if in BASIC, non-0 if in ASSEMBLER
BKPSAV   EQU 171               ; BREAKPOINT save during single-step
ASMSIZ   EQU 174               ; how many bytes to reserve for ASM RAM
P.TYPE   EQU 6                 ; Pgm type in Program Control Block (PCB)
P.LEN    EQU 7                 ; Program LENGTH in PCB
P.SFLG   EQU 25                ; Program security flags in PCB
P.BASE   EQU 30                ; Abs addr at which BPGM was last loaded
F.TYPE   EQU 7                 ; offset into LIF dir of file TYPE
*
* HP-85 ASSEMBLER ROM
*
* **********************************************************************
* NOTE: Because, while in ASSEMBLER mode, the key label area isn't used
* and gets re-initialized when returning to BASIC mode, the Assembler
* ROM sometimes uses that area (100710-101007) for temporary storage.
* See the DADs above for examples.
* **********************************************************************
*
         DATA 50,327           ; ROM# and complement
         DEF  RUNTIM           ; runtime routines addresses
         DEF  TOKENS           ; TOKENS (ASCII keywords)
         DEF  PARSE            ; parse routine addresses
         DEF  ERMSGS           ; warning and error messages
RUNTIM   DEF  INIT             ; ROM initialization routine
         DEF  ASMLR.           ; 01 ASSEMBLER
         DEF  BASIC.           ; 02 BASIC
         DEF  FREFS.           ; 03 FREFS
         DEF  MEMD.            ; 04 MEMD
         DEF  DEL.             ; 05 DELETE
         DEF  PLST.            ; 06 PLIST
         DEF  LST.             ; 07 LIST
         DEF  MEM.             ; 10 MEM
         DEF  ASMBL.           ; 11 ASSEMBLE
         DEF  ALOAD.           ; 12 ALOAD
         DEF  ASTOR.           ; 13 ASTORE
         DEF  SCRTB.           ; 14 SCRATCHBIN
         DEF  FLBL.            ; 15 FLABEL
         DEF  BKP.             ; 16 BKP
         DEF  CLR.             ; 17 CLR
         DEF  TREM.            ; 20 TREM
         DEF  REL.             ; 21 REL
         DEF  OCT.             ; 22 OCT
         DEF  DEC.             ; 23 DEC
         DEF  DEC.             ; 24 377 End of findable keywords
         DEF  ACOLN.           ; 25 :
         DEF  AEQUL.           ; 26 =
         DEF  ACOMA.           ; 27 ,
PARSE    DEF  DMPMEM           ; 'hidden' dump memory token
         DEF  ASMLR            ; 01 ASSEMBLER
         DEF  BASIC            ; 02 BASIC
         DEF  FREFS            ; 03 FREFS
         DEF  MEMD             ; 04 MEMD
         DEF  ALIST            ; 05 DELETE
         DEF  ALIST            ; 06 PLIST
         DEF  ALIST            ; 07 LIST
         DEF  MEMD             ; 10 MEM
         DEF  ASSEMB           ; 11 ASSEMBLE
         DEF  FREFS            ; 12 ALOAD
         DEF  FREFS            ; 13 ASTORE
         DEF  ABCOM            ; 14 SCRATCHBIN
         DEF  FREFS            ; 15 FLABEL
         DEF  BKP              ; 16 BKP
         DEF  CLR              ; 17 CLR
         DEF  BASIC            ; 20 TREM
TOKENS   DATA  `ASSEMBLER`      ; 01
BASSTR   DATA  `BASIC`          ; 02
FRESTR   DATA  `FREFS`          ; 03
         DATA  `MEMD`           ; 04
         DATA  `DELETE`         ; 05
         DATA  `PLIST`          ; 06
         DATA  `LIST`           ; 07
MEMASP   DATA  `MEM`            ; 10
ASSSTR   DATA  `ASSEMBLE`       ; 11
ALDSTR   DATA  `ALOAD`          ; 12
ASTSTR   DATA  `ASTORE`         ; 13
         DATA  `SCRATCHBIN`     ; 14
FLASTR   DATA  `FLABEL`         ; 15
BKPASP   DATA  `BKP`            ; 16
CLRASP   DATA  `CLR`            ; 17
         DATA  `TREM`           ; 20
         DATA  `REL`            ; 21
         DATA  `OCT`            ; 22
         DATA  `DEC`            ; 23
         DATA 377              ; 24 End of searchable/findable keywords
         DATA  `:`              ; 25
         DATA  `=`              ; 26
         DATA  `,`              ; 27
ERMSGS   JSB  =ROMJSB
         DEF  SCRAT.           ; do a SCRATCH command
         DATA 0
         RTN
DODISP   JSB  =ROMJSB
         DEF  DISP.            ; set output to DISPLAY
         DATA 0
         RTN
DOPRNT   JSB  =ROMJSB
         DEF  PRINT.           ; set output to PRINTER
         DATA 0
         RTN
*
         DATA  `ILL MODE`       ; 11
         DATA  `LBL`            ; 12
OPCOER   DATA  `OPCO`           ; 13
         DATA  `ARP-DRP`        ; 14
         DATA  `OPER`           ; 15
         DATA  `FIN-LNK`        ; 16
MASMRM   DATA  `ASSM ROM`       ; 17
         DATA 377              ; End of ERROR MESSAGES table
STBAS1   JSB  =GTABAS          ; Get ptr to ASM RAM in R14, leave ARP=14
         CLM  R40              ; clear R40-47
         STBD R40,X#,ASMMOD    ; Set ASMMOD to 0 (means "in BASIC mode")
         RTN
* ***************************************************************
* * ROM INITIALIZATION
* * ROMFL
* *   0	after system initialization at PWO (Power-On)
* *   1	after System RESET
* *   2	before SCRATCH
* *   3	after LOADBIN
* *   4	before RUN execution begins, after INIT allocation done
* *   5	before LOAD
* *   6	during STOP, PAUSE
* *   7	after CHAIN
* *  10	during allocation of class > 56
* *  11	during de-allocation of class > 56
* *  12	during decompile of class > 56
* *  13	during program halt on error
* ***************************************************************
INIT     BIN
         LDBD R34,=ROMFL       ; Get reason for INIT call
         JNZ  NOTPWO           ; jif not PWO (power-on)
         LDMD R34,=FWUSER      ; it's PWO, steal RAM for ASMROM's use
         STMD R34,=ASMBAS      ; save the address in the ROM's RAM table
         ADM  R34,=(ASMSIZ).2  ; move FWUSER (we use 174 = 124D bytes)
         STMD R34,=FWUSER      ; update ptr
         JSB  =ROMJSB
         DEF  SCRAT+           ; re-init to adjust for stolen RAM
         DATA 0
         JSB  =STBAS1          ; get ASM RAM in R14, DRP=40, ARP=14
         STMD R#,X#,MEMADR     ; zero 8 bytes
         STMD R#,X#,MEMROM     ; zero 8 more
         STMD R#,X#,DBGWRS     ; and another 8
         ICB  R#               ; set R40 = 1
         STMD R#,X#,TRCCNT     ; TRCCNT=1, seven more zeroed
         CLB  R#               ; set R40 back to 0
         LDB  R47,=20          ; make R40-R47 = REAL 1
         STMD R40,X#,DBS.C.    ; set DEBUG output Select Code to 1
         LDM  R32,=100,0
         STMD R32,X#,MEMLEN    ; set ASMBAS+61 = 100 (64D)
         LDM  R32,=R60K        ; base address of our ROM
         JSB  =RSUM8K          ; checksum it to make sure we're okay
         JZR  OKSUM            ; jif okay
         JSB  =AROMER          ; conditionally set ERRROM to ASMROM
         JSB  =ERROR           ; report error
         DATA 17               ; "ASSM ROM"
         JMP  OKSUM            ; continue
BARST?   DCB  R#               ; BASIC mode, after reset?
         JZR  OKSUM            ; jif yes, nothing special to do
         RTN
NOTPWO   JSB  =GETMOD          ; get ASM/BASIC mode -> R56
         DRP  R34              ; set DRP back to ROMFL reg
         JZR  BARST?           ; jif BASIC mode
         DCB  R34              ; ASM mode, after RESET?
         JNZ  NOTRST           ; jif no
         JSB  =ASMRST          ; do ASSEMBLER MODE reset
OKSUM    JSB  =GTABAS          ; load ASM ROM base
         JSB  =RSTBK1          ; restore BKP1 if saved
         CLM  R76
         ICM  R76
         STMD R76,X14,TRCCNT   ; set TRCCNT to 1 (ie, NO trace)
*
* When the System Monitor interrupts because a BREAKPOINT has been hit
* the CPU gets vectored to SPAR0, a RAM hook.  The Assembler ROM takes
* over SPAR0 so that it gets control, but SPAR0 isn't long enough to
* preserve everything it needs to preserve, jump to the ASM ROM, then
* restore everything on the return trip.  So, the ASM ROM takes over
* SPAR0 and points it to SAVR2 (in the CPU register save area), then
* copies the necessary code to SAVR2 to do all the dirty work of saving
* calling and restoring.
*
* The following code is what copies the INTSVC routine code to SAVR2
* by loading a 45 (byte count) into R75 and the address of INTSVC into
* R76-77.  45 is actually more bytes than we need, but it doesn't hurt.
*
CPYHOK   DATA 175,251,45       ; DRP 75 - LDM R75,=45,INTSVC
         DEF  INTSVC
         LDM  R0,=SAVR2        ; destination address to R0
CISLP    POBD R74,+R76         ; get next byte of INTSVC to r74
         PUBD R74,+R0          ; push it out to the SAVR2 buffer
         DCB  R75              ; dec byte count
         JNZ  CISLP            ; jif not done
*
* This is the code that takes over SPAR0 and points it at SAVR2
*
         DATA 174,251          ; DRP 74 -- LDM R74,= "JSB =SAVR2, RTN"
         JSB  =SAVR2           ; this is loaded into R74-77 along with
         RTN                   ;   this, too
         STMD R#,=SPAR0        ; Take over SPAR0 with JSB=SAVR2 and RTN
*
         LDMD R#,=ASMBAS       ; R74-75=ASMBAS, R76-77=junk, saves a DRP
         LDBD R#,X74,DBGWRS    ; get last command written to SysMon
         STBD R#,=DEBSTS       ; write it out (MSBit is clear)
         ADB  R#,=200          ; set MSbit
         STBD R#,=DEBSTS       ; write it again to set the MSbit
         STBD R#,=INTRSC       ; write any byte to INTRSC
ARTN98   RTN
*
* Don't allow LOADIN, RUN, LOAD, or STOP or PAUSE in ASSEMBLER MODE
* as those are BASIC mode things.
*
NOTRST   CMB  R#,=3            ; LOADBIN, RUN, LOAD, STOP/PAUSE?
         JNC  ARTN98           ; jif no, <3
         CMB  R#,=7            ; well?
         JCY  ARTN98           ; jif no, >=7
         CMB  R#,=6            ; STOP/PAUSE?
         JNZ  NOTSP            ; jif no
         JSB  =ERMSGS          ; Do Basic SCRATCH if STOP/PAUSE
NOTSP    JSB  =AROMER          ; Set ERROR ROM# to ASSEMBLER
         JSB  =ERROR+          ; report ERROR
         DATA 11               ; "ILL MODE"
*
INTSVC   SAD                   ; save CPU flags
         STMD R74,=SAVR74      ; save r74-r77 in CPU register save area
         LDMD R74,=ERTEMP      ; save 4 bytes of ERTEMP on stack
         PUMD R74,+R6
         STMD R0,=SAVR0        ; save R0-1 in CPU register save area
         JSB  =ROMJSB          ; call ASM ROM's breakpoint svc routine
         DEF  BKPSVC
         DATA 50
         POMD R74,-R6          ; restore 4 bytes
         STMD R74,=ERTEMP      ;  of ERTEMP
         LDMD R74,=SAVR74      ; restore r74-r77
         PAD                   ; restore CPU flags
         RTN                   ; return from the breakpoint
*
ASMSAV   DATA 143,200          ; save junk, PRALLM, PENUPF, SVCWRD, IOSW
         DEF  KEYHIT
         DEF  SCTEMP
         DEF  ERSV50
         DEF  DATLEN
         DEF  ERLIN#
*
* Servce routine when a BREAKPOINT is encountered by the System Monitor
* We arrive here via SPAR0 -> SAVR2 -> here
* First, save all CPU registers.  R0-1 and R74-77 were already saved by
* code that was in SAVR2.  That code is about to be overwritten by the
* register save, but will be restored again on the way out after most
* of the registers are restored.
*
BKPSVC   LDM  R76,=SAVR2       ; address of register save area
         LDB  R0,=2            ; start reg to save, 0-1 were done before
         BIN                   ; make sure we're in BIN mode
SREGLP   PUBD R*,+R76          ; save a CPU register in SAV*** area
         ICB  R0               ; bump register-indirect register
         CMB  R0,=74           ; Done? (R74-77 were already saved)
         JNZ  SREGLP           ; jif no, loop
*
         BCD                   ; BCD shift 4-bit E register into R0
         CLB  R0
         ELB  R0               ; get E
         BIN                   ; back to BIN
         PUBD R0,+R6           ; save E on stack
*
* When the System Monitor generates an interrupt because a breakpoint
* was hit, the current CPU address gets pushed on the stack and
* execution jumps to SPAR0. SPAR0 has been taken over and has a
* JSB=SAVR2 followed by a RTN, so execution quickly jumps to the
* SAVR2 RAM area, which has a copy of INTSVC (above) in it. That
* saves a few things that would otherwise get trashed by ROMJSB, and
* then calls ROMJSB to get here (BKPSVC).  So, at this point, the
* R6 stack looks like:
*
*  2 BYTES return from SPAR0 to wherever interrupted from
*  2 BYTES return from INTSVC to SPAR0
*  3 BYTES SAD (Save Arp/Drp and flags) in INTSVC
*  4 BYTES ERTEMP save in INTSVC
*  2 BYTES return from ROMJSB to INTSVC
*  2 BYTES R0 in ROMJSB
*  1 BYTE  current ROM# in ROMJSB
*  2 BYTES return from BKPSVC to ROMJSB
*  1 BYTE  E save in BKPSVC
* R6--->
*
* So, the following copy of R6 and adding 17 (octal) to it points R20
* at the "return from INTSVC to SPAR0", and the POMD r44,-r20 gets the
* addr of the code about to be executed when the breakpoint occurred.
*
         LDM  R20,R6           ; copy ptr to top of stack
         SBM  R20,=17,0        ; move back to breakpoint execution addr
         POMD R44,-R20         ; get addr where the breakpoint occurred
         STMD R44,=SAVR4       ; save it in SAVR4 (which is the PC)
         STMD R20,=SAVR6       ; save R20 in SAVR6
         JSB  =GTABAS          ; get the ASM ROM's RAM ptr into R14
*
         ADM  R#,=67,0         ; point R14 at DBSAV1
*
* NOTE: We're in a hardware interrupt routine, so we have to be VERY
* careful not to destroy ANYTHING ANYWHERE.  But we want to (have to)
* call SOME system routines which WILL destroy/change SOME things.
* So we have to carefully save EVERYTHING that might get changed.  The
* only place we can save those things, without destroying something
* ELSE, is in the ASM ROM's stolen RAM. Not everything that's saved
* NEEDS to be saved (it doesn't get destroyed) but it's cheaper (in
* bytes of ROM code) to save/restore a list of blocks of 8 bytes than
* to have a longer list with variable number of bytes. RAM was cheaper
* than ROM. Slightly.
*
         DATA 145,251,6        ; LDM  r45,=06,0320,0141
         DEF  ASMSAV           ; table of 6 System RAM locations to save
SAVLOP   POMI R60,+R46         ; get 8 bytes from next entry in table
         PUMD R60,+R14         ; save it in ASM ROM's RAM
         CLB  R60              ; clear SVCWRD (for future interrupts)
         STBD R60,=SVCWRD      ; silly to be inside loop, but oh well
         DCB  R45              ; decrement loop counter
         JNZ  SAVLOP           ; jif not done, go save more
*
         CLM  R16              ; set CSTAT (Capricorn STATus) to IDLE
         ICM  R16
BKREDO   JSB  =GTABAS          ; reload ASM ROM's RAM ptr
         LDMD R40,X#,DBS.C.    ; get DBG output select code
         STMD R40,=SCTEMP      ; set Select Code for doing the BKP dump
         LDM  R30,R#           ; point to ASM RAM output buffer
*
         LDMD R46,X#,TRCCNT    ; get trace count from ASM RAM
         DCM  R46              ; is it 1?
         JNZ  TRCIT            ; jif no
*
         JSB  =RSTBK1          ; restore BKP1 (in case single-stepping)
         JSB  =FRMMEM          ; format and disp/print "MEM addr" line
         JSB  =DMPME-          ; Do the memory dump
         JSB  =DMPFLG          ; Dump the flags
         JSB  =SPCDMP          ; blank line
         JSB  =DMPREG          ; dump the CPU registers
CHKERR   TSB  R17              ; Error?
         JPS  BRKIDL           ; jif no
* The following does LDM R4,=61627 (AERR-1)
         GTO AERR              ; else report error
*
RSTBK1   LDMD R65,X#,BKPSAV    ; Get saved BKP1 from ASM ROM RAM
         JZR  ARTN99           ; jif 0, none saved
         STMD R65,X#,DBGWRS    ; save in SysMonStat & BKP 1 in ASM RAM
         STM  R65,R45          ; also copy it to R45-47
         CLM  R65              ; clear BKP1 save
         STMD R65,X14,BKPSAV   ; zero BKPSAV, nothing saved there now
         CLM  R26              ; clear MSbit
         JSB  =STBKP1          ; write it to System Monitor
ARTN99   RTN
*
BRKIDL   JSB  =KEYLOP          ; wait for key
         LDBD R20,=KEYHIT      ; get the keycode
         LDM  R36,=(AKYTAB).2  ; table of our keys and actions
KTABLP   POMD R43,+R36         ; get next entry
*
         CMB  R43,R20          ; key match the current key?
         JZR  GOTKEY           ; jif yes
*
         CMB  R43,=316         ; ?
         JNZ  KTABLP           ; jif no
*
         CMB  R20,=220         ; STEP?
         JZR  SNGSTP           ; jif yes
*
         CMB  R20,=236         ; SCROLL UP?
         JNZ  NOT236           ; jif no
         JSB  =ALPHA.          ; force ALPHA crt mode
         JSB  =SCRUP           ; scroll screen up one line
RPTCHK   JSB  =COUNTK          ; wait for key up, repeat it
         JMP  CURSON
*
NOT236   CMB  R#,=237          ; SCROLL DOWN?
         JNZ  NOT226           ; jif no
         JSB  =ALPHA.          ; force ALPHA mode
         JSB  =SCRDN           ; scroll down a line
         JMP  RPTCHK
NOT226   CMB  R#,=215          ; RUN?
         JZR  ASMRUN           ; jif yes
         CMB  R#,=211          ; COPY?
         JNZ  NOT211           ; jif no
         JSB  =ROMJSB
         DEF  COPY.            ; do COPY
         DATA 0
NORPET   JSB  =EOJ2            ; no repeat, end keystroke
CURSON   JSB  =CURS            ; force ALPHA cursor ON
         JMP  CHKERR
*
TRCIT    STMD R#,X#,TRCCNT     ; save trace count in ASM ROM RAM
         PUMD R#,+R6           ; save on stack
         JSB  =PRTPC           ; print PC, DRP, ARP, BKP1, BKP2 values
         POMD R#,-R6           ; recover from stack
         JMP  TRCSTP
*
NOT211   CMB  R#,=212          ; PAPER ADVANCE?
         JNZ  NOT212           ; jif no
         JSB  =ROMJSB
         DEF  PAPER.           ; advance the paper
         DATA 0
         JMP  RPTCHK
*
GOTKEY   PUMD R44,+R6          ; save ptrs
         JSB  =BKPCMD          ; enter arguments and CR
         POMD R44,-R6          ; recover ptrs
         DRP  R76
         JSB  X44,ZRO          ; call function in R44-45 (from AKYTAB)
         JMP  NORPET
*
NOT212   CMB  R#,=223          ; GRAPH?
         JNZ  NORPET           ; jif no
         JSB  =GRAPH.          ; force GRAPHICS mode
         JMP  NORPET
*
SNGSTP   LDMD R55,X14,DBGWRS   ; get last SysMon bits and BKP1
         STMD R55,X14,BKPSAV   ; save (we're using BKP1 for single-step)
TRCSTP   CLM  R26
         LDMD R46,=SAVR4       ; get PC address we're returning to
         JSB  =STBKP1          ; set BKP1 to it (for single stepping)
*
* This is BREAKPOINT end, restore everything and resume normal execution
*
ASMRUN   ADM  R14,=147,0       ; point 1 above ASM ROM save area
*
* FALL THROUGH INTO "END BREAKPOINT" CODE and RESTORE EVERYTHING
*
* the following two lines do: LDM  r45,=06,0334,0141
* ie, R45=6, and R46-47=address of BKPSVC
*
         DATA 145,251,6
         DEF  BKPSVC
*
* BKPSVC is the address JUST after the ASMSAV table of 6 addresses from
* each of which 8 bytes are saved. The following code pops (decrementing
* ptr) 8 bytes of saved memory from ASM RAM and then pushes INDIRECTLY
* through the addresses in the table to restore the contents of RAM
*
RSTLOP   POMD R60,-R14         ; get 8 bytes of saved stuff
         PUMI R60,-R46         ; restore original memory contents
         DCB  R45              ; decrement table entry counter
         JNZ  RSTLOP           ; jif not done
*
         POBD R0,-R6           ; recover E from stack
         BCD
         ERB  R0               ; shift it from R0 into E
         BIN
         LDM  R76,=SAVR74      ; where to restore CPU registers from
         LDB  R0,=73           ; # of bytes of CPU registers to restore
RSTRLP   POBD R*,-R76          ; restore next register from SAVR area
         DCB  R0               ; dec counter
         CMB  R0,=7            ; reached R6?
         JNZ  RSTRLP           ; jif no, loop
         LDMD R2,=SAVR2        ; restore R2-3
         JSB  =CPYHOK          ; re-copy the INTSVC code to SAVR2
ARTN97   RTN
*
* BKP runtime for TRACE command
*
BKPT     JEZ  AERR             ; jif no count, ERROR
         CMB  R20,=16          ; jif anything BUT a count?
         JNZ  AERR             ; jif yes, error
         TSM  R76              ; zero?
         JZR  ARTN97           ; jif yes, ignore
         STMD R76,X14,TRCCNT   ; save TRACE cnt
         POMD R76,-R6          ; throw away return address
         JMP  SNGSTP           ; single-step and trace until TRCCNT=0
*
* Table of keycodes, runtimes, and ASCII name string for BKP commands
*
AKYTAB   DATA 102              ; B
         DEF  BKPB             ; execute BKP command in breakpoint
         DEF  BKPASP           ; `BKP`
*
         DATA 103              ; C
         DEF  BKPC             ; execute CLR command in breakpoint
         DEF  CLRASP           ; `CLR`
*
         DATA 115              ; M
         DEF  BKPM             ; execute MEM command in breakpoint
         DEF  MEMASP           ; `MEM`
*
         DATA 120              ; P
         DEF  BKPP             ; execute PC= command in breakpoint
         DEF  TYPPC            ; "PC="
*
         DATA 122              ; R
         DEF  BKPR             ; execute REG command in breakpoint
         DEF  HDRREG           ; "REG "
*
         DATA 124              ; T
         DEF  BKPT             ; execute TRACE command in breakpoint
         DEF  TYPT             ; "TRACE"
*
* NOTE: The code in KTABLP (061162) EXPECTS the above table to be
* followed by a byte of 316 (JSB at the start of the routine below)!
* Saves a byte by not dedicating a byte to terminating the table.
*
BKPB     JSB  =CONREL          ; get the addr, make it absolute if REL
         JEZ  AERR             ; jif error
         PUMD R#,+R6           ; save it on stack
         CMB  R20,=54          ; COMMA next?
         JNZ  BKPBGO           ; jif no, no output select code
         JSB  =AGTVAL          ; get select code for breakpoint dump
         JEZ  AERR+            ; jif error, clean stack and report
         STM  R#,R36           ; move it
         JSB  =CONBIN          ; convert it to REAL
         BIN
         STMD R40,X14,DBS.C.   ; save the debug output SELECT CODE
         ICM  R10              ; skip EOL(016) byte (DCM r10 at BKPFIN)
BKPBGO   POMD R46,-R6
         CLB  R26              ; clear MSbit
         JSB  =BKPSET          ; set it to SysMon
         JMP  BKPFIN
*
BKPC     CLM  R22
         CLB  R26              ; disable all BKPs
         LDBD R25,X14,DBGWRS   ; get last SysMon command
         JEN  BCONE            ; jif got number
         JSB  =CLRBTH          ; else clear both
BKPFIN   DCM  R10              ; put last char back
         POBD R20,+R10         ; get next char
         CMB  R20,=16          ; EOL?
         JNZ  AERR             ; jif no, error
         RTN                   ; else done
*
BCONE    DRP  R76
         JSB  =BKPCLR          ; clear just the one
         JMP  BKPFIN
*
AERR+    POMD R46,-R6
*
AERR     LDM  R46,=MASMRM      ; address of ASSM ROM error message
         CLB  R17              ; clear XCOM
         JSB  =CPYSTR          ; copy it
         JSB  =DUMPIT          ; dump it
         CLM  R40
         STMD R40,=ERLIN#      ; clear all the ERROR stuff
ARTN96   RTN
*
BKPM     JSB  =CONREL          ; get the addr, make it absolute if REL
         JEZ  AERR             ; jif error
         STM  R#,R36           ; copy it
         DCM  R10              ; put last char back
         JSB  =BKPMEM          ; set up the address in ASM ROM RAM
         POBD R20,+R10         ; get next char
         CMB  R20,=72          ; ':'?
         JNZ  BNOCLN           ; jif no
         JSB  =AGTVAL          ; get ROM#
         JEZ  AERR             ; jif error
         STBD R#,X14,MEMROM    ; save in ASM RAM
         POBD R20,+R10         ; get next char
BNOCLN   CMB  R#,=54           ; COMMA?
         JNZ  MNOCMA           ; jif no
         JSB  =GET#            ; else get the # of bytes
         JEZ  AERR             ; jif error
         JSB  =SMLEN           ; save it in ASM RAM
MNOCMA   CMB  R20,=75          ; '='?
         JNZ  BNOTEQ           ; jif no
         LDMD R26,X14,MEMPTR   ; get MEM ptr
BMLOOP   JSB  =GET#            ; get number to store there
         JEZ  TSTERR           ; jif error
         PUBD R#,+R26          ; else write the byte to memory
         CMB  R20,=54          ; COMMA?
         JZR  BMLOOP           ; jif yes, loop
BNOTEQ   CMB  R20,=16          ; end of line?
         JZR  TSTERR           ; jif yes
AERJMP   JMP  AERR             ; else error
*
BKPP     JEZ  AERR             ; jif error
         CMB  R20,=16          ; end of line?
JNZAER   JNZ  AERR             ; jif no
         LDM  R#,R6            ; copy R6 stack pointer
         SBM  R#,=25           ; adjust to where return addr is on stack
         ARP  R0
         STMD R76,R20          ; store new value (for eventual return)
         STMD R76,=SAVR4       ; also save in saved regs area for disp
TSTERR   TSB  R17              ; any error?
         JNG  ARTN96           ; jif yes
         POMD R22,-R6          ; else pop a return address
         GTO BKREDO            ; redo the breakpoint dump
*
BKPR     JEZ  BKPP             ; jif error
         CMM  R#,=100          ; reg# from 0 to 77?
         ARP  R0
         JCY  AERJMP           ; jif no, too big
         CMB  R20,=75          ; "="?
         JNZ  JNZAER           ; jif no, error
         PUMD R76,+R6          ; save register #
         JSB  =AGTVAL          ; get value to store in register
         POMD R46,-R#          ; recover register #
         JEZ  BKPP             ; jif error
         STBD R76,X46,SAVR0    ; change the value in the register
         JMP  TSTERR           ; redisplay the breakpoint dump
*
DMPFLG   JSB  =SPCDMP          ; blank line after memory dmp
         LDM  R46,=(HDR1).2    ; PC     DR AR BKPS
         JSB  =CPYDMP          ; output HDR1
         JSB  =PRTPC           ; dump PC, DRP, ARP, and BKPs
         LDM  R46,=(HDR2).2    ; "OV CY NG LZ ZR RZ OD DC E"
         JSB  =CPYDMP          ; output HDR2
         LDB  R44,=106         ; invert NOT-LDZ, NOT-Z, and NOT-RDZ flgs
         XRB  R77,R44          ; invert flags so they are LZ, ZR, and RZ
         STB  R75,R54          ; get OVF and CY flags
         JSB  =FRM2FL          ; format them to the output buffer
         STB  R77,R54          ; get NG (MSbit), LZ, ZR, RZ, OD (LSbit)
         JSB  =FRM2FL          ; format NG and LZ to output buffer
         LLB  R54              ; throw away 3 unused bits in the middle
         LLB  R54
         LLB  R54
         JSB  =FRMFLG          ; format ZR to output buffer
         JSB  =FRM2FL          ; format RZ and OD to output buffer
         LLB  R76              ; get DCM (BIN/BCD) to MSbit of R76
         STB  R76,R54          ; copy it to R54
         JSB  =FRMFLG          ; format DCM to output buffer
         POMD R#,-R6           ; get rtn addr & E register from R6 stack
         PUMD R#,+R6           ; put them back
         CLM  R36
         LDB  R36,R55          ; get E
         LDB  R20,=2           ; format 2 digits
         JMP  FRMDMP           ; format them, then dump to DISP or PRINT
*
PRTDRP   ANM  R#,=77           ; keep just the DRP/ARP value
         ARP  R0
         LDB  R20,=2           ; print 2 digits
         JSB  =FRMDGS          ; format them
         DRP  R36              ; return DRP=36 (saves code bytes)
         RTN
*
FRM2FL   JSB  =FRMFLG          ; format 1st flag, fall through to do 2nd
FRMFLG   LDM  R55,=30,20,20    ; when shifted left once, will be "0  "
         LLM  R54              ; next stat bit from R54 into LSbit R55
         PUMD R55,+R30         ; turning R55 to either "0  " or "1  "
         RTN                   ; push and return
*
PRTPC    LDMD R36,=SAVR4       ; get PC where breakpoint occurred
PRT36    JSB  =FRM6DG          ; Format # in R36 as 6 octal digits
         LDM  R76,R6           ; get stack ptr
*
* R6 stack, at this point, looks like:
*  2 BYTES rtn from SPAR0 to interrupted code
*  2 BYTES return from INTSVC to SPAR0
*  3 BYTES SAD (Save Arp/Drp and flags) in INTSVC
*  4 BYTES ERTEMP save in INTSVC
*  2 BYTES return from ROMJSB to INTSVC
*  2 BYTES R0 in ROMJSB
*  1 BYTE  current ROM# in ROMJSB
*  2 BYTES return from BKPSVC to ROMJSB
*  1 BYTE  E save in BKPSVC
*  2 BYTES ASM ROM's RAM 160
*  2 BYTES return from PRTPC
* R6--->
*
         POMD R50,-R76         ; move address back 8 into R6 stack
         POMD R50,-R76         ; move address back 16 into R6 stack
         POMD R75,-R76         ; grab 3-bytes of SAD (interrupt flags)
         LDB  R36,R76          ; OVF, DCM, DRP
         JSB  =PRTDRP          ; format out the DRP value
         LDB  R#,R75           ; OVF, CY, ARP
         JSB  =PRTDRP          ; format out the ARP value
         LDMD R#,X14,DBBKP1    ; get BKP1 address
         JSB  =FRM6DG          ; print it
         LDMD R36,X14,DBBKP2   ; get BKP2 address
         LDB  R20,=6           ; 6 digits
FRMDMP   JSB  =FRMDGS          ; print it
         JSB  =DMPBUF          ; dump the buffer
         RTN
*
HDR1     DATA  `PC     DR AR BKPS` ; breakpoint strings
HDR2     DATA  `OV CY NG LZ ZR RZ OD DC E`
HDRREG   DATA  `REG `
TYPPC    DATA  `PC=`
TYPT     DATA  `TRACE`
*
BKPCMD   JSB  =CPYSTR          ; copy R46-47 str into ASM output buf
         LDB  R46,=40          ; SPACE char
         PUBD R46,+R30         ; put a SPACE on the end
         ICM  R36              ; bump the length
         JSB  =HLFLIN          ; dump to DISP
         JSB  =CLREOL          ; clear the rest of the line
         LDM  R10,R14
         LDM  R26,R14          ; point to start of buffer
EOKEY    JSB  =EOJ2            ; end the key (no repeat)
         JSB  =CURS            ; force the cursor ON
         JSB  =KEYLOP          ; wait for a key
         LDBD R32,=KEYHIT      ; get the keycode
         CMB  R32,=200         ; alphanumeric key?
         JNC  ALNU             ; jif yes
         CMB  R32,=232         ; ENTER? CR?
         JZR  RETKEY           ; jif yes
         CMB  R32,=231         ; BACKSPACE?
         JNZ  EOKEY            ; jif no
         CMM  R26,R14          ; anywhere to back up to?
         JZR  BAKEND           ; jif no, clear the command, too
         JSB  =BKSPC           ; back up one on DISP
         DCM  R26              ; throw away last char in buffer
         JMP  EOKEY
*
ALNU     LDM  R34,R26          ; copy end of buffer
         SBM  R34,=36,0        ; minus 36 octal = 30 decimal
         CMM  R34,R14          ; past beginning of buffer?
         JCY  EOKEY            ; jif no, ignore key
         PUBD R32,+R26         ; add char to buffer
         JSB  =OUTCHR          ; output it to DISP
         JMP  EOKEY
*
RETKEY   JSB  =OUTST-          ; DO CR ACTION ON DISP
         LDB  R#,=16           ; Add a 16 to end of buffer
         PUBD R#,+R26
         JSB  =EOJ2            ; terminate the keystroke
GET#     JSB  =AGTVAL          ; try to get number
         ARP  R10
         JEZ  SDRP76           ; jif failed
         POBD R20,+R10         ; get first byte from buffer (command?)
SDRP76   DRP  R76
         RTN
*
BAKEND   POMD R42,-R6          ; throw away some stuff
         JSB  =FASTBS          ; back up to the start of the line
         GTO NORPET            ; GOTO NORPET (61244-1)
*
STKBIN   LDB  R31,R37          ; copy upper byte
         ANM  R31,=200         ; save MSbit (positive or negative?)
         JSB  =CONBIN          ; convert binary # to REAL
         PUMD R40,+R12         ; push on stack
         TSB  R31              ; was it negative?
         JZR  ARTN60           ; jif no
         LDM  R54,=377,66,125,6 ; load 65536 as INTEGER
         PUMD R50,+R12         ; push on stack
         JSB  =ADDROI          ; neg val + 64K = pos unsigned val
ARTN60   RTN                   ; leave result on R12 stack
*
KEYLOP   LDBD R32,=SVCWRD      ; wait for keyboard interrupt
         JEV  KEYLOP
         JSB  =DECUR2          ; remove cursors from screen
         RTN
*
* This looks for REL(addr) in a BKP or MEM command and converts
* it to an absolute address by adding BINTAB to it
*
CONREL   JEN  CMDEXT           ; jif argument error
         POMD R65,+R10         ; get 3 chars of input after current one
         LDB  R64,R20          ; copy the current char, too
         CMM  R64,=122,105,114,50 ; is it "REL("?
         JNZ  CMDEXT           ; jif no
         JSB  =GET#            ; get the number
         ADMD R#,=BINTAB       ; add BINTAB value to it
         CMB  R20,=51          ; is next char ")"?
         JZR  GOT)             ; jif yes, okay
         CLE                   ; flag error
GOT)     POBD R#,+R#           ; throw away ")", get next char
CMDEXT   DRP  R76
         RTN
*
* Set a BREAKPOINT
*
         DATA 241
BKP.     JSB  =ONER            ; get breakpoint address
         JSB  =GTABAS          ; get ASMBAS into R14
         CMMD R12,=TOS         ; any optional arguments?
         JZR  GTADR1           ; jif no optional arguments, just address
         STMD R40,X#,DBS.C.    ; else save BKP# (huh?  in DBS.C.????)
         JMP  BCONV            ; go get address and convert it
GTADR1   PUMD R40,+R12         ; put address back
BCONV    JSB  =OCTBIN          ; get & convert OCT to BINARY in R46-47
         LDB  R26,=200         ; Master breakpoint enable bit=ON
BKPSET   LDBD R25,X14,DBGWRS   ; get BKP 1 status from ASM ROM RAM
         ANM  R25,=20          ; is BKP 1 enabled (ie, is it set)?
         DRP  R46              ; set DRP to address
         JNZ  STBKP2           ; jif BKP 1 enabled
*
STBKP1   STMD R46,X14,DBBKP1   ; save BKP 1 address
         LDB  R25,=20          ; load "set BKP 1" command (and enable 1)
         JMP  SETBKP
*
STBKP2   STMD R#,X#,DBBKP2     ; save BKP 2 address
         LDB  R25,=62          ; load "set BKP 2" cmd (enable 1 and 2)
*
* R25 = DEBSTS command
* R46-47 = BKP address
*
SETBKP   STBD R#,=DEBSTS       ; write the low byte command
         STBD R46,=DEBBKP      ; store the low byte of the breakpoint
         ICB  R25              ; change the cmd to write the high byte
         STBD R25,=DEBSTS      ; write the hi byte command
         STBD R47,=DEBBKP      ; store the hi byte of the breakpoint
         LDBD R24,X#,DBGWRS    ; get the breakpoint status from ASM RAM
         ANM  R25,=60          ; keep only bkp# enabled bits
         ORB  R25,R24          ; or the other status info in
*
UPSTS    STBD R#,X14,DBGWRS    ; save new bkp status
         ADB  R#,R26           ; add in MS bit (0 or 200)
         STBD R#,=DEBSTS       ; write to SysMon command
         RTN
*
* RUNTIME for CLR breakpoint command
*
         DATA 241
CLR.     JSB  =GTABAS          ; get ASMBAS
         LDBD R25,X#,DBGWRS    ; get BKP status
         CLM  R22              ; zero breakpoint
         LDB  R26,=200
         CMMD R12,=TOS         ; any bkp# ?
         JZR  CLRBTH           ; jif no, clear both
         JSB  =ONEB            ; get BKP#
BKPCLR   DCM  R#               ; was it 1?
         JZR  CLR1             ; jif yes
         DCM  R#               ; was it 2?
         JZR  CLR2             ; jif yes
* anything but 1 or 2 clears both
CLRBTH   STMD R22,X#,DBBKP1    ; write 0 to ASM RAM bkp#1 address
         CLB  R25              ; clear all bits (disable both bkps)
CLR2     STMD R22,X14,DBBKP2   ; write 0 to ASM RAM bkp#2 address
         ANM  R25,=337         ; clear bit 040 (disable bkp 2)
         JMP  UPSTS            ; write to the System Monitor
*
CLR1     STMD R22,X14,DBBKP1   ; write 0 to ASM RAM bkp#1 address
         ANM  R25,=357         ; clear bit 020 (disable bkp 1)
         JMP  UPSTS            ; write to the System Monitor
*
* **********************************************************
* Entry from CHIDLE
* A key has been pressed, maybe handle it.
CHRHOK   LDBD R32,=KEYHIT      ; get keycode
         LDM  R34,=(KTABLE).2  ; address of our table
KLOOP5   POMD R45,+R34         ; get next key from table
         CMB  R45,R32          ; match?
         JZR  TYPAID           ; jif yes, output the typing aid
         CMB  R45,=316         ; end of table?
         JNZ  KLOOP5           ; jif no
         CMB  R32,=213         ; RESET?
         JNC  ARTN90           ; jif lower
         CMB  R32,=221         ; TEST?
         JNC  KFINI            ; jif lower
         CMB  R32,=224         ; LIST?
         JNZ  NOTLST           ; jif no
         JSB  =PREPTK          ; set up stacked token
         LDB  R#,=7            ; ASSEMBLER ROM LIST token
TOKSTK   PUMD R74,+R12         ; push it on the stack
KFINI    ICE
         JSB  =EOJ2            ; end keyhit
         POMD R63,-R6          ; pop RTN to ROMJSB, prev ROM#, saved R0
         POMD R42,-R6          ; toss returns to CHIDLE, CHEDIT & XCBITS
         PUMD R63,+R6          ; push RTN to ROMJSB, prev ROM#, saved R0
ARTN90   RTN                   ; rtn to ROMJSB & then to the EXEC loop
*
KTABLE   DATA 252              ; LOAD
         DEF  ALDSTR           ; ALOAD
         DATA 251              ; STORE
         DEF  ASTSTR           ; ASTORE
         DATA 200              ; K1
         DEF  BASSTR           ; BASIC
         DATA 201              ; K2
         DEF  FLASTR           ; FLABEL
         DATA 202              ; K3
         DEF  FRESTR           ; FREFS
         DATA 215              ; RUN
         DEF  ASSSTR           ; ASSEMBLE
* The table is terminated by the 316 opcode of the following JSB
TYPAID   JSB  =CPYSTR          ; copy the string to the buffer
         JSB  =HLFLIN          ; write it to the disply
         JSB  =CURS            ; turn the cursor on
         JMP  KFINI            ; finish up
NOTLST   CMB  R#,=225          ; PLIST?
         JNZ  ARTN90           ; jif no
         JSB  =PREPTK          ; prepare for the token on the stack
         LDB  R#,=6            ; ASSEMBLER ROM PLIST token
         JMP  TOKSTK
*
PREPTK   STMD R12,=STSIZE      ; set bottom of stack
         LDB  R16,=1           ; set CSTAT to CALC mode
         CLM  R74
         STMD R74,=AUTO#
         STBD R74,=EDMOD2      ; stop insert mode
         LDM  R74,=370,50,0,16 ; 370=OPTROM 050=ASM ROM# 00=tmp 016=EOL
         DRP  R76              ; set DRP to the 00 tmp-TOKEN#
         RTN
*
AROMER   LDBD R36,=ERRORS      ; already an error?
         JNZ  ARTN93           ; jif yes
         LDB  R36,=50          ; ASM ROM#
         STBD R36,=ERRROM      ; claim the error as ours
ARTN93   RTN
*
RSTR10   STMD R10,=SAVR10      ; save it
RSTR6    LDM  R6,=RRSTK        ; TRASH RETURN STACK
         STBD R6,=GINTEN       ; Enable interrupts
GOROMR   GTO ROMRTN            ; GOTO ROMRTN (4762-1)
*
GETMOD   LDMD R56,=ASMBAS      ; base of ASM ROM RAM
         LDBD R56,X56,ASMMOD   ; get ASMMOD (BASIC mode=0 ASM mode=1)
         RTN
*
ONLYBA   JSB  =GETMOD          ; which mode are we in?
         JZR  ARTN61           ; jif BASIC, okay
ERMODE   JSB  =AROMER          ; set ASM ROM as error
         JSB  =ERROR
         DATA 11               ; ILL MODE
RRJMP2   JMP  RSTR10
*
ONLYAS   JSB  =GETMOD          ; which mode are we in?
         JZR  ERMODE           ; jif BASIC, not okay
         RTN
*
* parse BASIC
*
BASIC    JSB  =ONLYAS          ; error if not in ASM mode
         JMP  ABCOM            ; finish common BASIC/ASSEMBLER parsing
*
* parse ASSEMBLER
*
ASMLR    JSB  =ONLYBA          ; error if not in BASIC mode
ABCOM    LDB  R47,R43          ; copy token
         JSB  =ROMTOK          ; push 370 50 r47 tokens
         JSB  =ROMJSB
         DEF  SCAN             ; scan for next token
         DATA 0
         JSB  =DMNDCR          ; error if it's not CR
RRJMP    JMP  GOROMR           ; ROMRTN (end of parsing)
*
ASM$     JSB  =ONLYAS          ; error if BASIC mode
         PUBD R43,+R6          ; save incoming token
         JSB  =ROMJSB
         DEF  GETSTP           ; parse a string expression
         DATA 0
         POBD R47,-R6          ; restore incoming token to r47
ARTN61   RTN
*
FREFS    JSB  =ASM$            ; get a string (or error)
ASMTOK   JSB  =ROMTOK          ; push the ASM ROM token
         JMP  RRJMP            ; ROMRTN
*
ALIST    PUBD R43,+R6          ; save 5=DELETE, 6=PLIST, 7=LIST
         JSB  =ROMJSB
         DEF  G012N            ; get 0, 1, or 2 numbers
         DATA 0
         POBD R47,-R12         ; trash token on stack
         POBD R47,-R6          ; recover incoming token (5,6,7)
         JSB  =GETMOD          ; ASM MODE?
         JNZ  ASMTOK           ; jif yes
*
* in BASIC mode, so we need to parse (push) the system tokens rather
* than the ASSEMBLER ROM's tokens
*
         LDM  R55,=201,236,113 ; system DELETE, PLIST, LIST tokens
         LDB  R0,=50
         ADB  R0,R47           ; R0 = 55, 56, or 57
         PUBD R*,+R12          ; push the appropriate system token
RRJMP3   JMP  RRJMP
*
ASSEMB   JSB  =ASM$            ; error if NOT in ASSEMBLER mode
         PUBD R47,+R6          ; save incoming token
         CMB  R14,=54          ; comma coming up next?
         JNZ  ASSNCO           ; jif no, push default of 0
         JSB  =PARNE2          ; get numeric expression
         JEN  AGOTCO           ; jif got it
BADEXP   JSB  =ERROR
         DATA 121              ; Bad expression
         JMP  RRJMP2
*
ASSNCO   LDB  R40,=4           ; system REAL CONSTANT token
         PUBD R40,+R12         ; push it
         CLM  R40              ; real# 0
         PUMD R40,+R12         ; push it
AGOTCO   POBD R47,-R6          ; recover incoming token
         JMP  ASMTOK           ; go push it
MEMD     PUBD R43,+R6          ; save token
         JSB  =PARNE+          ; scan and get a numeric expression
         JEZ  BADEXP           ; jif failed
         POBD R47,-R6          ; recover keyword token
         JSB  =ROMTOK          ; push it
         CMB  R14,=45          ; colon : token next?
         JNZ  NOCOLN           ; jif no
         JSB  =PARNE+          ; scan & get ROM# for "MEMD addr:rom#"
         JEZ  BADEXP           ; jif failed
         LDB  R47,=25          ; ASM ROM 'colon' token
         JSB  =ROMTOK          ; push it
NOCOLN   CMB  R14,=54          ; comma token?
         JNZ  NOCMMA           ; jif no
         JSB  =PARNE+          ; else scan and get numeric expression
         JEZ  BADEXP           ; jif failed
         LDB  R47,=27          ; ASM ROM 'comma' token
         JSB  =ROMTOK          ; push it
NOCMMA   CMB  R14,=65          ; = token?
         JNZ  MNOT=T           ; jif no
MEMVAL   JSB  =PARNE2          ; scan & get numeric expression
         JEZ  BADEXP           ; jif failed
         CMB  R14,=54          ; comma?
         JZR  MEMVAL           ; jif yes, loop
         LDB  R47,=26          ; ASM ROM = token
         JMP  MEMPSH           ; push it
*
MNOT=T   LDB  R47,=30          ; ASM token - indicating no '='????
MEMPSH   JSB  =ROMTOK          ; push ASM ROM token
         JMP  RRJMP3           ; ROMRTN
*
ROMTOK   LDB  R46,=50          ; ASM ROM#
         LDB  R45,=370         ; system opt-rom-call token
         PUMD R45,+R12         ; push 370 050 token#
ARTN91   RTN
*
* parse BKP command
BKP      PUBD R43,+R6          ; save BKP token
         JSB  =PARNE2          ; SCAN and get NUMEXP
         JEZ  BADEXP           ; jif failed
         CMB  R14,=54          ; COMMA?
         JNZ  BCFIN            ; jif no, done, finish up
         JSB  =PARNE2          ; else get second#
         JEZ  BADEXP           ; jif failed
*
BCFIN    POBD R47,-R6          ; recover keyword token
         JMP  MEMPSH           ; go push it and finish
*
* parse CLR command
*
CLR      PUBD R43,+R6          ; save CLR token
         JSB  =PARNE2          ; SCAN and get NUMEXP if one's there
         JMP  BCFIN            ; go push the token
*
* ***************************************************************
* PRSIDL comes here for parsing during ASSEMBLER mode
* A line is awaiting us in the INPBUF
* ***************************************************************
PRSHOK   LDM  R10,=INPBUF      ; point R10 to input
         JSB  =GCHAR           ; get next char
         JSB  =INTEGR          ; get line# into R40-R47
         BIN
         JEZ  ARTN91           ; jif not found
         LDMD R73,=ERLIN#      ; save error stuff
         PUMD R73,+R6
         LDM  R36,R40          ; get the line#
         STMD R36,=AUTO#       ; save it for auto-numbering
         PUMD R36,+R12         ; push it out
         STMD R12,=STSIZE      ; save stack size
         ICM  R12              ; reserve byte at start for line LEN
         TSM  R36              ; line# 0?
         JZR  LINERR           ; jif yes
         TSM  R42              ; too big (>9999)?
         JNZ  LINERR           ; jif yes
*
* we're in ASSEMBLER mode, so the ON KEY table at 101200 isn't used,
* so we use it for temp storage
*
         STBD R42,=GOODLI      ; write a 0
         LDMD R34,=LAVAIL      ; end of available RAM
         SBM  R34,=0,2         ; minus 512 bytes
         CMM  R34,R12          ; is there at least 512 free bytes?
         JNC  MEMERR           ; jif no, memory overflow
         CMB  R20,=15          ; CR?
         JZR  MTLINE           ; jif yes, delete line
         LDM  R24,R10          ; copy input ptr
         DCM  R24              ; "put back" the char alread fetched
         POMD R24,-R24         ; get the last two chars
         CMM  R24,=40,40       ; SPACE SPACE ? (ie, no label?)
         JZR  NOLABL           ; jif yes
         JSB  =GT!LBL          ; get comment or label
         TSB  R17              ; error?
         JNG  PRSEOL           ; jif yes
         JEZ  PSHEOL           ; jif line done
         JSB  =DUPLB?          ; check for duplicate label
         CMB  R20,=15          ; CR?
         JZR  OPCERR           ; jif yes
NOLABL   CLM  R24              ; indicate we're parsing a line
         LDM  R26,=(OPPRST).2  ; address of opcode parsing table
         JSB  =FINDOP          ; see if it's a valid opcode
         JEN  PRSEOL           ; jif no, maybe expression
         PUMD R65,+R12         ; else push opcode as simple ASCII text
         JSB  X26,ZRO          ; call routine to "parse" the rest of it
         CMB  R20,=40          ; space after the arguments?
         JNZ  NOSPAC           ; jif no
         JSB  =GCHAR           ; skip space
NOSPAC   CMB  R#,=41           ; BANG?
         JNZ  NOBANG           ; jif no, no eol comment
         JSB  =PSHCOM          ; push out eol comment
NOBANG   CMB  R20,=15          ; CR?
         JZR  PRSEOL           ; jif yes
         JSB  =ERREXP          ; else report bad expression
*
* fall through the following error call, which is a nop since there's
* already a reported error
*
LINERR   JSB  =ERROR
         DATA 132              ; LINE >9999
*
* Once one ERROR is set, successive calls to ERROR are ignored, so
* we can save a byte or two by simply falling from the above ERROR call
* through the following.
*
MEMERR   JSB  =ERROR
         DATA 23               ; MEM OVF
*
* Once one ERROR is set, successive calls to ERROR are ignored, so
* we can save a byte or two by simply falling from the above ERROR call
* through the following.
*
OPCERR   JSB  =AROMER          ; set ERROM# to Assembler ROM
         JSB  =ERROR           ; report error
         DATA 13               ; OPCO
*
* Once one ERROR is set, successive calls to ERROR are ignored, so
* we can save a byte or two by simply falling from the above ERROR call
* through the following.
*
         JSB  =AROMER
         JSB  =ERROR
         DATA 12               ; LBL
*
PRSEOL   TSB  R17              ; error reported?
         JNG  AEXPP            ; jif yes, try expression parsing
PSHEOL   LDB  R20,=16          ; EOL token
         PUBD R20,+R12         ; push it out
         STBD R20,=GOODLI      ; EOL token to what WAS 0????
MTLINE   BIN
         LDMD R36,=STSIZE      ; get bottom of stack
         SBM  R36,R12          ; how many bytes on stack?
         NCM  R36              ; subtracted wrong way, so have to negate
         STBI R36,=STSIZE      ; store len into 1st byte of our parsing
         CLB  R16              ; set IDLE mode
         JSB  =CLRPGM          ; set PCB 'type' to MAIN and 0 LENGTH
*
* Assembler source uses the same "file type" in the PCB as MAIN BASIC.
*
         JSB  =ROMJSB
         DEF  LINEDR           ; EDIT the line in (or delete it)
         DATA 0
         JSB  =ALOCUS          ; set pgm len & alloc'd to avoid trouble
         LDBD R#,=GOODLI       ; successfully 'parsed' source line?
         JZR  ANOERR           ; jif yes
         JSB  =DECUR2          ; turn off cursors
* The CRT cursor is currently at the left side of the screen on the line
* BELOW the lines containing the just entered source code.  The CRT RAM
* has only a 4-bit nybble at each address, so it takes TWO addresses for
* each character byte.  Therefore, to calculate the address of the line,
* we have to do CRTDATA- 2*(R10 - INPBUF) or CRTBYT - 2*R10 + 2*INPBUF
         LDMD R#,=CRTBYT      ; get cursor address
         SBM  R#,R10
         SBM  R#,R10           ; subtract 2 x end-of-buffer
         ADM  R#,=INPBUF
         ADM  R#,=INPBUF       ; add 2 x start-of-buffer
         ANM  R#,=300,17       ; AND with 7700 to wrap within alpha RAM
         JSB  =BYTCRT          ; move cursor there
         LDM  R24,R76          ; address of start of 'new' line
         POMD R45,+R24         ; get line# and len
         JSB  =LIST1           ; decompile line & prep for displaying
         JSB  =OUTSTR          ; redisplay the reformatted line
ANOERR   JSB  =UPAUTO          ; update the AUTO#, maybe spitting it out
         TSB  R17              ; error?
         JPS  POK              ; jif no
AEXPP    ICB  R16              ; set CALCULATOR mode
         LDMD R12,=STSIZE      ; get bottom of stack
         DCM  R12
         DCM  R12
         STMD R10,=SAVR10      ; save r10
         JSB  =ROMJSB
         DEF  E.PARS           ; try to get an expression
         DATA 0
POK      POMD R73,-R6          ; recover error values
         TSB  R17              ; error getting expression?
         JNG  SKPERR           ; jif yes
         STMD R73,=ERLIN#      ; restore error values
SKPERR   POMD R63,-R6          ; pop RTN to ROMJSB, prev ROM#, saved R0
         POMD R44,-R6          ; toss rtn to PRSIDL & rtn to PARSER
         PUMD R63,+R6          ; push RTN to ROMJSB, prev ROM#, saved R0
         RTN                   ; rtn to ROMJSB and whoever called PARSER
*
* FIND AN OPCODE
* Input: R20 = next char (first char of opcode)
*        R10 points to 2nd and 3rd chars of opcode
*        R26 = addr of table to do parsing or assembling of the opcode
*        R24 = 0 if PARSING, #0 if ASSEMBLING
* Output:
* if unsuccessful E#0
* else
* 	E=0
* 	R26-27 = opcode 'execution' address from R26 table
*
FINDOP   STB  R20,R65          ; copy first char of opcode
         LDMD R66,R10          ; get next two chars
         ANM  R65,=337,337,337 ; force uppercase on all three
FNDOP-   LDM  R20,=(OPTABL).2  ; address of opcode table
         CLM  R22              ; opcode counter
OPCLOP   CLE                   ; clear error flag
         CMMD R65,R20          ; match?
         JZR  GOTOPC           ; jif yes
         ADM  R20,=3,0         ; bump table ptr
         ICB  R22              ; increment opcode counter
         CMB  R22,=127         ; end of table?
         JNZ  OPCLOP           ; jif no, loop
         TSM  R24              ; parsing a line?
         JNZ  NLP              ; jif no
         JSB  =AROMER          ; set Assembler ROM error
         JSB  =ERROR           ; report error
         DATA 13               ; OPCO
NLP      ICE                   ; indicate error happened
         RTN
*
GOTOPC   TSM  R24              ; parsing a line?
         JNZ  NOADV            ; jif no
         ICM  R10              ; skip the last two bytes of the opcode
         ICM  R10
NOADV    LLM  R22              ; double the opcode# for address indexing
         ADM  R26,R22          ; add to base of opcode 'execution' table
         LDMD R26,R26          ; get the address of the routine
         JSB  =GCHAR           ; get next char after the 3-char opcode
         RTN
*
OPTABL   DATA  "ARPDRPELBELMERBERMLLBLLM" ; 0
         DATA  "LRBLRMICBICMICEDCBDCMDCE" ; 10
         DATA  "TCBTCMNCBNCMTSBTSMCLBCLM" ; 20
         DATA  "CLEORBORMXRBXRMBINBCDSAD" ; 30
         DATA  "RTNPADLDBLDMSTBSTMCMBCMM" ; 40
         DATA  "ADBADMSBBSBMANMPOBPOMPUB" ; 50
         DATA  "PUMJCYJEVJENJEZJLZJLNJMP" ; 60
         DATA  "JNOJNGJNZJNCJODJPSJRZJRN" ; 70
         DATA  "JSBJZRBSZABSASPBYTGTOASC" ; 100
         DATA  "DEF"            ; 110
         DATA  "NAM"
         DATA  "VAL"
GLONAM   DATA  "GLO"
         DATA  "FIN"
         DATA  "LST"
         DATA  "UNL"
         DATA  "LNK"
ORGNAM   DATA  "ORG"
SETNAM   DATA  "SET"
CLRNAM   DATA  "CLR"
AIFNAM   DATA  "AIF"
EIFNAM   DATA  "EIF"
DADNAM   DATA  "DAD"
EQUNAM   DATA  "EQU"
*
* TABLE OF OPCODE PARSING ROUTINES
*
OPPRST   DEF  P1REG            ; ARP
         DEF  P1REG            ; DRP
         DEF  P1REG            ; ELB
         DEF  P1REG            ; ELM
         DEF  P1REG            ; ERB
         DEF  P1REG            ; ERM
         DEF  P1REG            ; LLB
         DEF  P1REG            ; LLM
         DEF  P1REG            ; LRB
         DEF  P1REG            ; LRM
         DEF  P1REG            ; ICB
         DEF  P1REG            ; ICM
         DEF  ARTN88           ; ICE
         DEF  P1REG            ; DCB
         DEF  P1REG            ; DCM
         DEF  ARTN88           ; DCE
         DEF  P1REG            ; TCB
         DEF  P1REG            ; TCM
         DEF  P1REG            ; NCB
         DEF  P1REG            ; NCM
         DEF  P1REG            ; TSB
         DEF  P1REG            ; TSM
         DEF  P1REG            ; CLB
         DEF  P1REG            ; CLM
         DEF  ARTN88           ; CLE
         DEF  PORXR            ; ORB
         DEF  PORXR            ; ORM
         DEF  PORXR            ; XRB
         DEF  PORXR            ; XRM
         DEF  ARTN88           ; BIN
         DEF  ARTN88           ; BCD
         DEF  ARTN88           ; SAD
         DEF  ARTN88           ; RTN
         DEF  ARTN88           ; PAD
         DEF  PLDST            ; LDB
         DEF  PLDST            ; LDM
         DEF  PLDST            ; STB
         DEF  PLDST            ; STM
         DEF  PADSB            ; CMB
         DEF  PADSB            ; CMM
         DEF  PADSB            ; ADB
         DEF  PADSB            ; ADM
         DEF  PADSB            ; SBB
         DEF  PADSB            ; SBM
         DEF  PADSB            ; ANM
         DEF  PPUPO            ; POB
         DEF  PPUPO            ; POM
         DEF  PPUPO            ; PUB
         DEF  PPUPO            ; PUM
         DEF  PLBREF           ; JCY
         DEF  PLBREF           ; JEV
         DEF  PLBREF           ; JEN
         DEF  PLBREF           ; JEZ
         DEF  PLBREF           ; JLZ
         DEF  PLBREF           ; JLN
         DEF  PLBREF           ; JMP
         DEF  PLBREF           ; JNO
         DEF  PLBREF           ; JNG
         DEF  PLBREF           ; JNZ
         DEF  PLBREF           ; JNC
         DEF  PLBREF           ; JOD
         DEF  PLBREF           ; JPS
         DEF  PLBREF           ; JRZ
         DEF  PLBREF           ; JRN
         DEF  PJSB             ; JSB
         DEF  PLBREF           ; JZR
         DEF  BSZORG           ; BSZ
         DEF  PABS             ; ABS
         DEF  PASP             ; ASP
         DEF  PNXTO            ; BYT
         DEF  PLBREF           ; GTO
         DEF  PASP             ; ASC
         DEF  PLBREF           ; DEF
         DEF  PLBREF           ; NAM
         DEF  PLBREF           ; VAL
         DEF  PGLO             ; GLO
         DEF  ARTN88           ; FIN
         DEF  ARTN88           ; LST
         DEF  ARTN88           ; UNL
         DEF  PLNK             ; LNK
         DEF  BSZORG           ; ORG
         DEF  PLBREF           ; SET
         DEF  PLBREF           ; CLR
         DEF  PLBREF           ; AIF
         DEF  ARTN88           ; EIF
         DEF  PDADEQ           ; DAD
         DEF  PDADEQ           ; EQU
*
GT!LBL   CMB  R20,=41          ; BANG?
         JNZ  NOBNG            ; jif no
PSHCOM   LDB  R#,=376          ; REM token
REMCHR   PUBD R#,+R12          ; push it out
         POBD R#,+R10          ; get next char
         CMB  R#,=15           ; CR?
         JNZ  REMCHR           ; jif no
TRIMSP   POBD R22,-R12         ; get last char pushed
         CMB  R22,=40          ; space?
         JZR  TRIMSP           ; jif yes, trim trailing spaces
         PUBD R22,+R12         ; put last char back
         CLE                   ; flag successful
         RTN
*
NOBNG    CLE
         ICE                   ; flag failed to get REM
         LDMD R41,=BLANKS      ; load 7 SPACE characters
         LDB  R41,=377         ; LABEL token
         LDB  R0,=42           ; where to start copying the label (R42)
LBLLOP   STB  R20,R*           ; copy a char
         ICB  R0               ; move to next reg
         CMB  R0,=51           ; done? (label plus space in R50)
         JNZ  LBLOK            ; jif no
         JSB  =LBLERR          ; label too long, error
         RTN
*
LBLOK    POBD R20,+R10         ; get next char from input
         CMB  R20,=15          ; CR?
         JZR  PSHLBL           ; jif yes
         CMB  R20,=40          ; space (end of label)?
         JNZ  LBLLOP           ; jif no, get more
         JSB  =GCHAR           ; get next char into R20
PSHLBL   PUMD R41,+R12         ; push line leng & the blank-filled label
         RTN
*
DUPLB?   BIN
         JSB  =GTSTRT          ; get start of 'pgm' src, just after PCB
FLBLOP   POMD R32,+R30         ; get first line#
         CMM  R32,=231,251     ; 'permanent' END line# A999?
         JZR  ARTN92           ; jif yes
         CLM  R34
         POBD R34,+R30         ; get line length as WORD
         CMMD R41,R30          ; see if label is at start of line
         JZR  FNDLBL           ; jif found matching label
NXTLIN   ADM  R30,R34          ; else skip line
         JMP  FLBLOP
*
FNDLBL   CMMD R32,=AUTO#       ; matching label on same line#?
         JZR  NXTLIN           ; jif yes, not a dupe, keep searching
         ICE                   ; flag problem
         TSB  R0               ; called from FLABEL?
         JZR  ARTN92           ; jif yes, else called from PRSHOK
*
         PUMD R40,+R6          ; save R40-47 on stack
         STMD R32,=SAVER6      ; save line# in SAVER6
         STMD R32,=FLDCOM      ; set FirstLineDeCOMpile to that line
         LDM  R46,=(WDUPLB).2  ; R46-47 = addr of "DUPE LABEL" message
         JSB  =PRTERR          ; print it
         POMD R40,-R6          ; recover R40-47
         ICE
ARTN92   RTN
* ****************************************************************
* BASIC
* ****************************************************************
         DATA 141
BASIC.   JSB  =STBAS1          ; load ASM RAM ptr & set us to BASIC mode
         LDB  R#,=236          ; load RTN instruction into R40
         LDM  R41,R40          ; ripple-copy it through R41-47
         STMD R41,=CHIDLE      ; store 7 RTNs to CHIDLE (release hook)
         STMD R41,=PRSIDL      ; and release PRSIDL, too
ASMSUB   JSB  =ERMSGS          ; do a SCRATCH
SPITRD   LDM  R46,=(MREADY).2  ; READY message
SPITR-   JSB  =CPYSTR          ; copy it out
         JSB  =DODISP          ; set the CRT as the output device
         JSB  =DUMPIT          ; dump the message
         RTN
*
* **************************************************************
* ASSEMBLER
* **************************************************************
         DATA 141
ASMLR.   JSB  =ASMSUB          ; SCRATCH and spit READY message
         JSB  =ALOCUS          ; look like it's ALLOCATED BASIC program
* INIPGM at end of ALOCUS leaves R34=FWCURR and DRP=67
         LDB  R#,=200          ; SECURITY protects against STORE in ASM
         STBD R#,X34,P.SFLG    ; save it in the PCB
*
* The following does LDM R41,= "JSB=ROMJSB  DEF CHRHOK  DATA50  RTN"
ASMRST   DRP  R41
         DATA 251              ; load code for CHIDLE
         JSB  =ROMJSB
         DEF  CHRHOK
         DATA 50
         RTN
*
*
         STMD R#,=CHIDLE       ; take over CHIDLE keyboard hook
         LDM  R36,=PRSHOK      ; modify the code for taking PRSIDL
         STM  R36,R44          ; change CHRHOK addr in R44-45 to PRSIDL
         STMD R41,=PRSIDL      ; take over PRSIDL parsing hook
         JSB  =GTABAS          ; get ASM RAM ptr
         STBD R15,X#,ASMMOD    ; set flag (non-zero) we're in ASM mode
         RTN
*
MREADY   DATA  `READY`
*
* ***********************************************
* FLABEL
* ***********************************************
         DATA 141
FLBL.    JSB  =POPLBL          ; label in R42-47, R30=ptr start of src
         JZR  FDONE            ; jif no/empty label
         CLM  R0               ; clear auto-numbering
         STMD R0,=AUTO#
         JSB  =DUPLB?          ; find the label
         JEZ  FDONE            ; jif not found
FLBLLP   JSB  =DSPLIN          ; display the found line
         CLE
         JSB  =NXTLIN          ; again, in case label's on more lines
         JEN  FLBLLP           ; jif found again, loop
FDONE    JMP  SPITRD           ; else done
*
DSPLIN   JSB  =PSHRGS          ; save registers
         STMD R32,=FLDCOM      ; save line# of label
         STM  R32,R45          ; copy to R45-46
         STB  R34,R47          ; line len in R47
         STM  R30,R24          ; address of line for LIST
         JSB  =LIST1           ; decompile the line
         JSB  =DUMPIT          ; display it
         JSB  =POPRGS          ; restore registers
         RTN
*
* *******************************************
* FREFS
* *******************************************
         DATA 141
FREFS.   JSB  =POPLBL          ; get the label and setup
         JZR  FDONE            ; jif no label
FROLOP   POMD R32,+R30         ; get line#
         CMM  R32,=231,251     ; A999? (final hidden END line?)
         JZR  FDONE            ; jif yes
         CLM  R34
         POBD R34,+R30         ; line len
         LDM  R36,R30          ; copy line ptr
         LDM  R26,R30
         ADM  R26,R34          ; end of line ptr
FRILOP   POBD R40,+R36         ; get next byte of line
         CMB  R40,=377         ; label?
         JZR  FRGOTIT          ; jif yes
FREND?   CMM  R36,R26          ; end of line?
         JNZ  FRILOP           ; jif no
FRNEXT   LDM  R30,R26          ; point overall search ptr to end of line
         JMP  FROLOP           ; go search next line
*
FRGOTIT  POMD R52,+R36         ; get the label
         CMM  R52,R42          ; match the one we're looking for?
         JNZ  FREND?           ; jif no
         JSB  =DSPLIN          ; display the line
         JMP  FRNEXT           ; go to next line and continue searching
*
POPLBL   BIN
         JSB  =DODISP          ; set CRT as output device
         POMD R22,-R12         ; get string address
         POMD R24,-R12         ; get string len
         JZR  ARTN83           ; jif 0 len, nothing to do
         CMB  R24,=7           ; too long?
         JNC  LLENOK           ; jif no, okay
         LDB  R24,=6           ; limit len
LLENOK   LDB  R0,=42           ; point at R42
         ADB  R0,R24           ; plus len of string
         LDMD R42,R22          ; get the label string
* fall through and fill the label with trailing blanks
*
* The following code loads blanks into the register pointed to by R0,
* up to 8 of them.  The rest (that don't get loaded) are processed
* as ARP 40 instructions.
*
         DRP  R*
         DATA 251
BLANKS   DATA 40
         DATA 40
         DATA 40
         DATA 40
         DATA 40
         DATA 40
         DATA 40
         DATA 40
*
         LDB  R41,=377         ; put a LABEL 'token' in front of it
GTSTRT   CLE
         LDMD R30,=FWCURR      ; point at source code PCB
         ADM  R30,=30,0        ; point at first line of source code
ARTN83   RTN
*
* SCRATCHBIN
*
* ********************************************************
* SCRATCHBIN
* ********************************************************
         DATA 241              ; attribs: BASIC stmt legal after THEN
SCRTB.   LDB  R22,=2           ; ROMFL=2 means SCRATCH
         STBD R22,=ROMFL
*
         JSB  =ROMJSB
         DEF  BPINI            ; call the binary program's INIT routine
         DATA 0
*
         BIN
         LDMD R24,=BINTAB      ; get base address of BPGM
         JZR  ARTN82           ; jif 0, none loaded
         STBD R24,=GINTDS      ; disable global interrupts
         STM  R24,R22          ; copy BINTAB
         DCM  R24              ; -1 = last byte of what to copy/move
         SBMD R22,=LAVAIL      ; BINTAB-LAVAIL = how much to move
         LDMD R26,=LWAMEM      ; highest memory address
         JSB  =MOVDN           ; move CALCVRBs, tmpmem, for/next stk,etc
         LDMD R30,=LWAMEM      ; highest memory address
         SBMD R30,=BINTAB      ; -BINTAB = offset of movement - 1
         ICM  R30              ; offset of movement
         LDB  R22,=5           ; # (LAVAIL,CALVRB,RTNSTK,NXTRTN,FWBIN)
         LDM  R26,=LAVAIL      ; address of first ptr
ADJLOP   LDM  R36,R30          ; get next ptr
         ADMD R36,R26          ; add offset to it
         PUMD R36,+R26         ; store back out
         DCB  R22              ; dec loop counter
         JNZ  ADJLOP           ; jif not done
         CLM  R22
         STMD R22,=BINTAB      ; zero BINTAB (no binary loaded)
         STBD R22,=GINTEN      ; enable global interrupts
ARTN82   RTN
*
CLRPGM   JSB  =GTFWCU          ; get ptr to FWCURR
         CLM  R65
         STMD R65,X#,P.TYPE    ; set BASIC MAIN program and 0 len
         RTN
*
* ************************************************************
* DELETE
* ************************************************************
         DATA 141
DEL.     JSB  =CLRPGM          ; set P.TYPE, P.LEN to 0 (de-allocated)
         JSB  =ROMJSB
         DEF  DELET.           ; delete the assembler source lines
         DATA 0
*
* now (fake) re-allocate us, so system doesn't mess with source code
*
ALOCUS   JSB  =GTFWCU          ; get ptr to FWCURR in R56
         LDB  R66,=40          ; allocated bit for P.TYPE
         LDBD R67,X#,P.TYPE    ; get PCB type byte
         ORB  R67,R66          ; set the allocated bit
         STBD R67,X56,P.TYPE   ; save it
         JSB  =ROMJSB
         DEF  INIPGM           ; calc 'program' length and set it in PCB
         DATA 0
         RTN
*
* **********************************************************
* TREM
* **********************************************************
         DATA 141              ; attribs: non-programmable BASIC stmt
TREM.    JSB  =GTABAS          ; get ASM RAM ptr
         LDBD R20,X#,EOLREM    ; get hide/show remarks flag
         DCB  R20              ; 0->377, 1->0
         JZR  TREMST           ; jif 1->0
         LDB  R20,=1           ; 0->377, change to 1
TREMST   STBD R#,X#,EOLREM     ; save toggled flag
         RTN
*
* *************************************************************
* PLIST
* *************************************************************
         DATA 241              ; attribs: programmable BASIC statement
PLST.    JSB  =DOPRNT          ; set output device to PRINTER IS
         JMP  LST-             ; do rest of LIST
*
* *************************************************************
* LIST
* *************************************************************
         DATA 241              ; attribs: programmable BASIC statement
LST.     JSB  =DODISP          ; set output device to CRT IS
LST-     BIN
         LDMD R46,=LDFLTR      ; list break line count
         STMD R46,=MTFLAG      ; save temp copy of it
         JSB  =LIST1P          ; set LLDCOM to list one page
         JSB  =COPSUB          ; get SCTEMP (real) to R46-47 (bin)
         CMB  R#,=4            ; =4? (internal printer?)
         JNZ  LNOT4            ; jif no
         JSB  =CRTPOF          ; turn off the CRT
LNOT4    CMB  R46,=2
         JZR  L2               ; jif yes
*
         LDM  R74,=231,231,0,0 ; first line=0, last line==9999
         STMD R74,=LLDCOM      ; set last line decompile
L2       LDB  R0,=1            ; secure against LISTING
         JSB  =SECUR?          ; check security, gen error if so
*
         JSB  =ROMJSB
         DEF  TO?I             ; get 0, 1, or 2 args from stk as INTs
         DATA 0
*
         JEZ  LNOARG           ; jif none
         LDM  R26,R45          ; get first line argument
         STMD R26,=FLDCOM      ; save as FirstLineDeCOMpile
         DCE                   ; two arguments?
         JEZ  LNOARG           ; jif no, only first line#
         LDM  R26,R55          ; copy ending line#
         STMD R26,=LLDCOM      ; save as LastLineDeCOMpile
LNOARG   LDMD R76,=FLDCOM      ; get first line to list
*
         JSB  =ROMJSB
         DEF  FNDLIN           ; find the line
         DATA 0
*
         LDM  R24,R36          ; copy the ptr
LSTNLI   CMB  R17,=300         ; error finding the line?
         JCY  LSTEND           ; jif yes, bail
         LDBD R15,=SVCWRD      ; check if a key has been hit
         JOD  LSTEND           ; jif yes, abort the list
         LDMD R46,R24          ; get the line#
         STMD R46,=FLDCOM      ; save it as the new first line to list
         JSB  =ADCOML          ; list the line
         JEZ  LSTMEM           ; jif error, abort
         LDMD R76,=LLDCOM      ; get last line to list
         CMB  R77,=252         ; AA (page mode)? (if so r76 = line cnt)
         JNZ  LSTPRT           ; jif no, not page mode
DLNCNT   DCB  R76              ; dec line counter
         SBM  R66,=40,0        ; longer than 32 characters?
         JZR  LSVLLD           ; jif no, EXACTLY 32!
         JPS  DLNCNT           ; jif MORE than 32
LSVLLD   STBD R76,=LLDCOM      ; save new last line info
         JNG  LSTEND           ; jif reached end
LSTPRT   JSB  =COPSUB          ; get the select code of output device
         STB  R46,R45          ; save it in 45
         LDMD R46,X46,LISTBL   ; get address of output routine
*
         JSB  =ROMJSB
         DEF  DRV12+           ; output it
         DATA 0
*
         JMP  LSTNLI           ; go list the next line
*
LSTMEM   JSB  =ROMJSB
         DEF  LSRTN+           ; setup for freemem at end of list
         DATA 0
*
LSTEND   JSB  =ROMJSB
         DEF  CRTPUP           ; power up the CRT if it was powered-down
         DATA 0
         RTN                   ; done
*
ADCOML   POMD R45,+R24         ; get next line# and len
         BIN
         CMM  R45,=231,251,2   ; is it FINAL (hidden END) line?
         JZR  DCNFND           ; jif yes
         LDMD R36,=LLDCOM      ; get LastLineDeCOMpile
         BCD
         CMM  R36,R45          ; are we less than the last line to list?
         BIN
         JNC  DC1ERR           ; jif no, we're past it
*
* R45-46 = line#
* R47 = line len
* R24 = ptr to next byte AFTER line len
*
LIST1    CLB  R30
         STBD R30,=LSTFLG      ; turn off listing
         LDM  R30,=INPBUF      ; address of output buffer
         JSB  =DCOM1L          ; decompile line# R45/R24
         CMB  R17,=300         ; errors?
         JCY  DC1ERR           ; jif yes
         LDM  R26,=INPBUF      ; address of what to display
         LDB  R36,=15          ; CR character
         PUBD R36,+R#          ; add it to the end of the buffer
         LDM  R36,R#           ; copy the end of the buffer ptr
         SBM  R36,R26          ; minus the start = len
         STM  R36,R66          ; copy len
         CLE
         ICE                   ; flag successful
         RTN
*
DC1ERR   CLB  R47
DCNFND   CLE                   ; flag error
         RTN
*
* Decompile one line
* R45-46 = line#
* R47 = line len
* R24 = ptr to next byte AFTER line len
*
DCOM1L   CLB  R36
         STBD R36,=PRECNT      ; clear so system won't do...
         STBD R36,=ONFLG       ; ... decompile of src code
         STBD R36,=COMFLG      ; set not common vars
         LDM  R36,R45          ; copy line# from R45-46
         JSB  =DCLIN#          ; decompile it to R30 buffer
DCLST    LDMD R50,=BLANKS      ; get 8 blanks
         LDBD R20,R24          ; get next byte of line
         CMB  R20,=376         ; is it a REMARK?
         JZR  DCREM            ; jif yes
         JCY  DCLABL           ; jif there's a LABEL
         PUMD R51,+R30         ; if no label, push SEVEN SPACES
DCOPC    POMD R55,+R24         ; get the OPC
         PUMD R55,+R30         ; push it to output buffer
         POBD R20,+R24         ; get next byte after 3-char opcode
         CMB  R20,=111         ; 'I'?
         JZR  DCOPC4           ; jif yes
         CMB  R20,=104         ; 'D'?
         JZR  DCOPC4           ; jif yes
DCNXT+   PUBD R50,+R30         ; else push it out
DCNEXT   CMB  R20,=376         ; eol remark?
         JZR  DCEOLR           ; jif yes
         JCY  DCGCH            ; jif LABEL
         CMB  R20,=16          ; is it EOL?
         JZR  RTNA30           ; jif yes
         CMM  R30,=ERBEND      ; output buffer full?
         JZR  DCFULL           ; jif yes
DCCHAR   PUBD R20,+R30         ; push next char out
         POBD R20,+R24         ; get next byte of input
         JMP  DCNEXT
*
DCREM    POBD R20,+R24         ; skip the 376 label token
DCBANG   LDB  R20,=41          ; ASCII '!' character
         JMP  DCCHAR
*
DCLABL   POMD R51,+R24         ; get 0377 label token & 6 chars of label
         PUMD R52,+R30         ; push 6 chars of label to output buffer
         PUBD R50,+R30         ; push trailing SPACE
         JMP  DCOPC
*
DCOPC4   PUBD R20,+R30         ; push 4th char of opcode
         POBD R20,+R24         ; get next char
         JMP  DCNXT+
*
DCEOLR   JSB  =GTABAS          ; get base of ASM RAM
         LDBD R#,X#,EOLREM     ; hide EOL remark?
         JNZ  DCSHOW           ; jif no
DCHIDE   POBD R#,+R24          ; get next char of line
         CMB  R#,=16           ; EOL token?
         JNZ  DCHIDE           ; jif no, skip entire comment
         JMP  RTNA30
*
DCSHOW   LDM  R76,=INPBUF      ; address of output buffer
         ADM  R76,=40,0        ; skip to column 32 dec
         LDBD R75,=LSTFLG      ; display or printer?
         JZR  DCCRT            ; jif display
         ADM  R76,=12,0        ; bump comment over another 10 dec cols
DCCRT    PUBD R50,+R30         ; push out space
         CMM  R30,R76
         JNC  DCCRT            ; until we reach the desired column
         JMP  DCBANG
*
DCGCH    POBD R20,+R24         ; get next char
         JMP  DCNEXT
*
DCFULL   DCM  R#               ; move output buffer ptr back from end
DCSKPE   POBD R20,+R24         ; get next byte
         CMB  R20,=16          ; EOL token?
         JNZ  DCSKPE           ; jif no, skip to end of line
RTNA30   ARP  R30
         RTN
*
* Collect all the available space together, with all the code and
* the label table moved down to the end of available memory.
*
DATDN    LDMD R24,=ACODEN      ; end of src to move
         LDMD R26,=ALAVAI      ; dest (end of memory)
         STMD R26,=ACODEN      ; set new location for 'src'
         STM  R26,R36          ; copy dest
         LDM  R22,R24          ; copy src
         SBMD R22,=ALBTBL      ; len of src-1
         ICM  R22              ; len of src
         SBM  R36,R24          ; offset being moved by
         LDMD R34,=ACODBA      ; another ptr
         ADM  R34,R36          ; adjust that ptr by distance moved
         STMD R34,=ACODBA      ; resave it
         LDMD R34,=ALBTBL      ; beginning of what we're moving
         ADM  R34,R36          ; adjust it
         STMD R34,=ALBTBL      ; resave it
         JSB  =MOVDN           ; move them down (to end of avail memory)
         RTN
*
* recenter the code and the label table, splitting the available space
* above and below.
*
RECNTR   JSB  =DATDN           ; mov it all down
RECNT-   LDMD R26,=ALBTBL      ; address of end of hole (start of data)
         STM  R26,R24          ; set as source
         STM  R26,R36          ; copy
         SBM  R26,R12          ;  -start of hole = available space
         LRM  R27              ; find center of available space
         ADM  R26,R12          ; add it to base to get new center
DATUP-   STMD R#,=ALBTBL       ; save as new location
         LDMD R22,=ACODEN      ; get end of data
         STM  R22,R34          ; copy
         SBM  R22,R24          ; len of data to move
         SBM  R36,R26          ; offset of how far we're moving
         SBM  R34,R36          ; adjust end-address
         STMD R34,=ACODEN      ; resave it
         LDMD R34,=ACODBA      ; get mid-address
         SBM  R34,R36          ; ajdust it
         STMD R34,=ACODBA      ; resave it
         JSB  =MOVUP           ; move em back up
         RTN
*
* Collect all the available space together with all the code and
* the label table moved up to the beginning of available memory.
*
DATUP    LDMD R24,=ALBTBL      ; get the beginning of the data
         STM  R24,R36          ; copy
         LDM  R26,R12          ; get destination (start of avail memory)
         ADM  R26,=100,0       ; leave 64 bytes available
         JMP  DATUP-           ; go move it
*
CMEMBT   LDMD R22,=ALAVAI      ; end of available memory
         SBM  R22,=ACODEN      ; minu end of data
CKMEM-   CMM  R#,=200          ; at least 128 bytes left?
         ARP  R0
         RTN
*
CMEMTP   LDMD R22,=ALBTBL      ; get start of data
         SBM  R22,R12          ; minus start of top space
         JMP  CKMEM-           ; 128 bytes left at top?
*
FNMERR   JSB  =ERROR+
         DATA 103              ; ERROR: File name
*
* **********************************************************************
* * ASSEMBLE "filename" [,dont-load-bpgm]
* **********************************************************************
* NOTE: At Assemble-time, the ASM ROM uses storage
* for the LEGEND (key labels) and KEYTAB (ON GOSUB
* table) for variables, since they're not used while
* in Assembler mode and get reloaded going back to
* BASIC. See the DAD's at the top of the file for a
* list of the various variable-to-memory assignments.
*
* The Assembler uses all of memory between NXTMEM and
* LAVAIL to store references to so-far-undefined labels,
* the label table (defined and undefined), and the code
* as it's assembled.  The references to so-far-undefined
* labels is a table (or heap) of pairs of 2-byte entries
* between NXTMEM and R12.  Each pair contain an offset
* into the label table to the label that was referenced
* but not yet defined, and an offset into the code where
* the reference was made.  Every time a new label is
* encountered (DEFINED!), the ASM ROM searches through
* the list of references to see if there were any
* forward-references to it (because the label table offset
* matches) then the code offset from the table is used
* to insert the appropriate address or offset (depending
* upon the type of reference.
*
* The label table and code are kept together in the
* middle of available memory, with the label table growing
* upward towards R12/NXTMEM, and the code growing downward
* toward LAVAIL.  A minimum of 128 dec bytes is maintained
* between the end of the label table and R12 and between
* the end of the code and the end of available memory.
* When it gets too small on one end or the other, the label
* table and code gets re-centered.  So, memory looks like this:
*
*  lower addresses
*   |						|
*   +-----------------------+
*   |	Forward references	| <-- NXTMEM
*   ...						...
*   |		list			|
*   |						|
*   +-----------------------+
*   |						| <-- R12 (may be same as NXTMEM if
*   ...	free memory		   ...       forward-references list is empty)
*   |						|
*   +-----------------------+
*   |						| <-- ALBTBL (100720) growing-end of lbl tbl
*   |		Label			|
*   ...					   ...
*   |		table			|
*   |						|
*   +-----------------------+
*   |						| <-- ACODBA (100722) start of output code
*   |		output			|
*   ...	   assembled	   ...
*   |		 code			|
*   |						|
*   +-----------------------+
*   |						| <-- ACODEN (100724) end of output code
*   |						|
*   ...	free memory		   ...
*   |						|
*   |						| <-- ALAVAI (end of Assembler's avail mem
*   +-----------------------+
*   |	512 'safety' bytes	|
*   | for CALC MODE stuff	| <-- LAVAIL
*   +-----------------------+
* 	|						|
*  higher addresses
*
*  So, the ASM ROM makes a single pass through the source code,
*  building the output code at ACODEN, and keeping a table of
*  labels and a table of label forward-references.  (If the label
*  is already defined when it's referenced, then of course the
*  actual value can be used right then and there, removing any
*  need for adding to the forward-reference table. When forward
*  references are resolved, they are removed from the forward
*  reference table.
*
*  The entries on the "forward references list" (or table) consist
*  of pairs of 16-bit offsets.  The first (at the lower address)
*  contains the offset from ACODBA to the label in the label table.
*  The second (at the higher address) is the offset from ACODBA
*  into the code being assembled of where the label was referenced.
*
*  When the FIN is encountered at the end of the assembly, then
*  if there are any unresolved forward references and a global
*  file was specified, then the label table gets replaced with the
*  pre-assembled GLO file and another pass is done to try to satisfy
*  the unresolved forward references.
*
* **********************************************************************
         DATA 141              ; attrib: non-programmable BASIC stmt
ASMBL.   JSB  =ONEB            ; get dont-load-bpgm flag
* (0 was pushed during parse if none provided)
         ORB  R#,R47           ; OR two bytes together
         STBD R#,=ALODBP       ; save as a single byte flag
         CLM  R36
         STMD R36,=GNMLEN      ; ...in LEGEND area
         LDM  R56,=LAST+1      ; load addr of ERRBUF (same as LAST+1)
         STM  R56,R46          ; copy it
         POMD R24,-R12         ; get address of target BPGM file name
         POMD R26,-R12         ; get len of file name
         JZR  FNMERR           ; jif 0 len, error
         CMM  R26,=140,0       ; len > 96 dec
         JNC  AFNLOK           ; jif no
         LDM  R26,=140,0       ; limit to 96 dec
AFNLOK   POBD R30,+R24         ; copy the input filename
         PUBD R30,+R56         ;   to ERRBUF
         DCM  R26              ; dec len
         JNZ  AFNLOK           ; loop til copied
         LDB  R26,=16          ; put an EOL token on the end of it
         PUBD R26,+R56
         LDM  R56,=ABPNAM      ; where to put the cleaned-up BPGM name
         JSB  =GFNAME          ; 'parse' filename to <=10 chars & MSUS
         STMD R#,=ABNLEN       ; DRP 46, save len of filename
         LDMD R12,=NXTMEM      ; R12 stack is empty, we start at NXTMEM
         STMD R12,=AIFFLG      ; set conditional-assembly flag ON
         CLM  R40
         STMD R40,=KEYTAB      ; zeroes to all 16 bytes of KEYTAB
         STMD R40,=KYTB+8      ; first 8 and second 8
         LDMD R22,=LAVAIL      ; LAVAIL
         SBM  R22,=0,2         ;   -512 bytes
         STMD R22,=ALAVAI      ; =safe end of what we'll use
         LRM  R23              ; divide by 2
         LDM  R24,R12          ; get R12 ptr (NXTMEM)
         LRM  R25              ; divide by 2
         ADM  R22,R24          ; midway twixt start & end of avail mem
         STMD R22,=ACODBA      ; save start of output code in LEGEND
         STMD R22,=ACODEN      ; save end of output code in LEGEND
         STMD R22,=ALBTBL      ; save end, grows 'upward' to lower addrs
ASMLNK   JSB  =GTSTRT          ; set R30 pointing to first line of prgm
         STM  R#,R10           ; copy R30 to R10
FIXMEM   JSB  =CMEMBT          ; at least 128 bytes left?
         JCY  MOK1             ; jif yes
         JSB  =RECNTR          ; else recenter it
         JSB  =CMEMBT          ; now >= 128 bytes left?
         JCY  MOK1             ; jif yes
*
MNOTOK   JSB  =ERROR+          ; else terminal error
         DATA 23               ; MEM OVF
*
MOK1     JSB  =CMEMTP          ; at least 128 bytes at top?
         JCY  MOK2             ; jif yes
         JSB  =RECNTR          ; else recenter it
         JSB  =CMEMTP          ; now at least 128 bytes at top?
         JNC  MNOTOK           ; jif no, terminal error
MOK2     LDMD R24,=ACODEN      ; get end of new code
         STMD R10,=PCR         ; save current line ptr
         POMD R2,+R10          ; get line#
         CMM  R2,=231,251      ; final END line# A999?
         JNZ  LNOK             ; jif no
*
         JSB  =AROMER          ; Assembler ROM error
         JSB  =ERROR+
         DATA 16               ; FIN-LNK
*
LNOK     STMD R#,=SAVER6       ; save the line# in SAVER6
         CLM  R#
         POBD R#,+R#           ; get line len in R2
         STMD R10,=ASTLIN      ; save ptr to start of line in LEGEND
         LDB  R20,=376         ; comment 'token'
         CMBD R20,R#           ; comment?
         JZR  SKPLIN           ; jif yes, skip it
         JCY  OPJM             ; jif not label
*
* there's a label on the current line.  Check for dupes and fwd refs
*
         POMD R41,+R#          ; else get the label
         LDMD R20,=AIFFLG      ; is assembly conditionally on?
         JNZ  AIFON            ; jif yes
         LDMD R65,R#           ; assembly is off, get opcode
         CMMD R65,=EIFNAM      ; EIF?
         JNZ  DJMP1            ; jif no, just list it
AIFON    JSB  =SLBLTB          ; search the label table for the label
         JEN  DUP?             ; jif found, error if already defined
         PUMD R42,-R20         ; add it to the start of the label table
         LDM  R36,R20          ; get ptr
         SBM  R36,=3,0         ; reserve 3 bytes, line# or addr and flag
         STMD R36,=ALBTBL      ; update end-of-label-table ptr
IGNLBL   POMD R65,+R10         ; get the 3-char opcode
         CMMD R65,=EQUNAM      ; EQU?
         JZR  DODAEQ           ; jif yes
         CMMD R65,=DADNAM      ; DAD?
         JZR  DODAEQ           ; jif yes
         JSB  =INVARP          ; invalidate CURARP & CURDRP to 377
         LDM  R56,R24          ; end of code (addr where label exists)
         SBMD R56,=ACODBA      ; -code start = rel addr in code of label
         PUMD R56,-R20         ; push address into label table
         CLB  R56              ; clear flags byte
         PUBD R56,-R20         ; push 0 flags into label table
         JSB  =SATREF          ; label is defined, satisfy fwd-refs
         JMP  ITSOP-
*
SKPLIN   ADM  R10,R2           ; add len of line to current line ptr
         DCM  R10              ; -1 to adjust for already moved R10
         JMP  DJMP1            ; go spit the line to the output listing
*
DUP?     LDM  R36,R50          ; get line# for first label
         JZR  IGNLBL           ; jif not yet seen
         LDM  R46,=(EDUPLB).2  ; else spit out DUPE LAB err
         JSB  =PRTERR
         JMP  DJMP1
*
OPJM     JMP  ITSOP
*
DODAEQ   PUMD R20,+R6          ; save label table ptr
         PUMD R65,+R6          ; save opcode
         JSB  =AGTVAL          ; get value for the ADDR or EQU
         POMD R65,-R#          ; recover the opcode
         POMD R20,-R#          ; recover the label table ptr
         CMB  R65,=105         ; EQU?
         DRP  R76
         JZR  DDE              ; jif yes
         ADMD R76,=ORGBAS      ; add ORGBAS to ADDR value
DDE      PUMD R#,-R20          ; add value to table
         LDB  R#,=377          ; and label 'token'
         PUBD R#,-R20
         JSB  =SATREF
         POBD R20,+R10         ; get next char
DJMP1    JMP  ALSTIT           ; finish by listing line (if LST is on)
*
GOEOL    POBD R20,+R10         ; get next char
ATEOL?   CMB  R20,=16          ; at EOL?
         JNZ  GOEOL            ; jif no, find end
         GTO FIXMEM            ; go check/fix mem and attack next line
*
ASOPER   LDM  R46,=OPCOER      ; OPCO error
         JSB  =PRTERR          ; print it
         JMP  ATEOL?           ; skip rest of line
*
ITSOP    POMD R65,+R10         ; get 3-char opcode
ITSOP-   BIN
         LDMD R20,=AIFFLG      ; conditionally assembling
         JNZ  ASMIT            ; jif we're assembling (AIF is NOT false)
         CMMD R65,=EIFNAM      ; else see if opcode is EIF
         JNZ  ALSTIT           ; jif no, just list the line
*
ASMIT    LDM  R26,=(ASMTBL).2  ; address of table for assembling opcodes
         LDBD R22,=ISGLO       ; is this a global file?
         JZR  NOTGLO           ; jif no
         LDM  R20,=GLONAM      ; address of "GLO" for "table search"
         LDM  R22,=113,0       ; opcode counter for GLO
         JSB  =OPCLOP          ; handle get the assembly address for it
         JMP  NOTGL-
*
NOTGLO   JSB  =FNDOP-          ; find and get assembly routine for it
NOTGL-   JEN  ASOPER           ; jif unsuccessful
         LDMD R24,=ACODEN      ; get ptr where to put new code
         CLM  R70
         LRM  R23              ; R22=2*OPCODE, halve to get table index
         LDBD R73,X22,MACHCO   ; load machine code byte for this opcode
         JSB  X26,ZRO          ; call the assembly-time function
ALSTIT   BIN
         LDBD R66,=LSTFLG      ; get LST flag
         JZR  NOLST            ; jif LST is OFF
         JSB  =DOPRNT          ; set printer is output
         CLB  R26              ; flag 1st printed line for this src line
         PUBD R20,+R6          ; save R20
MOROBJ   LDM  R30,=INPBUF      ; where to format the line
         LDMD R22,=ACODEN      ; where new code for this line went
         LDM  R36,R22
         SBMD R36,=ACODBA      ; code offset for this line
         JSB  =FRM6DG          ; format the line address
         LDB  R34,=2           ; 2 bytes of obj code output
OBJLOP   CMM  R22,R24          ; any obj code bytes output on this line?
         JZR  OBJDON           ; jif no
         CLM  R36
         POBD R36,+R22         ; get byte of obj code
         LDB  R20,=3           ; 3 digits
         JSB  =FRMDGS          ; format them
         JMP  OBJSPC           ; go put another space after address
*
NOLST    STMD R24,=ACODEN      ; update end-of-code ptr
EOLJMP   GTO ATEOL?            ; and keep going with the next line
*
OBJDON   LDMD R44,=BLANKS      ; get 4 blanks
         PUMD R44,+R30         ; push 4 of them (3 obj digits & space)
OBJSPC   DCB  R34              ; dec obj code byte counter
         JNZ  OBJLOP           ; jif not done, do next obj byte
         CLM  R64
         LDBD R64,=PRNTLN      ; printer line length
         TSB  R26              ; 1st printed line for this line of SRC?
         JNZ  NOSRC            ; jif no, already shown the SRC
         JSB  =PSHRGS          ; save registers
         LDMD R24,=ASTLIN      ; ptr to start of curr line
         JSB  =DCLST           ; decompile the source into LST buffer
         LDM  R56,R#           ; copy R30 output ptr
         JSB  =POPRGS          ; restore registers
         LDM  R30,R56          ; put output ptr back in R30
NOSRC    LDM  R56,=INPBUF      ; start of buffer
         STM  R56,R66          ; address for DMPBU-
         ADM  R56,R64          ; line length for printer
         CMM  R56,R30          ; printer width < formatted length?
         JCY  PLENOK           ; jif no
         STM  R56,R30          ; clip formatted text to printer width
PLENOK   JSB  =DMPBU-          ; dump the line to the printer device
         ICM  R26              ; flag we're on non-src format line
         STMD R22,=ACODEN      ; set new code end ptr
         CMM  R22,R24          ; any more obj bytes to dump?
         JNZ  MOROBJ           ; jif yes
         POBD R20,-R6          ; restore R20
         JMP  EOLJMP           ; go do the next line
* ***********************************************
* Search label table for a label
* INPUT:
*   R42-47 = label
* OUTPUT:
*   E=0 failed, E=1 if found in table
*   R20 ptr to end of label table
*
SLBLTB   LDMD R20,=ACODBA      ; get end of label table
         CLE                   ; pre-set to NOT found in table
SLTLOP   CMMD R20,=ALBTBL      ; reached beginning of table?
         JZR  ARTN81           ; jif yes, didn't find it
         POMD R50,-R20         ; get next label and address/value
         DCM  R20              ; skip one more byte of flags
         CMM  R42,R52          ; labels match?
         JNZ  SLTLOP           ; jif no, loop
         ADM  R20,=3,0         ; move back up to label
         ICE                   ; flag found
ARTN81   RTN
*
* copies an DATA string from R46 to the ASM ROM output buffer
* returns length of string buffer in R36-37
*
CPYSTR   LDMD R30,=ASMBAS      ; get ptr to ASM ROM output buffer
         STM  R30,R26          ; save a copy of it
         POBD R36,+R46         ; get the first byte of the buffer
CPY$LP   PUBD R#,+R30          ; push the byte to the output buffer
         POBD R#,+R46          ; get the next byte of the input buffer
         JPS  CPY$LP           ; jif not end, loop til buffer is copied
         SBB  R#,=200          ; strip the MSbit off the last character
         PUBD R#,+R30          ; and push it
         LDM  R#,R30           ; get the end of the buffer
         SBM  R#,R26           ; minus the beginning = the buffer len
         RTN
*
AGTVAL   JSB  =GCHAR           ; get next NON-blank char from R10 buffer
AGTVA-   JSB  =PSHRGS          ; save registers
         JSB  =INTEGR          ; try to get a number
         JEZ  NMFAIL           ; jif none found
         LDM  R65,R40          ; get the int
         LDB  R64,=377         ; format it as a series 80 INTEGER
         JSB  =INTORL          ; convert it to a REAL format
         BIN
         CMB  R20,=104         ; D suffix (decimal value)?
         JZR  DECVAL           ; jif yes
         CMB  R20,=103         ; C suffix (BCD value)?
         JNZ  OCTVAL           ; jif no
*
BCDVAL   TSB  R60              ; non-0 EXPONENT?
         DRP  R67
         JNZ  CPYBCD           ; jif yes, two digits
         BCD
         LRB  R67              ; else shift single digit to LSnibble
         JMP  CPYBCD
*
OCTVAL   DCM  R10              ; no suffix, put last char back
         PUMD R60,+R12         ; push number to stack
         JSB  =DEC.            ; convert from OCT to DEC
         CLE                   ; pre-set E flag to FAILED
         CMB  R17,=300         ; error in conversion?
         JCY  NMFAIL           ; jif yes
         JSB  =GTBIN#          ; get # off stk as binary in R46 (DRP=46)
CPYBCD   STM  R#,R76           ; copy the value
NMGOT    CLE
         ICE                   ; flag successful
NMFAIL   JSB  =POPRGS          ; restore registers
         BIN
         DRP  R76
         RTN
*
DECVAL   JSB  =CONINT          ; convert REAL in R60 to BIN in R76
         JMP  NMGOT
*
* *********************************
* DEC()
* *********************************
*
* NOTE: In REAL math routines, the 8-byte REAL number gets
* split into a 6-byte (12-digit) Mantissa, a 2-byte (3-digit)
* signed exponent, and a mantissa sign.  If dealing with a
* single number, it's usually in R40-47 (mantissa), R36-37
* (exponent), and R32 (sign of mantissa).  If a second number
* is being used, it's usually in R50-57 (mantissa), R34-35
* (exponent), and R33 (sign of mantissa).
*
* I inherited this OCT/DEC code, probably from Homer Russell,
* the author of the math routines in the Series 80, and I have
* a hard time entirely grokking the whole thing... as I do most of the
* Series 80 math routines.  Homer was crazy awesome with math!
*
         DATA 20,55            ; attribs: numeric func, 1 numeric arg
DEC.     JSB  =SPLITI          ; get #, split it, handle non-0 frac part
         LDM  R36,R20          ; get the exponent count (21 oct)
         CMM  R36,R34          ; 21 oct (17 dec) >= original exponent?
         JCY  DECOK            ; jif yes
OORERR   JSB  =ERROR
         DATA 13               ; ARG OUT OF RANGE
         RTN
*
DECOK    LLM  R52              ; get MSdigit from argument -> E
         CLM  R62              ; R62-67 = 0
         ELB  R62              ; shift digit from E into R62
         CMB  R62,=10          ; >=8?
         JCY  INVPER           ; jif yes, inv parameter, must be oct#
         ADM  R42,R62          ; add into result (R40 was 0 from SPLITI)
         TSB  R34              ; done all digits?
         JZR  ODFIN            ; jif yes, done
         DCB  R34              ; else dec exponent (digit count)
         ADM  R42,R42          ; x2
         ADM  R42,R42          ; x4
         ADM  R42,R42          ; x8 move cnt, ready for next 0-7 val
         JMP  DECOK            ; loop
*
INVPER   JSB  =ERROR
         DATA 131              ; INVALID PARAM
         RTN
*
* *********************************
* REL()
* *********************************
         DATA 20,55            ; attribs: numeric func, 1 numeric arg
REL.     JSB  =OCTBIN          ; get OCT argument as binary
         ADMD R46,=BINTAB      ; add base address of BPGM
         STM  R46,R36          ; copy
I2BIN    JSB  =STKBIN          ; convert to INTEGER on R12 Stack
*
* The above code FALLS THROUGH to the OCT code, executing OCT's
* attributes as ARP instructions. Doesn't hurt anything, and saves
* 2 bytes of code.
*
* *********************************
* OCT()
* *********************************
*
* NOTE: In REAL math routines, the 8-byte REAL number gets
* split into a 6-byte (12-digit) Mantissa, a 2-byte (3-digit)
* signed exponent, and a mantissa sign.  If dealing with a
* single number, it's usually in R40-47 (mantissa), R36-37
* (exponent), and R32 (sign of mantissa).  If a second number
* is being used, it's usually in R50-57 (mantissa), R34-35
* (exponent), and R33 (sign of mantissa).
*
* I inherited this code from someone else (probably Homer Russell,
* the author of the math routines in the Series 80), and I have
* a hard time entirely grokking the whole thing...
*
         DATA 20,55            ; attribs: numeric func, 1 numeric arg
OCT.     JSB  =SPLITI          ; get #, split it, handle non-0 frac part
         LDM  R36,R34          ; copy original exponent
         CMM  R36,=20,0        ; <16?
         JNC  OCTOK            ; jif yes
         JNZ  OORERR           ; jif not ==16
         CMMD R52,=MAXDEC      ; > limit?
         JZR  OCTOK            ; jif =limit
         JCY  OORERR           ; jif too big
OCTOK    TCM  R36              ; negate exp for BRTS40 which incs til 0
         LDB  R47,=3           ; R40-R47 = 0, so put 3 in MSdigit
*
         JSB  =ROMJSB
         DEF  BRTS40           ; shift 3 over until orig exponent is 0
         DATA 0
*
         ADM  R50,R40          ; add 3 to the orig int at that location
         LDM  R36,=11,0        ; load an exponent of 9
         LDM  R42,=0,222,105,223,211,205 ; BCD = 00, 92, 45, 93, 89, 85
* mantissa of 8589934592 is exactly (MAXDEC + 1)/8
         CLB  R33              ; clear R50 sign (positive)
         JSB  =DIV20           ; R40 = R40/R50, SHRONF-
         CLM  R50              ; preclear result
         ARP  R40              ; loop's all ARP 40 so take out of loop
OCVTLP   CLE                   ; preclear E (shifted digit) to 0
         TSB  R37              ; exponent negative?
         JLN  OJD              ; jif yes, just shift in 0's
         LLM  R40              ; get another digit
OJD      ELM  R52              ; shift the new digit into R52-57
         LRM  R47              ; shift 47 over
         ICM  R36              ; increment exponent
         ADM  R40,R#           ; x2
         ADM  R40,R#           ; x4
         ADM  R40,R#           ; R40 = R40x8
         DCB  R20              ; started at 21 (17 decimal)
         JCY  OCVTLP           ; jif >=0 (loop 18 times)
*
         STM  R50,R#           ; copy R50 into R40
         LDM  R36,=21,0        ; exponent
ODFIN    JSB  =SHF10           ; normalize R40
         JSB  =NFR             ; pack R40 & exponent & sign, push it
         RTN
*
SPLITI   JSB  =INTFRA          ; get int R50 & frac R40 exponent R34
         TSM  R40              ; any fractional part?
         JZR  ISINT            ; jif no
         POMD R36,-R6          ; else toss rtn address
         JMP  INVPER           ; report invalid parameter
*
ISINT    TSM  R50              ; integer part =0?
         JNZ  LFJUS-           ; jif no
         GTO FTR73             ; push r40 (0) 0=0 whether dec or oct
*
LFJUST   LLM  R#               ; shift a digit left
LFJUS-   JLZ  LFJUST           ; shift left until MSnibble is not 0
         LDM  R20,=21,0        ; 17 decimal (exponent?)
         RTN
*
MAXDEC   DATA 120              ; 50 BCD max value for OCT()=68719476735
         DATA 163              ; 73
         DATA 166              ; 76
         DATA 224              ; 94
         DATA 161              ; 71
         DATA 150              ; 68
*
* ************************************************************
         DATA 241
MEM.     JSB  =GTABAS          ; get ASM ROM RAMbase
         POMD R40,-R12         ; get address off stack
         PUMD R40,+R12         ; put it back
         JSB  =SVMADR          ; save it in ASM ROM's RAM
         JSB  =OCTBIN          ; convert the octal address to binary
         STMD R46,X#,MEMPTR    ; save in ASM ROM's RAM
         RTN
*
* ************************************************************
         DATA 241
MEMD.    JSB  =MEM.            ; do mem stuff
         LDMD R36,R46          ; get the indirect address
BKPMEM   STMD R36,X14,MEMPTR   ; save in ASM ROM's RAM
         JSB  =I2BIN           ; convert to OCTAL value on stack
         POMD R40,-R12         ; get if from the stack
SVMADR   STMD R#,X14,MEMADR    ; save in ASM ROM's RAM
         RTN
*
* **********************************************************
* ':' token for MEM statements
* **********************************************************
         DATA 1,51             ; attribs=numeric binary op, precedence 1
ACOLN.   JSB  =GTBIN+          ; get the ROM#
         STBD R46,X#,MEMROM    ; save it in ASM RAM
         RTN
*
* **********************************************************
* ',' token for MEM statements
* **********************************************************
         DATA 1,51             ; attribs=numeric binary op, precedence 1
ACOMA.   JSB  =OCTBIN          ; get LEN oct#, convert to dec binary#
         DRP  R46              ; where it's at
SMLEN    STMD R#,X14,MEMLEN    ; save it to ASM RAM
         RTN
*
* ******************************************************
* '=' token for MEM statements
* ******************************************************
         DATA 1,51             ; attribs=numeric binary op, precedence 1
AEQUL.   JSB  =GTABAS          ; get ASM RAM ptr
         STMD R6,X#,MEMR6      ; save R6 in ASM RAM
AEQULP   JSB  =OCTBIN          ; get octal value as decimal binary#
         PUBD R46,+R6          ; save on the return stack
         CMMD R12,=TOS         ; op stack empty? (multiple '=' values?)
         JNZ  AEQULP           ; jif no, loop
         LDMD R20,X14,MEMPTR   ; get address we're storing to
*
* NOTE: during execution, the numbers to store into memory
* get pushed onto the operating stack, so when we pop them
* off, convert them and push them on the R6 stack, the
* 1st number the user specified is the LAST one OFF the
* operating stack (R12) and the FIRST one OFF the R6 stack.
*
AEQUL2   POBD R46,-R6          ; get a value off rtn stack
         PUBD R46,+R20         ; push it out to memory
         LDMD R46,X14,MEMR6    ; get starting point of R6 stack
         CMM  R46,R6           ; have we emptied all the args?
         JNZ  AEQUL2           ; jif no, pop and store some more
         RTN                   ; done
*
DMPREG   LDMD R54,=HDRREG      ; load "REG "
         STMD R54,R14          ; store to output buffer
         LDM  R26,R14          ; copy output buffer
         LDM  R36,=3,0         ; len of output (3 chars REG)
         JSB  =DUMPIT          ; dump to the DISP or PRINT
         LDM  R30,R#           ; get ouput buffer at start of ASM RAM
         LDM  R26,=SAVR0       ; memory to dump is 256 bytes of CPU regs
         LDM  R34,=100,0       ; len = 256
*
* Fall through into the "memory dump" routine to dump the CPU registers
*
* The following line loads r50-r57 with this CODE:
* DRP is R20 coming in, R24 points to RSELEC
*  024 246        :       STBD r#,r24    ; so select the other ROM
*  026 340        :       POBD r#,+r26   ; get byte into R20, +ptr
*  121 024 246    :       STBD r21,r24   ; R21=050 ASM ROM#, reselect it
*  236            :       RTN            ; return to ASM ROM
* When stored into RAM, it can be called to read a byte from another ROM
*
DMPSOM   LDM  R50,=24,246,26,340,121,24,246,236 ; load above func
         STMD R50,X#,ROMPEK    ; store above function into ASM RAM
DMLOOP   SBM  R34,=10,0        ; -8 from remaining bytes to MEM dump
         JNC  LESS8            ; jif less than 8
         JSB  =DMEM8           ; dump a line of 8 bytes
         JMP  DMLOOP           ; go back for more
*
LESS8    ADM  R#,=10,0         ; restore the count
         JZR  SPCDMP           ; jif none, all done
         STB  R34,R41          ; copy the # of bytes to dump
         JSB  =DMEMX           ; dump them
SPCDMP   LDB  R34,=40          ; load an ASCII ' ' char
         PUBD R34,+R30         ; push it to output buffer
         JMP  DMPJM2           ; dump the buffer
*
         DATA 44
DMPMEM   JSB  =DODISP          ; set DISP as print output
DMPME-   JSB  =GTABAS          ; get ASM RAM ptr
         STM  R#,R30           ; setup ptr to ASM RAM output buffer
         LDMD R26,X14,MEMPTR   ; get address of memory to dump
         LDMD R34,X14,MEMLEN   ; get MEM dump length from ASM RAM
         JZR  SPCDMP           ; jif 0, dump blank line
         JSB  =DMPSOM          ; dump them
         LDMD R34,X14,MEMLEN   ; get # to dump
         LDMD R26,X14,MEMPTR   ; get where to dump from
DASLOP   SBM  R34,=20,0        ; 16 bytes left?
         JNC  DASCEN           ; jif no
         JSB  =DMPASC          ; dump another 16
         JMP  DASLOP
*
DMEM8    LDB  R41,=10          ; # bytes to dump
DMEMX    JSB  =PEEK1           ; read a byte from memory into R20
         CLM  R36              ; clear R37
         LDB  R36,R20          ; copy byte into R36
         LDB  R20,=3           ; # digits to format out
         JSB  =FRMDGS          ; output digits with a SPACE on the end
         DCB  R41              ; dec byte counter
         JNZ  DMEMX            ; jif not done
DMPJM2   JMP  DMPJMP           ; dump the line
*
DASCEN   ADM  R34,=20,0        ; restore remaining count
         JZR  FRMMEM           ; jif none, done, dump buffer
         STB  R34,R51          ; else copy the byte counter
         JSB  =DASCLP          ; format them, fall thru to dump buffer
*
FRMMEM   LDMD R60,X14,MEMADR   ; get addr of memory dump
         PUMD R60,+R12         ; push # on R12 stack
         LDM  R44,=115,105,115,40 ; load ASCII "MEM "
         PUMD R44,+R30         ; push "MEM " to output buff
         JSB  =ONER            ; get number as REAL off R12 stack
         JSB  =ROMJSB
         DEF  CVNUM            ; format it out to R30 buffer
         DATA 0
DMPJMP   JMP  DMPBUF           ; display/print it
*
FRM6DG   LDB  R20,=6           ; number of digits to output
FRMDGS   CLM  R50              ; clear working regs
         LLM  R36              ; get bit 15 (MSbit) all by itself
         ELB  R57              ; get that MSbit into LSbit of 57
         ADB  R57,=60          ; add ASCII '0' (convert to '0' or '1')
         JSB  =FRMDIG          ; Format a second digit
         JSB  =FRM4DG          ; Format 4 more digits
         LDB  R0,=60           ; pointing register-indirect at R60
         SBB  R0,R20           ; minus # digits being output
* R0 pointing at R5x registers to push to the format buffer
         PUMD R*,+R30          ; push formatted chars into the buffer
         LDB  R*,=40           ; load a space
         PUBD R*,+R30          ; push it out to buffer after the digits
         RTN
*
FRM4DG   JSB  =FRM2DG          ; format 2 digits, fall thru & do 2 more
FRM2DG   JSB  =FRMDIG          ; format 1 digit, fall thru & do 1 more
*
* Get next three bits from R36-37 into an ASCII digit in R50-R57
*
FRMDIG   LRM  R37              ; shift rt 1 so when we get next 4 bits
         BCD                   ;  MSbit is 0 & next 3 bits in lower bits
         LRM  R57              ; shift already formatted output chars
         LRM  R57              ;   down one register
         LLM  R36              ; get the next 4 bits (really 3 bits)
         ELM  R57              ; put them in the bottom of R57
         BIN
         ADB  R57,=60          ; add a '0' char to convert to '0' to '7'
         RTN
*
CPYDMP   JSB  =CPYSTR          ; copy the string to the output buffer
DMPBUF   LDMD R66,=ASMBAS      ; address of buffer to disp/print
DMPBU-   JSB  =PSHRGS          ; save R20-R47
         PUMD R56,+R6          ; and R56-7
         PUMD R70,+R6          ; and R70-77
         PUMD R66,+R6          ; and R66-67
         LDM  R36,R30          ; copy output buffer ptr
         SBM  R36,R66          ; get curr length of buffer
         LDM  R26,R66          ; ptr to beginning of buffer (ASMBAS)
         JSB  =DUMPIT          ; DISPLAY or PRINT the buffer
         CMB  R17,=300         ; any errors?
         JNC  NOUTER           ; jif no
         GTO RSTR6             ; GOTO 63254 (RSTR6-1), bail out, ROMRTN
*
NOUTER   POMD R66,-R6          ; restore R66-67
         POMD R70,-R6          ; and R70-77
         POMD R56,-R6          ; and R56-57
         JSB  =POPRGS          ; restore R20-R47
         LDM  R30,R66          ; reset output buffer ptr
         RTN
*
PEEK1    LDB  R21,=50          ; ASM ROM#
         LDM  R24,=RSELEC      ; ptr to RSELEC
         LDBD R20,X14,MEMROM   ; ROM# to read from
* call PEEK code stored in ROMPEK @ 71105 in the ASM ROM
* to get a byte from MEMROM (or RAM or SYSTEM ROM) into R20
         JSB  X14,ROMPEK       ; get byte from ROM
         RTN
*
DMPASC   LDB  R51,=20          ; dump 16 bytes as CHARS
DASCLP   JSB  =PEEK1           ; get a byte
         LLB  R20              ; throw away the upper MSbit
         LRB  R20              ; shift-left/shift-right cheaper than ANM
         CMB  R20,=40          ; CTL character?  (less than a SPACE)
         JCY  NOTCTL           ; jif no
         LDB  R20,=40          ; replace with a SPACE
NOTCTL   PUBD R#,+R30          ; push the char to the output buffer
         DCB  R51              ; decrement the byte counter
         JNZ  DASCLP           ; jif not done
         JMP  DMPBUF
*
* Save CPU registers R20-R47 on R6 stack
*
PSHRGS   POMD R2,-R6           ; pop return address
         PUMD R40,+R6          ; save R40-47
         LDM  R40,R20          ; get R20-27
         PUMD R40,+R6          ; save them
         LDM  R40,R30          ; get R30-37
         PUMD R40,+R6          ; save them
         PUMD R2,+R6           ; push return address back on
         RTN
*
* Restore CPU registers R20-R47 from R6 stack
*
POPRGS   POMD R2,-R6           ; pop return address
         POMD R40,-R6          ; recover R30-37
         STM  R40,R30          ; copy them
         POMD R40,-R6          ; recover R20-27
         STM  R40,R20          ; copy them
         POMD R40,-R6          ; recover R40-47
         PUMD R2,+R6           ; push return address back
         RTN
*
* GTBIN# has to go through shenanigans to convert a BCD integer to a
* binary# because ONEB returns a SIGNED value (BCD INTEGERS are signed
* values). We want an UNsigned binary value, so we have to check the
* size first, save a flag, modify addresses >= 32768 to be <32768, do
* the conversion, then OR the MSbit back in (if necessary).
*
GTBIN#   PUMD R70,+R6          ; save R70-77
         JSB  =ONEI            ; get an INT off R12 stack into R45-R47
         POMD R70,-R6          ; restore R70-77
         LDM  R32,=FWUSER      ; get FWUSER
         BCD                   ; we're doing BCD math
         CMM  R45,=66,125,6    ; BCD 36,55,6 = INT 65536
         JCY  OORER2           ; jif greater, error, address too big
         SBM  R45,=150,47,3    ; BCD 68,27,3 = INT 32768
         JCY  GOTADR           ; jif address in RAM
         ADM  R45,=150,47,3    ; ADD 32768 back in (restore ROM address)
         CLM  R32              ; set MSbit to 0 for ROM address
*
GOTADR   PUMD R40,+R12         ; push address back on stack
         JSB  =ONEB            ; get it off as a binary number in R46-47
         ORM  R46,R32          ; OR-in MSbit of address
         ARP  R14              ; leave ARP at r14 (ASMBAS)
         RTN
*
OORER2   JSB  =ERROR+
         DATA 13               ; ARG OUT OF RANGE
*
* This is the table of routines to assemble particular opcodes
* (same sequence as opcodes in OPTABL)
*
ASMTBL   DEF  AARP.            ; 0
         DEF  ADRP.
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R            ; 10
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  PSHC.
         DEF  OPC1R
         DEF  OPC1R
         DEF  PSHC.
         DEF  OPC1R            ; 20
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  OPC1R
         DEF  PSHC.            ; 30
         DEF  BRCI.
         DEF  MRCI.
         DEF  BRCI.
         DEF  MRCI.
         DEF  PSHC.
         DEF  PSHC.
         DEF  PSHC.
         DEF  PSHC.            ; 40
         DEF  APAD.
         DEF  ALDSTB
         DEF  ALDSTM
         DEF  ALDSTB
         DEF  ALDSTM
         DEF  AMATHB
         DEF  AMATHM
         DEF  AMATHB           ; 50
         DEF  AMATHM
         DEF  AMATHB
         DEF  AMATHM
         DEF  AMATHM
         DEF  APUPO.
         DEF  APUPO.
         DEF  APUPO.
         DEF  APUPO.           ; 60
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.           ; 70
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  ARJMP.
         DEF  AJSB.            ; 100
         DEF  ARJMP.
         DEF  ABSZ.
         DEF  AABS.
         DEF  AASP.
         DEF  ABYT.
         DEF  AGTO.
         DEF  AASC.
         DEF  ADR16            ; 110
         DEF  ANAM.
         DEF  AVAL.
         DEF  AGLO.            ; 113 GLO
         DEF  AFIN.
         DEF  ALST.            ; LST
         DEF  AUNL.
         DEF  ALNK.            ; LNK
         DEF  AORG.            ; 120 ORG
         DEF  ASET.            ; SET
         DEF  ACLR.            ; CLR
         DEF  AAIF.            ; AIF
*
* This is the table of actual OPCODES
* (same sequence as opcodes in OPTABL)
*
MACHCO   DATA 6,165,200,201,202,203,204,205 ; ARPDRPELBELMERBERMLLBLLM
         DATA 206,207,210,211,234,212,213,233 ; LRBLRMICBICMICEDCBDCMDCE
         DATA 214,215,216,217,220,221,222,223 ; TCBTCMNCBNCMTSBTSMCLBCLM
         DATA 235,224,225,226,227,230,231,232 ; CLEORBORMXRBXRMBINBCDSAD
         DATA 236,237,240,241,242,243,300,301 ; RTNPADLDBLDMSTBSTMCMBCMM
         DATA 302,303,304,305,307,340,341,344 ; ADBADMSBBSBMANMPOBPOMPUB
         DATA 345,373,363,370,371,374,375,360 ; PUMJCYJEVJENJEZJLZJLNJMP
         DATA 361,364,366,372,362,365,376,377 ; JNOJNGJNZJNCJODJPSJRZJRN
         DATA 306,367          ; JSBJZR
*
MILNAM   DATA  `ILL NAM`
*
ANAM.    DRP  R45              ; these 3 lines do "LDM R45,=200,MILNAM"
         DATA 251,200
         DEF  MILNAM
*
         LDBD R21,=ISAROM      ; ABS ROM?
         JNZ  APRTER           ; jif yes, NAM is illegal
         LDBD R21,=ILNMAB      ; set MSbit of ILNMAB
         ORB  R21,R45          ; or in 0200
         STBD R21,=ILNMAB      ; save MSbit of ILNMAB = NAMs are illegal
         STBD R21,=ISAROM      ; not ABS ROM
         POMD R42,+R10         ; get NAM string
         PUMD R42,+R24         ; push it out
         LDB  R42,=2           ; BPGM type
         PUBD R42,+R24         ; push it out
         CLM  R42              ; a BUNCH of zeroes
         PUMD R42,+R24         ; push 19 more zeroes
         PUMD R42,+R24
         PUMD R42,+R24
         PUBD R42,+R24
         RTN
*
MAIFUN   DATA  `AIF UND`
*
APRTER   JSB  =PRTERR
         RTN
*
AAIF.    CLM  R26              ; preclear in case label not defined
         JSB  =GETLBL          ; get label, add to table if not defined
         LDM  R46,=MAIFUN      ; address of error message
         JEZ  APRTER           ; jif flag wasn't previously defined
SETGAT   STMD R56,=AIFFLG      ; store flg val to conditional gate
         JMP  POPCHR           ; finish
*
AABS.    LDM  R46,=(MILABS).2  ; preload ILL ABS error message address
         LDBD R22,=ILNMAB      ; ABS illegal?
         JNZ  APRTER           ; jif yes, print the error
         LDB  R22,=201         ; ABS illegal flag
         STBD R22,=ILNMAB      ; set flags
         CMB  R20,=122         ; 'R' ? (ABS ROM)
         JNZ  GETBAS           ; jif no, must be ABS 16 or ABS 32
         STBD R20,=ISAROM      ; set ABS ROM flag
         POMD R20,+R10         ; get "OM"
         POBD R20,+R10         ; get SPACE
         POBD R20,+R10         ; get next char
DRP20    DRP  R20
GETBAS   JSB  =AGTVA-          ; get base address
         STMD R#,=ABSBAS       ; save it
         RTN
*
MILABS   DATA  `ILL ABS`
*
* ***********************************************
* The following little snipped, so far, seems to
* be "dead code" that is never called or referenced
* from anywhere. "You can always find 100 bytes!"
* ***********************************************
         CLM  R56
         ICM  R56
         DCM  R10
         JMP  SETGAT
*
* ***********************************************
*
ACLR.    CLM  R26              ; value for flag
         JMP  ASTCLR           ; common finish
*
ASET.    CLM  R26
         ICM  R26              ; value for flag
ASTCLR   JSB  =GETLBL          ; get label, set to 1 if not defined
         JEZ  POPCHR           ; jif new label (so GETLBL set it to 1)
         ICM  R20
         PUMD R26,+R#          ; store the 1 into the value
POPCHR   POBD R20,+R10         ; get next char
         RTN                   ; done
*
* Get a label from the source and find (or add it) in the label table
* Return R56=address, R55=flags
*
GETLBL   POMD R42,+R10         ; get 6-byte label from src
GETLB-   JSB  =SLBLTB          ; search the label table for it
         JEN  LBFND            ; jif found it in the table
         PUMD R42,-R20         ; push label onto the end of the table
         PUMD R26,-R20         ; push the (possibly 0) address
         PUBD R27,-R20         ; push the (likely 0) flag
         STMD R20,=ALBTBL      ; save label table ptr
         ADM  R20,=3,0         ; +3 to get back above the address/flags
LBFND    POMD R56,-R20         ; get the address
         POBD R55,-R20         ; get the flags
         RTN
*
* Handle a label reference, pushing label value OR adding to placeholder
* to label table and pushing a reference on the forward-reference stack.
*
ADR16    POMD R42,+R10         ; get 6-byte label from src
ADR16-   CLM  R26              ; 0 addr if not already in table (fwd-ref
         JSB  =GETLB-          ; find or add the label
         JZR  FWDREF           ; jif added it, forward reference
         TSM  R56              ; address 0?
         JNZ  PSHADR           ; jif no, it's defined, just push addr
FWDREF   ICM  R20              ; skip back to the label
         ICM  R20
         ICM  R20
         LDMD R56,=ACODBA      ; get highest address of label table
         SBM  R56,R20          ; offset of label in the label table
         PUMD R56,+R12         ; add it to the forward-reference table
         LDM  R56,R24          ; copy the code output ptr
         SBMD R56,=ACODBA      ; get offset into code for the reference
         PUMD R56,+R12         ; add it to the forward-reference table
         LDM  R56,=326,326     ; put 326,326 in for temp address markers
PSHADR   PUMD R#,+R24          ; push the address
         JMP  POPCHR
*
ABYT.    DCM  R10              ; put last char back
ABYT-    JSB  =GET#            ; get a value
         PUBD R#,+R24          ; push it out
         CMB  R20,=54          ; comma?
         JZR  ABYT-            ; jif yes, keep going
         RTN
*
APAD.    JSB  =INVARP          ; invalidate CURARP & CURDRP
         DRP  R73              ;  (since PAD will change them)
PSHC.    PUBD R#,+R24          ; push the opcode out
         RTN
*
DRAR.    JSB  =A1DRP           ; handle DRP reference
AARP.    JSB  =A1ARP           ; handle ARP reference or immediate value
         RTN
*
ADRP.    JSB  =A1DRP           ; handle DRP reference
         RTN
*
OPC1R    JSB  =A1DRP           ; get possible DRP register
         JMP  PSHC.            ; push opcode
*
* for the following couple of routines:
*  R70=what arguments are found
* 0 = R,R
* 1 = R,=label or number
* 2 = R,R,=label
*  R71=what instruction opcode addressing was specified
* 0 = immediate (LDB)
* 1 = Direct (LDBD)
* 2 = Indirect (LDBI)
*  R72=Byte (LDBx) or Multi-byte (LDMx)
*  R73=base machine code to be pushed out after possible modification
*  R75=0 (R,R) or 1 (R,R,label  OR  R,label)
*
ALDSTM   ICB  R72              ; flag that it's a Multi-byte operation
ALDSTB   CMB  R20,=122         ; 'R'? (immed, not Direct or Indirect)
         JZR  AGOTR            ; jif yes
         ICB  R71              ; move to DIRECT addressing mode
         CMB  R20,=104         ; 'D' ?
         JZR  ALDSTN           ; jif yes
         ICB  R71              ; move to INDIRECT addressing mode
ALDSTN   POBD R20,+R10         ; get next char
AGOTR    JSB  =DRAR.           ; get DRP and possible ARP registers
         CLM  R26
         LDB  R26,R70          ; 0 for R,R  1 for R,=  2 for R,R,=
         BIN
         LLB  R26              ; double (to 0, 2, 4) for indexing
         ADB  R26,R70          ; triple (to 0, 3, 6)
         ADB  R26,R71          ; +address mode (0=LDB, 1=LDBD, 2=LDBI)
         LDBD R26,X26,LDSTCO   ; get opcode modification
         ADB  R26,R73          ; add the base opcode into it
AFINAL   PUBD R26,+R24         ; push the completed opcode out
         TSB  R75              ; R,R addressing? (another literal arg?)
         JZR  ARTN79           ; jif yes, no more addressing
         JSB  =PSHIMM          ; else push the label/numeric argument
ARTN79   RTN
*
* Opcode modifications for various addressing modes of LD, ST
*
LDSTCO   DATA 0,4,14,10,20,30,0,24,34
*
AMATHM   ICB  R72              ; flag Multi-byte operation
AMATHB   CMB  R20,=122         ; 'R' ? (immed addressing, not Direct)
         JZR  AGOTR2           ; jif yes
         ICB  R71              ; move to Direct
         POBD R20,+R10         ; get next char
AGOTR2   JSB  =DRAR.           ; get DRP and possible ARP registers
         LDB  R26,R71          ; copy addressing mode (0=R,R  1=Direct)
         BCD                   ; 4 opcodes handled (CM, AD, SB, ANM)
         LLB  R26              ;   left-shift 4 bits (0 or 16 dec)
         BIN
         ADB  R26,R73          ; plus the base opcode
         CMB  R70,R71          ; instruction and argument modes match?
         JZR  AFINAL           ; jif yes, do common finish
         ADB  R26,=10          ; else tweak
         JMP  AFINAL           ; and finish
*
MRCI.    ICB  R72              ; multibyte
BRCI.    JSB  =DRAR.           ; handle DRP and possible ARP
PSHCJM   JMP  PSHC.            ; go push the opcode
*
* PUBD, PUMD, PUBI, PUMI, POBD, POMD, POBI, POMI  +/-
*
APUPO.   CMB  R20,=104         ; 'D' ?
         JZR  APUPOD           ; jif yes, Direct mode
         ADB  R73,=10          ; else modify opcode to Indirect mode
APUPOD   POBD R20,+R10         ; get next char
         JSB  =A1DRP           ; handle the DRP register
         CMB  R20,=53          ; '+' ?
         JZR  APUPO+           ; jif yes
         ADB  R73,=2           ; else modify opcode to pu/po -R
APUPO+   POBD R20,+R10         ; get next char
         JSB  =A1ARP           ; handle ARP register
         JMP  PSHCJM           ; push the opcode
*
JMPERR   DATA  `JMP FROM`
*
* Assemble relative jmp instructions
*
ARJMP.   PUBD R#,+R24          ; push the opcode
         JSB  =ADR16           ; process label, push 16 bits of addr
         POMD R56,-R24         ; get those 16 bits of address back
         JEZ  PSH336           ; jif label was freshly added
         LDM  R56,R50          ; get the address
         JNZ  REALAD           ; jif REAL address (not 0)
PSH336   LDB  R#,=336          ; change marker from 326 to 336
PSHCJ2   JMP  PSHCJM           ;     for undefined 1-byte rel-jmp
*
REALAD   ADMD R56,=ACODBA      ; code offset + code base = curr abs addr
         SBM  R56,R24          ; - curr end-of-code addr
         DCM  R56              ; -1 for proper adjustment
         CMB  R56,=200         ; too large of a jump?
         JCY  RJOK?            ; jif no
JERRIT   LDM  R46,=JMPERR      ; JMP FROM error
         JSB  =PRTERR          ; print it
PSHOFF   DRP  R56
         JMP  PSHCJM
*
RJOK?    CMB  R57,=377         ; =377 if not too large a jmp
         JNZ  JERRIT           ; jif no, it's too large
         POMD R44,-R12         ; pop fwd-ref?  This seems WRONG!
         JMP  PSHOFF
*
AJSB.    LDB  R71,=1           ; for ASM, JSB is always Direct mode
         LDB  R21,=316         ; load simple JSB= opcode
         CMB  R20,=130         ; 'X' ?
         JNZ  AJSB=            ; jif no
         JSB  =A1ARP           ; else handle ARP index register
         LDB  R21,=306         ; change opcode to JSB X,=
AJSB=    PUBD R21,+R24         ; push out the opcode
         JSB  =PSHIMM          ; get and push the address
*
INVARP   CLM  R0
         DCM  R0               ; r0=377,377
         STMD R0,=CURARP       ; invalidate both CURARP and CURDRP
         RTN
*
ABSZ.    JSB  =AGTVA-          ; get number
         JSB  =CMEMBT          ; calc available space at end of code
         CMM  R#,R76           ; as much as we need for BSZ?
         JCY  GOBSZ            ; jif yes
         JSB  =DATUP           ; else move code and label table up
         LDMD R24,=ACODEN      ; get new end-of-code ptr
         JSB  =CMEMBT          ; recalc available space at end of code
         CMM  R#,R76           ; as much as we need now?
         JCY  GOBSZ            ; jif yes
         POMD R22,-R6          ; throw away return address
         GTO MNOTOK            ; go report the memory overflow error
*
GOBSZ    CLM  R40              ; overkill, we only need 1 zero
         TSM  R76              ; was it BSZ 0?
         JZR  ARTN62           ; jif yes, nothing to do, all done
BSZLOP   PUBD R40,+R24         ; else push a 0
         DCM  R76              ; dec count
         JNZ  BSZLOP           ; loop til done
ARTN62   RTN
*
AASP.    JSB  =AASC.           ; handle just like ASC
         LDB  R21,=200         ; get a MSBit set
         POBD R20,-R24         ; get the last char pushed
         ORB  R20,R21          ; set the MSbit
PSHCJ3   JMP  PSHCJ2           ; push it back
*
AGTO.    LDM  R22,=104,251     ; load R22-3 with "LDM R4,="
         PUMD R22,+R24         ; push them out
         JSB  =ADR16           ; get a two-byte address
         POMD R56,-R24         ; pop it back off
         CMM  R56,=326,326     ; undefined address?
         JZR  UNDGTO           ; jif yes
         DCM  R56              ; -1, R4 gets inc'd after the load
         PUMD R56,+R24         ; push it back out
         RTN
*
UNDGTO   CLM  R#
         DCM  R#               ; create a 377,377
         PUMD R#,+R#           ; push them instead of 326,326
         RTN                   ;   (ie, GTO ref that needs a -1 address)
*
AVAL.    JSB  =ADR16           ; get the value
         POMD R56,-R24         ; pop the 2-byte value back
         JEZ  AVAL1B           ; jif label was not defined in the table
         LDM  R76,R50          ; copy the label addr/value
         JNZ  AVAL1B           ; jif not 0
         DRP  R56              ; use the value in R56
AVAL1B   JMP  PSHCJ3           ; push the single byte value back out
*
MUNDLB   DATA  `UND LAB`
*
AASC.    JSB  =AGTVA-          ; get number
         JEN  PSTR             ; jif got it
QUOTLP   POBD R20,+R10         ; get next char
         CMB  R20,=42          ; " ?
         JZR  ARTN77           ; jif yes, end of quoted string
         PUBD R20,+R24         ; else push the unquoted char out
         JMP  QUOTLP
*
PSTR     TSM  R#               ; zero len?
         JZR  ARTN77           ; jif yes
         POBD R20,+R10         ; skip comma
STRLOP   POBD R20,+R10         ; get next char
         PUBD R20,+R24         ; push out to code
         DCM  R76              ; dec len
         JNZ  STRLOP           ; jif not done
ARTN77   RTN
*
AORG.    JSB  =AGTVA-          ; get ORG address
         STMD R#,=ORGBAS       ; save it
         RTN
*
ALNK.    LDM  R20,R10          ; copy ptr to LNK file name
         CLM  R2               ; len counter
LNKLEN   ICM  R2               ; bump len
         POBD R14,+R10         ; get next char from input
         CMB  R14,=16          ; EOL?
         JNZ  LNKLEN           ; jif no
         DCM  R2               ; one too many bumps
         PUMD R2,+R12          ; push len of filename
         PUMD R20,+R12         ; push adr of filename
         JSB  =DATDN           ; move code & LblTbl down to higher addr
         JSB  =PREPO-          ; prep file
         JEN  LNKTAP           ; jif no MS ROM
         JSB  =LNKRDN          ; move fwd-ref stk down & setup for load
         JSB  =ALODD           ; load ASM SRC from disk
         JMP  LNKCOM           ; go do common finish
*
LNKTAP   JSB  =PARGNM          ; set up file name
         JSB  =LNKRDN          ; move fwd-refs down, set up for ALOAD
         JSB  =ALODT           ; load ASM SRC from tape
LNKCOM   ICB  R16              ; set system to calculator mode
         POMD R24,-R6          ; pop address of low end of fwd-ref table
         ICM  R24              ; to get to first byte SRC
         LDMD R26,=NXTMEM      ; where to move it to DST
         STMD R26,=STSIZE      ; set stack bottom
         POMD R22,-R6          ; get len of fwd-ref table
         JSB  =MOVUP           ; move fwd-refs back up to lowest place
         STM  R26,R12          ; adjust R12 to the end of it
         JSB  =RECNT-          ; move code & label table back to center
         POMD R10,-R6          ; pop rtn addr (stop assemble at old loc)
         CMB  R17,=300         ; errors?
         JCY  ARTN73           ; jif yes
         GTO ASMLNK            ; jmp back to start with fresh SRC code
*
* move the fwd-ref stack down against the end of the label table
* to allow as much room as possible for loading the next file of
* ASSM source code.
*
LNKRDN   POMD R36,-R6          ; get return address off rtn stack
         LDM  R24,R12          ; end of fwd-ref stack
         DCM  R24              ; ptr to last byte
         LDM  R22,R12          ; copy as HIGH ptr
         SBMD R22,=NXTMEM      ; minus LOW ptr = len of fwd-ref stack
         PUMD R22,+R6          ; save len on rtn stack
         LDMD R26,=ALBTBL      ; DST ptr +1
         DCM  R26              ; adjust to actual DST ptr
         JSB  =MOVDN           ; move fwd-ref stk down against LblTbl
         PUMD R26,+R6          ; save addr of end (low) of fwd-ref stk
         JSB  =SETLDA          ; set file type and start/end ptrs
         PUMD R36,+R6          ; push return address back on rtn stack
ARTN73   RTN                   ; done
*
* push the output filename onto the R12 operating stack as a string-ref
*
GETONM   LDMD R56,=ABNLEN      ; get length of output filename
         PUMD R56,+R12         ; push on op stack
         LDM  R56,=ABPNAM      ; load address of output filename
         PUMD R56,+R12         ; push it
         RTN
*
AFIN.    POMD R30,-R6          ; toss rtn addr, we're done assembling
         LDBD R30,=ISGLO       ; is this a GLO file?
         JNZ  FINGLO           ; jif yes
*
* We had to add SOMLBL on the next line, because there's an extra
* (unneeded) DRP 30 in the ROM code, so the original ROM src
* must have had a label here to cause the CURDRP to be invalidated.
* So, to make this source assemble to the exact same bytes, we
* add a label to force an extra DRP
*
* bytes, we add a label to force an extra DRP
*
SOMLBL   LDMD R30,=ABSBAS      ; get output code base address (ABS)
         LDMD R36,=ACODBA      ; get ptr to start of output code
         LDMD R34,=ACODEN      ; get ptr to end of output code
         SBM  R34,R36          ; =len of output code
         LDBD R32,=ISAROM      ; get ABS flag
         CMB  R32,=201         ; ABS?
         JNZ  NOTABS           ; jif no
         LDM  R32,=END16K      ; end-of-RAM on a 16K HP-85
         CMB  R30,=16          ; ABS 16?
         JZR  ABS16            ; jif yes
         LDM  R32,=GINTEN      ; (177400) end-of-RAM on a 32K HP-85
ABS16    SBM  R32,R34          ; minus len of output code
         STM  R32,R30          ; = ABS base address of ABS BPGM
         STMD R32,X36,P.BASE   ; store it into the BPGM header
NOTABS   LDMD R32,=NXTMEM      ; bottom of forward-reference stack
NXTREF   CMM  R32,R12          ; anything on the forward-ref stack?
         JZR  REFSOK           ; jif no, okay
*
         POMD R22,+R32         ; get label table offset from ref-stack
         LDMD R24,=ACODBA      ; get code base address
         POMD R26,+R32         ; get code offset from ref-stack
         ADM  R26,R24          ; base+offset=ptr into code of ref loc
         SBM  R24,R22          ; end of LblTbl - offset =ptr into LblTbl
         POMD R22,-R24         ; get addr from label table
         POBD R20,-R24         ; get flag from label table
         JNZ  LBLDEF           ; jif flag is non-0
*
         TSM  R22              ; flag=0 and address=0 means undefined
         JZR  NXTREF           ; jif undefined, try next one
         ADM  R22,R30          ; add ABS base addr (or 0) to label addr
LBLDEF   LDMD R20,R26          ; get 2 bytes from code at ref location
         CMB  R20,=377         ; GTO ?
         JNZ  NOTGTO           ; jif no
         DCM  R22              ; -1 for LDM R4 post-inc
         PUMD R22,+R26         ; push out the real address
DREF     JSB  =DELREF          ; delete the reference from the fwd-refs
         JMP  NXTREF           ; go try the next one
*
NOTGTO   PUBD R22,+R26         ; push LSbyte back out
         CMB  R21,=326         ; 2-byte reference?
         JNZ  DREF             ; jif no
         PUBD R23,+R26         ; push MSbyte back out
         JMP  DREF             ; finish this ref
*
FINGLO   JSB  =FGLO            ; write LblTbl as a GLOBAL data file
         JMP  FINFIN           ; finish
*
NOREFS   LDMD R32,=AERCNT      ; get error count
         JNZ  FFJMP            ; jif had some errors
         LDBD R32,=ISAROM      ; get "is a ROM?" flag
         CMB  R32,=122         ; 'R' ABS ROM?
         JZR  FINROM           ; jif yes
         JSB  =PREPON          ; setup Output Name
         LDB  R56,=10          ; BPGM file type
         STBD R56,=FILTYP      ; store it
         LDMD R56,=ACODBA      ; get start of code
         LDMD R76,=ACODEN      ; get end of code
         JSB  =SETSR6          ; get spare memory on R6
         DRP  R20
         JEN  TAPSTB           ; jif TAPE
*
         JSB  =ROMJSB
         DEF  STRB-            ; STOREBIN in MSROM
         DATA 320
*
         LDBD R30,=ALODBP      ; get "reload BPGM" flag
         JNZ  FINFIN           ; jif don't
         JSB  =SCRTB.          ; else scratch the current BPGM
         JSB  =GETONM          ; get the name of the just-assembled one
*
         JSB  =ROMJSB
         DEF  MSLDB.           ; LOADBIN it via MS ROM
         DATA 320
*
FFJMP    JMP  FINFIN           ; finish up
*
REFSOK   LDMD R32,=NXTMEM      ; get beginning of fwd-ref stack
         CMM  R32,R12          ; anything left undefinded on it?
         JZR  NOREFS           ; jif no, all okay
         JMP  UNDFWD           ; spit out undefined labels
*
FINROM   JSB  =FROM            ; write ROM as DATA file of 125-byte strs
         JMP  FINFIN           ; finish up
*
TAPSTB   JSB  =PARGNM          ; set up output name
*
         JSB  =ROMJSB
         DEF  STORB-           ; STOREBIN it
         DATA 0
*
         LDBD R30,=ALODBP      ; get "reload BPGM" flag
         JNZ  FINFIN           ; jif no load
         JSB  =SCRTB.          ; SCRATCHBIN
         JSB  =PREPON          ; set up output name
*
         JSB  =ROMJSB
         DEF  LOADB.           ; LOADBIN via TAPE
         DATA 0
*
FINFIN   LDM  R46,=MREADY      ; READY msg
         JSB  =SPITR-          ; spit the message
         LDMD R36,=AERCNT      ; get error count
         JSB  =CONBIN          ; convert to REAL#
         LDMD R30,=ASMBAS      ; point to ASM ROM work buff
*
         JSB  =ROMJSB
         DEF  CVNUM            ; format the error count to R30
         DATA 0
*
* The following does LDM R51,=" ERRORS"
         DRP  R51
         DATA 251
         DATA  " ERRORS"
*
         PUMD R51,+R30         ; push " ERRORS" to R30
         JSB  =DMPBUF          ; dump it out
         JSB  =ST240+          ; set IMMEDIATE mode, IDLE, reset R12 stk
         RTN                   ; done
*
UNDFWD   LDMD R46,=GNMLEN      ; get len of GLOBAL name
         JNZ  NOTMT            ; jif non-empty, there's a GLOBALs file
UFWDLP   POMD R22,+R32         ; label table offset of next undef label
         LDMD R24,=ACODBA      ; end ('base') of label table
         POMD R26,+R32         ; get address in code of reference
         ADM  R26,R24          ; make it a pointer into the output code
         SBM  R24,R22          ; make R24 a pointer into the label table
         POMD R62,+R24         ; get label from the table into R62-67
         CLE
         ICE                   ; preset flag
         LDM  R46,=MUNDLB      ; address of UND LABEL
         JSB  =PRTER-          ; print out the UND LABEL message
         JSB  =DELREF          ; delete that ref from the fwd-ref stack
         CMM  R#,R#            ; CMM R32,R12 empty fwd-ref stack?
         JNZ  UFWDLP           ; jif no, loop
         JMP  FINFIN           ; finish up
*
* GLO file was included, read it in to satisfy undefined fwd-refs
*
NOTMT    JSB  =DATDN           ; move code & LblTbl down to highest RAM
         LDMD R34,=NXTMEM      ; get start of fwd-ref stack
CREFLP   LDM  R24,R12          ; get end of fwd-ref stack
         DCM  R24              ; actual last byte (SRC of what to move)
         LDM  R26,R12
         ADM  R26,=3,0         ; R26 = R12 + 3 (DST of where to move it)
         LDM  R22,R12
         SBM  R22,R34          ; R22 = len of fwd-refs (LEN to move)
         JSB  =MOVDN           ; MOVE THE FWD-REF STACK DOWN 4 BYTES
* we're in the process of changing a 4-byte fwd-ref
* into an eight byte entry containing the 6-byte label
* and the 2-byte offset into the code where the label
* was referenced.
         ADM  R12,=4,0         ; adjust R12
         LDMD R32,R34          ; get LblTbl offset of top item
         LDMD R36,=ACODBA      ; 'base' of label table
         SBM  R36,R32          ; abs mem ptr to label in table
         POMD R52,+R36         ; get label
         PUMD R52,+R34         ; push to fwd-ref stk in place of fwd-ref
         ICM  R34              ; skip two bytes of "code offset"
         ICM  R34
         CMM  R34,R12          ; done?
         JNZ  CREFLP           ; jif no, convert the rest
*
         LDMD R44,=GNMLEN      ; get len of GLO file name
         LDM  R46,=GLOFNM      ; address of GLO file name
         JSB  =ASGN1           ; ASSIGN# 1 TO "glo name"
*
* we're going to read in the GLOBALS file, leaving 256 bytes of
* space for the R12 stack to operate in, and potentially overwriting
* the just assembled label table (since we've already copied the
* undefined labels into the fwd-ref table.
*
         LDM  R36,R12          ; get end of R12 stack
         ADM  R36,=0,1         ; add 256 to get a buffer space
         PUMD R36,+R12         ; push the address twice on the op stack
         PUMD R36,+R12
         LDM  R34,=212,1       ; put oct-612/dec-394 into temp buffer
         PUMD R34,+R36         ; 1st WORD of global buffer=612=212,001
         LDMD R34,=ACODBA      ; get end of avail mem for global file
         SBM  R34,R36          ; length of available memory
         SBM  R34,=10,0        ; minus another 8 (for safety?)
         PUMD R34,+R36         ; push glo-avail-mem-len into buf 3 times
         PUMD R34,+R36
         PUMD R34,+R36
*
* so at this point, the global buffer starts with:
*  WORD 0612
*  WORD len-of-buffer
*  WORD len-of-buffer
*  WORD len-of-buffer
* <---R36
*
         PUMD R36,+R6          ; save global buf twice on rtn stk
RGLOLP   PUMD R36,+R6
         STMD R12,=TOS         ; set top of operating stack
         LDM  R34,=175,0       ; decimal-125
         PUMD R34,+R12         ; push 125 (len of str to read) to op stk
         PUMD R36,+R12         ; push buf addr (len/addr = string ref)
*
* assembled global files are DATA files containing 'strings'
* of 125 bytes each.  So, we have to read them in as chunks
* of 125 bytes.
*
         JSB  =REED$           ; read 125 bytes from the global file
*
         POMD R36,-R6          ; get address of where we just read to
         LDMD R40,R36          ; get 8 bytes from it
         CMMD R40,=BLANKS      ; 8 blanks?
         JZR  ENDGLO           ; jif yes, end of glob table
         ADM  R36,=372,0       ; +250 (125 for THIS read, 125 next)
         CMMD R36,=ACODBA      ; room for another read?
         JNC  GRDOK            ; jif yes
*
         JSB  =ERROR+
         DATA 23               ; MEM OVF
*
GRDOK    SBM  R#,=175,0        ; move R36 back 125 to read next block
         POMD R34,-R12         ; get buffer address from stack
         PUMD R34,+R12         ; push it back
         PUMD R34,+R12         ; push it again
         JMP  RGLOLP
*
ENDGLO   POMD R34,-R12         ; get address of glo buffer
DELBLN   POBD R34,-R36         ; get last char of glo buffer
         CMB  R34,=40          ; space?
         JZR  DELBLN           ; jif yes, throw-away last spaces
         STM  R36,R24          ; copy glo end ptr
         POMD R22,-R6          ; get ptr to beginning of glo buffer
         SBM  R36,R22          ; len of glo buffer
         STM  R36,R22          ; set as LEN for move
         DCM  R24              ; adjust ptr to SRC to 1st (highest) byte
         LDMD R26,=ACODBA      ; code base
         DCM  R26              ; -1 for DST ptr for move
         JSB  =MOVDN           ; move the global table down to the code
         ICM  R26              ; DST ptr=last (lowest) byte of glo table
         STMD R26,=ALBTBL      ; save as end of 'new' label table
         CLM  R34
         STMD R34,=GNMLEN      ; GLOBALS name len=0 to not process again
         LDMD R34,=NXTMEM      ; beginning of fwd-ref undefined table
GLBLLP   POMD R42,+R34         ; get label
         JSB  =SLBLTB          ; search the global label table for it
         JEN  GGLBL            ; jif found label in table
         PUMD R42,-R20         ; add label to the end of the label table
         CLM  R45              ; flags and address = 0
         PUMD R45,-R20         ; push into new entry in label table
         STMD R20,=ALBTBL      ; ajust end of table ptr
         ADM  R20,=3,0         ; move back to addr in table
GGLBL    LDMD R22,=ACODBA      ; beginning (high end) of label table
         SBM  R22,R20          ; minus ref = offset of label in table
         PUMD R22,-R34         ; push offset to LblTbl over last 2 bytes
         LDM  R32,R34          ; copy ptr to first 4 bytes of label
         JSB  =DELREF          ; del 1st 4 bytes of label as if fwd-ref
         CMM  R34,R#           ; R34==R12 = done processing fwd-ref stk
         JNZ  GLBLLP           ; jif not done, loop to do next one
         JSB  =ASGN*           ; close the globals file
         GTO NOTABS            ; now go finish normal processing
*
* ***************************************************
* NOTE: the following 4 bytes of ZERO don't appear to
* be called or referenced from anywhere.  No clue.
* ***************************************************
*
         DATA 0,0,0,0
*
* ***************************************************
*
ALST.    LDB  R#,=377          ; turn LISTING on
SLST     STBD R#,=LSTFLG       ; save LST state
         RTN
*
AUNL.    CLB  R#               ; turn LISTING off
         JMP  SLST
*
AGLO.    LDMD R45,=ILNMAB      ; already seen NAM or ABS?
         JZR  GGLONM           ; jif no, GLO is okay
         LDM  R46,=(MILGLO).2  ; else ILL GLO error
*
PRTERR   CLE
PRTER-   STM  R46,R60
         JSB  =PSHRGS          ; save R20-R47
         LDM  R46,R60
         JSB  =CPYSTR          ; copy string to output buf
         JSB  =DOPRNT          ; output = PRINTER IS device
         LDMD R36,=SAVER6      ; get line# of problem
         ARP  R30
         JEN  PELBL            ; jif show label
*
         DRP  R40              ; load " ON LINE" into R40-R47
         DATA 251
         DATA  " ON LINE"
*
         PUMD R40,+R30         ; push to output buffer
         PUBD R40,+R30         ; and space after " ON LINE"
         JSB  =DCLIN#          ; and the line#
PEDMP    JSB  =DMPBUF          ; print the buffer
         LDMD R2,=AERCNT       ; get the error counter
         ICM  R2               ; bump it up one
         STMD R2,=AERCNT       ; save it again
         JSB  =POPRGS          ; restore R20-R47
         RTN
*
WDUPLB   DATA  "WARN:"
EDUPLB   DATA  `DUP LAB`
*
PELBL    LDB  R61,=40          ; put space in front
         PUMD R61,+R#          ; push out the space-label
         JMP  PEDMP
*
GGLONM   CMB  R20,=16          ; EOL token?
         JZR  ST16             ; jif yes, this IS a global file
         LDM  R46,R10          ; copy input name ptr
         LDM  R56,=GLOFNM      ; global name buffer ptr
         JSB  =GFNAME          ; get a clean file name
         STMD R#,=GNMLEN       ; save len of GLOFNM
         RTN
*
ST16     STBD R#,=ISGLO        ; set flag that we're IN a global file
         RTN
*
MILGLO   DATA  `ILL GLO`
*
* INPUT:
* R46 = ptr to input (expected to be filename with EOL (16) tok on end)
* R56 = ptr to output
* OUTPUT:
* R10 = pointing to next byte after the EOL token
* R46 = len of filename that was processed
* filename in R56 has been limited to 10 chars and optionally a 6 char
* MSUS or volume label
GFNAME   LDB  R40,=12          ; maximum length of filename (10 dec)
         STM  R46,R44          ; copy starting ptr
FNAMLP   POBD R20,+R46         ; get byte of name
         CMB  R20,=16          ; EOL token?
         JZR  FEOL             ; jif yes
         CMB  R20,=72          ; ':' ?
         JZR  FCOLON           ; jif yes
         CMB  R20,=56          ; '.' ?
         JZR  FCOLON           ; jif yes
         TSB  R40              ; got all 10 chars?
         JZR  FNAMLP           ; jif yes (toss everything after 10)
         DCB  R40              ; decrement len counter
         PUBD R20,+R56         ; put the byte to the output
         JMP  FNAMLP           ; go get more
*
* got MSUS or VOLUME LABEL
FCOLON   PUBD R#,+R56          ; push the ':' or '.'
         LDB  R40,=6           ; allow 6 more chars
CODOLP   POBD R20,+R46         ; get next char
         CMB  R20,=16          ; EOL?
         JZR  FEOL             ; jif yes
         PUBD R20,+R56         ; else push the char out
         DCB  R40              ; decrement len counter
         JNZ  CODOLP           ; jif not exhausted
FEOL     STM  R46,R10          ; update R10 to what we've used up
         SBM  R46,R44          ; get len of what we pushed
         DCM  R46              ; minus 1 for the EOL token
         RTN
*
FROM     LDMD R24,=ACODBA      ; beginning of code
         STMD R24,=LEGEND      ; save address of what to write
         LDMD R26,=ACODEN      ; end of code
         DCM  R26              ; minus one = last byte to write
         STMD R26,=ENDWRI      ; save it
         JMP  WCOM
*
FGLO     LDMD R24,=ALBTBL      ; beginning of label table
         STMD R24,=LEGEND      ; save it
         LDMD R26,=ACODBA      ; end of label table
         STMD R26,=ENDWRI      ; save it
         STMD R27,R26          ; store byte with MSbit set
* I'm guessing the above line of code puts a byte with the MSbit set
* into the next byte after the 'last' label, which would be the FLAG
* byte of the 'next' label, if there were a next label.  The FLAG byte
* normally seems to have a 0 in the MSbyte, so this would flag "end of
* global table" in the GLO file.  Maybe.
*
WCOM     BIN
         SBM  R26,R24          ; len of what to write
*
* we're converting len of what to write into number of sectors
* sectors are 256 bytes, so adding 7 to the upper byte of the len
* and ignoring the LSbyte essentially rounds up the length to
* 6 more sectors than what's really needed.  This is done so that,
* as the ROM or BPGM is developed and continues to grow, it doesn't
* create an on-going series of ever-larger NULL file holes in the
* directory.  Rather, an extra-large "file hole" is created up front,
* and will remain in use through subsequent assemblies until the file
* grows larger than than (ie, by at least 1.5 Kbyte), at which point
* we'll then create a new "file hole" that is 6 sectors larger than
* what is needed at that point.  You'll still end up with ongoing
* disk/tape-fragmentation, but it will happen at a much slower rate.
*
         ADB  R27,=7           ; round up the file len by ~6 sectors
         STB  R27,R26          ; copy to the lower byte
         CLB  R27              ; 0 upper, now have rounded-up #sectors
         STM  R26,R36          ; copy to CONBIN's desired register
         JSB  =CONBIN          ; convert R36-37 to a REAL number
         STMD R12,=TOS         ; set top of stack
         PUMD R40,+R6          ; save the REAL value
         JSB  =PREPON          ; prepare output file name
         JSB  =SETSR6          ; set SAVER6 to space on the R6 stack
         JEN  FINTAP           ; jif MS ROM not present
*
         JSB  =ROMJSB
         DEF  DIRSCN           ; scan directory for our output name
         DATA 320
*
         JEN  DNOFIL           ; jif not found
*
         JSB  =ROMJSB
         DEF  GETTYP           ; get the file type
         DATA 320
*
         CMB  R30,=20          ; DATA file type?
         JZR  DATFIL           ; jif yes
TAPBAD   POMD R40,-R6          ; trash the record count on the stack
*
         JSB  =ROMJSB
         DEF  TAPEXT           ; exit clean up stuff
         DATA 0
*
         JSB  =ERROR
         DATA 104              ; File type
*
         RTN
*
DATFIL   JSB  =ROMJSB
         DEF  TYPOK2           ; seek to the file
         DATA 320
*
         JMP  WRIFI            ; go finish writing the file
*
DNOFIL   JSB  =GETONM          ; get the output file name
         POMD R40,-R6          ; get # of records
         PUMD R40,+R12         ; push on op stack
*
         JSB  =ROMJSB
         DEF  MSCRE.           ; CREATE "filename", #_recs
         DATA 320
*
         JMP  WRIFI-           ; now go write everything to it
*
TAPGO    LDBD R47,X36,F.TYPE   ; get file type
         ANM  R47,=374         ; strip 2 lower bits
         CMB  R47,=20          ; DATA file?
         JZR  WRIFI            ; jif yes, write to it
         JMP  TAPBAD           ; else BAD.  BAD BOY!
*
FINTAP   JSB  =PARGNM          ; push the output name
*
         JSB  =ROMJSB
         DEF  TAPINT           ; init the tape software
         DATA 0
*
         BIN
         CMB  R17,=300         ; errors?
         JCY  TAPBAD           ; jif yes
*
         JSB  =ROMJSB
         DEF  DSCAN            ; scan the tape directory
         DATA 0
*
         JEZ  TAPGO            ; jif file found
*
         JSB  =PREPON          ; push the output file name
         POMD R40,-R6          ; get the number of records
         PUMD R40,+R6          ; save again
         PUMD R40,+R12         ; push on op stack
*
         JSB  =ROMJSB
         DEF  CREAT.           ; do tape CREATE "filename", #_records
         DATA 0
*
WRIFI    POMD R40,-R6          ; get # records off stack
WRIFI-   LDMD R44,=ABNLEN      ; get len of output file name
         LDM  R46,=ABPNAM      ; get address of output file name
         JSB  =ASGN1           ; open the data file
         LDMD R46,=LEGEND      ; get addr of what to write
WRIDAT   LDM  R36,=175,0       ; # bytes to write at a time (125 dec)
         STM  R36,R44          ; store in R44-R45
         ADM  R46,R36          ; plus len = ptr to end of what to write
         CMMD R46,=ENDWRI      ; past end of what to write?
         JCY  ENDBLK           ; jif yes
         PUMD R46,+R6          ; else save end address
         SBM  R46,R36          ; get start address
         JSB  =PRT$            ; print this chunk to file (125 bytes)
         POMD R46,-R6          ; recover next address to write from
         JMP  WRIDAT           ; loop
*
ENDBLK   SBM  R#,R#            ; minus len = addr of start of last block
         LDMD R36,=ENDWRI      ; get address of last byte to write
         SBM  R36,R46          ; last ptr - start ptr =len-1
         ICM  R36              ; # bytes in last block
         STM  R36,R44          ; put in R44-45
         JSB  =PRT$            ; print the last block
         CLM  R44
         JSB  =PRT$            ; flush the buffer
ASGN*    JSB  =P12_1           ; push a REAL 1 on the op stack
         CLM  R44
         ICM  R44              ; len of 1
         LDM  R46,=ASTAR       ; addr of a '*' value in tape software
         JMP  ASGN             ; do ASSIGN# 1 TO * to close the file
*
P12_1    CLM  R50
         LDB  R57,=20          ; R50-57 = REAL# 1.000
         PUMD R50,+R12         ; push it on the op stack
         RTN
*
ASGN1    STMD R12,=TOS         ; set top of stack
         JSB  =P12_1           ; push REAL 1 on op stack
         JSB  =ASGN            ; do ASSIGN
         JSB  =P12_1           ; push REAL 1 on op stack
         JSB  =PRTNUM          ; start PRINT# 1
ARTN76   RTN
*
ASGN     PUMD R44,+R12         ; push file name and len on op stack
         PUMD R44,+R6          ; also save for later
         JSB  =PREPO-          ; prepare output file name
         POMD R44,-R6          ; recover the file name ptr and len
         JEN  TAPASG           ; jif no MS ROM
         PUMD R44,+R12         ; else push the file name again
*
         JSB  =ROMJSB
         DEF  ASSIG.           ; do MSROM ASSIGN# 1 TO "filename"
         DATA 320
*
         JMP  ERCHK9
*
TAPASG   POMD R64,-R12         ; pop MS ROM name
         PUMD R44,+R12         ; push TAPE name
         JSB  =ROMJSB
         DEF  ASIGN.           ; do TAP ASSIGN# 1 TO "filename"
         DATA 0
*
ERCHK9   CMB  R17,=300         ; errors?
         JNC  ARTN76           ; jif no
         JSB  =BAIL            ; else bail out, don't come back
*
A1DRP    LDM  R26,=CURDRP      ; address of CURDRP
         JSB  =AGTVAL          ; chew up R number
         JEZ  BDRPNU           ; jif failed
         LDB  R21,=100
         ORB  R76,R21          ; change reg# into DRP instruction
DRPCMP   CMBD R#,R26           ; same as previous DRP?
         JZR  SAMDRP           ; jif yes
         STBD R#,R26           ; else save new CURDRP
         PUBD R#,+R24          ; push out DRP instruction
SAMDRP   POBD R20,+R10         ; get next char
         CMB  R20,=54          ; comma?
         JNZ  DRP73R           ; jif no
         POBD R20,+R10         ; get next char
DRP73R   DRP  R73
         RTN
*
BDRPNU   CMB  R20,=43          ; '#' ?
         JZR  SAMDRP           ; jif yes
         LDB  R76,=101         ; else DRP 1 for R*
         JMP  DRPCMP
*
A1ARP    CMB  R20,=75          ; '=' ?
         JZR  AGOT=            ; jif yes
*
         LDM  R26,=CURARP      ; addres of CURARP
         JSB  =AGTVAL          ; get # from input asm line
         JEZ  BARPNU           ; jif failed
ARPCMP   CMBD R#,R26           ; same as previous value was?
         JZR  SAMARP           ; jif yes,
         STBD R#,R26           ; else save new ARP reg#
         PUBD R#,+R24          ; push out ARP instruction
SAMARP   POBD R20,+R10         ; get next char
         CMB  R20,=54          ; comma?
         JNZ  DRP73R           ; jif no
         ICB  R70
AGOT=    ICB  R70              ; R70=0 (R,R) =1 (R,=) =2 (R,R,=)
         ICB  R75              ; R75=0 (R,R) =1 (R,R,ADDR or ADDR)
         RTN
*
BARPNU   CMB  R20,=43          ; '#'?
         JZR  SAMARP           ; jif yes, was R#
         LDB  R76,=1           ; else ARP 1 for R*
         JMP  ARPCMP
*
PSHIMM   LDBD R20,R10          ; peek at next char
         JSB  =DIGIT           ; literal number?
         JEN  GETLIT           ; jif yes
         POMD R41,+R10         ; else should be a label, get it
         JSB  =ADR16-          ; push the label value or a fwd-ref
         TSB  R71              ; immediate addressing mode?
         JNZ  ARTN78           ; jif no
         TSB  R72              ; multi-byte immediate?
         JNZ  IMMULT           ; jif yes, leave as is
IMM-1    POMD R56,-R24         ; else pop two byte value
         PUBD R56,+R24         ; push back just one byte value
ARTN78   RTN
*
GETLIT   JSB  =GET#            ; get the numeric value
         PUBD R#,+R24          ; push it out
         CMB  R20,=54          ; comma?  (more?)
         JZR  GETLIT           ; jif yes
         RTN
*
IMMULT   LDBD R77,=CURDRP      ; get current DRP value
         CMB  R77,=40          ; less than 40?
         JCY  IMM8             ; jif no
         TSB  R77              ; if DRP is odd, only 1 byte
         JOD  IMM-1            ; jif yes, trash the second byte
         RTN
*
IMM8     ANM  R77,=7           ; get DRP offset in 8-byte register
         CMB  R77,=7           ; last byte of 8-byte reg so only 1 byte
         JZR  IMM-1            ; jif yes, trash the second byte
         RTN
*
MJMPTO   DATA  `JMP TO`
*
* **********************************************************************
* A previously referenced label has now been defined.
* Search through the forward reference list, find any references
* to the new label, and go back and patch their address.
* ENTRY:
* ARP=20
* R24 = ACODEN (end of new code ptr)
*
SATREF   POMD R55,+R#          ; get line#/addr and flags from LblTbl
         LDMD R46,=ACODBA      ; get end of label table ptr
         SBM  R46,R20          ; offset of label from end of table
         LDMD R32,=NXTMEM      ; get beginning of fwd-ref table
REFLOP   CMM  R32,R12          ; reached end of reference table?
         JCY  ARTN80           ; jif yes, done
         CMMD R46,R32          ; offset of label match offset from ref?
         JZR  GOTREF           ; jif yes
         ADM  R32,=4,0         ; skip to next entry in reference table
         JMP  REFLOP           ; try next one
*
GOTREF   POMD R30,+R#          ; throw away offset
         POMD R30,+R#          ; get offset into code where ref occurred
         ADMD R30,=ACODBA      ; add offset to base of code
         LDMD R34,R30          ; get bytes from where label ref occurred
*
         CMB  R34,=326         ; abs value ref (JSB, LD, ST, etc)?
         JZR  ABSREF           ; jif yes
*
         CMB  R34,=377         ; is it a GTO reference?
         JZR  GTOREF           ; jif yes
*
* must be a relative JMP instruction then
*
         LDM  R36,R24          ; address of label we're de-referencing
         SBM  R36,R30          ; minus location of ref
         DCM  R36
         CMB  R36,=200         ; > 128 bytes (rel jmp distance limit)
         JNC  RELJOK           ; jif less
RELJER   PUMD R65,+R6          ; save registers
         PUMD R32,+R6
         LDM  R46,=MJMPTO      ; JMP TO error
         JSB  =PRTERR          ; output the error
         POMD R32,-R6          ; restore registers
         POMD R65,-R6
         JMP  DELIT
*
RELJOK   CMB  R37,=0           ; make sure upper byte of distance is 0
         JNZ  RELJER           ; jif not, error
         STBD R36,R30          ; else set rel jmp offset at label ref
DELIT    JSB  =DELREF          ; delete used up reference
         JMP  REFLOP
*
DELREF   JSB  =PSHRGS          ; save regs
         LDM  R22,R12          ; end of forward-reference table
         SBM  R22,R32          ; - curr (finished) ref = len to move
         LDM  R24,R32          ; source (first byte) to move
         LDM  R26,R32          ; copy
         SBM  R26,=4,0         ; minus 4 = dest where to move to
         JSB  =MOVUP           ; deleting the finished ref
         SBM  R12,=4,0         ; adjust end-of-table ptr
         JSB  =POPRGS          ; restore regs
         SBM  R32,=4,0         ; adjust curr ref ptr for more looping
         ARP  R12
ARTN80   RTN
*
ABSREF   TSB  R55              ; addr known or is it a fwd-ref'd label?
         JZR  REFLOP           ; jif unknown, skip it
         PUBD R56,+R30         ; push byte of label value into code
         CMB  R35,=326         ; two bytes of abs value in code?
         JNZ  DELIT            ; jif no, done
         PUBD R57,+R30         ; push secont byte of label value
         JMP  DELIT            ; done
*
GTOREF   TSB  R55              ; addr known or is it a fwd-ref'd label?
         JZR  REFLOP           ; jif unknown, skip it
         DCM  R56              ; adjust addr by 1 required by LDM R4,=
         PUMD R56,+R30         ; push the address into the code
         JMP  DELIT            ; done
*
* *****************************************************
         DATA 141
ALOAD.   JSB  =PREPO-          ; prep file name
         JEN  ALODTP           ; jif no MS ROM
         JSB  =SCRUS           ; SCRATCH and set up for load
*
ALODD    JSB  =ROMJSB
         DEF  LOADBR           ; do modified load of ASM SRC file
         DATA 320
*
         JMP  ALDFIN           ; finish up
*
ALODTP   JSB  =PARGNM          ; set up tape name
         JSB  =SCRUS           ; SCRATCH and set up for load
*
ALODT    JSB  =ROMJSB
         DEF  LOADB&           ; do modified load of ASM SRC file
         DATA 0
*
ALDFIN   CLB  R16              ; set system idle mode
*
         JSB  =ROMJSB
         DEF  LDCOMN           ; enable interrupts, end the tape load
         DATA 0
*
         RTN
*
SCRUS    JSB  =ERMSGS          ; do SCRATCH
         LDMD R14,=MSBASE      ; MS ROM RAM
         LDMD R56,=LAVAIL      ; end of RAM
SETLDA   STMD R#,=LSTDAT       ; set last end of space to read into
         ICB  R16              ; set system calculator mode
         JSB  =STATYP          ; set ASSM file type and load FWCURR
         STMD R#,=NXTDAT       ; set start of where to read to
         RTN
*
STATYP   LDB  R56,=4           ; extended file type (ASSM SRC)
         STBD R56,=FILTYP      ; set it
GTFWCU   LDMD R56,=FWCURR      ; where to read in to
         ARP  R56
         RTN
*
* An OCTAL value has been passed on the R12 stack.  Convert it to a
* DECIMAL so we can get it off the stack and convert it to a BINARY
* value in R46-47.  Reload R14 with ASMBAS on the way out.
*
*
OCTBIN   JSB  =DEC.            ; convert octal# on stk to dec# on stk
         CMB  R17,=300         ; any errors?
         JCY  BAIL             ; jif yes
GTBIN+   JSB  =GTBIN#          ; get address as a binary value in R46-47
GTABAS   LDMD R14,=ASMBAS      ; load R14 with ASM ROM RAM address
         BIN                   ; make sure CPU is in BINARY mode
         ARP  R14              ; leave DRP and ARP both pointing at R14
         RTN
*
REED$    JSB  =STUPD
         JSB  =SETSR6          ; set SAVER6
         JEN  TREED$
*
         JSB  =ROMJSB
         DEF  RD#$             ; MSROM READ# string
         DATA 320
*
         JMP  CHKER8           ; check if errors
*
TREED$   JSB  =ROMJSB
         DEF  READ#$           ; TAPE READ# string
         DATA 0
*
CHKER8   CMB  R17,=300         ; any error?
         JNC  ARTN75           ; jif no
         LDMD R26,=CURLOC      ; get CURLOC
         JSB  =CLOSE+          ; close the file
*
* terminal error has occurred
* BAIL OUT!!!!
*
BAIL     LDM  R6,=STACK        ; reset R6 stack
         LDM  R34,=EXEC        ; to executive loop
         PUMD R34,+R6          ; push it on the stack
ARTN75   RTN                   ; return to the EXEC loop
*
PRT$     JSB  =STUPD           ; setup disk and get ready
         JSB  =SETSR6          ; save ptr to R6 stack area
         JEN  TAPPRT           ; jif no MS ROM
*
         JSB  =ROMJSB
         DEF  PR#$             ; print to file
         DATA 320
*
         JMP  CHKER8           ; check for errors
*
TAPPRT   JSB  =ROMJSB
         DEF  PRNT#$           ; call TAPE print$ routine
         DATA 0
*
         JMP  CHKER8           ; check for errors
*
STUPD    JSB  =INIMS           ; init MS ROM for access
         JEN  ARTN74           ; jif not there
*
         JSB  =ROMJSB
         DEF  CKMSUS           ; make sure MSUS and disk are okay
         DATA 320
*
ARTN74   RTN
*
PRTNUM   JSB  =MSIN?           ; MS ROM here?
         JEN  TAPNUM           ; jif no
*
         JSB  =ROMJSB
         DEF  MSPRT.           ; print DISK
         DATA 320
*
         JMP  CHKER8           ; see if errors
*
TAPNUM   JSB  =ROMJSB
         DEF  PRNT#.           ; print TAPE
         DATA 0
*
         JMP  CHKER8           ; see if error
*
* Send the buffer to the DISPLAY or PRINTER
DUMPIT   JSB  =ROMJSB
         DEF  DRV12.           ; DISP or PRINT the buffer
         DATA 0
         JSB  =GTABAS          ; reload R14 with ASM RAM
         RTN
*
PARNE+   JSB  =ROMJSB
         DEF  NUMEX+           ; parse a numeric expression
         DATA 0
         RTN
*
* who WROTE this code?  there are TWO identical subroutines!!!
* I hope one of them got removed in the HP-87 version!!!
*
PARNE2   JSB  =ROMJSB
         DEF  NUMEX+           ; scan and get numeric expression
         DATA 0
         RTN
*
PARGNM   JSB  =ROMJSB
         DEF  GETNAM           ; get the TAPE file name
         DATA 0
         RTN
*
* Prepare the output file name
*
PREPON   JSB  =GETONM          ; set up the output file name
PREPO-   JSB  =INIMS           ; init the MS ROM for access (if present)
         JEN  ARTN63           ; jif no MS ROM
*
         JSB  =ROMJSB
         DEF  TAPDS-           ; decode the file specifier
         DATA 320
*
         CMB  R17,=300         ; error?
         JCY  BAIL             ; jif yes
ARTN63   RTN                   ; else done
*
SETSR6   LDM  R20,R6           ; get ptr to top of R6 stack
         ADM  R20,=5,0         ; +5 (allow a little extra space?)
         STMD R20,=SAVER6      ; save the ptr to SAVER6
         RTN
*
* *********************************************
* ASTORE
* *********************************************
         DATA 141              ; attrib: non-programmable BASIC stmt
ASTOR.   JSB  =PREPO-          ; prepare the file name
         JSB  =SETSR6          ; set SAVER6
         JEN  ASTORT           ; jif no MSROM
         JSB  =STSEC?          ; check security, setup for store
*
         JSB  =ROMJSB
         DEF  STRB-            ; MS ROM store ASSM code as an ASSM file
         DATA 320
*
         RTN                   ; done
*
ASTORT   JSB  =PARGNM          ; set up file name
         JSB  =STSEC?          ; check security, setup for store
*
         JSB  =ROMJSB
         DEF  STORB-           ; TAPE store src code as an ASSM file
         DATA 0
*
         RTN                   ; done
*
STSEC?   LDB  R0,=1            ; store security
         JSB  =SECUR?          ; is it secured against storing?
         JEZ  STOK             ; jif no
         POMD R20,-R6          ; else trash return, don't continue
         RTN                   ; done
*
STOK     JSB  =STATYP          ; set ASSM file type and load FWCURR
         JSB  =ST240+          ; set IMMEDIATE mode, IDLE, reset R12 stk
         LDMD R76,X56,P.LEN    ; get source code "program" length
         BIN
         ADM  R76,R56          ; add to base = end of source code
         STMD R12,=STSIZE      ; set bottom of stack
         RTN
*
* Initialize the MS ROM for access
*
INIMS    BIN
         JSB  =MSIN?           ; is the MS ROM here?
         JEN  MSEX             ; jif no
*
         JSB  =ROMJSB
         DEF  MSIN             ; initialize the MS ROM for calls
         DATA 320
*
         JSB  =SETSR6          ; point SAVER6 into unused R6 stack
*
* return E=0 if MS ROM IS present, else E#0 if NOT present
*
MSIN?    CLE
         ICE                   ; preflag is NOT present
         LDM  R20,=ROMTAB      ; address of table of present ROMs
MSINLP   POMD R24,+R20         ; get next one
         CMB  R24,=377         ; end of table?
         JZR  MSEX             ; jif yes
         CMB  R24,=320         ; MS ROM?
         JNZ  MSINLP           ; jif no, keep looking
         CLE                   ; flag it IS here
MSEX     RTN
*
PABS     CLB  R30              ; clear ROM flag
         CMB  R20,=122         ; 'R' ?
         JNZ  ABSNOR           ; jif no
         PUBD R20,+R12         ; push 'R'
         JSB  =GCHAR           ; get next char
         CMB  R#,=117          ; 'O' ?
         JNZ  PABSER           ; jif no
         PUBD R#,+R12          ; push 'O'
         JSB  =GCHAR           ; get next char
         CMB  R#,=115          ; 'M' ?
         JNZ  PABSER           ; jif no
         PUBD R#,+R12          ; push 'M'
         LDB  R#,=40           ; SPACE
         PUBD R#,+R12          ; push SPACE
         ICB  R30              ; set ROM flag
         JSB  =GCHAR           ; get next char
         JSB  =PRGNUM          ; get address
         TSB  R23              ; get something?
         JZR  PABSER           ; jif no
         TSB  R22              ; digits > 7 ?
         JZR  ARTN88           ; jif no
PABSER   JSB  =ERREXP
ARTN88   RTN
*
ABSNOR   CMB  R#,=61           ; '1' ?
         JNZ  ABSNO1           ; jif no
         PUBD R#,+R12          ; push it
         JSB  =GCHAR           ; get next char
         CMB  R#,=66           ; '6' ?
ABSFIN   JNZ  PABSER           ; jif no
         GTO P#*               ; push it and finish
*
ABSNO1   CMB  R#,=63           ; '3' ?
         JNZ  PABSER           ; jif no
         PUBD R#,+R12          ; push it
         JSB  =GCHAR           ; get next char
         CMB  R#,=62           ; '2' ?
         JMP  ABSFIN           ; finish
*
PORXR    JSB  =PRGCMA          ; get a register reference and a comma
         JEZ  ERCMA            ; jif failed
*
*  else fall through and get the second register reference
*
P1REG    JSB  =PR              ; process/push the 'R'
P1REGN   JSB  =PREG#*          ; see if # or * is there
         JEN  ARTN88           ; jif yes, done
         JSB  =PRGNUM          ; else demand an actual register number
         TSB  R#               ; get digits <'7'?
         JNZ  ADERR            ; jif no
         CMB  R23,=3           ; too many digits?
         JCY  ADERR            ; jif yes
         TSB  R23              ; get ANY digits?
         JZR  ADERR            ; jif no
         CMB  R23,=1           ; just one digit?
         JNZ  ARTN88           ; jif no
         POBD R23,-R12         ; get last char
         PUBD R23,+R12         ; put it back
         CMB  R23,=61          ; '1'?  (Direct reference to R1 illegal)
         JNZ  ARTN88           ; jif no
ADERR    JSB  =AROMER          ; set Assembler ROM error
         JSB  =ERROR           ; report the error
         DATA 14               ; ARP-DRP
         RTN
*
PLDST    JSB  =P_IORD          ; see if I or D follows the 3-char opcode
         JEN  PID              ; jif yes
PIMMED   JSB  =PRGCMA          ; else immediate, get register and comma
         JEZ  ERCMA            ; jif no comma
         JSB  =PTRYEQ          ; parse '=' if there
         JEZ  P1REG            ; jif not, get a register ref
         JSB  =DIGIT           ; is a digit next?
         JEZ  PLBREF           ; jif no
PNXTO    JSB  =PRGNUM          ; get immediate arg value
         CMB  R23,=4           ; > three digits? (more than a byte?)
         JCY  OPERER           ; jif yes, operand error
         TSB  R23              ; no digits?
         JZR  OPERER           ; jif no, operand error
         JSB  =TSTCMA          ; is there a comma (list of operands)
         JEN  PNXTO            ; jif yes, get next operand
ARTN86   RTN
*
BSZORG   JSB  =PRGNUM          ; get number
         JNZ  ARTN86           ; jif got it
OPERER   JSB  =AROMER          ; set ASM ROM# into ERROM#
         JSB  =ERROR
         DATA 15               ; OPER error
         RTN
*
PID      JSB  =PRGCMA          ; get register and comma
         JEZ  ERCMA            ; jif failed
         JSB  =PTRYEQ          ; '=' ?
         JEN  PLBREF           ; jif yes, get the label
         JSB  =PX              ; 'X' ?
P1RJEZ   JEZ  P1REG            ; jif no
PCMALB   JSB  =TSTCMA          ; get comma
         JEN  PLBREF           ; jif yes, get label
*
ERCMA    JSB  =ERROR
         DATA 123              ; "," MISSING
         RTN
*
* parse CM, AD, SB, AN
PADSB    JSB  =CHK_D           ; 'D' ? (direct addressing?)
         JEZ  PIMMED           ; jif no, do immediate mode
         JSB  =PRGCMA          ; else get the register and comma
         JEZ  LBLERR           ; jif no comma
         JSB  =PTRYEQ          ; see if =
         JEZ  P1RJEZ           ; jif no, do register
PLBREF   CMB  R20,=15          ; CR next?
         JZR  LBLERR           ; jif yes, expected a label
         JSB  =NOBNG           ; get the label
         RTN
*
LBLERR   JSB  =AROMER          ; set Assembler ROM as error source
         JSB  =ERROR           ; report error
         DATA 12               ; LBL
         RTN                   ; done
*
* parse PU and PO
PPUPO    JSB  =P_IORD          ; see if 'I' or 'D'
         JEZ  ERREXP           ; jif no, PU/PO is direct or indirect
         JSB  =PRGCMA          ; get register reference and comma
         JEZ  ERCMA            ; jif no comma
         CMB  R#,=53           ; '+' ?
         JZR  PUSHID           ; jif yes
         CMB  R#,=55           ; '-' ?
         JZR  PUSHID           ; jif yes
*
ERREXP   JSB  =ERROR           ; report error
         DATA 121              ; Bad exression
         RTN
*
PUSHID   JSB  =P#*             ; push the I or D and GCHAR
         CLE                   ; clear E so P1RJEZ will jmp
         JMP  P1RJEZ           ; go get the second register reference
*
PJSB     JSB  =PTRYEQ          ; '=' ?
         JEN  PLBREF           ; jif yes, get label
         JSB  =PX              ; try to get index ('X' register)
         JEN  PCMALB           ; jif found, get comma and label
OEJMP    JMP  OPERER           ; else operand error
*
TSTCMA   CMB  R20,=54          ; comma?
         JMP  PTST             ; go push and/or set flags
*
PTRYEQ   CMB  R20,=75          ; '=' ?
         JMP  PTST             ; test and push
*
P_IORD   CLE                   ; clear successful flag
         CMB  R20,=111         ; 'I' ?
         JZR  P#*              ; jif yes
CHK_D    CMB  R20,=104         ; 'D'?
         JMP  PTST             ; finish test
*
* Parse the 'R' of a REGISTER reference
PR       LDB  R21,=122         ; load an 'R' character
         PUBD R21,+R12         ; push it
         CMB  R21,R20          ; did they TYPE the 'R' character?
         JNZ  ARTN87           ; jif no
         JSB  =GCHAR           ; else toss it and get the next char
ARTN87   RTN
*
PX       CLE                   ; preclear to failure
         CMB  R20,=130         ; 'X' ?
         JNZ  ARTN87           ; jif no, failed
         PUBD R20,+R12         ; push X
         JSB  =GCHAR           ; get next char
         JSB  =P1REGN          ; get the register number
         ICE
         RTN
*
PDADEQ   TSB  R41              ; was there a label on this line?
         JZR  LBLERR           ; jif no, need one for a ADDR or EQU
         JSB  =PRGNUM          ; get the address or value
         JZR  OEJMP            ; jif not found, op error
         RTN
*
* Parse the '#' or '*' in a REGISTER reference
PREG#*   CLE                   ; clear success flag
         CMB  R20,=43          ; '#' character?
         JNZ  P*?              ; jif no
P#*      PUBD R20,+R12         ; else push it out
         JSB  =GCHAR           ; get the next char
         ICE                   ; flag success
         RTN
*
P*?      CMB  R#,=52           ; '*' character?
PTST     CLE                   ; clear successful flag
         JZR  P#*              ; jif yes
         RTN
*
TSTSIZ   CMB  R23,=3           ; too many digits?
         JCY  OEJMP            ; jif yes
TSTDIG   TSM  R22              ; did we get at least ONE digit?
         RTN
*
REGDON   JSB  =CHK_D           ; see if 'D' after number
         JEN  TSTDIG           ; jif yes, see if any register numbers
         JSB  =TST_C           ; else see if 'C' after num
         JEN  TSTSIZ           ; jif yes, see if too many digits
         TSB  R22              ; get digits >7 ?
         JZR  TSTDIG           ; jif no, make sure we got SOME digit
OEJMP2   JMP  OEJMP            ; no C, no D, digit>7 = OPER error
*
PRGNUM   DCM  R10              ; put the last char back
         CLM  R22              ; clear flags
PGETDG   JSB  =GCDIG           ; get next char, then try for a digit
         JEZ  REGDON           ; jif no number
         PUBD R20,+R12         ; else push it out
         CMB  R20,=70          ; < '8' ?
         JNC  PDIGOK           ; jif less
         ICB  R22              ; increment count of digits > 7
PDIGOK   ICB  R23              ; increment count of digits seen
         JMP  PGETDG           ; try for a second one
*
TST_C    CMB  R20,=103         ; 'C' ?
         JMP  PTST
*
PASPQU   CMB  R20,=42          ; '`' ?
         JNZ  OEJMP2           ; jif no, operand error
         PUMD R12,+R6          ; save r12 output
         JSB  =PSHSTR          ; push everything from here to EOL
FENDQU   DCM  R10              ; put EOL back
         POBD R20,-R12         ; pop char from output
         CMB  R20,=42          ; '"' ? (find end/closing quote)
         JNZ  FENDQU           ; jif no
         POMD R22,-R6          ; recover starting R12 ptr
         CMM  R22,R12          ; different quote?
         JZR  OEJMP2           ; jif no, operand error
         JMP  P#*              ; else finish up
*
PASP     JSB  =PRGNUM          ; see if # for len of unquoted string
         JZR  PASPQU           ; jif no
         CMB  R20,=54          ; comma?
         JZR  PSHST-           ; jif yes
         GTO ERCMA             ; else error, comma expected
*
PSHSTR   CMB  R20,=15          ; CR?
         JZR  ARTN85           ; jif yes, eol
PSHST-   PUBD R#,+R12          ; push out char
         POBD R#,+R10          ; get next char
         JMP  PSHSTR           ; do rest of line
*
PGLO     CMB  R20,=15          ; CR?
         JZR  ARTN84           ; jif yes, declaring this a GLOBAL file
PLNK     LDB  R20,=377         ; label marker? (for file name)
         PUBD R20,+R12         ; push out
         LDM  R56,R12
         DCM  R10              ; put fetched char back
         STM  R10,R46          ; copy input ptr
         STM  R10,R66          ; and again
GLOEOL   POBD R76,+R#          ; get byte from copy of input ptr
         CMB  R76,=15          ; CR?
         JNZ  GLOEOL           ; jif no, find EOL
         DCM  R66              ; put the CR back
         ICB  R76              ; turns the 15 CR into 16 EOL token
         STBD R76,R#           ; put it on the end
         JSB  =GFNAME          ; get the filename
         STM  R56,R12          ; update output ptr to end of filename
         DCM  R76              ; change the EOL token back to a CR
         STBD R76,R66          ;    in the input buffer
GLOTOS   POBD R20,+R10         ; get the next char
         CMB  R20,=15          ; CR?
         JNZ  GLOTOS           ; jif no, throw everything else away
ARTN84   RTN
*
PRGCMA   JSB  =P1REG           ; get a register reference
         JSB  =TSTCMA          ; get comma
ARTN85   RTN
*
*        BSZ  12               ; unused bytes at ROM's end
*
*        DATA 113,304,155,143  ; ROM checksums
         END
