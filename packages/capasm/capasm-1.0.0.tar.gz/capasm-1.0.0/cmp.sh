od -x -Ax --endian=big cmp.bin  > soll.hex
od -x -Ax --endian=big result.bin  > ist.hex
kompare soll.hex ist.hex &
