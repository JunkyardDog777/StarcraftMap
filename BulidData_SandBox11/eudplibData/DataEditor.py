from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664548, Add, 139),# units:Graphics  index:80    from 43 To 182
        SetMemory(0x664548, Add, 9371648),# units:Graphics  index:82    from 39 To 182
        SetMemory(0x66454C, Add, 11206656),# units:Graphics  index:86    from 37 To 208
        SetMemory(0x66454C, Add, 2734686208),# units:Graphics  index:87    from 45 To 208
        SetMemory(0x664550, Add, 165),# units:Graphics  index:88    from 43 To 208
        SetMemory(0x664550, Add, 3840),# units:Graphics  index:89    from 115 To 130
        SetMemory(0x664550, Add, 6029312),# units:Graphics  index:90    from 116 To 208
        SetMemory(0x664550, Add, 2768240640),# units:Graphics  index:91    from 43 To 208
        SetMemory(0x664554, Add, 165),# units:Graphics  index:92    from 43 To 208
        SetMemory(0x664554, Add, 2560),# units:Graphics  index:93    from 198 To 208
        SetMemory(0x664554, Add, 589824),# units:Graphics  index:94    from 199 To 208
        SetMemory(0x664554, Add, 1560281088),# units:Graphics  index:95    from 114 To 207
        SetMemory(0x664558, Add, 7),# units:Graphics  index:96    from 200 To 207
        SetMemory(0x664560, Add, -2560),# units:Graphics  index:105    from 192 To 182
        SetMemory(0x6645C4, Add, -13312),# units:Graphics  index:205    from 173 To 121
        SetMemory(0x6645C4, Add, -3473408),# units:Graphics  index:206    from 174 To 121
        SetMemory(0x6645C8, Add, 1024),# units:Graphics  index:209    from 178 To 182
        SetMemory(0x660640, Add, -32),# units:Unit Direction  index:80    from 32 To 0
        SetMemory(0x660640, Add, -1900544),# units:Unit Direction  index:82    from 32 To 3
        SetMemory(0x660644, Add, -2097152),# units:Unit Direction  index:86    from 32 To 0
        SetMemory(0x660644, Add, -536870912),# units:Unit Direction  index:87    from 32 To 0
        SetMemory(0x660648, Add, -32),# units:Unit Direction  index:88    from 32 To 0
        SetMemory(0x660648, Add, -8192),# units:Unit Direction  index:89    from 32 To 0
        SetMemory(0x660648, Add, -2097152),# units:Unit Direction  index:90    from 32 To 0
        SetMemory(0x660648, Add, -536870912),# units:Unit Direction  index:91    from 32 To 0
        SetMemory(0x66064C, Add, -32),# units:Unit Direction  index:92    from 32 To 0
        SetMemory(0x66064C, Add, -8192),# units:Unit Direction  index:93    from 32 To 0
        SetMemory(0x66064C, Add, -2097152),# units:Unit Direction  index:94    from 32 To 0
        SetMemory(0x66064C, Add, -536870912),# units:Unit Direction  index:95    from 32 To 0
        SetMemory(0x660650, Add, -32),# units:Unit Direction  index:96    from 32 To 0
        SetMemory(0x660658, Add, 0),# units:Unit Direction  index:105    from 0 To 0
        SetMemory(0x6606C0, Add, 0),# units:Unit Direction  index:209    from 0 To 0
        SetMemory(0x6606C4, Add, 0),# units:Unit Direction  index:213    from 0 To 0
        SetMemory(0x664800, Add, -1),# units:Shield Enable  index:80    from 1 To 0
        SetMemory(0x664800, Add, -65536),# units:Shield Enable  index:82    from 1 To 0
        SetMemory(0x664804, Add, -65536),# units:Shield Enable  index:86    from 1 To 0
        SetMemory(0x664804, Add, -16777216),# units:Shield Enable  index:87    from 1 To 0
        SetMemory(0x664808, Add, -1),# units:Shield Enable  index:88    from 1 To 0
        SetMemory(0x660EA0, Add, -300),# units:Shield Amount  index:80    from 400 To 100
        SetMemory(0x660EA4, Add, -400),# units:Shield Amount  index:82    from 500 To 100
        SetMemory(0x660EAC, Add, -400),# units:Shield Amount  index:86    from 500 To 100
        SetMemory(0x660EAC, Add, -13107200),# units:Shield Amount  index:87    from 300 To 100
        SetMemory(0x660EB0, Add, -150),# units:Shield Amount  index:88    from 250 To 100
        SetMemory(0x662490, Add, 25497600),# units:Hit Points  index:80    from 102400 To 25600000
        SetMemory(0x662498, Add, 25395200),# units:Hit Points  index:82    from 204800 To 25600000
        SetMemory(0x6624A8, Add, -138240),# units:Hit Points  index:86    from 153600 To 15360
        SetMemory(0x6624AC, Add, -5120),# units:Hit Points  index:87    from 20480 To 15360
        SetMemory(0x6624B0, Add, -48640),# units:Hit Points  index:88    from 64000 To 15360
        SetMemory(0x6624BC, Add, -16640),# units:Hit Points  index:91    from 32000 To 15360
        SetMemory(0x6624C0, Add, -16640),# units:Hit Points  index:92    from 32000 To 15360
        SetMemory(0x6624F4, Add, -76800),# units:Hit Points  index:105    from 204800 To 128000
        SetMemory(0x662694, Add, 25587200),# units:Hit Points  index:209    from 12800 To 25600000
        SetMemory(0x6631A0, Add, -14),# units:Elevation Level  index:80    from 18 To 4
        SetMemory(0x6631A0, Add, -262144),# units:Elevation Level  index:82    from 16 To 12
        SetMemory(0x6631A4, Add, -262144),# units:Elevation Level  index:86    from 16 To 12
        SetMemory(0x6631A4, Add, 134217728),# units:Elevation Level  index:87    from 4 To 12
        SetMemory(0x6631A8, Add, -6),# units:Elevation Level  index:88    from 18 To 12
        SetMemory(0x6631A8, Add, 2560),# units:Elevation Level  index:89    from 4 To 14
        SetMemory(0x6631A8, Add, 524288),# units:Elevation Level  index:90    from 4 To 12
        SetMemory(0x6631A8, Add, -100663296),# units:Elevation Level  index:91    from 18 To 12
        SetMemory(0x6631AC, Add, -6),# units:Elevation Level  index:92    from 18 To 12
        SetMemory(0x6631AC, Add, 2048),# units:Elevation Level  index:93    from 4 To 12
        SetMemory(0x6631AC, Add, -393216),# units:Elevation Level  index:94    from 18 To 12
        SetMemory(0x6631AC, Add, 167772160),# units:Elevation Level  index:95    from 4 To 14
        SetMemory(0x6631B0, Add, 10),# units:Elevation Level  index:96    from 4 To 14
        SetMemory(0x6631B8, Add, -256),# units:Elevation Level  index:105    from 19 To 18
        SetMemory(0x66321C, Add, 2048),# units:Elevation Level  index:205    from 4 To 12
        SetMemory(0x66321C, Add, 524288),# units:Elevation Level  index:206    from 4 To 12
        SetMemory(0x663220, Add, 2048),# units:Elevation Level  index:209    from 4 To 12
        SetMemory(0x661018, Add, 0),# units:Unknown (old Movement)  index:80    from 197 To 197
        SetMemory(0x661018, Add, 0),# units:Unknown (old Movement)  index:82    from 197 To 197
        SetMemory(0x66101C, Add, -262144),# units:Unknown (old Movement)  index:86    from 197 To 193
        SetMemory(0x66101C, Add, 2147483648),# units:Unknown (old Movement)  index:87    from 65 To 193
        SetMemory(0x661020, Add, -4),# units:Unknown (old Movement)  index:88    from 197 To 193
        SetMemory(0x661020, Add, 32768),# units:Unknown (old Movement)  index:89    from 65 To 193
        SetMemory(0x661020, Add, 8388608),# units:Unknown (old Movement)  index:90    from 65 To 193
        SetMemory(0x661020, Add, 0),# units:Unknown (old Movement)  index:91    from 197 To 197
        SetMemory(0x661024, Add, -4),# units:Unknown (old Movement)  index:92    from 197 To 193
        SetMemory(0x661024, Add, 32768),# units:Unknown (old Movement)  index:93    from 65 To 193
        SetMemory(0x661024, Add, -262144),# units:Unknown (old Movement)  index:94    from 197 To 193
        SetMemory(0x661024, Add, 2147483648),# units:Unknown (old Movement)  index:95    from 65 To 193
        SetMemory(0x661028, Add, 128),# units:Unknown (old Movement)  index:96    from 65 To 193
        SetMemory(0x661030, Add, 50432),# units:Unknown (old Movement)  index:105    from 0 To 197
        SetMemory(0x663E20, Add, -12),# units:Rank/Sublabel  index:80    from 12 To 0
        SetMemory(0x663E20, Add, -1114112),# units:Rank/Sublabel  index:82    from 17 To 0
        SetMemory(0x663E24, Add, -720896),# units:Rank/Sublabel  index:86    from 12 To 1
        SetMemory(0x663E24, Add, -251658240),# units:Rank/Sublabel  index:87    from 16 To 1
        SetMemory(0x663E28, Add, -11),# units:Rank/Sublabel  index:88    from 12 To 1
        SetMemory(0x663E28, Add, 256),# units:Rank/Sublabel  index:89    from 0 To 1
        SetMemory(0x663E28, Add, 65536),# units:Rank/Sublabel  index:90    from 0 To 1
        SetMemory(0x663E28, Add, 16777216),# units:Rank/Sublabel  index:91    from 0 To 1
        SetMemory(0x663E2C, Add, 1),# units:Rank/Sublabel  index:92    from 0 To 1
        SetMemory(0x663E2C, Add, 256),# units:Rank/Sublabel  index:93    from 0 To 1
        SetMemory(0x663E2C, Add, 65536),# units:Rank/Sublabel  index:94    from 0 To 1
        SetMemory(0x663E2C, Add, 16777216),# units:Rank/Sublabel  index:95    from 0 To 1
        SetMemory(0x663E30, Add, 1),# units:Rank/Sublabel  index:96    from 0 To 1
        SetMemory(0x663E38, Add, 3584),# units:Rank/Sublabel  index:105    from 0 To 14
        SetMemory(0x662EF0, Add, 21),# units:Comp AI Idle  index:80    from 2 To 23
        SetMemory(0x662EF0, Add, -1769472),# units:Comp AI Idle  index:82    from 50 To 23
        SetMemory(0x662EF4, Add, -8388608),# units:Comp AI Idle  index:86    from 130 To 2
        SetMemory(0x662EF8, Add, -352321536),# units:Comp AI Idle  index:91    from 23 To 2
        SetMemory(0x662EFC, Add, -21),# units:Comp AI Idle  index:92    from 23 To 2
        SetMemory(0x662F08, Add, -5376),# units:Comp AI Idle  index:105    from 23 To 2
        SetMemory(0x662F70, Add, -36864),# units:Comp AI Idle  index:209    from 167 To 23
        SetMemory(0x6622B8, Add, 21),# units:Human AI Idle  index:80    from 2 To 23
        SetMemory(0x6622B8, Add, -1769472),# units:Human AI Idle  index:82    from 50 To 23
        SetMemory(0x6622BC, Add, -8388608),# units:Human AI Idle  index:86    from 130 To 2
        SetMemory(0x6622C0, Add, -41984),# units:Human AI Idle  index:89    from 166 To 2
        SetMemory(0x6622C0, Add, -10747904),# units:Human AI Idle  index:90    from 166 To 2
        SetMemory(0x6622C0, Add, -352321536),# units:Human AI Idle  index:91    from 23 To 2
        SetMemory(0x6622C4, Add, -21),# units:Human AI Idle  index:92    from 23 To 2
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -10747904),# units:Human AI Idle  index:94    from 166 To 2
        SetMemory(0x6622C4, Add, -2751463424),# units:Human AI Idle  index:95    from 166 To 2
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6622D0, Add, -5376),# units:Human AI Idle  index:105    from 23 To 2
        SetMemory(0x662338, Add, -36864),# units:Human AI Idle  index:209    from 167 To 23
        SetMemory(0x6648E8, Add, 21),# units:Return to Idle  index:80    from 2 To 23
        SetMemory(0x6648E8, Add, -1769472),# units:Return to Idle  index:82    from 50 To 23
        SetMemory(0x6648F0, Add, -41984),# units:Return to Idle  index:89    from 166 To 2
        SetMemory(0x6648F0, Add, -10747904),# units:Return to Idle  index:90    from 166 To 2
        SetMemory(0x6648F0, Add, -352321536),# units:Return to Idle  index:91    from 23 To 2
        SetMemory(0x6648F4, Add, -21),# units:Return to Idle  index:92    from 23 To 2
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -10747904),# units:Return to Idle  index:94    from 166 To 2
        SetMemory(0x6648F4, Add, -2751463424),# units:Return to Idle  index:95    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x664900, Add, -5376),# units:Return to Idle  index:105    from 23 To 2
        SetMemory(0x664968, Add, -36864),# units:Return to Idle  index:209    from 167 To 23
        SetMemory(0x663370, Add, 13),# units:Attack Unit  index:80    from 10 To 23
        SetMemory(0x663370, Add, -1966080),# units:Attack Unit  index:82    from 53 To 23
        SetMemory(0x663378, Add, -45568),# units:Attack Unit  index:89    from 188 To 10
        SetMemory(0x663378, Add, -11665408),# units:Attack Unit  index:90    from 188 To 10
        SetMemory(0x663378, Add, -218103808),# units:Attack Unit  index:91    from 23 To 10
        SetMemory(0x66337C, Add, -13),# units:Attack Unit  index:92    from 23 To 10
        SetMemory(0x66337C, Add, -45568),# units:Attack Unit  index:93    from 188 To 10
        SetMemory(0x66337C, Add, -11665408),# units:Attack Unit  index:94    from 188 To 10
        SetMemory(0x66337C, Add, -2986344448),# units:Attack Unit  index:95    from 188 To 10
        SetMemory(0x663380, Add, -178),# units:Attack Unit  index:96    from 188 To 10
        SetMemory(0x663388, Add, -3328),# units:Attack Unit  index:105    from 23 To 10
        SetMemory(0x6633F0, Add, 1024),# units:Attack Unit  index:209    from 19 To 23
        SetMemory(0x663AA0, Add, 21),# units:Attack Move  index:80    from 2 To 23
        SetMemory(0x663AA0, Add, -1769472),# units:Attack Move  index:82    from 50 To 23
        SetMemory(0x663AA8, Add, -47616),# units:Attack Move  index:89    from 188 To 2
        SetMemory(0x663AA8, Add, -12189696),# units:Attack Move  index:90    from 188 To 2
        SetMemory(0x663AA8, Add, -352321536),# units:Attack Move  index:91    from 23 To 2
        SetMemory(0x663AAC, Add, -21),# units:Attack Move  index:92    from 23 To 2
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -12189696),# units:Attack Move  index:94    from 188 To 2
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663AB8, Add, -5376),# units:Attack Move  index:105    from 23 To 2
        SetMemory(0x663708, Add, 55),# units:Ground Weapon  index:80    from 75 To 130
        SetMemory(0x66370C, Add, 3407872),# units:Ground Weapon  index:86    from 78 To 130
        SetMemory(0x66370C, Add, 1023410176),# units:Ground Weapon  index:87    from 69 To 130
        SetMemory(0x663710, Add, 16),# units:Ground Weapon  index:88    from 114 To 130
        SetMemory(0x663710, Add, 0),# units:Ground Weapon  index:90    from 130 To 130
        SetMemory(0x663710, Add, 0),# units:Ground Weapon  index:91    from 130 To 130
        SetMemory(0x663714, Add, 0),# units:Ground Weapon  index:92    from 130 To 130
        SetMemory(0x663714, Add, 0),# units:Ground Weapon  index:93    from 130 To 130
        SetMemory(0x663714, Add, 0),# units:Ground Weapon  index:94    from 130 To 130
        SetMemory(0x663714, Add, 0),# units:Ground Weapon  index:95    from 130 To 130
        SetMemory(0x663718, Add, -117),# units:Ground Weapon  index:96    from 130 To 13
        SetMemory(0x663720, Add, -28672),# units:Ground Weapon  index:105    from 130 To 18
        SetMemory(0x663788, Add, 8704),# units:Ground Weapon  index:209    from 96 To 130
        SetMemory(0x664630, Add, -1),# units:Max Ground Hits  index:80    from 1 To 0
        SetMemory(0x664634, Add, -65536),# units:Max Ground Hits  index:86    from 1 To 0
        SetMemory(0x664634, Add, -16777216),# units:Max Ground Hits  index:87    from 1 To 0
        SetMemory(0x664638, Add, -1),# units:Max Ground Hits  index:88    from 1 To 0
        SetMemory(0x664638, Add, 0),# units:Max Ground Hits  index:90    from 0 To 0
        SetMemory(0x664638, Add, 0),# units:Max Ground Hits  index:91    from 0 To 0
        SetMemory(0x66463C, Add, 0),# units:Max Ground Hits  index:92    from 0 To 0
        SetMemory(0x66463C, Add, 0),# units:Max Ground Hits  index:93    from 0 To 0
        SetMemory(0x66463C, Add, 0),# units:Max Ground Hits  index:94    from 0 To 0
        SetMemory(0x66463C, Add, 0),# units:Max Ground Hits  index:95    from 0 To 0
        SetMemory(0x664640, Add, 1),# units:Max Ground Hits  index:96    from 0 To 1
        SetMemory(0x664648, Add, 256),# units:Max Ground Hits  index:105    from 0 To 1
        SetMemory(0x6646B0, Add, -256),# units:Max Ground Hits  index:209    from 1 To 0
        SetMemory(0x661730, Add, 54),# units:Air Weapon  index:80    from 76 To 130
        SetMemory(0x661734, Add, 3407872),# units:Air Weapon  index:86    from 78 To 130
        SetMemory(0x661738, Add, 15),# units:Air Weapon  index:88    from 115 To 130
        SetMemory(0x661748, Add, -28928),# units:Air Weapon  index:105    from 130 To 17
        SetMemory(0x65FC68, Add, -1),# units:Max Air Hits  index:80    from 1 To 0
        SetMemory(0x65FC6C, Add, -65536),# units:Max Air Hits  index:86    from 1 To 0
        SetMemory(0x65FC70, Add, -1),# units:Max Air Hits  index:88    from 1 To 0
        SetMemory(0x65FC80, Add, 256),# units:Max Air Hits  index:105    from 0 To 1
        SetMemory(0x6601D0, Add, 50331648),# units:AI Internal  index:91    from 0 To 3
        SetMemory(0x6601D4, Add, 3),# units:AI Internal  index:92    from 0 To 3
        SetMemory(0x6641C0, Add, -1241514048),# units:Special Ability Flags  index:80    from 1509949508 To 268435460
        SetMemory(0x6641C8, Add, -738197568),# units:Special Ability Flags  index:82    from 1543503940 To 805306372
        SetMemory(0x6641D8, Add, -706740288),# units:Special Ability Flags  index:86    from 1512046660 To 805306372
        SetMemory(0x6641DC, Add, 400490436),# units:Special Ability Flags  index:87    from 404815936 To 805306372
        SetMemory(0x6641E0, Add, -704643136),# units:Special Ability Flags  index:88    from 1509949508 To 805306372
        SetMemory(0x6641E4, Add, 134152196),# units:Special Ability Flags  index:89    from 402718720 To 536870916
        SetMemory(0x6641E8, Add, 402587652),# units:Special Ability Flags  index:90    from 402718720 To 805306372
        SetMemory(0x6641EC, Add, 805306372),# units:Special Ability Flags  index:91    from 0 To 805306372
        SetMemory(0x6641F0, Add, 805306372),# units:Special Ability Flags  index:92    from 0 To 805306372
        SetMemory(0x6641F4, Add, 402587652),# units:Special Ability Flags  index:93    from 402718720 To 805306372
        SetMemory(0x6641F8, Add, 402587648),# units:Special Ability Flags  index:94    from 402718724 To 805306372
        SetMemory(0x6641FC, Add, 134152196),# units:Special Ability Flags  index:95    from 402718720 To 536870916
        SetMemory(0x664200, Add, 134152196),# units:Special Ability Flags  index:96    from 402718720 To 536870916
        SetMemory(0x664224, Add, 975176260),# units:Special Ability Flags  index:105    from 536870912 To 1512047172
        SetMemory(0x6643B4, Add, 4),# units:Special Ability Flags  index:205    from 536870912 To 536870916
        SetMemory(0x6643B8, Add, 4),# units:Special Ability Flags  index:206    from 536870912 To 536870916
        SetMemory(0x6643C4, Add, -872447996),# units:Special Ability Flags  index:209    from 1409318912 To 536870916
        SetMemory(0x662E08, Add, -4),# units:Target Acquisition Range  index:80    from 4 To 0
        SetMemory(0x662E08, Add, -524288),# units:Target Acquisition Range  index:82    from 8 To 0
        SetMemory(0x662E0C, Add, -262144),# units:Target Acquisition Range  index:86    from 5 To 1
        SetMemory(0x662E0C, Add, -33554432),# units:Target Acquisition Range  index:87    from 3 To 1
        SetMemory(0x662E10, Add, -3),# units:Target Acquisition Range  index:88    from 4 To 1
        SetMemory(0x662E10, Add, 256),# units:Target Acquisition Range  index:89    from 0 To 1
        SetMemory(0x662E10, Add, 65536),# units:Target Acquisition Range  index:90    from 0 To 1
        SetMemory(0x662E10, Add, -117440512),# units:Target Acquisition Range  index:91    from 8 To 1
        SetMemory(0x662E14, Add, -3),# units:Target Acquisition Range  index:92    from 4 To 1
        SetMemory(0x662E14, Add, 256),# units:Target Acquisition Range  index:93    from 0 To 1
        SetMemory(0x662E14, Add, 65536),# units:Target Acquisition Range  index:94    from 0 To 1
        SetMemory(0x662E14, Add, 16777216),# units:Target Acquisition Range  index:95    from 0 To 1
        SetMemory(0x662E18, Add, 1),# units:Target Acquisition Range  index:96    from 0 To 1
        SetMemory(0x662E20, Add, 1280),# units:Target Acquisition Range  index:105    from 0 To 5
        SetMemory(0x662E88, Add, -1280),# units:Target Acquisition Range  index:209    from 5 To 0
        SetMemory(0x663288, Add, -3),# units:Sight Range  index:80    from 10 To 7
        SetMemory(0x663288, Add, -131072),# units:Sight Range  index:82    from 9 To 7
        SetMemory(0x66328C, Add, -131072),# units:Sight Range  index:86    from 9 To 7
        SetMemory(0x663290, Add, -3),# units:Sight Range  index:88    from 10 To 7
        SetMemory(0x663290, Add, -16777216),# units:Sight Range  index:91    from 8 To 7
        SetMemory(0x6632A0, Add, -256),# units:Sight Range  index:105    from 8 To 7
        SetMemory(0x663304, Add, 1536),# units:Sight Range  index:205    from 1 To 7
        SetMemory(0x663304, Add, 393216),# units:Sight Range  index:206    from 1 To 7
        SetMemory(0x663308, Add, 256),# units:Sight Range  index:209    from 6 To 7
        SetMemory(0x663620, Add, 54),# units:Armor Upgrade  index:80    from 6 To 60
        SetMemory(0x663620, Add, 3538944),# units:Armor Upgrade  index:82    from 6 To 60
        SetMemory(0x663624, Add, -393216),# units:Armor Upgrade  index:86    from 6 To 0
        SetMemory(0x663624, Add, -83886080),# units:Armor Upgrade  index:87    from 5 To 0
        SetMemory(0x663628, Add, -6),# units:Armor Upgrade  index:88    from 6 To 0
        SetMemory(0x663628, Add, -15360),# units:Armor Upgrade  index:89    from 60 To 0
        SetMemory(0x663628, Add, -3932160),# units:Armor Upgrade  index:90    from 60 To 0
        SetMemory(0x663628, Add, -1006632960),# units:Armor Upgrade  index:91    from 60 To 0
        SetMemory(0x66362C, Add, -60),# units:Armor Upgrade  index:92    from 60 To 0
        SetMemory(0x66362C, Add, -15360),# units:Armor Upgrade  index:93    from 60 To 0
        SetMemory(0x66362C, Add, -3932160),# units:Armor Upgrade  index:94    from 60 To 0
        SetMemory(0x66362C, Add, -1006632960),# units:Armor Upgrade  index:95    from 60 To 0
        SetMemory(0x663630, Add, -60),# units:Armor Upgrade  index:96    from 60 To 0
        SetMemory(0x663638, Add, -14848),# units:Armor Upgrade  index:105    from 60 To 2
        SetMemory(0x6621D0, Add, -3),# units:Unit Size  index:80    from 3 To 0
        SetMemory(0x6621D0, Add, -196608),# units:Unit Size  index:82    from 3 To 0
        SetMemory(0x6621D4, Add, -196608),# units:Unit Size  index:86    from 3 To 0
        SetMemory(0x6621D4, Add, -16777216),# units:Unit Size  index:87    from 1 To 0
        SetMemory(0x6621D8, Add, -3),# units:Unit Size  index:88    from 3 To 0
        SetMemory(0x6621D8, Add, -256),# units:Unit Size  index:89    from 1 To 0
        SetMemory(0x6621D8, Add, -65536),# units:Unit Size  index:90    from 1 To 0
        SetMemory(0x6621D8, Add, -33554432),# units:Unit Size  index:91    from 2 To 0
        SetMemory(0x6621DC, Add, -2),# units:Unit Size  index:92    from 2 To 0
        SetMemory(0x6621DC, Add, -256),# units:Unit Size  index:93    from 1 To 0
        SetMemory(0x6621DC, Add, -65536),# units:Unit Size  index:94    from 1 To 0
        SetMemory(0x6621DC, Add, -16777216),# units:Unit Size  index:95    from 1 To 0
        SetMemory(0x6621E0, Add, -1),# units:Unit Size  index:96    from 1 To 0
        SetMemory(0x6621E8, Add, 768),# units:Unit Size  index:105    from 0 To 3
        SetMemory(0x662250, Add, -768),# units:Unit Size  index:209    from 3 To 0
        SetMemory(0x65FF18, Add, -3),# units:Armor  index:80    from 3 To 0
        SetMemory(0x65FF18, Add, -262144),# units:Armor  index:82    from 4 To 0
        SetMemory(0x65FF1C, Add, -196608),# units:Armor  index:86    from 3 To 0
        SetMemory(0x65FF1C, Add, -33554432),# units:Armor  index:87    from 2 To 0
        SetMemory(0x65FF20, Add, -3),# units:Armor  index:88    from 3 To 0
        SetMemory(0x65FF20, Add, -16777216),# units:Armor  index:91    from 1 To 0
        SetMemory(0x65FF24, Add, -1),# units:Armor  index:92    from 1 To 0
        SetMemory(0x65FF30, Add, 1024),# units:Armor  index:105    from 0 To 4
        SetMemory(0x6620E8, Add, 5),# units:Right-click Action  index:80    from 1 To 6
        SetMemory(0x6620E8, Add, 262144),# units:Right-click Action  index:82    from 1 To 5
        SetMemory(0x6620EC, Add, 262144),# units:Right-click Action  index:86    from 1 To 5
        SetMemory(0x6620EC, Add, 67108864),# units:Right-click Action  index:87    from 1 To 5
        SetMemory(0x6620F0, Add, 4),# units:Right-click Action  index:88    from 1 To 5
        SetMemory(0x6620F0, Add, 768),# units:Right-click Action  index:89    from 2 To 5
        SetMemory(0x6620F0, Add, 196608),# units:Right-click Action  index:90    from 2 To 5
        SetMemory(0x6620F0, Add, 83886080),# units:Right-click Action  index:91    from 0 To 5
        SetMemory(0x6620F4, Add, 5),# units:Right-click Action  index:92    from 0 To 5
        SetMemory(0x6620F4, Add, 768),# units:Right-click Action  index:93    from 2 To 5
        SetMemory(0x6620F4, Add, 196608),# units:Right-click Action  index:94    from 2 To 5
        SetMemory(0x6620F4, Add, 50331648),# units:Right-click Action  index:95    from 2 To 5
        SetMemory(0x6620F8, Add, 3),# units:Right-click Action  index:96    from 2 To 5
        SetMemory(0x662100, Add, 256),# units:Right-click Action  index:105    from 0 To 1
        SetMemory(0x66206C, Add, -549),# units:Ready Sound  index:86    from 549 To 0
        SetMemory(0x662074, Add, 0),# units:Ready Sound  index:91    from 0 To 0
        SetMemory(0x662090, Add, 16777216),# units:Ready Sound  index:105    from 0 To 256
        SetMemory(0x660050, Add, -510),# units:What Sound Start  index:80    from 540 To 30
        SetMemory(0x660054, Add, -677),# units:What Sound Start  index:82    from 707 To 30
        SetMemory(0x66005C, Add, -388),# units:What Sound Start  index:86    from 559 To 171
        SetMemory(0x66005C, Add, 11206656),# units:What Sound Start  index:87    from 0 To 171
        SetMemory(0x660060, Add, -965),# units:What Sound Start  index:88    from 1136 To 171
        SetMemory(0x660060, Add, 7667712),# units:What Sound Start  index:89    from 54 To 171
        SetMemory(0x660064, Add, 125),# units:What Sound Start  index:90    from 46 To 171
        SetMemory(0x660064, Add, 1966080),# units:What Sound Start  index:91    from 0 To 30
        SetMemory(0x660068, Add, 171),# units:What Sound Start  index:92    from 0 To 171
        SetMemory(0x660068, Add, -52494336),# units:What Sound Start  index:93    from 972 To 171
        SetMemory(0x66006C, Add, -805),# units:What Sound Start  index:94    from 976 To 171
        SetMemory(0x66006C, Add, 7602176),# units:What Sound Start  index:95    from 50 To 166
        SetMemory(0x660070, Add, -802),# units:What Sound Start  index:96    from 968 To 166
        SetMemory(0x660080, Add, 17367040),# units:What Sound Start  index:105    from 0 To 265
        SetMemory(0x660148, Add, 393216),# units:What Sound Start  index:205    from 24 To 30
        SetMemory(0x66014C, Add, 4),# units:What Sound Start  index:206    from 26 To 30
        SetMemory(0x660150, Add, 983040),# units:What Sound Start  index:209    from 15 To 30
        SetMemory(0x662C90, Add, -512),# units:What Sound End  index:80    from 543 To 31
        SetMemory(0x662C94, Add, -679),# units:What Sound End  index:82    from 710 To 31
        SetMemory(0x662C9C, Add, -391),# units:What Sound End  index:86    from 562 To 171
        SetMemory(0x662C9C, Add, 11206656),# units:What Sound End  index:87    from 0 To 171
        SetMemory(0x662CA0, Add, -968),# units:What Sound End  index:88    from 1139 To 171
        SetMemory(0x662CA0, Add, 7536640),# units:What Sound End  index:89    from 56 To 171
        SetMemory(0x662CA4, Add, 123),# units:What Sound End  index:90    from 48 To 171
        SetMemory(0x662CA4, Add, 2031616),# units:What Sound End  index:91    from 0 To 31
        SetMemory(0x662CA8, Add, 171),# units:What Sound End  index:92    from 0 To 171
        SetMemory(0x662CA8, Add, -52625408),# units:What Sound End  index:93    from 974 To 171
        SetMemory(0x662CAC, Add, -807),# units:What Sound End  index:94    from 978 To 171
        SetMemory(0x662CAC, Add, 7471104),# units:What Sound End  index:95    from 52 To 166
        SetMemory(0x662CB0, Add, -804),# units:What Sound End  index:96    from 970 To 166
        SetMemory(0x662CC0, Add, 17563648),# units:What Sound End  index:105    from 0 To 268
        SetMemory(0x662D88, Add, 393216),# units:What Sound End  index:205    from 25 To 31
        SetMemory(0x662D8C, Add, 4),# units:What Sound End  index:206    from 27 To 31
        SetMemory(0x662D90, Add, 1048576),# units:What Sound End  index:209    from 15 To 31
        SetMemory(0x663BE4, Add, -554),# units:Piss Sound Start  index:86    from 554 To 0
        SetMemory(0x663BE8, Add, -1130),# units:Piss Sound Start  index:88    from 1130 To 0
        SetMemory(0x663BEC, Add, 0),# units:Piss Sound Start  index:91    from 0 To 0
        SetMemory(0x663C08, Add, 16908288),# units:Piss Sound Start  index:105    from 0 To 258
        SetMemory(0x661F94, Add, -558),# units:Piss Sound End  index:86    from 558 To 0
        SetMemory(0x661F98, Add, -1135),# units:Piss Sound End  index:88    from 1135 To 0
        SetMemory(0x661F9C, Add, 0),# units:Piss Sound End  index:91    from 0 To 0
        SetMemory(0x661FB8, Add, 17301504),# units:Piss Sound End  index:105    from 0 To 264
        SetMemory(0x663CBC, Add, -563),# units:Yes Sound Start  index:86    from 563 To 0
        SetMemory(0x663CC0, Add, -1140),# units:Yes Sound Start  index:88    from 1140 To 0
        SetMemory(0x663CC4, Add, 0),# units:Yes Sound Start  index:91    from 0 To 0
        SetMemory(0x663CE0, Add, 17629184),# units:Yes Sound Start  index:105    from 0 To 269
        SetMemory(0x6614EC, Add, -565),# units:Yes Sound End  index:86    from 565 To 0
        SetMemory(0x6614F0, Add, -1143),# units:Yes Sound End  index:88    from 1143 To 0
        SetMemory(0x6614F4, Add, 0),# units:Yes Sound End  index:91    from 0 To 0
        SetMemory(0x661510, Add, 17825792),# units:Yes Sound End  index:105    from 0 To 272
        SetMemory(0x6629A0, Add, -35),# units:StarEdit Placement Box Width  index:80    from 36 To 1
        SetMemory(0x6629A8, Add, -63),# units:StarEdit Placement Box Width  index:82    from 64 To 1
        SetMemory(0x6629B8, Add, -43),# units:StarEdit Placement Box Width  index:86    from 44 To 1
        SetMemory(0x6629BC, Add, -23),# units:StarEdit Placement Box Width  index:87    from 24 To 1
        SetMemory(0x6629C0, Add, -35),# units:StarEdit Placement Box Width  index:88    from 36 To 1
        SetMemory(0x6629C4, Add, -31),# units:StarEdit Placement Box Width  index:89    from 32 To 1
        SetMemory(0x6629C8, Add, -31),# units:StarEdit Placement Box Width  index:90    from 32 To 1
        SetMemory(0x6629CC, Add, -31),# units:StarEdit Placement Box Width  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -31),# units:StarEdit Placement Box Width  index:92    from 32 To 1
        SetMemory(0x6629D4, Add, -31),# units:StarEdit Placement Box Width  index:93    from 32 To 1
        SetMemory(0x6629D8, Add, -31),# units:StarEdit Placement Box Width  index:94    from 32 To 1
        SetMemory(0x6629DC, Add, -31),# units:StarEdit Placement Box Width  index:95    from 32 To 1
        SetMemory(0x6629E0, Add, -31),# units:StarEdit Placement Box Width  index:96    from 32 To 1
        SetMemory(0x662A04, Add, -139),# units:StarEdit Placement Box Width  index:105    from 140 To 1
        SetMemory(0x662B94, Add, -135),# units:StarEdit Placement Box Width  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -135),# units:StarEdit Placement Box Width  index:206    from 136 To 1
        SetMemory(0x662BA4, Add, -63),# units:StarEdit Placement Box Width  index:209    from 64 To 1
        SetMemory(0x6629A0, Add, -2031616),# units:StarEdit Placement Box Height  index:80    from 32 To 1
        SetMemory(0x6629A8, Add, -4128768),# units:StarEdit Placement Box Height  index:82    from 64 To 1
        SetMemory(0x6629B8, Add, -2818048),# units:StarEdit Placement Box Height  index:86    from 44 To 1
        SetMemory(0x6629BC, Add, -1769472),# units:StarEdit Placement Box Height  index:87    from 28 To 1
        SetMemory(0x6629C0, Add, -2031616),# units:StarEdit Placement Box Height  index:88    from 32 To 1
        SetMemory(0x6629C4, Add, -2031616),# units:StarEdit Placement Box Height  index:89    from 32 To 1
        SetMemory(0x6629C8, Add, -2031616),# units:StarEdit Placement Box Height  index:90    from 32 To 1
        SetMemory(0x6629CC, Add, -2031616),# units:StarEdit Placement Box Height  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -2031616),# units:StarEdit Placement Box Height  index:92    from 32 To 1
        SetMemory(0x6629D4, Add, -2031616),# units:StarEdit Placement Box Height  index:93    from 32 To 1
        SetMemory(0x6629D8, Add, -2031616),# units:StarEdit Placement Box Height  index:94    from 32 To 1
        SetMemory(0x6629DC, Add, -2031616),# units:StarEdit Placement Box Height  index:95    from 32 To 1
        SetMemory(0x6629E0, Add, -2031616),# units:StarEdit Placement Box Height  index:96    from 32 To 1
        SetMemory(0x662A04, Add, -6488064),# units:StarEdit Placement Box Height  index:105    from 100 To 1
        SetMemory(0x662B1C, Add, -4194304),# units:StarEdit Placement Box Height  index:175    from 128 To 64
        SetMemory(0x662B94, Add, -8847360),# units:StarEdit Placement Box Height  index:205    from 136 To 1
        SetMemory(0x662B98, Add, -8847360),# units:StarEdit Placement Box Height  index:206    from 136 To 1
        SetMemory(0x662BA4, Add, -4128768),# units:StarEdit Placement Box Height  index:209    from 64 To 1
        SetMemory(0x661A48, Add, -18),# units:Unit Size Left  index:80    from 18 To 0
        SetMemory(0x661A58, Add, -32),# units:Unit Size Left  index:82    from 32 To 0
        SetMemory(0x661A78, Add, -21),# units:Unit Size Left  index:86    from 22 To 1
        SetMemory(0x661A80, Add, -11),# units:Unit Size Left  index:87    from 12 To 1
        SetMemory(0x661A88, Add, -17),# units:Unit Size Left  index:88    from 18 To 1
        SetMemory(0x661A90, Add, -15),# units:Unit Size Left  index:89    from 16 To 1
        SetMemory(0x661A98, Add, -15),# units:Unit Size Left  index:90    from 16 To 1
        SetMemory(0x661AA0, Add, -14),# units:Unit Size Left  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -14),# units:Unit Size Left  index:92    from 15 To 1
        SetMemory(0x661AB0, Add, -15),# units:Unit Size Left  index:93    from 16 To 1
        SetMemory(0x661AB8, Add, -15),# units:Unit Size Left  index:94    from 16 To 1
        SetMemory(0x661AC0, Add, -14),# units:Unit Size Left  index:95    from 16 To 2
        SetMemory(0x661AC8, Add, -14),# units:Unit Size Left  index:96    from 16 To 2
        SetMemory(0x661B10, Add, -60),# units:Unit Size Left  index:105    from 60 To 0
        SetMemory(0x661E30, Add, -25),# units:Unit Size Left  index:205    from 25 To 0
        SetMemory(0x661E38, Add, -44),# units:Unit Size Left  index:206    from 44 To 0
        SetMemory(0x661E50, Add, -32),# units:Unit Size Left  index:209    from 32 To 0
        SetMemory(0x661A48, Add, -983040),# units:Unit Size Up  index:80    from 16 To 1
        SetMemory(0x661A58, Add, -2031616),# units:Unit Size Up  index:82    from 32 To 1
        SetMemory(0x661A78, Add, -1376256),# units:Unit Size Up  index:86    from 22 To 1
        SetMemory(0x661A80, Add, -851968),# units:Unit Size Up  index:87    from 14 To 1
        SetMemory(0x661A88, Add, -983040),# units:Unit Size Up  index:88    from 16 To 1
        SetMemory(0x661A90, Add, -983040),# units:Unit Size Up  index:89    from 16 To 1
        SetMemory(0x661A98, Add, -983040),# units:Unit Size Up  index:90    from 16 To 1
        SetMemory(0x661AA0, Add, -917504),# units:Unit Size Up  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -917504),# units:Unit Size Up  index:92    from 15 To 1
        SetMemory(0x661AB0, Add, -983040),# units:Unit Size Up  index:93    from 16 To 1
        SetMemory(0x661AB8, Add, -983040),# units:Unit Size Up  index:94    from 16 To 1
        SetMemory(0x661AC0, Add, -917504),# units:Unit Size Up  index:95    from 16 To 2
        SetMemory(0x661AC8, Add, -917504),# units:Unit Size Up  index:96    from 16 To 2
        SetMemory(0x661B10, Add, -2555904),# units:Unit Size Up  index:105    from 40 To 1
        SetMemory(0x661E30, Add, -1048576),# units:Unit Size Up  index:205    from 17 To 1
        SetMemory(0x661E38, Add, -1048576),# units:Unit Size Up  index:206    from 17 To 1
        SetMemory(0x661E50, Add, -2031616),# units:Unit Size Up  index:209    from 32 To 1
        SetMemory(0x661A4C, Add, -17),# units:Unit Size Right  index:80    from 17 To 0
        SetMemory(0x661A5C, Add, -31),# units:Unit Size Right  index:82    from 31 To 0
        SetMemory(0x661A7C, Add, -20),# units:Unit Size Right  index:86    from 21 To 1
        SetMemory(0x661A84, Add, -10),# units:Unit Size Right  index:87    from 11 To 1
        SetMemory(0x661A8C, Add, -16),# units:Unit Size Right  index:88    from 17 To 1
        SetMemory(0x661A94, Add, -14),# units:Unit Size Right  index:89    from 15 To 1
        SetMemory(0x661A9C, Add, -14),# units:Unit Size Right  index:90    from 15 To 1
        SetMemory(0x661AA4, Add, -15),# units:Unit Size Right  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -15),# units:Unit Size Right  index:92    from 16 To 1
        SetMemory(0x661AB4, Add, -14),# units:Unit Size Right  index:93    from 15 To 1
        SetMemory(0x661ABC, Add, -14),# units:Unit Size Right  index:94    from 15 To 1
        SetMemory(0x661AC4, Add, -13),# units:Unit Size Right  index:95    from 15 To 2
        SetMemory(0x661ACC, Add, -13),# units:Unit Size Right  index:96    from 15 To 2
        SetMemory(0x661B14, Add, -59),# units:Unit Size Right  index:105    from 59 To 0
        SetMemory(0x661E34, Add, -44),# units:Unit Size Right  index:205    from 44 To 0
        SetMemory(0x661E3C, Add, -25),# units:Unit Size Right  index:206    from 25 To 0
        SetMemory(0x661E54, Add, -31),# units:Unit Size Right  index:209    from 31 To 0
        SetMemory(0x661A4C, Add, -917504),# units:Unit Size Down  index:80    from 15 To 1
        SetMemory(0x661A5C, Add, -1966080),# units:Unit Size Down  index:82    from 31 To 1
        SetMemory(0x661A7C, Add, -1310720),# units:Unit Size Down  index:86    from 21 To 1
        SetMemory(0x661A84, Add, -786432),# units:Unit Size Down  index:87    from 13 To 1
        SetMemory(0x661A8C, Add, -917504),# units:Unit Size Down  index:88    from 15 To 1
        SetMemory(0x661A94, Add, -917504),# units:Unit Size Down  index:89    from 15 To 1
        SetMemory(0x661A9C, Add, -917504),# units:Unit Size Down  index:90    from 15 To 1
        SetMemory(0x661AA4, Add, -983040),# units:Unit Size Down  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -983040),# units:Unit Size Down  index:92    from 16 To 1
        SetMemory(0x661AB4, Add, -917504),# units:Unit Size Down  index:93    from 15 To 1
        SetMemory(0x661ABC, Add, -917504),# units:Unit Size Down  index:94    from 15 To 1
        SetMemory(0x661AC4, Add, -851968),# units:Unit Size Down  index:95    from 15 To 2
        SetMemory(0x661ACC, Add, -851968),# units:Unit Size Down  index:96    from 15 To 2
        SetMemory(0x661B14, Add, -2555904),# units:Unit Size Down  index:105    from 39 To 0
        SetMemory(0x661D44, Add, -2031616),# units:Unit Size Down  index:175    from 63 To 32
        SetMemory(0x661E34, Add, -1245184),# units:Unit Size Down  index:205    from 20 To 1
        SetMemory(0x661E3C, Add, -1245184),# units:Unit Size Down  index:206    from 20 To 1
        SetMemory(0x661E54, Add, -1966080),# units:Unit Size Down  index:209    from 31 To 1
        SetMemory(0x663028, Add, 65490),# units:Portrait  index:80    from 45 To 65535
        SetMemory(0x66302C, Add, 65481),# units:Portrait  index:82    from 54 To 65535
        SetMemory(0x663034, Add, 33),# units:Portrait  index:86    from 46 To 79
        SetMemory(0x663034, Add, 1310720),# units:Portrait  index:87    from 59 To 79
        SetMemory(0x663038, Add, -16),# units:Portrait  index:88    from 95 To 79
        SetMemory(0x663038, Add, 1114112),# units:Portrait  index:89    from 62 To 79
        SetMemory(0x66303C, Add, 16),# units:Portrait  index:90    from 63 To 79
        SetMemory(0x66303C, Add, -4289724416),# units:Portrait  index:91    from 65535 To 79
        SetMemory(0x663040, Add, -65456),# units:Portrait  index:92    from 65535 To 79
        SetMemory(0x663040, Add, -1441792),# units:Portrait  index:93    from 101 To 79
        SetMemory(0x663044, Add, -23),# units:Portrait  index:94    from 102 To 79
        SetMemory(0x663044, Add, 983040),# units:Portrait  index:95    from 64 To 79
        SetMemory(0x663048, Add, -24),# units:Portrait  index:96    from 103 To 79
        SetMemory(0x663058, Add, -4294377472),# units:Portrait  index:105    from 65535 To 8
        SetMemory(0x663888, Add, -1638400),# units:Mineral Cost  index:1    from 25 To 0
        SetMemory(0x663928, Add, -599),# units:Mineral Cost  index:80    from 600 To 1
        SetMemory(0x66392C, Add, -699),# units:Mineral Cost  index:82    from 700 To 1
        SetMemory(0x663934, Add, -3276800),# units:Mineral Cost  index:87    from 100 To 50
        SetMemory(0x663938, Add, -600),# units:Mineral Cost  index:88    from 600 To 0
        SetMemory(0x663938, Add, -65536),# units:Mineral Cost  index:89    from 1 To 0
        SetMemory(0x66393C, Add, -1),# units:Mineral Cost  index:90    from 1 To 0
        SetMemory(0x66393C, Add, -6553600),# units:Mineral Cost  index:91    from 100 To 0
        SetMemory(0x663940, Add, -100),# units:Mineral Cost  index:92    from 100 To 0
        SetMemory(0x663940, Add, -65536),# units:Mineral Cost  index:93    from 1 To 0
        SetMemory(0x663944, Add, -1),# units:Mineral Cost  index:94    from 1 To 0
        SetMemory(0x663944, Add, 3211264),# units:Mineral Cost  index:95    from 1 To 50
        SetMemory(0x663948, Add, 49),# units:Mineral Cost  index:96    from 1 To 50
        SetMemory(0x663958, Add, 9830400),# units:Mineral Cost  index:105    from 250 To 400
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FDA0, Add, -299),# units:Vespene Cost  index:80    from 300 To 1
        SetMemory(0x65FDA4, Add, -599),# units:Vespene Cost  index:82    from 600 To 1
        SetMemory(0x65FDAC, Add, -1000),# units:Vespene Cost  index:86    from 1000 To 0
        SetMemory(0x65FDAC, Add, -19660800),# units:Vespene Cost  index:87    from 300 To 0
        SetMemory(0x65FDB0, Add, -300),# units:Vespene Cost  index:88    from 300 To 0
        SetMemory(0x65FDB0, Add, -65536),# units:Vespene Cost  index:89    from 1 To 0
        SetMemory(0x65FDB4, Add, -1),# units:Vespene Cost  index:90    from 1 To 0
        SetMemory(0x65FDB4, Add, -6553600),# units:Vespene Cost  index:91    from 100 To 0
        SetMemory(0x65FDB8, Add, -100),# units:Vespene Cost  index:92    from 100 To 0
        SetMemory(0x65FDB8, Add, -65536),# units:Vespene Cost  index:93    from 1 To 0
        SetMemory(0x65FDBC, Add, -1),# units:Vespene Cost  index:94    from 1 To 0
        SetMemory(0x65FDBC, Add, -65536),# units:Vespene Cost  index:95    from 1 To 0
        SetMemory(0x65FDC0, Add, -1),# units:Vespene Cost  index:96    from 1 To 0
        SetMemory(0x65FDD0, Add, -3276800),# units:Vespene Cost  index:105    from 250 To 200
        SetMemory(0x660428, Add, -49086464),# units:Build Time  index:1    from 750 To 1
        SetMemory(0x6604C8, Add, -2399),# units:Build Time  index:80    from 2400 To 1
        SetMemory(0x6604CC, Add, -4199),# units:Build Time  index:82    from 4200 To 1
        SetMemory(0x6604D4, Add, -4500),# units:Build Time  index:86    from 4800 To 300
        SetMemory(0x6604D4, Add, -78643200),# units:Build Time  index:87    from 1500 To 300
        SetMemory(0x6604D8, Add, -2399),# units:Build Time  index:88    from 2400 To 1
        SetMemory(0x6604D8, Add, 0),# units:Build Time  index:89    from 1 To 1
        SetMemory(0x6604DC, Add, 0),# units:Build Time  index:90    from 1 To 1
        SetMemory(0x6604DC, Add, -39256064),# units:Build Time  index:91    from 600 To 1
        SetMemory(0x6604E0, Add, -599),# units:Build Time  index:92    from 600 To 1
        SetMemory(0x6604E0, Add, 0),# units:Build Time  index:93    from 1 To 1
        SetMemory(0x6604E4, Add, 0),# units:Build Time  index:94    from 1 To 1
        SetMemory(0x6604E4, Add, 19595264),# units:Build Time  index:95    from 1 To 300
        SetMemory(0x6604E8, Add, 299),# units:Build Time  index:96    from 1 To 300
        SetMemory(0x6604F8, Add, -39321600),# units:Build Time  index:105    from 2400 To 1800
        SetMemory(0x6637F0, Add, -2),# units:Staredit Group Flags  index:80    from 12 To 10
        SetMemory(0x6637F0, Add, 7602176),# units:Staredit Group Flags  index:82    from 12 To 128
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F4, Add, -33554432),# units:Staredit Group Flags  index:87    from 12 To 10
        SetMemory(0x6637F8, Add, -2),# units:Staredit Group Flags  index:88    from 12 To 10
        SetMemory(0x6637F8, Add, -32256),# units:Staredit Group Flags  index:89    from 136 To 10
        SetMemory(0x6637F8, Add, -8257536),# units:Staredit Group Flags  index:90    from 136 To 10
        SetMemory(0x6637F8, Add, 16777216),# units:Staredit Group Flags  index:91    from 9 To 10
        SetMemory(0x6637FC, Add, 1),# units:Staredit Group Flags  index:92    from 9 To 10
        SetMemory(0x6637FC, Add, -32256),# units:Staredit Group Flags  index:93    from 136 To 10
        SetMemory(0x6637FC, Add, -8257536),# units:Staredit Group Flags  index:94    from 136 To 10
        SetMemory(0x6637FC, Add, -134217728),# units:Staredit Group Flags  index:95    from 136 To 128
        SetMemory(0x663800, Add, -8),# units:Staredit Group Flags  index:96    from 136 To 128
        SetMemory(0x663808, Add, -30208),# units:Staredit Group Flags  index:105    from 128 To 10
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663D40, Add, 0),# units:Supply Required  index:91    from 0 To 0
        SetMemory(0x664464, Add, -16711680),# units:Space Required  index:86    from 255 To 0
        SetMemory(0x664464, Add, -33554432),# units:Space Required  index:87    from 2 To 0
        SetMemory(0x664468, Add, -255),# units:Space Required  index:88    from 255 To 0
        SetMemory(0x664468, Add, -65280),# units:Space Required  index:89    from 255 To 0
        SetMemory(0x664468, Add, -16711680),# units:Space Required  index:90    from 255 To 0
        SetMemory(0x664468, Add, -4278190080),# units:Space Required  index:91    from 255 To 0
        SetMemory(0x66446C, Add, -255),# units:Space Required  index:92    from 255 To 0
        SetMemory(0x66446C, Add, -65280),# units:Space Required  index:93    from 255 To 0
        SetMemory(0x66446C, Add, -16711680),# units:Space Required  index:94    from 255 To 0
        SetMemory(0x66446C, Add, -4278190080),# units:Space Required  index:95    from 255 To 0
        SetMemory(0x664470, Add, -255),# units:Space Required  index:96    from 255 To 0
        SetMemory(0x6634B4, Add, 50),# units:Build Score  index:86    from 0 To 50
        SetMemory(0x6634B4, Add, 3276800),# units:Build Score  index:87    from 0 To 50
        SetMemory(0x6634B8, Add, 50),# units:Build Score  index:88    from 0 To 50
        SetMemory(0x6634B8, Add, 3276800),# units:Build Score  index:89    from 0 To 50
        SetMemory(0x6634BC, Add, 50),# units:Build Score  index:90    from 0 To 50
        SetMemory(0x6634BC, Add, 3276800),# units:Build Score  index:91    from 0 To 50
        SetMemory(0x6634C0, Add, 50),# units:Build Score  index:92    from 0 To 50
        SetMemory(0x6634C0, Add, 3276800),# units:Build Score  index:93    from 0 To 50
        SetMemory(0x6634C4, Add, 50),# units:Build Score  index:94    from 0 To 50
        SetMemory(0x6634C4, Add, 3276800),# units:Build Score  index:95    from 0 To 50
        SetMemory(0x6634C8, Add, 50),# units:Build Score  index:96    from 0 To 50
        SetMemory(0x663F58, Add, -2590),# units:Destroy Score  index:80    from 2600 To 10
        SetMemory(0x663F5C, Add, -3790),# units:Destroy Score  index:82    from 3800 To 10
        SetMemory(0x663F64, Add, -4000),# units:Destroy Score  index:86    from 4100 To 100
        SetMemory(0x663F64, Add, -85196800),# units:Destroy Score  index:87    from 1400 To 100
        SetMemory(0x663F68, Add, -2300),# units:Destroy Score  index:88    from 2400 To 100
        SetMemory(0x663F68, Add, 5898240),# units:Destroy Score  index:89    from 10 To 100
        SetMemory(0x663F6C, Add, 90),# units:Destroy Score  index:90    from 10 To 100
        SetMemory(0x663F6C, Add, 6553600),# units:Destroy Score  index:91    from 0 To 100
        SetMemory(0x663F70, Add, 100),# units:Destroy Score  index:92    from 0 To 100
        SetMemory(0x663F70, Add, 5898240),# units:Destroy Score  index:93    from 10 To 100
        SetMemory(0x663F74, Add, 90),# units:Destroy Score  index:94    from 10 To 100
        SetMemory(0x663F74, Add, 5898240),# units:Destroy Score  index:95    from 10 To 100
        SetMemory(0x663F78, Add, 90),# units:Destroy Score  index:96    from 10 To 100
        SetMemory(0x663F88, Add, 104857600),# units:Destroy Score  index:105    from 0 To 1600
        SetMemory(0x664058, Add, -5898240),# units:Destroy Score  index:209    from 100 To 10
        SetMemory(0x660730, Add, -1),# units:Broodwar Unit Flag  index:88    from 1 To 0
        SetMemory(0x660734, Add, -256),# units:Broodwar Unit Flag  index:93    from 1 To 0
        SetMemory(0x660734, Add, -65536),# units:Broodwar Unit Flag  index:94    from 1 To 0
        SetMemory(0x660738, Add, -1),# units:Broodwar Unit Flag  index:96    from 1 To 0
        SetMemory(0x6615B8, Add, 520),# units:Staredit Availability Flags  index:80    from 455 To 975
        SetMemory(0x6615BC, Add, 516),# units:Staredit Availability Flags  index:82    from 455 To 971
        SetMemory(0x6615C4, Add, 520),# units:Staredit Availability Flags  index:86    from 455 To 975
        SetMemory(0x6615C4, Add, 63635456),# units:Staredit Availability Flags  index:87    from 4 To 975
        SetMemory(0x6615C8, Add, 8),# units:Staredit Availability Flags  index:88    from 967 To 975
        SetMemory(0x6615C8, Add, 34144256),# units:Staredit Availability Flags  index:89    from 454 To 975
        SetMemory(0x6615CC, Add, 521),# units:Staredit Availability Flags  index:90    from 454 To 975
        SetMemory(0x6615CC, Add, 29818880),# units:Staredit Availability Flags  index:91    from 0 To 455
        SetMemory(0x6615D0, Add, 975),# units:Staredit Availability Flags  index:92    from 0 To 975
        SetMemory(0x6615D0, Add, 589824),# units:Staredit Availability Flags  index:93    from 966 To 975
        SetMemory(0x6615D4, Add, 9),# units:Staredit Availability Flags  index:94    from 966 To 975
        SetMemory(0x6615D4, Add, 29949952),# units:Staredit Availability Flags  index:95    from 454 To 911
        SetMemory(0x6615D8, Add, -55),# units:Staredit Availability Flags  index:96    from 966 To 911
        SetMemory(0x6615E8, Add, 29818880),# units:Staredit Availability Flags  index:105    from 0 To 455
        SetMemory(0x6616B0, Add, 48955392),# units:Staredit Availability Flags  index:205    from 32 To 779
        SetMemory(0x6616B4, Add, 747),# units:Staredit Availability Flags  index:206    from 32 To 779
        SetMemory(0x6616B8, Add, 48955392),# units:Staredit Availability Flags  index:209    from 32 To 779
        SetMemory(0x656CB0, Add, 0),# weapons:Graphics  index:2    from 143 To 143
        SetMemory(0x6CA484, Add, -65536),# flingy:Sprite  index:183    from 307 To 306
        SetMemory(0x6CA1D0, Add, 1),# flingy:Speed  index:182    from 0 To 1
        SetMemory(0x6C9DE4, Add, 1),# flingy:Acceleration  index:182    from 0 To 1
        SetMemory(0x6C9C08, Add, 1),# flingy:Halt Distance  index:182    from 0 To 1
        SetMemory(0x6C9E74, Add, -2621440),# flingy:Turn Radius  index:86    from 40 To 0
        SetMemory(0x6C9ED4, Add, 65536),# flingy:Turn Radius  index:182    from 0 To 1
        SetMemory(0x6C9EF0, Add, 10),# flingy:Turn Radius  index:208    from 0 To 10
        SetMemory(0x6C990C, Add, 0),# flingy:Movement Control  index:182    from 2 To 2
        SetMemory(0x6C990C, Add, -16777216),# flingy:Movement Control  index:183    from 2 To 1
        SetMemory(0x6C9928, Add, -2),# flingy:Movement Control  index:208    from 2 To 0
        SetMemory(0x66634C, Add, 65),# sprites:Image File  index:246    from 260 To 325
        SetMemory(0x666394, Add, 522),# sprites:Image File  index:282    from 353 To 875
        SetMemory(0x6663C4, Add, 0),# sprites:Image File  index:306    from 740 To 740
        SetMemory(0x6663C4, Add, -65536),# sprites:Image File  index:307    from 741 To 740
        SetMemory(0x666564, Add, -62717952),# sprites:Image File  index:515    from 958 To 1
        SetMemory(0x66E860, Add, -256),# images:Gfx Turns  index:1    from 1 To 0
        SetMemory(0x66E930, Add, 65536),# images:Gfx Turns  index:210    from 0 To 1
        SetMemory(0x66E934, Add, 16777216),# images:Gfx Turns  index:215    from 0 To 1
        SetMemory(0x66E964, Add, 16777216),# images:Gfx Turns  index:263    from 0 To 1
        SetMemory(0x66E968, Add, 65536),# images:Gfx Turns  index:266    from 0 To 1
        SetMemory(0x66E980, Add, 65536),# images:Gfx Turns  index:290    from 0 To 1
        SetMemory(0x66E994, Add, 256),# images:Gfx Turns  index:309    from 0 To 1
        SetMemory(0x66E9A4, Add, 0),# images:Gfx Turns  index:325    from 0 To 0
        SetMemory(0x66E9AC, Add, 65536),# images:Gfx Turns  index:334    from 0 To 1
        SetMemory(0x66E9B0, Add, 256),# images:Gfx Turns  index:337    from 0 To 1
        SetMemory(0x66E9CC, Add, 16777216),# images:Gfx Turns  index:367    from 0 To 1
        SetMemory(0x66EA04, Add, -1),# images:Gfx Turns  index:420    from 1 To 0
        SetMemory(0x66EA74, Add, 256),# images:Gfx Turns  index:533    from 0 To 1
        SetMemory(0x66EA80, Add, 1),# images:Gfx Turns  index:544    from 0 To 1
        SetMemory(0x66EAA8, Add, 0),# images:Gfx Turns  index:584    from 0 To 0
        SetMemory(0x66EB10, Add, 0),# images:Gfx Turns  index:689    from 0 To 0
        SetMemory(0x66EB40, Add, 65536),# images:Gfx Turns  index:738    from 0 To 1
        SetMemory(0x66EB44, Add, 1),# images:Gfx Turns  index:740    from 0 To 1
        SetMemory(0x66EB44, Add, 256),# images:Gfx Turns  index:741    from 0 To 1
        SetMemory(0x66EB4C, Add, 65536),# images:Gfx Turns  index:750    from 0 To 1
        SetMemory(0x66EBA8, Add, 256),# images:Gfx Turns  index:841    from 0 To 1
        SetMemory(0x66EBDC, Add, 0),# images:Gfx Turns  index:895    from 0 To 0
        SetMemory(0x66EBFC, Add, 256),# images:Gfx Turns  index:925    from 0 To 1
        SetMemory(0x66C150, Add, 256),# images:Clickable  index:1    from 0 To 1
        SetMemory(0x66C2E4, Add, 0),# images:Clickable  index:407    from 0 To 0
        SetMemory(0x66C39C, Add, 256),# images:Clickable  index:589    from 0 To 1
        SetMemory(0x66C39C, Add, 16777216),# images:Clickable  index:591    from 0 To 1
        SetMemory(0x66C3A0, Add, 256),# images:Clickable  index:593    from 0 To 1
        SetMemory(0x66C3A0, Add, 16777216),# images:Clickable  index:595    from 0 To 1
        SetMemory(0x66C3A4, Add, 256),# images:Clickable  index:597    from 0 To 1
        SetMemory(0x66C3A8, Add, 256),# images:Clickable  index:601    from 0 To 1
        SetMemory(0x66C3A8, Add, 65536),# images:Clickable  index:602    from 0 To 1
        SetMemory(0x66C3A8, Add, 16777216),# images:Clickable  index:603    from 0 To 1
        SetMemory(0x66C3AC, Add, 1),# images:Clickable  index:604    from 0 To 1
        SetMemory(0x66C3AC, Add, 256),# images:Clickable  index:605    from 0 To 1
        SetMemory(0x66C3AC, Add, 65536),# images:Clickable  index:606    from 0 To 1
        SetMemory(0x66C3B0, Add, 65536),# images:Clickable  index:610    from 0 To 1
        SetMemory(0x66C3B4, Add, 1),# images:Clickable  index:612    from 0 To 1
        SetMemory(0x66C3B4, Add, 65536),# images:Clickable  index:614    from 0 To 1
        SetMemory(0x66C3B8, Add, 1),# images:Clickable  index:616    from 0 To 1
        SetMemory(0x66C3B8, Add, 65536),# images:Clickable  index:618    from 0 To 1
        SetMemory(0x66C3BC, Add, 1),# images:Clickable  index:620    from 0 To 1
        SetMemory(0x66C3BC, Add, 65536),# images:Clickable  index:622    from 0 To 1
        SetMemory(0x66C3C0, Add, 1),# images:Clickable  index:624    from 0 To 1
        SetMemory(0x66C3C0, Add, 65536),# images:Clickable  index:626    from 0 To 1
        SetMemory(0x66C3C4, Add, 1),# images:Clickable  index:628    from 0 To 1
        SetMemory(0x66C3C4, Add, 65536),# images:Clickable  index:630    from 0 To 1
        SetMemory(0x66C3C8, Add, 1),# images:Clickable  index:632    from 0 To 1
        SetMemory(0x66C3C8, Add, 65536),# images:Clickable  index:634    from 0 To 1
        SetMemory(0x66C3CC, Add, 1),# images:Clickable  index:636    from 0 To 1
        SetMemory(0x66C3CC, Add, 65536),# images:Clickable  index:638    from 0 To 1
        SetMemory(0x66C3D0, Add, 1),# images:Clickable  index:640    from 0 To 1
        SetMemory(0x66C3D0, Add, 65536),# images:Clickable  index:642    from 0 To 1
        SetMemory(0x66C3D0, Add, 16777216),# images:Clickable  index:643    from 0 To 1
        SetMemory(0x66C3D4, Add, 1),# images:Clickable  index:644    from 0 To 1
        SetMemory(0x66C3D4, Add, 16777216),# images:Clickable  index:647    from 0 To 1
        SetMemory(0x66C3D8, Add, 1),# images:Clickable  index:648    from 0 To 1
        SetMemory(0x66C3DC, Add, 65536),# images:Clickable  index:654    from 0 To 1
        SetMemory(0x66C3DC, Add, 16777216),# images:Clickable  index:655    from 0 To 1
        SetMemory(0x66C3E0, Add, 65536),# images:Clickable  index:658    from 0 To 1
        SetMemory(0x66C3F0, Add, 16777216),# images:Clickable  index:675    from 0 To 1
        SetMemory(0x66C3F4, Add, 256),# images:Clickable  index:677    from 0 To 1
        SetMemory(0x66C3F4, Add, 65536),# images:Clickable  index:678    from 0 To 1
        SetMemory(0x66C400, Add, 1),# images:Clickable  index:688    from 0 To 1
        SetMemory(0x66C400, Add, 256),# images:Clickable  index:689    from 0 To 1
        SetMemory(0x66C404, Add, 256),# images:Clickable  index:693    from 0 To 1
        SetMemory(0x66C408, Add, 16777216),# images:Clickable  index:699    from 0 To 1
        SetMemory(0x66C40C, Add, 1),# images:Clickable  index:700    from 0 To 1
        SetMemory(0x66C40C, Add, 256),# images:Clickable  index:701    from 0 To 1
        SetMemory(0x66C40C, Add, 65536),# images:Clickable  index:702    from 0 To 1
        SetMemory(0x66C418, Add, 1),# images:Clickable  index:712    from 0 To 1
        SetMemory(0x66C418, Add, 256),# images:Clickable  index:713    from 0 To 1
        SetMemory(0x66C418, Add, 65536),# images:Clickable  index:714    from 0 To 1
        SetMemory(0x66C418, Add, 16777216),# images:Clickable  index:715    from 0 To 1
        SetMemory(0x66C41C, Add, 1),# images:Clickable  index:716    from 0 To 1
        SetMemory(0x66C41C, Add, 256),# images:Clickable  index:717    from 0 To 1
        SetMemory(0x66C41C, Add, 65536),# images:Clickable  index:718    from 0 To 1
        SetMemory(0x66C41C, Add, 16777216),# images:Clickable  index:719    from 0 To 1
        SetMemory(0x66C420, Add, 1),# images:Clickable  index:720    from 0 To 1
        SetMemory(0x66C420, Add, 256),# images:Clickable  index:721    from 0 To 1
        SetMemory(0x66C420, Add, 65536),# images:Clickable  index:722    from 0 To 1
        SetMemory(0x66C434, Add, 65536),# images:Clickable  index:742    from 0 To 1
        SetMemory(0x66C43C, Add, 65536),# images:Clickable  index:750    from 0 To 1
        SetMemory(0x66C498, Add, 256),# images:Clickable  index:841    from 0 To 1
        SetMemory(0x66C4A0, Add, 16777216),# images:Clickable  index:851    from 0 To 1
        SetMemory(0x66C4A4, Add, 1),# images:Clickable  index:852    from 0 To 1
        SetMemory(0x66C4A4, Add, 65536),# images:Clickable  index:854    from 0 To 1
        SetMemory(0x66C4A8, Add, 1),# images:Clickable  index:856    from 0 To 1
        SetMemory(0x66C4A8, Add, 65536),# images:Clickable  index:858    from 0 To 1
        SetMemory(0x66C4AC, Add, 1),# images:Clickable  index:860    from 0 To 1
        SetMemory(0x66C4B4, Add, 1),# images:Clickable  index:868    from 0 To 1
        SetMemory(0x66C4B4, Add, 16777216),# images:Clickable  index:871    from 0 To 1
        SetMemory(0x66C4B8, Add, 1),# images:Clickable  index:872    from 0 To 1
        SetMemory(0x66C4BC, Add, 65536),# images:Clickable  index:878    from 0 To 1
        SetMemory(0x66C4C0, Add, 16777216),# images:Clickable  index:883    from 0 To 1
        SetMemory(0x66C4C8, Add, 256),# images:Clickable  index:889    from 0 To 1
        SetMemory(0x66C4C8, Add, 65536),# images:Clickable  index:890    from 0 To 1
        SetMemory(0x66C4CC, Add, 1),# images:Clickable  index:892    from 0 To 1
        SetMemory(0x66C4CC, Add, 65536),# images:Clickable  index:894    from 0 To 1
        SetMemory(0x66C4CC, Add, 16777216),# images:Clickable  index:895    from 0 To 1
        SetMemory(0x66C4D0, Add, 65536),# images:Clickable  index:898    from 0 To 1
        SetMemory(0x66D7BC, Add, -1),# images:Use Full Iscript  index:740    from 1 To 0
        SetMemory(0x66D7BC, Add, -256),# images:Use Full Iscript  index:741    from 1 To 0
        SetMemory(0x66D7C4, Add, -65536),# images:Use Full Iscript  index:750    from 1 To 0
        SetMemory(0x667718, Add, 256),# images:Draw If Cloaked  index:1    from 0 To 1
        SetMemory(0x669E28, Add, -2048),# images:Draw Function  index:1    from 10 To 2
        SetMemory(0x669EB4, Add, -256),# images:Draw Function  index:141    from 10 To 9
        SetMemory(0x66A10C, Add, -1),# images:Draw Function  index:740    from 1 To 0
        SetMemory(0x66A18C, Add, -134217728),# images:Draw Function  index:871    from 10 To 2
        SetMemory(0x66A190, Add, 83886080),# images:Draw Function  index:875    from 10 To 15
        SetMemory(0x66A19C, Add, 2560),# images:Draw Function  index:885    from 0 To 10
        SetMemory(0x66F15C, Add, 85),# images:Iscript ID  index:325    from 138 To 223
        SetMemory(0x66F2A4, Add, 35),# images:Iscript ID  index:407    from 215 To 250
        SetMemory(0x66F2D8, Add, -48),# images:Iscript ID  index:420    from 272 To 224
        SetMemory(0x66F800, Add, -117),# images:Iscript ID  index:750    from 340 To 223
    ])

