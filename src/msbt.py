from enum import IntEnum
from marshmallow_dataclass import dataclass
from typing import List, Optional
from dataclasses import field

class WordDataPatternID(IntEnum):
    Str = 0
    FontTag = 1
    ColorTag = 2
    SizeTag = 3
    CtrlTag = 4
    WordTag = 5
    SpriteFont = 6
    Event = 7

class MsgEventID(IntEnum):
    NONE = 0
    NewLine = 1
    Wait = 2
    ScrollPage = 3
    ScrollLine = 4
    CallBack = 5
    GuidIcon = 6
    End = 7

class GroupTagID(IntEnum):
    System = 0
    Name = 1
    Digit = 2
    Grm = 16
    EN = 19
    FR = 20
    IT = 21
    DE = 22
    ES = 23
    Kor = 25
    SC = 26
    Character1 = 50
    Character2 = 51
    Ctrl1 = 189
    Ctrl2 = 190

class TagPatternID(IntEnum):
    Word = 0
    Digit = 1
    Conversion = 2
    RichText = 3
    Grammar = 4
    GrammarWord = 5
    ControlDesign = 6
    ControlMessage = 7
    SpriteFont = 8

class ForceGrmTagID(IntEnum):
    '''
    Apparently this does nothing in BDSP and can be ignored
    '''
    NONE = 0
    Singular = 1
    Plural = 2
    Masculine = 3
    InitialCap = 4

class NameTagID(IntEnum):
    Default = 0
    PokemonName = 1
    PokemonNickname = 2
    PokeType = 3
    PokedexType = 4
    Place = 5
    Ability = 6
    Move = 7
    Nature = 8
    Item = 9
    ItemClassified = 10
    ItemAcc = 11
    PokemonNicknameTwo = 12
    Status = 13
    TrainerType = 14
    Poffin = 15
    ItemAccClassified = 16
    GoodsName = 17
    Pocket = 18
    ItemText = 19
    TrainerNameField = 20
    Poketch = 21
    UgItem = 22
    BagPocketIcon = 23
    PocketIcon = 24
    Word = 25
    Question = 26
    Answer = 27
    Accessory = 28
    Gym = 29
    TimeZone = 30
    Contest = 31
    ContestRank = 32
    PokeGender = 33
    PokeLevel = 34
    GroupName = 35
    Location = 36
    Area = 37
    Ribbon = 38
    UndergroundItemDefArt = 39
    UndergroundItemIndefArt = 40
    Taste = 41
    SerialNumber = 42
    FreeWord = 43
    Undefined = 44
    PlayerNickname = 45
    PlayerNicknamePrefix = 46
    TrimmianFormName = 47
    TrainerTypeAndName = 48
    HairStyle_Name = 49
    Bangs_Name = 50
    HairColor_Name = 51
    TournamentName = 52
    FullPowerMove = 53
    BattleState = 54
    FlySpotName = 55
    Record_Name = 56
    BattleTeam = 57
    BoxName = 58
    KisekaeItem = 59
    KisekaeItemColor = 60
    BGM = 61
    Uniformnumber = 62
    BirthdayM = 63
    BirthdayD = 64
    TrainerNameUpperCase = 65
    PokemonNicknameUpperCase = 66
    CookName = 67
    Classname = 68
    AnotherName = 69
    CompanyName = 70
    PlaceIndirect = 71
    FormName = 72
    RegurationName = 73
    Memory_Place = 74
    Memory_Feeling = 75
    Memory_Rank = 76
    Sticker = 77
    ParkItem = 78
    Kinomi = 79
    UgItemAcc = 80
    UgItemClassified = 81
    UgItemAccClassified = 82
    PoffinAcc = 83
    StyleName = 84
    BattleRule = 85

class DigitTagID(IntEnum):
    OneDigit = 0
    TwoDigits = 1
    ThreeDigits = 2
    FourDigits = 3
    FiveDigits = 4
    SixDigits = 5
    SevenDigits = 6
    EightDigits = 7
    NineDigits = 8
    TenDigits = 9

class EnglishTagID(IntEnum):
    Gender = 0
    Qty = 1
    GenderQty = 2
    DefArt = 3
    DefArtCap = 4
    IndArt = 5
    IndArtCap = 6
    ForceSingular = 7
    ForcePlural = 8
    ForceInitialCap = 9
    QtyZero = 10

class FrenchTagID(IntEnum):
    Gender = 0
    Qty = 1
    GenderQty = 2
    DefArt = 3
    DefArtCap = 4
    IndArt = 5
    IndArtCap = 6
    A_DefArt = 7
    A_DefArtCap = 8
    De_DefArt = 9
    De_DefArtCap = 10
    De = 11
    DeCap = 12
    ForceSingular = 13
    ForcePlural = 14
    Que = 15
    QueCap = 16
    Elision = 17
    ForceInitialCap = 18
    QtyZero = 19

