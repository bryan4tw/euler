# Maximum Path Sum I

# I'm not sure if dijkstra or similar will work here
import networkx as nx


triangle = [0 for _ in range(15)]

# fmt: off
triangle[0]  = [75]
triangle[1]  = [95, 64]
triangle[2]  = [17, 47, 82]
triangle[3]  = [18, 35, 87, 10]
triangle[4]  = [20, 4, 82, 47, 65]
triangle[5]  = [19, 1, 23, 75, 3, 34]
triangle[6]  = [88, 2, 77, 73, 7, 63, 67]
triangle[7]  = [99, 65, 4, 28, 6, 16, 70, 92]
triangle[8]  = [41, 41, 26, 56, 83, 40, 80, 70, 33]
triangle[9]  = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
triangle[10] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
triangle[11] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
triangle[12] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
triangle[13] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
triangle[14] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
# fmt:on

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
end_nodes = [f"14.{i}" for i in range(len(triangle[14]))]


def find_shortest_path(graph, start, ends):
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

    return shortest_path, min_weight


def recalculate_path(shortest_path, triangle):
    weight = 0
    for i in range(len(shortest_path)):
        row, col = shortest_path[i].split(".")
        print(
            f"Processing node {shortest_path[i]} with weight {triangle[int(row)][int(col)]}"
        )
        weight += triangle[int(row)][int(col)]

    return weight


shortest_path = find_shortest_path(graph, start_node, end_nodes)
print(f"Shortest path: {shortest_path[0]} with weight {shortest_path[1]}")

print(f"Recalculated path weight: {recalculate_path(shortest_path[0], triangle)}")
