class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
        if(s.length()!=t.length()) return false;

        unordered_map<char, char> mp;
        for(int i=0; i<s.length(); i++){
            if(mp.count(s[i])){
                if(t[i] != mp[s[i]]) return false;
            }
            mp[s[i]] = t[i];
        }

        mp.clear();
        for(int i=0; i<s.length(); i++){
            if(mp.count(t[i])){
                if(s[i] != mp[t[i]]) return false;
            }
            mp[t[i]] = s[i];
        }

        return true;

    }
};