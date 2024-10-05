import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(15, 22, seed=12345)
fig, ax = plt.subplots()

pos = nx.circular_layout(G)

nx.draw(G, pos=pos, ax=ax, with_labels=True)

ax.set_title("Network with minimum spanning tree overlaid")

min_span_tree = nx.minimum_spanning_tree(G)

print(list(min_span_tree.edges))

nx.draw_networkx_edges(min_span_tree, pos=pos, ax=ax, width=1.5, 
edge_color="r")

plt.show()