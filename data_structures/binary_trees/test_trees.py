import unittest

from data_structures.binary_trees.trees import Tree, isValidBSTRange, isValidBSTValue, maxTreeValue, minTreeValue, \
    mirror, equals, isSubTree, isHeightBalanced, inOrderTraverse, isMirror, preOrderTraverse, postOrderTraverse, \
    insertInPlace, insertAndCopy, contains, deleteInPlace, clone, sortedArrayToBST, maxDepth, elementsInLevel, \
    elementsLevelOrder, pathToElement, lowestCommonAncestor, left_view, rite_view, inOrderTraverseStack, \
    elementsLevelOrderGrouped


def binary_search_tree():
    tree = Tree(100)
    tree.left = Tree(50)
    tree.left.left = Tree(25)
    tree.left.rite = Tree(75)
    tree.rite = Tree(150)
    tree.rite.left = Tree(125)
    tree.rite.rite = Tree(175)
    return tree


def subtree():
    tree = Tree(50, Tree(25), Tree(75))
    return tree


def height_imbalanced_tree():
    tree = Tree(100)
    tree.left = Tree(50)
    tree.left.left = Tree(25)
    tree.left.rite = Tree(75)
    return tree


def full_skewed_tree():
    tree = Tree(10)
    tree.rite = Tree(20)
    tree.rite.rite = Tree(30)
    tree.rite.rite.rite = Tree(40)
    tree.rite.rite.rite.rite = Tree(50)
    tree.rite.rite.rite.rite.rite = Tree(60)
    return tree


def binary_search_tree_mirrored():
    tree = Tree(100)
    tree.rite = Tree(50)
    tree.rite.rite = Tree(25)
    tree.rite.left = Tree(75)
    tree.left = Tree(150)
    tree.left.rite = Tree(125)
    tree.left.left = Tree(175)
    return tree


def invalid_binary_search_tree():
    tree = Tree(100)
    tree.left = Tree(10)
    tree.left.left = Tree(25)
    tree.left.rite = Tree(75)
    tree.rite = Tree(200)
    tree.rite.left = Tree(125)
    tree.rite.rite = Tree(175)
    return tree


