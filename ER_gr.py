import random


def gen_ER(n, p):
    graph = [set() for i in range(n)]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            a = random.random()
            if a < p:
                graph[i].add(j)
                graph[j].add(i)
    return graph
