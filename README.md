# CECS 427 PROJECT 1: ERDOS-RENYI RANDOM GRAPH G(N,P). BREADTH FIRST SEARCH.
#### Written by: Chi Vo
#### Date: February 7, 2025

This is a class project from CECS 427 at California State University Long Beach, instructed by Dr. Oscar Morales Ponce.  

### Objective
Implement Erdos-Renyi random graph in Python with NetworkX and Matplotlib libraries. 
Must be able to read graphs from files, write graphs into files, compute all shortest paths from a specific node using breadth-first search (BFS) and visualize it.


### How to run the code? 
There are 5 possible parameters that can be used for commands:

1) `--input [filename]`:
Input a .gml file into the code. E.g. "graph_file.gml" 

2) `--create_random_graph [--nodes] [--constant]`:
This parameter creates a graph using the Erdos-Renyi random graph algorithm, which needs the number of nodes and a probability p. While the node quantity is provided by the [--nodes] parameter, the probability p can be obtained using the function: p = (c ln(n))/n, where c is the [--constant] parameter and n is the number of nodes. The output should be a graph with the same node quantity, with its edge generation depending on [--constant] from the user.

3) `--BFS [source]`:
This parameter creates a BFS graph tree from a provided NetworkX graph (input graph). User should specify a source node which is a non-negative integer, and the code will generate a BFS graph containing all shortest paths from the source node to all other nodes (e.g., --BFS 2). The BFS tree will then be saved as a .png image, just for my convenience when I want to compare the highlighted graph with the BFS tree. 

4) `--plot`:
This parameter does not need any inputs, and is used to plot a NetworkX graph. If the user types --BFS before --plot, the --plot parameter will generate the graph highlighting all shortest paths in red. 

5) `--output [filename]`:
Create an output .gml file and save it at user's current directory. 



To run the code, type your commands in the terminal. The sample commands that users can use:

`python ./graph.py --create_random_graph 100 1.1 --output out_graph_file.gml`:
This command generates an Erdős-Rényi graph with 100 nodes and an edge probability of (1.1 ln 100) / 100, storing the graph in out_graph_file.gml

`python ./graph.py --input graph_file.gml --BFS 1 --plot`:
This command reads the graph stored in graph_file.gml and plots the BFS graph from node 1.



