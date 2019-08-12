import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CompareVersionNumbers {
    public class Solution {
        public int compareVersion(String version1, String version2) {
            String[] list1 = version1.split("\\.");
            String[] list2 = version2.split("\\.");
            int length = Math.max(list1.length, list2.length);
            for(int i=0; i < length; i++) {
                int num1 = i < list1.length ? Integer.parseInt(list1[i]) : 0;
                int num2 = i < list2.length ? Integer.parseInt(list2[i]) : 0;
                int compare = Integer.compare(num1,num2);
                if(compare!=0) return compare;
            }
            return 0;
        }
    }

    public static class UnitTest {
        @Test
        public void test() {
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1.2", "1.1"),1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1", "0"),1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("0", "1"),-1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("0.1.1", "0.1"),1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1.2.3", "1.2.3"),0);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1.2.3", "1.2.13"),-1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1.0.0", "1"),0);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1.0.1", "1"),1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1", "1.1"),-1);
            assertEquals(new CompareVersionNumbers().new Solution().compareVersion("1", "1.00"),0);
        }
    }
}
