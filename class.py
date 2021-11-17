class Car (object):
    def __init__(self, model, speed, money, seats):
        self.model = model
        self.speed = speed
        self.money = money
        self.seats = seats 
        def setModel(self):   
         print("stopped")  
        print("started")            
# Define some car
lamborgini = Car("Lamborgini", 400, 20000000, 2)
limozine = Car("Limozine", 300, 50000000, 7)

print(lamborgini.setModel())