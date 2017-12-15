# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from heapq import heappop, heappush

pop = heappop
push = heappush

def twice_around(G, s):
    Mst = nx.minimum_spanning_tree(G) # gero a mst a partir do grafo original
    Mst = nx.MultiGraph(Mst) # como somente multigrafos aceitam arestas paralelas
       
    for u,v in Mst.edges():
        Mst.add_edge(u,v)     #duplico arestas da mst
    
    euleraux = list(nx.eulerian_circuit(Mst, s)) # gero um circuito euleriano
    I = nx.Graph()
    aux = []
    for u,v in euleraux: 
        aux.append(u)
        aux.append(v)
    h = []
    for i in aux: 
        if (i not in h):    # elimino repetições
            h.append(i)
    h.append(origin)
    for i in range (30):
        I.add_edge(h[i],h[i+1]) # gero grafo resultante
        I[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight'] # copiando também o peso    
    return I

A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)
