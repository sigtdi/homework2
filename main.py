import comp_net_analysis
import graph_operations
from computer_network_gr import computer_network
from UPA_gr import gen_UPA
from ER_gr import gen_ER
from alg_targeted_order import targeted_order
from alg_fast_targeted_order import fast_targeted_order
import matplotlib.pyplot as plt


# Звукова
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

    plt.rcParams['figure.figsize'] = (18.0, 9.0)
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    # В копии каждого графа удаляем вершины в случайном порядке и считаем размеры компонент связности
    for graph in graphs:
        result = comp_net_analysis.compute_resilience(graph_operations.copy_graph(graphs[graph]["type"]), comp_net_analysis.random_order(n))
        plt.subplot(2, 2, 1)
        plt.plot(result, label=graphs[graph]["name"])

    plt.title("Удаление случайных вершин")
    plt.xlabel('Количество удаленных вершин')
    plt.ylabel('Размер наибольшей КС')
    plt.legend()

    # В копии каждого графа удаляем вершины по количеству инцидентных им ребер и считаем размеры компонент связности
    for graph in graphs:
        result = comp_net_analysis.compute_resilience(graph_operations.copy_graph(graphs[graph]["type"]),
                                                      fast_targeted_order(graphs[graph]["type"]))
        plt.subplot(2, 2, 3)
        plt.plot(result, label=graphs[graph]["name"])

    plt.title("Удаление вершин по количеству инцидентных им ребер")
    plt.xlabel('Количество удаленных вершин')
    plt.ylabel('Размер наибольшей КС')
    plt.legend()

    # Проводим анализ функций fast_targeted_order и targeted_order на различных графах
    funcs = {
        "Fast targeted order": {"func": fast_targeted_order, "name": "Fast targeted order"},
        "Targeted order": {"func": targeted_order, "name": "Targeted order"}}

    for func in funcs:
        R = 1000
        step = 10
        trials = 10
        result = comp_net_analysis.emp_analysis(funcs[func]["func"], R, step, trials)
        plt.subplot(2, 2, 2)
        plt.plot(result, label=funcs[func]["name"])

    plt.title("Время работы алгоритмов")
    plt.xlabel('Количество вершин в графе /10')
    plt.ylabel('Секунды')
    plt.legend()

    plt.show()




