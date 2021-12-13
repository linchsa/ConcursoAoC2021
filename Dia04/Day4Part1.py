import numpy as np
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia04/input2.txt')
numsecuence = file.readline()
p=1
f=p+4
cont=0
contwinner=0
print(numsecuence[0])




while(f<19):
    f=p+4
    matrix = file.readlines()[p:f]
    for i in numsecuence:
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if(matrix[j][k]==i):
                    matrix[i][j]=-1
                cont+=1
        for j in range(len(matrix)):
            if(np.all(matrix==-1)):
                break
        for j in range(len(matrix)):
            None

