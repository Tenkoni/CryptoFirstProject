import csv

import des_module as des
import AES_module as aes
ctr = __import__ ('AES-CTR_module')
ofb = __import__ ('AES-OFB_module')
import arc4_module as arc4
import sha1_module as sha1
import sha256_module as sha2
import md5_module as md5
oaep = __import__ ('RSA-OAEP_module')
pss = __import__ ('RSA-PSS_module')
import DSA_module as dsa

with open("signature_vectors.elf") as tv:
	sign_vectors = tv.readlines()
sign_vectors = [bytes.fromhex(x.strip()) for x in sign_vectors]
tv.close()

print("Testing DSA")
dsa_test = dsa.dsa_timing(sign_vectors)


print(format(sum(dsa_test[0])/len(dsa_test), '.12f'))
print(format(sum(dsa_test[1])/len(dsa_test), '.12f'))

dsa_test = [(format(x[0], '.22f'), format(x[1], '.22f')) for x in dsa_test]


with open ('Results/dsa.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Signature time', 'Verification Time'])
	for row in dsa_test:
		csv_res.writerow(row)