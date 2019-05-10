import networkx as nx
from hypothesis import given
from hypothesis import strategies as st
import networkx as nx
from hypothesis_networkx import graph_builder
from model import GraphModel
import sys


def test_astar_grid():
    graph = nx.grid_graph(dim=[5,5])
    assert nx.astar_path_length(graph,(0,0),(4,4)) == len(nx.astar_path(graph, (0,0),(4,4)))-1

def test_astar_graph():
    graph = nx.Graph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3)]
    graph.add_weighted_edges_from(e)
    assert nx.astar_path_length(graph,'a','e') == 1

    graph2 = nx.Graph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3),('a','e', 0.5)]
    graph2.add_weighted_edges_from(e)

    assert nx.astar_path_length(graph,'a','e') > nx.astar_path_length(graph2,'a','e')

def test_astar_Digraph():
    graph = nx.DiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3)]
    graph.add_weighted_edges_from(e)
    assert nx.astar_path_length(graph,'a','e') == 1

    graph2 = nx.DiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3),('a','e', 0.5)]
    graph2.add_weighted_edges_from(e)

    assert nx.astar_path_length(graph,'a','e') > nx.astar_path_length(graph2,'a','e')

# def test_astar_MultiDigraph():
#     graph = nx.MultiDiGraph()
#     e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3)]
#     graph.add_weighted_edges_from(e)
#     assert nx.astar_path_length(graph,'a','e') == 1

# def test_astar_MultiGraph():
#     graph = nx.MultiGraph()
#     e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e', 1.3)]
#     graph.add_weighted_edges_from(e)
#     assert nx.astar_path_length(graph,'a','e') == 1
