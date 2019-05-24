import networkx as nx
from hypothesis import given
from hypothesis import strategies as st
import networkx as nx
from hypothesis_networkx import graph_builder
import sys
from Dijkstra import Graph



def test_shortest_path_dijkstra():
    graph = nx.Graph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    #follows a -> c -> e

    path = nx.shortest_path(graph, 'a', 'e')
    assert nx.shortest_path_length(graph, 'a', 'e') == len(path)-1
    assert nx.has_path(graph, 'a', 'e') == True
    allPaths = nx.all_shortest_paths(graph, 'a', 'e')
    assert path in allPaths

    
    graph2 = nx.Graph()
    e2=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3),('a','e',0.4)]
    graph2.add_weighted_edges_from(e2)
    #follows a -> e
    
    path2 = nx.shortest_path(graph2, 'a', 'e')
    assert nx.shortest_path_length(graph2, 'a', 'e') == len(path2)-1
    assert nx.has_path(graph2, 'a', 'e') == True
    allPaths2 = nx.all_shortest_paths(graph2, 'a', 'e')
    assert path2 in allPaths2


    #graph1 shortest path should be diffrent from graph2 shortest path
    assert nx.shortest_path_length(graph, 'a', 'e') != nx.shortest_path_length(graph2, 'a', 'e')
    #graph1 paths should not contain graph2 shortest path
    assert nx.shortest_path(graph2, 'a', 'e') not in nx.all_shortest_paths(graph, 'a', 'e')
    #When removed edge, they should equal again
    graph2.remove_edge('a','e')
    assert nx.shortest_path_length(graph, 'a', 'e') == nx.shortest_path_length(graph2, 'a', 'e')
    assert nx.shortest_path(graph2, 'a', 'e') in nx.all_shortest_paths(graph, 'a', 'e')


    #Outputs the same path as dijkstra_path
    assert nx.shortest_path(graph, 'a', 'e') == nx.dijkstra_path(graph, 'a', 'e')

    #Path should equal Dijkstra implementation path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == nx.shortest_path(graph, 'a', 'e')
    assert nx.dijkstra_path(graph, 'a', 'e') == nx.shortest_path(graph, 'a', 'e')
    


def test_shortest_path_dijkstra2():
    graph = nx.MultiGraph()
    e=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3)]
    graph.add_weighted_edges_from(e)
    #follows a -> c -> e

    path = nx.shortest_path(graph, 'a', 'e')
    assert nx.shortest_path_length(graph, 'a', 'e') == len(path)-1
    assert nx.has_path(graph, 'a', 'e') == True
    allPaths = nx.all_shortest_paths(graph, 'a', 'e')
    assert path in allPaths

    
    graph2 = nx.MultiGraph()
    e2=[('a','b',0.3),('b','c',0.9),('a','c',0.5),('c','d',1.2),('c','e',1.6),('b','e',0.7),('d','e',1.3),('a','e',0.4)]
    graph2.add_weighted_edges_from(e2)
    #follows a -> e
    
    path2 = nx.shortest_path(graph2, 'a', 'e')
    assert nx.shortest_path_length(graph2, 'a', 'e') == len(path2)-1
    assert nx.has_path(graph2, 'a', 'e') == True
    allPaths2 = nx.all_shortest_paths(graph2, 'a', 'e')
    assert path2 in allPaths2


    #graph1 shortest path should be diffrent from graph2 shortest path
    assert nx.shortest_path_length(graph, 'a', 'e') != nx.shortest_path_length(graph2, 'a', 'e')
    #graph1 paths should not contain graph2 shortest path
    assert nx.shortest_path(graph2, 'a', 'e') not in nx.all_shortest_paths(graph, 'a', 'e')
    #When removed edge, they should equal again
    graph2.remove_edge('a','e')
    assert nx.shortest_path_length(graph, 'a', 'e') == nx.shortest_path_length(graph2, 'a', 'e')
    assert nx.shortest_path(graph2, 'a', 'e') in nx.all_shortest_paths(graph, 'a', 'e')

    #Outputs the same path as dijkstra_path
    assert nx.shortest_path(graph, 'a', 'e') == nx.dijkstra_path(graph, 'a', 'e')

    #Path should equal Dijkstra implementation path
    dijkstraImpl = Graph(e)
    assert dijkstraImpl.dijkstra('a', 'e') == nx.shortest_path(graph, 'a', 'e')
    assert nx.dijkstra_path(graph, 'a', 'e') == nx.shortest_path(graph, 'a', 'e')
    


    


    



