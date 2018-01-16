import random

class Node:

    def __init__(self, value, nodes_number):
        probability = random.randint(1, nodes_number)
        self.all_null = True
        self.value = value
        self.adjacent_nodes_maximum_amount = random.randint(0, nodes_number) #We get the range
        self.adjacent_nodes_amount = random.randint(0, self.adjacent_nodes_maximum_amount) #Plus the amount of nodes we are going to pick up capped at our previous variable, so we don't pick more than there are
        self.adjacency_list = list(range(0, probability))
        self.adjacency_list = [n + 1 for n in self.adjacency_list]
        self.adjacency_list = [vertex for vertex in self.adjacency_list if vertex != self.value]
        self.adjacency_list = [(vertex, random.randint(0, 100)) for vertex in self.adjacency_list]

    def get_adjacency_list(self):
        return self.adjacency_list


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def make_undirected(self):
        nodes_dictionary = {}
        for node in self.nodes:
            node.adjacency_list = [vertex[0] for vertex in node.adjacency_list]
            nodes_dictionary[node.value] = node.adjacency_list
        for node in self.nodes:
            value = node.value
            for adjacent_node in node.adjacency_list:
                nodes_dictionary[adjacent_node].append(value)
        for node in self.nodes:
            node.adjacency_list = set(nodes_dictionary[node.value])

def create_graph(n_nodes):
    nodes = [Node(n + 1, n_nodes) for n in range(0, n_nodes)]
    graph = Graph(nodes)  # We generate a random graph
    return graph

def main():
    n_nodes = int(input("Type a number of vertices" ))
    graph = create_graph(n_nodes) #It creates a directed graph by default
    for node in graph.nodes:
        print("Node: ")
        print(str(node.value))
        print("Adjacent nodes to " + str(node.value))
        print(node.adjacency_list)
        print("\n")

if __name__ == '__main__':
    main()