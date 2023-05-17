
def computer_network():
    graph = []
    with open('alg_rf7.txt') as input_file:
        while True:
            adj_lst = [int(i) for i in input_file.readline().split()]
            if adj_lst:
                adj_lst.pop(0)
                graph.append(set(adj_lst))
            else:
                break
    return graph


if __name__ == '__main__':
    comp_network_graph = computer_network()

