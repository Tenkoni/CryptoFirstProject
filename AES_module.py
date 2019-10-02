#AES
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

#key generation, we opted for generating our own keys and not using the provided at the test vectors
key = secrets.token_bytes(32)
print(key)
iv = secrets.token_bytes(16)
print(iv)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"a secret message") + encryptor.finalize()
print("ciphertext: " + str(ciphertext))
decryptor = cipher.decryptor()
plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
print("Deciphered text: "+ str(plaintext_d))

