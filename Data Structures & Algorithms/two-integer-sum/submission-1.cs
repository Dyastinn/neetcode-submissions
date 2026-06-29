public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int,int>();
        int [] output = new int [2]; 
        for(int i = 0; i < nums.Length; i++){
            if(dict.ContainsKey(nums[i])){
                output[0] = dict[nums[i]];
                output[1] = i;
                return output;
            }
            dict[target - nums[i]] = i;
        }
        return output;
    }
}
