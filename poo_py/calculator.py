
class Calculator:
    def __init__(self, batteryMax):
        self.batteryMax=batteryMax
        self.battery=0
        self.display=0

    def useBattery(self):
        if self.battery <= 0:
            print("No charge")
            return False
        else:
            self.battery-=1
            return True

    def charge(self, value):
        if value >= self.batteryMax:
            print("Full batery")
            self.battery=self.batteryMax%value
        else:
            self.battery+=value

    def sum(self, a, b):
        if self.useBattery()==True:
            result=a+b
            self.display=result
            print(f"Result:{result}")
    
    def sub(self, a, b):
        if self.useBattery()==True:
            result=a-b
            self.display=result
            print(f"Result:{result}")

    def mult(self, a, b):
        if self.useBattery()==True:
            result=a*b
            self.display=result
            print(f"Result:{result}")
    
    def div(self, a, b):
        if self.useBattery()==True:
            if b != 0:
                result=a/b
                self.display=result
                print(f"Result:{result}")
            else:
                print("Cannot make a division by zero")
            
    def toString(self):
        str=f"display = {self.display}, battery = {self.battery}"
        print(str)
        # return str

print('Init a calc first...')
print('type help to show the commands')
while 1:
    cmd=input("Insert a command: ")

    if cmd == "end":
        break
    elif cmd == "init":
        btm=int(input("Insert the batteryMax value: "))
        calc = Calculator(btm)
    elif cmd == "show":
        calc.toString()
    elif cmd == "sum":
        a=int(input('Insert the first number: '))
        b=int(input('Insert the second number: '))
        calc.sum(a,b)
    elif cmd == "sub":
        a=int(input('Insert the first number: '))
        b=int(input('Insert the second number: '))
        calc.sub(a,b)
    elif cmd == "div":
        a=int(input('Insert the first number: '))
        b=int(input('Insert the second number: '))
        calc.div(a,b)
    elif cmd == "mult":
        a=int(input('Insert the first number: '))
        b=int(input('Insert the second number: '))
        calc.sum(a,b)
    elif cmd == "charge":
        a=int(input('Insert the charge value: '))
        calc.charge(a)
    elif cmd == "help":
        print('Commands:\n-show\n-end\n-init\n-charge\n-sum\n-sub\n-mult\n-div\n')
    else:
        print('Invalid command')