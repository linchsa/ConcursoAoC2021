#Day3Part1 : This one was a hard one. My brain is fucked after all this

file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia03/input.txt')
list = file.readlines()
list2 = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
col=[]
gamma=[]
epsilon = []
j=0
i = 0
for i in [0,1,2,3,4,5,6,7,8,9,10,11]: #Q mal queda esto dios mío
    for fila in list:
        col.append(int(fila[i]))
    if(col.count(1) > col.count(0)): 
        gamma.append(1) ## .append añade un elemento a una lista
        epsilon.append(0)
    else: 
        gamma.append(0)
        epsilon.append(1)
    col=[]
    #Siendo sincero es un código de mierda pero funciona. Puto Python lpm
binario = 2**0*gamma[11]+2**1*gamma[10]+2**2*gamma[9]+2**3*gamma[8]+2**4*gamma[7]+2**5*gamma[6]+2**6*gamma[5]+2**7*gamma[4]+2**8*gamma[3]+2**9*gamma[2]+2**10*gamma[1]+2**11*gamma[0]
binario2 = 2**0*epsilon[11]+2**1*epsilon[10]+2**2*epsilon[9]+2**3*epsilon[8]+2**4*epsilon[7]+2**5*epsilon[6]+2**6*epsilon[5]+2**7*epsilon[4]+2**8*epsilon[3]+2**9*epsilon[2]+2**10*epsilon[1]+2**11*epsilon[0]
#Vaya joyita calcular binario y binario2 a mano. Me cago en toda la punta
print(binario*binario2)
