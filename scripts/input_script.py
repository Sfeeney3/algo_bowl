import random
import networkx as nx

class InputScript():
    """
    A class used to randomly generate an undirected graph and a subgraph
    for input into an algorithm that determines a tree with minimal cost

    ...

    Attributes
    ----------
    self: self

    params: a list of params currently the min or max nodes used to build
            the graph

    Methods
    -------
    equilikely:

        Generates a uniform equilikely distribution based on two given integers

    buld_graph:

        Builds an undirected fully connected networkx graph and builds a random sub graph from it
    
    output_graph:

        Generates an output in .txt file format based upon the input requirements for the algo_bowl
        project
        
        """

    def __init__(self,params:list) -> None:
        self.num_nodes = self.equilikely(min(params), max(params)) 
        self.num_required = self.equilikely(2, self.num_nodes)  # at least two required vertices
        self.build_graph()

    def equilikely(self, a: int, b: int) -> int:

        r = random.uniform(0.00001, 0.99999)
        return a + int((b - a + 1) * r)

    def build_graph(self) -> None:

        # Create an empty undirected graph
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(1, self.num_nodes + 1))  # Nodes start from 1
        
        for i in range(1, self.num_nodes + 1):
            for j in range(i + 1, self.num_nodes + 1): # Avoid adding self-loops and duplicate edges
                weight = self.equilikely(1, 50)
                self.graph.add_edge(i, j, weight=weight)
        
        self.required_vertices = random.sample(range(1, self.num_nodes + 1), self.num_required)

    def output_graph(self, filename='output_graph.txt') -> None:

        with open(filename, 'w') as file:
            num_edges = self.graph.number_of_edges()
            file.write(f"{self.num_nodes} {num_edges} {self.num_required}\n") #First row of file reqs
            file.write(" ".join(map(str, self.required_vertices)) + '\n') #Second row of file reqs
            
            #The corresponding sub graph edges and their weights
            for edge in self.graph.edges(data=True):
                file.write(f"{edge[0]} {edge[1]} {edge[2]['weight']}\n")



