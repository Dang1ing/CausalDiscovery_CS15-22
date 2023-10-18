import networkx as nx
import pandas as pd
from cdt.causality.graph import CGNN
from cdt.data import load_dataset
import os

# data, graph = load_dataset("sachs")
obj = CGNN(nh=20, nruns=16, njobs=None, gpus=None, batch_size=-1, lr=0.01,
           train_epochs=50, test_epochs=50, verbose=None, dataloader_workers=0)
data = pd.read_csv('cs18.csv')
output = obj.predict(data)  # No graph provided as an argument
nx.drawing.nx_agraph.write_dot(output, 'cs18_CGNN.dot')
os.system('dot -Tsvg cs18_CGNN.dot -o cs18_CGNN.svg')
