
import copy
file= open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia08/input.txt')
lista=[]
lista2=[]
order=[]
cont=0
sum=0
listaremove=[]
num=[]
inputnum=0
for line in file:
    num=[]
    listaremove=[]
    dictvalues=[]
    inputdict={0:'none',1:'none',2:'none',3:'none',4:'none',5:'none',6:'none',7:'none',8:'none'}
    vector= line.split('|')
    lista=vector[0].split()
    lista2=vector[1].split()
    for i in lista:
        z=''.join(sorted(i))
        if(len(z)==2):
            inputdict[1]=copy.copy(z)
            listaremove.append(i)
        if(len(z)==3):
            inputdict[7]=copy.copy(z)
            listaremove.append(i)
        if(len(z)==4):
            inputdict[4]=copy.copy(z)
            listaremove.append(i)
        if(len(z)==7):
            inputdict[8]=copy.copy(z)
            listaremove.append(i)
    for i in listaremove:
        lista.remove(i)

    for i in lista:
        z=''.join(sorted(i))
        if(len(z)==5):
            cont=0
            for i in inputdict[8]:
                for j in z:
                    if(i==j):
                        cont+=1
            if(cont==5):
                cont=0
                for i in z:
                    for j in inputdict[7]:
                        if(i==j):
                            cont+=1
                if(cont==3):
                    inputdict[3]=copy.copy(z)
                else:
                    cont=0
                    for i in z:
                        for j in inputdict[4]:
                            if(i==j):
                                cont+=1
                    if(cont==3):
                        inputdict[5]=copy.copy(z)
                    else:
                        inputdict[2]= copy.copy(z)
        if(len(z)==6):
            cont=0
            for i in z:
                for j in inputdict[1]:
                    if(i==j):
                        cont+=1
            if(cont==1):
                inputdict[6]=copy.copy(z)
            else:
                cont=0
                for i in z:
                    for j in inputdict[4]:
                        if(i==j):
                            cont+=1
                if(cont==4):
                    inputdict[9]= copy.copy(z)
                else:
                    inputdict[0]= copy.copy(z)
    for i in lista2:
        z=''.join(sorted(i))
        for j in inputdict.values():
            if(z==j):
                for z in inputdict.keys():
                    if(inputdict[z]==j):
                        num.append(z)

    inputnum= num[0]*1000+num[1]*100+num[2]*10+num[3]
    sum+=inputnum
print(sum)