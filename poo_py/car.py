class Car:
    def __init__(self):
        self.psg=0
        self.psgMax=2
        self.fuel=0
        self.fuelMax=100
        self.km=0
    
    def enter(self):
        if self.psg >= self.psgMax:
            print("max of passengers reached")
        else:
            self.psg+=1
        
    def leave(self):
        if self.psg == 0:
            print("empty car")
        else:
            self.psg-=1
    
    def drive(self, value):
        if self.psg == 0:
            print("empty car")
        elif self.fuel == 0:
            print("no fuel in the car")
        elif self.fuel < value:
            print(f"empty tank after ride {self.fuel} km")
            self.km+=self.fuel
            self.fuel=0
        else:
            self.fuel-=value
            self.km+=value

    def toFuel(self, value):
        self.fuel+=value
        if self.fuel > self.fuelMax:
            self.fuel = self.fuelMax % self.fuel

    def toString(self):
        print(f"pass:{self.psg}; gas:{self.fuel}; km:{self.km}")
        
def chain():
    car = Car()
    print("Commands:\n-end\n-show\n-enter\n-leave\n-fuel\n-drive")

    while 1:
        cmd=input("Insert a command:")
        if cmd == "end":
            break
        elif cmd == "show":
            car.toString()
        elif cmd == "enter":
            car.enter()
        elif cmd == "leave":
            car.leave()
        elif cmd == "fuel":
            value=int(input("Insert the value of fuel:"))
            car.toFuel(value)
        elif cmd == "drive":
            value=int(input("Insert the value of km:"))
            car.drive(value)
        else:
            print("Command not found...")
            
chain()
