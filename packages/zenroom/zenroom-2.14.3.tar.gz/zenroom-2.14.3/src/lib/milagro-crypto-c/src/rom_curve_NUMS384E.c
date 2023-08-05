/*
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
*/

#include "arch.h"
#include "ecp_NUMS384E.h"

/*  NUMS 384-bit Curve - Edwards */

#if CHUNK==16

#error Not supported

#endif

#if CHUNK==32

const int CURVE_Cof_I_NUMS384E= 4;
const BIG_384_29 CURVE_Cof_NUMS384E= {0x4,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0};
const int CURVE_A_NUMS384E= 1;
const int CURVE_B_I_NUMS384E= -11556;
const BIG_384_29 CURVE_B_NUMS384E= {0x1FFFD19F,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x7F};
const BIG_384_29 CURVE_Order_NUMS384E= {0x6A3897D,0x5CEE627,0xD721E48,0x8AAB556,0x1E1CF61E,0xD0E5A35,0x1FFF891C,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1FFFFFFF,0x1F};
const BIG_384_29 CURVE_Gx_NUMS384E= {0xC206BDE,0x6AA0723,0x116504D4,0x52562CA,0x163406FF,0x1FD47998,0x10015D8F,0x8DCB7C9,0x15B30BF4,0x14D72AED,0x102DA884,0xB524CD9,0x1B111FB4,0x30};
const BIG_384_29 CURVE_Gy_NUMS384E= {0x10729392,0xC681F0F,0x1B123727,0x561F28D,0x1964B007,0xC7BFB22,0x1D5A0C3E,0xE9E284B,0x1716AD82,0x11D886E,0x1CE2C69,0x134DDD61,0x983E67B,0x41};
#endif

#if CHUNK==64

const int CURVE_Cof_I_NUMS384E= 4;
const BIG_384_56 CURVE_Cof_NUMS384E= {0x4L,0x0L,0x0L,0x0L,0x0L,0x0L,0x0L};
const int CURVE_A_NUMS384E= 1;
const int CURVE_B_I_NUMS384E= -11556;
const BIG_384_56 CURVE_B_NUMS384E= {0xFFFFFFFFFFD19FL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFL};
const BIG_384_56 CURVE_Order_NUMS384E= {0xB9DCC4E6A3897DL,0x555AAB35C87920L,0x1CB46BE1CF61E4L,0xFFFFFFFFE2471AL,0xFFFFFFFFFFFFFFL,0xFFFFFFFFFFFFFFL,0x3FFFFFFFFFFFL};
const BIG_384_56 CURVE_Gx_NUMS384E= {0xD540E46C206BDEL,0x92B16545941350L,0xA8F33163406FF2L,0xE5BE4C005763FFL,0xE55DB5B30BF446L,0x266CC0B6A2129AL,0x61B111FB45A9L};
const BIG_384_56 CURVE_Gy_NUMS384E= {0x8D03E1F0729392L,0xB0F946EC48DC9DL,0xF7F645964B0072L,0xF1425F56830F98L,0xB10DD716AD8274L,0xEEB08738B1A423L,0x82983E67B9A6L};
#endif
