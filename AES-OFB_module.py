#AES-OFB
import sys
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from timeit import default_timer as timer

def aes_ofb_timer(test_vectors):
	"""Encrypts (AES-OFB) each element of test_vector and returns a list of tuples with (encryption time, decryption time) """
	timelist = []
	for vector in test_vectors: #test_vector elements are of byte type
		#key generation, we opted for generating our own keys and not using the provided at the test vectors
		key = secrets.token_bytes(32) #secrets provides the most secure pseudo-random function the os has
		iv = secrets.token_bytes(32) #iv for OFB, must be the same size as the block size
		#print(key)
		#print(iv)
		#end of key generation
		#creating a cipher object
		aes = algorithms.AES(key)
		aes.block_size = 256
		cipher = Cipher(aes, modes.OFB(iv), backend = default_backend())
		encryptor = cipher.encryptor()
		#encryption begins
		start_e = timer()
		ciphertext = encryptor.update(vector) + encryptor.finalize()
		end_e = timer()
		print(len(ciphertext.hex()))
		#encryption ends -this is the fragment we should time for encryption time
		print("ciphertext: " + str(ciphertext.hex()))
		decryptor = cipher.decryptor()
		#decryption begins
		start_d = timer()
		plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
		end_d = timer()
		#decryption ends -this is the fragment we should time for decryption time
		print("Deciphered text: "+ str(plaintext_d))
		timelist.append((end_e - start_e, end_d - start_d))
	return timelist


benin = [b"stre", b"thisisateststreamjusttoseeifthisworks", b"yayitworks"]
print(aes_ofb_timer(benin))