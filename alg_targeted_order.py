'''
    Не очень эффективная реализация удалениея вершин с учетом структуры графа
    Удаление происходит в порядке убывания степеней вершин, находящихся в графе
'''

# импорт вспомогательных функций для работы с графом
from graph_operations import *

# Павлова
def targeted_order(ugraph):
    '''
        :параметр ugraph: неориентированный граф
        :возвращает: упорядоченный список вершин order в порядке убывания их степеней

        Использует вспомогательные функции для работы с графом
    '''
    # создаем копию графа
    new_graph = copy_graph(ugraph)

    # инициализируем пустой список для хранения удаляемых вершин
    order = []
    num_nodes = len(new_graph)
    num_nodes_order = 0
    # пока в графе есть вершины, удаляем их
    while num_nodes != num_nodes_order:
        # Находит узел с максимальной степенью.
        # Если таковых несколько, то выбирает любой.
        max_degree = -1
        for node in range(num_nodes):
            if new_graph[node] is not None and len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        # Удаляет узел с максимальной степенью и все инцидентные ребра из графа.
        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)
        num_nodes_order += 1

    return order

# testing
if __name__ == '__main__':
    from UPA_gr import gen_UPA
    g = gen_UPA(5, 2)
    print(targeted_order(g), g)