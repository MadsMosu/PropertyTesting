from hypothesis import given
from hypothesis import strategies as st
from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule, precondition
import networkx as nx
from collections import defaultdict
from hypothesis_networkx import graph_builder

node_data = st.fixed_dictionaries({'name': st.text(), 'number': st.integers()})
edge_data = st.fixed_dictionaries({'weight': st.floats(allow_nan=False, allow_infinity=False)})

builder = graph_builder(graph_type=nx.Graph,
                        node_keys=st.integers(),
                        node_data=node_data,
                        edge_data=edge_data,
                        min_nodes=2, max_nodes=30,
                        min_edges=1, max_edges=None,
                        self_loops=False,
                        connected=True)

class GraphModel(RuleBasedStateMachine):
    def __init__(self):
        super(GraphModel, self).__init__()
        self.graph = nx.Graph()
        self.model = defaultdict(set)



    nodes = Bundle('nodes')
    values = Bundle('values')

    @rule(x=nodes)
    def addNode(self, x):
        self.graph.add_node(x)
    
    @precondition(lambda self: self.graph.size > 1)
    @rule(u=nodes, v=nodes, x=st.integers())
    def addEdge(self, u, v, x):
        self.graph.add_edge(u, v, weight=x)

    @precondition(lambda self: self.graph.size > 0)
    @rule(x=nodes)
    def removeNode(self, x):
        self.graph.remove_node(x)


    @rule(u=nodes, v=nodes)
    def removeEdge(self, u, v):
        self.graph.remove_edge(u, v)
    
    @precondition(lambda self: self.graph.size > 1)
    @rule(y=nodes, x=st.integers())
    def addPath(self, y, x):
        self.graph.add_path(y, weight=x)
    


testGraphModel = GraphModel.TestCase