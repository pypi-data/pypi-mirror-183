from cubelib.types import VarInt, String, UnsignedShort, NextState, Long, ByteArray
from cubelib.p import Night

class Handshaking:        
    class Handshake(Night):
        proto_ver: VarInt
        servername: String
        serverport: UnsignedShort
        nextstate: NextState

    map = {0: Handshake}
    inv_map = {Handshake: 0}

class Status:
    class Request(Night):
        pass
        
    class Ping(Night):
        uniq: Long
    
    map = {0: Request, 1: Ping}
    inv_map = {Request: 0, Ping: 1}

class ClassicLogin:
           
    class LoginStart(Night):
        username: String    

    class EncryptionResponse(Night):
        Shared_Secret_Length: VarInt
        Shared_Secret: ByteArray
        Verify_Token_Length: VarInt
        Verify_Token: ByteArray

    map = {0: LoginStart, 1: EncryptionResponse}
    inv_map = {LoginStart: 0, EncryptionResponse: 1}
