from ...types import VarInt, UnsignedShort, Long, String, NextState, UnsignedByte, Byte, Bool, Int, ByteArray, Position, Float, Double, Short, Angle
from ...p import Night
from cubelib.proto.version_independent.ClientBound import ClassicLogin

class Login(ClassicLogin):
    pass
    
class Play:

    map = {}
    inv_map = {}