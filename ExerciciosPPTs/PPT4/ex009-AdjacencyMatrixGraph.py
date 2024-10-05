import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.dense_gnm_random_graph(5, 5, seed=12345)

fig, ax = plt.subplots()
layout = nx.shell_layout(G)

nx.draw(G, ax=ax, pos=layout, with_labels=True)

ax.set_title("Simple Networkx Drawing")

plt.show()