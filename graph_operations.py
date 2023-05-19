def copy_graph(graph):
    new_graph = []
    num_nodes = len(graph)
    for node in range(num_nodes):
        new_graph.append(set(graph[node]))
    return new_graph


def delete_node(ugraph, node):
    neighbors = ugraph[node]
    ugraph[node] = None
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

# testing
if __name__ == '__main__':
    pass