import queue
import time

def createNode(value, depth):
    return TreeNode(value, depth)

class TreeNode:
    def __init__(self, value, depth=0):
        self.data = value
        self.depth = depth
        self.left = None
        self.right = None


def freeTree(node):
    if node is None:
        return
    freeTree(node.left)
    freeTree(node.right)
    del node


def printTree(root, space=0):
    if root is None:
        return
    printTree(root.right, space + 4)
    print()
    for i in range(space):
        print("---- ", end="")
    print(root.data)
    printTree(root.left, space + 4)


def insert(root, value):
    if root is None:
        return createNode(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root


def countNodesAtEachLevel(root):
    if root is None:
        return []

    result = []
    q = queue.Queue()
    q.put(root)

    while not q.empty():
        level_size = q.qsize()
        result.append(level_size)

        for _ in range(level_size):
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    return result


def createTreeFromArray(values, depth):
    if not values:
        return None

    if len(values) == 1:
        return createNode(values[0][0], values[0][1])

    mid_val = len(values) // 2
    if values[mid_val][1] < depth:
        return None

    node = createNode(values[mid_val][0], values[mid_val][1])

    node.left = createTreeFromArray(values[:mid_val], depth + 1)
    node.right = createTreeFromArray(values[mid_val + 1:], depth + 1)

    return node


def writeTreeToFile(root, filename):
    with open(filename, 'w') as file:
        writeTreeToFileHelper(root, file, 0)


def writeTreeToFileHelper(node, file, depth):
    if node is None:
        return
    writeTreeToFileHelper(node.right, file, depth + 1)
    file.write(f"{node.data} {depth}\n")
    writeTreeToFileHelper(node.left, file, depth + 1)


# Example usage:
#values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#root = createTreeFromArray(values)
with open("input_tree.txt", 'r') as file:
    values = [(int(line.split()[0]), int(line.split()[1])) for line in file.readlines()]

root = createTreeFromArray(values, 0)

time_start = time.time()
levels_count = countNodesAtEachLevel(root)
time_end = time.time()

print("Number of nodes on each level of the tree:")
for level, count in enumerate(levels_count):
    print(f"Level {level}: {count} nodes")


print(time_end - time_start)
