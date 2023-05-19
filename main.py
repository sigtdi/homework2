import comp_net_analysis
from computer_network_gr import computer_network
from UPA_gr import gen_UPA
from ER_gr import gen_ER
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = 1347
    m, p = 2, 0.003

    # Создаем три типа графов
    comp_network_graph = computer_network(n)
    upa_graph = gen_UPA(n, m)
    er_graph = gen_ER(n, p)

    graphs = {
        "Тестовая модель компьютерной сети": {"type": comp_network_graph, "name": "Тестовая модель компьютерной сети"},
        "UPA-граф": {"type": upa_graph, "name": "UPA-граф"},
        "ER-граф": {"type": er_graph, "name": "ER-граф"}}

    plt.rcParams['figure.figsize'] = (8.0, 4.0)
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    # В копии каждого графа удаляем вершины в случайном порядке и считаем размеры компонент связности
    for graph in graphs:
        result = comp_net_analysis.compute_resilience(comp_net_analysis.copy_graph(graphs[graph]["type"]), comp_net_analysis.random_order(n))
        plt.plot(result, label=graphs[graph]["name"])

    plt.title("Случайный порядок вершин")
    plt.ylabel('Размер наибольшей КС')
    plt.legend()
    plt.show()




