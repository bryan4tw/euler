# Maximum Path Sum II

# I'm not sure if dijkstra or similar will work here
import networkx as nx
import timeit

triangle = [0 for _ in range(100)]

# Import the 0067.txt triangle data
# split each line by spaces and convert to list of integers
with open("input/0067.txt", "r") as f:
    for i, line in enumerate(f):
        triangle[i] = list(map(int, line.split()))

# loop over the triangle, and add add two edges for the rows below
# 0.0 has edges 1.0 and 1.1
# 1.0 has edges 2.0 and 2.1, 1.1 has edges 2.1 and 2.2
# the logic is same index, and index


def generate_graph(triangle):
    graph = nx.DiGraph()
    for row in range(len(triangle) - 1):
        for col in range(len(triangle[row])):
            graph.add_edge(
                f"{row}.{col}",
                f"{row+1}.{col}",
                # There's probably a way to calculate the slowest path, but this '200 - sum' flips the path
                weight=(200 - (triangle[row][col] + triangle[row + 1][col])),
            )
            graph.add_edge(
                f"{row}.{col}",
                f"{row+1}.{col+1}",
                weight=(200 - (triangle[row][col] + triangle[row + 1][col + 1])),
            )

    return graph


graph = generate_graph(triangle)

start_node = "0.0"
end_nodes = [f"{len(triangle) - 1}.{i}" for i in range(len(triangle[-1]))]


def find_shortest_path_dijkstra(graph, start, ends):
    shortest_path = None
    min_weight = float("inf")
    for end in ends:
        try:
            path = nx.dijkstra_path(graph, start, end)
            weight = nx.path_weight(graph, path, "weight")
            if weight < min_weight:
                min_weight = weight
                shortest_path = path
        except nx.NetworkXNoPath:
            continue

    return shortest_path


def find_shortest_path_bellman_ford(graph, start, ends):
    shortest_path = None
    min_weight = float("inf")
    for end in ends:
        try:
            path = nx.bellman_ford_path(graph, start, end)
            weight = nx.path_weight(graph, path, "weight")
            if weight < min_weight:
                min_weight = weight
                shortest_path = path
        except nx.NetworkXNoPath:
            continue

    return shortest_path


def find_shortest_path_a(graph, start, ends):
    shortest_path = None
    min_weight = float("inf")
    for end in ends:
        try:
            path = nx.astar_path(graph, start, end)
            weight = nx.path_weight(graph, path, "weight")
            if weight < min_weight:
                min_weight = weight
                shortest_path = path
        except nx.NetworkXNoPath:
            continue

    return shortest_path


def recalculate_path(shortest_path, triangle):
    weight = 0
    for i in range(len(shortest_path)):
        row, col = shortest_path[i].split(".")

        weight += triangle[int(row)][int(col)]

    return weight


shortest_path_dijkstra = find_shortest_path_dijkstra(graph, start_node, end_nodes)


# print(f"Recalculated path weight: {recalculate_path(shortest_path, triangle)}")

# execution_time_dijkstra = timeit.timeit(
#     lambda: find_shortest_path_dijkstra(graph, start_node, end_nodes), number=10
# )
# print(f"Execution time (Dijkstra): {execution_time_dijkstra}")

# execution_time_bellman_ford = timeit.timeit(
#     lambda: find_shortest_path_bellman_ford(graph, start_node, end_nodes), number=10
# )
# print(f"Execution time (Bellman-Ford): {execution_time_bellman_ford}")

# execution_time_a_star = timeit.timeit(
#     lambda: find_shortest_path_a(graph, start_node, end_nodes), number=10
# )
# print(f"Execution time (A*): {execution_time_a_star}")
