import stack as s

DEBUG = False


# Perform and evaluate PEA_FIND_SSC2 algorithm
def apply_alg(graph):
    stack = s.Stack()
    index = 1
    c = graph.number_of_nodes() - 1
    rindex = {}

    def visit(v):
        nonlocal graph, stack, index, c, rindex
        if DEBUG:
            print("Visiting: {}".format(v))
        root = True
        rindex[v] = index
        index = index + 1
        if DEBUG:
            print("\tOutgoing edge: {}".format(len(graph.out_edges(v))))
        for out_edge in graph.out_edges(v):
            w = out_edge[1]
            if rindex[w] == 0:
                visit(w)
            if rindex[w] < rindex[v]:
                rindex[v] = rindex[w]
                root = False
        if root:
            index = index - 1
            while (not stack.isEmpty()) and rindex[v] <= rindex[stack.peek()]:
                w = stack.pop()
                rindex[w] = c
                index = index - 1
            rindex[v] = c
            c = c - 1
        else:
            stack.push(v)
        return

    for node in graph.nodes:
        rindex[node] = 0
    for node in graph.nodes:
        if rindex[node] == 0:
            visit(node)
    return [rindex[e] for e in rindex]
