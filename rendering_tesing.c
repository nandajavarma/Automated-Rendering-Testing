#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
  int i = 0, j, k, l, opsize, tpsize, m = 0, c = 0;
  FILE *op, *tp, *rp;
  if(argc != 3)
    {
      printf("Usage: ./rendering_testing orig_glyph.txt rendered_glyphs.txt\n");
      exit(0);
    }
  op = fopen(argv[1], "r");
  tp = fopen(argv[2], "r");
  rp = fopen("result.txt", "rw"); //file to store the results of matching
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
	      printf("%s\n", glyph);    

				//Getting corresponding glyph from the correct glyphs' file 	
				//TODO								
				char glyph0[20] = {}
				int n = 0;
				if(bufferop[m] == '['  || bufferop[m] == ',')
				{
					while(bufferop[m++] != ',' && bufferop[m] != ']')
						glyph0[n++] = bufferop[m];
				}


				//Comparing the glyphs
				//TODO

				//writing the results to a third new file
				//TODO
	    }	
	   	else i++;
   	}
    while(buffertp[i] != '[')
    	i++;
  }

	fclose(op);
	fclose(tp);
	fclose(rp);
}



      
		
