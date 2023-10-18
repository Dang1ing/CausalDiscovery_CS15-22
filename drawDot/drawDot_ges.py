import pandas as pd
from graphviz import Source
import networkx as nx
import cdt
import matplotlib.pyplot as plt
import cdt.causality.graph as graph
from cdt.data import load_dataset
from IPython.display import Image, display
from cdt.metrics import (precision_recall, SID, SHD)
import os

data = pd.read_csv('cs15_22.csv')
# skel = nx.drawing.nx_agraph.read_dot('ard.dot')
# obs和int没区别
model = graph.GES(score="obs")
output = model.predict(data)
nx.drawing.nx_agraph.write_dot(output, 'cs15_22_ges.dot')
os.system('dot -Tsvg cs15_22_ges.dot -o cs15_22_ges.svg')
