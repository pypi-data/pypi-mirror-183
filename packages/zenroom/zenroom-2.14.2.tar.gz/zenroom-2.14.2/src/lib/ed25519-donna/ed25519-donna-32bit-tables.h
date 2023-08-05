static const ge25519 ALIGN(16) ge25519_basepoint = {
	{0x0325d51a,0x018b5823,0x00f6592a,0x0104a92d,0x01a4b31d,0x01d6dc5c,0x027118fe,0x007fd814,0x013cd6e5,0x0085a4db},
	{0x02666658,0x01999999,0x00cccccc,0x01333333,0x01999999,0x00666666,0x03333333,0x00cccccc,0x02666666,0x01999999},
	{0x00000001,0x00000000,0x00000000,0x00000000,0x00000000,0x00000000,0x00000000,0x00000000,0x00000000,0x00000000},
	{0x01b7dda3,0x01a2ace9,0x025eadbb,0x0003ba8a,0x0083c27e,0x00abe37d,0x01274732,0x00ccacdd,0x00fd78b7,0x019e1d7c}
};

/*
	d
*/

static const bignum25519 ALIGN(16) ge25519_ecd = {
	0x035978a3,0x00d37284,0x03156ebd,0x006a0a0e,0x0001c029,0x0179e898,0x03a03cbb,0x01ce7198,0x02e2b6ff,0x01480db3
};

static const bignum25519 ALIGN(16) ge25519_ec2d = {
	0x02b2f159,0x01a6e509,0x022add7a,0x00d4141d,0x00038052,0x00f3d130,0x03407977,0x019ce331,0x01c56dff,0x00901b67
};

/*
	sqrt(-1)
*/

static const bignum25519 ALIGN(16) ge25519_sqrtneg1 = {
	0x020ea0b0,0x0186c9d2,0x008f189d,0x0035697f,0x00bd0c60,0x01fbd7a7,0x02804c9e,0x01e16569,0x0004fc1d,0x00ae0c92
};

