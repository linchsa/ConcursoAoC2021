import copy
file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2021/Dia14/input2.txt')
startlist = file.readline().split()
database=[]
store=[]
newlist=copy.copy(startlist)
str=[]
l=1
p=-1
count={'B':0, 'C':0,'H':0,'N':0,'F':0,'K':0,'O':0,'P':0,'V':0,'S':0}

print(startlist)
num=1
#database2=['ON', 'C', 'CK', 'H', 'HC', 'B', 'NP', 'S', 'NH', 'H', 'CB', 'C', 'BB', 'H', 'BC', 'H', 'NN', 'C', 'OH', 'B', 'SF', 'V', 'PB', 'H', 'CP', 'P', 'BN', 'O', 'NB', 'B', 'KB', 'P', 'PV', 'F', 'SH', 'V', 'KP', 'S', 'OF', 'K', 'BS', 'V', 'PF', 'O', 'BK', 'S', 'FB', 'B', 'SV', 'B', 'BH', 'V', 'VK', 'N', 'CS', 'V', 'FV', 'F', 'HS', 'C', 'KK', 'O', 'SP', 'N', 'FK', 'B', 'CF', 'C', 'HP', 'F', 'BF', 'O', 'KC', 'C', 'VP', 'O', 'BP', 'P', 'FF', 'V', 'NO', 'C', 'HK', 'C', 'HV', 'B', 'PK', 'P', 'OV', 'F', 'VN', 'H', 'PC', 'K', 'SB', 'H', 'VO', 'V', 'BV', 'K', 'NC', 'H', 'OB', 'S', 'SN', 'B', 'HF', 'P', 'VF', 'B', 'HN', 'H', 'KS', 'S', 'SC', 'S', 'CV', 'B', 'NS', 'P', 'KO', 'V', 'FS', 'O', 'PH', 'K', 'BO', 'C', 'FH', 'B', 'CO', 'O', 'FO', 'F', 'VV', 'N', 'CH', 'V', 'NK', 'N', 'PO', 'K', 'OK', 'K', 'PP', 'O', 'OC', 'P', 'FC', 'N', 'VH', 'S', 'PN', 'C', 'VB', 'C', 'VS', 'P', 'HO', 'F', 'OP', 'S', 'HB', 'N', 'CC', 'K', 'KN', 'S', 'SK', 'C', 'OS', 'N', 'KH', 'B', 'FP', 'S', 'NF', 'S', 'CN', 'S', 'KF', 'C', 'SS', 'C', 'SO', 'S', 'NV', 'O', 'FN', 'B', 'PS', 'S', 'HH', 'C', 'VC', 'S', 'OO', 'C', 'KV', 'P']
database=['CH', 'B', 'HH', 'N', 'CB', 'H', 'NH', 'C', 'HB', 'C', 'HC', 'B', 'HN', 'C', 'NN', 'C', 'BH', 'H', 'NC', 'B', 'NB','B', 'BN', 'B', 'BB', 'N', 'BC', 'B', 'CC', 'N', 'CN', 'C']
adjacents={}
for i in range(0,len(database)-1,2):
    adjacents[database[i]]=0
for i in range(0,len(startlist)-1):
    count[startlist[i]]=1
#print(count)
#print(adjacents)
'''for i in file:
    new=i.split()
    database.extend(new)'''
#print(database)

while(l<=40):
    l=41