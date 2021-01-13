# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:59:31 2020

@author: acava
"""

import pandas as pd
import numpy as np
import os

path_script = 'C:\\Users\\acava\\Documents\\GitHub\\genGraphPercolation\\script'
os.chdir(path_script)
os.getcwd()

from class_graph import Graph
import functions as F

genetic_bases = 'ACGT'
len_sequence = 4
prob_thre = 0.3
num_iteration = 5

np.random.seed(42)

# generation of the dictionary generating the genetic graph
graph_dict = F.graph_generator(genetic_bases, len_sequence)

# creation of the object graph
graph_structure = Graph(graph_dict)

# Edges of the link are kept if the extracted probability is less than threshold
list_edges_pruned = F.edges_pruning(graph_structure.edges(), prob_thre)
            




list_first_neig = [[i,ogg] for i, ogg in enumerate(list_edges_pruned) if len(set.intersection(list_edges_pruned[0], ogg))==1]
