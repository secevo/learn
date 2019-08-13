class Solution {
    public boolean isPalindrome(int x) {
        if (x<0) return false;
            if(x<10) return true;
            int max = 10;
            while(x / max >= 10) {
                max *= 10;
            }
            while(max >= 10) {
                int left = x / max;
                x = x % max;
                int right = x % 10;
                x = x /10;
                if(left!=right) return false;
                max /= 100;
            }
            return true;
    }
}