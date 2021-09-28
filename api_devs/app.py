from flask import Flask, jsonify, request, json

app = Flask(__name__)

devs = [
    {"id":0, "name": "Andrews", "habilidades": ["Python", "Flask"]},
    {"id":1, "name": "Schulla", "habilidades": ["Python", "Java"]}
]

## Retorna, Altera e Deleta Desenvolvedro pelo id.
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            msg = 'Desenvolvedor não encontrado pelo id informado'.format(id)
            response ={'Status error':'404', 'Message':msg}
        except Exception:
            msg = 'Erro desconhecido'
            response ={'Status error':'ERROR', 'Message':msg}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({"Status":"Sucesso", "Mensagem":"Resgitro excluído"})

## Retorna todos os Desenvolvedores
@app.route('/dev/', methods=['GET', 'POST'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)
        return jsonify(devs[pos])
    
    elif request.method == 'GET':
        return jsonify(devs)

if __name__ == '__main__':
    app.run(debug=True)