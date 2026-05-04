// Last updated: 5/4/2026, 4:32:49 PM
1class Solution {
2   public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        unordered_map<string, vector<string>> index;
5        for (string str : strs) {
6            vector<int> charCount(26, 0);
7            for (char c : str) {
8                charCount[c - 'a'] += 1;
9            }
10            string key = to_string(charCount[0]);
11            for (int i = 1; i < 26; i++) {
12                key += ',' + to_string(charCount[i]);
13            }
14            index[key].push_back(str);
15        }
16        vector<vector<string>> res;
17        for (auto& pair : index) {
18            res.push_back(pair.second);
19        }
20        return res;
21    }
22};
23