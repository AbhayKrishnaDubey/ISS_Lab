from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

def encrypt_message(key, nonce, plaintext):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(plaintext)

# Messages to encrypt
plaintext1 = b"This is a top secret message."
plaintext2 = b"Attack at dawn with full force!"

# Use same nonce and key (this is the vulnerability)
key = get_random_bytes(16)
nonce = get_random_bytes(8)

# Encrypt both messages
ciphertext1 = encrypt_message(key, nonce, plaintext1)
ciphertext2 = encrypt_message(key, nonce, plaintext2)

# XOR ciphertexts to simulate attacker knowledge
xor_result = bytes(a ^ b for a, b in zip(ciphertext1, ciphertext2))

# Try to recover plaintext1 if plaintext2 is known (known plaintext attack)
recovered = bytes(a ^ b for a, b in zip(xor_result, plaintext2))

print("Recovered Message 1 (from XOR & known plaintext):", recovered.decode())
