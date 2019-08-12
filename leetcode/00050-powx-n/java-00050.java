import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class PowXN {
    public class Solution {
        public double myPow(double x, int n) {
            double pow = 1;
            if(n <0) {
                x = 1/x;
            }
            while(n!=0) {
                if((n&1)==1) {
                    pow *= x;
                }
                x = x * x;
                n /= 2;
            }
            return pow;
        }
    }

    public static class UnitTest {
        @Test
        public void test() {
            assertEquals(new PowXN().new Solution().myPow(2,-3),0.125);
            assertEquals(new PowXN().new Solution().myPow(2,3),8);
            assertEquals(new PowXN().new Solution().myPow(2,0),1);
            assertEquals(new PowXN().new Solution().myPow(2,Integer.MIN_VALUE),0);
        }
    }
}
