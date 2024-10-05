import networkx as nx
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng(12345)
G = nx.gnm_random_graph(10, 17, seed=12345)

fig, ax = plt.subplots()
nx.draw_circular(G, ax=ax, with_labels=True)

ax.set_title("Random network for shortest path finding")

plt.show()