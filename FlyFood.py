import matplotlib.pyplot as plt
def gerarArranjos(lista, tam_lista=None):
    Tlocais = tuple(lista)
    n = tam_lista
    indices = list(range(n))
    ciclos = list(range(n, 0, -1))
    yield tuple(Tlocais[i] for i in indices[:tam_lista])
    print(tuple(Tlocais[i] for i in indices[:tam_lista]))
    while n:
        for i in reversed(range(tam_lista)):
            ciclos[i] -= 1
            if ciclos[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1] #troca o item indices[i] com seu sucessor
                ciclos[i] = n - i
            else:
                j = ciclos[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(Tlocais[i] for i in indices[:tam_lista])
                print(tuple(Tlocais[i] for i in indices[:tam_lista]))
                break
        else:
            return



def menorCaminho(lista_arranjos,lista_coordenadas, lista_vazia):
    menor_caminho = 0
    i = 0
    j = 0
    distancia = 0
    for c in range(len(lista_arranjos)):
        for d in range(len(lista_arranjos[c])-1):
            while (lista_coordenadas[i][0] != lista_arranjos[c][d]):
                i += 1
            while (lista_coordenadas[j][0] != lista_arranjos[c][d+1]):
                j += 1
            a, b = lista_coordenadas[i][1], lista_coordenadas[j][1]
            x, y = lista_coordenadas[i][2], lista_coordenadas[j][2]
            distancia += (abs(a-b) + abs(x-y))
            i = j = 0
        if(menor_caminho == 0):
            lista_vazia = lista_arranjos[c]
            menor_caminho = distancia
        elif(distancia < menor_caminho):
            menor_caminho = distancia
            lista_vazia = lista_arranjos[c]
        distancia = 0
    return lista_vazia



lista_nova = []
L, C = [int(x) for x in input().split()]
matriz = list(range(L))

for i in range(L):
    linha = [str(x) for x in input().split()]
    matriz[i] = linha

#procurar pelos pontos e guardar suas localizações:

locais = []
posicoes = []

for i in range(L):
    for j in range(C):
        if matriz[i][j] != '0':
            coordenadas = []
            coordenadas.append(matriz[i][j])
            coordenadas.append(i)
            coordenadas.append(j)
            posicoes.append(coordenadas)
            if matriz[i][j] != 'R':
                locais.append(matriz[i][j])
            else:
                ponto_inicial = matriz[i][j]

arranjo = list(gerarArranjos(locais, len(locais)))
print(arranjo)
lista_arranjos = []
#transformar tupla em lista
for item in arranjo:
    lista_arranjos.append(list(item))
#inserir ponto de inicio e fim "R"
for item in lista_arranjos:
    item.append(ponto_inicial)
    item.insert(0, ponto_inicial)

melhor_rota = menorCaminho(lista_arranjos, posicoes, lista_nova)
print(melhor_rota)
