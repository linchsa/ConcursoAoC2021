file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia02/input.txt')
list = file.readlines()
h=0
f=0
for i in list:
    final = i.split(' ')
    if(final[0]=='up'): h-=int(final[1])
    elif(final[0]=='down'): h+=int(final[1])
    else: f+=int(final[1])
print(h*f)