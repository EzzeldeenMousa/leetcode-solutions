#include<string>
#include<iostream>
using  namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t found = haystack.find(needle);

        if(found == string::npos){
            return -1;
        }

        else{
            return (int)found;
        }
        
    }
};