#include<iostream>
using namespace std;
int main()
{
    if(1)
    {
        goto label_1;
        label_1: cout<<"Hello";
    }
    else{
        goto label_2;
        label_2: cout<<"Nidhi";
    }
    return 0;
}