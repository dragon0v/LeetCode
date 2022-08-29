package main

import "fmt"

func main() {
	a := []int {1,3,5,7,4,9} 
	fmt.Println(findLengthOfLCIS(a))
}

func findLengthOfLCIS(nums []int) int {
    if len(nums) <= 1{
		return len(nums)
	}
	maxlen := 1
	t := 1
	for i := 1;i<len(nums);i++{
		if nums[i]>nums[i-1]{
			t++
		}else{
			if t > maxlen{
				maxlen = t
			}
			t = 0
		}
	}
    
	return maxlen

}