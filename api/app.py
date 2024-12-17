from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Rota que faz o proxy para a API externa
@app.route('/users', methods=['POST'])
def usersEduardo():
    try:
        # Dados recebidos do frontend
        data = request.json

        # Requisição para a API externa
        response = requests.post(
            'https://api.millanobroker.com/api/auth/signin',
            json=data,  # Passa os dados do frontend como JSON
            headers={'Content-Type': 'application/json'}
        )

        token = response.headers['Set-Cookie'].split(';')[0]

        # Retorna a resposta da API externa para o frontend
        return jsonify(token), response.status_code

    except Exception as e:
        # Trata erros e retorna mensagem amigável
        return jsonify({'error': 'Erro ao conectar com a API externa', 'details': str(e)}), 500

# Rota que faz o proxy para a API externa
@app.route('/balances', methods=['POST'])
def balancesEduardo():
    try:
        token = request.json['token']

        # Configurar o cabeçalho da requisição
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'cookie': token
        }

        # Requisição para a API externa
        response = requests.get('https://api.millanobroker.com/api/user/balances', headers=headers)

        balances = list(dict(response.json())['data'])

        for balance in balances:
            if balance['type'] == 'REAL':
                return jsonify({'balance': balance['balance']}), 200
        return jsonify({}), 401

    except Exception as e:
        # Trata erros e retorna mensagem amigável
        return jsonify({'error': 'Erro ao conectar com a API externa', 'details': str(e)}), 500


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, port=10001)
=======
    app.run(debug=True, port=10000)
>>>>>>> 2183fe8dbef7bbd6cc19f9860b653918a6f5e7f2
