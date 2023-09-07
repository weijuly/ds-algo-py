import sys

prev = None


class Tree:
    def __init__(self, data, left=None, rite=None):
        self.data, self.left, self.rite = data, left, rite

    def __repr__(self):
        return '%s <= %d => %s' % (
            str(self.left.data) if self.left else '#', self.data, str(self.rite.data) if self.rite else '#')


def isValidBSTRange(tree, minval=-sys.maxsize, maxval=sys.maxsize):
    if not tree:
        return True
    if tree.data < minval or tree.data > maxval:
        return False
    return isValidBSTRange(tree.left, minval, tree.data - 1) and isValidBSTRange(tree.rite, tree.data + 1, maxval)


def isValidBSTValue(tree):
    global prev
    if not tree:
        return True
    if not isValidBSTValue(tree.left):
        return False
    if prev and tree.data < prev.data:
        return False
    prev = tree
    return isValidBSTValue(tree.rite)


def maxTreeValue(tree):
    if not tree:
        return -sys.maxsize
    return max([tree.data, maxTreeValue(tree.left), maxTreeValue(tree.rite)])


def minTreeValue(tree):
    if not tree:
        return sys.maxsize
    return min([tree.data, minTreeValue(tree.left), minTreeValue(tree.rite)])


def mirror(tree):
    if not tree:
        return None
    return Tree(tree.data, mirror(tree.rite), mirror(tree.left))


def isMirror(a, b):
    if not a and not b:
        return True
    if True in [a and not b, b and not a, a.data != b.data]:
        return False
    return isMirror(a.left, b.rite) and isMirror(a.rite, b.left)


def equals(a, b):
    if not a and not b:
        return True
    if True in [a and not b, b and not a]:
        return False
    if a.data != b.data:
        return False
    return equals(a.left, b.left) and equals(a.rite, b.rite)


def isSubTree(tree, subtree):
    if not tree and not subtree:
        return True
    if True in [tree and not subtree, subtree and not tree]:
        return False
    if subtree.data > tree.data:
        return isSubTree(tree.rite, subtree)
    if subtree.data < tree.data:
        return isSubTree(tree.left, subtree)
    return equals(tree, subtree)


def isHeightBalanced(tree):
    if not tree:
        return 0, True
    lheight, lbal = isHeightBalanced(tree.left)
    if not lbal:
        return lheight, False
    rheight, rbal = isHeightBalanced(tree.rite)
    if not rbal:
        return rheight, False
    if abs(lheight - rheight) > 1:
        return max([lheight, rheight]) + 1, False
    return max([lheight, rheight]) + 1, True


def inOrderTraverse(tree, array=[]):
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.data)
        inOrderTraverse(tree.rite, array)
    return array


def inOrderTraverseStack(tree):
    if not tree:
        return []
    stack, array, curr = [], [], tree
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            array.append(curr.data)
            curr = curr.rite
        if not stack and not curr:
            break
    return array


def preOrderTraverse(tree, array=[]):
    if tree:
        array.append(tree.data)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.rite, array)
    return array


def postOrderTraverse(tree, array=[]):
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.rite, array)
        array.append(tree.data)
    return array


def insertInPlace(tree, data):
    if not tree:
        return Tree(data)
    if tree.data == data:
        return tree
    if data < tree.data:
        tree.left = insertInPlace(tree.left, data)
    else:
        tree.rite = insertInPlace(tree.rite, data)
    return tree


def insertAndCopy(tree, data):
    if not tree:
        return Tree(data)
    if data == tree.data:
        return Tree(data, tree.left, tree.rite)
    if data < tree.data:
        return Tree(tree.data, insertAndCopy(tree.left, data), tree.rite)
    return Tree(tree.data, tree.left, insertAndCopy(tree.rite, data))


def contains(tree, data):
    if not tree:
        return False
    if tree.data == data:
        return True
    if data < tree.data:
        return contains(tree.left, data)
    return contains(tree.rite, data)


def deleteInPlace(tree, data):
    if not tree:
        return None
    if data < tree.data:
        tree.left = deleteInPlace(tree.left, data)
    if data > tree.data:
        tree.rite = deleteInPlace(tree.rite, data)
    if data == tree.data:
        if not tree.left:
            temp = tree.rite
            tree = None
            return temp
        if not tree.rite:
            temp = tree.left
            tree = None
            return temp
        if tree.left and tree.rite:
            data = minTreeValue(tree.rite)
            tree.data = data
            tree.rite = deleteInPlace(tree.rite, data)
    return tree


def clone(tree):
    if not tree:
        return None
    return Tree(tree.data, clone(tree.left), clone(tree.rite))


def sortedArrayToBST(array):
    if not array:
        return None
    mid = int(len(array) / 2)
    return Tree(array[mid], sortedArrayToBST(array[:mid]), sortedArrayToBST(array[mid + 1:]))


def maxDepth(tree):
    if not tree:
        return 0
    return 1 + max([maxDepth(tree.left), maxDepth(tree.rite)])


def elementsInLevel(tree, level):
    if not tree or level < 1:
        return []
    if level == 1:
        return [tree.data]
    else:
        return elementsInLevel(tree.left, level - 1) + elementsInLevel(tree.rite, level - 1)


def elementsLevelOrder(tree):
    if not tree:
        return []
    queue = []
    queue.append(tree)
    elems = []
    while len(queue) > 0:
        node = queue.pop(0)
        elems.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.rite:
            queue.append(node.rite)
    return elems

def elementsLevelOrderGrouped(tree):
    def inner(tree, level, group):
        if not tree:
            return group
        if level not in group:
            group[level] = []
        group[level].append(tree.data)
        inner(tree.left, level + 1, group)
        inner(tree.rite, level + 1, group)
        return group
    group = inner(tree, 0, {})
    return [group[k] for k in sorted(group.keys())]



def pathToElement(tree, data):
    if not tree:
        return []
    if tree.data == data:
        return [data]
    if tree.left:
        path = pathToElement(tree.left, data)
        if path and path[-1] == data:
            return [tree.data] + path
    if tree.rite:
        path = pathToElement(tree.rite, data)
        if path and path[-1] == data:
            return [tree.data] + path
    return []


def lowestCommonAncestor(tree, x, y):
    xpath = pathToElement(tree, x)
    ypath = pathToElement(tree, y)
    ancestor = None
    while xpath and ypath:
        if xpath[0] == ypath[0]:
            ancestor = xpath[0]
            xpath.pop(0)
            ypath.pop(0)
        else:
            break
    return ancestor


def left_view(tree, level=0, elements=None):
    if elements is None:
        elements = []
    if not tree:
        return elements
    if len(elements) == level:
        elements.append(tree.data)
    left_view(tree.left, level + 1, elements)
    left_view(tree.rite, level + 1, elements)
    return elements


def rite_view(tree, level=0, elements=None):
    if elements is None:
        elements = []
    if not tree:
        return elements
    if len(elements) == level:
        elements.append(tree.data)
    rite_view(tree.rite, level + 1, elements)
    rite_view(tree.left, level + 1, elements)
    return elements
