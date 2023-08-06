import requests, json

cotization = requests.get("https://api.bluelytics.com.ar/v2/latest").json()
oficial = cotization["oficial"]["value_buy"]
blue = cotization["blue"]["value_buy"]
euro = cotization["oficial_euro"]["value_buy"]
euro_blue = cotization["blue_euro"]["value_buy"]

class CDolarOficial:
    def __init__(self):
        pass

    def aPesos(cantUsd = 1):
        # Transforma dolares a pesos. Parametros: cantUsd (Cantidad de dolares)
        cant = oficial * cantUsd
        x = {
            "usd": cantUsd,
            "dolarPrice": oficial,
            "total": cant
        }
        x = json.dumps(x)
        y = json.loads(x)
        return y


def calcularImpuestoPais(cantidad = 1):
    # Calcula el impuesto pais segun cuanto pongas. Parametros: cantidad (Cantidad de dinero)
    total = cantidad * (175 / 100)
    agregado = total - cantidad
    x = {
        "cantidadVieja": cantidad,
        "agregado": agregado,
        "cantidadFinal": total 
    }
    x = json.dumps(x)
    y = json.loads(x)
    return y


dolarOficial = CDolarOficial