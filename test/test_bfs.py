# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # Load the tiny network graph
    G_tiny = graph.Graph("./data/tiny_network.adjlist")
    # Traverse from Lani Wu
    lani_wu_traverse = G_tiny.bfs("Lani Wu", end=None)
    # Check all 30 nodes appear, beginning with Lani Wu then the
    # neighbours of that node
    assert len(lani_wu_traverse) == 30
    assert all(node in lani_wu_traverse[:5] for node in 
               ["Lani Wu", "32042149", "32036252", "31806696", "30727954"])
    # Check a traversal from nonexistent node "Toni Capra" fails
    with pytest.raises(KeyError):
        toni_capra_traverse = G_tiny.bfs("Toni Capra", end=None)
    
    # Create an empty graph. Verify BFS traverse fails (using a node not in it)
    G_empty = graph.Graph("./data/empty_network.adjlist")
    assert len(list(G_empty.graph.nodes)) == 0
    assert len(list(G_empty.graph.edges)) == 0
    with pytest.raises(KeyError):
        nonexistent_traverse = G_empty.bfs("Nonexistent Node", end=None)

    # Load a graph with two disconnected chains. Verify BFS from a node in
    # either chain traverses that whole chain in order, but does not reach the
    # other chain
    G_chains = graph.Graph("./data/chain_network.adjlist")
    assert G_chains.bfs("1", end=None) == ["1", "2", "3", "4", "5"]
    assert G_chains.bfs("a", end=None) == ["a", "b", "c", "d", "e"]
    # Check that starting halfway through the chain does not backtrack
    assert G_chains.bfs("2", end=None) == ["2", "3", "4", "5"]
    assert G_chains.bfs("d", end=None) == ["d", "e"]

    # Load a cyclical graph. Verify BFS terminates and returns all nodes.
    G_cycle = graph.Graph("./data/cycle_network.adjlist")
    cycle_traverse = G_cycle.bfs("1", end=None)
    assert cycle_traverse == ["1", "2", "3", "4", "5", "6"]

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # Load the citation network graph
    G_citation = graph.Graph("./data/citation_network.adjlist")
    # Traverse from one node to another, verify the shortest path is found
    G_Tony_Joe = G_citation.bfs("Tony Capra", end="Joseph DeRisi")
    assert G_Tony_Joe in list(nx.all_shortest_paths(G_citation.graph, source="Tony Capra", target="Joseph DeRisi"))
    # Repeat with another pair
    G_Martin_Jill = G_citation.bfs("Martin Kampmann", end="Jill Hollenbach")
    assert G_Martin_Jill in list(nx.all_shortest_paths(G_citation.graph, source="Martin Kampmann", target="Jill Hollenbach"))

    # Load the empty graph and verify BFS search fails (using non-existent nodes)
    G_empty = graph.Graph("./data/empty_network.adjlist")
    assert len(list(G_empty.graph.nodes)) == 0
    assert len(list(G_empty.graph.edges)) == 0
    with pytest.raises(KeyError):
        nonexistent_traverse = G_empty.bfs("Nonexistent Node",
                                           end="Nonexistent Node 2")
        
    # Load a graph with two disconnected chains. Verify BFS from a node in
    # either chain searches that chain, but does not reach the other chain
    G_chains = graph.Graph("./data/chain_network.adjlist")
    assert G_chains.bfs("1", end="4") == ["1", "2", "3", "4"]
    assert G_chains.bfs("c", end="e") == ["c", "d", "e"]
    assert G_chains.bfs("2", end="b") is None
    assert G_chains.bfs("a", end="4") is None
    # Verify running BFS from and to a node not in the graph fails
    with pytest.raises(KeyError):
        G_chains_Tony = G_chains.bfs("Tony Capra", end="1")
    assert G_chains.bfs("b", end="Tony Capra") is None

    # Load a cyclical graph, verify BFS terminates
    G_cycle = graph.Graph("./data/cycle_network.adjlist")
    search_1_3 = G_cycle.bfs("1", end="3")
    assert search_1_3 == ["1", "2", "3"]
    # Verify BFS search terminates correctly if the end node is the start node
    search_1_1 = G_cycle.bfs("1", end="1")
    assert search_1_1 == ["1"]
