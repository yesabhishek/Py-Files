class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.data == 0:
            print("None")
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            
            self.right.PrintTree()


root = Node(0)

""" N = int(input("Enter the Size:"))
for i in range(0,N):
    root.insert(input())
 """


root.insert(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(60)


root.PrintTree()