#DES
import secrets
from des import DesKey
from cryptography.hazmat.primitives import padding

def des_timer(test_vectors):
	"""Encrypts (DES) each element of test_vector with a padding (64 bits) 
		and returns a list of tuples with (encryption time, decryption time)"""
	timelist = []
	for vector in test_vectors: #test_vector elements are of byte type
		#key creation for DES
		iv = secrets.token_bytes(8)
		des_instance = DesKey(secrets.token_bytes(8))
		print(des_instance.is_single())
		#creating padding instance
		padder = padding.PKCS7(64).padder()
		#encrypting begins (using CBC mode)
		padded_m = padder.update(vector) + padder.finalize() #padding is included in the process as instructed
		cyphertext = des_instance.encrypt(padded_m, initial = iv)
		#encrypting ends, timing this section
		print(str(cyphertext))
		#creating unpadding instance
		unpadder = padding.PKCS7(64).unpadder()
		#decrypting begins 
		plaintext_d = des_instance.decrypt(cyphertext, initial = iv)
		plaintext = unpadder.update(plaintext_d) + unpadder.finalize()
		#decryption ends
		print(plaintext)

benin = [b"heloelelello", b"mahler is also a great composer", b"tuturuuuuuuuuuuuuuuuuuuuuuuus"]
des_timer(benin)



