# algo_bowl 

### Code by: Jacob Sagal, Saniya Minase, Sean Feeney

## Problem Description
The task is to develop an algorithm that, given a weighted, undirected, connected graph \(G = (V, E)\), and a subset \(R\) of required vertices, determines a tree with minimal cost that connects all of the vertices in \(R\).

## Input Format
The input comprises:
- A line with three integers: \(n\)(number of vertices), \(m\)(number of edges), and \(r\)(number of required vertices in \(R\)).
- A line listing the \(r\) required vertices, represented by integers in the range \([1, n]\).
- \(m\) lines, each representing an edge of the graph and its weight. 


### Restrictions
- The graph will have at most 1,000 vertices and 100,000 edges.
- Edge weights are integers in \([1, 50]\).
- \(2 ≤ |R| ≤ |V|\).

## Output Format
The output will contain:
- The total cost of the resulting tree.
- The number of edges \(e\) in the tree.
- The next \(e\) lines will each contain two vertex IDs corresponding to an edge of the tree.

# Our Solution