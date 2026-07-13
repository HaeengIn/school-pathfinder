import networkx
from graph import create_graph

graph = create_graph()


def heuristic(current: str, goal: str) -> int:
    current_floor = graph.nodes[current]["floor"]
    goal_floor = graph.nodes[goal]["floor"]

    return abs(current_floor - goal_floor)


def find_path(start: str, goal: str):
    path = networkx.astar_path(graph, start, goal, heuristic=heuristic, weight="weight")
    cost = networkx.path_weight(graph, path, weight="weight")

    return path, cost
