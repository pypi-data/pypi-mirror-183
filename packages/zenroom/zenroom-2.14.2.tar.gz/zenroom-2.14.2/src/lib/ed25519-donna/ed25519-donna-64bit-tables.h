static const ge25519 ge25519_basepoint = {
	{0x00062d608f25d51a,0x000412a4b4f6592a,0x00075b7171a4b31d,0x0001ff60527118fe,0x000216936d3cd6e5},
	{0x0006666666666658,0x0004cccccccccccc,0x0001999999999999,0x0003333333333333,0x0006666666666666},
	{0x0000000000000001,0x0000000000000000,0x0000000000000000,0x0000000000000000,0x0000000000000000},
	{0x00068ab3a5b7dda3,0x00000eea2a5eadbb,0x0002af8df483c27e,0x000332b375274732,0x00067875f0fd78b7}
};

static const bignum25519 ge25519_ecd = {
	0x00034dca135978a3,0x0001a8283b156ebd,0x0005e7a26001c029,0x000739c663a03cbb,0x00052036cee2b6ff
};

static const bignum25519 ge25519_ec2d = {
	0x00069b9426b2f159,0x00035050762add7a,0x0003cf44c0038052,0x0006738cc7407977,0x0002406d9dc56dff
};

static const bignum25519 ge25519_sqrtneg1 = {
	0x00061b274a0ea0b0,0x0000d5a5fc8f189d,0x0007ef5e9cbd0c60,0x00078595a6804c9e,0x0002b8324804fc1d
};

