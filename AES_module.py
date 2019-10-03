#AES
import sys
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from timeit import default_timer as timer


def aes_timer(test_vectors):
	"""Encrypts (AES) each element of test_vector with a padding (256 bits) 
		and returns a list of tuples with (encryption time, decryption time) """
	timelist = []
	for vector in test_vectors: #test_vector elements are of byte type
		#key generation, we opted for generating our own keys and not using the provided at the test vectors
		key = secrets.token_bytes(32) #secrets provides the most secure pseudo-random function the os has
		#print(key)
		iv = secrets.token_bytes(32)
		#print(iv)
		#end of key generation
		#creating a cipher object
		aes = algorithms.AES(key)
		aes.block_size = 256
		cipher = Cipher(aes, modes.CBC(iv), backend = default_backend())
		#creating padding object
		padder = padding.PKCS7(256).padder()
		encryptor = cipher.encryptor()
		#encryption begins
		start_e = timer()
		padded_m = padder.update(vector) + padder.finalize() #padding is included in the process as instructed
		ciphertext = encryptor.update(padded_m) + encryptor.finalize()
		end_e = timer()
		#encryption ends -this is the fragment we should time for encryption time
		#print("ciphertext: " + str(ciphertext.hex()))
		decryptor = cipher.decryptor()
		unpadder = padding.PKCS7(256).unpadder() #unpadding object
		#decryption begins
		start_d = timer()
		plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
		data = unpadder.update(plaintext_d) + unpadder.finalize() #unpadding result
		end_d = timer()
		#decryption ends -this is the fragment we should time for decryption time
		#print("Deciphered text: "+ str(data))
		timelist.append((end_e - start_e, end_d - start_d))
	return timelist

