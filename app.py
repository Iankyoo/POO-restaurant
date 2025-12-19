import requests 
import json
import unicodedata

def normalizar_nome(nome):
    nome = unicodedata.normalize("NFKD", nome)
    nome = nome.replace("’", "'")
    return nome.strip().lower()

url = "https://gist.githubusercontent.com/Iankyoo/5e2ef19429a0980c98d037a33ba942e9/raw/restaurantes.json"
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = normalizar_nome(item["Company"])
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []
        dados_restaurante[nome_do_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })
else:
    print(f"O erro foi {response.status_code}")

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w', encoding='utf-8') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante, indent=4, ensure_ascii=False)

    


