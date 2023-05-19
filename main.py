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


