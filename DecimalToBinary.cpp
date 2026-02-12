#include<iostream>
using namespace std;

void DecimalToBinary(int n){
    int binary[30], i = 0;
    while(n > 0){
        binary[i] = n % 2;
        n /= 2;
        i++;
    }
    for(int j = i-1; j >= 0;j--){
        cout<<binary[j];
    }
}
int main(){
    int num;
    cout<<"Enter Decimal Number:";
    cin>>num;
    DecimalToBinary(num);
}