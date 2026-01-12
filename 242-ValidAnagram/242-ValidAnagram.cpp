// Last updated: 1/12/2026, 1:13:53 PM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        int freq[26] = {0};
5
6        for (char c: s) freq[c-'a']++;
7        for (char c: t) freq[c-'a']--;
8
9        for (int i = 0; i < 26; i++){
10            if(freq[i] !=0){
11                return false;
12            }
13        }
14        return true;
15    }
16};