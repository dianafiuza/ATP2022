
import csv
import matplotlib.pyplot as plt


def leAlunos (filename):
    file = open (filename, encoding = "UTF8")
    file.readline()
    csv_file = csv.reader (file,delimiter = ",")

    lista = []
    for aluno in csv_file:
        lista.append(tuple(aluno))
      
    return lista

alunos = leAlunos("alunos.csv")

            
def distCurso(alunos):
    dici = {}
    for _, _, curso, *_ in alunos:
        if curso in dici.keys():  
            dici[curso] =  dici[curso] + 1
        else:
            dici[curso] = 1
    return dici



def media_aluno(alunos):
    lista2 = []
    for id, nome, curso, tpc1, tpc2, tpc3, tpc4 in alunos:
        soma = int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4)
        media = soma/4
        tuplo = (id, nome, curso, tpc1, tpc2, tpc3, tpc4, media)
        lista2.append(tuplo)
    return lista2

alunos2 = media_aluno(alunos)

def escaloes_notas(alunos2):
    escalao = ()
    lista3 = []
    for id, nome, curso, tpc1, tpc2, tpc3, tpc4, media in alunos2:
        if 1 <=media <=4:
            escalao = ("E")
        if 5 <=media <=8:
            escalao = ("D")
        if 9 <=media <=12:
            escalao = ("C")
        if 13 <=media <=16:
            escalao = ("B")
        if 17 <=media <=20:
            escalao = ("A")
        tuplo = (id, nome, curso, tpc1, tpc2, tpc3, tpc4, media, escalao)
        lista3.append(tuplo)

    return lista3
        
alunos3 = escaloes_notas(alunos2)   


def distEscalao(alunos3):

    dici = {}
    for _, _, _, _, _, _, _, _, escalao in alunos3:
        if escalao in dici.keys():  
            dici[escalao] =  dici[escalao] + 1
        else:
            dici[escalao] = 1
    x = dici.keys()
    y = dici.values()

    plt.bar(x, y)
    plt.xlabel('escalão')
    plt.ylabel('número de alunos')
    plt.title('Distribuições')
    plt.show()
    
   
def distTabela (alunos3):
    dici = {}
    for _, _, curso,*_ in alunos3:
        if curso in dici:
            dici[curso] += 1
        else:
            dici[curso] = 1

    for curso in  dici:
        print(f"{curso:30} ==> {dici[curso]}")
    
def menu ():
    print("""
    --------------------------------------------------------------------------------------------------------------
    (1) Calcula a distribuição dos alunos por curso
    (2) Calcula a média das notas de cada aluno e acrescenta essa nova coluna no dataset em memória
    (3) Calcula a distribuição dos alunos por escalão
    (4) Gráfico de linha a distribuição dos alunos por escalão
    (0) Sair
    --------------------------------------------------------------------------------------------------------------
    """)

    opcao = int(input("O que desejas?"))
    leAlunos("alunos.csv")
    while opcao!= 0:
        opcao = int(input("O que desejas?"))
        if opcao == 1:
            print(distCurso(alunos))
        if opcao == 2:
            print(media_aluno(alunos))
        if opcao == 3:
            distEscalao(alunos3)
        if opcao == 4:
            distTabela(alunos3)
       
    if opcao == 0:
        print("Até à próxima, campeão!")
    

menu()
