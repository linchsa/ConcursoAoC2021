#import numpy as np
import math
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia13/input.txt')
y=7
x=655
cont=0
matrix=[]
for i in range(1501):
    matrix.append([])
    for j in range(1501):
        matrix[i].append('.')
for line in file:
    coor=line.split(',')
    i=int(coor[1])
    j=int(coor[0])
    matrix[i][j]='#'



for i in range(len(matrix)):
    for j in range(x,len(matrix[i])):
        if(matrix[i][j]=='#'):
            z=j-x
            newj=abs(z-x)
            matrix[i][newj]='#'

for i in range(len(matrix)):
    for j in range(x):
        if(matrix[i][j]=='#'):
            cont+=1
print(cont)


        

