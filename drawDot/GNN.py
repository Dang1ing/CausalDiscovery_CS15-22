from cdt.causality.pairwise import GNN
import networkx as nx
import matplotlib.pyplot as plt
from cdt.data import load_dataset
data, labels = load_dataset('tuebingen')
obj = GNN()
# This example uses the predict() method
output = obj.predict(data)
# This example uses the orient_graph() method. The dataset used
# can be loaded using the cdt.data module
# data, graph = load_dataset("sachs")
# output = obj.orient_graph(data, nx.Graph(graph))
# To view the directed graph run the following command
nx.draw_networkx(output, font_size=8)
plt.show()
