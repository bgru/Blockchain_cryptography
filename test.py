# !pip install pynacl
import base64
import json
from datetime import datetime

import nacl.secret
import nacl.utils

# Przygotowanie danych

messageText = "Text Message AAAAA"
data = {"message": messageText, "timestamp": str(datetime.now())}
dataString = json.dumps(data, sort_keys=True)
dataBytes = dataString.encode("UTF-8")

# Przygotowanie klucza

key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)
print("Przygotowany klucz: ")
print(key)
keyBase64 = base64.b64encode(key).decode("UTF-8")
print("\nklucz base64: ")
print(keyBase64)

# Tworzymy szyfrowanie
box = nacl.secret.SecretBox(key)
encrypted = box.encrypt(dataBytes)
print("\nwiadomość: ")
print(dataBytes)
print("\nencrypted wiadomość: ")
print(encrypted)
encryptedBase64 = base64.b64encode(encrypted).decode("utf-8")
print("\nencrypted wiadomość Base64: ")
print(encryptedBase64)

# Odszyfrowanie wiadomości
keyFromEmail = keyBase64
key = base64.b64decode(keyFromEmail.encode("utf-8"))
print("\nodszyfrowany klucz: ")
print(key)
dataFromEmail = encryptedBase64
dataEncrypted = base64.b64decode(dataFromEmail.encode("utf-8"))
print("\nzaszyfrowana wiadomosc: ")
print(dataEncrypted)

# Odszyfrowanie, ciąg dalszy
box = nacl.secret.SecretBox(key)
dataBytes = box.decrypt(dataEncrypted)

print ("\nWiadomosc oraz wiadomosc z maila: ")
print(data)
print(dataBytes)
