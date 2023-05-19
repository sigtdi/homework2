'''
    Эффективная реализация удаление вершин с учетом структуры графа
    Удаление происходит в порядке убывания степеней вершин, находящихся в графе
'''

# импорт вспомогательных функций для работы с графом
from graph_operations import *


def fast_targeted_order(ugraph):
    new_graph = copy_graph(ugraph)
    num_nodes = len(new_graph)
    degree_sets = [set([]) for _ in range(num_nodes)]
    for node in range(num_nodes):
        degree_node = len(new_graph[node])
        degree_sets[degree_node].add(node)

    order = []

    for k in range(num_nodes - 1, -1, -1):
        while degree_sets[k]:
            node = degree_sets[k].pop()
            for neighbor in new_graph[node]:
                d_neighbor = len(new_graph[neighbor])
                degree_sets[d_neighbor].remove(neighbor)
                degree_sets[d_neighbor - 1].add(neighbor)

            order.append(node)
            delete_node(new_graph, node)

    return order

# testing
if __name__ == '__main__':
    from UPA_gr import gen_UPA
    g = gen_UPA(5, 2)
    print(fast_targeted_order(g), g)