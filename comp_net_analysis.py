from random import shuffle
import graph_operations
import time

from UPA_gr import gen_UPA


# Звукова
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


# Звукова
def random_order(n):
    res = [i for i in range(n)]
    shuffle(res)
    return res


# Звукова
def emp_analysis(func, R, step, trials):
    # Массив времени обработки графов по увеличению их размера
    res = []

    # Проводим измерения на графах разного размера
    for n in range(10, R, step):
        # Время выполнения серии измерений
        temp_time = 0

        # Несколько измерений на графе одного размера для усреднения результата
        for i in range(trials):
            graph = gen_UPA(n, 5)
            time_start = time.time()
            func(graph)
            # Добавляем к общему времени время выполнения текущего измерения
            temp_time += (time.time() - time_start)

        # Кладем в массив среднее значение времени
        res.append(temp_time / trials)

    return res
