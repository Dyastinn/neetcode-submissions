public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        Array.Sort(strs);
        string shortest = strs[0];
        string longest = strs[strs.Length - 1];
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < shortest.Length; i++){
            if(shortest[i] == longest[i]) sb.Append(shortest[i]);
            else break;
        }
        return sb.ToString();


    }
}