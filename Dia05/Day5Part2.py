import numpy as np
import copy
from numpy import *
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia05/input.txt')

matrix = np.zeros((1000, 1000))
cont=0
cont2=0
list=[]
f=1
while(f<=500):
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
    elif(int(list[1])==int(list[3])):

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
    else:
        c=0
        if((int(list[0])-int(list[2]))+(int(list[1])-int(list[3]))==0):
            if(int(list[0])>int(list[2])):
                    i=int(list[0])
                    j=int(list[1])
                    #while(c!=abs(int(list[0])-int(list[2])+1)):
                    while(j<=int(list[3])):
                        matrix[j,i]+=1
                        i-=1
                        j+=1
                        c+=1
            else:
                    i=int(list[2])
                    j=int(list[3])
                    while(j<=int(list[1])):
                        matrix[j,i]+=1
                        i-=1
                        j+=1
                        c+=1
        else:
        #elif((int(list[0])-int(list[2]))+(int(list[1])-int(list[3]))==2*abs(int(list[0])-int(list[2]))):
            c=0
            if(int(list[0])<int(list[2])):
                    i=int(list[0])
                    j=int(list[1])
                    while(j<=int(list[3])):
                        matrix[j,i]+=1
                        i+=1
                        j+=1
                        c+=1
            else:
                    i=int(list[2])
                    j=int(list[3])
                    while(j<=int(list[1])):
                        matrix[j,i]+=1
                        i+=1
                        j+=1
                        c+=1
            
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