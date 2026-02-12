#include<iostream>
#include<vector>
using namespace std;
void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0 ;
        int  right = n - 1 ;
         for( int i = 0;i < k; i++){
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
         
         for(int i = 0 ; i < n ; i++){
            cout<< nums[i]<<" " ;
         }
    }
    int main(){
      vector<int>  nums = {1,2,3,4,5,6};
       int k = 3;
        rotate(nums,k);
        return 0;
    }