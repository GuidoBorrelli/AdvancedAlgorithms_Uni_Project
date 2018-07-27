import networkx as nx
import os
import psutil
import alg1 as tarjan
import alg2 as nuutila
import alg3 as pearce

GRAPH = False
TEST_NODE_SIZE = 600
TEST_EDGE_PROBABILITY = 0.03
TEST_ALG = 1


# This function handle both graph creation and algorithm test
# Controller is given by global variable usage
# TEST_ALG is: 1(Pearce), 2(Nuutila), 3(Tarjan)
# GRAPH is: True(Generate and save in a file a graph), False(Function load the graph file and apply the algorithm)
# TEST_NODE_SIZE & TEST_EDGE_PROBABILITY: parameters for graph random creation


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
        if TEST_ALG == 3:
            _ = pearce.apply_alg(graph)
            memory_used = process.memory_info().rss
        elif TEST_ALG == 2:
            _ = nuutila.apply_alg(graph)
            memory_used = process.memory_info().rss
        elif TEST_ALG == 1:
            _ = tarjan.apply_alg(graph)
            memory_used = process.memory_info().rss
        else:
            return -1
        increment = memory_used - tara
        percentage_increment = increment * 100 / tara
        print("Memory used: {} - Tara: {}".format(memory_used, tara))
        print("Increment: {} - %: {}%".format(increment, percentage_increment))
    return
