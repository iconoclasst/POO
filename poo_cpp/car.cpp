#include <iostream>
using namespace std;

class Car {
//atributes
int pass=0;
int passMax=2;
int gas=0;
int gasMax=100;
int km=0;

//methods
public:

Car(){}

void enter(){
    if(this->pass >= 2)
        cout << "Full car!\n";
    else
        this->pass+=1;
}

void leave(){
    if(this->pass <= 0)
        cout << "Empty car!\n";
    else
        this->pass-=1;
}

void drive(int value){
    if(this->pass <= 0)
        cout << "Empty car!\n";
    else if(this->gas <= 0)
        cout << "Empty tank\n";
    else if(value > this->gas){
        cout << "Empty tank after ride " << this->gas << " km\n";
        this->km+=gas;
        gas=0;
    } else {
        this->gas-=value;
        this->km+=value;
    }
}

void toFuel(int value){
    this->gas+=value;
    if(this->gas > this->gasMax)
        this->gas=this->gasMax%gas;

}

void show(){
    cout <<"pass:" << this->pass 
    <<", gas: " << this->gas << ", km:" 
    << this->km << "\n";
}

};

void commandLine(Car car){
string cmd;
cout << "Type \"help\" to show all commands.\n";

while(true){
cout << "Insert a command: ";
cin >> cmd;

if(cmd == "end"){
    break;
} else if(cmd == "show"){
    car.show();
} else if(cmd == "enter"){
    car.enter();
} else if(cmd == "leave"){
    car.leave();
} else if(cmd == "fuel"){
    int value=0;
    cout << "Insert the value of fuel: ";
    cin >> value;
    car.toFuel(value);

} else if(cmd == "drive"){
    int value=0;
    cout << "Insert the value of km: ";
    cin >> value;
    car.drive(value);
} else if(cmd == "help"){
    cout << "Commands:\n-end\n-show\n-enter\n-leave\n-fuel\n-drive-\n";
} else {
    cout << "Command not found...\n";
}
}

}

int main() {

Car car;
commandLine(car);

}
