file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia02/input2.txt')
list = file.readlines()
h=0 #depth
f=0 #forward
for i in list:
    final = i.split(' ') #.split separates the elements of a list so as it creates a new list for each line ['word',number]
    if(final[0]=='up'): h-=int(final[1])
    elif(final[0]=='down'): h+=int(final[1])
    else: f+=int(final[1])
print(h*f)