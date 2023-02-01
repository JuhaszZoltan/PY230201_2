file = open(file='diakok.txt', encoding='utf-8-sig', mode='r')

nev = ''
maximum = -1

for sor in file:
    darabok:list[str] = sor.split(' ')
    
    if int(darabok[2]) > maximum:
        maximum = int(darabok[2])
        nev = f'{darabok[0]} {darabok[1]}'

print(f'legmagasabb diák: {nev} ({maximum} cm)')