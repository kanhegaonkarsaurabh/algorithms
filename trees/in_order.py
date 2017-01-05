def in_order(node, visited=[]):
    if node is not None:
        in_order(node.left, visited)
        visited.append(node)
        in_order(node.right, visited)
    return visited

def in_order_iterative(root):
    node, stack = root, []
    visited = []
    while stack or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            visited.append(node)
            node = node.right
    return visited
