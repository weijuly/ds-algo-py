# Binary Trees

## Binary Search Trees
Read about them [here](https://en.wikipedia.org/wiki/Binary_search_tree)

### Common operations

#### Check if a BT is a valid BST
There are two approaches:

1. For each node, check its value is between a range: `isValidBSTRange()`
2. For each node, check if its value is greater than the node to its left: `isValidBSTValue()` 

Both are *O(n)* time complexity

#### Get the max and min value of a tree
Just iterate through the tree recursively while computing a minimum and maximum 
at each point: `maxTreeValue()` `minTreeValue()`. These run at *O(n)* time complexity

#### Mirror a tree
This is simple, copy the left side of the tree to the right side and vice-versa 
for a new tree: `mirror()`. Also, `isMirror()` checks if a tree is a mirror of 
another using same strategy. Both are *O(n)* time complexity

#### Equality
`equals()` checks if both trees are equal using value comparision with recursion. It
runs at *O(n)* time complexity

#### Balance factor
A BST is said to be balanced if the difference between the heights of left and right
subtrees doesn't exceed 1 at any level. When the tree is balanced, lookup operations
are faster. `isHeightBalanced()` returns a tuple `(height, balanced)`, where height
denotes the depth of the tree and balanced is `True` for balanced trees, else `False` 

#### Add and delete nodes from the BST
The add operation is straightforward. We find a leaf node at the insertion point and
attach our node to it. `insertInPlace()` modifies the tree, whilst `insertAndCopy()`
creates a copy on insertion. Deletion is a little tricky, and we need to cover three
scenarios:
1. Node with no left children
2. Node with no right children
3. Node with both children

For 1 & 2, we just delete the node and swap the children in their place. For 3, we
find the next minimal node and swap it with the deleted node's  place, see 
`deleteInPlace()`
> Note: if the value is already in the tree during insertion, we skip it. Plus, if
the value isn't in the tree while deletion, we don't touch the tree. Insertion and
deletion operations are bound to make the tree unbalanced, we need to balance it
if required

### clone
That's as simple as copying the whole tree into a new place `clone()`

### sorted array to BST
We just split the array into two halfs with a middle element and use them to 
construct a tree recursively.


