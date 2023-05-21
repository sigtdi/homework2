import random


# Звукова
def gen_ER(n, p):
    # Граф в виде списка списков смежности, представленных в виде множеств
    graph = [set() for i in range(n)]

    # Проходим по всем возможным парам вершин
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # Вычисляем случайное значение от 0 до 1
            a = random.random()
            # Если значение меньше заданной вероятности, добавляем ребра (i, j) и (j, i) в граф
            if a < p:
                graph[i].add(j)
                graph[j].add(i)

    return graph
