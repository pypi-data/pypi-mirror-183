from requests import post
from json import loads, dumps
from random import choice
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, urlsafe_b64decode
from Crypto.Cipher import AES
from re import findall
from colorama import Fore

web = {'app_name': 'Main', 'app_version': '4.0.8', 'platform': 'Web', 'package': 'web.rubika.ir', 'lang_code': 'fa'}

android = {'app_name': 'Main', 'app_version': '3.0.9', 'platform': 'Android', 'package': 'app.rbmain.a', 'lang_code': 'fa'}

class encoderjson:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while (s < len(n)):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        return b64encode(AES.new(self.key, AES.MODE_CBC, self.iv).encrypt(pad(text.encode('UTF-8'), AES.block_size))).decode('UTF-8')

    def decrypt(self, text):
        return unpad(AES.new(self.key, AES.MODE_CBC, self.iv).decrypt(urlsafe_b64decode(text.encode('UTF-8'))),AES.block_size).decode('UTF-8')


class encoder_photo:

    def getThumbInline(image_bytes: bytes):
        import io, base64, PIL.Image
        im = PIL.Image.open(io.BytesIO(image_bytes))
        width, height = im.size
        if height > width:
            new_height = 40
            new_width = round(new_height * width / height)
        else:
            new_width = 40
            new_height = round(new_width * height / width)
        im = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
        changed_image = io.BytesIO()
        im.save(changed_image, format='PNG')
        changed_image = changed_image.getvalue()
        return base64.b64encode(changed_image)
        
class welcome:
        print(f"-🔥- Rubika_Pv : {Fore.CYAN} @aQa_MoHaMad_CoDer{Fore.WHITE}\n\n-🚨- Rubika_Channel : {Fore.CYAN} @python_source_dark{Fore.WHITE}\n\nدر حـال فعـال شـدن | منتظر بمـانیـد ...                                   \n - - - - - - - - - - - - - - - - \n")