class TreeNode:

    def __init__(self, data):

        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):

        self.children.append(child)
        child.parent = self


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|_ _" if self.parent else ""
        print(prefix,self.data)
        if (self.children):
            for child in self.children:
                child.print()

def build_product_tree():

    root = TreeNode("Electronics")                              # Root of the Tree or the Top Element

    laptop = TreeNode("Laptop")                                 # Child node of the tree or the 1st Gen   
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Hp"))
    laptop.add_child(TreeNode("Lenovo"))



    television = TreeNode("Television")  
    television.add_child(TreeNode("Sony"))
    television.add_child(TreeNode("Lg"))
    television.add_child(TreeNode("Samsung"))
    television.add_child(TreeNode("Onida"))


    mobile = TreeNode("Mobile")  
    mobile.add_child(TreeNode("Apple"))
    mobile.add_child(TreeNode("Xiaomi"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Oppo"))


    washing_machine = TreeNode("Washing Machine") 
    washing_machine.add_child(TreeNode("IFB"))
    washing_machine.add_child(TreeNode("LG"))
    washing_machine.add_child(TreeNode("Bosch"))
    washing_machine.add_child(TreeNode("Samsung"))

    root.add_child(laptop)                                     # Leaf node of the tree or the Last Gen
    root.add_child(television)
    root.add_child(washing_machine)
    root.add_child(mobile)

    
    root.print()


if  __name__ == "__main__":
    
    root = build_product_tree()
  
