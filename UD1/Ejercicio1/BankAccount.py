class BanckAccount:
    def __init__(self):
        pass 

    def set_details(self, name, balance= 0):
        self.name = name
        self.balance = balance

    def display(self):
        print("Este es mi nombre:",self.name)
        print("Este es mi balance:",self.balance)
    
    def recall(self,amount):
       
        self.balance -= amount
    
    def deposit (self,amount):
       
        self.balance += amount
    

obj1 = BanckAccount()
obj2 = BanckAccount()

obj1.set_details("Juan",5000)
obj2.set_details("Fran",7000)

obj1.display()
obj2.display()

obj1.recall(300)
obj2.deposit(500)

obj1.display()
obj2.display()
