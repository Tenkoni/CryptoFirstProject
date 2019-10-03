#RC4
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from timeit import default_timer as timer

def arc4_timer(test_vectors):
	"""Encrypts (Alleged-RC4) each element of test_vector and returns a list of tuples with (encryption time, decryption time) """
	timelist = []
	for vector in test_vectors: #test_vector elements are of byte type
		#key generation, we opted for generating our own keys and not using the provided at the test vectors
		key = secrets.token_bytes(32) #secrets provides the most secure pseudo-random function the os has
		#print(key)
		#end of key generation
		#creating a cipher object
		cipher = Cipher(algorithms.ARC4(key), mode = None, backend = default_backend())
		encryptor = cipher.encryptor()
		#encryption begins
		start_e = timer()
		ciphertext = encryptor.update(vector) + encryptor.finalize()
		end_e = timer()
		#encryption ends -this is the fragment we should time for encryption time
		#print("ciphertext: " + str(ciphertext))
		decryptor = cipher.decryptor()
		#decryption begins
		start_d = timer()
		plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
		end_d = timer()
		#decryption ends -this is the fragment we should time for decryption time
		#print("Deciphered text: "+ str(plaintext_d))
		timelist.append((end_e - start_e, end_d - start_d))
	return timelist
