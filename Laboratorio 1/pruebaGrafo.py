from ctypes import sizeof
from os import remove
import networkx as nx
from matplotlib import pyplot as plt
import math
import sys
import random
import os


sys.setrecursionlimit(5000)

def initGrafo(G, num):
    aux = 0
    for i in range(0,num):
        if(i == 0):
            G.add_node(i,pos = (i,aux))
        else:
            G.add_node(i,pos = (i,aux))
            G.add_edge(i,i-1, peso = 1)

    for i in range(1,num):
        for j in range(0, num):
            actual = (num*i) + j
            if(j == 0):
                G.add_node(actual, pos = (j, i))
                G.add_edge(actual, (actual)-num, peso = 1)
                G.add_edge(actual, (actual)-num + 1, peso = math.sqrt(2))
            if (j == num-1):
                G.add_node(actual, pos = (j, i))
                G.add_edge(actual, (actual)-1, peso = 1)
                G.add_edge(actual, (actual)-num - 1, peso = math.sqrt(2))
                G.add_edge(actual, (actual)-num, peso = 1)
            if(j > 0 and j < num-1):
                G.add_node(actual, pos = (j, i))
                G.add_edge(actual, (actual)-1, peso = 1)
                G.add_edge(actual, (actual)-num - 1, peso = math.sqrt(2))
                G.add_edge(actual, (actual)-num, peso = 1)
                G.add_edge(actual, (actual)-num + 1, peso = math.sqrt(2))

#Best First Search
def Best_First_Search(start, target, graph, res, queue = [], visited = []):
    if start not in visited:
        res.append(start)
        visited.append(start)

    queue = queue + [x for x in graph[start].items() if x[0] not in visited]
    queue.sort(key=lambda x:x[1]['peso'])

    if queue[0][0] == target:
        res.append(queue[0][0])
        # print("entro fin")
    else:
        pricessing = queue[0]
        queue.remove(pricessing)
        # print("entro else")
        Best_First_Search(pricessing[0], target, graph, res, queue, visited)

#DFS
def dfs(start, target, graph):
        
    path = [[start]]
    steps =0
    while path:
        steps = steps + 1
        index = -1
        s_path = path.pop(index)
        l_node = s_path[-1] # the last node is our target, it's done

        if l_node == target:
            print("Cantidad de Pasos -> {}" .format(steps))
            return s_path
        else:
            for node in graph[l_node]:
                if node not in s_path:
                    new_path = s_path + [node]  
                    path.append(new_path)               
    print('El camino no existe' %(start, target))


#BFS
def bfs1(start, target, graph):
    
    path = [[start]]
    steps = 0
    while path:
        steps = steps + 1
        index = 0
        s_path = path.pop(index)
        l_node = s_path[-1] # the last node is our target, it's done

        if l_node == target:
            print("Cantidad de Pasos -> {}" .format(steps))
            return s_path
        else:
            for node in graph[l_node]:
                if node not in s_path:
                    new_path = s_path + [node]  
                    path.append(new_path)
    
    print("El camino no existe {} {}" .format(start, target))                
    
    
def delNodes(G, porcentaje, tam, ini, fin):
    porcentajeInt = math.floor((tam*tam)*porcentaje/100)
    for i in random.sample(range(0,tam*tam),porcentajeInt):
        if(i != ini and i != fin):
            G.remove_node(i)



G = nx.Graph()
print("Elige el tama??o del grafo: ")
tam = int(input())
print("Escribe en que nodo inicia la busqueda del 0 al {}".format(tam*tam))
inicio = int(input())
print("Escribe en que nodo termina la busqueda del 0 al {}".format(tam*tam))
final = int(input())
print("Escribe el porcentaje de nodos que quieres eliminar:")
porcentaje = int(input())
## RECIBE EL GRAFO Y N PARA CREAR UN GRAFO DE N * N
initGrafo(G, tam)

delNodes(G,porcentaje,tam,inicio,final)

res=[]
#sorted(graph[start].items(),key=lambda x: getitem(x[1],'peso'))
while(True):

    print("Que busqueda deseas realizar: \n")
    print("1. Best First Search \n")
    print("2. A* \n")
    print("3. BFS \n")
    print("4. DFS \n")
    print("5. Salir")
    
    option = int(input("-> "))

    if(option == 1):
        Best_First_Search(inicio, final, G, res)
        color_map = []
        for node in G:
            if node in res:
                color_map.append('red')
            else: 
                color_map.append('blue')
        print("Cantidad de Pasos -> {}" .format(len(res)))
        print(res)
        nx.draw(G, nx.get_node_attributes(G, 'pos'),node_color = color_map, with_labels=True)
        plt.show()

    if(option == 3):
        res = bfs1(inicio, final, G)
        color_map = []
        for node in G:
            if node in res:
                color_map.append('red')
            else: 
                color_map.append('blue')
        print(res)
        nx.draw(G, nx.get_node_attributes(G, 'pos'),node_color = color_map, with_labels=True)
        plt.show()

    if(option == 4):
        res = dfs(inicio, final, G)
        color_map = []
        for node in G:
            if node in res:
                color_map.append('red')
            else: 
                color_map.append('blue')
        print(res)
        nx.draw(G, nx.get_node_attributes(G, 'pos'),node_color = color_map, with_labels=True)
        plt.show()
    if(option == 5):
        break
    os.system('cls' if os.name == 'nt' else 'clear')
        
    


# dfs(inicio, final, G, res)
# print(res)

# # G.remove_node(25)
# # G.remove_node(37)
# #G.remove_node(171)
# # print(list(G.nodes))

# color_map = []
# for node in G:
#     if node in res:
#         color_map.append('red')
#     else: 
#         color_map.append('blue') 

# ## dibujar nodos y aristas
# # nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True)
# nx.draw(G, nx.get_node_attributes(G, 'pos'),node_color = color_map, with_labels=True)

# ## MOSTRAR EL PESO DE LAS ARISTAS
# # nx.draw(
# #     G, nx.get_node_attributes(G, 'pos'), width=1, linewidths=1,
# #     node_size=500, node_color='pink', alpha=0.9,
# #     with_labels=True
# # )

# # nx.draw_networkx_edge_labels(
# #     G, nx.get_node_attributes(G, 'pos'),
# #     edge_labels= nx.get_edge_attributes(G, 'peso'),
# #     font_color='red'
# # )

# plt.show()