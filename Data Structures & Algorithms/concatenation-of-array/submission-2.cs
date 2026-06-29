public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int[] ans = new int[nums.Length * 2];
        for(int i = 0; nums.Length > i; ++i){
            ans[i] = nums[i];
            ans[i + nums.Length] = nums[i];
        }

        return ans;
        // return  nums.Concat(nums).ToArray();
    }
}