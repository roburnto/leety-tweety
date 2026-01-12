// Last updated: 1/12/2026, 1:41:41 PM
class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;

        int[] prefix = new int[n];
        int[] postfix = new int[n];
        int prefix_sum = 0;
        for(int i = 1; i < n; i++){
            prefix_sum += nums[i-1];
            prefix[i]=prefix_sum;
        }
        int postfix_sum = 0;
        for(int i = n-2; i >=0; i--){
            postfix_sum += nums[i+1];
            postfix[i] = postfix_sum;
        }
        for(int i = 0; i < n; i++){
            if (postfix[i] == prefix[i]){
                return i;
            }
        }
        return -1;
    }
}