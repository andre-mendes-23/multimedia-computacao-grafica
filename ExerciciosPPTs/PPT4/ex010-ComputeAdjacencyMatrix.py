import networkx as nx

G = nx.dense_gnm_random_graph(5, 5, seed=12345)

matrix = nx.adjacency_matrix(G).todense()
Matrix = nx.to_numpy_array(G)

print(matrix)