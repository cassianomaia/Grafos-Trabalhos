# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

def Prim(G, r):
	λ = {}
	π = {}
    #Setando todos os nodes como infinito
	for v in G.nodes():
		λ[v] = np.inf
		π[v] = 'null'
   #Setando o node inicial como zero
	λ[r] = 0
	Mst = nx.create_empty_copy(G)
    
	while λ:
		u = min(λ,key = λ.get)
		del λ[u]
		for neighboor in G[u]:
			if neighboor in λ and G[u][neighboor]['weight'] < λ[neighboor]:
				π[neighboor] = u
				λ[neighboor] = G[u][neighboor]['weight']
		if π[u] is not 'null':
			for v1,v2,data in G.edges(data=True):
				if (v1 == π[u] and v2 == u):
					Mst.add_edge(v1,v2, weight=data['weight']) 
					Mst_final = Mst.copy() 
				elif (v1 == u and v2 == π[u]):
					Mst.add_edge(v2,v1, weight=data['weight'])
					Mst_final = Mst.copy()
	return Mst_final

A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

M = Prim(G, 0)
nx.draw_networkx(M)
plt.savefig("teste.pdf")
plt.show()