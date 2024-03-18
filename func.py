from collections import deque
import time

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def createNode(value):
    return TreeNode(value)

def generatePerfectBinaryTree(depth):
    if depth <= 0:
        return None

    root = createNode(1)
    q = [root]  # Use a list instead of deque for faster operations

    level = 1
    while q and level < depth:
        node_count = len(q)

        for _ in range(node_count):
            node = q.pop(0)  # Pop from the beginning for faster removal

            node.left = createNode(node.data << 1)  # Use bitwise shift for faster calculations
            q.append(node.left)

            if level < depth - 1:
                node.right = createNode((node.data << 1) + 1)
                q.append(node.right)

        level += 1

    return root

depth = int(input())
time_start = time.time()
root = generatePerfectBinaryTree(depth)

# Output tree for verification
def print_tree(root):
    nodes = [(root, 0)]
    while nodes:
        node, level = nodes.pop()
        if node:
            print("    " * level + "|---" + str(node.data))
            nodes.append((node.right, level + 1))
            nodes.append((node.left, level + 1))

with open('input_tree.txt', 'w') as file:
    for level in range(depth):
        nodes_at_level = [(root, 0)]
        while nodes_at_level:
            node, current_level = nodes_at_level.pop()
            if current_level == level and node:
                file.write(f"{node.data} {level}\n")
            if node:
                nodes_at_level.append((node.right, current_level + 1))
                nodes_at_level.append((node.left, current_level + 1))

time_end = time.time()
print(time_end - time_start)