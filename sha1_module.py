#sha-1 module
from timeit import default_timer as timer
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


def sha1_timer(test_vectors): #the test_vector must have ONLY bytes-type elements
	"""Hash (sha-1) each element of test_vector and returns a list with execution times"""
	time_list = [] #list to save each execution time
	for vector in test_vectors:
		digest = hashes.Hash(hashes.SHA1(), backend = default_backend()) #initialize hash digest
		start = timer()
		digest.update(vector) #hash vector
		end = timer()
		a = digest.finalize() #output hash
		#print(str(vector)+" ->" + str(a.hex())) #aux to verify proper hashing
		time_list.append(end-start)
	return(time_list)

