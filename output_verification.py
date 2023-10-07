import networkx as nx

input_file = './inputs/hard_test_1_2_75num_bias2.txt'
input_file = open(input_file)
file_lines = input_file.readlines()

num_nodes, num_in_edges, num_R = [int(i) for i in file_lines[0].split()]
# print(num_nodes, num_edges, num_R)

# required vertices
R = [int(v) for v in file_lines[1].split()]
# print(R)

input_edges = []
for i in range(num_in_edges):
    input_edges.append(file_lines[i+2].split())

# print(input_edges)
# create graph from input file
input_graph = nx.Graph()

for in_edge in input_edges:
    input_graph.add_edge(in_edge[0], in_edge[1], weight=int(in_edge[2]))

print(input_graph)


# read from submitted output file, change later to read from stdin
filename = 'output_test.txt'
# filename = open(sys.argv[1])

file = open(filename)
input_values = file.readlines()

# cost of MST
total_cost = int(input_values[0])
# print(total_cost)
# number of edges in the MST
num_edges = int(input_values[1])

# edges in the MST from the output file
edges = input_values[2:]
# print(edges[0])
# print(num_edges)
# create a graph from the output file
def create_MST(edges):
    if len(edges) != num_edges:
        print('Invalid output: Not enough edges provided')
        return
    else:
        G = nx.Graph()
        for i in range(num_edges):
            edge = edges[i]
            edge = edge.split()
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
def check_nodes(G, R):
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
def check_cost(input_graph, edges, total_cost):
    cost = 0
    for i in range(num_edges):
        edge = edges[i]
        edge = edge.split()
        cost += input_graph.get_edge_data(edge[0], edge[1])['weight']
    # print(cost)
    if cost == total_cost:
        return True
    else:
        print('Invalid output: Incorrect total cost')
        return False


# CHECK OUTPUT
G = create_MST(edges)
check_tree(G)
check_nodes(G, R)
check_cost(input_graph, edges, total_cost)
