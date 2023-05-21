'''
    Эффективная реализация удаления вершин с учетом структуры графа
    Удаление происходит в порядке убывания степеней вершин, находящихся в графе
'''

# импорт вспомогательных функций для работы с графом
from graph_operations import *


# Павлова
def fast_targeted_order(ugraph):
    '''
        :параметр ugraph: неориентированный граф
        :возвращает: упорядоченный список вершин order в порядке убывания их степеней

        Использует вспомогательные функции для работы с графом
    '''
    # создаем копию графа
    new_graph = copy_graph(ugraph)
    num_nodes = len(new_graph)
    # создаем список, содержащий информацию о степенях вершин, где  k-тый элемент содержит
    # множество узлов со степенью k
    degree_sets = [set([]) for _ in range(num_nodes)]
    for node in range(num_nodes):
        degree_node = len(new_graph[node])
        degree_sets[degree_node].add(node)
    # инициализируем пустой список для хранения удаляемых вершин
    order = []
    # перебираем все элементы degree_sets в порядке убывания степени k.
    for k in range(num_nodes - 1, -1, -1):
        # Далее поочередно удаляем все вершины из этого множества
        # и параллельно обновляем множества из degree_sets
        while degree_sets[k]:
            node = degree_sets[k].pop()
            for neighbor in new_graph[node]:
                d_neighbor = len(new_graph[neighbor])
                degree_sets[d_neighbor].remove(neighbor)
                degree_sets[d_neighbor - 1].add(neighbor)
            # добавляем найденную вершину в order и удаляем ее из графа
            order.append(node)
            delete_node(new_graph, node)

    return order

# testing
if __name__ == '__main__':
    from UPA_gr import gen_UPA
    g = gen_UPA(5, 2)
    print(fast_targeted_order(g), g)