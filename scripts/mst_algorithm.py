
import networkx as nx
import sys
import random
import math




class MST:
    '''
    Class that constructs input graph and finds the Minimum Spanning Tree for a set of vertices
    '''
    def __init__(self, data):
        '''
        Take data and construct graph
        '''
        self.data = data
        self.generate_graph()
        nodes = self.graph.nodes
        
        # Initialize final edge list
        self.final_edges = []
        
    #-----------Methods-------------------
    def find_minimum_subset_tree(self):
        '''
        Run full algorithm to find minimum tree spanning subset R of V
        '''
        self.get_all_shortest_paths(self.graph)
        self.create_shortest_paths_graph()
        self.mst(self.graph)
        self.get_mst_of_sp_graph()
        self.final_cost = self.get_graph_cost(self.final_edges)
        
        # generate output
        out_string = str(self.final_cost) + '\n'
        out_string += str(len(self.final_edges)) + '\n'
        
        for edge in self.final_edges:
            out_string += '{} {}\n'.format(edge[0], edge[1])
        
        return out_string
    
    def get_all_shortest_paths(self, graph):
        '''
        Calculate shortest paths between node i and node j, for all (i, j) in required vertices
        '''
        self.shortest_paths_list = []
        
        for i in range(int(self.dims[2])):
            for j in range(i+1, int(self.dims[2])):
                
                # Run Dijkstra's to compute shortest path between i and j
                self.shortest_paths_list.append(nx.shortest_path(graph, source=self.r_vertices[i], target=self.r_vertices[j], method='dijkstra'))
        
    def create_shortest_paths_graph(self):
        '''Creates graph of shortest paths between all required vertices'''
        
        self.sp_graph = nx.Graph()
        self.edge_dict = {} # Conversion dictionary for edges
        
        for sp in self.shortest_paths_list:
            # Get edges
            edges = [(sp[i], sp[i+1]) for i in range(len(sp) - 1)]
            # Get weights of edges
            tot_weight = 0
            for edge in edges:
                weight = self.graph.get_edge_data(edge[0], edge[1])['weight']
                tot_weight += weight
            # Create edge from the beginning of path to end of path, assigning total weight to edge
            self.sp_graph.add_edge(sp[0], sp[-1], weight=tot_weight)
            self.edge_dict['(\'{}\', \'{}\')'.format(sp[0], sp[-1])] = edges     
            
    def get_mst_of_sp_graph(self):
        '''
        Compute the minimum spanning tree of shortest paths graph, then create the final edge list
        '''
        self.sp_graph = self.mst(self.sp_graph)
        
        for edge in self.sp_graph.edges:
            self.final_edges.extend(self.edge_dict[str(edge)])
        
    def mst(self, graph):
        '''
        Run Prim's algorithm on given graph
        '''
        return nx.minimum_spanning_tree(graph, algorithm='prim')
            
    def generate_graph(self):
        self.dims = self.data.pop(0).split(' ')
        self.r_vertices = self.data.pop(0).split(' ')
        self.graph = nx.Graph()
        self.graph.add_nodes_from([str(i) for i in range(1, int(self.dims[0]) + 1)]) # Graph is 1-indexed
        
        for i, edge in enumerate(self.data):
            edge = edge.strip().split(' ')
            self.graph.add_edge(edge[0], edge[1], weight=int(edge[2]))
    
    def get_graph_cost(self, graph):
        cost = 0
        if isinstance(graph, list):
            for edge in graph:
                cost += self.graph.get_edge_data(edge[0], edge[1])['weight']
        else:
            for edge in graph.edges:
                cost += graph.get_edge_data(edge[0], edge[1])['weight']
                
        return cost
    
    def check_tree(self, graph):
        '''
        Run search algorithm to check if input graph is a valid tree
        '''
        return nx.is_tree(graph)
    
#     def simulate_annealing(self):
#         '''
#         Run simulated annealing algorithm to find minimum spanning tree of required vertices
#         !! WILL NOT BE USING THIS FOR ALGOBOWL UNLESS WE NEED TO!!
#         '''
#         current_state = self.generate_random_tree()
#         k_steps = 10000
#         for k in range(k_steps+1):
#             T = (k_steps - k)
#             if T <=0:
#                 return current_state
#             next_state = self.get_neighbor()
#             delta = self.get_tree_cost(next_state) - self.get_tree_cost(current_state)
#             if delta < 0:
#                 current_state = next_state
#             else:
#                 prob = random.uniform(0,1)
#                 if prob <= math.exp(-delta/T):
#                     next_state = current_state
#         return current_state
    
#     def generate_random_tree(self):
#         pass
    
#     def get_neighbor(self, tree):
#         pass

