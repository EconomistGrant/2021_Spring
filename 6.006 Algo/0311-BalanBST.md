Balanced BST Strategy
Augment every node with useful INFO
Define a local INVARIANT on INFO

AVL Tree (Adelson-Velskii-Landis)
INFO: "height": leaves have height 0, their parents 1, ...
INVARIANT: the height of left child and right child differ by at most 1

Maintaining invariant
trick of rotation(on your handwritten notes)

Inserting
















# Rec 8
Why important to be balanced: height h = O(logn)
-> O(h) = O(logn)
## AVL Tree
AVL property: the heights of the children differ by at most 1
skew: A.right.height - A.left.height

a height balanced(AVL property) tree is balanced(h = Olog(n))

## Rotations
Rotate Right:
     D
   B   E
  A C 

     B
   A   D
      C E

before right rotate: if B is right heavy -> make it left heavy

Downside up: from a leaf to higher 

if a delete: