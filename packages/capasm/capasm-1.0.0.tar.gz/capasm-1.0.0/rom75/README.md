HP-75 SYSTEM ROM source files (NCAS Assembler format)
=====================================================

Index
-----

* [Description](#description)
* [Origin](#orign)
* [Generate ROM Files](#generate-rom-files)


Description
-----------

This directory contains the source files for revision "d" of SYSROM,
BASROM, MELROM and ALTROM. The files can be assembled with the
NCAS assembler which is part of the CAPASM software suite.


Origin
------

The starting point of my work were the files which were partly disassembled and
documented by Everett Kaser. Using the HP-75 Internal ROM Rev D Source Listings
the disassembly was completed in the NCAS assembler format. This work was
done to have a comprehensive regression test for the NCAS assembler.

The binaries assembled with NCAS are identical to the HP-75 system ROMs. The only
exception are some conditional return pseudo-ops which jump to a previous instead
of a next return because the source of a ROM is now in a single source file.


ROM File Generation
-------------------

The ROM files are assembled with the following commands:

    ncas SYSROM.asm -l SYSROM.lis -g 75 -r 2
    ncas BASROM.asm -l BASROM.lis -g 75 -r 2
    ncas MELROM.asm -l MELROM.lis -g 75 -r 2
    ncas ALTROM.asm -l ALTROM.lis -g 75 -r 2

These commands generate the files *SYSROM.bin, BASROM.bin, MELROM.bin* and
*ALTROM.bin* and assembler listing files with a cross-reference symbol table.

The checksum.py Python script can be used to compute the checksums of the
binaries. See the documentation in the header of the program.
