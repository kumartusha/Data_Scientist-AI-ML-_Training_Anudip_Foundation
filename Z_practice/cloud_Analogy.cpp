// //  C++ All the concepts here...

// #include <bits/stdc++.h>
#include <iostream>
#include <stdexcept>
#include <fstream>
#include <climits>
using namespace std;

// class Tushar
// {
// public:
//     const int age = 20;

//     //    Constructor of the Class...
//     Tushar()
//     {
//         cout << "My name is Tushar Kumar";
//     }
// };

// int main()
// {

//     Tushar *ts = new Tushar();
//     cout<<ts->age;

//     //  Statically Object Created..
//     // Tushar ts;
//     // cout << ts.age;
// }

// int main(){
//    double bal = 1000;
//    int value = 0;

//    try
//    {
//     int result = bal / value;
//      throw invalid_argument("Exception Occured");
//     cout<<result;
//    }
//    catch(exception& e)
//    {
//     cout<<"Exception Occured in Catch";
//     cout<<e.what();
//    }
// }

// int main()
// {

//     int bal = 1000;
//     try
//     {
//         int amount;
//         cout << "Enter the Amount:- ";
//         cin >> amount;

//         //   Deposit Amount Code..
//         if (amount <= 0)
//         {
//             throw invalid_argument("Invalid Deposit Request");
//         }
//         bal = amount + bal;
//         cout << "The Available Balance are:- " << bal;

//         //   ithdrawal Request..
//         int withdraw;
//         cout << "Enter withdraw amount";
//         cin >> withdraw;

//         if (withdraw > bal)
//         {
//             throw runtime_error("Invalid Withdraw Request");
//         }
//         bal = bal - withdraw;
//         cout << "The Avalable Balance are:- " <<bal;
//     }
//     catch (runtime_error &e)
//     {
//         std::cerr << e.what() << '\n';
//     }

// }

// int main(){

//  For write or create the file step..
// ofstream onFile;
// //  For open the File if present then write otherwise create the file..
// onFile.open("C:\\Users\\USER\\OneDrive\\Desktop\\Demo.txt");

// //  write the Data.
// onFile<<"Hello My name is tushar Kumar";

// // onFile.write("Hello My name is tushar Kumar");
// onFile.close();

//  For read the data from the File.*****************.

// ifstream inFile;
// string str;

// inFile.open("C:\\Users\\USER\\OneDrive\\Desktop\\Demo.txt");
// while (getline(inFile, str))
// {
//     cout<<str;
// }

//  For Copied the Data from one file to another *****************
// ofstream inFile;
// ifstream ofFile;
// string str;

// inFile.open("C:\\Users\\USER\\OneDrive\\Desktop\\Demo.txt");
// ofFile.open("C:\\Users\\USER\\OneDrive\\Desktop\\Demo2.txt");

// while (inFile.get(str))
// {
//     ofFile.put(str);
// }

// cout<<"Successfully Copied the Data";
// inFile.close();
// ofFile.close();
// }

// class Tushar{

// private:
// string name;
// int age;
// int weight;

// public:
// //  Constructor Should be Called..
//    Tushar(){
//     cout<<"Object Created";
//    }

//    void input(){
//     cout<<"Enter the name:- ";
//     cin>>name;

//     cout<<"Enter the age:- ";
//     cin>>age;

//     cout<<"Enter the weight:- ";
//     cin>>weight;

//    }

//    void show(){
//     cout<<"Name are:- "<<name;
//     cout<<"Age are:- "<<age;
//     cout<<"Weight are:- "<<weight;
//    }

// };

// int main(){

// Tushar ankit,tushar,rakshit;

// ankit.input();
// ankit.show();

// tushar.input();
// tushar.show();

// rakshit.input();
// rakshit.show();
// }

// class Tushar
// {

// private:
//     int age;
//     string name;

// public:
//     Tushar(int iage, string iname)
//     {
//         this->age = iage;
//         this->name = iname;
//     }
//     void print()
//     {
//         cout<<this->age;
//         cout<<this->name;
//     }
// };

// int main()
// {
//     Tushar ts(20,"Tushar");
//     ts.print();
// }

// class Base
// {
//     protected:
//     int age;
//     string name;

// public:
//     // Constructor..
//     Base()
//     {
//         cout << "Constructor Called";
//     }

//     //  Function..
//       void demo1(){
//         cout<<"Base Demo Function";
//       }
// };

// class Derived : public Base
// {
// private:
//     int age2;
//     string name2;

// public:
//     Derived()
//     {
//         cout << "Derieved Constructor Called";
//     }

//     void demo1()
//     {
//         cout << "I am Derived Demo";
//     }
//     int demo1(int age)
//     {
//         //   cout<<"The age are: -"<<age;
//         // cout << "I am Derived Demo";
//         return age;
//     }
//     int demo1(int age2)
//     {
//         // cout<<"The name are:- "<<name;
//         // cout << "I am Derived Demo";
//         return age2;
//     }
// };

// int main()
// {
//     // int **arr = new int*[5];

//     Base *ref1 = new Base();
//     Derived *ref2 = new Derived();
//     // ref->demo1();
//     // ref->demo2();

//     // ref2->demo1();
//     // ref2->demo1(23);
//     // ref2->demo1(89);
//     // ref2->demo1();

