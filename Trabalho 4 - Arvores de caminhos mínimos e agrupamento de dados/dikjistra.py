# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
from heapq import heappop, heappush
from matplotlib import pyplot as plt

push = heappush
pop = heappop
    
def Relax(G):
    


def Dijkstra (G,s):
    λ = {}
    π = {}
    #Setando todos os nodes como infinito
	for v in G.nodes():
		λ[v] = np.inf
		π[v] = 'null'
        
    for v,u in G.edges():
        if ('weight' not in G[u][v]):
            G[e][x]['weight'] = 1
        
    