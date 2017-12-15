# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx

def power_method(Matriz, qtd):
    vertices = Matriz.shape[0]
    digrafo = [0 for v in range(vertices)]
    
    
    for v in range(qtd):
        digrafo = np.dot(digrafo, Matriz)
    
    digrafo = digrafo.tolist()
    digrafo = digrafo[0]
    tabela = {}
    for v in range(0, len(digrafo)):
        tabela[v+1] = digrafo[v]
    return tabela

def PageRank(Matriz, qtd, α):
    vertices = Matriz.shape[0]
    matriz_ = np.dot((1-α), Matriz) + (α*(1/vertices))
    
    tabela = power_method(matriz_, qtd)
    return tabela


Digrafo = nx.DiGraph()
Digrafo.add_nodes_from(range(1, 37))
Digrafo.add_edges_from([(1, 2), (1, 3)])
Digrafo.add_edges_from([(3, 4), (3, 5)])
Digrafo.add_edges_from([(6, 7), (6, 8)])
Digrafo.add_edges_from([(7, 8),  (7, 9)])
Digrafo.add_edges_from([(8, 9),  (8, 10)])
Digrafo.add_edges_from([(10, 11),  (10, 12)])
Digrafo.add_edges_from([(11, 12),  (11, 13)])
Digrafo.add_edges_from([(12, 13),  (12, 14)])
Digrafo.add_edges_from([(13, 14),  (13, 15)])
Digrafo.add_edges_from([(14, 15),  (14, 16)])
Digrafo.add_edges_from([(15, 16),  (15, 17)])
Digrafo.add_edges_from([(16, 17),  (16, 18)])
Digrafo.add_edges_from([(19, 20),  (19, 21)])
Digrafo.add_edges_from([(21, 22),  (21, 23)])
Digrafo.add_edges_from([(22, 23),  (22, 24)])
Digrafo.add_edges_from([(23, 24),  (23, 25)])
Digrafo.add_edges_from([(23, 24),  (23, 25)])
Digrafo.add_edges_from([(26, 27),  (26, 28)])
Digrafo.add_edges_from([(27, 28),  (27, 29)])
Digrafo.add_edges_from([(28, 29),  (28, 30)])
Digrafo.add_edges_from([(29, 30),  (29, 31)])
Digrafo.add_edges_from([(30, 31),  (30, 32)])
Digrafo.add_edges_from([(31, 32),  (31, 33)])
Digrafo.add_edges_from([(33, 34),  (33, 35)])
Digrafo.add_edge(2, 15)
Digrafo.add_edge(5, 7)
Digrafo.add_edge(9, 27)
Digrafo.add_edge(18, 29)
Digrafo.add_edge(25, 35)
Digrafo.add_edge(17, 4)
Digrafo.add_edge(20, 6)
Digrafo.add_edge(24, 16)
Digrafo.add_edge(32, 30)
Digrafo.add_edge(34, 12)

#calculo da matriz de transição
Matriz_Adjacência = nx.to_numpy_matrix(Digrafo)
Matriz_Deltas = np.zeros((36,36))
for v in range(1,37):
    if Digrafo.degree(v) != 0:
        Matriz_Deltas[v-1][v-1] = 1/float(Digrafo.degree(v))
    
Matriz_Probabilidades = np.dot(Matriz_Deltas, Matriz_Adjacência)
np.savetxt('matriz_adjacencias.txt', Matriz_Adjacência, delimiter=',', fmt='%1.0e')
np.savetxt('deltas.txt', Matriz_Deltas, delimiter=',', fmt='%1.0e')
Results = power_method(Matriz_Probabilidades, 100)

for v in range(1,37):
    print(Results[v])