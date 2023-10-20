def adicionar(P1):
    num = str(input("Digite algum caracter ou um numero de 0 a 9: "))
    P1.append(num)

def retirar(p1):
    return p1.pop(0)

def topo(p1):
    return p1[-1]

def tamanho(p1):
    return len(p1)

def limpar(p1):
    p1[:] = []

def organizar(p1, p2, p3):
    p = 0
    pos = 0
    comp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(p1)):
        for n in range(len(comp)):
            if p1[p] == comp[pos]:
                p2.append(p1[p])
                pos = 0
                p += 1
                break
            else:
                pos += 1
                if pos == 10:
                    p3.append(p1[p])
                    
        







        


