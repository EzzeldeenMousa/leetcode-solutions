class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> seen;

        for(int i=0; i < strs.size(); i++){
            string key = strs[i];
            sort(key.begin(), key.end());
            seen[key].push_back(strs[i]);

        }

        vector<vector<string>> result;
        for(auto& pair: seen){
            result.push_back(pair.second);
        }

        return result;
        
    }
};