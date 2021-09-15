from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#@app.route("/<numero>", methods=['GET', 'POST'])
@app.route("/<int:id>")
def pessoas(id):
#    return 'Ola mundo. {}'.format(numero)
    return jsonify({'id': id, 'nome':'Andrews', 'profissao': 'dev'})

#Função passando valores pela URL
@app.route("/soma/<int:valor1>/<int:valor2>")
def somaURL(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})

#Função passando valores pelo body(json)
@app.route("/soma", methods = ['POST'])
def somaBody():
    dados = json.loads(request.data)
    total = sum(dados['valores'])

    print (dados)
    return jsonify({'soma': total})





if __name__ == '__main__':
    app.run(debug=True)
