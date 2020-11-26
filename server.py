import os
from flask import Flask, request
from jwt.jwks import JWKS

jwks = JWKS(os.environ['OKTA_ISSUER_URI'] + '/v1/keys')
print(str(jwks))

app = Flask(__name__, static_url_path='', static_folder='client')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/<path:file>', methods=['GET'])
def serve_static(file):
    return app.send_static_file(file)

@app.route('/api/messages', methods=['POST'])
def messages():
    request.headers.get('Authorization')
    request.form.get('message')

app.run(host='0.0.0.0', port=8080)
