class Organization:

    def __init__(self, val):

        self.val = val
        self.boss = None
        self.worker = []

    def print_hierarchy(self):
        
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|_ _" if self.boss else ""
        print(prefix,self.val)
        if self.worker:
            for w in self.worker:
                w.print_hierarchy()  


    def insert_into(self,w):
        
        self.worker.append(w)
        w.boss = self


    def find(self,data):
        pass

    def get_level(self):
        
        level = 0
        p = self.boss
        while p:
            level += 1
            p = p.boss

        return level



def make_connection():

    ceo = Organization("Nilupul (CEO) ")

    cto = Organization("Chinmay (CTO)")

    hr = Organization("Gels (HR HEAD)")

    hr.insert_into(Organization("Peter (Recruitment Manager)"))


    
    hr.insert_into(Organization("Waqas (Policy Manager)"))

    
    infrastructure_head = Organization("Vishwa (Infrastructure Head)")
    application_head = Organization("Aamir (Application Head)")

   
    
    infrastructure_head.insert_into(Organization("Dhaval (Cloud Manager)"))
    infrastructure_head.insert_into(Organization("Abhijeet (App Manager)"))

    



    ceo.insert_into(cto)
    ceo.insert_into(hr)

    cto.insert_into(infrastructure_head)
    cto.insert_into(application_head)


    print(ceo.__dict__,"\n")
    print(cto.__dict__,"\n")
    print(infrastructure_head.__dict__,"\n")



    ceo.print_hierarchy()

if __name__ == "__main__":
        
    print("1. Print only Desingnation")
    print("2. Print only Names")
    print("3. Print both")
    print("4. Exit ")
    choice = input("Enter the Choice:")


    if choice == '3':
        ceo = make_connection()

    elif choice == '4':
        exit(0)

    else:
        print("Wrong Input, Exitting ")
        exit(0) 

    
        


        