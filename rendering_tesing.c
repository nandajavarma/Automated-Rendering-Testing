#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
  int i = 0, j = 0, k = 0, m =0, n=0, l =0, opsize, tpsize;
  char word[20][20], glyph[20][20];
  FILE *op, *tp, *rp;
  if(argc != 3)
    {
      printf("Usage: ./rendering_testing orig_glyph.txt rendered_glyphs.txt\n");
      exit(0);
    }
  op = fopen(argv[1], "r");
  tp = fopen(argv[2], "r");
  rp = fopen("result.txt", "rw");
  fseek(op, 0, SEEK_END); // seek to end of file
  opsize = ftell(op); // get current file pointer
  fseek(op, 0, SEEK_SET); // seek back to beginning of file
  fseek(tp, 0, SEEK_END); // seek to end of file
  tpsize = ftell(tp); // get current file pointer
  fseek(tp, 0, SEEK_SET); // seek back to beginning of file
  char bufferop[opsize], buffertp[tpsize];
  fread(bufferop, opsize, 1, op);
  fread(buffertp, tpsize, 1, tp);
}
