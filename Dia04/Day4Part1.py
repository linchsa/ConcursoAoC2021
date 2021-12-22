import numpy as np
def checkFilas (matrix):
    i=0
    cont=0
    for i in len(matrix):
        for j in len(matrix[0]):
            if(matrix[i][j]==-1):
                cont+=1
        if(cont==5):
            return True
        else:
            cont=0
    return False
        





file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia04/input2.txt')
numsecuence = file.readline()
p=1
f=p+4
iwin=0
cont=0
contwinner=0
print(numsecuence[0])
def checkFilas (matrix):
    for i in len(matrix):
        print(i)



while(f<19):
    f=p+4
    matrix = file.readlines()[p:f]
    for i in numsecuence:
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if(matrix[j][k]==i):
                    matrix[j][k]='-1'