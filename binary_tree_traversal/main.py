# Pre-order traversal
def pre_order(node, order=None):
    order = order or []
    if node:
        order.append(node.data)
        order = pre_order(node.left, order)
        order = pre_order(node.right, order)

    return order


# In-order traversal
def in_order(node, order=None):
    order = order or []
    if node:
        order = in_order(node.left, order)
        order.append(node.data)
        order = in_order(node.right, order)

    return order


# Post-order traversal
def post_order(node, order=None):
    order = order or []
    if node:
        order = post_order(node.left, order)
        order = post_order(node.right, order)
        order.append(node.data)

    return order
