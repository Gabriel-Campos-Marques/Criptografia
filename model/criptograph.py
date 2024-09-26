import base64
from stegano import lsb
from cryptography.fernet import Fernet

chave = Fernet.generate_key()

class Criptograph():
    def criptgraph_file(self, file64: bytes):        
        key = Fernet.generate_key()
        print(key.__str__)
        fernet = Fernet(key)
        
        oFileCriptgraph = fernet.encrypt(base64.b64decode(file64))
        return {
            "file": base64.b64encode(oFileCriptgraph),
            "key": key
        }
                
    def descriptgraph_file(self, file64: bytes, sKey:str):
        fernet = Fernet(sKey)
        oFileDescriptgraph = fernet.decrypt(base64.b64decode(file64))
        return {
            "file": base64.b64encode(oFileDescriptgraph),
        }
 

    def steganography_file(self, file64: bytes, sMessage: str):
        oFileSecret = lsb.hide(base64.b64decode(file64), sMessage)
        return base64.b64encode(oFileSecret.save())

    def steganography_reveal(self, file64: bytes):
        sMessageSecret = lsb.reveal(base64.b64decode(file64))
        return sMessageSecret