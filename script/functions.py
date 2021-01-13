# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:04:35 2020

@author: acava
"""

from itertools import product
import random

# Generating all the possible combination of genetic sequence o given length

def graph_generator(gen_bases, len_seq):
    
    list_vertices = [''.join(pastata) for pastata in vertices_generator(gen_bases, len_seq)]
    graph_dict ={}
    
    for ind in list_vertices:
        graph_dict[ind] = edges_generator(ind, list_vertices)
        
    return graph_dict


def vertices_generator(bases, str_len):
    
    chars = list(bases)
    results = []
    
    for c in product(chars, repeat = str_len):
       results.append(c)
  
    return results


def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))


def edges_generator(vertex, list_vertex):
    
    list_results = []
    
    for ind in list_vertex:
        if(hamming_distance(vertex,ind)==1):
            list_results.append(ind)
    
    return list_results


def edges_pruning(old_list, proba):
    new_list = []
    for ind, ver in enumerate(old_list):
        if random.uniform(0, 1) < proba:
            new_list.append(ver)
            
    return new_list