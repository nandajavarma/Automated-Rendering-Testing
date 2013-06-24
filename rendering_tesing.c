#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
  int i;
  char buffer[20];
  char original[1024] = {'\0'};
  char testing[1024] = {'\0'};
  FILE *op, *tp, *rp;
  if(argc != 3)
    {
      printf("Usage: ./rendering_testing orig_glyph.txt rendered_glyphs.txt\n");
      exit(0);
    }
  snprintf(original, 1024, "%s", argv[1]);
  snprintf(testing, 1024, "%s", argv[2]);
  op = fopen(original, "r");
  tp = fopen(testing, "r");
  rp = fopen("result.txt", "rw");
  for(i = 0; buffer[i] != '['; i++)
    {
      fread(&buffer[i], 1, 1, op);
    }
  for(i = 0; i != '/0'; i++)
    printf("%s", buffer[i]);
}
