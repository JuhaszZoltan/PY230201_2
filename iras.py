from math import pi

file = open(file="pelda.txt", mode='w', encoding='UTF-8-sig')

nevek:list[str] = []
for x in range(3):
    nev:str = input('írj be egy nevet: ')
    nevek.append(nev +'\n')

file.writelines(nevek)

file.write(f'pi = {pi}')
