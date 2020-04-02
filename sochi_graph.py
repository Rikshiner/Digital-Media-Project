# Requires Networkx and matplotlib
import networkx as nx
import matplotlib.pyplot as plt
# Data file and creating an empty graph to use
s_data ="sochiAD.txt"
Graphtype=nx.Graph()

# How to read from a file from the edge list
G = nx.read_edgelist(s_data, create_using=Graphtype, data=(('weight',int),))
# Removes the nodes wiht no connections
G.remove_nodes_from(list(nx.isolates(G)))

# Below are the filters to delete certain nodes based on some criteria

# The first 2 are based on the amount of nodes in a component, top gets rid of components over a certain amount
'''
for component in list(nx.connected_components(G)):
    if len(component)>1000:
        for node in component:
            G.remove_node(node)
'''
# The second takes out components of less than a certain amount
for component in list(nx.connected_components(G)):
    if len(component)<3:
        for node in component:
            G.remove_node(node)

# These 2 delete nodes depending on their degree, with the top deleting all over a certain degree

to_del = [n for n in G if G.degree(n) >= 100]
G.remove_nodes_from(to_del)

# This second one deletes the nodes below a certain degree

to_del_2 = [n for n in G if G.degree(n) <= 30]
G.remove_nodes_from(to_del_2)

# Prints the amount of nodes
print(len(G))
# Draws the graph
nx.draw(G)  # networkx draw()
plt.draw()  # pyplot draw()
plt.show()
