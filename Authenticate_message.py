import nacl.encoding
import nacl.signing
import nacl.secret
import nacl.hash
import nacl.exceptions
import nacl.utils

# ===================================== Klucz symetryczny =====================================

# Generowanie klucza dla SecretBox
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Tworzenie SecretBox
box = nacl.secret.SecretBox(key)

# Przykładowa wiadomość
message = b"Hello, world!"

# Zakodowanie wiadomości kluczem prywatnym
signing_key = nacl.signing.SigningKey.generate()
signed_message = signing_key.sign(message)
print("Zakodowana wiadomość:", signed_message)

# Tworzenie hasha wiadomości
hash_message = nacl.hash.sha256(message)

# Zaszyfrowanie hasha wiadomości kluczem prywatnym
encrypted_hash = box.encrypt(hash_message)
print("Zaszyfrowany hash wiadomości:", encrypted_hash)

# Odszyfrowanie wiadomości kluczem publicznym
public_key = signing_key.verify_key
try:
    verified_message = public_key.verify(signed_message)
    print("Odszyfrowana wiadomość:", verified_message)
except nacl.exceptions.BadSignatureError:
    print("Błąd: Podpis nieprawidłowy.")

# Odszyfrowanie hasha wiadomości kluczem publicznym
try:
    decrypted_hash = box.decrypt(encrypted_hash)
    print("Odszyfrowany hash wiadomości:", decrypted_hash)
except nacl.exceptions.CryptoError:
    print("Błąd: Odszyfrowanie nie powiodło się.")

print("\n\n\n")

# ===================================== Klucz asymetryczny =====================================


# Generowanie klucza prywatnego i publicznego
private_key = nacl.signing.SigningKey.generate()
public_key = private_key.verify_key

# Przykładowa wiadomość
message = b"Hello, world!"
print("Wiadomość:", message)

# Zakodowanie wiadomości kluczem prywatnym
signed_message = private_key.sign(message)
print("Zakodowana wiadomość:", signed_message)

# Tworzenie hasha wiadomości
hash_message = nacl.hash.sha256(message)

# Zaszyfrowanie hasha wiadomości kluczem prywatnym
sealed_box = nacl.secret.SecretBox(private_key.encode())
encrypted_hash = sealed_box.encrypt(hash_message)
print("Zaszyfrowany hash wiadomości:", encrypted_hash)


# Odszyfrowanie wiadomości kluczem publicznym
try:
    verified_message = public_key.verify(signed_message)
    print("Odszyfrowana wiadomość:", verified_message)
except nacl.exceptions.BadSignatureError:
    print("Błąd: Podpis nieprawidłowy.")

# Odszyfrowanie hasha wiadomości kluczem publicznym
opened_box = nacl.secret.SecretBox(public_key.encode())
try:
    decrypted_hash = opened_box.decrypt(encrypted_hash)
    print("Odszyfrowany hash wiadomości:", decrypted_hash)
except nacl.exceptions.CryptoError:
    print("Błąd: Odszyfrowanie nie powiodło się.")





