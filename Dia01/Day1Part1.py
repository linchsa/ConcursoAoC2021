file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia01/input.txt')
list = file.readlines()
cont=1
i=0
for i in range(1,len(list)-1):
    if(list[i+1]>list[i]): 
        cont=cont+1
print(int(cont))