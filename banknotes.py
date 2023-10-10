valor = int(input())
total = valor
ced100 = 100
ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced2 = 2
ced1 = 1

totced = 0
print(f'{total}')
while True:
    if total >= ced100:
        total -= round(ced100, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced100},00')
        totced = 0
        break

while True:
    if total >= ced50:
        total -= round(ced50, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced50},00')
        totced = 0
        break

while True:
    if total >= ced20:
        total -= round(ced20, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced20},00')
        totced = 0
        break

while True:
    if total >= ced10:
        total -= round(ced10, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced10},00')
        totced = 0
        break

while True:
    if total >= ced5:
        total -= round(ced5, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced5},00')
        totced = 0
        break

while True:
    if total >= ced2:
        total -= round(ced2, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced2},00')
        totced = 0
        break

while True:
    if total >= ced1:
        total -= round(ced1, 2)
        totced += 1
    else:
        print(f'{totced} nota(s) de R$ {ced1},00')
        totced = 0
        break