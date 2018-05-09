# Linked Lists

## Singly linked lists
Read about them [here](https://en.wikipedia.org/wiki/Linked_list#Singly_linked_list).

#### Length of a linked list.
Both the iterative `getLength()` and recursive `getLengthRecursive()` operate 
at *O(n)* time time complexity, traversing the list linearly till the end

#### Check if an element is in the list 
Again, both `contains()` and `containsRecursive()` operate at *O(n)* time 
complexity, traversing the list linearly

#### Find nth to last element, for eg, 3rd from last
We maintain two references, which initially point at head of the list. 
Then we let one of the references run `n` steps into the list. Next we 
let the two references run through the list, until the first reference
hits the end. The second reference gives the element in interest.
`findNthFromLast()`

#### Check if list is ordered ( ascending or descending )
Keep on checking the element with its next one until we hit the end.
`isAscending()` and `isDescending()`

#### Check if two lists are equal
Traverse through two lists until the end and check every element in each step.
`equals`

#### Reverse a list
In iterative approach, maintain a previous and current reference to subsequent
nodes. Note the next node of current node and make the previous node as the 
successor of next node and move on. `reverse()`. In recursive approach too,
the same logic applies `reverseRecursive()`. 