class Test(unittest.TestCase):
    def test_isValidBSTRange(self):
        self.assertTrue(isValidBSTRange(binary_search_tree()))
        self.assertFalse(isValidBSTRange(invalid_binary_search_tree()))

    def test_isValidBSTValue(self):
        self.assertTrue(isValidBSTValue(binary_search_tree()))
        self.assertFalse(isValidBSTValue(invalid_binary_search_tree()))

    def test_maxTreeValue(self):
        self.assertEqual(maxTreeValue(binary_search_tree()), 175)
        self.assertEqual(maxTreeValue(invalid_binary_search_tree()), 200)

    def test_minTreeValue(self):
        self.assertEqual(minTreeValue(binary_search_tree()), 25)
        self.assertEqual(minTreeValue(invalid_binary_search_tree()), 10)

    def test_equals(self):
        self.assertTrue(equals(binary_search_tree(), binary_search_tree()))
        self.assertFalse(equals(binary_search_tree(), invalid_binary_search_tree()))

    def test_mirror(self):
        tree = mirror(binary_search_tree())
        self.assertIsNotNone(tree)
        self.assertTrue(equals(tree, binary_search_tree_mirrored()))

    def test_isMirror(self):
        self.assertTrue(isMirror(binary_search_tree(), binary_search_tree_mirrored()))
        self.assertFalse(isMirror(binary_search_tree(), invalid_binary_search_tree()))

    def test_isSubTree(self):
        self.assertTrue(isSubTree(binary_search_tree(), subtree()))

    def test_isHeightBalanced(self):
        height, balanced = isHeightBalanced(binary_search_tree())
        self.assertTrue(balanced)
        self.assertEqual(height, 3)
        height, balanced = isHeightBalanced(height_imbalanced_tree())
        self.assertFalse(balanced)
        self.assertEqual(height, 3)

    def test_inOrderTraverse(self):
        self.assertEqual(inOrderTraverse(binary_search_tree()), [25, 50, 75, 100, 125, 150, 175])

    def test_inOrderTraverseStack(self):
        self.assertEqual(inOrderTraverseStack(binary_search_tree()), [25, 50, 75, 100, 125, 150, 175])

    def test_preOrderTraverse(self):
        self.assertEqual(preOrderTraverse(binary_search_tree()), [100, 50, 25, 75, 150, 125, 175])

    def test_postOrderTraverse(self):
        self.assertEqual(postOrderTraverse(binary_search_tree()), [25, 75, 50, 125, 175, 150, 100])

    def test_insert(self):
        tree = binary_search_tree()
        insertInPlace(tree, 45)
        insertInPlace(tree, 46)
        insertInPlace(tree, 47)
        self.assertEqual(tree.left.left.rite.data, 45)
        self.assertEqual(tree.left.left.rite.rite.data, 46)
        self.assertEqual(tree.left.left.rite.rite.rite.data, 47)

    def test_contains(self):
        self.assertTrue(contains(binary_search_tree(), 25))
        self.assertFalse(contains(binary_search_tree(), 37))

    def test_insertAndCopy(self):
        tree = binary_search_tree()
        othr = insertAndCopy(tree, 45)
        self.assertFalse(equals(tree, othr))
        self.assertTrue(contains(othr, 45))

    def test_deleteInPlace(self):
        tree = deleteInPlace(binary_search_tree(), 50)
        self.assertFalse(contains(tree, 50))
        tree = deleteInPlace(binary_search_tree(), 51)
        self.assertTrue(equals(tree, binary_search_tree()))

    def test_clone(self):
        tree = binary_search_tree()
        othr = clone(tree)
        self.assertTrue(equals(tree, othr))
        self.assertFalse(id(tree) == id(othr))

    def test_sortedArrayToBST(self):
        tree = sortedArrayToBST([25, 50, 75, 100, 125, 150, 175])
        self.assertTrue(equals(tree, binary_search_tree()))

    def test_maxDepth(self):
        self.assertEqual(maxDepth(None), 0)
        self.assertEqual(maxDepth(full_skewed_tree()), 6)

    def test_elementsInLevel(self):
        tree = binary_search_tree()
        self.assertEqual(elementsInLevel(tree, 0), [])
        self.assertEqual(elementsInLevel(tree, 1), [100])
        self.assertEqual(elementsInLevel(tree, 2), [50, 150])
        self.assertEqual(elementsInLevel(tree, 3), [25, 75, 125, 175])
        self.assertEqual(elementsInLevel(tree, 4), [])

    def test_elementsLevelOrder(self):
        tree = binary_search_tree()
        self.assertEqual(elementsLevelOrder(tree), [100, 50, 150, 25, 75, 125, 175])

    def test_elementsLevelOrderGrouped(self):
        tree = binary_search_tree()
        self.assertEqual(elementsLevelOrderGrouped(tree), [[100], [50, 150], [25, 75, 125, 175]])

    def test_pathToElement(self):
        tree = binary_search_tree()
        self.assertEqual(pathToElement(tree, 100), [100])
        self.assertEqual(pathToElement(tree, 50), [100, 50])
        self.assertEqual(pathToElement(tree, 25), [100, 50, 25])
        self.assertEqual(pathToElement(tree, 75), [100, 50, 75])
        self.assertEqual(pathToElement(tree, 175), [100, 150, 175])
        self.assertEqual(pathToElement(tree, 300), [])

    def test_lowestCommonAncestor(self):
        tree = binary_search_tree()
        self.assertIsNone(lowestCommonAncestor(tree, 1, 100))
        self.assertEqual(lowestCommonAncestor(tree, 100, 100), 100)
        self.assertEqual(lowestCommonAncestor(tree, 75, 25), 50)
        self.assertEqual(lowestCommonAncestor(tree, 50, 175), 100)
        self.assertEqual(lowestCommonAncestor(tree, 50, 25), 50)

    def test_left_view(self):
        self.assertEqual(left_view(binary_search_tree()), [100, 50, 25])
        self.assertEqual(left_view(full_skewed_tree()), [10, 20, 30, 40, 50, 60])

    def test_rite_view(self):
        self.assertEqual(rite_view(binary_search_tree()), [100, 150, 125])
        self.assertEqual(rite_view(full_skewed_tree()), [10, 20, 30, 40, 50, 60])


if __name__ == '__main__':
    unittest.main()
