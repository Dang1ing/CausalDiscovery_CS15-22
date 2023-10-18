import networkx as nx
import pandas as pd
from cdt.causality.graph import IAMB
from cdt.data import load_dataset
import os

# data, graph = load_dataset("sachs")
obj = IAMB(alpha=0.05)
data = pd.read_csv('cs15_22_float.csv')
output = obj.predict(data)  # No graph provided as an argument
nx.drawing.nx_agraph.write_dot(output, 'cs15_22_IAMB.dot')
os.system('dot -Tsvg cs15_22_IAMB.dot -o cs15_22_IAMB.svg')
