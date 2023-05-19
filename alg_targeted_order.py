################
# в разработке #
################
from graph_operations import *

def delete_node(ugraph, node):
    neighbors = ugraph[node]
    ugraph[node] = None
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


def targeted_order(ugraph):
    new_graph = copy_graph(ugraph)

    order = []
    num_nodes = len(new_graph)
    num_nodes_order = 0
    while num_nodes != num_nodes_order:
        max_degree = -1
        for node in range(num_nodes):
            if new_graph[node] is not None and len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)
        num_nodes_order += 1

    return order

# testing
if __name__ == '__main__':
    from UPA_gr import gen_UPA
    g = gen_UPA(5, 2)
    print(targeted_order(g), g)