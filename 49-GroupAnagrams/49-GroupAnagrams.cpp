// Last updated: 1/12/2026, 1:40:51 PM
1class Solution {
2public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        
5        unordered_map<string, vector<string>> mp;
6
7        for (string s : strs) {
8            string sign = s;                 // copy original string
9            sort(sign.begin(), sign.end()); // sort the copy to create a key
10
11            mp[sign].push_back(s);           // group by sorted key
12        }
13
14        vector<vector<string>> result;
15        for (auto& pair : mp) {
16            result.push_back(pair.second);
17        }
18
19        return result;
20    }
21};
22