#include <stdio.h>
#include <string.h>
#include <stdbool.h>



void generateVariables(bool* arr){
	arr[325]  = arr[163] ^ arr[301];
	arr[326]  = arr[164] ^ arr[302];
	arr[327]  = arr[165] ^ arr[303];
	arr[328]  = arr[166] ^ arr[304];
	arr[329]  = arr[167] ^ arr[305];
	arr[330]  = arr[168] ^ arr[306];
	arr[331]  = arr[169] ^ arr[307];
	arr[332]  = arr[170] ^ arr[308];
	arr[333]  = arr[171] ^ arr[309];
	arr[334]  = arr[172] ^ arr[310];
	arr[335]  = arr[173] ^ arr[311];
	arr[336]  = arr[174] ^ arr[312];
	arr[337]  = arr[175] ^ arr[313];
	arr[338]  = arr[176] ^ arr[314];
	arr[339]  = arr[177] ^ arr[315];
	arr[340]  = arr[178] ^ arr[316];
	arr[341]  = arr[179] ^ arr[317];
	arr[342]  = arr[180] ^ arr[318];
	arr[343]  = arr[181] ^ arr[319];
	arr[344]  = arr[182] ^ arr[320];
	arr[345]  = arr[183] ^ arr[321];
	arr[346]  = arr[184] ^ arr[322];
	arr[347]  = arr[185] ^ arr[323];
	arr[348]  = arr[186] ^ arr[324];
	arr[349]  = arr[187] ^ arr[304];
	arr[350]  = arr[188] ^ arr[305];
	arr[351]  = arr[189] ^ arr[306];
	arr[352]  = arr[190] ^ arr[307];
	arr[353]  = arr[191] ^ arr[308];
	arr[354]  = arr[192] ^ arr[309];
	arr[355]  = arr[193] ^ arr[310];
	arr[356]  = arr[194] ^ arr[311];
	arr[357]  = arr[195] ^ arr[312];
	arr[358]  = arr[196] ^ arr[313];
	arr[359]  = arr[197] ^ arr[314];
	arr[360]  = arr[198] ^ arr[315];
	arr[361]  = arr[199] ^ arr[316];
	arr[362]  = arr[200] ^ arr[317];
	arr[363]  = arr[201] ^ arr[318];
	arr[364]  = arr[202] ^ arr[319];
	arr[365]  = arr[203] ^ arr[320];
	arr[366]  = arr[204] ^ arr[321];
	arr[367]  = arr[205] ^ arr[322];
	arr[368]  = arr[206] ^ arr[323];
	arr[369]  = arr[207] ^ arr[324];
	arr[370]  = arr[280] ^ arr[325];
	arr[371]  = arr[281] ^ arr[326];
	arr[372]  = arr[282] ^ arr[327];
	arr[373]  = arr[283] ^ arr[328];
	arr[374]  = arr[284] ^ arr[329];
	arr[375]  = arr[285] ^ arr[330];
	arr[376]  = arr[286] ^ arr[331];
	arr[377]  = arr[287] ^ arr[332];
	arr[378]  = arr[288] ^ arr[333];
	arr[379]  = arr[289] ^ arr[334];
	arr[380]  = arr[290] ^ arr[335];
	arr[381]  = arr[291] ^ arr[336];
	arr[382]  = arr[292] ^ arr[337];
	arr[383]  = arr[293] ^ arr[338];
	arr[384]  = arr[294] ^ arr[339];
	arr[385]  = arr[295] ^ arr[340];
	arr[386]  = arr[296] ^ arr[341];
	arr[387]  = arr[297] ^ arr[342];
	arr[388]  = arr[298] ^ arr[343];
	arr[389]  = arr[299] ^ arr[344];
	arr[390]  = arr[300] ^ arr[345];
	arr[391]  = arr[301] ^ arr[346];
	arr[392]  = arr[302] ^ arr[347];
	arr[393]  = arr[303] ^ arr[348];
	arr[394]  = arr[208] ^ arr[254];
	arr[395]  = arr[255] ^ arr[370];
	arr[396]  = arr[256] ^ arr[371];
	arr[397]  = arr[257] ^ arr[372];
	arr[398]  = arr[258] ^ arr[373];
	arr[399]  = arr[259] ^ arr[374];
	arr[400]  = arr[260] ^ arr[375];
	arr[401]  = arr[261] ^ arr[376];
	arr[402]  = arr[262] ^ arr[377];
	arr[403]  = arr[263] ^ arr[378];
	arr[404]  = arr[264] ^ arr[379];
	arr[405]  = arr[265] ^ arr[380];
	arr[406]  = arr[266] ^ arr[381];
	arr[407]  = arr[267] ^ arr[382];
	arr[308]  = arr[268] ^ arr[383];
	arr[409]  = arr[269] ^ arr[384];
	arr[410]  = arr[270] ^ arr[385];
	arr[411]  = arr[271] ^ arr[386];
	arr[412]  = arr[272] ^ arr[387];
	arr[413]  = arr[273] ^ arr[388];
	arr[414]  = arr[274] ^ arr[389];
	arr[415]  = arr[275] ^ arr[390];
	arr[416]  = arr[276] ^ arr[391];
	arr[417]  = arr[277] ^ arr[392];
	arr[418]  = arr[278] ^ arr[393];
	arr[419]  = arr[279] ^ arr[349];
	
}

