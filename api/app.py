from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Rota que faz o proxy para a API externa
@app.route('/api/auth/signin', methods=['POST'])
def proxy_signin():
    try:
        # Dados recebidos do frontend
        data = request.json

        # Requisição para a API externa
        response = requests.post(
            'https://api.millanobroker.com/api/auth/signin',
            json=data,  # Passa os dados do frontend como JSON
            headers={'Content-Type': 'application/json'}
        )

        # Retorna a resposta da API externa para o frontend
        return jsonify(response.json()), response.status_code

    except Exception as e:
        # Trata erros e retorna mensagem amigável
        return jsonify({'error': 'Erro ao conectar com a API externa', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)