def tree_by_levels(root):
    tree_list = []
    queue = [root] if root else []

    while len(queue):
        tree_list.append(queue[0].value)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return tree_list
