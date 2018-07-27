import networkx as nx
import os
import psutil
import alg1 as tarjan
import alg2 as nuutila
import alg3 as pearce

GRAPH = False
TEST_NODE_SIZE = 600
TEST_EDGE_PROBABILITY = 600**(-1/10)
TEST_ALG = 3


def memory_test():
    if GRAPH:
        graph = nx.gnp_random_graph(TEST_NODE_SIZE, TEST_EDGE_PROBABILITY, seed=None, directed=True)
        # Save graph
        nx.write_gpickle(graph, "./graph-memory-test")
        print("Graph saved")
    else:
        process = psutil.Process(os.getpid())
        # Read graph
        graph = nx.read_gpickle("./graph-memory-test")
        print(nx.density(graph))
        tara = process.memory_info().rss
        if TEST_ALG == 1:
            _ = pearce.apply_alg(graph)
            memory_used = process.memory_info().rss
        elif TEST_ALG == 2:
            _ = nuutila.apply_alg(graph)
            memory_used = process.memory_info().rss
        elif TEST_ALG == 3:
            _ = tarjan.apply_alg(graph)
            memory_used = process.memory_info().rss
        increment = memory_used - tara
        percentage_increment = increment * 100 / tara
        print("Memory used: {} - Tara: {}".format(memory_used, tara))
        print("Increment: {} - %: {}%".format(increment, percentage_increment))
    return
