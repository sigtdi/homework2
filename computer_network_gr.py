def computer_network(n):
    graph = [set() for i in range(n)] #Создаем список пустых множеств нужного размера
    with open('alg_rf7.txt') as input_file:
        for line in input_file.readlines():
            adj_lst = list(map(int, line.split())) #Проходим по всем строкам в файле, создаем из них списки смежности
            if adj_lst:
                vertex1 = adj_lst.pop(0)
                graph[vertex1].update(adj_lst) #Добаляем список смежности в множество в нужной ячейке списка
                for vertex2 in adj_lst:
                    graph[vertex2].add(vertex1) #Добавляем в списки смежности соседних вершин текущую вершину
            else:
                break
    return graph
