class Solution {
    public:
        int countNumbersWithUniqueDigits(int n) {
            if(n==0) return 1;
            // if(n==1) return 10;
            int dp[n+1];
            dp[0]=0;dp[1]=0; /// dp is the repeat of count i;
            for(int i = 2 ; i <= n ;i++ ){
                dp[i] = dp[i-1]*10+(9*pow(10,i-2) - dp[i-1])*(i-1);
                // (9*pow(10,i-2) - dp[i-1]) 指的是无重复的个数
            }
            int sum = 0 ; 
            for(int i = 0 ; i < n+1;i++){
                sum+=dp[i];
            }
            return pow(10,n)-sum;
        }
    };
    
// 作者：faker-28
// 链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits/solution/dpqiu-jie-jian-dan-yi-dong-by-faker-28-08te/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// 如果已经知道n位的结果，如何获得n+1位的结果呢，可以这样考虑。
// 对于n+1位的数字有两种可能，

// 前边的n位已经有了重复，那么最后一位0-9都可以
// 前边的n位数字是没有重复的，那么最后一位可以是这n位数字中的任何一位

// 作者：faker-28
// 链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits/solution/dpqiu-jie-jian-dan-yi-dong-by-faker-28-08te/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。