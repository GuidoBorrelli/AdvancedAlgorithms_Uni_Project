import stack as s

DEBUG = False


# Perform and evaluate Nuutila algorithm 2
def apply_alg(graph):
    DIM_NODES = len(graph)
    current_counter = 0
    stack = s.Stack()
    stack.push(-1)
    root = {}
    in_component = {}
    order = {}

    def visit(v):
        if DEBUG:
            print("Visiting: {}".format(n))
        nonlocal current_counter, order, stack, root, graph, in_component
        root[v] = v
        order[v] = current_counter
        current_counter = current_counter + 1
        in_component[v] = False
        for out_edge in graph.out_edges(v):
            w = out_edge[1]
            if order[w] == DIM_NODES:
                visit(w)
            if not in_component[root[w]]:
                if order[root[v]] > order[root[w]]:
                    root[v] = root[w]
        if root[v] == v:
            if stack.peek() > -1 and order[stack.peek()] >= order[v]:
                while stack.peek() > -1 and order[stack.peek()] >= order[v]:
                    w = stack.pop()
                    in_component[w] = True
                    root[w] = v
            else:
                in_component[v] = True
        elif not stack.contains(root[v]):
            stack.push(root[v])
        return

    in_component = [False] * DIM_NODES
    order = [DIM_NODES] * DIM_NODES
    for node in graph.nodes:
        # If the value of node w in the dictionary is still DIM_NODES, not yet visited
        if order[node] == DIM_NODES:
            visit(node)

    # Due to let me test the results, I need to store all component reference of all nodes like in the other alg
    def update(i):
        nonlocal root
        if root[i] != root[root[i]]:
            update(root[i])
            root[i] = root[root[i]]

    for i in root:
        update(i)
    return root
