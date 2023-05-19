import com_net_analysis
from computer_network_gr import computer_network
from UPA_gr import gen_UPA
from ER_gr import gen_ER
import matplotlib.pyplot as plt
import time




if __name__ == '__main__':
    n = 1347
    """
    m и p Подобрать
    """
    m, p = 0, 0
    comp_network_graph = computer_network(n)
    upa_graph = gen_UPA(n, m)
    er_graph = gen_ER(n, p)
    graphs = {
        "Тестовая модель компьютерной сети": { "type": comp_network_graph, "name": "Тестовая модель компьютерной сети"},
        "UPA-граф": { "type": upa_graph, "name": "UPA-граф"},
        "ER-граф": { "type": er_graph, "name": "ER-граф"}}

    plt.rcParams['figure.figsize'] = (8.0, 4.0)
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    for graph in graphs:
        result = com_net_analysis.compute_resilience(graph["type"], com_net_analysis.random_order(n))
        plt.plot(result, label=graph["name"])
    plt.title(sort_types[plot][1])
    plt.ylabel('сек')
    plt.legend()
    plt.show()

    plt.rcParams['figure.figsize'] = _old_value



