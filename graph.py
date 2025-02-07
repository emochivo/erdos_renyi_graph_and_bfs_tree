'''
CECS 427 Project 1 
Date: February 7, 2025
Written by: Chi Vo
'''

import argparse
import matplotlib.pyplot as plt
import networkx as nx
import math


''' FUNCTIONS '''

def input_graph(inputFile):
    G = nx.read_adjlist(inputFile)
    return G

def create_random_graph(n, c):
    p = c*math.log(n)/n
    G = nx.erdos_renyi_graph(n, p)

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True, font_size=9, node_size=260, font_color='#ffffff')
    plt.show()

    return G


def BFS(G, startNode):
    
    newG = nx.Graph()
    shortest_paths_data = dict(nx.single_source_all_shortest_paths(G, startNode))
    paths = list(shortest_paths_data.values())

    path_list = []

    for i in paths:
        for j in range(len(i)):
            if len(i[j]) > 1:
                path_list.append(i[j])

    for j in path_list:
        nx.add_path(newG, j)

    
    pos = nx.bfs_layout(newG, startNode)

    nx.draw_networkx(newG, pos=pos, with_labels=True, font_size=9, node_size=255, font_color='#ffffff', arrows=False)
    plt.savefig("bfsTree.png")
    plt.show()

    return newG



def plot(G, newG=None):
    pos = nx.spring_layout(G)

    nx.draw_networkx(G, pos=pos, with_labels=True, font_size=9, node_size=255, font_color='#ffffff')
    if newG != None:
        nx.draw_networkx_edges(newG, pos=pos, edgelist=newG.edges, width=1.4,  edge_color='#ff0000')

    plt.show()

    


def output_graph(G, outputFile):
    nx.write_adjlist(G, outputFile)




''' MAIN CODE '''

parser = argparse.ArgumentParser(prog='graph')

# create commands
parser.add_argument('--input', type=str)
parser.add_argument('--create_random_graph', nargs=2, metavar=('--nodes','--constant'), type=lambda x: int(x) if "." not in x else float(x))
parser.add_argument('--BFS', type=str)
parser.add_argument('--plot', action='store_true')
parser.add_argument('--output', type=str)


# parse arguments
args = parser.parse_args()

hasBFS = False

# access values from the arguments
if args.input:
    inputFile = args.input
    G = input_graph(inputFile)


if args.create_random_graph:
    n, c = args.create_random_graph
    G = create_random_graph(n, c)

if args.BFS:
    startNode = args.BFS
    newG = BFS(G, startNode)
    hasBFS = True

if args.plot:
    if hasBFS:
        plot(G, newG)
    else:
        plot(G)

if args.output:
    outputFile = args.output
    output_graph(G, outputFile)

