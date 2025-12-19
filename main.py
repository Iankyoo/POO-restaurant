from fastapi import FastAPI, Query
import requests


app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe hello world!
    '''
    return {'hello':'world'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver o cardápio dos restaurantes!
    '''
    url = "https://gist.githubusercontent.com/Iankyoo/5e2ef19429a0980c98d037a33ba942e9/raw/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item   ": item["Item"],
                    "price": item["price"],
                    "description": item["description"]
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro': f'{response.status_code} - {response.text}'}    