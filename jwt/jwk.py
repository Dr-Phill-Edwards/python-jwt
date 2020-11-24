import base64

class JWK:
    def __init__(self, jwk):
        self.alg = jwk['alg']
        self.kid = jwk['kid']
        self.e = int.from_bytes(base64.urlsafe_b64decode(jwk['e']), byteorder='big')
        self.n = jwk['n']

    def __str__(self):
        return 'kid={self.kid} alg={self.alg} e={self.e} n={self.n}'.format(self=self)
