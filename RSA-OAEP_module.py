#RSA-OAEP
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from timeit import default_timer as timer

#key generation
private_key = rsa.generate_private_key(public_exponent = 65537, key_size =2048, backend = default_backend())
public_key = private_key.public_key()
plaintext = b"testin'"

paddington = padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()), algorithm = hashes.SHA256(), label = None) #padding scheme
ciphertext = public_key.encrypt(plaintext, paddington)
print(ciphertext)
print("Bytes = " + str(len(ciphertext) * 8))
plaintext = private_key.decrypt(ciphertext, paddington)
print(plaintext)
