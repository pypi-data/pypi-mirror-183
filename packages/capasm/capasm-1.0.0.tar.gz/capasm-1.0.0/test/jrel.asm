       HED "Test JREL"
BACK   BSZ  123D
       CMB  R2,=5
       JNZ  BACK
       JNZ  BACK
       JMP  FORW
       JMP  FORW
       BSZ 127D
FORW   RTN
       FIN
