10 ! --------------------------
20 ! FKEY$ LEX file for HP 75
30 ! Recreated with HP 85
40 ! Martin Hepperle, 2016
50 ! --------------------------
60 !      LST
70 ! --------------------------
80        BYT 306,256
90 ! -------------------------
100        DEF RUNTIM           ! the 5 addresses
110        DEF ASCII 
120        DEF PARSE 
130        DEF ERRMSG
140        DEF INTCPT
150 ! -------------------------
160 RUNTIM BYT 0,0              ! first addr is skipped
170        DEF FKEY$R
180 ! -------------------------
190 PARSE  BYT 0,0              ! first addr is skipped
200        DEF FKEY$P
210        BYT 377,377          ! RELMAR
220 ! -------------------------
230 ASCII  ASP "FKEY$"
240 ! -------------------------
250 ERRMSG BYT 377,377          ! first 377 ends KW table
260 !                            and is also first error #
270 !                            second 377 ends ERR table
280 ! -------------------------
290        BYT 101              ! rev. number "A" (optional)
300        BYT 27               ! 27 = 10111B
310 !                             code attribute bits
320 !                             0 RAMable
330 !                             1 ROMable
340 !                             2 position independent
350 !                            4 LEX# independent
360 INTCPT BSZ 0                ! no handling
370 ! -------------------------
380 FKEY$P RTN 
390 ! -------------------------
400        BYT 0,56
410 FKEY$R BIN 
420        CLM R56              ! anticipate no char
430        LDMD R46,=KEYSTS
440 !      LDB R46,=101
450        CMB R46,=177
460        JNC DONE  
470        ICM R56              ! one char
480 DONE   JSB =RSMEM-
490        PUMD R56,+R12
500        PUMD R26,+R12        ! address
510        TSB R56
520        JZR EXIT  
530        STBD R47,R26
540 EXIT   RTN 
550 ! -------------------------
560 KEYSTS DAD 177402
570 RSMEM- DAD 22037
580 ! -------------------------
590        FIN 
