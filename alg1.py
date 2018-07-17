import stack as s

DEBUG = False


# Perform and evaluate Tarjan algorithm
def apply_alg(graph):
    DIM_NODES = len(graph)
    current_counter = 0
    stack = s.Stack()
    root = {}
    in_component = {}
    order = {}

    def visit(v):
        if DEBUG:
            print("Visiting: {}".format(v))
        nonlocal graph, current_counter, order, stack, root, in_component
        root[v] = v
        order[v] = current_counter
        current_counter = current_counter + 1
        stack.push(v)
        if DEBUG:
            print("\tOutgoing edge: {}".format(len(graph.out_edges(v))))
        for out_edge in graph.out_edges(v):
            w = out_edge[1]
            # If the value of node w in the dictionary is still DIM_NODES, not yet visited
            if order[w] == DIM_NODES:
                visit(w)
            if not in_component[w]:
                if order[root[v]] > order[root[w]]:
                    root[v] = root[w]

        if root[v] == v:
            while True:
                w = stack.pop()
                in_component[w] = True
                # Otherwise I don't have all references of all nodes updated to allow testing, - no side effects
                root[w] = v
                if v == w:
                    break
        return

    order = [DIM_NODES] * DIM_NODES
    in_component = [False] * DIM_NODES
    for node in graph.nodes:
        # If the value of node w in the dictionary is still DIM_NODES, not yet visited
        if order[node] == DIM_NODES:
            visit(node)
    return root
