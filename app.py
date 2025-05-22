from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def chavesJson(json):
    try:
        items = json["items"]
        listaChaves = list(items[0]["values"].keys())

        dicioChaves = {}

        for chaves in listaChaves:
            dicioChaves[chaves] = chaves

        return {"msg": dicioChaves, "codigo": 200}
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

    return jsonify(chaves["msg"]), chaves["codigo"]

if __name__ == '__main__':
    app.run(port=3000, debug=True)