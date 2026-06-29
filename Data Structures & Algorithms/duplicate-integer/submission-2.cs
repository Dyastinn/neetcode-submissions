public class Solution {
    public bool hasDuplicate(int[] nums) {
        var lNumbers = new HashSet<int>();
        foreach (int n in nums){
            if (!lNumbers.Add(n)){
                return true;
            }
        }
        return false;
    }
}