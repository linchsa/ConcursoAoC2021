#NO ESTÁ TERMINADO
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia10/input2.txt')

check= True
open = ['[','<','(','{']
close = [']','>',')','}']
contopen=0
contclose=0
stackopen=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8]
stackclose=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
while(check==True):
    list = file.readline()
    print(list)
    for i in list:
        if(i=='[' or i=='{' or i=='(' or i=='<'):
            stackopen[contopen]=i
            contopen+=1
        else:
            stackclose[contclose]=i
            contclose+=1
        

    check= False
print(stackopen)
print(stackclose)