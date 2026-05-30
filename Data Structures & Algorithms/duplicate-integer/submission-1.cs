public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> duplicates = new HashSet<int>();
        foreach (var n in nums) {
            if (duplicates.Contains(n)) {
                return true;
            }
            duplicates.Add(n);
        }
        return false;
    }
}