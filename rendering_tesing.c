//Automated rendering testing

#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
  int i = 0, j, k, l, opsize, tpsize, m = 0, c = 0, n;
  FILE *op, *tp, *rp;
  if(argc != 3)
    {
      printf("Usage: ./rendering_testing orig_glyph.txt rendered_glyphs.txt\n");
      exit(0);
    }
  op = fopen(argv[1], "r");
  tp = fopen(argv[2], "r");
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
         		printf("I couldn't open results.dat for writing.\n");
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
	fclose(op);
	fclose(tp);
	fclose(rp);
	return 0;
}



      
		
