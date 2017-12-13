# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
import pylab as plt

def ExtractMin(Q):
	dict_min = {}

	for key, value in Q.items():
		dict_min[key] = value['key']

	return min(dict_min, key=dict_min.get)

def PrimMST(G, r):
	λ = {}
	π = {}
	for v in G.nodes():
		λ[v] = np.inf
		π[v] = 'null'

	λ[r] = 0
	S = {}

	while λ:
		u = ExtractMin(λ)
		del λ[u]
		S.append(u)

		for neighboor in G[u]:
			if neighboor in λ:
				if G[u][neighboor]['weight'] < λ[neighboor]:
					π[neighboor] = u
					λ[neighboor] = G[u][neighboor]['weight']
					