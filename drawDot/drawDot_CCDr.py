import networkx as nx
import pandas as pd
from cdt.causality.graph import CCDr
from cdt.data import load_dataset
import os

# data, graph = load_dataset("sachs")
obj = CCDr()
data = pd.read_csv('cs15_22.csv')
output = obj.predict(data)  # No graph provided as an argument
nx.drawing.nx_agraph.write_dot(output, 'cs15_22_CCDr.dot')
os.system('dot -Tsvg cs15_22_CCDr.dot -o cs15_22_CCDr.svg')
