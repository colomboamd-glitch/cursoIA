#Primeiro Instalar bibliotecas
#pip install request
#Segundo add/importar codigo

import requests
cep = input("Digite seu cep: ")
nome = input ("digite seu nome: ")
email = input ("digite se email: ")
telefone = input (" digite seu telefone: ")

url = f"https://viacep.com.br/ws/{cep}/json/"   #utilizamos f string para atribuir link

dados = requests.get(url).json()

dados = (f"bem vindo ao mercado livre {nome}! o seu email é {email}, seu telefone {telefone}. Voce mora na rua {dados['logradouro']}, no bairro {dados['bairro']}, na cidade {dados['localidade']} ")

rua = dados['logradouro']
bairro = dados['bairro']
cidade = dados['localidade']
#print(rua)
#print(bairro)     #atribuindo variaveis para cada um dos resultados
#print(cidade)
#print (f"seu endereço é: {rua}, {bairro}, {cidade}")

