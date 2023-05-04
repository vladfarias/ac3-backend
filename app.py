from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/home', methods=['GET'])
def home():
    return 'Esta é a tela HOME 🏚️'

@app.route('/contato', methods=['POST'])
def contato():
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    reclamacao = request.get_json()
    reclamacao['id'] = str(uuid.uuid4())
    data.append(reclamacao)

    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

    return 'Reclamação recebida! Agurade nosso contato'

if __name__ =='__main__':
    app.run(port=5000, debug=True)
