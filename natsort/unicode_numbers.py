# -*- coding: utf-8 -*-
"""
Contains all possible non-ASCII unicode numbers.
"""
from __future__ import (
    print_function,
    division,
    unicode_literals,
    absolute_import
)

# Std. lib imports.
import unicodedata

# Local imports.
from natsort.compat.py23 import py23_unichr


# Rather than determine this on the fly, which would incur a startup
# runtime penalty, the hex values of the Unicode numeric characters
# are hard-coded below.
numeric_hex = (
    0XB2, 0XB3, 0XB9, 0XBC, 0XBD, 0XBE, 0X660, 0X661, 0X662,
    0X663, 0X664, 0X665, 0X666, 0X667, 0X668, 0X669, 0X6F0,
    0X6F1, 0X6F2, 0X6F3, 0X6F4, 0X6F5, 0X6F6, 0X6F7, 0X6F8,
    0X6F9, 0X7C0, 0X7C1, 0X7C2, 0X7C3, 0X7C4, 0X7C5, 0X7C6,
    0X7C7, 0X7C8, 0X7C9, 0X966, 0X967, 0X968, 0X969, 0X96A,
    0X96B, 0X96C, 0X96D, 0X96E, 0X96F, 0X9E6, 0X9E7, 0X9E8,
    0X9E9, 0X9EA, 0X9EB, 0X9EC, 0X9ED, 0X9EE, 0X9EF, 0X9F4,
    0X9F5, 0X9F6, 0X9F7, 0X9F8, 0X9F9, 0XA66, 0XA67, 0XA68,
    0XA69, 0XA6A, 0XA6B, 0XA6C, 0XA6D, 0XA6E, 0XA6F, 0XAE6,
    0XAE7, 0XAE8, 0XAE9, 0XAEA, 0XAEB, 0XAEC, 0XAED, 0XAEE,
    0XAEF, 0XB66, 0XB67, 0XB68, 0XB69, 0XB6A, 0XB6B, 0XB6C,
    0XB6D, 0XB6E, 0XB6F, 0XB72, 0XB73, 0XB74, 0XB75, 0XB76,
    0XB77, 0XBE6, 0XBE7, 0XBE8, 0XBE9, 0XBEA, 0XBEB, 0XBEC,
    0XBED, 0XBEE, 0XBEF, 0XBF0, 0XBF1, 0XBF2, 0XC66, 0XC67,
    0XC68, 0XC69, 0XC6A, 0XC6B, 0XC6C, 0XC6D, 0XC6E, 0XC6F,
    0XC78, 0XC79, 0XC7A, 0XC7B, 0XC7C, 0XC7D, 0XC7E, 0XCE6,
    0XCE7, 0XCE8, 0XCE9, 0XCEA, 0XCEB, 0XCEC, 0XCED, 0XCEE,
    0XCEF, 0XD58, 0XD59, 0XD5A, 0XD5B, 0XD5C, 0XD5D, 0XD5E,
    0XD66, 0XD67, 0XD68, 0XD69, 0XD6A, 0XD6B, 0XD6C, 0XD6D,
    0XD6E, 0XD6F, 0XD70, 0XD71, 0XD72, 0XD73, 0XD74, 0XD75,
    0XD76, 0XD77, 0XD78, 0XDE6, 0XDE7, 0XDE8, 0XDE9, 0XDEA,
    0XDEB, 0XDEC, 0XDED, 0XDEE, 0XDEF, 0XE50, 0XE51, 0XE52,
    0XE53, 0XE54, 0XE55, 0XE56, 0XE57, 0XE58, 0XE59, 0XED0,
    0XED1, 0XED2, 0XED3, 0XED4, 0XED5, 0XED6, 0XED7, 0XED8,
    0XED9, 0XF20, 0XF21, 0XF22, 0XF23, 0XF24, 0XF25, 0XF26,
    0XF27, 0XF28, 0XF29, 0XF2A, 0XF2B, 0XF2C, 0XF2D, 0XF2E,
    0XF2F, 0XF30, 0XF31, 0XF32, 0XF33, 0X1040, 0X1041, 0X1042,
    0X1043, 0X1044, 0X1045, 0X1046, 0X1047, 0X1048, 0X1049,
    0X1090, 0X1091, 0X1092, 0X1093, 0X1094, 0X1095, 0X1096,
    0X1097, 0X1098, 0X1099, 0X1369, 0X136A, 0X136B, 0X136C,
    0X136D, 0X136E, 0X136F, 0X1370, 0X1371, 0X1372, 0X1373,
    0X1374, 0X1375, 0X1376, 0X1377, 0X1378, 0X1379, 0X137A,
    0X137B, 0X137C, 0X16EE, 0X16EF, 0X16F0, 0X17E0, 0X17E1,
    0X17E2, 0X17E3, 0X17E4, 0X17E5, 0X17E6, 0X17E7, 0X17E8,
    0X17E9, 0X17F0, 0X17F1, 0X17F2, 0X17F3, 0X17F4, 0X17F5,
    0X17F6, 0X17F7, 0X17F8, 0X17F9, 0X1810, 0X1811, 0X1812,
    0X1813, 0X1814, 0X1815, 0X1816, 0X1817, 0X1818, 0X1819,
    0X1946, 0X1947, 0X1948, 0X1949, 0X194A, 0X194B, 0X194C,
    0X194D, 0X194E, 0X194F, 0X19D0, 0X19D1, 0X19D2, 0X19D3,
    0X19D4, 0X19D5, 0X19D6, 0X19D7, 0X19D8, 0X19D9, 0X19DA,
    0X1A80, 0X1A81, 0X1A82, 0X1A83, 0X1A84, 0X1A85, 0X1A86,
    0X1A87, 0X1A88, 0X1A89, 0X1A90, 0X1A91, 0X1A92, 0X1A93,
    0X1A94, 0X1A95, 0X1A96, 0X1A97, 0X1A98, 0X1A99, 0X1B50,
    0X1B51, 0X1B52, 0X1B53, 0X1B54, 0X1B55, 0X1B56, 0X1B57,
    0X1B58, 0X1B59, 0X1BB0, 0X1BB1, 0X1BB2, 0X1BB3, 0X1BB4,
    0X1BB5, 0X1BB6, 0X1BB7, 0X1BB8, 0X1BB9, 0X1C40, 0X1C41,
    0X1C42, 0X1C43, 0X1C44, 0X1C45, 0X1C46, 0X1C47, 0X1C48,
    0X1C49, 0X1C50, 0X1C51, 0X1C52, 0X1C53, 0X1C54, 0X1C55,
    0X1C56, 0X1C57, 0X1C58, 0X1C59, 0X2070, 0X2074, 0X2075,
    0X2076, 0X2077, 0X2078, 0X2079, 0X2080, 0X2081, 0X2082,
    0X2083, 0X2084, 0X2085, 0X2086, 0X2087, 0X2088, 0X2089,
    0X2150, 0X2151, 0X2152, 0X2153, 0X2154, 0X2155, 0X2156,
    0X2157, 0X2158, 0X2159, 0X215A, 0X215B, 0X215C, 0X215D,
    0X215E, 0X215F, 0X2160, 0X2161, 0X2162, 0X2163, 0X2164,
    0X2165, 0X2166, 0X2167, 0X2168, 0X2169, 0X216A, 0X216B,
    0X216C, 0X216D, 0X216E, 0X216F, 0X2170, 0X2171, 0X2172,
    0X2173, 0X2174, 0X2175, 0X2176, 0X2177, 0X2178, 0X2179,
    0X217A, 0X217B, 0X217C, 0X217D, 0X217E, 0X217F, 0X2180,
    0X2181, 0X2182, 0X2185, 0X2186, 0X2187, 0X2188, 0X2189,
    0X2460, 0X2461, 0X2462, 0X2463, 0X2464, 0X2465, 0X2466,
    0X2467, 0X2468, 0X2469, 0X246A, 0X246B, 0X246C, 0X246D,
    0X246E, 0X246F, 0X2470, 0X2471, 0X2472, 0X2473, 0X2474,
    0X2475, 0X2476, 0X2477, 0X2478, 0X2479, 0X247A, 0X247B,
    0X247C, 0X247D, 0X247E, 0X247F, 0X2480, 0X2481, 0X2482,
    0X2483, 0X2484, 0X2485, 0X2486, 0X2487, 0X2488, 0X2489,
    0X248A, 0X248B, 0X248C, 0X248D, 0X248E, 0X248F, 0X2490,
    0X2491, 0X2492, 0X2493, 0X2494, 0X2495, 0X2496, 0X2497,
    0X2498, 0X2499, 0X249A, 0X249B, 0X24EA, 0X24EB, 0X24EC,
    0X24ED, 0X24EE, 0X24EF, 0X24F0, 0X24F1, 0X24F2, 0X24F3,
    0X24F4, 0X24F5, 0X24F6, 0X24F7, 0X24F8, 0X24F9, 0X24FA,
    0X24FB, 0X24FC, 0X24FD, 0X24FE, 0X24FF, 0X2776, 0X2777,
    0X2778, 0X2779, 0X277A, 0X277B, 0X277C, 0X277D, 0X277E,
    0X277F, 0X2780, 0X2781, 0X2782, 0X2783, 0X2784, 0X2785,
    0X2786, 0X2787, 0X2788, 0X2789, 0X278A, 0X278B, 0X278C,
    0X278D, 0X278E, 0X278F, 0X2790, 0X2791, 0X2792, 0X2793,
    0X2CFD, 0X3007, 0X3021, 0X3022, 0X3023, 0X3024, 0X3025,
    0X3026, 0X3027, 0X3028, 0X3029, 0X3038, 0X3039, 0X303A,
    0X3192, 0X3193, 0X3194, 0X3195, 0X3220, 0X3221, 0X3222,
    0X3223, 0X3224, 0X3225, 0X3226, 0X3227, 0X3228, 0X3229,
    0X3248, 0X3249, 0X324A, 0X324B, 0X324C, 0X324D, 0X324E,
    0X324F, 0X3251, 0X3252, 0X3253, 0X3254, 0X3255, 0X3256,
    0X3257, 0X3258, 0X3259, 0X325A, 0X325B, 0X325C, 0X325D,
    0X325E, 0X325F, 0X3280, 0X3281, 0X3282, 0X3283, 0X3284,
    0X3285, 0X3286, 0X3287, 0X3288, 0X3289, 0X32B1, 0X32B2,
    0X32B3, 0X32B4, 0X32B5, 0X32B6, 0X32B7, 0X32B8, 0X32B9,
    0X32BA, 0X32BB, 0X32BC, 0X32BD, 0X32BE, 0X32BF, 0X3405,
    0X3483, 0X382A, 0X3B4D, 0X4E00, 0X4E03, 0X4E07, 0X4E09,
    0X4E5D, 0X4E8C, 0X4E94, 0X4E96, 0X4EBF, 0X4EC0, 0X4EDF,
    0X4EE8, 0X4F0D, 0X4F70, 0X5104, 0X5146, 0X5169, 0X516B,
    0X516D, 0X5341, 0X5343, 0X5344, 0X5345, 0X534C, 0X53C1,
    0X53C2, 0X53C3, 0X53C4, 0X56DB, 0X58F1, 0X58F9, 0X5E7A,
    0X5EFE, 0X5EFF, 0X5F0C, 0X5F0D, 0X5F0E, 0X5F10, 0X62FE,
    0X634C, 0X67D2, 0X6F06, 0X7396, 0X767E, 0X8086, 0X842C,
    0X8CAE, 0X8CB3, 0X8D30, 0X9621, 0X9646, 0X964C, 0X9678,
    0X96F6, 0XA620, 0XA621, 0XA622, 0XA623, 0XA624, 0XA625,
    0XA626, 0XA627, 0XA628, 0XA629, 0XA6E6, 0XA6E7, 0XA6E8,
    0XA6E9, 0XA6EA, 0XA6EB, 0XA6EC, 0XA6ED, 0XA6EE, 0XA6EF,
    0XA830, 0XA831, 0XA832, 0XA833, 0XA834, 0XA835, 0XA8D0,
    0XA8D1, 0XA8D2, 0XA8D3, 0XA8D4, 0XA8D5, 0XA8D6, 0XA8D7,
    0XA8D8, 0XA8D9, 0XA900, 0XA901, 0XA902, 0XA903, 0XA904,
    0XA905, 0XA906, 0XA907, 0XA908, 0XA909, 0XA9D0, 0XA9D1,
    0XA9D2, 0XA9D3, 0XA9D4, 0XA9D5, 0XA9D6, 0XA9D7, 0XA9D8,
    0XA9D9, 0XA9F0, 0XA9F1, 0XA9F2, 0XA9F3, 0XA9F4, 0XA9F5,
    0XA9F6, 0XA9F7, 0XA9F8, 0XA9F9, 0XAA50, 0XAA51, 0XAA52,
    0XAA53, 0XAA54, 0XAA55, 0XAA56, 0XAA57, 0XAA58, 0XAA59,
    0XABF0, 0XABF1, 0XABF2, 0XABF3, 0XABF4, 0XABF5, 0XABF6,
    0XABF7, 0XABF8, 0XABF9, 0XF96B, 0XF973, 0XF978, 0XF9B2,
    0XF9D1, 0XF9D3, 0XF9FD, 0XFF10, 0XFF11, 0XFF12, 0XFF13,
    0XFF14, 0XFF15, 0XFF16, 0XFF17, 0XFF18, 0XFF19, 0X10107,
    0X10108, 0X10109, 0X1010A, 0X1010B, 0X1010C, 0X1010D,
    0X1010E, 0X1010F, 0X10110, 0X10111, 0X10112, 0X10113,
    0X10114, 0X10115, 0X10116, 0X10117, 0X10118, 0X10119,
    0X1011A, 0X1011B, 0X1011C, 0X1011D, 0X1011E, 0X1011F,
    0X10120, 0X10121, 0X10122, 0X10123, 0X10124, 0X10125,
    0X10126, 0X10127, 0X10128, 0X10129, 0X1012A, 0X1012B,
    0X1012C, 0X1012D, 0X1012E, 0X1012F, 0X10130, 0X10131,
    0X10132, 0X10133, 0X10140, 0X10141, 0X10142, 0X10143,
    0X10144, 0X10145, 0X10146, 0X10147, 0X10148, 0X10149,
    0X1014A, 0X1014B, 0X1014C, 0X1014D, 0X1014E, 0X1014F,
    0X10150, 0X10151, 0X10152, 0X10153, 0X10154, 0X10155,
    0X10156, 0X10157, 0X10158, 0X10159, 0X1015A, 0X1015B,
    0X1015C, 0X1015D, 0X1015E, 0X1015F, 0X10160, 0X10161,
    0X10162, 0X10163, 0X10164, 0X10165, 0X10166, 0X10167,
    0X10168, 0X10169, 0X1016A, 0X1016B, 0X1016C, 0X1016D,
    0X1016E, 0X1016F, 0X10170, 0X10171, 0X10172, 0X10173,
    0X10174, 0X10175, 0X10176, 0X10177, 0X10178, 0X1018A,
    0X1018B, 0X102E1, 0X102E2, 0X102E3, 0X102E4, 0X102E5,
    0X102E6, 0X102E7, 0X102E8, 0X102E9, 0X102EA, 0X102EB,
    0X102EC, 0X102ED, 0X102EE, 0X102EF, 0X102F0, 0X102F1,
    0X102F2, 0X102F3, 0X102F4, 0X102F5, 0X102F6, 0X102F7,
    0X102F8, 0X102F9, 0X102FA, 0X102FB, 0X10320, 0X10321,
    0X10322, 0X10323, 0X10341, 0X1034A, 0X103D1, 0X103D2,
    0X103D3, 0X103D4, 0X103D5, 0X104A0, 0X104A1, 0X104A2,
    0X104A3, 0X104A4, 0X104A5, 0X104A6, 0X104A7, 0X104A8,
    0X104A9, 0X10858, 0X10859, 0X1085A, 0X1085B, 0X1085C,
    0X1085D, 0X1085E, 0X1085F, 0X10879, 0X1087A, 0X1087B,
    0X1087C, 0X1087D, 0X1087E, 0X1087F, 0X108A7, 0X108A8,
    0X108A9, 0X108AA, 0X108AB, 0X108AC, 0X108AD, 0X108AE,
    0X108AF, 0X108FB, 0X108FC, 0X108FD, 0X108FE, 0X108FF,
    0X10916, 0X10917, 0X10918, 0X10919, 0X1091A, 0X1091B,
    0X109BC, 0X109BD, 0X109C0, 0X109C1, 0X109C2, 0X109C3,
    0X109C4, 0X109C5, 0X109C6, 0X109C7, 0X109C8, 0X109C9,
    0X109CA, 0X109CB, 0X109CC, 0X109CD, 0X109CE, 0X109CF,
    0X109D2, 0X109D3, 0X109D4, 0X109D5, 0X109D6, 0X109D7,
    0X109D8, 0X109D9, 0X109DA, 0X109DB, 0X109DC, 0X109DD,
    0X109DE, 0X109DF, 0X109E0, 0X109E1, 0X109E2, 0X109E3,
    0X109E4, 0X109E5, 0X109E6, 0X109E7, 0X109E8, 0X109E9,
    0X109EA, 0X109EB, 0X109EC, 0X109ED, 0X109EE, 0X109EF,
    0X109F0, 0X109F1, 0X109F2, 0X109F3, 0X109F4, 0X109F5,
    0X109F6, 0X109F7, 0X109F8, 0X109F9, 0X109FA, 0X109FB,
    0X109FC, 0X109FD, 0X109FE, 0X109FF, 0X10A40, 0X10A41,
    0X10A42, 0X10A43, 0X10A44, 0X10A45, 0X10A46, 0X10A47,
    0X10A48, 0X10A7D, 0X10A7E, 0X10A9D, 0X10A9E, 0X10A9F,
    0X10AEB, 0X10AEC, 0X10AED, 0X10AEE, 0X10AEF, 0X10B58,
    0X10B59, 0X10B5A, 0X10B5B, 0X10B5C, 0X10B5D, 0X10B5E,
    0X10B5F, 0X10B78, 0X10B79, 0X10B7A, 0X10B7B, 0X10B7C,
    0X10B7D, 0X10B7E, 0X10B7F, 0X10BA9, 0X10BAA, 0X10BAB,
    0X10BAC, 0X10BAD, 0X10BAE, 0X10BAF, 0X10CFA, 0X10CFB,
    0X10CFC, 0X10CFD, 0X10CFE, 0X10CFF, 0X10D30, 0X10D31,
    0X10D32, 0X10D33, 0X10D34, 0X10D35, 0X10D36, 0X10D37,
    0X10D38, 0X10D39, 0X10E60, 0X10E61, 0X10E62, 0X10E63,
    0X10E64, 0X10E65, 0X10E66, 0X10E67, 0X10E68, 0X10E69,
    0X10E6A, 0X10E6B, 0X10E6C, 0X10E6D, 0X10E6E, 0X10E6F,
    0X10E70, 0X10E71, 0X10E72, 0X10E73, 0X10E74, 0X10E75,
    0X10E76, 0X10E77, 0X10E78, 0X10E79, 0X10E7A, 0X10E7B,
    0X10E7C, 0X10E7D, 0X10E7E, 0X10F1D, 0X10F1E, 0X10F1F,
    0X10F20, 0X10F21, 0X10F22, 0X10F23, 0X10F24, 0X10F25,
    0X10F26, 0X10F51, 0X10F52, 0X10F53, 0X10F54, 0X11052,
    0X11053, 0X11054, 0X11055, 0X11056, 0X11057, 0X11058,
    0X11059, 0X1105A, 0X1105B, 0X1105C, 0X1105D, 0X1105E,
    0X1105F, 0X11060, 0X11061, 0X11062, 0X11063, 0X11064,
    0X11065, 0X11066, 0X11067, 0X11068, 0X11069, 0X1106A,
    0X1106B, 0X1106C, 0X1106D, 0X1106E, 0X1106F, 0X110F0,
    0X110F1, 0X110F2, 0X110F3, 0X110F4, 0X110F5, 0X110F6,
    0X110F7, 0X110F8, 0X110F9, 0X11136, 0X11137, 0X11138,
    0X11139, 0X1113A, 0X1113B, 0X1113C, 0X1113D, 0X1113E,
    0X1113F, 0X111D0, 0X111D1, 0X111D2, 0X111D3, 0X111D4,
    0X111D5, 0X111D6, 0X111D7, 0X111D8, 0X111D9, 0X111E1,
    0X111E2, 0X111E3, 0X111E4, 0X111E5, 0X111E6, 0X111E7,
    0X111E8, 0X111E9, 0X111EA, 0X111EB, 0X111EC, 0X111ED,
    0X111EE, 0X111EF, 0X111F0, 0X111F1, 0X111F2, 0X111F3,
    0X111F4, 0X112F0, 0X112F1, 0X112F2, 0X112F3, 0X112F4,
    0X112F5, 0X112F6, 0X112F7, 0X112F8, 0X112F9, 0X11450,
    0X11451, 0X11452, 0X11453, 0X11454, 0X11455, 0X11456,
    0X11457, 0X11458, 0X11459, 0X114D0, 0X114D1, 0X114D2,
    0X114D3, 0X114D4, 0X114D5, 0X114D6, 0X114D7, 0X114D8,
    0X114D9, 0X11650, 0X11651, 0X11652, 0X11653, 0X11654,
    0X11655, 0X11656, 0X11657, 0X11658, 0X11659, 0X116C0,
    0X116C1, 0X116C2, 0X116C3, 0X116C4, 0X116C5, 0X116C6,
    0X116C7, 0X116C8, 0X116C9, 0X11730, 0X11731, 0X11732,
    0X11733, 0X11734, 0X11735, 0X11736, 0X11737, 0X11738,
    0X11739, 0X1173A, 0X1173B, 0X118E0, 0X118E1, 0X118E2,
    0X118E3, 0X118E4, 0X118E5, 0X118E6, 0X118E7, 0X118E8,
    0X118E9, 0X118EA, 0X118EB, 0X118EC, 0X118ED, 0X118EE,
    0X118EF, 0X118F0, 0X118F1, 0X118F2, 0X11C50, 0X11C51,
    0X11C52, 0X11C53, 0X11C54, 0X11C55, 0X11C56, 0X11C57,
    0X11C58, 0X11C59, 0X11C5A, 0X11C5B, 0X11C5C, 0X11C5D,
    0X11C5E, 0X11C5F, 0X11C60, 0X11C61, 0X11C62, 0X11C63,
    0X11C64, 0X11C65, 0X11C66, 0X11C67, 0X11C68, 0X11C69,
    0X11C6A, 0X11C6B, 0X11C6C, 0X11D50, 0X11D51, 0X11D52,
    0X11D53, 0X11D54, 0X11D55, 0X11D56, 0X11D57, 0X11D58,
    0X11D59, 0X11DA0, 0X11DA1, 0X11DA2, 0X11DA3, 0X11DA4,
    0X11DA5, 0X11DA6, 0X11DA7, 0X11DA8, 0X11DA9, 0X12400,
    0X12401, 0X12402, 0X12403, 0X12404, 0X12405, 0X12406,
    0X12407, 0X12408, 0X12409, 0X1240A, 0X1240B, 0X1240C,
    0X1240D, 0X1240E, 0X1240F, 0X12410, 0X12411, 0X12412,
    0X12413, 0X12414, 0X12415, 0X12416, 0X12417, 0X12418,
    0X12419, 0X1241A, 0X1241B, 0X1241C, 0X1241D, 0X1241E,
    0X1241F, 0X12420, 0X12421, 0X12422, 0X12423, 0X12424,
    0X12425, 0X12426, 0X12427, 0X12428, 0X12429, 0X1242A,
    0X1242B, 0X1242C, 0X1242D, 0X1242E, 0X1242F, 0X12430,
    0X12431, 0X12432, 0X12433, 0X12434, 0X12435, 0X12436,
    0X12437, 0X12438, 0X12439, 0X1243A, 0X1243B, 0X1243C,
    0X1243D, 0X1243E, 0X1243F, 0X12440, 0X12441, 0X12442,
    0X12443, 0X12444, 0X12445, 0X12446, 0X12447, 0X12448,
    0X12449, 0X1244A, 0X1244B, 0X1244C, 0X1244D, 0X1244E,
    0X1244F, 0X12450, 0X12451, 0X12452, 0X12453, 0X12454,
    0X12455, 0X12456, 0X12457, 0X12458, 0X12459, 0X1245A,
    0X1245B, 0X1245C, 0X1245D, 0X1245E, 0X1245F, 0X12460,
    0X12461, 0X12462, 0X12463, 0X12464, 0X12465, 0X12466,
    0X12467, 0X12468, 0X12469, 0X1246A, 0X1246B, 0X1246C,
    0X1246D, 0X1246E, 0X16A60, 0X16A61, 0X16A62, 0X16A63,
    0X16A64, 0X16A65, 0X16A66, 0X16A67, 0X16A68, 0X16A69,
    0X16B50, 0X16B51, 0X16B52, 0X16B53, 0X16B54, 0X16B55,
    0X16B56, 0X16B57, 0X16B58, 0X16B59, 0X16B5B, 0X16B5C,
    0X16B5D, 0X16B5E, 0X16B5F, 0X16B60, 0X16B61, 0X16E80,
    0X16E81, 0X16E82, 0X16E83, 0X16E84, 0X16E85, 0X16E86,
    0X16E87, 0X16E88, 0X16E89, 0X16E8A, 0X16E8B, 0X16E8C,
    0X16E8D, 0X16E8E, 0X16E8F, 0X16E90, 0X16E91, 0X16E92,
    0X16E93, 0X16E94, 0X16E95, 0X16E96, 0X1D2E0, 0X1D2E1,
    0X1D2E2, 0X1D2E3, 0X1D2E4, 0X1D2E5, 0X1D2E6, 0X1D2E7,
    0X1D2E8, 0X1D2E9, 0X1D2EA, 0X1D2EB, 0X1D2EC, 0X1D2ED,
    0X1D2EE, 0X1D2EF, 0X1D2F0, 0X1D2F1, 0X1D2F2, 0X1D2F3,
    0X1D360, 0X1D361, 0X1D362, 0X1D363, 0X1D364, 0X1D365,
    0X1D366, 0X1D367, 0X1D368, 0X1D369, 0X1D36A, 0X1D36B,
    0X1D36C, 0X1D36D, 0X1D36E, 0X1D36F, 0X1D370, 0X1D371,
    0X1D372, 0X1D373, 0X1D374, 0X1D375, 0X1D376, 0X1D377,
    0X1D378, 0X1D7CE, 0X1D7CF, 0X1D7D0, 0X1D7D1, 0X1D7D2,
    0X1D7D3, 0X1D7D4, 0X1D7D5, 0X1D7D6, 0X1D7D7, 0X1D7D8,
    0X1D7D9, 0X1D7DA, 0X1D7DB, 0X1D7DC, 0X1D7DD, 0X1D7DE,
    0X1D7DF, 0X1D7E0, 0X1D7E1, 0X1D7E2, 0X1D7E3, 0X1D7E4,
    0X1D7E5, 0X1D7E6, 0X1D7E7, 0X1D7E8, 0X1D7E9, 0X1D7EA,
    0X1D7EB, 0X1D7EC, 0X1D7ED, 0X1D7EE, 0X1D7EF, 0X1D7F0,
    0X1D7F1, 0X1D7F2, 0X1D7F3, 0X1D7F4, 0X1D7F5, 0X1D7F6,
    0X1D7F7, 0X1D7F8, 0X1D7F9, 0X1D7FA, 0X1D7FB, 0X1D7FC,
    0X1D7FD, 0X1D7FE, 0X1D7FF, 0X1E8C7, 0X1E8C8, 0X1E8C9,
    0X1E8CA, 0X1E8CB, 0X1E8CC, 0X1E8CD, 0X1E8CE, 0X1E8CF,
    0X1E950, 0X1E951, 0X1E952, 0X1E953, 0X1E954, 0X1E955,
    0X1E956, 0X1E957, 0X1E958, 0X1E959, 0X1EC71, 0X1EC72,
    0X1EC73, 0X1EC74, 0X1EC75, 0X1EC76, 0X1EC77, 0X1EC78,
    0X1EC79, 0X1EC7A, 0X1EC7B, 0X1EC7C, 0X1EC7D, 0X1EC7E,
    0X1EC7F, 0X1EC80, 0X1EC81, 0X1EC82, 0X1EC83, 0X1EC84,
    0X1EC85, 0X1EC86, 0X1EC87, 0X1EC88, 0X1EC89, 0X1EC8A,
    0X1EC8B, 0X1EC8C, 0X1EC8D, 0X1EC8E, 0X1EC8F, 0X1EC90,
    0X1EC91, 0X1EC92, 0X1EC93, 0X1EC94, 0X1EC95, 0X1EC96,
    0X1EC97, 0X1EC98, 0X1EC99, 0X1EC9A, 0X1EC9B, 0X1EC9C,
    0X1EC9D, 0X1EC9E, 0X1EC9F, 0X1ECA0, 0X1ECA1, 0X1ECA2,
    0X1ECA3, 0X1ECA4, 0X1ECA5, 0X1ECA6, 0X1ECA7, 0X1ECA8,
    0X1ECA9, 0X1ECAA, 0X1ECAB, 0X1ECAD, 0X1ECAE, 0X1ECAF,
    0X1ECB1, 0X1ECB2, 0X1ECB3, 0X1ECB4, 0X1F100, 0X1F101,
    0X1F102, 0X1F103, 0X1F104, 0X1F105, 0X1F106, 0X1F107,
    0X1F108, 0X1F109, 0X1F10A, 0X1F10B, 0X1F10C, 0X20001,
    0X20064, 0X200E2, 0X20121, 0X2092A, 0X20983, 0X2098C,
    0X2099C, 0X20AEA, 0X20AFD, 0X20B19, 0X22390, 0X22998,
    0X23B1B, 0X2626D, 0X2F890,
)

