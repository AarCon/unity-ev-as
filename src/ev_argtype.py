from enum import IntEnum, auto
class EvArgType(IntEnum):
    @classmethod
    def to_yaml(cls, dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:int', str(int(data)))

    CmdType = 0
    Value = 1
    Work = 2
    Flag = 3
    SysFlag = 4
    String = 5
    # Not used by the game. Internal variant for marking when something is a true
    # string, and not an index in the strList table
    MacroString = 6 