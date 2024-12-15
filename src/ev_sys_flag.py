from enum import IntEnum, auto

class EvSysFlag(IntEnum):
    SYS_FLAG_ARRIVE_START = 0
    SYS_FLAG_BAG_GET = auto()
    SYS_FLAG_PAIR = auto()
    SYS_FLAG_KAIRIKI = auto()
    SYS_FLAG_FNOTE_GET = auto()
    SYS_FLAG_GAME_CLEAR = auto()
    SYS_FLAG_ONE_STEP = auto()
    SYS_FLAG_COMM_COUNTER = auto()
    SYS_FLAG_SAFARI_MODE = auto()
    SYS_FLAG_CON_STYLE_MASTER = auto()
    SYS_FLAG_CON_BEAUTIFUL_MASTER = auto()
    SYS_FLAG_CON_CUTE_MASTER = auto()
    SYS_FLAG_CON_CLEVER_MASTER = auto()
    SYS_FLAG_CON_STRONG_MASTER = auto()
    SYS_FLAG_BTL_SEARCHER_USE = auto()
    SYS_FLAG_UG_ARRIVE = auto()
    SYS_FLAG_UG_DIG = auto()
    SYS_FLAG_UG_TAMA = auto()
    SYS_FLAG_UG_BASE = auto()
    SYS_FLAG_UG_GOODS = auto()
    SYS_FLAG_UG_HATA = auto()
    SYS_FLAG_GTC_OPEN = auto()
    SYS_FLAG_BTOWER_OPEN = auto()
    SYS_FLAG_SHIP = auto()
    SYS_FLAG_PST = auto()
    SYS_FLAG_POKEPARK_MODE = auto()
    SYS_FLAG_FLASH = auto()
    SYS_FLAG_KIRIBARAI = auto()
    SYS_FLAG_POKETCH_HOOK = auto()
    SYS_FLAG_REIAIHAI = auto()
    SYS_FLAG_MIZUKI = auto()
    SYS_FLAG_BS_LV1 = auto()
    SYS_FLAG_BS_LV2 = auto()
    SYS_FLAG_BS_LV3 = auto()
    SYS_FLAG_BS_LV4 = auto()
    SYS_FLAG_BS_LV5 = auto()
    SYS_FLAG_BGM_D28 = auto()
    SYS_FLAG_BGM_GINGA = auto()
    SYS_FLAG_BGM_D26 = auto()
    SYS_FLAG_BGM_C04 = auto()
    SYS_FLAG_BGM_D02 = auto()
    SYS_FLAG_BGM_D13 = auto()
    SYS_FLAG_BGM_R224 = auto()
    SYS_FLAG_BGM_C10 = auto()
    SYS_FLAG_WIFI_USE = auto()
    SYS_FLAG_T05_GINGA_EVENT = auto()
    SYS_FLAG_BGM_D27 = auto()
    SYS_FLAG_BGM_D29 = auto()
    SYS_FLAG_BGM_D16 = auto()
    SYS_FLAG_BGM_C02 = auto()
    SYS_FLAG_UG_FIRST = auto()
    SYS_FLAG_BGM_T02 = auto()
    SYS_FLAG_CYCLINGROAD = auto()
    SYS_FLAG_BGM_D10 = auto()
    OLD_FLAG_ARRIVE_T01 = auto()
    OLD_FLAG_ARRIVE_T02 = auto()
    OLD_FLAG_ARRIVE_T03 = auto()
    OLD_FLAG_ARRIVE_T04 = auto()
    OLD_FLAG_ARRIVE_T05 = auto()
    OLD_FLAG_ARRIVE_T06 = auto()
    OLD_FLAG_ARRIVE_T07 = auto()
    OLD_FLAG_ARRIVE_C01 = auto()
    OLD_FLAG_ARRIVE_C02 = auto()
    OLD_FLAG_ARRIVE_C03 = auto()
    OLD_FLAG_ARRIVE_C04 = auto()
    OLD_FLAG_ARRIVE_C05 = auto()
    OLD_FLAG_ARRIVE_C06 = auto()
    OLD_FLAG_ARRIVE_C07 = auto()
    OLD_FLAG_ARRIVE_C08 = auto()
    OLD_FLAG_ARRIVE_C09 = auto()
    OLD_FLAG_ARRIVE_C10 = auto()
    OLD_FLAG_ARRIVE_C11 = auto()
    OLD_FLAG_ARRIVE_D01R0101 = auto()
    OLD_FLAG_ARRIVE_D02R0101 = auto()
    OLD_FLAG_ARRIVE_D03 = auto()
    OLD_FLAG_ARRIVE_D04R0101 = auto()
    OLD_FLAG_ARRIVE_D05 = auto()
    OLD_FLAG_ARRIVE_D05R0114 = auto()
    OLD_FLAG_ARRIVE_D06 = auto()
    OLD_FLAG_ARRIVE_D07R0102 = auto()
    OLD_FLAG_ARRIVE_D09R0101 = auto()
    OLD_FLAG_ARRIVE_D10R0101 = auto()
    OLD_FLAG_ARRIVE_D11R0101 = auto()
    OLD_FLAG_ARRIVE_D12R0101 = auto()
    OLD_FLAG_ARRIVE_D13R0101 = auto()
    OLD_FLAG_ARRIVE_D14R0101 = auto()
    OLD_FLAG_ARRIVE_D15 = auto()
    OLD_FLAG_ARRIVE_D16 = auto()
    OLD_FLAG_ARRIVE_D16R0101 = auto()
    OLD_FLAG_ARRIVE_D17 = auto()
    OLD_FLAG_ARRIVE_D17R0102 = auto()
    OLD_FLAG_ARRIVE_D18 = auto()
    OLD_FLAG_ARRIVE_D20R0101 = auto()
    OLD_FLAG_ARRIVE_D21R0101 = auto()
    OLD_FLAG_ARRIVE_D22R0101 = auto()
    OLD_FLAG_ARRIVE_D23R0101 = auto()
    OLD_FLAG_ARRIVE_D24 = auto()
    OLD_FLAG_ARRIVE_D24R0101 = auto()
    OLD_FLAG_ARRIVE_D25R0101 = auto()
    OLD_FLAG_ARRIVE_D26R0101 = auto()
    OLD_FLAG_ARRIVE_D27 = auto()
    OLD_FLAG_ARRIVE_D27R0103 = auto()
    OLD_FLAG_ARRIVE_D28 = auto()
    OLD_FLAG_ARRIVE_D28R0103 = auto()
    OLD_FLAG_ARRIVE_D29 = auto()
    OLD_FLAG_ARRIVE_D29R0103 = auto()
    OLD_FLAG_ARRIVE_D30 = auto()
    OLD_FLAG_ARRIVE_C11R0101 = auto()
    OLD_FLAG_ARRIVE_R206 = auto()
    OLD_FLAG_ARRIVE_R208R0101 = auto()
    OLD_FLAG_ARRIVE_R209R0101 = auto()
    OLD_FLAG_ARRIVE_R210AR0101 = auto()
    OLD_FLAG_ARRIVE_R210BR0101 = auto()
    OLD_FLAG_ARRIVE_R212AR0101 = auto()
    OLD_FLAG_ARRIVE_R212BR0101 = auto()
    OLD_FLAG_ARRIVE_R213R0201 = auto()
    OLD_FLAG_ARRIVE_L02R0101 = auto()
    OLD_FLAG_ARRIVE_R222R0101 = auto()
    OLD_FLAG_ARRIVE_R222R0201 = auto()
    OLD_FLAG_ARRIVE_W226R0101 = auto()
    OLD_FLAG_ARRIVE_R221 = auto()
    OLD_FLAG_ARRIVE_R221R0101 = auto()
    OLD_FLAG_ARRIVE_CHAMPLEAGUE = auto()
    OLD_FLAG_ARRIVE_MAX = auto()
    BADGE_ID_C03 = auto()
    BADGE_ID_C04 = auto()
    BADGE_ID_C07 = auto()
    BADGE_ID_C06 = auto()
    BADGE_ID_C05 = auto()
    BADGE_ID_C02 = auto()
    BADGE_ID_C09 = auto()
    BADGE_ID_C08 = auto()
    BADGE_MAX = auto()
    FIRST_SAVE = auto()
    FLAG_ARRIVE_C01 = auto()
    FLAG_ARRIVE_C01FS0101 = auto()
    FLAG_ARRIVE_C01PC0101 = auto()
    FLAG_ARRIVE_C01PC0102 = auto()
    FLAG_ARRIVE_C01PC0103 = auto()
    FLAG_ARRIVE_C01R0101 = auto()
    FLAG_ARRIVE_C01R0102 = auto()
    FLAG_ARRIVE_C01R0103 = auto()
    FLAG_ARRIVE_C01R0201 = auto()
    FLAG_ARRIVE_C01R0202 = auto()
    FLAG_ARRIVE_C01R0203 = auto()
    FLAG_ARRIVE_C01R0204 = auto()
    FLAG_ARRIVE_C01R0205 = auto()
    FLAG_ARRIVE_C01R0206 = auto()
    FLAG_ARRIVE_C01R0207 = auto()
    FLAG_ARRIVE_C01R0208 = auto()
    FLAG_ARRIVE_C01R0301 = auto()
    FLAG_ARRIVE_C01R0302 = auto()
    FLAG_ARRIVE_C01R0501 = auto()
    FLAG_ARRIVE_C01R0502 = auto()
    FLAG_ARRIVE_C01R0601 = auto()
    FLAG_ARRIVE_C01R0701 = auto()
    FLAG_ARRIVE_C01R0801 = auto()
    FLAG_ARRIVE_C01R0802 = auto()
    FLAG_ARRIVE_C02 = auto()
    FLAG_ARRIVE_C02FS0101 = auto()
    FLAG_ARRIVE_C02GYM0101 = auto()
    FLAG_ARRIVE_C02PC0101 = auto()
    FLAG_ARRIVE_C02PC0102 = auto()
    FLAG_ARRIVE_C02PC0103 = auto()
    FLAG_ARRIVE_C02R0101 = auto()
    FLAG_ARRIVE_C02R0102 = auto()
    FLAG_ARRIVE_C02R0103 = auto()
    FLAG_ARRIVE_C02R0201 = auto()
    FLAG_ARRIVE_C02R0301 = auto()
    FLAG_ARRIVE_C02R0401 = auto()
    FLAG_ARRIVE_C02R0501 = auto()
    FLAG_ARRIVE_C02R0601 = auto()
    FLAG_ARRIVE_C03 = auto()
    FLAG_ARRIVE_C03FS0101 = auto()
    FLAG_ARRIVE_C03GYM0101 = auto()
    FLAG_ARRIVE_C03PC0101 = auto()
    FLAG_ARRIVE_C03PC0102 = auto()
    FLAG_ARRIVE_C03PC0103 = auto()
    FLAG_ARRIVE_C03R0101 = auto()
    FLAG_ARRIVE_C03R0102 = auto()
    FLAG_ARRIVE_C03R0201 = auto()
    FLAG_ARRIVE_C03R0202 = auto()
    FLAG_ARRIVE_C03R0301 = auto()
    FLAG_ARRIVE_C03R0401 = auto()
    FLAG_ARRIVE_C03R0501 = auto()
    FLAG_ARRIVE_C03R0601 = auto()
    FLAG_ARRIVE_C03R0602 = auto()
    FLAG_ARRIVE_C03R0701 = auto()
    FLAG_ARRIVE_C04 = auto()
    FLAG_ARRIVE_C04FS0101 = auto()
    FLAG_ARRIVE_C04GYM0101 = auto()
    FLAG_ARRIVE_C04GYM0102 = auto()
    FLAG_ARRIVE_C04PC0101 = auto()
    FLAG_ARRIVE_C04PC0102 = auto()
    FLAG_ARRIVE_C04PC0103 = auto()
    FLAG_ARRIVE_C04R0101 = auto()
    FLAG_ARRIVE_C04R0201 = auto()
    FLAG_ARRIVE_C04R0202 = auto()
    FLAG_ARRIVE_C04R0203 = auto()
    FLAG_ARRIVE_C04R0204 = auto()
    FLAG_ARRIVE_C04R0301 = auto()
    FLAG_ARRIVE_C04R0302 = auto()
    FLAG_ARRIVE_C04R0303 = auto()
    FLAG_ARRIVE_C04R0401 = auto()
    FLAG_ARRIVE_C04R0501 = auto()
    FLAG_ARRIVE_C04R0601 = auto()
    FLAG_ARRIVE_C04R0701 = auto()
    FLAG_ARRIVE_C04R0801 = auto()
    FLAG_ARRIVE_C05 = auto()
    FLAG_ARRIVE_C05FS0101 = auto()
    FLAG_ARRIVE_C05GYM0101 = auto()
    FLAG_ARRIVE_C05GYM0102 = auto()
    FLAG_ARRIVE_C05GYM0103 = auto()
    FLAG_ARRIVE_C05GYM0104 = auto()
    FLAG_ARRIVE_C05GYM0105 = auto()
    FLAG_ARRIVE_C05GYM0106 = auto()
    FLAG_ARRIVE_C05GYM0107 = auto()
    FLAG_ARRIVE_C05GYM0108 = auto()
    FLAG_ARRIVE_C05GYM0109 = auto()
    FLAG_ARRIVE_C05GYM0110 = auto()
    FLAG_ARRIVE_C05GYM0111 = auto()
    FLAG_ARRIVE_C05GYM0112 = auto()
    FLAG_ARRIVE_C05GYM0113 = auto()
    FLAG_ARRIVE_C05PC0101 = auto()
    FLAG_ARRIVE_C05PC0102 = auto()
    FLAG_ARRIVE_C05PC0103 = auto()
    FLAG_ARRIVE_C05R0101 = auto()
    FLAG_ARRIVE_C05R0102 = auto()
    FLAG_ARRIVE_C05R0103 = auto()
    FLAG_ARRIVE_C05R0201 = auto()
    FLAG_ARRIVE_C05R0301 = auto()
    FLAG_ARRIVE_C05R0401 = auto()
    FLAG_ARRIVE_C05R0501 = auto()
    FLAG_ARRIVE_C05R0601 = auto()
    FLAG_ARRIVE_C05R0701 = auto()
    FLAG_ARRIVE_C05R0801 = auto()
    FLAG_ARRIVE_C05R0802 = auto()
    FLAG_ARRIVE_C05R0803 = auto()
    FLAG_ARRIVE_C05R0901 = auto()
    FLAG_ARRIVE_C05R1001 = auto()
    FLAG_ARRIVE_C05R1101 = auto()
    FLAG_ARRIVE_C05R1102 = auto()
    FLAG_ARRIVE_C05R1103 = auto()
    FLAG_ARRIVE_C05R1201 = auto()
    FLAG_ARRIVE_C06 = auto()
    FLAG_ARRIVE_C06FS0101 = auto()
    FLAG_ARRIVE_C06GYM0101 = auto()
    FLAG_ARRIVE_C06PC0101 = auto()
    FLAG_ARRIVE_C06PC0102 = auto()
    FLAG_ARRIVE_C06PC0103 = auto()
    FLAG_ARRIVE_C06R0101 = auto()
    FLAG_ARRIVE_C06R0102 = auto()
    FLAG_ARRIVE_C06R0201 = auto()
    FLAG_ARRIVE_C06R0301 = auto()
    FLAG_ARRIVE_C06R0401 = auto()
    FLAG_ARRIVE_C06R0501 = auto()
    FLAG_ARRIVE_C06R0601 = auto()
    FLAG_ARRIVE_C07 = auto()
    FLAG_ARRIVE_C07GYM0101 = auto()
    FLAG_ARRIVE_C07PC0101 = auto()
    FLAG_ARRIVE_C07PC0102 = auto()
    FLAG_ARRIVE_C07PC0103 = auto()
    FLAG_ARRIVE_C07R0101 = auto()
    FLAG_ARRIVE_C07R0201 = auto()
    FLAG_ARRIVE_C07R0202 = auto()
    FLAG_ARRIVE_C07R0203 = auto()
    FLAG_ARRIVE_C07R0204 = auto()
    FLAG_ARRIVE_C07R0205 = auto()
    FLAG_ARRIVE_C07R0206 = auto()
    FLAG_ARRIVE_C07R0301 = auto()
    FLAG_ARRIVE_C07R0401 = auto()
    FLAG_ARRIVE_C07R0501 = auto()
    FLAG_ARRIVE_C07R0601 = auto()
    FLAG_ARRIVE_C07R0701 = auto()
    FLAG_ARRIVE_C07R0801 = auto()
    FLAG_ARRIVE_C07R0901 = auto()
    FLAG_ARRIVE_C08 = auto()
    FLAG_ARRIVE_C08FS0101 = auto()
    FLAG_ARRIVE_C08GYM0101 = auto()
    FLAG_ARRIVE_C08GYM0102 = auto()
    FLAG_ARRIVE_C08GYM0103 = auto()
    FLAG_ARRIVE_C08PC0101 = auto()
    FLAG_ARRIVE_C08PC0102 = auto()
    FLAG_ARRIVE_C08PC0103 = auto()
    FLAG_ARRIVE_C08R0101 = auto()
    FLAG_ARRIVE_C08R0201 = auto()
    FLAG_ARRIVE_C08R0301 = auto()
    FLAG_ARRIVE_C08R0401 = auto()
    FLAG_ARRIVE_C08R0501 = auto()
    FLAG_ARRIVE_C08R0601 = auto()
    FLAG_ARRIVE_C08R0701 = auto()
    FLAG_ARRIVE_C08R0801 = auto()
    FLAG_ARRIVE_C08R0802 = auto()
    FLAG_ARRIVE_C09 = auto()
    FLAG_ARRIVE_C09FS0101 = auto()
    FLAG_ARRIVE_C09GYM0101 = auto()
    FLAG_ARRIVE_C09PC0101 = auto()
    FLAG_ARRIVE_C09PC0102 = auto()
    FLAG_ARRIVE_C09PC0103 = auto()
    FLAG_ARRIVE_C09R0101 = auto()
    FLAG_ARRIVE_C09R0201 = auto()
    FLAG_ARRIVE_C10 = auto()
    FLAG_ARRIVE_C10PC0101 = auto()
    FLAG_ARRIVE_C10PC0102 = auto()
    FLAG_ARRIVE_C10PC0103 = auto()
    FLAG_ARRIVE_C10R0101 = auto()
    FLAG_ARRIVE_C10R0102 = auto()
    FLAG_ARRIVE_C10R0103 = auto()
    FLAG_ARRIVE_C10R0104 = auto()
    FLAG_ARRIVE_C10R0105 = auto()
    FLAG_ARRIVE_C10R0106 = auto()
    FLAG_ARRIVE_C10R0107 = auto()
    FLAG_ARRIVE_C10R0108 = auto()
    FLAG_ARRIVE_C10R0109 = auto()
    FLAG_ARRIVE_C10R0110 = auto()
    FLAG_ARRIVE_C10R0111 = auto()
    FLAG_ARRIVE_C10R0112 = auto()
    FLAG_ARRIVE_C10R0113 = auto()
    FLAG_ARRIVE_C10R0114 = auto()
    FLAG_ARRIVE_C10R0115 = auto()
    FLAG_ARRIVE_C11 = auto()
    FLAG_ARRIVE_C11FS0101 = auto()
    FLAG_ARRIVE_C11PC0101 = auto()
    FLAG_ARRIVE_C11PC0102 = auto()
    FLAG_ARRIVE_C11PC0103 = auto()
    FLAG_ARRIVE_C11R0101 = auto()
    FLAG_ARRIVE_C11R0201 = auto()
    FLAG_ARRIVE_C11R0301 = auto()
    FLAG_ARRIVE_C11R0401 = auto()
    FLAG_ARRIVE_D01R0101 = auto()
    FLAG_ARRIVE_D01R0102 = auto()
    FLAG_ARRIVE_D02 = auto()
    FLAG_ARRIVE_D02R0101 = auto()
    FLAG_ARRIVE_D03 = auto()
    FLAG_ARRIVE_D03R0101 = auto()
    FLAG_ARRIVE_D04 = auto()
    FLAG_ARRIVE_D04R0101 = auto()
    FLAG_ARRIVE_D05R0101 = auto()
    FLAG_ARRIVE_D05R0102 = auto()
    FLAG_ARRIVE_D05R0103 = auto()
    FLAG_ARRIVE_D05R0104 = auto()
    FLAG_ARRIVE_D05R0105 = auto()
    FLAG_ARRIVE_D05R0106 = auto()
    FLAG_ARRIVE_D05R0107 = auto()
    FLAG_ARRIVE_D05R0108 = auto()
    FLAG_ARRIVE_D05R0109 = auto()
    FLAG_ARRIVE_D05R0110 = auto()
    FLAG_ARRIVE_D05R0111 = auto()
    FLAG_ARRIVE_D05R0112 = auto()
    FLAG_ARRIVE_D05R0113 = auto()
    FLAG_ARRIVE_D05R0114 = auto()
    FLAG_ARRIVE_D05R0115 = auto()
    FLAG_ARRIVE_D05R0116 = auto()
    FLAG_ARRIVE_D06R0201 = auto()
    FLAG_ARRIVE_D06R0202 = auto()
    FLAG_ARRIVE_D06R0203 = auto()
    FLAG_ARRIVE_D06R0204 = auto()
    FLAG_ARRIVE_D06R0205 = auto()
    FLAG_ARRIVE_D06R0206 = auto()
    FLAG_ARRIVE_D07R0101 = auto()
    FLAG_ARRIVE_D07R0102 = auto()
    FLAG_ARRIVE_D07R0103 = auto()
    FLAG_ARRIVE_D07R0104 = auto()
    FLAG_ARRIVE_D07R0105 = auto()
    FLAG_ARRIVE_D07R0106 = auto()
    FLAG_ARRIVE_D07R0107 = auto()
    FLAG_ARRIVE_D07R0108 = auto()
    FLAG_ARRIVE_D07R0109 = auto()
    FLAG_ARRIVE_D07R0110 = auto()
    FLAG_ARRIVE_D07R0111 = auto()
    FLAG_ARRIVE_D07R0112 = auto()
    FLAG_ARRIVE_D07R0113 = auto()
    FLAG_ARRIVE_D07R0114 = auto()
    FLAG_ARRIVE_D07R0115 = auto()
    FLAG_ARRIVE_D07R0116 = auto()
    FLAG_ARRIVE_D07R0117 = auto()
    FLAG_ARRIVE_D07R0118 = auto()
    FLAG_ARRIVE_D07R0119 = auto()
    FLAG_ARRIVE_D09R0101 = auto()
    FLAG_ARRIVE_D09R0102 = auto()
    FLAG_ARRIVE_D09R0103 = auto()
    FLAG_ARRIVE_D09R0104 = auto()
    FLAG_ARRIVE_D09R0105 = auto()
    FLAG_ARRIVE_D09R0106 = auto()
    FLAG_ARRIVE_D10R0101 = auto()
    FLAG_ARRIVE_D11R0101 = auto()
    FLAG_ARRIVE_D12R0101 = auto()
    FLAG_ARRIVE_D13R0101 = auto()
    FLAG_ARRIVE_D13R0102 = auto()
    FLAG_ARRIVE_D14R0101 = auto()
    FLAG_ARRIVE_D14R0102 = auto()
    FLAG_ARRIVE_D15 = auto()
    FLAG_ARRIVE_D15R0101 = auto()
    FLAG_ARRIVE_D16 = auto()
    FLAG_ARRIVE_D16R0101 = auto()
    FLAG_ARRIVE_D16R0102 = auto()
    FLAG_ARRIVE_D16R0103 = auto()
    FLAG_ARRIVE_D17R0101 = auto()
    FLAG_ARRIVE_D17R0102 = auto()
    FLAG_ARRIVE_D17R0103 = auto()
    FLAG_ARRIVE_D17R0104 = auto()
    FLAG_ARRIVE_D17R0105 = auto()
    FLAG_ARRIVE_D17R0106 = auto()
    FLAG_ARRIVE_D17R0107 = auto()
    FLAG_ARRIVE_D17R0108 = auto()
    FLAG_ARRIVE_D17R0109 = auto()
    FLAG_ARRIVE_D17R0110 = auto()
    FLAG_ARRIVE_D17R0111 = auto()
    FLAG_ARRIVE_D17R0112 = auto()
    FLAG_ARRIVE_D17R0113 = auto()
    FLAG_ARRIVE_D17R0114 = auto()
    FLAG_ARRIVE_D17R0115 = auto()
    FLAG_ARRIVE_D17R0116 = auto()
    FLAG_ARRIVE_D17R0117 = auto()
    FLAG_ARRIVE_D17R0118 = auto()
    FLAG_ARRIVE_D17R0119 = auto()
    FLAG_ARRIVE_D17R0120 = auto()
    FLAG_ARRIVE_D17R0121 = auto()
    FLAG_ARRIVE_D17R0122 = auto()
    FLAG_ARRIVE_D18 = auto()
    FLAG_ARRIVE_D20R0101 = auto()
    FLAG_ARRIVE_D20R0102 = auto()
    FLAG_ARRIVE_D20R0103 = auto()
    FLAG_ARRIVE_D20R0104 = auto()
    FLAG_ARRIVE_D20R0105 = auto()
    FLAG_ARRIVE_D20R0106 = auto()
    FLAG_ARRIVE_D21R0101 = auto()
    FLAG_ARRIVE_D21R0102 = auto()
    FLAG_ARRIVE_D22R0101 = auto()
    FLAG_ARRIVE_D22R0102 = auto()
    FLAG_ARRIVE_D22R0103 = auto()
    FLAG_ARRIVE_D23R0101 = auto()
    FLAG_ARRIVE_D24 = auto()
    FLAG_ARRIVE_D24R0101 = auto()
    FLAG_ARRIVE_D24R0102 = auto()
    FLAG_ARRIVE_D24R0103 = auto()
    FLAG_ARRIVE_D24R0104 = auto()
    FLAG_ARRIVE_D24R0105 = auto()
    FLAG_ARRIVE_D24R0106 = auto()
    FLAG_ARRIVE_D24R0201 = auto()
    FLAG_ARRIVE_D25R0101 = auto()
    FLAG_ARRIVE_D25R0102 = auto()
    FLAG_ARRIVE_D25R0103 = auto()
    FLAG_ARRIVE_D25R0104 = auto()
    FLAG_ARRIVE_D25R0105 = auto()
    FLAG_ARRIVE_D25R0106 = auto()
    FLAG_ARRIVE_D25R0107 = auto()
    FLAG_ARRIVE_D25R0108 = auto()
    FLAG_ARRIVE_D25R0109 = auto()
    FLAG_ARRIVE_D26R0101 = auto()
    FLAG_ARRIVE_D26R0102 = auto()
    FLAG_ARRIVE_D26R0103 = auto()
    FLAG_ARRIVE_D26R0104 = auto()
    FLAG_ARRIVE_D26R0105 = auto()
    FLAG_ARRIVE_D26R0106 = auto()
    FLAG_ARRIVE_D26R0107 = auto()
    FLAG_ARRIVE_D26R0108 = auto()
    FLAG_ARRIVE_D27R0101 = auto()
    FLAG_ARRIVE_D27R0102 = auto()
    FLAG_ARRIVE_D27R0103 = auto()
    FLAG_ARRIVE_D28R0101 = auto()
    FLAG_ARRIVE_D28R0102 = auto()
    FLAG_ARRIVE_D28R0103 = auto()
    FLAG_ARRIVE_D29R0101 = auto()
    FLAG_ARRIVE_D29R0102 = auto()
    FLAG_ARRIVE_D29R0103 = auto()
    FLAG_ARRIVE_D30 = auto()
    FLAG_ARRIVE_D30R0101 = auto()
    FLAG_ARRIVE_D31 = auto()
    FLAG_ARRIVE_D31R0101 = auto()
    FLAG_ARRIVE_D31R0201 = auto()
    FLAG_ARRIVE_D31R0202 = auto()
    FLAG_ARRIVE_D31R0203 = auto()
    FLAG_ARRIVE_D31R0204 = auto()
    FLAG_ARRIVE_D31R0205 = auto()
    FLAG_ARRIVE_D31R0206 = auto()
    FLAG_ARRIVE_D31R0207 = auto()
    FLAG_ARRIVE_DIRECT2 = auto()
    FLAG_ARRIVE_DIRECT4 = auto()
    FLAG_ARRIVE_EVERYWHERE = auto()
    FLAG_ARRIVE_L01 = auto()
    FLAG_ARRIVE_L02 = auto()
    FLAG_ARRIVE_L02R0101 = auto()
    FLAG_ARRIVE_L02R0201 = auto()
    FLAG_ARRIVE_L02R0301 = auto()
    FLAG_ARRIVE_L03 = auto()
    FLAG_ARRIVE_L04 = auto()
    FLAG_ARRIVE_NOTHING = auto()
    FLAG_ARRIVE_R201 = auto()
    FLAG_ARRIVE_R202 = auto()
    FLAG_ARRIVE_R203 = auto()
    FLAG_ARRIVE_R204A = auto()
    FLAG_ARRIVE_R204B = auto()
    FLAG_ARRIVE_R205A = auto()
    FLAG_ARRIVE_R205AR0101 = auto()
    FLAG_ARRIVE_R205B = auto()
    FLAG_ARRIVE_R206 = auto()
    FLAG_ARRIVE_R206R0101 = auto()
    FLAG_ARRIVE_R207 = auto()
    FLAG_ARRIVE_R208 = auto()
    FLAG_ARRIVE_R208R0101 = auto()
    FLAG_ARRIVE_R209 = auto()
    FLAG_ARRIVE_R209R0101 = auto()
    FLAG_ARRIVE_R209R0102 = auto()
    FLAG_ARRIVE_R209R0103 = auto()
    FLAG_ARRIVE_R209R0104 = auto()
    FLAG_ARRIVE_R209R0105 = auto()
    FLAG_ARRIVE_R210A = auto()
    FLAG_ARRIVE_R210AR0101 = auto()
    FLAG_ARRIVE_R210B = auto()
    FLAG_ARRIVE_R210BR0101 = auto()
    FLAG_ARRIVE_R211A = auto()
    FLAG_ARRIVE_R211B = auto()
    FLAG_ARRIVE_R212A = auto()
    FLAG_ARRIVE_R212AR0101 = auto()
    FLAG_ARRIVE_R212AR0102 = auto()
    FLAG_ARRIVE_R212AR0103 = auto()
    FLAG_ARRIVE_R212B = auto()
    FLAG_ARRIVE_R212BR0101 = auto()
    FLAG_ARRIVE_R213 = auto()
    FLAG_ARRIVE_R213R0101 = auto()
    FLAG_ARRIVE_R213R0201 = auto()
    FLAG_ARRIVE_R213R0301 = auto()
    FLAG_ARRIVE_R213R0401 = auto()
    FLAG_ARRIVE_R213R0501 = auto()
    FLAG_ARRIVE_R213R0601 = auto()
    FLAG_ARRIVE_R214 = auto()
    FLAG_ARRIVE_R214R0101 = auto()
    FLAG_ARRIVE_R215 = auto()
    FLAG_ARRIVE_R216 = auto()
    FLAG_ARRIVE_R216R0101 = auto()
    FLAG_ARRIVE_R217 = auto()
    FLAG_ARRIVE_R217R0101 = auto()
    FLAG_ARRIVE_R217R0201 = auto()
    FLAG_ARRIVE_R218 = auto()
    FLAG_ARRIVE_R218R0101 = auto()
    FLAG_ARRIVE_R218R0201 = auto()
    FLAG_ARRIVE_R219 = auto()
    FLAG_ARRIVE_R221 = auto()
    FLAG_ARRIVE_R221R0101 = auto()
    FLAG_ARRIVE_R221R0201 = auto()
    FLAG_ARRIVE_R222 = auto()
    FLAG_ARRIVE_R222R0101 = auto()
    FLAG_ARRIVE_R222R0201 = auto()
    FLAG_ARRIVE_R222R0301 = auto()
    FLAG_ARRIVE_R224 = auto()
    FLAG_ARRIVE_R225 = auto()
    FLAG_ARRIVE_R225R0101 = auto()
    FLAG_ARRIVE_R227 = auto()
    FLAG_ARRIVE_R227R0101 = auto()
    FLAG_ARRIVE_R228 = auto()
    FLAG_ARRIVE_R228R0101 = auto()
    FLAG_ARRIVE_R228R0201 = auto()
    FLAG_ARRIVE_R228R0301 = auto()
    FLAG_ARRIVE_R229 = auto()
    FLAG_ARRIVE_RECORD = auto()
    FLAG_ARRIVE_T01 = auto()
    FLAG_ARRIVE_T01R0101 = auto()
    FLAG_ARRIVE_T01R0102 = auto()
    FLAG_ARRIVE_T01R0201 = auto()
    FLAG_ARRIVE_T01R0202 = auto()
    FLAG_ARRIVE_T01R0301 = auto()
    FLAG_ARRIVE_T01R0401 = auto()
    FLAG_ARRIVE_T02 = auto()
    FLAG_ARRIVE_T02FS0101 = auto()
    FLAG_ARRIVE_T02PC0101 = auto()
    FLAG_ARRIVE_T02PC0102 = auto()
    FLAG_ARRIVE_T02PC0103 = auto()
    FLAG_ARRIVE_T02R0101 = auto()
    FLAG_ARRIVE_T02R0201 = auto()
    FLAG_ARRIVE_T02R0202 = auto()
    FLAG_ARRIVE_T02R0301 = auto()
    FLAG_ARRIVE_T03 = auto()
    FLAG_ARRIVE_T03FS0101 = auto()
    FLAG_ARRIVE_T03PC0101 = auto()
    FLAG_ARRIVE_T03PC0102 = auto()
    FLAG_ARRIVE_T03PC0103 = auto()
    FLAG_ARRIVE_T03R0101 = auto()
    FLAG_ARRIVE_T03R0201 = auto()
    FLAG_ARRIVE_T03R0301 = auto()
    FLAG_ARRIVE_T04 = auto()
    FLAG_ARRIVE_T04FS0101 = auto()
    FLAG_ARRIVE_T04PC0101 = auto()
    FLAG_ARRIVE_T04PC0102 = auto()
    FLAG_ARRIVE_T04PC0103 = auto()
    FLAG_ARRIVE_T04R0101 = auto()
    FLAG_ARRIVE_T04R0201 = auto()
    FLAG_ARRIVE_T04R0301 = auto()
    FLAG_ARRIVE_T04R0401 = auto()
    FLAG_ARRIVE_T04R0501 = auto()
    FLAG_ARRIVE_T05 = auto()
    FLAG_ARRIVE_T05PC0101 = auto()
    FLAG_ARRIVE_T05PC0102 = auto()
    FLAG_ARRIVE_T05PC0103 = auto()
    FLAG_ARRIVE_T05R0101 = auto()
    FLAG_ARRIVE_T05R0201 = auto()
    FLAG_ARRIVE_T05R0301 = auto()
    FLAG_ARRIVE_T05R0401 = auto()
    FLAG_ARRIVE_T05R0501 = auto()
    FLAG_ARRIVE_T06 = auto()
    FLAG_ARRIVE_T06FS0101 = auto()
    FLAG_ARRIVE_T06PC0101 = auto()
    FLAG_ARRIVE_T06PC0102 = auto()
    FLAG_ARRIVE_T06PC0103 = auto()
    FLAG_ARRIVE_T06R0101 = auto()
    FLAG_ARRIVE_T06R0201 = auto()
    FLAG_ARRIVE_T06R0301 = auto()
    FLAG_ARRIVE_T07 = auto()
    FLAG_ARRIVE_T07FS0101 = auto()
    FLAG_ARRIVE_T07PC0101 = auto()
    FLAG_ARRIVE_T07PC0102 = auto()
    FLAG_ARRIVE_T07PC0103 = auto()
    FLAG_ARRIVE_T07R0101 = auto()
    FLAG_ARRIVE_T07R0102 = auto()
    FLAG_ARRIVE_T07R0103 = auto()
    FLAG_ARRIVE_T07R0201 = auto()
    FLAG_ARRIVE_T07R0301 = auto()
    FLAG_ARRIVE_UG = auto()
    FLAG_ARRIVE_UNION = auto()
    FLAG_ARRIVE_W220 = auto()
    FLAG_ARRIVE_W223 = auto()
    FLAG_ARRIVE_W226 = auto()
    FLAG_ARRIVE_W226R0101 = auto()
    FLAG_ARRIVE_W230 = auto()
    FLAG_ARRIVE_W231 = auto()
    FLAG_ARRIVE_UNION01 = auto()
    FLAG_ARRIVE_UNION02 = auto()
    FLAG_ARRIVE_UNION03 = auto()
    FLAG_ARRIVE_C04R0205 = auto()
    FLAG_ARRIVE_D10R0201 = auto()
    FLAG_ARRIVE_D10R0202 = auto()
    FLAG_ARRIVE_D10R0301 = auto()
    FLAG_ARRIVE_D10R0302 = auto()
    FLAG_ARRIVE_D10R0303 = auto()
    FLAG_ARRIVE_D10R0401 = auto()
    FLAG_ARRIVE_D10R0402 = auto()
    FLAG_ARRIVE_D10R0403 = auto()
    FLAG_ARRIVE_D10R0501 = auto()
    FLAG_ARRIVE_D10R0502 = auto()
    FLAG_ARRIVE_D10R0601 = auto()
    FLAG_ARRIVE_D10R0701 = auto()
    FLAG_ARRIVE_D10R0801 = auto()
    FLAG_ARRIVE_UGA01 = auto()
    FLAG_ARRIVE_UGA02 = auto()
    FLAG_ARRIVE_UGA03 = auto()
    FLAG_ARRIVE_UGA04 = auto()
    FLAG_ARRIVE_UGA05 = auto()
    FLAG_ARRIVE_UGA06 = auto()
    FLAG_ARRIVE_UGA07 = auto()
    FLAG_ARRIVE_UGA08 = auto()
    FLAG_ARRIVE_UGA09 = auto()
    FLAG_ARRIVE_UGA10 = auto()
    FLAG_ARRIVE_UGB01 = auto()
    FLAG_ARRIVE_UGB02 = auto()
    FLAG_ARRIVE_UGB03 = auto()
    FLAG_ARRIVE_UGB04 = auto()
    FLAG_ARRIVE_UGB05 = auto()
    FLAG_ARRIVE_UGB06 = auto()
    FLAG_ARRIVE_UGB07 = auto()
    FLAG_ARRIVE_UGC01 = auto()
    FLAG_ARRIVE_UGD01 = auto()
    FLAG_ARRIVE_UGD02 = auto()
    FLAG_ARRIVE_UGD03 = auto()
    FLAG_ARRIVE_UGD04 = auto()
    FLAG_ARRIVE_UGD05 = auto()
    FLAG_ARRIVE_UGE01 = auto()
    FLAG_ARRIVE_UGE02 = auto()
    FLAG_ARRIVE_UGE03 = auto()
    FLAG_ARRIVE_UGE04 = auto()
    FLAG_ARRIVE_UGE05 = auto()
    FLAG_ARRIVE_UGF01 = auto()
    FLAG_ARRIVE_UGF02 = auto()
    FLAG_ARRIVE_UGF03 = auto()
    FLAG_ARRIVE_UGF04 = auto()
    FLAG_ARRIVE_UGF05 = auto()
    FLAG_ARRIVE_UGF06 = auto()
    FLAG_ARRIVE_UGF07 = auto()
    FLAG_ARRIVE_UGSPACE01 = auto()
    FLAG_ARRIVE_UGSPACE02 = auto()
    FLAG_ARRIVE_UGSPACE03 = auto()
    FLAG_ARRIVE_UGSPACE04 = auto()
    FLAG_ARRIVE_UGSPACE05 = auto()
    FLAG_ARRIVE_UGSPACE06 = auto()
    FLAG_ARRIVE_UGSPACE07 = auto()
    FLAG_ARRIVE_UGSPACE08 = auto()
    FLAG_ARRIVE_UGSPACE09 = auto()
    FLAG_ARRIVE_UGSPACE10 = auto()
    FLAG_ARRIVE_UGSPACE11 = auto()
    FLAG_ARRIVE_UGSPACE12 = auto()
    FLAG_ARRIVE_UGSPACE13 = auto()
    FLAG_ARRIVE_UGSPACE14 = auto()
    FLAG_ARRIVE_UGSPACE15 = auto()
    FLAG_ARRIVE_UGSPACE16 = auto()
    FLAG_ARRIVE_UGSPACE17 = auto()
    FLAG_ARRIVE_UGSPACE18 = auto()
    FLAG_ARRIVE_UGSPACE19 = auto()
    FLAG_ARRIVE_UGSPACE20 = auto()
    FLAG_ARRIVE_UGSPACE21 = auto()
    FLAG_ARRIVE_UGSPACE22 = auto()
    FLAG_ARRIVE_UGSPACE23 = auto()
    FLAG_ARRIVE_UGSPACE24 = auto()
    FLAG_ARRIVE_UGSPACE25 = auto()
    FLAG_ARRIVE_UGSPACE26 = auto()
    FLAG_ARRIVE_UGSPACE27 = auto()
    FLAG_ARRIVE_UGSPACE28 = auto()
    FLAG_ARRIVE_UGSPACE29 = auto()
    FLAG_ARRIVE_UGSPACE30 = auto()
    FLAG_ARRIVE_UGSPACE31 = auto()
    FLAG_ARRIVE_UGSPACE32 = auto()
    FLAG_ARRIVE_UGSPACE33 = auto()
    FLAG_ARRIVE_UGSPACE34 = auto()
    FLAG_ARRIVE_UGSPACE35 = auto()
    FLAG_ARRIVE_UGSPACE36 = auto()
    FLAG_ARRIVE_UGSPACE37 = auto()
    FLAG_ARRIVE_UGSPACE38 = auto()
    FLAG_ARRIVE_UGSPACE39 = auto()
    FLAG_ARRIVE_UGSPACE40 = auto()
    FLAG_ARRIVE_UGSPACE41 = auto()
    FLAG_ARRIVE_UGSPACE42 = auto()
    FLAG_ARRIVE_UGSPACE43 = auto()
    FLAG_ARRIVE_UGSPACE44 = auto()
    FLAG_ARRIVE_UGSPACE45 = auto()
    FLAG_ARRIVE_UGSPACE46 = auto()
    FLAG_ARRIVE_UGSPACE47 = auto()
    FLAG_ARRIVE_UGSPACE48 = auto()
    FLAG_ARRIVE_UGSPACE49 = auto()
    FLAG_ARRIVE_UGSPACE50 = auto()
    FLAG_ARRIVE_UGSPACE51 = auto()
    FLAG_ARRIVE_UGSPACE52 = auto()
    FLAG_ARRIVE_UGSPACE53 = auto()
    FLAG_ARRIVE_UGSPACE54 = auto()
    FLAG_ARRIVE_UGSPACE55 = auto()
    FLAG_ARRIVE_UGSPACE56 = auto()
    FLAG_ARRIVE_UGSPACE57 = auto()
    FLAG_ARRIVE_UGSPACE58 = auto()
    FLAG_ARRIVE_UGSPACE59 = auto()
    FLAG_ARRIVE_UGSPACE60 = auto()
    FLAG_ARRIVE_UGSPACE61 = auto()
    FLAG_ARRIVE_UGSPACE62 = auto()
    FLAG_ARRIVE_UGSPACE63 = auto()
    FLAG_ARRIVE_UGSPACE64 = auto()
    FLAG_ARRIVE_UGSPACE65 = auto()
    FLAG_ARRIVE_UGSPACE66 = auto()
    FLAG_ARRIVE_UGSPACE67 = auto()
    FLAG_ARRIVE_UGSPACE68 = auto()
    FLAG_ARRIVE_UGSPACEL01 = auto()
    FLAG_ARRIVE_UGSPACEL02 = auto()
    FLAG_ARRIVE_UGSPACEL03 = auto()
    FLAG_ARRIVE_UGSPACEL04 = auto()
    FLAG_ARRIVE_UGSPACEL05 = auto()
    FLAG_ARRIVE_UGSPACEL06 = auto()
    FLAG_ARRIVE_UGSPACEL07 = auto()
    FLAG_ARRIVE_D05R0117 = auto()
    FLAG_ARRIVE_D10R0901 = auto()
    FLAG_ARRIVE_UGSECRETBASE01 = auto()
    FLAG_ARRIVE_UGSECRETBASE02 = auto()
    FLAG_ARRIVE_UGSECRETBASE03 = auto()
    FLAG_ARRIVE_UGSECRETBASE04 = auto()
    SYS_FLAG_CON_STYLE_NORMAL = auto()
    SYS_FLAG_CON_STYLE_GREAT = auto()
    SYS_FLAG_CON_STYLE_ULTRA = auto()
    SYS_FLAG_CON_BEAUTIFUL_NORMAL = auto()
    SYS_FLAG_CON_BEAUTIFUL_GREAT = auto()
    SYS_FLAG_CON_BEAUTIFUL_ULTRA = auto()
    SYS_FLAG_CON_CUTE_NORMAL = auto()
    SYS_FLAG_CON_CUTE_GREAT = auto()
    SYS_FLAG_CON_CUTE_ULTRA = auto()
    SYS_FLAG_CON_CLEVER_NORMAL = auto()
    SYS_FLAG_CON_CLEVER_GREAT = auto()
    SYS_FLAG_CON_CLEVER_ULTRA = auto()
    SYS_FLAG_CON_STRONG_NORMAL = auto()
    SYS_FLAG_CON_STRONG_GREAT = auto()
    SYS_FLAG_CON_STRONG_ULTRA = auto()
    SYS_FLAG_CAMERA_REVERSAL = auto()
    SYS_FLAG_ZENKOKU_GYM_KAIHOU = auto()
    SYS_FLAG_FIELD_STOPER_NOTHING = auto()
    SYS_FLAG_BATTLE_TOWER_M_S_OPEN = auto()
    SYS_FUREAI_EXIT = auto()
    SYS_HUSIGINAOKURIMONO_OPEN_FLAG = auto()
    SYS_GET_CAP = auto()
    SYS_NO_CAP_MODEL = auto()
    SYS_INPUT_OFF = auto()
    SYS_BOX_SYSTEM_OFF = auto()
    SYS_DENDOU_OFF = auto()
    SYS_ZENMETU_MUSI = auto()
    SYS_FLAG_BATTLE_TOWER_M_D_OPEN = auto()
    SYS_ROTOMU_HOT = auto()
    SYS_ROTOMU_WASH = auto()
    SYS_ROTOMU_COLD = auto()
    SYS_ROTOMU_FAN = auto()
    SYS_ROTOMU_CUT = auto()
    SYS_TRAINER_CARD_OPEN = auto()
    SYS_FLAG_CON_FUR_NORMAL = auto()
    SYS_FLAG_CON_FUR_GREAT = auto()
    SYS_FLAG_CON_FUR_ULTRA = auto()
    SYS_FLAG_SUPPORT_HOUSE = auto()
    SYS_FLAG_USE_TODAY_IWAKUDAKI = auto()
    SYS_FLAG_USE_TODAY_IAIGIRI = auto()
    SYS_FLAG_USE_TODAY_SORAWOTOBU = auto()
    SYS_FLAG_USE_TODAY_KIRIBARAI = auto()
    SYS_FLAG_USE_TODAY_NAMINORI = auto()
    SYS_FLAG_USE_TODAY_KAIRIKI = auto()
    SYS_FLAG_USE_TODAY_ROKKUKURAIMU = auto()
    SYS_FLAG_USE_TODAY_TAKINOBORI = auto()
    SYS_FLAG_UG_FRIEND_KASEKIHORI_SUCCESS = auto()
    SYS_FLAG_UG_HIMITUKITI_INTO = auto()
    SYS_FLAG_WILDCARD_000 = auto()
    SYS_FLAG_WILDCARD_001 = auto()
    SYS_FLAG_WILDCARD_002 = auto()
    SYS_FLAG_WILDCARD_003 = auto()
    SYS_FLAG_WILDCARD_004 = auto()
    SYS_FLAG_WILDCARD_005 = auto()
    SYS_FLAG_WILDCARD_006 = auto()
    SYS_FLAG_WILDCARD_007 = auto()
    SYS_FLAG_WILDCARD_008 = auto()
    SYS_FLAG_WILDCARD_009 = auto()
    SYS_FLAG_WILDCARD_010 = auto()
    SYS_FLAG_WILDCARD_011 = auto()
    SYS_FLAG_WILDCARD_012 = auto()
    SYS_FLAG_WILDCARD_013 = auto()
    SYS_FLAG_WILDCARD_014 = auto()
    SYS_FLAG_WILDCARD_015 = auto()
    SYS_FLAG_WILDCARD_016 = auto()
    SYS_FLAG_WILDCARD_017 = auto()
    SYS_FLAG_WILDCARD_018 = auto()
    SYS_FLAG_WILDCARD_019 = auto()
    SYS_FLAG_WILDCARD_020 = auto()
    SYS_FLAG_WILDCARD_021 = auto()
    SYS_FLAG_WILDCARD_022 = auto()
    SYS_FLAG_WILDCARD_023 = auto()
    SYS_FLAG_WILDCARD_024 = auto()
    SYS_FLAG_WILDCARD_025 = auto()
    SYS_FLAG_WILDCARD_026 = auto()
    SYS_FLAG_WILDCARD_027 = auto()
    SYS_FLAG_WILDCARD_028 = auto()
    SYS_FLAG_WILDCARD_029 = auto()
    SYS_FLAG_WILDCARD_030 = auto()
    SYS_FLAG_WILDCARD_031 = auto()
    SYS_FLAG_WILDCARD_032 = auto()
    SYS_FLAG_WILDCARD_033 = auto()
    SYS_FLAG_WILDCARD_034 = auto()
    SYS_FLAG_WILDCARD_035 = auto()
    SYS_FLAG_WILDCARD_036 = auto()
    SYS_FLAG_WILDCARD_037 = auto()
    SYS_FLAG_WILDCARD_038 = auto()
    SYS_FLAG_WILDCARD_039 = auto()
    SYS_FLAG_WILDCARD_040 = auto()
    SYS_FLAG_WILDCARD_041 = auto()
    SYS_FLAG_WILDCARD_042 = auto()
    SYS_FLAG_WILDCARD_043 = auto()
    SYS_FLAG_WILDCARD_044 = auto()
    SYS_FLAG_WILDCARD_045 = auto()
    SYS_FLAG_WILDCARD_046 = auto()
    SYS_FLAG_WILDCARD_047 = auto()
    SYS_FLAG_WILDCARD_048 = auto()
    SYS_FLAG_WILDCARD_049 = auto()
    SYS_FLAG_WILDCARD_050 = auto()
    SYS_FLAG_WILDCARD_051 = auto()
    SYS_FLAG_WILDCARD_052 = auto()
    SYS_FLAG_WILDCARD_053 = auto()
    SYS_FLAG_WILDCARD_054 = auto()
    SYS_FLAG_WILDCARD_055 = auto()
    SYS_FLAG_WILDCARD_056 = auto()
    SYS_FLAG_WILDCARD_057 = auto()
    SYS_FLAG_WILDCARD_058 = auto()
    SYS_FLAG_WILDCARD_059 = auto()
    SYS_FLAG_WILDCARD_060 = auto()
    SYS_FLAG_WILDCARD_061 = auto()
    SYS_FLAG_WILDCARD_062 = auto()
    SYS_FLAG_WILDCARD_063 = auto()
    SYS_FLAG_WILDCARD_064 = auto()
    SYS_FLAG_WILDCARD_065 = auto()
    SYS_FLAG_WILDCARD_066 = auto()
    SYS_FLAG_WILDCARD_067 = auto()
    SYS_FLAG_WILDCARD_068 = auto()
    SYS_FLAG_WILDCARD_069 = auto()
    SYS_FLAG_WILDCARD_070 = auto()
    SYS_FLAG_WILDCARD_071 = auto()
    SYS_FLAG_WILDCARD_072 = auto()
    SYS_FLAG_WILDCARD_073 = auto()
    SYS_FLAG_WILDCARD_074 = auto()
    SYS_FLAG_WILDCARD_075 = auto()
    SYS_FLAG_WILDCARD_076 = auto()
    SYS_FLAG_WILDCARD_077 = auto()
    SYS_FLAG_WILDCARD_078 = auto()
    SYS_FLAG_WILDCARD_079 = auto()
    SYS_FLAG_WILDCARD_080 = auto()
    SYS_FLAG_WILDCARD_081 = auto()
    SYS_FLAG_WILDCARD_082 = auto()
    SYS_FLAG_WILDCARD_083 = auto()
    SYS_FLAG_WILDCARD_084 = auto()
    SYS_FLAG_WILDCARD_085 = auto()
    SYS_FLAG_WILDCARD_086 = auto()
    SYS_FLAG_WILDCARD_087 = auto()
    SYS_FLAG_WILDCARD_088 = auto()
    SYS_FLAG_WILDCARD_089 = auto()
    SYS_FLAG_WILDCARD_090 = auto()
    SYS_FLAG_WILDCARD_091 = auto()
    SYS_FLAG_WILDCARD_092 = auto()
    SYS_FLAG_WILDCARD_093 = auto()
    SYS_FLAG_WILDCARD_094 = auto()
    SYS_FLAG_WILDCARD_095 = auto()
    SYS_FLAG_WILDCARD_096 = auto()
    SYS_FLAG_WILDCARD_097 = auto()
    SYS_FLAG_WILDCARD_098 = auto()
    SYS_FLAG_WILDCARD_099 = auto()
    SYS_FLAG_WILDCARD_100 = auto()
    SYS_FLAG_AUTOSAVE_STOP = auto()
    SYS_FLAG_MAP_INFO_STOP = auto()
    SYS_FLAG_BTL_RETURN_CALL_SP = auto()
    FLAG_ARRIVE_D10R0902 = auto()
    FLAG_ARRIVE_SEA01 = auto()
    FLAG_ARRIVE_C01R0209 = auto()
    FLAG_ARRIVE_UGAASECRETBASE01 = auto()
    FLAG_ARRIVE_UGAASECRETBASE02 = auto()
    FLAG_ARRIVE_UGAASECRETBASE03 = auto()
    FLAG_ARRIVE_UGABSECRETBASE01 = auto()
    FLAG_ARRIVE_UGABSECRETBASE02 = auto()
    FLAG_ARRIVE_UGABSECRETBASE03 = auto()
    FLAG_ARRIVE_UGBASECRETBASE01 = auto()
    FLAG_ARRIVE_UGBASECRETBASE02 = auto()
    FLAG_ARRIVE_UGBASECRETBASE03 = auto()
    FLAG_ARRIVE_UGCASECRETBASE01 = auto()
    FLAG_ARRIVE_UGCASECRETBASE02 = auto()
    FLAG_ARRIVE_UGCASECRETBASE03 = auto()
    FLAG_ARRIVE_UGDASECRETBASE01 = auto()
    FLAG_ARRIVE_UGDASECRETBASE02 = auto()
    FLAG_ARRIVE_UGDASECRETBASE03 = auto()
    FLAG_ARRIVE_UGEASECRETBASE01 = auto()
    FLAG_ARRIVE_UGEASECRETBASE02 = auto()
    FLAG_ARRIVE_UGEASECRETBASE03 = auto()
    FLAG_ARRIVE_UGFASECRETBASE01 = auto()
    FLAG_ARRIVE_UGFASECRETBASE02 = auto()
    FLAG_ARRIVE_UGFASECRETBASE03 = auto()
    FLAG_ARRIVE_D10R0202B = auto()
    FLAG_ARRIVE_D10R0301B = auto()
    FLAG_ARRIVE_D10R0302B = auto()
    FLAG_ARRIVE_D10R0303B = auto()
    FLAG_ARRIVE_D10R0401B = auto()
    FLAG_ARRIVE_D10R0402B = auto()
    FLAG_ARRIVE_D10R0403B = auto()
    FLAG_ARRIVE_D10R0501B = auto()
    FLAG_ARRIVE_D10R0502B = auto()
    FLAG_ARRIVE_D10R0601B = auto()
    FLAG_ARRIVE_OTHER_ZONE1 = auto()
    FLAG_ARRIVE_OTHER_ZONE2 = auto()
    FLAG_ARRIVE_OTHER_ZONE3 = auto()
    FLAG_ARRIVE_OTHER_ZONE4 = auto()
    FLAG_ARRIVE_OTHER_ZONE5 = auto()
    FLAG_ARRIVE_OTHER_ZONE6 = auto()
    FLAG_ARRIVE_OTHER_ZONE7 = auto()
    FLAG_ARRIVE_OTHER_ZONE8 = auto()
    FLAG_ARRIVE_OTHER_ZONE9 = auto()
    FLAG_ARRIVE_OTHER_ZONE10 = auto()
    FLAG_ARRIVE_OTHER_ZONE11 = auto()
    FLAG_ARRIVE_OTHER_ZONE12 = auto()
    FLAG_ARRIVE_OTHER_ZONE13 = auto()
    FLAG_ARRIVE_OTHER_ZONE14 = auto()
    FLAG_ARRIVE_OTHER_ZONE15 = auto()
    FLAG_ARRIVE_OTHER_ZONE16 = auto()
    FLAG_ARRIVE_OTHER_ZONE17 = auto()
    FLAG_ARRIVE_OTHER_ZONE18 = auto()
    FLAG_ARRIVE_OTHER_ZONE19 = auto()
    FLAG_ARRIVE_OTHER_ZONE20 = auto()
    FLAG_STOP_EYE_ENCOUNT = auto()