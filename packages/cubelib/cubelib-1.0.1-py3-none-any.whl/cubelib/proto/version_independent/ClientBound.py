from cubelib.types import String, Long, VarInt, ByteArray
from cubelib.p import Night

class Status:
    class Response(Night):
        JsonRsp: String
        
    class Pong(Night):
        uniq: Long

    map = {0: Response, 1: Pong}
    inv_map = {Response: 0, Pong: 1}

class ClassicLogin:

    class Disconnect(Night):
        reason: String
    
    class SetCompression(Night):     
        Threshold: VarInt
    
    class LoginSuccess(Night):
        uuid: String
        username: String
    
    class EncryptionRequest(Night):
        Server_ID: String[[20]]
        Public_Key_Length: VarInt
        Public_Key: ByteArray
        Verify_Token_Length: VarInt
        Verify_Token: ByteArray

    map = {0: Disconnect, 1: EncryptionRequest, 2: LoginSuccess, 3: SetCompression}
    inv_map = {v: k for k, v in map.items()}
     