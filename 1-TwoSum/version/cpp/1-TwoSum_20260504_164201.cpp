// Last updated: 5/4/2026, 4:42:01 PM
1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        unordered_map<int,int> index;
5        for(int i = 0; i < nums.size(); i++){
6            int comp = target - nums[i];
7            if(index.contains(comp)){
8                return {index[comp], i};
9            }
10            index[nums[i]]=i;
11        }
12        return {1,1};
13    }
14};
15