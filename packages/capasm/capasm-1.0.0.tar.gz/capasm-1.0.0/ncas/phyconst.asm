* -------------------------
* HP 75 LEX File
* ASTORE "PHYCONS75S"
* ASSEMBLE "PHYCONS75B",1
* -------------------------
       DATA 62,2              ; HP 75 specific (LEX #instead of NAM)
* -------------------------
       DEF RUNTIM            ; tables
       DEF ASCIIS
       DEF PARSE 
       DEF ERRMSG
       DEF INTCPT           ; HP 75 specific (intercept function)
* -------------------------
PARSE  DATA 0,0
RUNTIM DATA 0,0              ; RUNTIM table
       DEF UNIT$ 
       DEF VLITE 
       DEF CHARGE
       DEF PLANCK
       DEF ELMASS
       DEF AVGDRO
       DEF MOLRGC
       DEF BOLTK 
       DEF GRAVK 
       DEF MOLVOL
       DEF FARADK
       DEF RYDBRK
       DEF FINSTK
       DEF ELRAD 
       DEF BOHRAD
       DEF MAGFLX
       DEF ATMASS
       DEF PRMASS
       DEF NTMASS
       DEF ELGK  
       DEF BOHRMG
       DEF NUCLMG
       DEF ELMAG 
       DEF PRMAG 
       DEF PRGYMR
       DEF GRACCL
       DATA 0FFH,0FFH
* -------------------------
ASCIIS DATA "UNIT$"
       DATA "VLITE"
       DATA "CHARGE"
       DATA "PLANCK"
       DATA "ELMASS"
       DATA "AVGDRO"
       DATA "MOLRGC"
       DATA "BOLTK"
       DATA "GRAVK"
       DATA "MOLVOL"
       DATA "FARADK"
       DATA "RYDBRK"
       DATA "FINSTK"
       DATA "ELRAD"
       DATA "BOHRAD"
       DATA "MAGFLX"
       DATA "ATMASS"
       DATA "PRMASS"
       DATA "NTMASS"
       DATA "ELGK"
       DATA "BOHRMG"
       DATA "NUCLMG"
       DATA "ELMAG"
       DATA "PRMAG"
       DATA "PRGYMR"
       DATA "GRACCL"
       DATA 0FFH             ; end of table
* -------------------------
ERRMSG DATA 0FFH
* -------------------------
       DATA 15               ; HP 75 specific (LEX attribute)
INTCPT RTN 
* -------------------------
* runtime functions start here
* -------------------------
       DATA 0,56             ; function, return a string
UNIT$  LDM R56,=2,0
       JSB =RSMEM-
       PUMD R56,+R12        ; length
       PUMD R26,+R12        ; address
       LDM R20,=123,111     ; 123,111 = 83 73 = "SI"
       PUMD R20,+R26        ; store
       RTN 
*
* table with up to 256 constants
* 8 bytes float format
*
TABLE  DATA 10,0,0,200,105,222,227,51 ; 0 VLITE
       DATA 201,220,0,0,222,30,2,26 ; 1 CHARGE
       DATA 146,220,0,0,140,27,46,146 ; 2 PLANCK
       DATA 151,220,0,0,100,123,11,221 ; 3 ELMASS
       DATA 43,0,0,0,120,4,42,0 ; 4 AVGDRO
       DATA 0,0,0,0,0,101,24,203 ; 5 MOLRGC
       DATA 167,220,0,0,40,146,200,23 ; 6 BOLTK
       DATA 211,220,0,0,0,0,162,146 ; 7 GRAVK
       DATA 230,220,0,0,30,70,101,42 ; 10 MOLVOL
       DATA 4,0,0,0,140,105,110,226 ; 11 FARADK
       DATA 7,0,0,167,61,67,227,20 ; 12 RYDBRK
       DATA 2,0,0,0,4,66,160,23 ; 13 FINSTK
       DATA 205,220,0,0,200,223,27,50 ; 14 ELRAD
       DATA 211,220,0,0,6,167,221,122 ; 15 BOHRAD
       DATA 205,220,0,0,6,205,147,40 ; 16 MAGFLX
       DATA 163,220,0,0,125,126,140,26 ; 17 ATMASS
       DATA 163,220,0,0,205,144,162,26 ; 20 PRMASS
       DATA 163,220,0,0,103,225,164,26 ; 21 NTMASS
       DATA 0,0,160,126,226,25,1,20 ; 22 ELGK
       DATA 166,220,0,0,200,7,164,222 ; 23 BOHRMG
       DATA 163,220,0,0,100,202,120,120 ; 24 NUCLMG
       DATA 166,220,0,0,40,203,204,222 ; 25 ELMAG
       DATA 164,220,0,0,161,141,20,24 ; 26 PRMAG
       DATA 10,0,0,0,207,31,165,46 ; 27 PRGYMR
       DATA 0,0,0,0,0,65C,06C,98C ; 30 GRACCL 9.81 m/s^2
* R36 = index 0,1,...,255
LOOKUP BIN 
*      DATA 336             ; DEBUG BREAKPOINT
* HP 75 specific (ROMPTR instead of BINTAB)
       LDMD R30,=ROMPTR    ; get load address to make...
       ADM R30,=TABLE      ; ... abs. address of TABLE
       CLB R37             ; zero out for R36-R37 shift
       ELM R36             ; * 2 (ELM shifts CY into R37)
       ELM R36             ; * 4 (LLM would drop CY)
       ELM R36             ; * 8
       ADM R30,R36         ; address of constant
       LDMD R40,R30        ; get and ...
       PUMD R40,+R12       ; push on R12 stack
       RTN 
* each constant takes
* length of its name
* + 7 bytes here
* + 8 bytes in table
* VLITE = 299792458 m/s
       DATA 0,55            ; function, return a float
VLITE  LDB R36,=0
       JMP LOOKUP
* CHARGE = 1.6021892E-19 coulombs (charge)
       DATA 0,55
CHARGE LDB R36,=1
       JMP LOOKUP
* PLANCK = 6.626176E-34
       DATA 0,55
PLANCK LDB R36,=2
       JMP LOOKUP
* ELMASS = 9.109534E-31 kg (electron mass)
       DATA 0,55
ELMASS LDB R36,=3
       JMP LOOKUP
* AVGDRO = 6.022045E23
       DATA 0,55
AVGDRO LDB R36,=4
       JMP LOOKUP
* MOLRGC = 8.31441
       DATA 0,55
MOLRGC LDB R36,=5
       JMP LOOKUP
* BOLTK = 1.380662E-23
       DATA 0,55
BOLTK  LDB R36,=6
       JMP LOOKUP
* GRAVK = 6.672E-11 m^3/s^2/kg (universal gravity constant)
       DATA 0,55
GRAVK  LDB R36,=7
       JMP LOOKUP
* MOLVOL = 0.022413818
       DATA 0,55
MOLVOL LDB R36,=10
       JMP LOOKUP
* FARADK = 96484.56
       DATA 0,55
FARADK LDB R36,=11
       JMP LOOKUP
* RYDBRK = 10973731.77
       DATA 0,55
RYDBRK LDB R36,=12
       JMP LOOKUP
* FINSTK = 137.03604
       DATA 0,55
FINSTK LDB R36,=13
       JMP LOOKUP
* ELRAD = 2.817938E-15
       DATA 0,55
ELRAD  LDB R36,=14
       JMP LOOKUP
* BOHRAD = 5.2917706E-11
       DATA 0,55
BOHRAD LDB R36,=15
LOOK_1 JMP LOOKUP          ; trampoline
* MAGFLX = 2.0678506E-15
       DATA 0,55
MAGFLX LDB R36,=16
       JMP LOOK_1
* ATMASS = 1.6605655E-27
       DATA 0,55
ATMASS LDB R36,=17
       JMP LOOK_1
* PRMASS = 1.6726485E-27
       DATA 0,55
PRMASS LDB R36,=20
       JMP LOOK_1
* NTMASS = 1.6749543E-27
       DATA 0,55
NTMASS LDB R36,=21
       JMP LOOK_1
* ELGK = 1.0011596567
       DATA 0,55
ELGK   LDB R36,=22
       JMP LOOK_1
* BOHRMG = 9.274078E-24
       DATA 0,55
BOHRMG LDB R36,=23
       JMP LOOK_1
* NUCLMG = 5.050824E-27
       DATA 0,55
NUCLMG LDB R36,=24
       JMP LOOK_1
* ELMAG = 9.284832E-24
       DATA 0,55
ELMAG  LDB R36,=25
       JMP LOOK_1
* PRMAG = 1.4106171E-26
       DATA 0,55
PRMAG  LDB R36,=26
       JMP LOOK_1
* PRGYMR = 267519870
       DATA 0,55
PRGYMR LDB R36,=27
       JMP LOOK_1
* gravity acceleration GRACCEL = 9.80665 m/s^2
       DATA 0,55
GRACCL LDB R36,=30
       JMP LOOK_1
       END
