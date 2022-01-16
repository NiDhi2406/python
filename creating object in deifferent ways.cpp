#include<iostream>
using namespace std;
class Human{
public:
string name;
void introduce(){
    cout<<"hi"<<name<<endl;

}
};
int main()
{
    Human nidhi;
    Human*siya=new Human();

    nidhi.name="nidhi";
    nidhi.introduce();

    siya->name="siya";
    siya->introduce();
    return 0;
}





