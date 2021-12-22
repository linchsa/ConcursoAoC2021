

file= open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia08/input.txt')
lista=[]
lista2=[]
order=[]
cont=0
for line in file:
    vector= line.split('|')
    lista=vector[0].split()
    lista2=vector[1].split()
    for i in lista2:
        z=''.join(sorted(i))
        if(len(z)==2 or len(z)==4 or len(z)==3 or len(z)==7):
            cont+=1
print(cont)