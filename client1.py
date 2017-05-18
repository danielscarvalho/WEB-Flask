#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json

#Exemplo de programa em Python 3 consumindo um serviço (WEB SERVICE)

#pega valor do usuário a ser calculado fatorial
fat = input("Faborial de: ")

#Monta string com a URL, passando o valor como parâmetro
url = 'http://danielscarvalho.pythonanywhere.com/fatorial/' + str(fat)

#Abre a URL (Request) e recebe o Response
res = urllib.request.urlopen(url)

#Pega apenas os dados (JSON em string) do Response recebido
#E converte texto em JSON para estrutura de dados dicionário do Python
data_dict = json.loads(res.read().decode('utf8'))

#Exibe apenas o valor do fatorial que está no dicionário
print(data_dict["fatorial"])

#Qual é a diferença entre JSON e um dicionário do Python??
#Estudar sobre protocolo HTTP
