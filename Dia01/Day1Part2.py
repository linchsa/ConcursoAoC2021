file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia01/input.txt')
list = file.readlines()
cont=0
i=0
for i in range(0,len(list)-3):
    a=int(list[i])+int(list[i+1])+int(list[i+2])
    b=int(list[i+1])+int(list[i+2])+int(list[i+3])
    if(a<b):
        cont=cont+1
print(int(cont))