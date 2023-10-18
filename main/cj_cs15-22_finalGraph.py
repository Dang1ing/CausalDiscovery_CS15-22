import networkx as nx
from graphviz import Digraph

# 创建一个空的图用于保存边的出现次数
edge_counts = nx.Graph()

# 遍历9个 dot 文件，统计边的出现次数
for i in range(1, 10):
    # 读取第 i 个 dot 文件并将其转换为 NetworkX 图
    dot_file = f'graph ({i}).dot'
    graph = nx.drawing.nx_agraph.read_dot(dot_file)

    # 统计每条边的出现次数
    for edge in graph.edges():
        if edge in edge_counts:
            edge_counts[edge] += 1
        else:
            edge_counts[edge] = 1

# 创建一个新的 Digraph 对象来保存结果
final_graph = Digraph(format='png')

# 遍历边的出现次数，根据条件标记边的属性
for edge, count in edge_counts.items():
    if count > 7:
        # 高置信度边，使用实线
        final_graph.edge(edge[0], edge[1], style='solid')
    elif count > 3:
        # 低置信度边，使用虚线
        final_graph.edge(edge[0], edge[1], style='dashed')

# 保存最终图为 dot 文件
final_graph.save('final_graph.dot')

# 可以选择将最终图保存为其他格式（例如 PNG 图像）：
# final_graph.render('final_graph', format='png')
