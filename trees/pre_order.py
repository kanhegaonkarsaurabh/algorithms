def pre_order(node, visited=[]):
    if node is not None:
        visited.append(node)
        pre_order(node.left, visited)
        pre_order(node.right, visited)

def pre_order_iterative(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        if node.left is not None:
            stack.push(node.left)
        if node.right is not None:
            stack.push(node.right)
