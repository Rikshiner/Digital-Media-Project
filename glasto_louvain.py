# You need these 3 imports to run
import community
import networkx as nx
import matplotlib.pyplot as plt
# Data file and creating an empty graph to use
g_data ="glastoAD_bands_ext.txt"
Graphtype=nx.Graph()

# How to read from a file from the edge list
G = nx.read_edgelist(g_data, create_using=Graphtype, data=(('weight',int),))

# Below the exact same deletion method is used, please refer to notes in the graph code, different at the partition and beyomd

G.remove_nodes_from(list(nx.isolates(G)))

'''
for component in list(nx.connected_components(G)):
    if len(component)>1000:
        for node in component:
            G.remove_node(node)
'''
for component in list(nx.connected_components(G)):
    if len(component)<20:
        for node in component:
            G.remove_node(node)
'''
to_del = [n for n in G if G.degree(n) >= 100]
G.remove_nodes_from(to_del)


to_del_2 = [n for n in G if G.degree(n) <= 30]
G.remove_nodes_from(to_del_2)
'''
# First step is to find the best partition for the louvain
# Using the community package it finds the best partition for the modified graph

partition = community.best_partition(G, resolution = 1.5)
#partition = community.best_partition(G)
# Draws out the graph
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
# Begins the count to further partion until all nodes can no longer be put in a new community
count = 0
for com in set(partition.values()) :
     count += 1.
     list_nodes = [nodes for nodes in partition.keys()
                                 if partition[nodes] == com]
# Finally draw the graph itself from the communties found and plot these
     nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, node_color= str(count / size))
     #nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20, cmap=plt.get_cmap('jet'), node_color= range(31))
nx.draw_networkx_edges(G, pos, alpha=0.5)
print(partition)
print(max(partition.values()))
plt.show()
