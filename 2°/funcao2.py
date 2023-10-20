import os
def adicionar(aluno):
    nome = str(input("Digite o nome do aluno: "))
    matricula = int(input("Digite sua matricula: "))
    nota1 = float(input("Digite sua nota"))
    nota2 = float(input("Digite sua nota"))
    faltas = int(input("Digite suas faltas em horas"))
    aluno.append(nome, matricula, nota1, nota2, faltas)
    return aluno

def status(aluno):
    if len(aluno) == 0:
        print("Não possui dados")
        os.system("pause")
        os.system("cls")
        return 
    
        
    if (aluno[2] + aluno[3]) / 2 < 7 and (aluno[2] + aluno[3]) / 2 >= 5:
        print("Recuperação")
        os.system("pause")
        os.system("cls")
    elif (aluno[2] + aluno[3]) / 2 < 5:
        print("REPROVADO!")
        os.system("pause")
        os.system("cls")
    
    if (aluno[2] + aluno[3]) / 2 >= 7 and aluno[4] >= 30:
        print("Aprovado!")
        os.system("pause")
        os.system("cls")
        
    return
    

