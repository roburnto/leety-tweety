// Last updated: 1/12/2026, 1:41:25 PM
import java.util.*;

class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        // Convert arrays to sets (remove duplicates automatically)
        Set<Integer> set1 = new HashSet<>();
        for (int n : nums1) set1.add(n);

        Set<Integer> set2 = new HashSet<>();
        for (int n : nums2) set2.add(n);

        // Copy sets so we don’t modify the originals
        Set<Integer> diff1 = new HashSet<>(set1);
        Set<Integer> diff2 = new HashSet<>(set2);

        // Remove common elements
        diff1.removeAll(set2); // nums1 elements not in nums2
        diff2.removeAll(set1); // nums2 elements not in nums1

        // Convert to lists
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(new ArrayList<>(diff1));
        answer.add(new ArrayList<>(diff2));

        return answer;
    }
}
