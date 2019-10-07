#Master controller.
#In charge of feeding the modules with test vectors properly formated,
#recopilating the timing data and show significative data obtanied
#from it. 
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


##block for test_vector loading
##asume the format of the files is just a 1 test vector by row
##each testing group shares a test_vector
with open("signature_vectors.elf") as tv:
	sign_vectors = tv.readlines()
sign_vectors = [bytes.fromhex(x.strip()) for x in sign_vectors]
tv.close()

with open("block_vectors.elf") as tv:
	block_vectors = tv.readlines()
block_vectors = [bytes.fromhex(x.strip()) for x in block_vectors]
tv.close()

with open("hash_vectors.elf") as tv:
	hash_vectors = tv.readlines()
hash_vectors = [bytes.fromhex(x.strip()) for x in hash_vectors]
tv.close()
##

##modules testing
print("Testing arc4")
arc4_test = arc4.arc4_timer(block_vectors)
print("Testing AES-OFB")
aes_ofb_test = ofb.aes_ofb_timer(block_vectors)
print("Testing AES-CTR")
aes_ctr_test = ctr.aes_ctr_timer(block_vectors)
print("Testing DES")
des_test = des.des_timer(block_vectors)
print("Testing AES")
aes_test = aes.aes_timer(block_vectors)
print("Testing RSA-OAEP")
rsa_oaep_test = oaep.rsa_oaep_timing(block_vectors)
print("Testing MD5")
md5_test = md5.md5_timer(hash_vectors)
print("Testing SHA-1")
sha1_test = sha1.sha1_timer(hash_vectors)
print("Testing SHA-2")
sha2_test = sha2.sha256_timer(hash_vectors)
print("Testing RSA-PSS")
rsa_pss_test = pss.rsa_pss_timing(sign_vectors)
print("Testing DSA")
dsa_test = dsa.dsa_timing(sign_vectors)
##
##do something with the data
print("Average Encription time")
print(format(sum(arc4_test[0])/len(arc4_test), '.12f'))
print(format(sum(aes_ctr_test[0])/len(aes_ctr_test), '.12f'))
print(format(sum(aes_ofb_test[0])/len(aes_ofb_test), '.12f'))
print(format(sum(des_test[0])/len(des_test), '.12f'))
print(format(sum(aes_test[0])/len(aes_test), '.12f'))
print(format(sum(rsa_oaep_test[0])/len(rsa_oaep_timing), '.12f'))
print(format(sum(rsa_pss_test[0])/len(rsa_pss_test), '.12f'))
print(format(sum(dsa_test[0])/len(dsa_test), '.12f'))

print("Average Decryption time")
print(format(sum(arc4_test[1])/len(arc4_test), '.12f'))
print(format(sum(aes_ctr_test[1])/len(aes_ctr_test), '.12f'))
print(format(sum(aes_ofb_test[1])/len(aes_ofb_test), '.12f'))
print(format(sum(des_test[1])/len(des_test), '.12f'))
print(format(sum(aes_test[1])/len(aes_test), '.12f'))
print(format(sum(rsa_oaep_test[1])/len(rsa_oaep_timing), '.12f'))
print(format(sum(rsa_pss_test[1])/len(rsa_pss_test), '.12f'))
print(format(sum(dsa_test[1])/len(dsa_test), '.12f'))


print("Average Hashing time")
print(format(sum(md5_test)/len(md5_test), '.12f'))
print(format(sum(sha1_test)/len(sha1_test), '.12f'))
print(format(sum(sha2_test)/len(sha2_test), '.12f'))

##creating csv files for each test
with open ('Results/arc4.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in arc4_test:
		csv_res.writerow(row)

with open ('Results/aes_ctr.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in aes_ctr_test:
		csv_res.writerow(row)

with open ('Results/aes_ofb.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in aes_ofb_test:
		csv_res.writerow(row)

with open ('Results/des.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in des_test:
		csv_res.writerow(row)

with open ('Results/aes.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in aes_test:
		csv_res.writerow(row)
		
with open ('Results/rsa_oaep.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Encryption time', 'Decryption Time'])
	for row in rsa_oaep_test:
		csv_res.writerow(row)

with open ('Results/md5.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Hashing time'])
	for row in md5_test:
		csv_res.writerow([row])

with open ('Results/sha1.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Hashing time'])
	for row in sha1_test:
		csv_res.writerow([row])
		
with open ('Results/sha2.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Hashing time'])
	for row in sha2_test:
		csv_res.writerow([row])

with open ('Results/rsa_pss.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Signature time', 'Verification Time'])
	for row in rsa_pss_test:
		csv_res.writerow(row)

with open ('Results/des.csv', 'w') as out:
	csv_res = csv.writer(out)
	csv_res.writerow(['Signature time', 'Verification Time'])
	for row in des_test:
		csv_res.writerow(row)
