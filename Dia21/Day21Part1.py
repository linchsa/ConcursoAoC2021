import copy

startp1 = 6
startp2 = 1
scorep1=0
scorep2=0
spacep1=0
spacep2=0
scorecont=0
cont=0
times=0
while(scorep1<1000 or scorep2<1000):
    scorecont=(cont+1)%10+(cont+2)%10+(cont+3)%10
    if((startp1+scorecont)%10!=0):
        spacep1=(startp1+scorecont)%10
    else:
        spacep1=10
    scorep1+=spacep1
    if(scorep1>=1000):
        cont+=3
        break
    cont+=3
    startp1=copy.copy(spacep1)


    if(cont+3==99): #Arreglo chapuza
        scorecont=20
    else:
        scorecont=(cont+1)%10+(cont+2)%10+(cont+3)%10
    if((startp2+scorecont)%10!=0):
        spacep2=(startp2+scorecont)%10
    else:
        spacep2=10
    scorep2+=spacep2
    cont+=3
    startp2=copy.copy(spacep2)
print(scorep2)
print(scorep1)
print(cont)

if(scorep1<scorep2):
    print(cont*scorep1)
else:
    print(cont*scorep2)