n = input()
lista = list(map(int, input().split()))
print(lista)

e = len(lista)
d = 1

while True:
    if lista[d] > lista[d-1]:
        while True:
            if lista[d]<