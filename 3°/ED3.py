from funcao3 import adicionar, retirar, topo, tamanho, limpar, organizar
import os
opc = 0

P1 = []
P2 = []
P3 = []

while opc != 7 :
    
    print("""
        1 - Adicionar
        2 - Retirar
        3 - Topo
        4 - Tamanho
        5 - Limpar pilha
        6 - Organizar
        7 - Sair
          """)
    opc = int(input("Digite sua opção: "))
    if opc == 1:
        adicionar(P1)
        
    elif opc == 2:
        retirar(P1)
    
    elif opc == 3:
        print(topo(P1))
        os.system("pause")

    elif opc == 4:
        print(tamanho(P1))
        os.system("pause")
    
    elif opc == 5:
        limpar(P1)

    elif opc == 6:
        organizar(P1, P2, P3)
        print("P1: ", P1, "P2: ", P2,"P3: ", P3)
        os.system("pause")
        


    
