import networkx as nx
import sys
# input_file = 'input.txt'
# required vertices
R = [1, 2, 3, 5]
num_nodes = 4
G = nx.Graph()

filename = 'output.txt'
# filename = open(sys.argv[1])

filename = open(filename)
input_values = filename.readlines()
total_cost = input_values[0].split()

num_edges = int(input_values[1])

# create a graph from the output file
for i in range(num_edges):
    edge = input_values[i+2]
    edge = edge[0:3].split()
    G.add_edge(edge[0], edge[1])

# check if the graph is a tree
def check_tree():
    if nx.is_tree(G):
        pass
    else:
        print("Invalid output: Output is not a tree")
        return False
    return True

# check if required nodes are present in the tree
def check_nodes(G):
    for i in range(len(R)):
        vertex = R[i]
        if G.has_node(str(vertex)):
            # print(vertex)
            pass
        else:
            print("Required nodes not present in tree")
            return False
    return True

# check if the weights in the input graph add up to the total cost
    