static const ge25519_niels ALIGN(16) ge25519_niels_sliding_multiples[32] = {
	{{0x0340913e,0x000e4175,0x03d673a2,0x002e8a05,0x03f4e67c,0x008f8a09,0x00c21a34,0x004cf4b8,0x01298f81,0x0113f4be},{0x018c3b85,0x0124f1bd,0x01c325f7,0x0037dc60,0x033e4cb7,0x003d42c2,0x01a44c32,0x014ca4e1,0x03a33d4b,0x001f3e74},{0x037aaa68,0x00448161,0x0093d579,0x011e6556,0x009b67a0,0x0143598c,0x01bee5ee,0x00b50b43,0x0289f0c6,0x01bc45ed}},
	{{0x00fcd265,0x0047fa29,0x034faacc,0x01ef2e0d,0x00ef4d4f,0x014bd6bd,0x00f98d10,0x014c5026,0x007555bd,0x00aae456},{0x00ee9730,0x016c2a13,0x017155e4,0x01874432,0x00096a10,0x01016732,0x01a8014f,0x011e9823,0x01b9a80f,0x01e85938},{0x01d0d889,0x01a4cfc3,0x034c4295,0x0110e1ae,0x0162508c,0x00f2db4c,0x0072a2c6,0x0098da2e,0x02f12b9b,0x0168a09a}},
	{{0x0047d6ba,0x0060b0e9,0x0136eff2,0x008a5939,0x03540053,0x0064a087,0x02788e5c,0x00be7c67,0x033eb1b5,0x005529f9},{0x00a5bb33,0x00af1102,0x01a05442,0x001e3af7,0x02354123,0x00bfec44,0x01f5862d,0x00dd7ba3,0x03146e20,0x00a51733},{0x012a8285,0x00f6fc60,0x023f9797,0x003e85ee,0x009c3820,0x01bda72d,0x01b3858d,0x00d35683,0x0296b3bb,0x010eaaf9}},
	{{0x023221b1,0x01cb26aa,0x0074f74d,0x0099ddd1,0x01b28085,0x00192c3a,0x013b27c9,0x00fc13bd,0x01d2e531,0x0075bb75},{0x004ea3bf,0x00973425,0x001a4d63,0x01d59cee,0x01d1c0d4,0x00542e49,0x01294114,0x004fce36,0x029283c9,0x01186fa9},{0x01b8b3a2,0x00db7200,0x00935e30,0x003829f5,0x02cc0d7d,0x0077adf3,0x0220dd2c,0x0014ea53,0x01c6a0f9,0x01ea7eec}},
	{{0x039d8064,0x01885f80,0x00337e6d,0x01b7a902,0x02628206,0x015eb044,0x01e30473,0x0191f2d9,0x011fadc9,0x01270169},{0x02a8632f,0x0199e2a9,0x00d8b365,0x017a8de2,0x02994279,0x0086f5b5,0x0119e4e3,0x01eb39d6,0x0338add7,0x00d2e7b4},{0x0045af1b,0x013a2fe4,0x0245e0d6,0x014538ce,0x038bfe0f,0x01d4cf16,0x037e14c9,0x0160d55e,0x0021b008,0x01cf05c8}},
	{{0x01864348,0x01d6c092,0x0070262b,0x014bb844,0x00fb5acd,0x008deb95,0x003aaab5,0x00eff474,0x00029d5c,0x0062ad66},{0x02802ade,0x01c02122,0x01c4e5f7,0x00781181,0x039767fb,0x01703406,0x0342388b,0x01f5e227,0x022546d8,0x0109d6ab},{0x016089e9,0x00cb317f,0x00949b05,0x01099417,0x000c7ad2,0x011a8622,0x0088ccda,0x01290886,0x022b53df,0x00f71954}},
	{{0x027fbf93,0x01c04ecc,0x01ed6a0d,0x004cdbbb,0x02bbf3af,0x00ad5968,0x01591955,0x0094f3a2,0x02d17602,0x00099e20},{0x02007f6d,0x003088a8,0x03db77ee,0x00d5ade6,0x02fe12ce,0x0107ba07,0x0107097d,0x00482a6f,0x02ec346f,0x008d3f5f},{0x032ea378,0x0028465c,0x028e2a6c,0x018efc6e,0x0090df9a,0x01a7e533,0x039bfc48,0x010c745d,0x03daa097,0x0125ee9b}},
	{{0x028ccf0b,0x00f36191,0x021ac081,0x012154c8,0x034e0a6e,0x01b25192,0x00180403,0x01d7eea1,0x00218d05,0x010ed735},{0x03cfeaa0,0x01b300c4,0x008da499,0x0068c4e1,0x0219230a,0x01f2d4d0,0x02defd60,0x00e565b7,0x017f12de,0x018788a4},{0x03d0b516,0x009d8be6,0x03ddcbb3,0x0071b9fe,0x03ace2bd,0x01d64270,0x032d3ec9,0x01084065,0x0210ae4d,0x01447584}},
	{{0x0020de87,0x00e19211,0x01b68102,0x00b5ac97,0x022873c0,0x01942d25,0x01271394,0x0102073f,0x02fe2482,0x01c69ff9},{0x010e9d81,0x019dbbe5,0x0089f258,0x006e06b8,0x02951883,0x018f1248,0x019b3237,0x00bc7553,0x024ddb85,0x01b4c964},{0x01c8c854,0x0060ae29,0x01406d8e,0x01cff2f9,0x00cff451,0x01778d0c,0x03ac8c41,0x01552e59,0x036559ee,0x011d1b12}},
	{{0x00741147,0x0151b219,0x01092690,0x00e877e6,0x01f4d6bb,0x0072a332,0x01cd3b03,0x00dadff2,0x0097db5e,0x0086598d},{0x01c69a2b,0x01decf1b,0x02c2fa6e,0x013b7c4f,0x037beac8,0x013a16b5,0x028e7bda,0x01f6e8ac,0x01e34fe9,0x01726947},{0x01f10e67,0x003c73de,0x022b7ea2,0x010f32c2,0x03ff776a,0x00142277,0x01d38b88,0x00776138,0x03c60822,0x01201140}},
	{{0x0236d175,0x0008748e,0x03c6476d,0x013f4cdc,0x02eed02a,0x00838a47,0x032e7210,0x018bcbb3,0x00858de4,0x01dc7826},{0x00a37fc7,0x0127b40b,0x01957884,0x011d30ad,0x02816683,0x016e0e23,0x00b76be4,0x012db115,0x02516506,0x0154ce62},{0x00451edf,0x00bd749e,0x03997342,0x01cc2c4c,0x00eb6975,0x01a59508,0x03a516cf,0x00c228ef,0x0168ff5a,0x01697b47}},
	{{0x00527359,0x01783156,0x03afd75c,0x00ce56dc,0x00e4b970,0x001cabe9,0x029e0f6d,0x0188850c,0x0135fefd,0x00066d80},{0x02150e83,0x01448abf,0x02bb0232,0x012bf259,0x033c8268,0x00711e20,0x03fc148f,0x005e0e70,0x017d8bf9,0x0112b2e2},{0x02134b83,0x001a0517,0x0182c3cc,0x00792182,0x0313d799,0x001a3ed7,0x0344547e,0x01f24a0d,0x03de6ad2,0x00543127}},
	{{0x00dca868,0x00618f27,0x015a1709,0x00ddc38a,0x0320fd13,0x0036168d,0x0371ab06,0x01783fc7,0x0391e05f,0x01e29b5d},{0x01471138,0x00fca542,0x00ca31cf,0x01ca7bad,0x0175bfbc,0x01a708ad,0x03bce212,0x01244215,0x0075bb99,0x01acad68},{0x03a0b976,0x01dc12d1,0x011aab17,0x00aba0ba,0x029806cd,0x0142f590,0x018fd8ea,0x01a01545,0x03c4ad55,0x01c971ff}},
	{{0x00d098c0,0x000afdc7,0x006cd230,0x01276af3,0x03f905b2,0x0102994c,0x002eb8a4,0x015cfbeb,0x025f855f,0x01335518},{0x01cf99b2,0x0099c574,0x01a69c88,0x00881510,0x01cd4b54,0x0112109f,0x008abdc5,0x0074647a,0x0277cb1f,0x01e53324},{0x02ac5053,0x01b109b0,0x024b095e,0x016997b3,0x02f26bb6,0x00311021,0x00197885,0x01d0a55a,0x03b6fcc8,0x01c020d5}},
	{{0x02584a34,0x00e7eee0,0x03257a03,0x011e95a3,0x011ead91,0x00536202,0x00b1ce24,0x008516c6,0x03669d6d,0x004ea4a8},{0x00773f01,0x0019c9ce,0x019f6171,0x01d4afde,0x02e33323,0x01ad29b6,0x02ead1dc,0x01ed51a5,0x01851ad0,0x001bbdfa},{0x00577de5,0x00ddc730,0x038b9952,0x00f281ae,0x01d50390,0x0002e071,0x000780ec,0x010d448d,0x01f8a2af,0x00f0a5b7}},
	{{0x031f2541,0x00d34bae,0x0323ff9d,0x003a056d,0x02e25443,0x00a1ad05,0x00d1bee8,0x002f7f8e,0x03007477,0x002a24b1},{0x0114a713,0x01457e76,0x032255d5,0x01cc647f,0x02a4bdef,0x0153d730,0x00118bcf,0x00f755ff,0x013490c7,0x01ea674e},{0x02bda3e8,0x00bb490d,0x00f291ea,0x000abf40,0x01dea321,0x002f9ce0,0x00b2b193,0x00fa54b5,0x0128302f,0x00a19d8b}},
	{{0x022ef5bd,0x01638af3,0x038c6f8a,0x01a33a3d,0x039261b2,0x01bb89b8,0x010bcf9d,0x00cf42a9,0x023d6f17,0x01da1bca},{0x00e35b25,0x000d824f,0x0152e9cf,0x00ed935d,0x020b8460,0x01c7b83f,0x00c969e5,0x01a74198,0x0046a9d9,0x00cbc768},{0x01597c6a,0x0144a99b,0x00a57551,0x0018269c,0x023c464c,0x0009b022,0x00ee39e1,0x0114c7f2,0x038a9ad2,0x01584c17}},
	{{0x03b0c0d5,0x00b30a39,0x038a6ce4,0x01ded83a,0x01c277a6,0x01010a61,0x0346d3eb,0x018d995e,0x02f2c57c,0x000c286b},{0x0092aed1,0x0125e37b,0x027ca201,0x001a6b6b,0x03290f55,0x0047ba48,0x018d916c,0x01a59062,0x013e35d4,0x0002abb1},{0x003ad2aa,0x007ddcc0,0x00c10f76,0x0001590b,0x002cfca6,0x000ed23e,0x00ee4329,0x00900f04,0x01c24065,0x0082fa70}},
	{{0x02025e60,0x003912b8,0x0327041c,0x017e5ee5,0x02c0ecec,0x015a0d1c,0x02b1ce7c,0x0062220b,0x0145067e,0x01a5d931},{0x009673a6,0x00e1f609,0x00927c2a,0x016faa37,0x01650ef0,0x016f63b5,0x03cd40e1,0x003bc38f,0x0361f0ac,0x01d42acc},{0x02f81037,0x008ca0e8,0x017e23d1,0x011debfe,0x01bcbb68,0x002e2563,0x03e8add6,0x000816e5,0x03fb7075,0x0153e5ac}},
	{{0x02b11ecd,0x016bf185,0x008f22ef,0x00e7d2bb,0x0225d92e,0x00ece785,0x00508873,0x017e16f5,0x01fbe85d,0x01e39a0e},{0x01669279,0x017c810a,0x024941f5,0x0023ebeb,0x00eb7688,0x005760f1,0x02ca4146,0x0073cde7,0x0052bb75,0x00f5ffa7},{0x03b8856b,0x00cb7dcd,0x02f14e06,0x001820d0,0x01d74175,0x00e59e22,0x03fba550,0x00484641,0x03350088,0x01c3c9a3}},
	{{0x00dcf355,0x0104481c,0x0022e464,0x01f73fe7,0x00e03325,0x0152b698,0x02ef769a,0x00973663,0x00039b8c,0x0101395b},{0x01805f47,0x019160ec,0x03832cd0,0x008b06eb,0x03d4d717,0x004cb006,0x03a75b8f,0x013b3d30,0x01cfad88,0x01f034d1},{0x0078338a,0x01c7d2e3,0x02bc2b23,0x018b3f05,0x0280d9aa,0x005f3d44,0x0220a95a,0x00eeeb97,0x0362aaec,0x00835d51}},
	{{0x01b9f543,0x013fac4d,0x02ad93ae,0x018ef464,0x0212cdf7,0x01138ba9,0x011583ab,0x019c3d26,0x028790b4,0x00e2e2b6},{0x033bb758,0x01f0dbf1,0x03734bd1,0x0129b1e5,0x02b3950e,0x003bc922,0x01a53ec8,0x018c5532,0x006f3cee,0x00ae3c79},{0x0351f95d,0x0012a737,0x03d596b8,0x017658fe,0x00ace54a,0x008b66da,0x0036c599,0x012a63a2,0x032ceba1,0x00126bac}},
	{{0x03dcfe7e,0x019f4f18,0x01c81aee,0x0044bc2b,0x00827165,0x014f7c13,0x03b430f0,0x00bf96cc,0x020c8d62,0x01471997},{0x01fc7931,0x001f42dd,0x00ba754a,0x005bd339,0x003fbe49,0x016b3930,0x012a159c,0x009f83b0,0x03530f67,0x01e57b85},{0x02ecbd81,0x0096c294,0x01fce4a9,0x017701a5,0x0175047d,0x00ee4a31,0x012686e5,0x008efcd4,0x0349dc54,0x01b3466f}},
	{{0x02179ca3,0x01d86414,0x03f0afd0,0x00305964,0x015c7428,0x0099711e,0x015d5442,0x00c71014,0x01b40b2e,0x01d483cf},{0x01afc386,0x01984859,0x036203ff,0x0045c6a8,0x0020a8aa,0x00990baa,0x03313f10,0x007ceede,0x027429e4,0x017806ce},{0x039357a1,0x0142f8f4,0x0294a7b6,0x00eaccf4,0x0259edb3,0x01311e6e,0x004d326f,0x0130c346,0x01ccef3c,0x01c424b2}},
	{{0x0364918c,0x00148fc0,0x01638a7b,0x01a1fd5b,0x028ad013,0x0081e5a4,0x01a54f33,0x0174e101,0x003d0257,0x003a856c},{0x00051dcf,0x00f62b1d,0x0143d0ad,0x0042adbd,0x000fda90,0x01743ceb,0x0173e5e4,0x017bc749,0x03b7137a,0x0105ce96},{0x00f9218a,0x015b8c7c,0x00e102f8,0x0158d7e2,0x0169a5b8,0x00b2f176,0x018b347a,0x014cfef2,0x0214a4e3,0x017f1595}},
	{{0x006d7ae5,0x0195c371,0x0391e26d,0x0062a7c6,0x003f42ab,0x010dad86,0x024f8198,0x01542b2a,0x0014c454,0x0189c471},{0x0390988e,0x00b8799d,0x02e44912,0x0078e2e6,0x00075654,0x01923eed,0x0040cd72,0x00a37c76,0x0009d466,0x00c8531d},{0x02651770,0x00609d01,0x0286c265,0x0134513c,0x00ee9281,0x005d223c,0x035c760c,0x00679b36,0x0073ecb8,0x016faa50}},
	{{0x02c89be4,0x016fc244,0x02f38c83,0x018beb72,0x02b3ce2c,0x0097b065,0x034f017b,0x01dd957f,0x00148f61,0x00eab357},{0x0343d2f8,0x003398fc,0x011e368e,0x00782a1f,0x00019eea,0x00117b6f,0x0128d0d1,0x01a5e6bb,0x01944f1b,0x012b41e1},{0x03318301,0x018ecd30,0x0104d0b1,0x0038398b,0x03726701,0x019da88c,0x002d9769,0x00a7a681,0x031d9028,0x00ebfc32}},
	{{0x0220405e,0x0171face,0x02d930f8,0x017f6d6a,0x023b8c47,0x0129d5f9,0x02972456,0x00a3a524,0x006f4cd2,0x004439fa},{0x00c53505,0x0190c2fd,0x00507244,0x009930f9,0x01a39270,0x01d327c6,0x0399bc47,0x01cfe13d,0x0332bd99,0x00b33e7d},{0x0203f5e4,0x003627b5,0x00018af8,0x01478581,0x004a2218,0x002e3bb7,0x039384d0,0x0146ea62,0x020b9693,0x0017155f}},
	{{0x03c97e6f,0x00738c47,0x03b5db1f,0x01808fcf,0x01e8fc98,0x01ed25dd,0x01bf5045,0x00eb5c2b,0x0178fe98,0x01b85530},{0x01c20eb0,0x01aeec22,0x030b9eee,0x01b7d07e,0x0187e16f,0x014421fb,0x009fa731,0x0040b6d7,0x00841861,0x00a27fbc},{0x02d69abf,0x0058cdbf,0x0129f9ec,0x013c19ae,0x026c5b93,0x013a7fe7,0x004bb2ba,0x0063226f,0x002a95ca,0x01abefd9}},
	{{0x02f5d2c1,0x00378318,0x03734fb5,0x01258073,0x0263f0f6,0x01ad70e0,0x01b56d06,0x01188fbd,0x011b9503,0x0036d2e1},{0x0113a8cc,0x01541c3e,0x02ac2bbc,0x01d95867,0x01f47459,0x00ead489,0x00ab5b48,0x01db3b45,0x00edb801,0x004b024f},{0x00b8190f,0x011fe4c2,0x00621f82,0x010508d7,0x001a5a76,0x00c7d7fd,0x03aab96d,0x019cd9dc,0x019c6635,0x00ceaa1e}},
	{{0x01085cf2,0x01fd47af,0x03e3f5e1,0x004b3e99,0x01e3d46a,0x0060033c,0x015ff0a8,0x0150cdd8,0x029e8e21,0x008cf1bc},{0x00156cb1,0x003d623f,0x01a4f069,0x00d8d053,0x01b68aea,0x01ca5ab6,0x0316ae43,0x0134dc44,0x001c8d58,0x0084b343},{0x0318c781,0x0135441f,0x03a51a5e,0x019293f4,0x0048bb37,0x013d3341,0x0143151e,0x019c74e1,0x00911914,0x0076ddde}},
	{{0x006bc26f,0x00d48e5f,0x00227bbe,0x00629ea8,0x01ea5f8b,0x0179a330,0x027a1d5f,0x01bf8f8e,0x02d26e2a,0x00c6b65e},{0x01701ab6,0x0051da77,0x01b4b667,0x00a0ce7c,0x038ae37b,0x012ac852,0x03a0b0fe,0x0097c2bb,0x00a017d2,0x01eb8b2a},{0x0120b962,0x0005fb42,0x0353b6fd,0x0061f8ce,0x007a1463,0x01560a64,0x00e0a792,0x01907c92,0x013a6622,0x007b47f1}}
};
