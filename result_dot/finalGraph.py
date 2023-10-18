import networkx as nx
import os
# 创建一个空的有向图
new_graph = nx.DiGraph()

# 读取9个dot文件并统计边的出现次数
edge_counts = {}
for i in range(1, 10):
    dot_file = f"graph ({i}).dot"
    graph = nx.drawing.nx_agraph.read_dot(dot_file)
    edges = graph.edges()
    for edge in edges:
        if edge in edge_counts:
            edge_counts[edge] += 1
        else:
            edge_counts[edge] = 1

# 遍历边和它们的出现次数，根据条件添加到新图中
for edge, count in edge_counts.items():
    if count > 6:
        new_graph.add_edge(edge[0], edge[1], style='solid')
    elif count > 5:
        new_graph.add_edge(edge[0], edge[1], style='dashed')


# 将新图保存为dot文件
nx.drawing.nx_agraph.write_dot(new_graph, 'final_graph.dot')
os.system('dot -Tsvg final_graph.dot -o final_graph.svg')
