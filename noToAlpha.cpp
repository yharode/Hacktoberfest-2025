#include<iostream>
#include<string>
#include<typeinfo>
using namespace std;

int main(){
    char arr[10] = {'a','b','c','d','e','f','g','h','i','j'};
    string number;
    cout<<"Enter any number : ";
    cin>>number;
    int len = number.size();
    cout<<"Alphabates conresponding to numbers :"<<endl;
    int i=0;
    while(1){
        if(number[i] == '\0'){
            break;
        }
        
        int a = number[i]-48;
        cout<<arr[a];
        i++;
    }
    return 0;
}