# Convert each hex into the literal Unicode character.
# Stop if a ValueError is raised in case of a narrow Unicode build.
# The extra check with unicodedata is in case this Python version
# does not support some characters.
numeric_chars = []
for a in numeric_hex:
    try:
        l = py23_unichr(a)
    except ValueError:  # pragma: no cover
        break
    if unicodedata.numeric(l, None) is None:
        continue  # pragma: no cover
    numeric_chars.append(l)

# The digit characters are a subset of the numerals.
digit_chars = [a for a in numeric_chars
               if unicodedata.digit(a, None) is not None]

# The decimal characters are a subset of the numberals
# (probably of the digits, but let's be safe).
decimal_chars = [a for a in numeric_chars
                 if unicodedata.decimal(a, None) is not None]

# Create a single string with the above data.
decimals = ''.join(decimal_chars)
digits = ''.join(digit_chars)
numeric = ''.join(numeric_chars)
digits_no_decimals = ''.join([x for x in digits if x not in decimals])
numeric_no_decimals = ''.join([x for x in numeric if x not in decimals])

# Some code that can be used to create the above list of hex numbers.
if __name__ == '__main__':
    import textwrap
    from natsort.compat.py23 import py23_range

    hex_chars = []
    for i in py23_range(0X110000):
        try:
            a = py23_unichr(i)
        except ValueError:
            break
        if a in set('0123456789'):
            continue
        if unicodedata.numeric(a, None) is not None:
            hex_chars.append(i)

    hex_string = ', '.join(['0X{:X}'.format(i) for i in hex_chars])
    for line in textwrap.wrap(hex_string, width=60):
        print('   ', line)
