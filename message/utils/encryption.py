from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hmac
import hashlib
import os

def encrypt_message(content, key):
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, content.encode(), None)
    return nonce + ciphertext

def decrypt_message(ciphertext, key):
    nonce = ciphertext[:12]
    ciphertext = ciphertext[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None).decode()

def sign_message(content, key):
    return hmac.new(key, content.encode(), hashlib.sha256).hexdigest()

def verify_message(content, signature, key):
    return hmac.compare_digest(sign_message(content, key), signature)