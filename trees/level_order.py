def level_order(root):
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return visited
