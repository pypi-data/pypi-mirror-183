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
#include "ecp_BRAINPOOL.h"

/* Brainpool Curve  */
/* Note that the original curve has been transformed to an isomorphic curve with A=-3 */

#if CHUNK==16

#error Not supported

#endif

#if CHUNK==32

const int CURVE_Cof_I_BRAINPOOL= 1;
const BIG_256_28 CURVE_Cof_BRAINPOOL= {0x1,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0};
const int CURVE_A_BRAINPOOL= -3;
const int CURVE_B_I_BRAINPOOL= 0;
const BIG_256_28 CURVE_B_BRAINPOOL= {0xEE92B04,0xE58101F,0xF49256A,0xEBC4AF2,0x6B7BF93,0x733D0B7,0x4FE66A7,0x30D84EA,0x62C61C4,0x6};
const BIG_256_28 CURVE_Order_BRAINPOOL= {0x74856A7,0x1E0E829,0x1A6F790,0x7AA3B56,0xD718C39,0x909D838,0xC3E660A,0xA1EEA9B,0x9FB57DB,0xA};
const BIG_256_28 CURVE_Gx_BRAINPOOL= {0xE1305F4,0xA191562,0xFBC2B79,0x42C47AA,0x149AFA1,0xB23A656,0x7732213,0xC1CFE7B,0x3E8EB3C,0xA};
const BIG_256_28 CURVE_Gy_BRAINPOOL= {0xB25C9BE,0xABE8F35,0x27001D,0xB6DE39D,0x17E69BC,0xE146444,0xD7F7B22,0x3439C56,0xD996C82,0x2};
#endif

#if CHUNK==64

const int CURVE_Cof_I_BRAINPOOL= 1;
const BIG_256_56 CURVE_Cof_BRAINPOOL= {0x1L,0x0L,0x0L,0x0L,0x0L};
const int CURVE_A_BRAINPOOL= -3;
const int CURVE_B_I_BRAINPOOL= 0;
const BIG_256_56 CURVE_B_BRAINPOOL= {0xE58101FEE92B04L,0xEBC4AF2F49256AL,0x733D0B76B7BF93L,0x30D84EA4FE66A7L,0x662C61C4L};
const BIG_256_56 CURVE_Order_BRAINPOOL= {0x1E0E82974856A7L,0x7AA3B561A6F790L,0x909D838D718C39L,0xA1EEA9BC3E660AL,0xA9FB57DBL};
const BIG_256_56 CURVE_Gx_BRAINPOOL= {0xA191562E1305F4L,0x42C47AAFBC2B79L,0xB23A656149AFA1L,0xC1CFE7B7732213L,0xA3E8EB3CL};
const BIG_256_56 CURVE_Gy_BRAINPOOL= {0xABE8F35B25C9BEL,0xB6DE39D027001DL,0xE14644417E69BCL,0x3439C56D7F7B22L,0x2D996C82L};
#endif

