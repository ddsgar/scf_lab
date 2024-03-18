import queue
import time

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def createNode(value):
    return TreeNode(value)


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


def createTreeFromFile(filename):
    root = None
    nodesStack = []
    with open(filename, 'r') as file:
        for line in file:
            value, depth = map(int, line.strip().split())
            node = createNode(value)
            while nodesStack and nodesStack[-1][1] >= depth:
                nodesStack.pop()
            if not nodesStack:
                root = node
            else:
                parent = nodesStack[-1][0]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            nodesStack.append((node, depth))
    return root


def writeTreeToFile(root, filename):
    with open(filename, 'w') as file:
        writeTreeToFileHelper(root, file, 0)


def writeTreeToFileHelper(node, file, depth):
    if node is None:
        return
    writeTreeToFileHelper(node.right, file, depth + 1)
    file.write(f"{node.data} {depth}\n")
    writeTreeToFileHelper(node.left, file, depth + 1)


# Пример использования:
#root = createTreeFromFile("example.txt")
root = createTreeFromFile("input_tree.txt")

time_start = time.time()
levels_count = countNodesAtEachLevel(root)

print("Количество вершин на каждом уровне дерева:")
for level, count in enumerate(levels_count):
    print(f"Уровень {level}: {count} вершин")
time_end = time.time()
print(time_end - time_start)
writeTreeToFile(root, "output_tree.txt")