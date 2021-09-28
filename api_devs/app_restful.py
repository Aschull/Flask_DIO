from flask import Flask, request, json
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)

devs = [
    {"id":0, "name": "Andrews", "habilidades": ["Python", "Flask"]},
    {"id":1, "name": "Schulla", "habilidades": ["Python", "Java"]}
]

class Dev(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            msg = 'Desenvolvedor não encontrado pelo id informado'.format(id)
            response ={'Status error':'404', 'Message':msg}
        except Exception:
            msg = 'Erro desconhecido'
            response ={'Status error':'ERROR', 'Message':msg}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados

        return dados
    
    def delete(self, id):
        devs.pop(id)

        return {"Status":"Sucesso", "Mensagem":"Resgitro excluído"}

class ListaDevs(Resource):
    def get(self):
        try:
            response = devs
        except Exception:
            msg = 'Erro desconhecido'
            response ={'Status error':'ERROR', 'Message':msg}
        return response

    def post(self):
        dados = json.loads(request.data)
        pos = len(devs)
        dados['id'] = pos
        devs.append(dados)

        return (devs[pos])

api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(ListaDevs, '/dev/')

        
if __name__ == '__main__':
    app.run(debug=True)