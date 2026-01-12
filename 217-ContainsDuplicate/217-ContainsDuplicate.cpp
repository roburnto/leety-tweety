// Last updated: 1/12/2026, 1:00:34 PM
1class Solution {
2public:
3    bool containsDuplicate(vector<int>& nums) {
4        std::set<int> set{};
5        for (int num: nums){
6            if (set.contains(num)){
7                return true;
8            }
9            set.insert(num);
10        }
11        return false;
12    }
13};