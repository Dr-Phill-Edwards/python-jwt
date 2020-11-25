import os
from flask import Flask, request
from jwt.jwks import JWKS

jwks = JWKS('https://' + os.environ['OKTA_DOMAIN'] + '/oauth2/default/v1/keys')
print(str(jwks))

app = Flask(__name__, static_url_path='', static_folder='client')

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return app.send_static_file(path)

@app.route('/api/messages', methods=['POST'])
def messages():
    request.headers.get('Authorization')
    request.form.get('message')

app.run(host='0.0.0.0', port=8080)
