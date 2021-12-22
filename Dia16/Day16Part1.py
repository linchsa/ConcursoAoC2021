

file= open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia16/input2.txt')
hex=[]
scale= 16
list= file.readline()
list = bin(int(list, scale)).zfill(8)
print(list)

for i in list:
    hex.append(i)
print(hex)

for i in range(2,len(hex)):
    None