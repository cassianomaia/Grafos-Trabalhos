# -*- coding: utf-8 -*-
import numpy as np

def power_method(Matriz, qtd):
    Vertices = Matriz.shape[0]
    digrafo = {}
    for i in range(Vertices):
        digrafo[i] = 0
    