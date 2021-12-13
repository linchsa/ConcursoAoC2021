file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia04/input2.txt')
numsecuence = file.readline()
p=1
f=p+4
cont=0
contwinner=0
print(numsecuence[0])
while(f<19):
    matrix = file.readlines()[p:f]
    # for i in numsecuence:

