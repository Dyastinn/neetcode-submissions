class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hash = {}

        for (let i of nums) {
            if (i in hash) return true; // Stops the loop early
            hash[i] = true;
        }

        return false;
    }
}
