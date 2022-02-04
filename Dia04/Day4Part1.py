import numpy as np
import copy

file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia04/input2.txt')
numsecuence = file.readline().split(',')
print(numsecuence)
p=1
f=p+4
iwin=0
cont=0
minfilas=0
sumfilas=0
sumcol=0
sumcolwinner=0
lastnumbefwin=0
sumfilaswinner=0
minfilaswinner=1000
mincolwinner=1000
mincolumnas=0
contwinner=0


while(f<19):
    f=p+6
    matrix = file.readlines()[p:f]
    print(matrix)
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            sumfilas+=int(matrix[j][k])
            for i in numsecuence:
                if(matrix[j][k]==i):
                    cont+=1
                if(cont==5):
                    minfilas= numsecuence.index(i)
                    if(minfilas<minfilaswinner):
                        minfilaswinner = copy.copy(minfilas)
                        sumfilaswinner = copy.copy(sumfilas)
                        lastnumbefwin=i
            cont=0 
            sumfilas=0 
    cont=0
    for k in range(len(matrix[0])):
        for j in range(len(matrix)):
            sumcol+=matrix[j][k]
            for i in numsecuence:
                if(matrix[j][k]==i):
                    cont+=1
                if(cont==5):
                    mincolumnas= numsecuence.index(i)
                    if(mincolumnas<mincolwinner):
                        minfilaswinner = copy.copy(mincolumnas)
                        sumcolwinner = copy.copy(sumcol)
                        lastnumbefwin = i
            cont=0
            sumfilas=0

    f+=1
    p+=6

if(mincolwinner<minfilaswinner):
    print(mincolwinner*lastnumbefwin)
else:
    print(minfilaswinner*lastnumbefwin)