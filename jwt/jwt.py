import base64
from datetime import datetime
import json

class JWT:
    def __init__(self, token, claims = {}, max_age = 365):
        parts = token.split('.')
        self.payload = parts[0] + '.' + parts[1]
        header = self.decode64(parts[0])
        self.process_header(header)
        claimset = self.decode64(parts[1])
        self.process_claims(claimset, claims, max_age * 24 * 3600)
        self.signature = base64.urlsafe_b64decode(parts[2] + '===')

    def __str__(self):
        iat = datetime.fromtimestamp(self.iat).isoformat()
        return 'kid={self.kid} alg={self.alg} iss={self.iss} aud={self.aud} iat={iat}'.format(self=self, iat=iat)

    def decode64(self, b64):
        return json.loads(base64.urlsafe_b64decode(b64 + '==='))

    def process_header(self, header):
        self.kid = header['kid']
        self.alg = header['alg']
        if (self.alg != 'RS256') :
            raise Exception('alg must be RS256 not ' + self.alg)

    def process_claims(self, claimset, claims, max_age):
        self.iss = claimset['iss']
        if 'iss' in claims and self.iss != claims['iss']:
            raise Exception('iss must be ' + claims['iss'])
        self.aud = claimset['aud']
        if 'aud' in claims and self.aud != claims['aud']:
            raise Exception('aud must be ' + claims['aud'])
        self.iat = claimset['iat']
        now = datetime.now().timestamp()
        if abs(now - self.iat) > max_age:
            raise Exception('token out of date')

