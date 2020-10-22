class GrandParent:
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
    
  

class Parent(GrandParent):
    
    def __init__(self, name, money, asset):
        super().__init__(name, money)
        self.name = name
        self.money = money
        self.asset = asset + money

    


class Child(Parent):

    def __init__(self, name, money, asset):
        super().__init__(name, money, asset)
        self.name = name
        self.money = money
        self.asset = asset + money


if __name__ == "__main__":
    
    g = GrandParent("Kamlesh", 10000)
    p = Parent("Asim", 15000, g.money) 
    c = Child("Abhishek", 20000, p.asset) 

    print(g.name, g.money)
    print(p.name, p.money, p.asset)
    print(c.name, c.money, c.asset)
    
    