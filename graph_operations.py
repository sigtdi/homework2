'''
    Вспомогательные функции для работы с неориентированным графом:

    copy_graph - создает копию графа
    delete_node - удаляет вершину из графа
'''

def copy_graph(graph):
    '''
        :параметр graph: неориентированный граф
        :возвращает: копию неориентированного графа
    '''

    # инициализируем новый граф и копируем в него информацию о ребрах из старого
    new_graph = []
    num_nodes = len(graph)
    for node in range(num_nodes):
        new_graph.append(set(graph[node]))
    return new_graph


def delete_node(ugraph, node):
    '''
        :параметр ugraph: неориентированный граф
        :параметр node: удаляемая вершина неориентированного графа
        :возвращает: ничего не возвращает
    '''

    # удаляем вершину из графа, сохранив список ее соседей;
    # у каждого соседа node удаляем из списка смежности выкинутую вершину
    neighbors = ugraph[node]
    ugraph[node] = None
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)

# testing
if __name__ == '__main__':
    pass