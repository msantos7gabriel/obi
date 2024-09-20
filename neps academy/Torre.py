# O Seguinte codigo está funcional porem passa do limite de tempo de execução predefinido pelo neps academy

def soma_linha(x, j):
    # x = Valor Fixo
    # k = valor para não somar
    soma = 0
    for i in range(0, len(matriz[x])):
        if i != j:
            soma += matriz[x][i]
    return soma


def soma_coluna(x, j):
    # x = Valor Fixo
    # k = valor para não somar
    soma = 0
    for i in range(0, len(matriz[x])):
        if i != j:
            soma += matriz[i][x]
    return soma


matriz = []
somas = []
dim = int(input())
for i in range(0, dim):
    linhas = list(map(int, input().split()))
    matriz.append(linhas[:])
    linhas.clear()

for i in range(0, len(matriz)):
    for j in range(0, dim):
        somas.append(soma_coluna(j, i)+soma_linha(i, j))
somas.sort(reverse=True)
print(somas[0])
