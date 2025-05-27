from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from json import loads

app = Flask(__name__)
CORS(app)

def checaatributo(json):
    items = json["items"][0]["values"]
    atributoJson = []
    chavesatributoJson = []
    atributoJsonInterno = []
    chavesJsonInterno = []
    for item in items:

        try:
            teste = loads(items[item])              # Tenta transformar o valor em dict ou list
            if type(teste).__name__ == 'list':      # verifica se o tipo é igual a list 
                atributoJson.append(item)           # adiciona no array atributoJson

                for valores in teste:                     # navega no atributo JSON
                    for valor in valores:                 # navega nas chaves do atributo Json
                        chavesatributoJson.append(valor)  # adiciona essas chaves no array chavesJsonIn

                        if type(valores[valor]).__name__ == 'list':     #verifica se algum dos valores dentro do atributo JSON também é um Json
                            atributoJsonInterno.append(valor)
                            for coisa in valores[valor][0]:             # caso sim, navega por esse item
                                   chavesJsonInterno.append(coisa)       # adiciona ele no array lista chavesJsonInJson

        except:
            pass
    
    if atributoJson:
        conteudo = {
        "atribujoJson": atributoJson,
        "chavesAtributoJson": chavesatributoJson,
        "atributoJsonInterno": atributoJsonInterno,
        "chavesJsonInterno": chavesJsonInterno
        }
        return conteudo

    else:
        return False


def chavesJson(json):
    try:
        keys = json["items"][0]["keys"]
        values = json["items"][0]["values"]

        atributos = []
        primaryKeys = []

        for key in keys:
            primaryKeys.append(key)

        for value in values:
            atributos.append(value)

        verificacao = checaatributo(json)

        if verificacao:
            return {
                "id": primaryKeys,
                "atributos": atributos,
                "atributojson": verificacao["atribujoJson"],
                "chaveatributojson": verificacao["chavesAtributoJson"],
                "atributoJsonInterno": verificacao["atributoJsonInterno"],
                "chavesJsonInterno": verificacao["chavesJsonInterno"],
                "codigo": 200
            }
        else: 
            return {
                "id": primaryKeys,
                "atributos": atributos,
                "codigo": 200
            }
    except:
       return {"msg": "A Data Extension fornecida está vazia ou não contém atributos! :/", "codigo": 400}


@app.route("/dataextension", methods=["POST"])
def getDE():

    dados = request.json
    clientId = dados.get("client_id")
    clientSecret = dados.get("client_secret")
    mid = dados.get("mid")
    externalKey = dados.get("external_key")
    
    urlToken = 'https://mc5xbd7xlshs20w0l7rx9c47l2q1.auth.marketingcloudapis.com/v2/token'
    payload = {
        "grant_type": "client_credentials",
        "client_id": clientId,
        "client_secret": clientSecret,
        "account_id": mid
    }

    response = requests.post(urlToken, json=payload)
    token = response.json()["access_token"]

    #externalKey = '9280E31B-9E86-49AA-8852-2561E098A5D7'
    urlDe = f'https://mc5xbd7xlshs20w0l7rx9c47l2q1.rest.marketingcloudapis.com/data/v1/customobjectdata/key/{externalKey}/rowset'

    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    resposta = requests.get(urlDe, headers=headers)
    json_resposta = resposta.json()

    chaves = chavesJson(json_resposta)

    if chaves["codigo"] == 200:
        return jsonify(chaves), chaves["codigo"]
    else:
        return jsonify(chaves["msg"]), chaves["codigo"]

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)