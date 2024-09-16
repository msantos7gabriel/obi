from string import ascii_lowercase

letras = [ascii_lowercase]
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input()).lower()


def encontrar_vogal(indice):
    f = t = indice
    while True:
        if letras[0][t] not in vogais:
            t -= 1
        else:
            break
        if letras[0][f] not in vogais:
            f += 1
        else:
            break
    if f - indice == indice - t:
        return t
    elif f - indice < indice - t:
        return f
    else:
        return t


def encontrar_consoante(indice):
    f = indice
    while True:
        if indice == 26:
            break
        elif letras[0][f] in vogais or letras[0][f] == letras[0][indice]:
            f += 1
        else:
            break
    return f


for i in range(0, len(palavra)):
    j = 0
    if palavra[i] not in vogais:
        while palavra[i] != letras[0][j]:
            j += 1
        print(f'{letras[0][j]}{letras[0][encontrar_vogal(j)]}{
              letras[0][encontrar_consoante(j)]}', end='')
    else:
        print(f'{palavra[i]}', end='')
