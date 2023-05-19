from random import shuffle

def compute_resilience(graph, vertices):
    connect_comp = [] #Список размеров наибольших компонент связности
    n = len(graph)
    del_vertices = [] #Список уже удаленных вершин
    for vertex in vertices:
        del_vertices.append(vertex)
        graph[vertex] = set() #Удаляем ребра из текущей удаляемой вершины
        for adj_lst in graph:
            if vertex in adj_lst:
                adj_lst.remove(vertex)  #Удаяем спискам смежности других вершин удаляемую вершину
        visited = [False] * n #Список, в котором храним информацию о посещенных вершинах
        answer = 0 #Размер наибольшей компоненты связности
        for i in range(n):
            temp_size = 0 #В этой переменной сохраняем размер текущей компоненты связности
            if visited[i] or i in del_vertices: #Если вершина уже посещена, мы посчитали эту компоненту
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
                        queue.append(to) #Добавляем в очередь соседние вершины
            answer = max(answer, temp_size)
        connect_comp.append(answer) #Добавляем размер текущей наибольшей компоненты связности
    return connect_comp


def random_order(n): #Возвращает список вершин в случайном порядке
    res = [i for i in range(n)]
    shuffle(res)
    return res


def copy_graph(graph):
    pass
