#include<stdio.h>
#include<string.h>
main()
{
	int ch;
	int i = 0, j, k, l, opsize, tpsize, m = 0, c = 0, n;
	FILE *op, *tp, *rp;
	char rendfile[20], wordfile[20], reffile[20];
	printf("Welcome! Select the font for testing\n1.Meera\n2.Rachana\n3.Suruma\n4.Lohith-malayalam\n5.Something else\n");
	scanf("%d", &ch);
					switch(ch)
					{
						case 1: op = fopen("meera-glyph.txt", "r");
										tp = fopen("harfbuzz_Meera.ttf.txt","r");;
										break;
						case 2: op = fopen("rachana-glyph.txt", "r");
										tp = fopen("harfbuzz_Rachana.ttf.txt","r");;
										break;
						case 3: op = fopen("suruma-glyph.txt", "r");
										tp = fopen("harfbuzz_Suruma.ttf.txt", "r");;
										break;
						case 4: op = fopen("lohith-glyph.txt", "r");
										tp = fopen("harfbuzz_Lohith-Malayalam.ttf.txt", "r");;
										break;
						case 5: printf("\nEnter the name of the reference words file and its correcponding glyph names' file:");
										scanf("%s%s",wordfile,reffile);
										printf("Enter the name of the file containing the harfbuzz renderings:");
										scanf("%s",rendfile);
										op = fopen(reffile, "r");
										tp = fopen(rendfile, "r");;				
										break;
						default:printf("\nWell that was just wrong! Cya!\n");
										exit(0);
					}
	rp = fopen("result.txt", "w+"); //file to store the results of matching
  //getting the size of first file
  fseek(op, 0, SEEK_END); 
  opsize = ftell(op); 
  fseek(op, 0, SEEK_SET);
  //getting the size of second file
  fseek(tp, 0, SEEK_END); 
  tpsize = ftell(tp); 
  fseek(tp, 0, SEEK_SET); 
            
  char bufferop[opsize], buffertp[tpsize];    
  fread(bufferop, opsize, 1, op);
  fread(buffertp, tpsize, 1, tp);
 	printf("%s", bufferop);  
	printf("%s", buffertp);
  //Reading each glyph name one by one
  while(i <= tpsize- 1)
  {
    j = 0;
    c++; // To get the current word corresponding to the glyph,  this will be used
    while(buffertp[i] != ']')
    {
      char glyph[20] = {};
      if(buffertp[i] == '[' || buffertp[i] == '|')
      {
        k = 0;
        while(buffertp[++i] != '=')
        {
          glyph[k] = buffertp[i];
          k++;
        }
        //printf("%s\t", glyph);    

        //Getting corresponding glyph from the correct glyphs' file   
        char glyph0[20] = {};
        ++m;
        for(n = 0; bufferop[m] != ',' && bufferop[m] != ']'; n++)
          glyph0[n] = bufferop[m++];
        //printf("%s\n", glyph0);                                         
        if(bufferop[m] == ']')
        {
          while(bufferop[m] != '[')
            m++;
        }

        //Comparing the glyphs and writing the results to a third new file
        if(strcmp(glyph, glyph0) != 0)
        {
          if (rp == NULL)
          {
            printf("I couldn't open results file for writing.\n");
            exit(0);
          }
          fprintf(rp, "%d\n", c);
        }

      }
      else i++;
    }
    while(buffertp[i] != '[')
      i++;
  }
  fseek(rp, 0, SEEK_END);
  if(ftell(rp) == 0)
      printf("No rendering problems detected\n");
  else printf("Rendering problems were detected and are stored in result.txt file\n");
  fclose(op);
  fclose(tp);
  fclose(rp);
  return 0;
}
	
						 


