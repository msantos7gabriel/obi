n_linhas = int(input())
linhas = []

for i in range(0, n_linhas):
    n1, n2, n3 = map(int, input().split())
    linhas.append([n1, n2, n3])
print(linhas)
