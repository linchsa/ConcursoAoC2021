#NO ESTÁ TERMINADO
import numpy as np

with open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia09/input2.txt','r') as f:
    datos = ''.join(f.readlines()).replace('\n',';')

matrix = np.matrix(datos)
print(matrix)
'''for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if(i==0 and j==0):
            if(matrix[i][j]<)
        
        
        
        
        
        
        if(matrix[i][j]<matrix[i+1][j] and matrix[i][j]<matrix[i][j+1] and matrix[i][j]<matrix[i-1][j] and matrix[i][j]<matrix[i][j-1]):
'''

