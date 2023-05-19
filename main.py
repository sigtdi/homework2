
def computer_network():
    graph = [set() for i in range(1347)] #Создаем список пустых множеств нужного размера
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


def compute_resilience(graph, vertices):
    connect_comp = [] #Список размеров наибольших компонент связности
    n = len(graph)
    for vertex in vertices:
        graph[vertex] = set() #Удаляем ребра из текущей удаляемой вершины
        for adj_lst in graph:
            if vertex in adj_lst:
                adj_lst.remove(vertex)  #Удаяем спискам смежности других вершин удаляемую вершину
        visited = [False] * n #Список, в котором храним информацию о посещенных вершинах
        answer = 0 #Размер наибольшей компоненты связности
        for i in range(n):
            temp_size = 0 #В этой переменной сохраняем размер текущей компоненты связности
            if visited[i]: #Если вершина уже посещена, мы посчитали эту компоненту
                continue
            visited[i] = True #Нашли непосещенную вершину - новая компонента связности
            queue = [i] #Очередь обработки вершин в этой компоненте
            temp_size += 1
            while queue:
                v = queue.pop()
                for to in graph[v]: #Помечаем всех соседей вершины из очереди
                    if not visited[to]:
                        temp_size += 1 #За каждую помеченную вершину добавляем размер компоненты
                        visited[to] = True
                        answer = max(answer, temp_size)
                        queue.append(to) #Добавляем в очередь соседние вершины
        connect_comp.append(answer) #Добавляем размер текущей наибольшей компоненты связности
    return connect_comp



if __name__ == '__main__':
    comp_network_graph = computer_network()

