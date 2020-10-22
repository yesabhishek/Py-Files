class TreeNode:

    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        
        if data == self.data:
            return 
        
        if data < self.data:
            #add in left SubTree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = TreeNode(data)

        else:
            #add in right SubTree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = TreeNode(data)


    def Traverse_InOrder(self):

        elements = []
        # Visit the left Node first
        if self.left:
            elements += self.left.Traverse_InOrder()
        # Visit the center Node first
        elements.append(self.data)
        # Visit the right Node first
        if self.right:
            elements += self.right.Traverse_InOrder()                                                                                                                                                                                                                                                                                                                                                                                        .Traverse_InOrder()


        return elements

    def Traverse_PostOrder(self):

        elements = []

        if self.left:
            elements += self.left.Traverse_PostOrder()
        if self.right:
            elements += self.right.Traverse_PostOrder()

        elements.append(self.data)
        
        return elements

        

    def Traverse_PreOrder(self):

        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.Traverse_PreOrder()
        if self.right:
            elements += self.right.Traverse_PreOrder()

        
        
        return elements


    def BreadthFirstSearch(self, val):
        pass

    def delete(self,val):
        pass

    def TotalElements(self):
        pass

    def Search(self, data):

        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.Search(data)
            else:
                return False
            
        else:
            if self.right:
                return self.right.Search(data)
            else:
                return False

    def Max(self):

        
        while self.right != None:
            self = self.right

        return self.data

    def min(self):

        while self.left != None:
            self = self.left

        return self.data


    def left_view(self):

        l = []
        
        if self.left:
            l += self.left.left_view()
        l.append(self.data)
        
        return l

def BuildTree(elements):
    
    root = TreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])


    return root


if __name__ == "__main__":
    
    num = [1, 2, 3, 4, 5]
    print("Input List \t\t  :", num)
    numbers = BuildTree(num)
    
    #print("BST in In Order Traversal :",numbers.Traverse_InOrder())
    print("BST in Post Order Traversal :",numbers.Traverse_PostOrder())
    print("BST in Pre Order Traversal :",numbers.Traverse_PreOrder())

    print("Found : ",numbers.Search(7))

    print("Max Element is : ",numbers.Max())
    print("Min Element is : ",numbers.min())

    print(numbers.left_view())