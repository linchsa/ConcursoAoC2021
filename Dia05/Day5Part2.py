import numpy as np
from numpy import *
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia05/input2.txt')

matrix = np.zeros((10, 10))
cont=0
cont2=0
list=[]
f=1
while(f<=10):
    list=file.readline().split(',')
    print(list)
    #print(f)
    #print(list)
    if(int(list[0])==int(list[2])):
        
        if(int(list[1])<int(list[3])):
            i=int(list[0])
            j=int(list[1])
            while(j<=int(list[3])):
                matrix[j,i]+=1
                j+=1
        else:
            i=int(list[0])
            j=int(list[3])
            while(j<=int(list[1])):
                matrix[j,i]+=1
                j+=1
    if(int(list[1])==int(list[3])):

        if(int(list[0])<int(list[2])):
            i=int(list[0])
            j=int(list[1])
            while(i<=int(list[2])):
                matrix[j,i]+=1
                i+=1
        else:
            i=int(list[2])
            j=int(list[1])
            while(i<=int(list[0])):
                matrix[j,i]+=1
                i+=1
    if(int(list[0])==int(list[1]) and int(list[2])==int(list[3])):
        if(int(list[1])<int(list[3])):
            i=int(list[0])
            j=int(list[3])
            while(i<=int(list[3])):
                matrix[i,i]+=1
                i+=1
        else:
            i=int(list[2])
            j=int(list[3])
            while(i<=int(list[1])):
                matrix[i,i]+=1
                i+=1
    if(int(list[0])==int(list[3]) and int(list[2])==int(list[1])):
        if(int(list[2])<int(list[0])):
            i=int(list[0])
            j=int(list[1])
            while(i<=int(list[0])):
                matrix[j,i]+=1
                j-=1
                i+=1
        else:
            i=int(list[1])
            j=int(list[0])
            while(j<=int(list[1])):
                matrix[j,i]+=1
                i-=1
                j+=1
    f+=1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        '''print(matrix[i][j])'''
        #print(cont2)
        if(matrix[i][j]>1):
            cont+=1
        cont2=cont2+1
print(cont)
print(matrix)