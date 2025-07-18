from flask import Flask, request, jsonify
from flask_cors import CORS
from maluquices import BancoDeHoras

app = Flask(__name__)  # Criando a aplicação
CORS(app, origins=["http://127.0.0.1:5500"])


# GET - pegar todos os usuários
@app.route('/calculos', methods=['POST'])
def calcular():
    dados = request.json  # pega os dados enviados
    print(dados)

    h1 =  dados['hora1'].split(':')
    h2 =  dados['hora2'].split(':')

    print(h1, h2)

    bando = BancoDeHoras()






    # return jsonify({
    #     'status': 'success',
    #     'mensagem': 'Cálculo realizado com sucesso!',
    #     'dados': dados
    # }), 201


# Rodar o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)