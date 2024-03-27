import time
import random

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def create_random_array(size, range_min, range_max):
    # Shuffle indices first
    indices = list(range(range_min, range_max + 1))
    random.shuffle(indices)

    # Create an array with the shuffled indices
    return indices[:size]

def generate_perfect_binary_tree_from_array(arr):
    def build_tree(arr):
        if not arr:
            return None
        mid = len(arr) // 2
        node = TreeNode(arr[mid])
        node.left = build_tree(arr[:mid])
        node.right = build_tree(arr[mid + 1:])
        return node

    return build_tree(arr)

def generate_perfect_binary_tree(num_nodes):
    if num_nodes <= 0:
        return None

    num_internal_nodes = num_nodes - 1  # Subtracting 1 for the root node
    depth = 0

    # Determine the depth iteratively
    while True:
        if 2**depth > num_internal_nodes:
            break
        depth += 1

    arr = create_random_array(2**depth - 1, 0, num_nodes)
    return generate_perfect_binary_tree_from_array(arr)

num_nodes = int(input())
time_start = time.time()
root = generate_perfect_binary_tree(num_nodes)

# Output tree for verification
def print_tree(root, depth):
    nodes = [(root, 0)]
    while nodes:
        node, level = nodes.pop()
        if node:
            print("    " * level + "|---" + str(node.data))
            nodes.append((node.right, level + 1))
            nodes.append((node.left, level + 1))

with open('input_1_000_000.txt', 'w') as file:
    #print_tree(root, int(2 * num_nodes - 2))

    for level in range(int(2 * num_nodes - 2)):
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