import json


class Graph:
    """
    general graph data structure
    """
    def __init__(self, directed = False):
        """
        :param directed: whether directed graph
        :return:
        """
        self.nodes = {}
        self.adjList = {}
        self.directed = directed
        self.weights = {}

    def add_node(self, id, data):
        """
        add node
        :param id: node id
        :param data: data for node
        :return: True if success false otherwise
        """
        if id in self.nodes:
            return False

        else:
            self.nodes[id] = data
            self.adjList[id] = []
            return True

    def add_edge(self, id1, id2, weight = 0):
        """
        add edge
        :param id1: node1 id
        :param id2: node2 id
        :param weight: weight of the edge
        :return: True if success false otherwise
        """
        if id1 not in self.nodes or id2 not  in self.nodes:
            return False

        else:
            if id2 in self.adjList[id2]:
                return False

            else:
                self.adjList[id1].append(id2)

                self.weights[(id1, id2)] = weight
                if not self.directed:

                    self.adjList[id2].append(id1)

                    self.weights[(id2, id1)] = weight

                return True

    def set_weight(self, id1, id2, weight):
        """
        set weight of edge
        :param id1: node1 id
        :param id2: node2 id
        :param weight: weight of the edge
        :return: None
        """
        if id1 not in self.nodes or id2 not  in self.nodes:
            return False

        self.weights[(id1, id2)] = weight

        if not self.directed:

            self.weights[(id2, id1)] = weight

    def get_weight(self, id1, id2):
        """
        :param id1:
        :param id2:
        :return: weight of edge (id1, id2)
        """
        if (id1, id2) not in self.weights:

            return None

        else:

            return self.weights[(id1, id2)]


    def get_data(self, id):
        """
        :param id: node id
        :return: data for this node
        """
        if id not in self.nodes:

            return None

        else:
            return self.nodes[id]


    def get_neighbors(self, id):
        """

        :param id: node id
        :return: a list of neigh node ids
        """
        if id not  in self.nodes:
            return None

        else:
            return self.adjList[id]

    def get_nodes(self):
        """
        :return: all nodes
        """
        return self.nodes

    def write_to_json(self, filename):
        """
        write graph to json file
        :param filename: file name to write
        :return: None
        """
        with open(filename, 'w') as f:

            weights = {'$'.join(k):v for k, v in self.weights.items()}

            g = {'nodes': self.nodes, 'adjList': self.adjList, 'directed': self.directed, 'weights': weights}
            json.dump(g, f)

    def load_from_json(self, filename):
        """
        load graph from json file
        :param filename:
        :return: None
        """
        with open(filename) as f:

            g = json.load(f)

            self.nodes = g['nodes']

            self.adjList = g['adjList']

            self.directed = g['directed']

            weights = { (tuple(k.split('$'))):w for k, w in g['weights'].items()}

            self.weights = weights

