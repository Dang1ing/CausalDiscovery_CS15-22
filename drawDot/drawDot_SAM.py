# import networkx as nx
# import pandas as pd
# from cdt.causality.graph import SAM
# from cdt.data import load_dataset
# import os

# # data, graph = load_dataset("sachs")
# obj = SAM(lr=0.01, dlr=0.001, mixed_data=False, lambda1=10, lambda2=0.001, nh=20, dnh=200, train_epochs=100, test_epochs=100, batch_size=-1,      losstype='fgan', dagloss=True, dagstart=0.5,
#           dagpenalization=0, dagpenalization_increase=0.01, functional_complexity='l2_norm', hlayers=2, dhlayers=2, sampling_type='sigmoidproba', linear=False, nruns=8, njobs=None, gpus=None, verbose=None)
# # obj = SAM()
# data = pd.read_csv('cs18.csv')
# output = obj.predict(data)  # No graph provided as an argument
# nx.drawing.nx_agraph.write_dot(output, 'cs18_SAM.dot')
# os.system('dot -Tsvg cs18_SAM.dot -o cs18_SAM.svg')

import networkx as nx
import matplotlib as plt
from cdt.causality.graph import SAM
from cdt.data import load_dataset
data, graph = load_dataset("sachs")
obj = SAM(lr=0.01, dlr=0.001, mixed_data=False, lambda1=10, lambda2=0.001, nh=20, dnh=200, train_epochs=100, test_epochs=100, batch_size=-1, losstype='fgan', dagloss=True, dagstart=0.5,
          dagpenalization=0, dagpenalization_increase=0.01, functional_complexity='l2_norm', hlayers=2, dhlayers=2, sampling_type='sigmoidproba', linear=False, nruns=8, njobs=1, gpus=1, verbose=None)

# The predict() method works without a graph, or with a
# directed or undirected graph provided as an input
output = obj.predict(data)  # No graph provided as an argument
# output = obj.predict(data, nx.Graph(graph))  #With an undirected graph
# output = obj.predict(data, graph)  #With a directed graph
# To view the graph created, run the below commands:
nx.draw_networkx(output, font_size=8)
plt.show()
