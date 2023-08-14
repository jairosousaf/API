# import requests

# def consultar_cep(cep):
#     url = f'https://viacep.com.br/ws/{cep}/json/'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         return None
    
# cep = '65060764'

# dados_cep = consultar_cep(cep)
# print(dados_cep)

##########################################

import requests

pokemon_name = 'onix'
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
data = response.json()
print(f'Nome: {data["name"].capitalize()}')
print(f'Altura: {data["height"]/10} metros')
print(f'Peso: {data["weight"]/10} Kg')