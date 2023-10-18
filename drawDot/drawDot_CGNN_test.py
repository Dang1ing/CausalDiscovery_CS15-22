import networkx as nx
from cdt.causality.graph import CGNN
from cdt.data import load_dataset
import matplotlib as plt

data, graph = load_dataset("sachs")
obj = CGNN(nh=20, nruns=16, njobs=None, gpus=None, batch_size=-1, lr=0.01,
           train_epochs=50, test_epochs=50, verbose=None, dataloader_workers=0)
# The predict() method works without a graph, or with a
# directed or undirected graph provided as an input

output = obj.predict(data, nx.Graph(graph))  # With an undirected graph

# To view the graph created, run the below commands:
nx.draw_networkx(output, font_size=8)
plt.show()
