#RSA-PSS
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from timeit import default_timer as timer

def rsa_pss_timing(test_vectors):
	"""Signs (RSA-PSS) each element of test_vector and returns a list of tuples with (signature time, verifying time) """
	timelist = []
	for vector in test_vectors:
		#key generation
		private_key = rsa.generate_private_key(public_exponent = 65537, key_size =1024, backend = default_backend())
		public_key = private_key.public_key()
		paddington = padding.PSS(mgf = padding.MGF1(algorithm = hashes.SHA256()), salt_length = 20) #padding scheme
		#encryption starts
		start_s = timer()
		signature = private_key.sign(vector, paddington, hashes.SHA256())
		end_s = timer()
		#print(signature.hex())
		#encryption ends
		paddington = padding.PSS(mgf = padding.MGF1(algorithm = hashes.SHA256()), salt_length = 20) #if the salt is different the verifying process throws an invalid signature exception
		#decryption starts
		start_v = timer()
		try:
			public_key.verify(signature, vector, paddington, hashes.SHA256())
		except:
			print("Invalid Signature!!")
		end_v = timer()
		#decryption ends
		timelist.append((end_s - start_s, end_v - start_v))
	return timelist
