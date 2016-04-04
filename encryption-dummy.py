from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/security/v1/dukpt/encrypt/', methods=['POST'])
def encrypt():
	print(request.data)
	data = json.loads(request.data)
	plain_text = data['plainText']
	encrypted = plain_text[::-1]
	json_rsp = json.dumps({'cipherText': encrypted})
	print('encryption response: ' + encrypted)
	return json_rsp, 200
	#return jsonify(cipherText=encrypted)


@app.route('/security/v1/dukpt/decrypt/', methods=['POST'])
def decrypt():
	data = json.loads(request.data)
	encrypted_text = data['encryptedText']
	decrypted = encrypted_text[::-1]
	return jsonify(plainText=decrypted)


if __name__ == '__main__':
	app.run(port=8080)
