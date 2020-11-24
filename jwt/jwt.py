import base64
import json

class JWT:
    def __init__(self, token):
        parts = token.split('.')
        header = self.decode64(parts[0])
        self.kid = header['kid']
        self.alg = header['alg']
        claims = self.decode64(parts[1])
        self.iss = claims['iss']
        self.aud = claims['aud']

    def __str__(self):
        return 'kid={self.kid} alg={self.alg} iss={self.iss} aud={self.aud}'.format(self=self)

    def decode64(self, b64):
        return json.loads(base64.b64decode(b64 + '==='))
