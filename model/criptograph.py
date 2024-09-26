import base64
from stegano import lsb
from cryptography.fernet import Fernet
from PIL import Image
import io

class Criptograph():
    def criptgraph_file(self, file64: bytes):        
        key = Fernet.generate_key()
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
        file = base64.b64decode(file64)
        image = Image.open(io.BytesIO(file))
        oFileSecret = lsb.hide(image=image, message=sMessage)
        buffer = io.BytesIO()
        oFileSecret.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue())

    def steganography_reveal(self, file64: bytes):
        #missing_padding = len(file64) % 4
        ##   file64 += b'=' * (4 - missing_padding)
        
        # Decodificar o arquivo base64
        file = base64.b64decode(file64)
        image = Image.open(io.BytesIO(file))
        sMessageSecret = lsb.reveal(image)
        return sMessageSecret