#RSA-OAEP
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from timeit import default_timer as timer

def rsa_oaep_timing(test_vectors):
	"""Encrypts (RSA-OAEP) each element of test_vector and returns a list of tuples with (encryption time, decryption time) """
	timelist = []
	for vector in test_vectors:
		#key generation
		private_key = rsa.generate_private_key(public_exponent = 65537, key_size =2048, backend = default_backend())
		public_key = private_key.public_key()
		paddington = padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()), algorithm = hashes.SHA256(), label = None) #padding scheme
		#encryption starts
		start_e = timer()
		ciphertext = public_key.encrypt(vector, paddington)
		end_e = timer()
		#encryption ends
		print(ciphertext)
		print("Bytes = " + str(len(ciphertext) * 8))
		#decryption starts
		start_d = timer()
		plaintext = private_key.decrypt(ciphertext, paddington)
		end_d = timer()
		#decryption ends
		print(plaintext)
		timelist.append((end_e - start_e, end_d - start_d))
	return timelist


benin = [b"sttre", b"thisisateststreamjusttoseeifthisworks", b"yayitworks"]
print(rsa_oaep_timing(benin))

