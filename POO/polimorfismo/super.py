class Super:
    def hello(self):
        print("Olá, sou a superclasse!")
    
class Sub(Super):
    def hello(self):
        print("Olá, eu sou a subclasse!")
        
class Subsub(Sub):
    def hello(self):
        print("Olá, eu sou a subsubclasse")