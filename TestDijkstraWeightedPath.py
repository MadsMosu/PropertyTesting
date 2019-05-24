import networkx as nx
from hypothesis import given
from hypothesis import strategies as st
import networkx as nx
from hypothesis_networkx import graph_builder
import sys
from Dijkstra import Graph

def test_dijkstra_path1():
    graph = nx.DiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    path = nx.dijkstra_path(graph, 'a', 'e')

    assert nx.dijkstra_path_length(graph, 'a', 'e') == 1

    #Dijkstra implementation should equal shortest path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == path

def test_dijkstra_path2():
    graph = nx.Graph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    path = nx.dijkstra_path(graph, 'a', 'e')

    assert nx.dijkstra_path_length(graph, 'a', 'e') == 1

    #Dijkstra implementation should equal shortest path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == path

def test_dijkstra_path3():
    graph = nx.MultiDiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    path = nx.dijkstra_path(graph, 'a', 'e')

    assert nx.dijkstra_path_length(graph, 'a', 'e') == 1

    #Dijkstra implementation should equal shortest path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == path

def test_dijkstra_path4():
    graph = nx.MultiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    path = nx.dijkstra_path(graph, 'a', 'e')

    assert nx.dijkstra_path_length(graph, 'a', 'e') == 1

    #Dijkstra implementation should equal shortest path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == path