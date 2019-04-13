
import json

from graph import Graph

def load_graph(fn):

    with open(fn) as f:

        graph = Graph()

        arr = json.load(f)

        for data in arr:

            for id in data:
                graph.add_node(id, data[id])

            for id in data:
                obj = data[id]

                if obj['json_class'] == 'Actor':
                    neighbors = obj['movies']

                else:
                    neighbors = obj['actors']

                for neighbor in neighbors:

                    graph.add_edge(id, neighbor)


    return graph

if __name__ == '__main__':

    graph = load_graph("data.json")




