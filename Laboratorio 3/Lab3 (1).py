import networkx as nx
from matplotlib import pyplot as plt
import math
import sys
import random
import os

def Dist(Nodo1, Nodo2):
    return math.sqrt(math.pow((Nodo1[0] - Nodo2[0]), 2) + math.pow((Nodo1[0] - Nodo2[1]),2))

def getFit(G, arr):
    res = []
    finalRes = 0
    for i in range(0, len(arr)-1):
        res.append(Dist(nx.get_node_attributes(G, 'pos')[arr[i]], nx.get_node_attributes(G, 'pos')[arr[i + 1]]))
        #print(Dist(nx.get_node_attributes(G, 'pos')[arr[i]], nx.get_node_attributes(G, 'pos')[arr[i + 1]]))
    for j in res:
        finalRes = finalRes + j
    return (math.floor(finalRes))  

def initNodos(graph, nroNodos):
    x = []
    y = []
    for i in random.sample(range(0,100),nroNodos):
        x.append(i)
    for j in random.sample(range(0,100),nroNodos):
        y.append(j)

    for i in range(nroNodos):
        graph.add_node(i, pos = (x[i],y[i]))

    print (nx.get_node_attributes(graph, 'pos'))

def dibujar(G):
    fig, ax = plt.subplots()
    plt.title('Nodos Generados')

    ax.set_xlim([0,100])
    ax.set_ylim([0,100])
    nx.draw(G, nx.get_node_attributes(G,'pos'), with_labels=True, ax=ax)
    ax.set_axis_on()
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    plt.grid(b=True)
    plt.show()

def genPoblacion(NodoInicio, Tam, NroNodos, G):
    aux = []
    firstDict = {}
    poblacion = {}
    for i in range(Tam):
        for j in random.sample(range(0,NroNodos), NroNodos):
            aux.append(j)
        aux.remove(NodoInicio) 
        ##random.shuffle(aux)
        aux.insert(0,NodoInicio)
        aux.append(NodoInicio)

        # Obtener fit
        Fit = getFit(G, aux)

        firstDict = {"Camino": aux, "Fit": Fit}
        poblacion[i] = firstDict

        #poblacion.append(aux)
        aux = []
    return poblacion 

def alg_gen_posicion(G,poblacion,tam,NroGen, promedios, mejores):
    min_g=sys.maxsize 
    max_g=0
    p=0
    for i in range(tam):
        a= poblacion[i]['Fit']
        p=p+a
        if min_g > a:
            min_g = a
        elif max_g < a:
            max_g = a
    mejores.append(min_g)
    promedios.append(p/tam)
    print('Poblacion Inicial:')
    print(poblacion)
    j=1
    while j < NroGen:
        min=sys.maxsize
        max=0
        pro=0
        i=0
        while i < tam:
            aux=poblacion[i]['Camino']
            fit_o=poblacion[i]['Fit']
            pos1=random.randint(1,len(aux)-2)
            pos2=random.randint(1,len(aux)-2)
            t=poblacion[i]['Camino'][pos1]
            poblacion[i]['Camino'][pos1]=poblacion[i]['Camino'][pos2]
            poblacion[i]['Camino'][pos2]=t
            fit=getFit(G,poblacion[i]['Camino'])
            poblacion[i]['Fit'] = fit
            if(fit > promedios[-1]):
                poblacion[i]['Camino']= aux
                poblacion[i]['Fit']=fit_o
            else:
                i=i+1
                pro=pro+fit
                if max < fit: max= fit
                elif min > fit: min= fit
        mejores.append(min)
        promedios.append(pro/tam)
        print(j,' º Generacion')
        print(poblacion)
        j=j+1


def alg_gen_desorden(G,poblacion,tam,NroGen, promedios, mejores,indice):
    min_g=sys.maxsize 
    max_g=0
    p=0
    for i in range(tam):
        a= poblacion[i]['Fit']
        p=p+a
        if min_g > a:
            min_g = a
        elif max_g < a:
            max_g = a
    mejores.append(min_g)
    promedios.append(p/tam)
    print('Poblacion Inicial:')
    print(poblacion)
    j=1
    while j < NroGen:
        min=sys.maxsize
        max=0
        pro=0
        i=0
        while i < tam:
            aux=poblacion[i]['Camino']
            fit_o=poblacion[i]['Fit']
            pos1=random.randint(1,len(aux)-2)
            pos2=random.randint(1,len(aux)-2)
            it1=0
            it2=0
            if pos1 < pos2:
                it1=pos1
                it2=pos2
            else:
                it2=pos1
                it1=pos2
            sub_l=poblacion[i]['Camino'][it1:it2+1]
            random.shuffle(sub_l)
            q=0
            while it1 <= it2:
                poblacion[i]['Camino'][it1]=sub_l[q]
                q=q+1
                it1=it1+1
            
            fit=getFit(G,poblacion[i]['Camino'])
            poblacion[i]['Fit'] = fit
            if(fit > promedios[-1]):
                poblacion[i]['Camino']= aux
                poblacion[i]['Fit']=fit_o
            else:
                i=i+1
                pro=pro+fit
                if max < fit: max= fit
                elif min > fit: min= fit
        mejores.append(min)
        indice=i
        promedios.append(pro/tam)
        print(j,' º Generacion')
        print(poblacion)
        j=j+1
    

def main():
    G = nx.Graph()
    print("Elige el numero de nodos")
    NroNodos = int(input("->"))

    initNodos(G,NroNodos)
    dibujar(G)

    print("Elige el nodo de inicio")
    NodoInicio = int(input("->"))
    print("Elige el numero de caminos")
    NroCaminos = int(input("->"))
    poblacion = genPoblacion(NodoInicio, NroCaminos, NroNodos, G)
    print(poblacion)



    print("Elige la cantidad de generaciones")
    NroGen = int(input("->"))
    #gen
    indice=0
    promedios=[]
    mejores=[]
    #alg_gen_posicion(G,poblacion,NroCaminos,NroGen, promedios, mejores)
    alg_gen_desorden(G,poblacion,NroCaminos,NroGen, promedios, mejores,indice)
    
    mej=mejores[-1]
    for i in range(NroCaminos):
        if(poblacion[i]["Fit"]==mej):
            indice=i
    print(indice)
    print('Promedios',promedios)
    print('Mejores',mejores)

    li=[]
    for w in range(0, NroGen):
        li.append(w)
    
    fig, ax = plt.subplots()
    ax.plot(li, promedios)
    ax.set_title('Evaluacion Respecto a Promedios',fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_xlabel("Generacion")
    ax.set_ylabel("Promedio")
    plt.show()

    fig1, ax1 = plt.subplots()
    ax1.plot(li, mejores)
    ax1.set_title('Evaluacion Respecto a Mejor Individuo',fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    ax1.set_xlabel("Generacion")
    ax1.set_ylabel("Mejor Individuo")
    plt.show()

    for i in range(len(poblacion[indice]["Camino"])-1):
        G.add_edge(poblacion[indice]["Camino"][i], poblacion[indice]["Camino"][i+1])

    dibujar(G)
main()































































#motomami