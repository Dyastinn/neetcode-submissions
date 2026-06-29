public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string, List<string>>();

        foreach(string str in strs){
            int[] charFrequency = new int[26];
            foreach(char c in str){
                int asc = (int)c - (int)'a';
                charFrequency[asc] += 1; 
            }
            string key = string.Join(",", charFrequency);
            dict.TryAdd(key, new List<string>());
            dict[key].Add(str);
        }
        var list = new List<List<string>>();
        foreach (var value in dict.Values)
        {
            list.Add(value);
        }

        return list;
    }
}
