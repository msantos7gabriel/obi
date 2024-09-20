def soma_linha(x, j):
    # x = Valor Fixo
    # valor para não somar

    somas = []
    soma = 0
    for i in range(0, len(matriz[x])):
        if matriz[x][i] != matriz[x][j]:
            soma += matriz[x][i]
    somas.append(soma)
    somas.sort()
    print(somas[0])



matriz = []
somas = []
dim = int(input())
for i in range(0, dim):
    linhas = list(map(int, input().split()))
    matriz.append(linhas[:])
    linhas.clear()

soma_linha(0)

for i in range(0, len(matriz)):
    for j in range(0, dim):
        print(matriz[0][j])
        soma_linha(i, j)
