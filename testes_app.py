import unittest
import requests
from app import chavesJson, checaatributo

class TestStringMethods(unittest.TestCase):

    def test_001_JsonSimples(self):
        jsonSimples = {
    "count": 9,
    "customObjectId": "xxxxx",
    "customObjectKey": "xxxxx",
    "items": [
        {
            "keys": {
                "id": "123"
            },
            "values": {
                "celular": "5511912345678",
                "dataentrada": "6/23/2024 12:00:00 AM",
                "email": "fulano.ciclano@test.com",
                "ferias": "False",
                "firstname": "Fulano",
                "imagem": "teste",
                "lastname": "Ciclano",
                "local": "pt-br",
                "niver": "6/13/2005 12:00:00 AM",
                "optin": """Null""",
                "personas": """Null"""
            }
        }
    ],
    "links": {
        "self": "xxx"
    },
    "page": 1,
    "pageSize": 2500,
    "requestToken": "xxxx",
    "tokenExpireDateUtc": "2025-05-23T18:26:43.697",
    "top": 0
        }

        teste = chavesJson(jsonSimples)
        if type(teste).__name__ not in ('dict', 'list'):
            self.fail("Retorno Inesperado.")
        
        elif not 'id' in teste or not 'atributos' in teste:
            self.fail("Json Incompleto")


    def test_002_JsonSemiComplexo(self):
        jsonSemiComplexo = {
    "links": {
        "self": "123"
    },
    "requestToken": "xxxx",
    "tokenExpireDateUtc": "2025-05-28T16:59:13.837",
    "customObjectId": "xxxxx",
    "customObjectKey": "xxxxxx",
    "pageSize": 2500,
    "page": 1,
    "count": 2,
    "top": 0,
    "items": [
        {
            "keys": {},
            "values": {
                "subscriberkey": "123xxxx456",
                "emailaddress": "fulano@teste.com",
                "financial_card": "[{\"credit_card_brand\":\"Visa\",\"card_status\":\"Ativo\\r\",\"card_category\":\"Infinity\"}]"
            }
        }
    ]
    }   
        teste = chavesJson(jsonSemiComplexo)
        if type(teste).__name__ not in ('dict', 'list'):
            self.fail("Retorno Inesperado.")
        
        elif not 'id' in teste or not 'atributos' in teste:
            self.fail("Json Incompleto")
        
        elif not 'atributojson' in teste or not 'chaveatributojson' in teste:
            self.fail("Incompleto...")

        elif len(teste["atributojson"]) <= 0 and len(teste["chaveatributojson"]) <= 0:
            self.fail("Atributos/Chaves Faltantes")


    def test_003_JsonComplexo(self):
        jsonComplexo = {
    "links": {
        "self": "123456"
    },
    "requestToken": "xxxxxxx",
    "tokenExpireDateUtc": "2025-05-27T14:16:08.357",
    "customObjectId": "xxxxxxx",
    "customObjectKey": "xxxxxxx",
    "pageSize": 2500,
    "page": 1,
    "count": 1,
    "top": 0,
    "items": [
        {
            "keys": {},
            "values": {
                "subscriberkey": "123Teste456",
                "emailaddress": "fulano@teste.com",
                "transactions": """[{
            "Type": "Pix",
            "Client_Id": "123",
            "Transaction_Date": "2025-05-16T09:21:00.000Z",
            "Products": [
                {
                "Name": "Sonico",
                "Price": 30.90
                },
                {
                "Name": "Ultra Lazer",
                "Price": 41.95
                }
            ],
            "Total_Amount": 89.85
            }
            ]"""
                        }
                    }
                ]
            }
        
        teste = chavesJson(jsonComplexo)
        if type(teste).__name__ not in ('dict', 'list'):
            self.fail("Retorno Inesperado.")
        
        elif not 'id' in teste or not 'atributos' in teste:
            self.fail("Json Incompleto")
        
        elif not 'atributojson' in teste or not 'chaveatributojson' in teste:
            self.fail("Incompleto...")

        elif len(teste["atributojson"]) <= 0 and len(teste["chaveatributojson"]) <= 0:
            self.fail("Atributos/Chaves Faltantes")

        elif not 'atributoJsonInterno' in teste or not 'chavesJsonInterno':
            self.fail("Incompleto")
        
        elif len(teste["atributoJsonInterno"]) <= 0 and len(teste["chavesJsonInterno"]):
            self.fail("Atributos/Chaves incompletas")



    

def runTestes():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)    

if __name__ == '__main__':
    runTestes()
