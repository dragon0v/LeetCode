class Solution {
public:
    int arraySign(vector<int>& nums) {
        // 统计负数的个数，根据个数返回符号
        int neg = 0;
        for (auto n:nums){
            if(n==0){
                return 0;
            }
            if (n<0){
                neg++;
            }
        }
        return neg%2 ? -1:1;
        
    }
};