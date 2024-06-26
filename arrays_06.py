"""Ler o nome e a idade de 5 pessoas e mostrar o nome do mais velho"""
import numpy as np

MAX_ITEMS = 5

nomes = np.empty(MAX_ITEMS,dtype = "U20")
idades = np.empty(MAX_ITEMS,dtype ="f")

for i in range(len(idades)):
    nomes[i] = input("Insira o nome:")
    idades[i] = int(input("Insira a sua idade:"))

posicao = 0
maior = idades[posicao]

for i in range(1,MAX_ITEMS):
    if idades[i] > maior:
        maior = idades[i]
        posicao = i

print(f"O mais velho é {nomes[posicao]} e tem a idade de {idades[posicao]}")
