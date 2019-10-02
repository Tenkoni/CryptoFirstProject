#AES
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

#key generation, we opted for generating our own keys and not using the provided at the test vectors
key = secrets.token_bytes(32)
print(key)
iv = secrets.token_bytes(16)
print(iv)
padder = padding.PKCS7(256).padder()
padded_m = padder.update(b"Shine on you, crazy diamond!") + padder.finalize()
print(b"Shine on you, crazy diamond!")
print(padded_m)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_m) + encryptor.finalize()
print("ciphertext: " + str(ciphertext))
decryptor = cipher.decryptor()
plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
print("Deciphered text with padd: "+ str(plaintext_d))
unpadder = padding.PKCS7(256).unpadder()
data = unpadder.update(plaintext_d) + unpadder.finalize()
print("Unpadded dec: " + str(data))

