import base64
from datetime import datetime
import json

class JWT:
    def __init__(self, token):
        parts = token.split('.')
        self.payload = parts[0] + '.' + parts[1]
        header = self.decode64(parts[0])
        self.kid = header['kid']
        self.alg = header['alg']
        claims = self.decode64(parts[1])
        self.iss = claims['iss']
        self.aud = claims['aud']
        self.iat = claims['iat']
        self.signature = base64.urlsafe_b64decode(parts[2] + '===')

    def __str__(self):
        iat = datetime.fromtimestamp(self.iat).isoformat()
        return 'kid={self.kid} alg={self.alg} iss={self.iss} aud={self.aud} iat={iat}'.format(self=self, iat=iat)

    def decode64(self, b64):
        return json.loads(base64.urlsafe_b64decode(b64 + '==='))
