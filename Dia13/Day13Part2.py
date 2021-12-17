import numpy as np
import math
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia13/input.txt')
fold = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia13/foldalong.txt')

l=1
distributor=[]
matrix=[]
for i in range(895):
    matrix.append([])
    for j in range(1311):
        matrix[i].append('.')
        
for line in file:
    coor=line.split(',')
    i=int(coor[0])
    j=int(coor[1])
    matrix[j][i]='#'

lenmatrixi=895
lenmatrixj=1311

while(l<=12):
    distributor= fold.readline().split('=')
    if(distributor[0]=='x'):
        x=int(distributor[1])
        print(x)
        cont=0
        for j in range(x,lenmatrixj):
            for i in range(lenmatrixi):
                if(matrix[i][j]=='#'):
                    z=j-x
                    newj=abs(z-x)
                    matrix[i][newj]='#'

        lenmatrixj=lenmatrixj-1-x
        l+=1

    if(distributor[0]=='y'):
        y=int(distributor[1])
        print(y)
        for j in range(y,lenmatrixi):
            for i in range(lenmatrixj):
                if(matrix[j][i]=='#'):
                    z=j-y
                    newi=abs(z-y)
                    matrix[newi][i]='#'

        lenmatrixi=lenmatrixi-1-y
        l+=1
print(lenmatrixi)
print(lenmatrixj)
for j in range(lenmatrixi):
    for i in range(lenmatrixj):
        print(matrix[j][i],end=" ")
    print()