#include<iostream>
#include<vector> 
using namespace std;
 void shorting(int arr[] , int n ){
    for(int i = 0 ; i < n - 1; i++){
        int smallest = i ;
        for(int j = i+1 ; j < n ; j++){
            if(arr[j] < arr[smallest]){
                smallest = j ;
            }
        }
        swap(arr[i] , arr[smallest]);
    }
 }
 void printarr(int arr[] , int n ){
    for(int i = 0 ; i < n ; i++){
        cout<< arr[i]<<" ";
    }
 }
 int main(){
    int arr[] = {5,6,3,4,2,1};
    int n = 6;
    shorting(arr,n);
    printarr(arr,n);
    return 0;
 }