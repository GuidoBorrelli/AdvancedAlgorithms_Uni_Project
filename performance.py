import matplotlib.pyplot as plt
from statistics import mean, median, variance, stdev, StatisticsError
import numpy as np

DEBUG = False
DIGITS_ACCURACY = 8


# Given aggregated performance of an algorithm, return statistics measure
def extract_statistics(perf_list):
    avg = round(mean(perf_list), DIGITS_ACCURACY)
    try:
        var = round(variance(perf_list, avg), DIGITS_ACCURACY)
        std = round(stdev(perf_list), DIGITS_ACCURACY)
    except StatisticsError:
        var = 0
        std = 0
    return avg * 1000, var * 1000


# Receive in input global performance dict and graph type times desired
# Extract statistics of all algorithms on the given graph type
def get_values(performance_dict, graph_type):
    times_alg1 = performance_dict['Tarjan']
    times_alg2 = performance_dict['Nuutila']
    times_alg3 = performance_dict['Pearce']
    times_alg1 = times_alg1[graph_type]
    times_alg2 = times_alg2[graph_type]
    times_alg3 = times_alg3[graph_type]
    y, e = [], []
    e_0, e_1, e_2 = [], [], []
    y_0, y_1, y_2 = [], [], []
    x = np.array(times_alg1.index)
    # Fill performance of each algorithm
    for i in range(0, len(times_alg1.index)):
        avg_1, var_1 = extract_statistics(times_alg1.iloc[i])
        y_0.append(avg_1)
        e_0.append(var_1)
        avg_2, var_2 = extract_statistics(times_alg2.iloc[i])
        y_1.append(avg_2)
        e_1.append(var_2)
        avg_3, var_3 = extract_statistics(times_alg3.iloc[i])
        y_2.append(avg_3)
        e_2.append(var_3)
    # Merge in a single list of lists algorithms' performance
    y.append(np.array(y_0))
    e.append(np.array(e_0))
    y.append(np.array(y_1))
    e.append(np.array(e_1))
    y.append(np.array(y_2))
    e.append(np.array(e_2))
    return x, y, e


# Build graph of performance and variance of algorithms
def plot_graph(x, y, e, type):
    # One color per each algorithm
    colors = ['red', 'green', 'blue']
    for k in range(3):
        plt.figure(1)
        plt.plot(x, y[k], mfc=colors[k], linestyle=':', marker='o', color=colors[k])
        plt.figure(2)
        plt.plot(x, e[k], mfc=colors[k], linestyle='-.', marker='o', color=colors[k])
    plt.figure(1)
    plt.legend(['Tarjan', 'Nuutila', 'Pearce'], loc='upper left')
    plt.title("{} graph - Mean time".format(type))
    plt.xlabel('Number Of Nodes')
    plt.ylabel('Mean time value [millisecs]')
    plt.ylim(0)
    plt.figure(2)
    plt.legend(['Tarjan', 'Nuutila', 'Pearce'], loc='upper left')
    plt.title("{} graph - Variance".format(type))
    plt.xlabel('Number Of Nodes')
    plt.ylabel('Variance')
    plt.ylim(0)
    plt.figure(1)
    plt.savefig("./graphs/{}-results.png".format(type))
    plt.figure(2)
    plt.savefig("./graphs/{}-variance.png".format(type))
    plt.show()
    return


# This function shows graphically performance result of considered algorithm
# There is a comparison graph for each kind of graph: Sparse, Medium, Dense
def plot_result(performance_dict):
    # This function let get data in a format useful to plot
    x_sp, y_sp, e_sp = get_values(performance_dict, 'Sparse')
    x_md, y_md, e_md = get_values(performance_dict, 'Medium')
    x_de, y_de, e_de = get_values(performance_dict, 'Dense')
    # This function plot the data for each category
    plot_graph(x_sp, y_sp, e_sp, 'Sparse')
    plot_graph(x_md, y_md, e_md, 'Medium')
    plot_graph(x_de, y_de, e_de, 'Dense')
    return
