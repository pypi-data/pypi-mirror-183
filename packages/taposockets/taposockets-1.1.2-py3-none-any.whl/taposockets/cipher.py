import pkcs7
import base64

from Crypto.Cipher import AES


class TpLinkCipher:
    def __init__(self, key: bytearray, iv: bytearray):
        self.iv = iv
        self.key = key

    def encrypt(self, data):
        data = pkcs7.PKCS7Encoder().encode(data)
        cipher = AES.new(bytes(self.key), AES.MODE_CBC, bytes(self.iv))
        encrypted = cipher.encrypt(data.encode("UTF-8"))

        return base64.b64encode(encrypted).decode("UTF-8").replace("\r\n","")

    def decrypt(self, data: str):
        aes = AES.new(bytes(self.key), AES.MODE_CBC, bytes(self.iv))
        pad_text = aes.decrypt(base64.b64decode(data.encode("UTF-8"))).decode("UTF-8")
        return pkcs7.PKCS7Encoder().decode(pad_text)
