import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from(range(10))
G.add_edges_from([
(0, 1), (1, 2), (2, 3), (2, 4), 
(2, 5), (3, 4), (4, 5), (6, 7),
(6, 8), (6, 9), (7, 8), (8, 9)
])
fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)
ax.set_title("Simple network")
plt.show()

is_planar = nx.check_planarity(G)
print("Is planar: ", is_planar)