from typing import Iterable


def rotacionar(iteravel: Iterable, k: int ):
    lista = list(iteravel)
    primera_fatia = lista[-k:]
    segunda_fatia = lista[:-k]
    return primera_fatia + segunda_fatia

lista_numeros = '1234567'

print(rotacionar(lista_numeros, 3))



