
def computer_network():
    graph = [set()] * 1347
    with open('alg_rf7.txt') as input_file:
        for line in input_file.readlines():
            adj_lst = list(map(int, line.split()))
            if adj_lst:
                vertex1 = adj_lst.pop(0)
                graph[vertex1] = set(adj_lst)
                for vertex2 in adj_lst:
                    graph[vertex2].add(vertex1)
            else:
                break
    return graph


def compute_resilience(graph, vertices):
    for vertex in vertices:
        graph[vertex] = set()



if __name__ == '__main__':
    comp_network_graph = computer_network()

