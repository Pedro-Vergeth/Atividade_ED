from funcao2 import adicionar, status
import os
opc = 0
aluno = []

while opc != 3:
    print("""
    1 - adicionar dados aluno
    2 - Verificar status de notas
    3 - Sair
    Digite sua opção:
    """)
    opc = int(input(""))

    if opc == 1:
        adicionar(aluno)
        print("Aluno adicionado")
        os.system("pause")
        os.system("cls")
    elif opc == 2:
        status(aluno)
    elif opc == 3:
        break    



