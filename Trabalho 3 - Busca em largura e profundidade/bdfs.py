# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

def BFS(G,s):
    color = {}
    λ = {} #vetor de distancia
    π = {} #vetor de predecessores
    
    for v in G.nodes():
        color[v] = 'white'
        λ[v] = np.inf
        π[v] = 'null'
    
    color[s] = 'gray'
    λ[s] = 0
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in G.neighbors(u):
            if color[v] == 'white':
                color[v] = 'gray'
                λ[v] = λ[u] + 1
                π[v] = u
                Q.append(v)
        color[u] = 'black'
    BFS_tree = nx.create_empty_copy(G)
    for v1,v2,data in G.edges():
        if (π[v2] is v1) or (π[v1] is v2 and not nx.is_directed(BFS_tree)):
            BFS_tree.add_edge( v1,v2,data )
            BFS_tree.node[v1]['depth'] = π[v1]
            BFS_tree.node[v2]['depth'] = π[v2]
    return BFS_tree


G_karate = nx.read_pajek('karate.paj')
G_dolphins = nx.read_pajek('dolphins.paj')

Karate_bfs = BFS(G_karate, 1)
nx.draw_networkx(Karate_bfs)
plt.show()