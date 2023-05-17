
def computer_network():
    graph = [set()] * 1347
    with open('alg_rf7.txt') as input_file:
        for line in input_file.readlines():
            adj_lst = list(map(int, line.split()))
            if adj_lst:
                vertex1 = adj_lst.pop(0)
                graph[vertex1].update(adj_lst)
                for vertex2 in adj_lst:
                    graph[vertex2].add(vertex1)
            else:
                break
    return graph


def compute_resilience(graph, vertices):
    connect_comp = []
    n = len(graph)
    for vertex in vertices:
        graph[vertex] = set()
        for adj_lst in graph:
            if vertex in adj_lst:
                adj_lst.remove(vertex)
        visited = [False] * n
        answer = 0
        for i in range(n):
            temp_size = 0
            if visited[i]:
                continue
            visited[i] = True
            queue = [i]
            temp_size += 1
            while queue:
                v = queue.pop()
                for to in graph[v]:
                    if not visited[to]:
                        temp_size += 1
                        visited[to] = True
                        answer = max(answer, temp_size)
                        queue.append(to)
        connect_comp.append(answer)
    return connect_comp



if __name__ == '__main__':
    comp_network_graph = computer_network()

