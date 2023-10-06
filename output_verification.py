import networkx as nx
from mst_algorithm.ipynb import *
# input_file = 'input.txt'

# # required vertices
# R = [1, 2, 3, 5]
# num_nodes = 5
# input_edges = ['1 2 2', '1 5 2', '1 4 1', '2 4 1', '3 4 1', '5 4 1', '2 3 2']

# # create graph from input file
# input_graph = nx.Graph()

# for in_edge in input_edges:
#     in_edge = in_edge.split()
#     input_graph.add_edge(in_edge[0], in_edge[1], weight=int(in_edge[2]))

# read from submitted output file, change later to read from stdin
filename = 'output.txt'
# filename = open(sys.argv[1])

file = open(filename)
input_values = file.readlines()

# cost of MST
total_cost = int(input_values[0])

# number of edges in the MST
num_edges = int(input_values[1])

# edges in the MST from the output file
edges = input_values[2:]
print(edges)
# create a graph from the output file
def create_MST(edges):
    if len(edges) != num_edges:
        print('Invalid output: Not enough edges provided')
        return
    else:
        G = nx.Graph()
        for i in range(num_edges):
            edge = edges[i]
            edge = edge[0:3].split()
            G.add_edge(edge[0], edge[1])
        return G

# check if the graph is a tree
def check_tree(G):
    if nx.is_tree(G):
        return True
    else:
        print("Invalid output: Output is not a tree")
        return False


# check if required nodes are present in the tree
def check_nodes(G):
    for i in range(len(R)):
        vertex = R[i]
        if G.has_node(str(vertex)):
            # print(vertex)
            pass
        else:
            print("Invalid output: All required nodes not present")
            return False
    return True

# check if the weights in the input graph add up to the total cost
def check_cost(input_graph, total_cost):
    cost = 0
    for i in range(num_edges):
        edge = input_values[i + 2]
        edge = edge[0:3].split()
        cost += input_graph.get_edge_data(edge[0], edge[1])['weight']
        print(type(cost))
    if cost == total_cost:
        return True
    else:
        print('Invalid output: Incorrect total cost')
        return False


# CHECK OUTPUT
G = create_MST(edges)
check_tree(G)
check_nodes(G)
check_cost(input_graph, total_cost)