void reduction(bool* arr){
	arr[162] = arr[162] ^ arr[208] ^ arr[279] ^ arr[300];
	arr[161] = arr[161] ^ arr[369] ^ arr[278] ^ arr[299];
	arr[160] = arr[160] ^ arr[368] ^ arr[277] ^ arr[298]; 
	arr[159] = arr[159] ^ arr[367] ^ arr[276] ^ arr[297];
	arr[158] = arr[158] ^ arr[366] ^ arr[275] ^ arr[296];
	arr[157] = arr[157] ^ arr[365] ^ arr[274] ^ arr[295]; 
	arr[156] = arr[156] ^ arr[364] ^ arr[273] ^ arr[294];
	arr[155] = arr[155] ^ arr[363] ^ arr[272] ^ arr[293];
	arr[154] = arr[154] ^ arr[362] ^ arr[271] ^ arr[292]; 
	arr[153] = arr[153] ^ arr[361] ^ arr[270] ^ arr[291];
	arr[152] = arr[152] ^ arr[360] ^ arr[269] ^ arr[290];
	arr[151] = arr[151] ^ arr[359] ^ arr[268] ^ arr[289]; 
	arr[150] = arr[150] ^ arr[358] ^ arr[267] ^ arr[288];
	arr[149] = arr[149] ^ arr[357] ^ arr[266] ^ arr[287];
	arr[148] = arr[148] ^ arr[356] ^ arr[265] ^ arr[286]; 
	arr[147] = arr[147] ^ arr[355] ^ arr[264] ^ arr[285];
	arr[146] = arr[146] ^ arr[354] ^ arr[263] ^ arr[284];
	arr[145] = arr[145] ^ arr[353] ^ arr[262] ^ arr[283]; 
	arr[144] = arr[144] ^ arr[352] ^ arr[261] ^ arr[282];
	arr[143] = arr[143] ^ arr[351] ^ arr[260] ^ arr[281];
	arr[142] = arr[142] ^ arr[350] ^ arr[259] ^ arr[280]; 
	arr[141] = arr[141] ^ arr[258] ^ arr[419];
	arr[140] = arr[140] ^ arr[257] ^ arr[418];
	arr[139] = arr[139] ^ arr[256] ^ arr[417]; 
	arr[138] = arr[138] ^ arr[255] ^ arr[416];
	arr[137] = arr[137] ^ arr[254] ^ arr[415];
	arr[136] = arr[136] ^ arr[253] ^ arr[414]; 
	arr[135] = arr[135] ^ arr[252] ^ arr[413];
	arr[134] = arr[134] ^ arr[251] ^ arr[412];
	arr[133] = arr[133] ^ arr[250] ^ arr[411]; 
	arr[132] = arr[132] ^ arr[249] ^ arr[410];
	arr[131] = arr[131] ^ arr[248] ^ arr[409];
	arr[130] = arr[130] ^ arr[247] ^ arr[408]; 
	arr[129] = arr[129] ^ arr[246] ^ arr[407];
	arr[128] = arr[128] ^ arr[245] ^ arr[406];
	arr[127] = arr[127] ^ arr[244] ^ arr[405]; 
	arr[126] = arr[126] ^ arr[243] ^ arr[404];
	arr[125] = arr[125] ^ arr[242] ^ arr[403];
	arr[124] = arr[124] ^ arr[241] ^ arr[402];
	arr[123] = arr[123] ^ arr[240] ^ arr[401];
	arr[122] = arr[122] ^ arr[239] ^ arr[400];
	arr[121] = arr[121] ^ arr[238] ^ arr[399];
	arr[120] = arr[120] ^ arr[237] ^ arr[398];
	arr[119] = arr[119] ^ arr[236] ^ arr[397];
	arr[118] = arr[118] ^ arr[235] ^ arr[396];
	arr[117] = arr[117] ^ arr[234] ^ arr[395];
	arr[116] = arr[116] ^ arr[233] ^ arr[394];
	arr[115] = arr[115] ^ arr[207] ^ arr[232] ^ arr[253];
	arr[114] = arr[114] ^ arr[206] ^ arr[231] ^ arr[252];
	arr[113] = arr[113] ^ arr[205] ^ arr[230] ^ arr[251];
	arr[112] = arr[112] ^ arr[204] ^ arr[229] ^ arr[250];
	arr[111] = arr[111] ^ arr[203] ^ arr[228] ^ arr[249];
	arr[110] = arr[110] ^ arr[202] ^ arr[227] ^ arr[248];
	arr[109] = arr[109] ^ arr[201] ^ arr[226] ^ arr[247];
	arr[108] = arr[108] ^ arr[200] ^ arr[225] ^ arr[246];
	arr[107] = arr[107] ^ arr[199] ^ arr[224] ^ arr[245];
	arr[106] = arr[106] ^ arr[198] ^ arr[223] ^ arr[244];
	arr[105] = arr[105] ^ arr[197] ^ arr[222] ^ arr[243];
	arr[104] = arr[104] ^ arr[196] ^ arr[221] ^ arr[242];
	arr[103] = arr[103] ^ arr[195] ^ arr[220] ^ arr[241]; 
	arr[102] = arr[102] ^ arr[194] ^ arr[219] ^ arr[240];
	arr[101] = arr[101] ^ arr[193] ^ arr[218] ^ arr[239];
	arr[100] = arr[100] ^ arr[192] ^ arr[217] ^ arr[238];
	arr[99] = arr[99] ^ arr[191] ^ arr[216] ^ arr[237];
	arr[98] = arr[98] ^ arr[190] ^ arr[215] ^ arr[236];
	arr[97] = arr[97] ^ arr[189] ^ arr[214] ^ arr[235];
	arr[96] = arr[96] ^ arr[188] ^ arr[213] ^ arr[234];
	arr[95] = arr[95] ^ arr[187] ^ arr[212] ^ arr[233];
	arr[94] = arr[94] ^ arr[348] ^ arr[211] ^ arr[232];
	arr[93] = arr[93] ^ arr[347] ^ arr[210] ^ arr[231];
	arr[92] = arr[92] ^ arr[346] ^ arr[209] ^ arr[230];
	arr[91] = arr[91] ^ arr[345] ^ arr[208] ^ arr[229];
	arr[90] = arr[90] ^ arr[344] ^ arr[369] ^ arr[228];
	arr[89] = arr[89] ^ arr[343] ^ arr[368] ^ arr[227];
	arr[88] = arr[88] ^ arr[342] ^ arr[367] ^ arr[226];
	arr[87] = arr[87] ^ arr[341] ^ arr[366] ^ arr[225];
	arr[86] = arr[86] ^ arr[340] ^ arr[365] ^ arr[224];
	arr[85] = arr[85] ^ arr[339] ^ arr[364] ^ arr[223];
	arr[84] = arr[84] ^ arr[338] ^ arr[363] ^ arr[222];
	arr[83] = arr[83] ^ arr[337] ^ arr[362] ^ arr[221];
	arr[82] = arr[82] ^ arr[336] ^ arr[361] ^ arr[220];
	arr[81] = arr[81] ^ arr[335] ^ arr[360] ^ arr[219];
	arr[80] = arr[80] ^ arr[334] ^ arr[359] ^ arr[218];
	arr[79] = arr[79] ^ arr[333] ^ arr[358] ^ arr[217];
	arr[78] = arr[78] ^ arr[332] ^ arr[357] ^ arr[216];
	arr[77] = arr[77] ^ arr[331] ^ arr[356] ^ arr[215];
	arr[76] = arr[76] ^ arr[330] ^ arr[355] ^ arr[214];
	arr[75] = arr[75] ^ arr[329] ^ arr[354] ^ arr[213];
	arr[74] = arr[74] ^ arr[328] ^ arr[353] ^ arr[212];
	arr[73] = arr[73] ^ arr[327] ^ arr[352] ^ arr[211];
	arr[72] = arr[72] ^ arr[326] ^ arr[351] ^ arr[210];
	arr[71] = arr[71] ^ arr[325] ^ arr[350] ^ arr[209];
	arr[70] = arr[70] ^ arr[419];
	arr[69] = arr[69] ^ arr[418];
	arr[68] = arr[68] ^ arr[417];
	arr[67] = arr[67] ^ arr[416];
	arr[66] = arr[66] ^ arr[415];
	arr[65] = arr[65] ^ arr[414];
	arr[64] = arr[64] ^ arr[413];
	arr[63] = arr[63] ^ arr[412];
	arr[62] = arr[62] ^ arr[411];
	arr[61] = arr[61] ^ arr[410];
	arr[60] = arr[60] ^ arr[409];
	arr[59] = arr[59] ^ arr[408];
	arr[58] = arr[58] ^ arr[407];
	arr[57] = arr[57] ^ arr[406];
	arr[56] = arr[56] ^ arr[405];
	arr[55] = arr[55] ^ arr[404];
	arr[54] = arr[54] ^ arr[403];
	arr[53] = arr[53] ^ arr[402];
	arr[52] = arr[52] ^ arr[401];
	arr[51] = arr[51] ^ arr[400];
	arr[50] = arr[50] ^ arr[399];
	arr[49] = arr[49] ^ arr[398];
	arr[48] = arr[48] ^ arr[397];
	arr[47] = arr[47] ^ arr[396];
	arr[46] = arr[46] ^ arr[395];
	arr[45] = arr[45] ^ arr[394];
	arr[44] = arr[44] ^ arr[369] ^ arr[253];
	arr[43] = arr[43] ^ arr[368] ^ arr[252];
	arr[42] = arr[42] ^ arr[367] ^ arr[251];
	arr[41] = arr[41] ^ arr[366] ^ arr[250];
	arr[40] = arr[40] ^ arr[365] ^ arr[249];
	arr[39] = arr[39] ^ arr[364] ^ arr[248];
	arr[38] = arr[38] ^ arr[363] ^ arr[247];
	arr[37] = arr[37] ^ arr[362] ^ arr[246];
	arr[36] = arr[36] ^ arr[361] ^ arr[245];
	arr[35] = arr[35] ^ arr[360] ^ arr[244];
	arr[34] = arr[34] ^ arr[359] ^ arr[243];
	arr[33] = arr[33] ^ arr[358] ^ arr[242];
	arr[32] = arr[32] ^ arr[357] ^ arr[241];
	arr[31] = arr[31] ^ arr[356] ^ arr[240];
	arr[30] = arr[30] ^ arr[355] ^ arr[239];
	arr[29] = arr[29] ^ arr[354] ^ arr[238];
	arr[28] = arr[28] ^ arr[353] ^ arr[237];
	arr[27] = arr[27] ^ arr[352] ^ arr[236];
	arr[26] = arr[26] ^ arr[351] ^ arr[235];
	arr[25] = arr[25] ^ arr[350] ^ arr[234];
	arr[24] = arr[24] ^ arr[349] ^ arr[233];
	arr[23] = arr[23] ^ arr[232] ^ arr[393];
	arr[22] = arr[22] ^ arr[231] ^ arr[392];
	arr[21] = arr[21] ^ arr[230] ^ arr[391];
	arr[20] = arr[20] ^ arr[229] ^ arr[390];
	arr[19] = arr[19] ^ arr[228] ^ arr[389];
	arr[18] = arr[18] ^ arr[227] ^ arr[388];
	arr[17] = arr[17] ^ arr[226] ^ arr[387];
	arr[16] = arr[16] ^ arr[225] ^ arr[386];
	arr[15] = arr[15] ^ arr[224] ^ arr[385];
	arr[14] = arr[14] ^ arr[223] ^ arr[384];
	arr[13] = arr[13] ^ arr[222] ^ arr[383];
	arr[12] = arr[12] ^ arr[221] ^ arr[382];
	arr[11] = arr[11] ^ arr[220] ^ arr[381];
	arr[10] = arr[10] ^ arr[219] ^ arr[380];
	arr[9] = arr[9] ^ arr[218] ^ arr[379];
	arr[8] = arr[8] ^ arr[217] ^ arr[378];
	arr[7] = arr[7] ^ arr[216] ^ arr[377];
	arr[6] = arr[6] ^ arr[215] ^ arr[376];
	arr[5] = arr[5] ^ arr[214] ^ arr[375];
	arr[4] = arr[4] ^ arr[213] ^ arr[374];
	arr[3] = arr[3] ^ arr[212] ^ arr[373];
	arr[2] = arr[2] ^ arr[211] ^ arr[372];
	arr[1] = arr[1] ^ arr[210] ^ arr[371];
	arr[0] = arr[0] ^ arr[209] ^ arr[370];
	
	

}

int main( int argc, const char* argv[] )
{

	bool bits[419];
	int i;
	for (i = 0; i < 419; i++) {
	 	bits[i] = 0;
	}

	
	bits[322] = true;
	bits[323] = true;
	bits[324] = true;

	generateVariables(bits);
	
	reduction(bits);

	char greeting[600];
	for(i = 163; i > -1; i--){
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
