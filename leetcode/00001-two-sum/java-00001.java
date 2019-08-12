public class TwoSum {
    public class Solution {
        public int[] twoSum(int[] nums, int target) {
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            for(int i = 0; i < nums.length; i++) {
                int x = nums[i];
                if(map.containsKey(target - x)) {
                    return new int[]{ map.get(target - x), i };
                }
                map.put(x, i);
            }
            throw new IllegalArgumentException("No two sum solution");
        }
    }
}
