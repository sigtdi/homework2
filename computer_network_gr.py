# Звукова
def computer_network(n):
    # Создаем список пустых множеств нужного размера
    graph = [set() for i in range(n)]

    with open('alg_rf7.txt') as input_file:
        for line in input_file.readlines():
            # Проходим по всем строкам в файле, создаем из них списки смежности
            adj_lst = list(map(int, line.split()))
            if adj_lst:
                vertex1 = adj_lst.pop(0)
                # Добавляем список смежности в множество в нужной ячейке списка
                graph[vertex1].update(adj_lst)
                for vertex2 in adj_lst:
                    # Добавляем в списки смежности соседних вершин текущую вершину
                    graph[vertex2].add(vertex1)
            else:
                break

    return graph
