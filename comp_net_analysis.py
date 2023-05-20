from random import shuffle
import graph_operations
import time

from UPA_gr import gen_UPA


def compute_resilience(graph, vertices):
    # Список размеров наибольших компонент связности
    connect_comp = []
    n = len(graph)
    # Список уже удаленных вершин
    del_vertices = []

    for vertex in vertices:
        del_vertices.append(vertex)
        neighbors = graph[vertex]

        # Удаляем вершину
        graph_operations.delete_node(graph, vertex)

        # Список, в котором храним информацию о посещенных вершинах
        visited = [False] * n
        # Размер наибольшей компоненты связности
        answer = 0

        for i in range(n):
            # Сохраняем размер текущей компоненты связности
            temp_size = 0

            # Если вершина уже посещена, мы посчитали эту компоненту
            if visited[i] or i in del_vertices:
                continue

            # Нашли не посещенную вершину - новая компонента связности
            visited[i] = True
            # Очередь обработки вершин в этой компоненте
            queue = [i]
            temp_size += 1

            while queue:
                v = queue.pop()
                # Помечаем всех соседей вершины из очереди
                for to in graph[v]:
                    if not visited[to]:
                        # За каждую помеченную вершину добавляем размер компоненты
                        temp_size += 1
                        visited[to] = True
                        # Добавляем в очередь соседние вершины
                        queue.append(to)

            answer = max(answer, temp_size)

        # Добавляем размер текущей наибольшей компоненты связности
        connect_comp.append(answer)

    return connect_comp


def random_order(n):
    res = [i for i in range(n)]
    shuffle(res)
    return res


def emp_analysis(func, R, step):
    res = []
    for n in range(10, R, step):
        graph = gen_UPA(n, 5)
        time_start = time.time()
        func(graph)
        time_stop = time.time()
        res.append((time_stop - time_start))
    return res
