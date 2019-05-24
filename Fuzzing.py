import networkx as nx
from hypothesis import given
from hypothesis import strategies as st
import networkx as nx
from hypothesis_networkx import graph_builder
import sys
from Dijkstra import Graph
import random
from hypothesis import find, settings, Verbosity

node_data = st.fixed_dictionaries({'number': st.text()})
edge_data = st.fixed_dictionaries({'weight': st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       min_value=1)})

builder = graph_builder(graph_type=nx.MultiDiGraph,
                        node_keys=st.integers(),
                        node_data=node_data,
                        edge_data=edge_data,
                        min_nodes=10, max_nodes=10,
                        min_edges=10, max_edges=None,
                        self_loops=False,
                        connected=True)

node_data2 = st.fixed_dictionaries({'number': st.text()})
edge_data2 = st.fixed_dictionaries({'weight': st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       min_value=1)})

builder2 = graph_builder(graph_type=nx.DiGraph,
                        node_keys=st.integers(),
                        node_data=node_data,
                        edge_data=edge_data,
                        min_nodes=10, max_nodes=10,
                        min_edges=10, max_edges=None,
                        self_loops=False,
                        connected=True)

node_data3 = st.fixed_dictionaries({'number': st.text()})
edge_data3 = st.fixed_dictionaries({'weight': st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       min_value=1)})

builder3 = graph_builder(graph_type=nx.Graph,
                        node_keys=st.integers(),
                        node_data=node_data,
                        edge_data=edge_data,
                        min_nodes=10, max_nodes=10,
                        min_edges=10, max_edges=None,
                        self_loops=False,
                        connected=True)

node_data4 = st.fixed_dictionaries({'number': st.text()})
edge_data4 = st.fixed_dictionaries({'weight': st.floats(allow_nan=False,
                                                       allow_infinity=False,
                                                       min_value=1)})

builder4 = graph_builder(graph_type=nx.MultiGraph,
                        node_keys=st.integers(),
                        node_data=node_data,
                        edge_data=edge_data,
                        min_nodes=10, max_nodes=10,
                        min_edges=10, max_edges=None,
                        self_loops=False,
                        connected=True)


@given(graph=builder)
def test_dijkstra_MultiDiGraph(graph):
    source = random.choice(list(graph.nodes))
    target = random.choice(list(graph.nodes))
    while(target == source):
        target = random.choice(graph.nodes)

    dijkstraImpl = Graph(graph.edges)
    # print('source: ' + str(source) + ', target: ' + str(target))
    # print(graph.edges())

    if (nx.has_path(graph, source, target) or len(dijkstraImpl.dijkstra(source, target)) > 0):
        assert nx.dijkstra_path(graph, source, target) == dijkstraImpl.dijkstra(source, target)

@given(graph=builder2)
def test_dijkstra_DiGraph(graph):
    source = random.choice(list(graph.nodes))
    target = random.choice(list(graph.nodes))
    while(target == source):
        target = random.choice(graph.nodes)

    dijkstraImpl = Graph(graph.edges)
    # print('source: ' + str(source) + ', target: ' + str(target))
    # print(graph.edges())

    if (nx.has_path(graph, source, target) or len(dijkstraImpl.dijkstra(source, target)) > 0):
        assert nx.dijkstra_path(graph, source, target) == dijkstraImpl.dijkstra(source, target)

@given(graph=builder3)
def test_dijkstra_Graph(graph):
    source = random.choice(list(graph.nodes))
    target = random.choice(list(graph.nodes))
    while(target == source):
        target = random.choice(graph.nodes)

    dijkstraImpl = Graph(graph.edges, both_ends=True)
    print('source: ' + str(source) + ', target: ' + str(target))
    print(graph.edges())

    if (nx.has_path(graph, source, target) or len(dijkstraImpl.dijkstra(source, target)) > 0):
        assert nx.dijkstra_path(graph, source, target) == dijkstraImpl.dijkstra(source, target)

@given(graph=builder4)
def test_dijkstra_MultiGraph(graph):
    source = random.choice(list(graph.nodes))
    target = random.choice(list(graph.nodes))
    while(target == source):
        target = random.choice(graph.nodes)

    dijkstraImpl = Graph(graph.edges, both_ends=True)
    # print('source: ' + str(source) + ', target: ' + str(target))
    # print(graph.edges())

    if (nx.has_path(graph, source, target) or len(dijkstraImpl.dijkstra(source, target)) > 0):
        assert nx.dijkstra_path(graph, source, target) == dijkstraImpl.dijkstra(source, target)

