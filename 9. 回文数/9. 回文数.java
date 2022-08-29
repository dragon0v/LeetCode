class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        int x1 = x;
        int x2 = 0;
        while (x>0) {
            x2 = 10*x2 + x%10;
            x = x/10;
        }
        if(x1==x2){
            return true;
        }else{
            return false;
        }
    }
}
// 这里本来有个陷阱，翻转后可能会超出2^31-1
// 但是其实溢出不影响，因为这个数原来肯定不溢出，但是翻转后溢出，所以必然不是回文数