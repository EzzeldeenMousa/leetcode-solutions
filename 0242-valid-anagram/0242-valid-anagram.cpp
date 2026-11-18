class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> S_freq;
        unordered_map<char, int> T_freq;

        if(s.size()!=t.size()){
            return false;
        }

        for(int i=0; i<s.size(); i++){
            if(S_freq.contains(s[i])){
                S_freq[s[i]]++;
            }

            else{
                S_freq[s[i]] = 1;
            }
        }

        for(int i=0; i<t.size(); i++){
            if(T_freq.contains(t[i])){
                T_freq[t[i]]++;
            }

            else{
                T_freq[t[i]]=1;
            }
        }


        if(S_freq==T_freq){
            return true;
        }


        return false;
    }
};
        

        