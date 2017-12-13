# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

def PrimMST(G, r):
	λ = {}
	π = {}
	for v in G.nodes():
		λ[v] = np.inf
		π[v] = 'null'

	λ[r] = 0
	Arestas = nx.create_empty_copy(G)

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
					Arestas.add_edge(v1,v2, weight=data['weight']) 
					Mst = Arestas.copy() 
				elif (v1 == u and v2 == π[u]):
					Arestas.add_edge(v2,v1, weight=data['weight'])
					Mst = Arestas.copy()
	return Mst







A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)

M = PrimMST(G, 0)
nx.draw_networkx(M)
plt.savefig("teste.pdf")
plt.show()