public class Solution {
    public String intToRoman(int num) {
        int[] nums = {1000,900,500, 400,100, 90 , 50,  40, 10,  9 , 5 ,  4 , 1 };
        String[] romans = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int i = 0;
        String res = "";

        while(num>0){
            if(nums[i]<=num){
                num -= nums[i];
                res += romans[i];
            }else{
                i++;
            }

        }
        
        return res;
    }
}

// 是按python版翻译的，python版这个方法挺不错的
