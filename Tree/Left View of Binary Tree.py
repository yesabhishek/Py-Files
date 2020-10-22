""" Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible 
when tree is visited from Left side. The task is to complete the function leftView(),
which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Input Format:

The values in the string are in the order of level order traversal of the tree where, 
numbers denote node values, and a character “N” denotes NULL child.

For example:

 
For the above tree, the string will be: 1 2 3 N N 4 6 N 5 N N 7 N

Example 1:

Input:
S = 1 3 2
Output: 1 3
Explanation:Below is the given tree with
its nodes
   1                   
 /  \
3    2
Here left view of the tree will be 1 3.
Example 2:

Input:
S = 10 20 30 40 60 N N
Output: 10 20 40
Explanation:below is a given tree with its
nodes.

We can clearly see that nodes which are at
left view of tree they are 10 20 40.
Your Task:
You just have to complete the function leftView() that prints the left view. The newline is automatically appended by the driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 100
1 <= Data of a node <= 1000 """


''' Corner case '''

class Node:

    def init(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self):
        
        pass

    def traverse(self):
        pass



root = Node()