//     cout<<ref2->demo1(29);
//     cout<<ref2->demo1(34);

// }

// class Cloud
// {

//    void fun(){
//     cout<<"I am the fun function";
//    }
// };

// cloud_Analogy::cloud_Analogy(/* args */)
// {
// }

// cloud_Analogy::~cloud_Analogy()
// {
// }

// Cloud::Cloud(){

// }

// Cloud::Cloud(){

// }

// class Parent{

// public:
// int age = 10;
// string name = "Rakshit";
// string sirname = "Mehta";
// string property = "10_Bigha";

// void fun(){
//     cout<<"I am the Parent Class Fun";
// }

// };

// class Child1{
// public:

// };

// class Child2:public Parent, public Child1{
// public:

// };

// int main(){

// // Child1 *ch = new Child1();
// Child2 *ch = new Child2();
// cout<<ch->age;
// cout<<ch->name;
// cout<<ch->property;
// cout<<ch->sirname;
// ch->fun();
// ch->age;

// }

// class GrandParent{

// public:
// virtual void first() = 0;
// virtual void second() = 0;

// };

// class GrandChild: public GrandParent{
// public:
// void first(){
//     cout<<"I am the first";
// }
// void second(){
//     cout<<"I am the second";
// }

// };

// class Parent
// {

// public:
//     virtual void show() = 0;

//     void fun()
//     {
//         cout << "I am the fun Class method";
//     }
// };

// class Child : public Parent
// {
// public:
//     //  If we dont override the Virtual Function then it will also become the abstract Class.
//     void show() override
//     {
//         cout << "Hello I am the Pure Virtual FUnction";
//     }
// };

// int main()
// {

//     // Parent *pr = new Parent();
//     // Child *ch = new Child();
//     // ch->show();

//     GrandChild *ch = new GrandChild();
//     ch->first();
//     ch->second();
// }

// class Base {
// public:
//     void display() { // Virtual function
//         std::cout << "Base class display" << std::endl;
//     }
// };

// class Derived : public Base {
// public:
//     void display(){ // Overriding the base class function
//         std::cout << "Derived class display" << std::endl;
//     }
// };

// int main() {
//     Base* basePtr;
//     Derived derivedObj;

//     basePtr = &derivedObj;

//     // Calls Derived's display() due to virtual keyword
//     basePtr->display();

//     return 0;
// }


// #include <iostream>
// using namespace std;

// class Base {
// private:
//     int privateVar; // Only accessible within the Base class

// protected:
//     int protectedVar; // Accessible within Base and its derived classes

// public:
//     int publicVar; // Accessible anywhere

//     Base() : privateVar(10), protectedVar(20), publicVar(30) {}

//     void showPrivateVar() { // Public member function to access private variable
//         cout << "Private Variable: " << privateVar << endl;
//     }
// };

// class Derived : private Base {
// public:
//     void showVariables() {
//         // privateVar is not accessible here, because it is private in Base
//         // cout << privateVar; // ERROR: Cannot access privateVar directly

//         // protectedVar is accessible in the derived class
//         cout << "Protected Variable: " << protectedVar << endl;

//         // publicVar is accessible in the derived class
//         cout << "Public Variable: " << publicVar << endl;
//     }
// };

// int main() {
//     Base baseObj;
//     Derived derivedObj;

//     // Accessing public variable directly
//     cout << "Public Variable from Base: " << baseObj.publicVar << endl;

//     // Accessing protected or private variables directly is not allowed
//     // cout << baseObj.protectedVar; // ERROR
//     // cout << baseObj.privateVar;   // ERROR

//     // Accessing private variable via public function
//     baseObj.showPrivateVar();

//     // Accessing protected and public variables in derived class
//     derivedObj.showVariables();

//     return 0;
// }


// class Anit{
// private:
//    int money1 = 10000;
//    friend void rohit(Anit, Ankush);

// };


// class Ankush{
// private:
//    int money2 = 20000;
//    friend void rohit(Anit, Ankush);

// };

// void rohit(Anit a1, Ankush a2){

// cout<<a1.money1 + a2.money2;

// }

// int main(){

// Ankush obj1;
// Anit obj2;

// rohit(obj2, obj1);

// }
// #include <iostream> // Include iostream for cout
// using namespace std;

// class Anit{
// private:
//     int money1 = 10000;
//     friend void rohit(Anit, Ankush);
// };

// class Ankush{
// private:
//     int money2 = 20000;
//     friend void rohit(Anit, Ankush);
// };

// void rohit(Anit a1, Ankush a2) {
//     cout << a1 -> money1 + a2->money2; // Access private members through friendship
// }

// int main() {
//     Ankush obj1;
//     Anit obj2;

//     rohit(obj2, obj1); // Call the friend function
//     return 0;
// }


// class Tushar{


// public:
// static int value = 0;

// static void fun(){
//     cout<<"I'm the static Function";
// }
// };

// #include <iostream>
// using namespace std;

class MyClass {
private:
    static int data; // Static data member

public:
    static void setData(int value) { // Static member function
        data = value;
    }

    static void getData() {
        cout << "Data: " << data << endl;
    }
};

int MyClass::data = 0; // Define and initialize static member

int main() {
    // MyClass::setData(42); // Call static function
    // MyClass::getData();   // Output: Data: 42
    // return 0;

    MyClass::setData(25);
    MyClass::getData();
}