static const ge25519_niels ge25519_niels_sliding_multiples[32] = {
	{{0x00003905d740913e,0x0000ba2817d673a2,0x00023e2827f4e67c,0x000133d2e0c21a34,0x00044fd2f9298f81},{0x000493c6f58c3b85,0x0000df7181c325f7,0x0000f50b0b3e4cb7,0x0005329385a44c32,0x00007cf9d3a33d4b},{0x00011205877aaa68,0x000479955893d579,0x00050d66309b67a0,0x0002d42d0dbee5ee,0x0006f117b689f0c6}},
	{{0x00011fe8a4fcd265,0x0007bcb8374faacc,0x00052f5af4ef4d4f,0x0005314098f98d10,0x0002ab91587555bd},{0x0005b0a84cee9730,0x00061d10c97155e4,0x0004059cc8096a10,0x00047a608da8014f,0x0007a164e1b9a80f},{0x0006933f0dd0d889,0x00044386bb4c4295,0x0003cb6d3162508c,0x00026368b872a2c6,0x0005a2826af12b9b}},
	{{0x000182c3a447d6ba,0x00022964e536eff2,0x000192821f540053,0x0002f9f19e788e5c,0x000154a7e73eb1b5},{0x0002bc4408a5bb33,0x000078ebdda05442,0x0002ffb112354123,0x000375ee8df5862d,0x0002945ccf146e20},{0x0003dbf1812a8285,0x0000fa17ba3f9797,0x0006f69cb49c3820,0x00034d5a0db3858d,0x00043aabe696b3bb}},
	{{0x00072c9aaa3221b1,0x000267774474f74d,0x000064b0e9b28085,0x0003f04ef53b27c9,0x0001d6edd5d2e531},{0x00025cd0944ea3bf,0x00075673b81a4d63,0x000150b925d1c0d4,0x00013f38d9294114,0x000461bea69283c9},{0x00036dc801b8b3a2,0x0000e0a7d4935e30,0x0001deb7cecc0d7d,0x000053a94e20dd2c,0x0007a9fbb1c6a0f9}},
	{{0x0006217e039d8064,0x0006dea408337e6d,0x00057ac112628206,0x000647cb65e30473,0x00049c05a51fadc9},{0x0006678aa6a8632f,0x0005ea3788d8b365,0x00021bd6d6994279,0x0007ace75919e4e3,0x00034b9ed338add7},{0x0004e8bf9045af1b,0x000514e33a45e0d6,0x0007533c5b8bfe0f,0x000583557b7e14c9,0x00073c172021b008}},
	{{0x00075b0249864348,0x00052ee11070262b,0x000237ae54fb5acd,0x0003bfd1d03aaab5,0x00018ab598029d5c},{0x000700848a802ade,0x0001e04605c4e5f7,0x0005c0d01b9767fb,0x0007d7889f42388b,0x0004275aae2546d8},{0x00032cc5fd6089e9,0x000426505c949b05,0x00046a18880c7ad2,0x0004a4221888ccda,0x0003dc65522b53df}},
	{{0x0007013b327fbf93,0x0001336eeded6a0d,0x0002b565a2bbf3af,0x000253ce89591955,0x0000267882d17602},{0x0000c222a2007f6d,0x000356b79bdb77ee,0x00041ee81efe12ce,0x000120a9bd07097d,0x000234fd7eec346f},{0x0000a119732ea378,0x00063bf1ba8e2a6c,0x00069f94cc90df9a,0x000431d1779bfc48,0x000497ba6fdaa097}},
	{{0x0003cd86468ccf0b,0x00048553221ac081,0x0006c9464b4e0a6e,0x00075fba84180403,0x00043b5cd4218d05},{0x0006cc0313cfeaa0,0x0001a313848da499,0x0007cb534219230a,0x00039596dedefd60,0x00061e22917f12de},{0x0002762f9bd0b516,0x0001c6e7fbddcbb3,0x00075909c3ace2bd,0x00042101972d3ec9,0x000511d61210ae4d}},
	{{0x000386484420de87,0x0002d6b25db68102,0x000650b4962873c0,0x0004081cfd271394,0x00071a7fe6fe2482},{0x000676ef950e9d81,0x0001b81ae089f258,0x00063c4922951883,0x0002f1d54d9b3237,0x0006d325924ddb85},{0x000182b8a5c8c854,0x00073fcbe5406d8e,0x0005de3430cff451,0x000554b967ac8c41,0x0004746c4b6559ee}},
	{{0x000546c864741147,0x0003a1df99092690,0x0001ca8cc9f4d6bb,0x00036b7fc9cd3b03,0x000219663497db5e},{0x00077b3c6dc69a2b,0x0004edf13ec2fa6e,0x0004e85ad77beac8,0x0007dba2b28e7bda,0x0005c9a51de34fe9},{0x0000f1cf79f10e67,0x00043ccb0a2b7ea2,0x00005089dfff776a,0x0001dd84e1d38b88,0x0004804503c60822}},
	{{0x000021d23a36d175,0x0004fd3373c6476d,0x00020e291eeed02a,0x00062f2ecf2e7210,0x000771e098858de4},{0x00049ed02ca37fc7,0x000474c2b5957884,0x0005b8388e816683,0x0004b6c454b76be4,0x000553398a516506},{0x0002f5d278451edf,0x000730b133997342,0x0006965420eb6975,0x000308a3bfa516cf,0x0005a5ed1d68ff5a}},
	{{0x0005e0c558527359,0x0003395b73afd75c,0x000072afa4e4b970,0x00062214329e0f6d,0x000019b60135fefd},{0x0005122afe150e83,0x0004afc966bb0232,0x0001c478833c8268,0x00017839c3fc148f,0x00044acb897d8bf9},{0x000068145e134b83,0x0001e4860982c3cc,0x000068fb5f13d799,0x0007c9283744547e,0x000150c49fde6ad2}},
	{{0x0001863c9cdca868,0x0003770e295a1709,0x0000d85a3720fd13,0x0005e0ff1f71ab06,0x00078a6d7791e05f},{0x0003f29509471138,0x000729eeb4ca31cf,0x00069c22b575bfbc,0x0004910857bce212,0x0006b2b5a075bb99},{0x0007704b47a0b976,0x0002ae82e91aab17,0x00050bd6429806cd,0x00068055158fd8ea,0x000725c7ffc4ad55}},
	{{0x00002bf71cd098c0,0x00049dabcc6cd230,0x00040a6533f905b2,0x000573efac2eb8a4,0x0004cd54625f855f},{0x00026715d1cf99b2,0x0002205441a69c88,0x000448427dcd4b54,0x0001d191e88abdc5,0x000794cc9277cb1f},{0x0006c426c2ac5053,0x0005a65ece4b095e,0x0000c44086f26bb6,0x0007429568197885,0x0007008357b6fcc8}},
	{{0x00039fbb82584a34,0x00047a568f257a03,0x00014d88091ead91,0x0002145b18b1ce24,0x00013a92a3669d6d},{0x0000672738773f01,0x000752bf799f6171,0x0006b4a6dae33323,0x0007b54696ead1dc,0x00006ef7e9851ad0},{0x0003771cc0577de5,0x0003ca06bb8b9952,0x00000b81c5d50390,0x00043512340780ec,0x0003c296ddf8a2af}},
	{{0x00034d2ebb1f2541,0x0000e815b723ff9d,0x000286b416e25443,0x0000bdfe38d1bee8,0x0000a892c7007477},{0x000515f9d914a713,0x00073191ff2255d5,0x00054f5cc2a4bdef,0x0003dd57fc118bcf,0x0007a99d393490c7},{0x0002ed2436bda3e8,0x00002afd00f291ea,0x0000be7381dea321,0x0003e952d4b2b193,0x000286762d28302f}},
	{{0x00058e2bce2ef5bd,0x00068ce8f78c6f8a,0x0006ee26e39261b2,0x00033d0aa50bcf9d,0x0007686f2a3d6f17},{0x000036093ce35b25,0x0003b64d7552e9cf,0x00071ee0fe0b8460,0x00069d0660c969e5,0x00032f1da046a9d9},{0x000512a66d597c6a,0x0000609a70a57551,0x000026c08a3c464c,0x0004531fc8ee39e1,0x000561305f8a9ad2}},
	{{0x0002cc28e7b0c0d5,0x00077b60eb8a6ce4,0x0004042985c277a6,0x000636657b46d3eb,0x000030a1aef2c57c},{0x0004978dec92aed1,0x000069adae7ca201,0x00011ee923290f55,0x00069641898d916c,0x00000aaec53e35d4},{0x0001f773003ad2aa,0x000005642cc10f76,0x00003b48f82cfca6,0x0002403c10ee4329,0x00020be9c1c24065}},
	{{0x0000e44ae2025e60,0x0005f97b9727041c,0x0005683472c0ecec,0x000188882eb1ce7c,0x00069764c545067e},{0x000387d8249673a6,0x0005bea8dc927c2a,0x0005bd8ed5650ef0,0x0000ef0e3fcd40e1,0x000750ab3361f0ac},{0x00023283a2f81037,0x000477aff97e23d1,0x0000b8958dbcbb68,0x0000205b97e8add6,0x00054f96b3fb7075}},
	{{0x0005afc616b11ecd,0x00039f4aec8f22ef,0x0003b39e1625d92e,0x0005f85bd4508873,0x00078e6839fbe85d},{0x0005f20429669279,0x00008fafae4941f5,0x00015d83c4eb7688,0x0001cf379eca4146,0x0003d7fe9c52bb75},{0x00032df737b8856b,0x0000608342f14e06,0x0003967889d74175,0x0001211907fba550,0x00070f268f350088}},
	{{0x0004112070dcf355,0x0007dcff9c22e464,0x00054ada60e03325,0x00025cd98eef769a,0x000404e56c039b8c},{0x00064583b1805f47,0x00022c1baf832cd0,0x000132c01bd4d717,0x0004ecf4c3a75b8f,0x0007c0d345cfad88},{0x00071f4b8c78338a,0x00062cfc16bc2b23,0x00017cf51280d9aa,0x0003bbae5e20a95a,0x00020d754762aaec}},
	{{0x0004feb135b9f543,0x00063bd192ad93ae,0x00044e2ea612cdf7,0x000670f4991583ab,0x00038b8ada8790b4},{0x0007c36fc73bb758,0x0004a6c797734bd1,0x0000ef248ab3950e,0x00063154c9a53ec8,0x0002b8f1e46f3cee},{0x00004a9cdf51f95d,0x0005d963fbd596b8,0x00022d9b68ace54a,0x0004a98e8836c599,0x000049aeb32ceba1}},
	{{0x00067d3c63dcfe7e,0x000112f0adc81aee,0x00053df04c827165,0x0002fe5b33b430f0,0x00051c665e0c8d62},{0x00007d0b75fc7931,0x00016f4ce4ba754a,0x0005ace4c03fbe49,0x00027e0ec12a159c,0x000795ee17530f67},{0x00025b0a52ecbd81,0x0005dc0695fce4a9,0x0003b928c575047d,0x00023bf3512686e5,0x0006cd19bf49dc54}},
	{{0x0007619052179ca3,0x0000c16593f0afd0,0x000265c4795c7428,0x00031c40515d5442,0x0007520f3db40b2e},{0x0006612165afc386,0x0001171aa36203ff,0x0002642ea820a8aa,0x0001f3bb7b313f10,0x0005e01b3a7429e4},{0x00050be3d39357a1,0x0003ab33d294a7b6,0x0004c479ba59edb3,0x0004c30d184d326f,0x00071092c9ccef3c}},
	{{0x0000523f0364918c,0x000687f56d638a7b,0x00020796928ad013,0x0005d38405a54f33,0x0000ea15b03d0257},{0x0003d8ac74051dcf,0x00010ab6f543d0ad,0x0005d0f3ac0fda90,0x0005ef1d2573e5e4,0x0004173a5bb7137a},{0x00056e31f0f9218a,0x0005635f88e102f8,0x0002cbc5d969a5b8,0x000533fbc98b347a,0x0005fc565614a4e3}},
	{{0x0006570dc46d7ae5,0x00018a9f1b91e26d,0x000436b6183f42ab,0x000550acaa4f8198,0x00062711c414c454},{0x0002e1e67790988e,0x0001e38b9ae44912,0x000648fbb4075654,0x00028df1d840cd72,0x0003214c7409d466},{0x0001827406651770,0x0004d144f286c265,0x00017488f0ee9281,0x00019e6cdb5c760c,0x0005bea94073ecb8}},
	{{0x0005bf0912c89be4,0x00062fadcaf38c83,0x00025ec196b3ce2c,0x00077655ff4f017b,0x0003aacd5c148f61},{0x0000ce63f343d2f8,0x0001e0a87d1e368e,0x000045edbc019eea,0x0006979aed28d0d1,0x0004ad0785944f1b},{0x00063b34c3318301,0x0000e0e62d04d0b1,0x000676a233726701,0x00029e9a042d9769,0x0003aff0cb1d9028}},
	{{0x0005c7eb3a20405e,0x0005fdb5aad930f8,0x0004a757e63b8c47,0x00028e9492972456,0x000110e7e86f4cd2},{0x0006430bf4c53505,0x000264c3e4507244,0x00074c9f19a39270,0x00073f84f799bc47,0x0002ccf9f732bd99},{0x0000d89ed603f5e4,0x00051e1604018af8,0x0000b8eedc4a2218,0x00051ba98b9384d0,0x00005c557e0b9693}},
	{{0x0001ce311fc97e6f,0x0006023f3fb5db1f,0x0007b49775e8fc98,0x0003ad70adbf5045,0x0006e154c178fe98},{0x0006bbb089c20eb0,0x0006df41fb0b9eee,0x00051087ed87e16f,0x000102db5c9fa731,0x000289fef0841861},{0x00016336fed69abf,0x0004f066b929f9ec,0x0004e9ff9e6c5b93,0x00018c89bc4bb2ba,0x0006afbf642a95ca}},
	{{0x0000de0c62f5d2c1,0x00049601cf734fb5,0x0006b5c38263f0f6,0x0004623ef5b56d06,0x0000db4b851b9503},{0x00055070f913a8cc,0x000765619eac2bbc,0x0003ab5225f47459,0x00076ced14ab5b48,0x00012c093cedb801},{0x00047f9308b8190f,0x000414235c621f82,0x00031f5ff41a5a76,0x0006736773aab96d,0x00033aa8799c6635}},
	{{0x0007f51ebd085cf2,0x00012cfa67e3f5e1,0x0001800cf1e3d46a,0x00054337615ff0a8,0x000233c6f29e8e21},{0x0000f588fc156cb1,0x000363414da4f069,0x0007296ad9b68aea,0x0004d3711316ae43,0x000212cd0c1c8d58},{0x0004d5107f18c781,0x00064a4fd3a51a5e,0x0004f4cd0448bb37,0x000671d38543151e,0x0001db7778911914}},
	{{0x000352397c6bc26f,0x00018a7aa0227bbe,0x0005e68cc1ea5f8b,0x0006fe3e3a7a1d5f,0x00031ad97ad26e2a},{0x00014769dd701ab6,0x00028339f1b4b667,0x0004ab214b8ae37b,0x00025f0aefa0b0fe,0x0007ae2ca8a017d2},{0x000017ed0920b962,0x000187e33b53b6fd,0x00055829907a1463,0x000641f248e0a792,0x0001ed1fc53a6622}}
};
