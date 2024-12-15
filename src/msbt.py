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

class ForceGrmID(IntEnum):
    NONE = 0
    Singular = 1
    Plural = 2
    Masculine = 3
    InitialCap = 4

class TagID(IntEnum):
    Default = 0
    PokeType = 3
    Number = 4

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