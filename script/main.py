# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:59:31 2020

@author: acava
"""

import pandas as pd
import os

path_script = 'C:\\Users\\acava\\Documents\\data_science\\genGraphPercolation\\script'
os.chdir(path_script)
os.getcwd()

import class_graph
import functions as F

genetic_bases = 'ACGT'
len_sequence = 4

graph = F.graph_generator(genetic_bases, len_sequence)

        
