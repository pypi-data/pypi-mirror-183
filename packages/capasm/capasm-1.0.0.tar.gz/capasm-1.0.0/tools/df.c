#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
int main(argc, argv)
int argc;
char **argv;
{
  int infile1;
  int infile2;
  unsigned char i1,i2;
  int ret,count;
  int diffs;
  size_t length;

  infile1=open(argv[1],O_RDONLY);
  infile2=open(argv[2],O_RDONLY);
  count=0;
  length=1;
  diffs=0;
  while (1) {
     ret=read(infile1,(void *) &i1,length);
     if (ret==0) break;
     ret=read(infile2,(void *) &i2,length);
     if (ret==0) break;
     count+=1;
     if (i1!=i2) {
        printf("Byte differ at pos %o %o %o\n",count,i1,i2);
        diffs+=1;
/*        break; */
     }
  }
  close(infile1);
  close(infile2);
  if(diffs > 0) {
     fprintf(stderr,"%d differences found\n",diffs);
     return(1);
   } else {
     return(0);
   }
}
