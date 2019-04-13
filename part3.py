

import matplotlib.pyplot as plt
import networkx as nx
from load_graph import load_graph

graph = load_graph("data.json")

G = nx.Graph()

def getLabel(name):

    if graph.get_nodes()[name]['json_class'] == 'Actor':

        return name + " age: " + str(graph.get_nodes()[name]["age"])
    else:
        return name + " gross: " + str(graph.get_nodes()[name]["box_office"])

s = 'Mickey Rourke'

neimovies = graph.get_neighbors(s)

for nei in neimovies:

    G.add_edge(getLabel(s), getLabel(nei))

    for act in graph.get_neighbors(nei):

        G.add_edge(getLabel(act), getLabel(nei))


pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)

nx.draw_networkx_edges(G, pos)


nx.draw_networkx_labels(G, pos)

plt.axis('off')
plt.show()