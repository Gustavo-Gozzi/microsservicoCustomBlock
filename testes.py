json = {
    "count": 9,
    "customObjectId": "0f47daab-ea19-ef11-a5c4-5cba2c704e68",
    "customObjectKey": "D78357C0-A392-4539-B069-6D4B0DFEE56D",
    "items": [
        {
            "keys": {
                "id": "121215454542121"
            },
            "values": {
                "celular": "5511954333394",
                "dataentrada": "6/23/2024 12:00:00 AM",
                "email": "amanda.massari@gentrop.com",
                "ferias": "False",
                "firstname": "Amanda",
                "imagem": "https://image.s7.sfmc-content.com/lib/fe8d1372726d057c72/m/1/4194aec3-b1c4-4cf5-a546-3ffdd9351fda.jpg",
                "lastname": "Massari",
                "local": "pt-br",
                "niver": "6/13/2005 12:00:00 AM",
                "optin": "True",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "arthur.damasceno@gentrop.com"
            },
            "values": {
                "celular": "5511943201278",
                "dataentrada": "5/8/2024 12:00:00 AM",
                "email": "arthur.damasceno@gentrop.com",
                "ferias": "True",
                "firstname": "Arthur",
                "imagem": "",
                "lastname": "Morila",
                "local": "pt-br",
                "niver": "6/29/2007 12:00:00 AM",
                "optin": "True",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "Gab_Xereguim01"
            },
            "values": {
                "celular": "5511933019606",
                "dataentrada": "6/15/2024 12:00:00 AM",
                "email": "gabriel.xereguim@gentrop.com",
                "ferias": "False",
                "firstname": "Gabriel",
                "imagem": "https://image.s7.sfmc-content.com/lib/fe8d1372726d057c72/m/1/8f15364e-2264-4ee0-aa53-a585e49638da.jpeg",
                "lastname": "Xereguim",
                "local": "pt-br",
                "niver": "6/13/2001 12:00:00 AM",
                "optin": "True",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "gio123"
            },
            "values": {
                "celular": "5515996919166",
                "dataentrada": "6/1/2024 12:00:00 AM",
                "email": "giovana.souza@gentrop.com",
                "ferias": "False",
                "firstname": "Giovana",
                "imagem": "",
                "lastname": "Faria",
                "local": "pt-br",
                "niver": "5/22/2010 12:00:00 AM",
                "optin": "False",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "Maria_Eduarda01"
            },
            "values": {
                "celular": "5511956852642",
                "dataentrada": "",
                "email": "maria.eduarda@gentrop.com",
                "ferias": "False",
                "firstname": "Maria",
                "imagem": "https://image.s7.sfmc-content.com/lib/fe8d1372726d057c72/m/1/119f50be-f6a2-45ef-a2d7-a33b4e6fa778.jpeg",
                "lastname": "Souza",
                "local": "pt-br",
                "niver": "6/13/2005 12:00:00 AM",
                "optin": "True",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "VLM2023"
            },
            "values": {
                "celular": "5543996230194",
                "dataentrada": "6/19/2024 12:00:00 AM",
                "email": "vitor.machado@gentrop.com",
                "ferias": "True",
                "firstname": "Vitor",
                "imagem": "",
                "lastname": "Leandro",
                "local": "pt-br",
                "niver": "",
                "optin": "",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "A12345z7"
            },
            "values": {
                "celular": "5511972369990",
                "dataentrada": "",
                "email": "gustavo.gozzi@gentrop.com",
                "ferias": "False",
                "firstname": "Gustavo",
                "imagem": "",
                "lastname": "Gozzi",
                "local": "pt-br",
                "niver": "",
                "optin": "",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "7abc"
            },
            "values": {
                "celular": "5518997025655",
                "dataentrada": "",
                "email": "renan.buarraj@gentrop.com",
                "ferias": "True",
                "firstname": "Renan",
                "imagem": "",
                "lastname": "Buarraj",
                "local": "pt-br",
                "niver": "",
                "optin": "",
                "personas": ""
            }
        },
        {
            "keys": {
                "id": "vitor_hugo001"
            },
            "values": {
                "celular": "5511933834009",
                "dataentrada": "",
                "email": "vitor.andrade@gentrop.com",
                "ferias": " True",
                "firstname": "Vitor",
                "imagem": "",
                "lastname": " Andrade",
                "local": "pt-br",
                "niver": "",
                "optin": "",
                "personas": ""
            }
        }
    ],
    "links": {
        "self": "/v1/customobjectdata/token/e8dc6eb4-8d29-48f9-b715-4bc99cafb879/rowset?$page=1"
    },
    "page": 1,
    "pageSize": 2500,
    "requestToken": "e8dc6eb4-8d29-48f9-b715-4bc99cafb879",
    "tokenExpireDateUtc": "2025-05-23T18:26:43.697",
    "top": 0
}
def chavesJson(json):
    items = json["items"]
    listaChaves = list(items[0]["values"].keys())

    dicioChaves = {}

    for chaves in listaChaves:
        dicioChaves[chaves] = chaves

    return dicioChaves

bombardino = chavesJson(json)
print(bombardino)
