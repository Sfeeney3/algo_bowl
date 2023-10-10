import networkx as nx

# our input, will remain constant
input_file = r'/home/saniya/PycharmProjects/algobowl/algo_bowl/inputs/keg_graph_bias_6367_1_5V_15_50R.txt'
input_file = open(input_file)
in_graph = input_file.readlines()

# number of nodes, number of edges, number of R vertices
num_nodes, num_in_edges, num_R = [int(i) for i in in_graph[0].split()]

# required vertices
R = [int(v) for v in in_graph[1].split()]
# print(R)

# edges in the input graph
input_edges = []
for i in range(num_in_edges):
    input_edges.append(in_graph[i+2].split())

# create graph from input file
input_graph = nx.Graph()
for in_edge in input_edges:
    input_graph.add_edge(in_edge[0], in_edge[1], weight=int(in_edge[2]))

print(input_graph)
# print(nx.is_connected(input_graph))
# output file submitted by other groups,  change to read from output folder
filename = '/home/saniya/PycharmProjects/algobowl/algo_bowl/outputs/keg_graph_bias_6367_1_5V_15_50R_sa.txt'
# filename = open(sys.argv[1])

file = open(filename)
file_lines = file.readlines()

# cost of MST
total_cost = int(file_lines[0])

# number of edges in the MST
num_edges = int(file_lines[1])

# edges in the MST from the output file
edges = file_lines[2:]
# print(edges)
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
            # print(edge)
            G.add_edge(edge[0], edge[1])
        # print(G)
        return G

# check if the graph is a tree
def check_tree(G):
    if nx.is_tree(G):
        pass
    else:
        print("Invalid output: Output is not a tree")
    return


# check if the required nodes are present in the tree
def check_nodes(G, R):
    for i in range(len(R)):
        vertex = R[i]
        if G.has_node(str(vertex)):
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