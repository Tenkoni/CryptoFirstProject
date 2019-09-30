#sha-2 module
from timeit import default_timer as timer
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


digest = hashes.Hash(hashes.SHA256(), backend = default_backend())
digest.update(b"a")
a = digest.finalize()
print(a.hex())
# time_list = []
# for elem in inp:
# 	start = timer()
# 	testo_funco(elem)
# 	end = timer()
# 	time_list.append(end-start)
# 	print("This time:" + str(end - start))
# print("Average time: " + str(sum(time_list)/len(time_list)))