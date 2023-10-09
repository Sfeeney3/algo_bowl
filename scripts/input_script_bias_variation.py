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
        self.num_nodes = 1000 #self.equilikely(min(params), max(params))
        self.num_edges = 100000 
        self.num_required = self.equilikely(int(self.num_nodes*.63), int(self.num_nodes*.67))  # at least two required vertices
        self.build_graph()
        self.output_graph()

    def equilikely(self, a: int, b: int) -> int:

        r = random.uniform(0.000001, 0.999999)
        return a + int((b - a + 1) * r)

    def build_graph(self) -> None:

        self.graph = nx.random_regular_graph(200,self.num_nodes)
        # Define a mapping from old node label to new node label
        mapping = {node: node+1 for node in self.graph.nodes()}

        # Use relabel_nodes to change the node numbers
        self.graph = nx.relabel_nodes(self.graph, mapping)
        self.required_vertices = random.sample(range(1, self.num_nodes + 1), self.num_required)




        for (i, j) in self.graph.edges():
            


            if i in self.required_vertices and j in self.required_vertices:
                if random.random() < 0.5:
                    weight = self.equilikely(25, 50)
                else:
                    weight = self.equilikely(15, 25)
            elif i in self.required_vertices or j in self.required_vertices:
                weight = self.equilikely(5, 20)
            else:
                weight = self.equilikely(1, 5)


            self.graph[i][j]['weight'] =  weight





    def output_graph(self, filename='./inputs/keg_graph_bias_6367_1_5V_15_50R.txt') -> None:

        with open(filename, 'w') as file:
            num_edges = self.graph.number_of_edges()
            file.write(f"{self.num_nodes} {num_edges} {self.num_required}\n") #First row of file reqs
            file.write(" ".join(map(str, self.required_vertices)) + '\n') #Second row of file reqs
            
                    # The corresponding sub graph edges and their weights
            edge_lines = [f"{edge[0]} {edge[1]} {edge[2]['weight']}" for edge in self.graph.edges(data=True)]
            file.write("\n".join(edge_lines))



