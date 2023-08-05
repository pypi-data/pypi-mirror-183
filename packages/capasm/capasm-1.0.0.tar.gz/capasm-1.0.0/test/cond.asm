       ABS
       ORG 6000H
       .IFDEF TEST1
       DATA "TEST1 IS SET"
         .IFDEF TEST2
         DATA "TEST2 IS SET"
         .ELSE 
         DATA "TEST2 IS NOT SET"
         .ENDIF
       .ELSE
         .SET TEST8
         .CLR TEST9
         .IFDEF TEST3
         DATA "TEST3 IS SET"
         .ELSE
         DATA "TEST3 IS NOT SET"
         .ENDIF
         .IFDEF TEST8
         DATA "TEST8 IS SET"
         .ENDIF
         .IFDEF TEST9
         DATA "TEST9 IS NOT SET"
         .ENDIF
         .IFNDEF TEST9
         DATA "TEST9 IS NOT SET"
         .ENDIF
       DATA "TEST1 IS NOT SET"
       .ENDIF
       .IFSET TEST2
       DATA "TEST2 IS SET"
       .ENDIF
       END
