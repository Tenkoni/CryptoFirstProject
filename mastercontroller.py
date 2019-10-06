#Master controller.
#In charge of feeding the modules with test vectors properly formated,
#recopilating the timing data and show significative data obtanied
#from it. 
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
with open("test_vector_name.elf") as tv:
	test_vector1 = tv.readlines()
test_vector1 = [bytes.fromhex(x.strip()) for x in test_vector1]
##

##modules testing
arc4_test = arc4.arc4_timer(test_vector1)
aes_ofb_test = ofb.aes_ofb_timer(test_vector1)
aes_ctr_test = ctr.aes_ctr_timer(test_vector1)
des_test = des.des_timer(test_vector1)
aes_test = aes.aes_timer(test_vector1)
rsa_oaep_test = oaep.rsa_oaep_timing(test_vector1)
md5_test = md5.md5_timer(test_vector1)
sha1_test = sha1.sha1_timer(test_vector1)
sha2_test = sha2.sha256_timer(test_vector1)
rsa_pss_test = pss.rsa_pss_timing(test_vector1)
dsa_test = dsa.dsa_timing(test_vector1)
##
##do something with the data
print(arc4_test)
print(aes_ctr_test)
print(aes_ofb_test)
print(des_test)
print(aes_test)
print(rsa_oaep_test)
print(rsa_pss_test)
print(md5_test)
print(sha1_test)
print(sha2_test)
print(rsa_pss_test)
print(dsa_test)

