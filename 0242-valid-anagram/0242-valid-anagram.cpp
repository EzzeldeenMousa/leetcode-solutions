class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> S_freq;
        unordered_map<char, int> T_freq;

        if(s.size()!=t.size()){
            return false;
        }

        for(int i=0; i<s.size(); i++){
            S_freq[s[i]]++;    
        }

        for(int i=0; i<t.size(); i++){
            T_freq[t[i]]++;
        }

        if(S_freq==T_freq){
            return true;
        }


        return false;
    }
};
        

        