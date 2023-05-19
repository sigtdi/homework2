from alg_upa_trial import UPATrial

def gen_UPA(n, m):
    '''
    :параметр n: общее количество вершин в создаваемом графе
    :параметр m: (m<n) количество вершин, к которым подсоединяется каждая вновь созданная вершина
    :возвращает: случайный граф

    Использует класс для инкапсуляции оптимизированных испытаний UPATrial
    '''

    # инициализируем граф и создаем полносвязный граф на m вершинах
    upaG = [set([]) for _ in range(n)]
    nodes_of_g_complete = set(range(m))
    for i in range(m):
        upaG[i] = nodes_of_g_complete.difference({i})

    # создаем объект класса UPATrial для проведения случайных испытаний;
    # для каждой добавляемой вершины проводим испытания и соединем ее с новыми соседями,
    # полученными в результате испытаний
    upatrial = UPATrial(m)
    for v in range(m, n):
        new_node_neighbors = upatrial.run_trial(m)
        for u in new_node_neighbors:
            upaG[v].add(u)
            upaG[u].add(v)

    return upaG

# testing
if __name__ == '__main__':
    n, m = map(int, input().split())
    G = gen_UPA(n, m)
    print(G)