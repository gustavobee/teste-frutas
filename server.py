from flask import Flask, jsonify, request

app = Flask(__name__)

DATA_LOJA = {"frutas": {"banana": 1, "abacaxi": 5, "manga": 8}}

@app.route("/frutas", methods=['GET'])
def get_frutas():
    id_token = request.headers.get("id-token")
    if autenticacao(id_token):
        frutas = {
            "frutas": list(DATA_LOJA["frutas"].keys()),
        }
        return jsonify(frutas)
    else:
        return jsonify({"mensagem": "Token nao autorizado"}), 401
    
@app.route("/frutas/quantidade/<nome_fruta>", methods=['GET'])
def get_quantidade_frutas(nome_fruta):
    id_token = request.headers.get("id-token")
    if autenticacao(id_token):
        return jsonify(DATA_LOJA["frutas"][nome_fruta])
    else:
        return jsonify({"mensagem": "Token nao autorizado"}), 401
    
def autenticacao(id_token):
    if id_token == "token_autorizado":
        return True
    else:
        return False
    
if __name__ == '__main__':
    app.run(debug=True)