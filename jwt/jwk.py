import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from datetime import datetime

class JWK:
    def __init__(self, jwk):
        self.alg = jwk['alg']
        self.kid = jwk['kid']
        self.e = int.from_bytes(base64.urlsafe_b64decode(jwk['e']), byteorder='big')
        self.n = int.from_bytes(base64.urlsafe_b64decode(jwk['n'] + '==='), byteorder='big')
        self.publicKey = RSA.construct((self.n, self.e))

    def __str__(self):
        return 'kid={self.kid} alg={self.alg} e={self.e} n={self.n}'.format(self=self)
    
    def verify(self, jwt):
        hash = SHA256.new(str.encode(jwt.payload))
        pkcs1_15.new(self.publicKey).verify(hash, jwt.signature)
        