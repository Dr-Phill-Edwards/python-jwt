from datetime import datetime
from hashlib import sha256
import json
from jwt.jwk import JWK
import os
from tornado.httpclient import HTTPClient

class JWKS:
    def __init__(self, url):
        self.keys = {}
        keys = self.loadFromUrl(url)
        for key in keys['keys']:
            jwk = JWK(key)
            self.keys[jwk.kid] = jwk

    def loadFromUrl(self, url):
        httpClient = HTTPClient()
        response = httpClient.fetch(url)
        keys = json.loads(response.body)
        httpClient.close()
        return keys

    def __str__(self):
        result = 'JWKS\n'
        for key in self.keys:
            result = result + '\t' + str(key) + '\n'
        return result
    
    def verify(self, jwt):
        return self.keys[jwt.kid].verify(jwt)

