class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_max_value(root):
    while root.right is not None:
        root = root.right
    return root.key


def find_min_value(root):
    while root.left is not None:
        root = root.left
    return root.key


def tree_sum(root):
    if root is None:
        return 0
    return root.key + tree_sum(root.left) + tree_sum(root.right)


# Приклад створення дерева
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(33)
root.right.left = Node(10)
root.right.right = Node(5)

# Знаходження найбільшого значення
max_value = find_max_value(root)
print(f"Найбільше значення в дереві: {max_value}")

# Знаходження найменшого значення
min_value = find_min_value(root)
print(f"Найменше значення в дереві: {min_value}")

# Знаходження суми всіх значень
tree_sum_value = tree_sum(root)
print(f"Сума всіх значень в дереві: {tree_sum_value}")
