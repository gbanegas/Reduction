#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main( int argc, const char* argv[] )
{

	bool bits[51];
	int i;
	for (i = 0; i < 51; i++) {
	 	bits[i] = 0;
	}

	bits[19] = true;
	bits[20] = true;
	bits[21] = true;
	its[22] = true;
	bits[23] = true;
	bits[24] = true;
	bits[25] = true;
	bits[26] = true;
	bits[27] = true;
	bits[28] = true;
	bits[29] = true;
	bits[30] = true;
	bits[31] = true;
	bits[32] = true;
	
	bits[37] = bits[19] ^ bits[31];
	bits[38] = bits[23] ^ bits[35];
	bits[39] = bits[34] ^ bits[36];
	bits[40] = bits[22] ^ bits[39];
	bits[41] = bits[21] ^ bits[33];
	bits[42] = bits[32] ^ bits[33];
	bits[43] = bits[35] ^ bits[41];
	bits[44] = bits[28] ^ bits[29];
	bits[45] = bits[20] ^ bits[34];
	bits[46] = bits[30] ^ bits[31];
	bits[47] = bits[37] ^ bits[42];
	bits[48] = bits[25] ^ bits[26];
	bits[49] = bits[27] ^ bits[32];
	bits[50] = bits[24] ^ bits[36];

	bits[0] = bits[0] ^ bits[47];
	bits[1] = bits[1] ^ bits[42] ^ bits[45];
	bits[2] = bits[2] ^ bits[34] ^ bits[43];
	bits[3] = bits[3] ^ bits[35] ^ bits[40];
	bits[4] = bits[4] ^ bits[36] ^ bits[38];
	bits[5] = bits[5] ^ bits[47] ^ bits[50];
	bits[6] = bits[6] ^ bits[25] ^ bits[37] ^ bits[45];
	bits[7] = bits[7] ^ bits[20] ^ bits[26] ^ bits[37] ^ bits[43];
	bits[8] = bits[8] ^ bits[20] ^ bits[21] ^ bits[40] ^ bits[49];
	bits[9] = bits[9] ^ bits[22] ^ bits[28] ^ bits[38] ^ bits[41];
	bits[10] = bits[10] ^ bits[23] ^ bits[24] ^ bits[29] ^ bits[40];
	bits[11] = bits[11] ^ bits[24] ^ bits[25] ^ bits[30] ^ bits[38];
	bits[12] = bits[12] ^ bits[31] ^ bits[48] ^ bits[50];
	bits[13] = bits[13] ^ bits[48] ^ bits[49];
	bits[14] = bits[14] ^ bits[26] ^ bits[27] ^ bits[28] ^ bits[33];
	bits[15] = bits[15] ^ bits[27] ^ bits[34] ^ bits[44];
	bits[16] = bits[16] ^ bits[30] ^ bits[35] ^ bits[44];
	bits[17] = bits[17] ^ bits[29] ^ bits[36] ^ bits[46];
	bits[18] = bits[18] ^ bits[32] ^ bits[46];
	
	char greeting[180];
	for(i = 18; i > -1; i--){
		if(bits[i]){
		char p[10];
         	sprintf(p, "+ x^%d ", i);
		strcat(greeting, p);
		}
	}
	strcat(greeting, "\n");
	
	printf( greeting );

	return 0;
}