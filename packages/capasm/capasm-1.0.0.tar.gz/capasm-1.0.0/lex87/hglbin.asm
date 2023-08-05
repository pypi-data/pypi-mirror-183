1000 !*********************************************************************
1010 !*   This binary program implements a string function called HGL$    *
1020 !* which accepts one string parameter and returns that string with   *
1030 !* the most significant bit of each character set.                   *
1040 !*   This binary program is a translation of the UDL$ binary program *
1050 !* from the HP-85 Assembler Rom manual.                              *
1060 !*                                                                   *
1070 !*               (c) Hewlett-Packard Co. 1982                        *
1080 !*                                                                   *
1090 !* An example of how this function might be used is:                 *
1100 !*                                                                   *
1110 !*   100 INPUT A$                                                    *
1120 !*   110 DISP HGL$(A$)                                               *
1130 !*                                                                   *
1140 !*********************************************************************
1150          NAM 53,HGLBIN          ! SET UP THE PROGRAM CONTROL BLOCK
1160          DEF RUNTIM             ! PTR TO RUNTIME ADDRESS TABLE
1170          DEF ASCIIS             ! PTR TO KEYWORD TABLE
1180          DEF PARSE              ! PTR TO PARSE ADDRESS TABLE
1190          DEF ERMSG              ! PTR TO ERROR MESSAGE TABLE
1200          DEF INIT               ! PTR TO INIT ROUTINE
1210 !*********************************************************************
1220 PARSE    BSZ 0                  ! NO PARSE ROUTINES
1230 !*********************************************************************
1240 RUNTIM   BYT 0,0                ! DUMMY TOK# 0 RUNTIME ADDRESS
1250          DEF REV.               ! TOK# 1 RUNTIME ADDRESS
1260          DEF HGL$.              ! TOK# 2 RUNTIME ADDRESS
1270          BYT 377,377            ! TERMINATE RELOCATION
1280 !*********************************************************************
1290 ASCIIS   ASP "HGL$B"            ! KEYWORD #1
1300          ASP "HGL$"             ! KEYWORD #2
1310 ERMSG    BYT 377                ! TERMINATE ASCII TABLE & ERMSG TABLE
1320 !*********************************************************************
1330 INIT     RTN                    ! NO INITIALIZATION TO BE DONE
1340 !*********************************************************************
1350          BYT 30,56              ! ATTRIBUTES ($ FUNCTION, 1 $ PARAMETER)
1360 HGL$.    POMD R45,-R12          ! POP STRING ADDRESS OFF OF STACK
1370          POMD R30,-R12          ! GET LENGTH OF STRING OFF OF STACK
1380          STM R30,R55            ! LENGTH NEEDS TO BE IN 55 FOR 'RSMEM-'
1390          CLB R57                ! ZERO OUT MSB OF RESERVED LENGTH
1400          JSB =RSMEM-            ! GO GET SOME TEMPORARY MEMORY
1410          PUMD R30,+R12          ! PUSH LENGTH BACK ONTO THE R132 STACK
1420          PUMD R65,+R12          ! PUSH ADDRESS RETURNED BY RSMEM ON STACK
1430          BIN                    ! MAKE SURE OF MATH MODE FOR LOOP COUNTER
1440          LDMD R75,=PTR1-        ! SAVE VALUE OF PTR1
1450          PUMD R75,+R6           !    ON R6 STACK
1460          LDB R34,=200           ! SET UP MASK
1470          STMD R45,=PTR1-        ! ADDRESS OF 1st BYTE OF ORIGINAL STRING
1480          STMD R65,=PTR2-        ! ADDRESS OF 1st BYTE OF RESERVED MEMORY
1490 MORE     DCM R30                ! DECREMENT LOOP COUNTER
1500          JNC DONE               ! JIF NO CHARACTERS LEFT
1510          LDBI R20,=PTR1-        ! GET NEXT CHARACTER FROM ORIGINAL STRING
1520          ORB R20,R34            ! SET MSB OF CURRENT CHARACTER
1530          STBI R20,=PTR2-        ! STORE HI-LIGHTED BYTE TO RESERVED MEMORY
1540          JMP MORE               ! GO GET SOME MORE
1550 DONE     POMD R75,-R6           ! RETRIEVE OLD VALUE OF PTR1
1560          STMD R75,=PTR1-        !   AND RESTORE IT BEFORE RETURNING
1570          RTN                    ! DONE
1580 !*********************************************************************
1590          BYT 0,56               ! NO PARAMETERS, STRING FUNCTION
1600 REV.     BIN                    ! FOR ADDRESS MATH
1610          LDM R43,=40D,0         ! LOAD THE LENGTH OF THE STRING
1620          DEF DATE-              !    AND THE ADDRESS OF THE STRING
1630          BYT 0                  !         (MAKE IT A THREE BYTE ADDRESS)
1640          ADMD R45,=BINTAB       ! MAKE THE ADDRESS ABSOLUTE
1650          PUMD R43,+R12          ! PUSH IT TO THE OPERATING STACK
1660          RTN                    ! DONE
1670 DATE     ASC "40.102:veR  2891 .oC drakcaP-ttelweH )C("
1680 DATE-    BSZ 0                  ! PLACE HOLDER FOR ADDRESS LOAD
1690 !*********************************************************************
1700 BINTAB   DAD 104070             !
1710 RSMEM-   DAD 31741              !
1720 PTR1-    DAD 177711             ! DEFINE ADDRESSES
1730 PTR2-    DAD 177715             !
1740          FIN                    ! TERMINATE ASSEMBLY
