od -x -Ax --endian=big $1  > soll.hex
od -x -Ax --endian=big $2  > ist.hex
kompare soll.hex ist.hex &
