#AES
import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def aes_timer(test_vectors):
	"""Encrypts (AES) each element of test_vector with a padding (256 bits) 
		and returns a list of tuples with (encryption time, decryption time) """
	for vector in test_vectors: #test_vector elements are of byte type
		#key generation, we opted for generating our own keys and not using the provided at the test vectors
		key = secrets.token_bytes(32) #secrets provides the most secure pseudo-random function the os has
		print(key)
		iv = secrets.token_bytes(16)
		print(iv)
		#end of key generation
		#creating a cipher object
		cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
		#creating padding object
		padder = padding.PKCS7(256).padder()
		encryptor = cipher.encryptor()
		#encryption begins
		padded_m = padder.update(vector) + padder.finalize() #padding is included in the process as instructed
		ciphertext = encryptor.update(padded_m) + encryptor.finalize()
		#encryption ends -this is the fragment we should time for encryption time
		#print("ciphertext: " + str(ciphertext))
		decryptor = cipher.decryptor()
		unpadder = padding.PKCS7(256).unpadder() #unpadding object
		#decryption begins
		plaintext_d = decryptor.update(ciphertext) + decryptor.finalize()
		data = unpadder.update(plaintext_d) + unpadder.finalize() #unpadding result
		#decryption ends -this is the fragment we should time for decryption time
		print("Deciphered text: "+ str(data))


