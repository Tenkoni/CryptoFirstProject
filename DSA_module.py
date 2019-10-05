#DSA
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from timeit import default_timer as timer

def dsa_timing(test_vectors):
	"""Signs (DSA) each element of test_vector and returns a list of tuples with (signature time, verifying time) """
	timelist = []
	for vector in test_vectors:
		#key generation
		private_key = dsa.generate_private_key(key_size = 1024, backend = default_backend())
		public_key = private_key.public_key()
		#signing starts
		start_s = timer()
		signature = private_key.sign(vector, hashes.SHA256())
		end_s = timer()
		print(signature.hex())
		#signing ends
		#veryifing starts
		start_v = timer()
		try:
			public_key.verify(signature, vector, hashes.SHA256())
		except:
			print("Invalid Signature!!")
		end_v = timer()
		#verifying ends
		timelist.append((end_s - start_s, end_v - start_v))
	return timelist


testo = [b"signature testing", b"also another signature testing", b"and yet we have another test of this signature algorithm named DSA"]
print(dsa_timing(testo))