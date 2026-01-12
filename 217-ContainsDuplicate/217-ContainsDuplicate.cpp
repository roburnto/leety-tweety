// Last updated: 1/12/2026, 1:02:53 PM
1class Solution {
2public:
3    bool containsDuplicate(vector<int>& nums) {
4        // use std::unordered_set<int>
5        std::unordered_set<int> seen;
6        for (int num: nums){
7            if (seen.count(num)){
8                return true;
9            }
10            seen.insert(num);
11        }
12        return false;
13    }
14};