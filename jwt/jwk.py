import base64
from datetime import datetime
from hashlib import sha256

class JWK:
    def __init__(self, jwk):
        self.alg = jwk['alg']
        self.kid = jwk['kid']
        self.e = int.from_bytes(base64.urlsafe_b64decode(jwk['e']), byteorder='big')
        self.n = int.from_bytes(base64.urlsafe_b64decode(jwk['n'] + '==='), byteorder='big')

    def __str__(self):
        return 'kid={self.kid} alg={self.alg} e={self.e} n={self.n}'.format(self=self)
    
    def verify(self, jwt):
        now = datetime.now()
        hash = int.from_bytes(sha256(jwt.payload.encode('utf-8')).digest(), byteorder='big')
        print(hash)