class ItalianTagID(IntEnum):
    Gender = 0
    Qty = 1
    GenderQty = 2
    DefArt = 3
    DefArtCap = 4
    IndArt = 5
    IndArtCap = 6
    Di_DefArt = 7
    Di_DefArtCap = 8
    Su_DefArt = 9
    Su_DefArtCap = 10
    A_DefArt = 11
    A_DefArtCap = 12
    ForceSingular = 13
    ForcePlural = 14
    ForceMasculine = 15
    In_DefArt = 16
    In_DefArtCap = 17
    Ed = 18
    EdCap = 19
    Ad = 20
    AdCap = 21
    ForceInitialCap = 22
    QtyZero = 23
    DateIT = 24

class GermanTagID(IntEnum):
    Gender = 0
    Qty = 1
    GenderQty = 2
    DefArtNom = 3
    DefArtNomCap = 4
    IndArtNom = 5
    IndArtNomCap = 6
    DefArtAcc = 7
    DefArtAccCap = 8
    IndArtAcc = 9
    IndArtAccCap = 10
    ForceSingular = 11
    ForcePlural = 12
    ForceInitialCap = 13
    QtyZero = 14
    ItemAcc = 15
    ItemAccClassified = 16

class SpanishTagID(IntEnum):
    Gender = 0
    Qty = 1
    GenderQty = 2
    DefArt = 3
    DefArtCap = 4
    IndArt = 5
    IndArtCap = 6
    De_DefArt = 7
    De_DefArtCap = 8
    A_DefArt = 9
    A_DefArtCap = 10
    DefArt_TrTypeAndName = 11
    DefArtCap_TrTypeAndName = 12
    A_DefArt_TrTypeAndName = 13
    De_DefArt_TrTypeAndName = 14
    ForceSingular = 15
    ForcePlural = 16
    ForceInitialCap = 17
    QtyZero = 18
    y_e = 19
    Y_E = 20
    o_u = 21
    O_U = 22

class KoreanTagID(IntEnum):
    Particle = 0
    Gender = 1
    Qty = 2
    GenderQty = 3
    QtyZero = 4

class SimpChineseTagID(IntEnum):
    Gender = 0

class DigitTagParamID(IntEnum):
    '''
    Only used when the GroupTagID is Digit.
    It's used as the separator for large numbers
    Default will be the best option 99% of the time
    '''
    Nothing = 0 # The enum in game uses None but that's a python keyword
    Default = 1
    Comma = 2
    Period = 3
    HalfSpace = 4
    QuarterSpace = 5

@dataclass
class UnityGameObject:
    m_FileID: int
    m_PathID: int

    class Meta:
        ordered = True

@dataclass
class StyleInfo:
    styleIndex: int
    colorIndex: int
    fontSize: int
    maxWidth: int
    controlID: int# MessageEnumData.MsgControlID 

    @classmethod
    def default(cls):
        # Based on regular text from people
        return cls(
            0,
            -1,
            54,
            1080,
            0
        )

    class Meta:
        ordered = True

@dataclass
class TagData:
    tagIndex: int
    groupID: int # MessageEnumData.GroupTagID 
    tagID: int
    tagPatternID: int # MessageEnumData.TagPatternID 
    forceArticle: int
    tagParameter: int
    tagWordArray: List[str]
    forceGrmID: int # MessageEnumData.ForceGrmID 
    
    class Meta:
        ordered = True 

@dataclass
class WordData:
    patternID: int # MessageEnumData.WordDataPatternID 
    eventID: int # MessageEnumData.MsgEventID 
    tagIndex: int
    tagValue: float
    str: str # type: ignore
    strWidth: float

    class Meta:
        ordered = True

    def __post_init__(self):
        # Ensure tagValue is a float except when it's zero
        if self.tagValue == 0:
            self.tagValue = 0  # Keep it as an integer zero
        else:
            self.tagValue = float(self.tagValue)  # Convert to float

        # Ensure strWidth is a float except when it's zero or -1
        if self.strWidth == 0:
            self.strWidth = 0  # Keep it as an integer zero
        elif self.strWidth == -1:
            self.strWidth = -1
        else:
            self.strWidth = float(self.strWidth)  # Convert to float

        if len(self.str) == 0:
            self.str = None
        else:
            self.str = str(self.str)

@dataclass
class LabelData:
    labelIndex: int
    arrayIndex: int
    labelName: str
    styleInfo: StyleInfo
    attributeValueArray: List[int]
    tagDataArray: List[TagData]
    wordDataArray: List[WordData]

    @staticmethod
    def defaultAttributeValueArray():
        return [-1, 0, 0, -1, 0]

    class Meta:
        ordered = True

@dataclass
class MsbtFile:
    m_GameObject: Optional[UnityGameObject]
    m_Enabled: Optional[int]
    m_Script: Optional[UnityGameObject]
    m_Name: Optional[str]

    hash: int
    langID: int # Should grab the enum
    isResident: int
    isKanji: int
    labelDataArray: List[LabelData]

    class Meta:
        ordered = True