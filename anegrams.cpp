#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

bool areanagram(string s1 , string s2){

if(s1.length() != s2.length()) return false;

unordered_map<char , int>freq;

for(char ch : s1){
    freq[ch]++; 
}

for(char ch : s2){
    freq[ch]--;
}
for(auto it : freq){
    if(it.second != 0 ) return false ;
    else{
        return true ;
    }
    return true ;
}

}
int main(){
    string str1 = "part";
    string str2 = "care";
    if(areanagram(str1 , str2)){
        cout<<"string  are anagrams ";
    }
    else{
        cout<<"string are not anegrams";
    }
    return 0;
}