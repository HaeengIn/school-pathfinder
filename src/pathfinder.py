import networkx
from graph import create_graph

graph = create_graph()


def find_path(start: str, goal: str):
    # Return opimized path between start and goal
    return networkx.astar_path(graph, start, goal, weight="weight")
