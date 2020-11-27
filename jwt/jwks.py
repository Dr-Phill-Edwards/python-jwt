import json
from jwt.jwk import JWK
import requests

class JWKS:
    def __init__(self, url):
        self.keys = {}
        response = requests.get(url)
        keys = json.loads(response.text)
        for key in keys['keys']:
            jwk = JWK(key)
            self.keys[jwk.kid] = jwk

    def __str__(self):
        result = 'JWKS\n'
        for key in self.keys.values():
            result = result + '\t' + str(key) + '\n'
        return result
    
    def verify(self, jwt):
        if jwt.kid not in self.keys:
            raise Exception('Invalid kid')
        self.keys[jwt.kid].verify(jwt)

