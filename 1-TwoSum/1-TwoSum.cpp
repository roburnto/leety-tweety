// Last updated: 1/12/2026, 1:27:56 PM
1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        // map for numbers and their index
5        std::unordered_map<int, int> index;
6        // looking through the vector
7        for( int i = 0; i < nums.size(); i++ ){
8            // difference between target and num
9            int diff = target - nums[i];
10            //checking in hash_map
11            if(auto it = index.find(diff); it != index.end()){
12                // returning the index of both numbers
13                return {it->second, i};
14            }
15            // inserting number in hashmap
16            index[nums[i]] = i;
17        }
18        // if none is found
19        return {};
20    }
21};