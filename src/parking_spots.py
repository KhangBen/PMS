# polyline drawing order : top-left -> top-right -> bottom-right -> bottom->left

parking_spots = [
  {
    "polygon": [(144, 615), (243, 608), (237, 638), (132, 641)],       # row 1
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(253, 609), (345, 604), (344, 633), (248, 638)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(353, 604), (446, 602), (456, 630), (355, 633)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(451, 600), (543, 599), (563, 629), (466, 629)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(552, 598), (648, 593), (672, 621), (571, 623)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(654, 591), (742, 586), (774, 614), (679, 617)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(748, 586), (829, 582), (876, 610), (781, 613)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(840, 581), (931, 580), (974, 603), (886, 606)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(943, 578), (1028, 576), (1071, 599), (986, 603)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1037, 576), (1117, 572), (1168, 596), (1085, 598)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },

  { 
    "polygon": [(85, 699), (212, 701), (197, 756), (58, 761)],          # row 2
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(228, 696), (341, 694), (345, 752), (211, 754)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(355, 692), (467, 685), (489, 743), (357, 750)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(485, 686), (593, 679), (634, 735), (504, 741)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(608, 676), (720, 676), (775, 729), (653, 735)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(739, 679), (850, 673), (918, 724), (794, 732)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(866, 671), (982, 663), (1054, 715), (938, 722)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(994, 659), (1099, 652), (1168, 708), (1066, 714)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1117, 654), (1208, 652), (1291, 698), (1190, 707)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1224, 652), (1329, 646), (1420, 690), (1309, 697)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1342, 642), (1430, 634), (1531, 678), (1438, 688)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },

  { 
    "polygon": [(50, 769), (190, 767), (173, 841), (12, 847)],          # row 3
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(207, 767), (344, 761), (353, 834), (189, 841)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(357, 761), (494, 754), (521, 826), (365, 835)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(506, 754), (641, 747), (696, 818), (537, 828)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(657, 747), (786, 739), (855, 809), (710, 817)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(800, 740), (930, 733), (1018, 798), (870, 807)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(944, 732), (1063, 724), (1170, 787), (1033, 797)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1078, 726), (1188, 716), (1319, 775), (1182, 785)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1202, 713), (1313, 706), (1448, 762), (1331, 774)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1331, 705), (1437, 697), (1577, 749), (1465, 761)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1452, 697), (1549, 687), (1708, 734), (1596, 748)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },

  {
    "polygon": [(1, 1023), (124, 1023), (113, 1076), (2, 1074)],       # row 4
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(135,1022), (362, 1012), (363, 1076), (128, 1074)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(370,1012), (586, 999), (616, 1075), (375, 1074)], 
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(597, 996), (805, 980), (876, 1075), (633, 1076)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(821, 977), (1028, 954), (1133, 1073), (894, 1074)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1041, 953), (1221, 932), (1400, 1075), (1153, 1074)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1245, 933), (1402, 909), (1589, 1050), (1432, 1075)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1424, 914), (1609, 894), (1817, 1018), (1603, 1043)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  },
  {
    "polygon": [(1628, 897), (1741, 888), (1920, 1001), (1833, 1017)],
    "counter": 0,
    "last_seen": 0,
    "occupied": False
  }
  #,
  # {
  #   "polygon": [(1641, 627), (1727, 620), (1821, 645), (1718, 658)],
  #   "counter": 0,
  #   "last_seen": 0,
  #   "occupied": False
  # }

]




