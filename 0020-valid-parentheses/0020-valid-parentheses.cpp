#include<iostream>
#include<stack>
#include<unordered_map>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map <char, char> dict;
        dict = {{')','('}, {']','['}, {'}', '{'}};
        stack<char> stack;

        for(int i=0; i < s.length(); i++){
            if(dict.find(s[i])==dict.end()){
                stack.push(s[i]);}
            else{
                if(stack.empty() || stack.top() != dict[s[i]]){
                    return false;
                }
                stack.pop();
            }
        
            
            


        }
        
        return stack.empty();
        
    }
};