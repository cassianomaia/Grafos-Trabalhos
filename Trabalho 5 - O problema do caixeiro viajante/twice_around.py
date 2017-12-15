# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from heapq import heappop, heappush

pop = heappop
push = heappush

def tour_weight(G): 
    weight = 0
    weight_vector = nx.get_edge_attributes(G, 'weight')
    for v in G.edges(): 
        weight += weight_vector[v]
    return weight

def twice_around(G, s):
    Mst = nx.minimum_spanning_tree(G)
    Mst = nx.MultiGraph(Mst)
       
    for u,v in Mst.edges():
        Mst.add_edge(u,v)
    
    tour_euler = list(nx.eulerian_circuit(Mst, s)) 
    Result = nx.Graph()
    aux = []
    for u,v in tour_euler: 
        aux.append(u)
        aux.append(v)
    h = []
    for i in aux: 
        if (i not in h):
            h.append(i)
    h.append(s)
    for i in range (30):
        Result.add_edge(h[i],h[i+1])
        Result[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight']   
    return Result


A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

Result = twice_around(G, 1)
nx.draw_networkx(Result)
plt.show()