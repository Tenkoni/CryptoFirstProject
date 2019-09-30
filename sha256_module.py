#sha-2 module
from timeit import default_timer as timer
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


def sha256_timer(test_vectors): #the test_vector must have ONLY bytes-type elements
    """Hash each element of test_vector and returns a list with execution times"""
	time_list = [] #list to save each execution time
	for vector in test_vectors:
		start = timer()
		digest = hashes.Hash(hashes.SHA256(), backend = default_backend()) #initialize hash digest
		digest.update(vector) #hash vector
		a = digest.finalize() #output hash
		end = timer()
		#print(str(vector)+" ->" + str(a.hex())) #aux to verify proper hashing
		time_list.append(end-start)
	return(time_list)
