import networkx
from src.loader import load_json


def create_graph():
    graph = networkx.Graph()
    nodes = load_json("nodes.json")
    edges = load_json("edges.json")

    # Add nodes
    for name, info in nodes.items():
        graph.add_node(name, floor=info["floor"])

    # Add edges
    for start, end, weight in edges:
        graph.add_edge(start, end, weight=weight)

    return graph
