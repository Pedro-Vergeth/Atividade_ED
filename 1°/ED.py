from funcao import adicionar, retirar, tamanhofila
import os
opc = 0
fila = []

while opc != 4:
    if len(fila) == 0:
        print("Não tem ninguem na fila")
    else:
        print(fila[0])
    print(fila)
    print("""
    1 - Adicionar a fila
    2 - Retirar da fila
    3 - Tamanho da fila
    4 - Encerrar
    Digite sua opção:
    """)
    opc = int(input(""))

    if opc == 1:
        adicionar(fila)
        print("Adicionado")
        os.system("cls")
    elif opc == 2:
        retirar(fila)
        print("Retirado com sucesso")
        os.system("cls")
    elif opc == 3:
        tamanho = tamanhofila(fila)
        print(tamanho)
        os.system("pause")
        os.system("cls")
    elif opc == 4:
        print(len(fila)," Pessoas não atendidas")
        break

    







