import os
def adicionar(fila):
    os.system("cls")
    nome = str(input("Digite seu nome:"))
    fila.append(nome)
    return fila

def retirar(fila):
    os.system("cls")
    fila.pop(0)
    return fila

def tamanhofila(fila):
    os.system("cls")
    tamanho = len(fila)
    return tamanho




