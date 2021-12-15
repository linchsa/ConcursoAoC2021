import copy
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia14/input.txt')
startlist = file.readline().split()
database=[]
newlist=copy.copy(startlist)
str=[]
l=1
p=-1
print(startlist)
num=1
database=['ON', 'C', 'CK', 'H', 'HC', 'B', 'NP', 'S', 'NH', 'H', 'CB', 'C', 'BB', 'H', 'BC', 'H', 'NN', 'C', 'OH', 'B', 'SF', 'V', 'PB', 'H', 'CP', 'P', 'BN', 'O', 'NB', 'B', 'KB', 'P', 'PV', 'F', 'SH', 'V', 'KP', 'S', 'OF', 'K', 'BS', 'V', 'PF', 'O', 'BK', 'S', 'FB', 'B', 'SV', 'B', 'BH', 'V', 'VK', 'N', 'CS', 'V', 'FV', 'F', 'HS', 'C', 'KK', 'O', 'SP', 'N', 'FK', 'B', 'CF', 'C', 'HP', 'F', 'BF', 'O', 'KC', 'C', 'VP', 'O', 'BP', 'P', 'FF', 'V', 'NO', 'C', 'HK', 'C', 'HV', 'B', 'PK', 'P', 'OV', 'F', 'VN', 'H', 'PC', 'K', 'SB', 'H', 'VO', 'V', 'BV', 'K', 'NC', 'H', 'OB', 'S', 'SN', 'B', 'HF', 'P', 'VF', 'B', 'HN', 'H', 'KS', 'S', 'SC', 'S', 'CV', 'B', 'NS', 'P', 'KO', 'V', 'FS', 'O', 'PH', 'K', 'BO', 'C', 'FH', 'B', 'CO', 'O', 'FO', 'F', 'VV', 'N', 'CH', 'V', 'NK', 'N', 'PO', 'K', 'OK', 'K', 'PP', 'O', 'OC', 'P', 'FC', 'N', 'VH', 'S', 'PN', 'C', 'VB', 'C', 'VS', 'P', 'HO', 'F', 'OP', 'S', 'HB', 'N', 'CC', 'K', 'KN', 'S', 'SK', 'C', 'OS', 'N', 'KH', 'B', 'FP', 'S', 'NF', 'S', 'CN', 'S', 'KF', 'C', 'SS', 'C', 'SO', 'S', 'NV', 'O', 'FN', 'B', 'PS', 'S', 'HH', 'C', 'VC', 'S', 'OO', 'C', 'KV', 'P']


while(l<=10):
    p=-1
    startlist= copy.copy(newlist)
    for i in range(len(startlist)-1):
        str=startlist[i]+startlist[i+1]
        for j in database:
            if(j==str):
                p+=2
                newlist.insert(p,database[database.index(str)+1])
    l+=1
print(newlist.count('B'))
print(newlist.count('C'))
print(newlist.count('H'))
print(newlist.count('N'))
print(newlist.count('F'))
print(newlist.count('K'))
print(newlist.count('O'))
print(newlist.count('P'))
print(newlist.count('V'))
print(newlist.count('S'))




