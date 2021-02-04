import Crypto.Cipher.AES as AES
import random
import sys
import secrets
import string

with open(sys.argv[1], 'rb') as f:
    source_code = f.read()


key = secrets.token_bytes(16)
iv = secrets.token_bytes(16)

xor_key_lenght = random.randint(5, 20)
xor_key = secrets.token_bytes(xor_key_lenght)

key_crypt = []
iv_crypt = []

for i in range(16):
    key_crypt.append(key[i] ^ xor_key[i % xor_key_lenght])
    iv_crypt.append(iv[i] ^ xor_key[i % xor_key_lenght])





def get_random_name():
    return random.choice(string.ascii_uppercase + string.ascii_lowercase) + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(random.randint(5, 17)))

enc_data = AES.new(key, AES.MODE_CFB, iv).encrypt(source_code)


name_aes = get_random_name()
name_xor_key = get_random_name()
name_xor_key_aes = get_random_name()
name_xor_key_iv = get_random_name()
name_decrypt_aes_key = get_random_name()
name_decrypt_aes_iv = get_random_name()
name_encrypt_data = get_random_name()
name_decrypt_data = get_random_name()


gen_code = ''
gen_code += 'from Crypto.Cipher import AES as %s' % name_aes #import AES
gen_code += '\n'
gen_code += '\n'
gen_code += '%s = %s\n' % (name_encrypt_data, enc_data) #encrypting data
gen_code += '%s = %s' % (name_xor_key, xor_key) #xor key
gen_code += '\n'
gen_code += '%s = %s\n' % (name_xor_key_aes, str(key_crypt))# encrypted key aes
gen_code += '%s = %s\n' % (name_xor_key_iv, str(iv_crypt))# encrypted key aes
gen_code += '%s = []\n' % (name_decrypt_aes_iv)
gen_code += '%s = []\n' % (name_decrypt_aes_key)#list for decrypting aes key
gen_code += 'for i in range(len(%s)):\n' % name_xor_key_aes #name 
gen_code += '    %s.append(%s[i] ^ %s[i %% len(%s)])\n' % (name_decrypt_aes_key, name_xor_key_aes, name_xor_key, name_xor_key)
gen_code += '    %s.append(%s[i] ^ %s[i %% len(%s)])\n' % (name_decrypt_aes_iv, name_xor_key_iv, name_xor_key, name_xor_key)
gen_code += '\n'
gen_code += '%s = %s.new(bytes(%s), %s.MODE_CFB, bytes(%s)).decrypt(%s)\n' %(name_decrypt_data, name_aes, name_decrypt_aes_key, name_aes, name_decrypt_aes_iv, name_encrypt_data)
gen_code += 'print(%s)' % name_decrypt_data
with open('generated_code.py', 'w') as f:
    f.write(gen_code)
print(gen_code)