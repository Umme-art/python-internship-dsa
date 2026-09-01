class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int k=s1.length();
       if (s1.length() > s2.length()) {
            return false;
        }

        vector<int> mp1(26, 0);
        vector<int> mp2(26, 0);
        for (int i = 0; i < k; i++) {
            mp1[s1[i] - 'a']++;
            mp2[s2[i] - 'a']++;
        }

        if (mp1 == mp2) {
            return true;
        }
        for (int h = k; h < s2.length(); h++) {
             mp2[s2[h - k] - 'a']--;
             mp2[s2[h] - 'a']++;
            if (mp1 == mp2) {
                return true;
            }
        }

        return false;

    }
};