# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from heapq import heappop, heappush
from matplotlib import pyplot as plt

push = heappush
pop = heappop

def Dijkstra(G,s,m,f):
    λ = {}
    π = {}
    mst = nx.create_empty_copy(G)
    #Setando todos os nodes como infinito
    for v in G.nodes():
        λ[v] = np.inf
        π[v] = 'null'
        
    for v,u in G.edges():
        if ('weight' not in G[u][v]):
            G[u][v]['weight'] = 1
    
    λ[s] = 0
    π[s] = None
    #if para multisource até 3 no caso
    if m != 0:
        λ[m] = 0
        π[m] = None
    if f != 0:
        λ[f] = 0
        π[f] = None
        
    while λ:
        u = min(λ,key = λ.get)
        
        for neighbor in G[u]:
        	if neighbor in λ:
        		if λ[neighbor] > λ[u] + G[u][neighbor]['weight']:
        			π[neighbor] = u
        			λ[neighbor] = λ[u] + G[u][neighbor]['weight'] 

        del λ[u]

        if π[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if (v1 == π[u] and v2 == u):
                    mst.add_edge(v1,v2, weight=data['weight']) 
                elif (v1 == u and v2 == π[u]):
                    mst.add_edge(v2,v1, weight=data['weight'])
    return mst

A = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)


M_1 = Dijkstra(G, 0, 0, 0)
M_2 = Dijkstra(G, 0, 0, 58)
M_3 = Dijkstra(G, 0, 29, 58)
nx.draw_networkx(M_1)
plt.savefig("teste1.pdf")
plt.show()
nx.draw_networkx(M_2)
plt.savefig("teste2.pdf")
plt.show()
nx.draw_networkx(M_3)
plt.savefig("teste3.pdf")
plt.show()
