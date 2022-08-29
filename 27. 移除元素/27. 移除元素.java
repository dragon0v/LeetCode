class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        // i是左指针，0-i之间是返回的结果
        // j是右指针，用于比较，nums[j]=val则j++，否则ij++
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=val){
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
    public static void main(String[] args) {
        int[] nums = {1,2,3,4,4,4,4,};
        int r = removeElements(nums,4);
        System.out.println(r);
    }
}

// 双指针交换