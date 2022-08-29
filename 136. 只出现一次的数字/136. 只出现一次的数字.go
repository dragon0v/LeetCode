// 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

// 使用位运算 异或 ，对所有元素进行位运算，最后剩下的就是解
// 异或：任何数异或0，结果仍未原来的数
// 		任何数和自己异或，结果为0，
// 		满足交换律和结合律


package main

import "fmt"

func main() {
	a := []int{1,2,3,4,5,5,4,3,2}
	fmt.Println(singleNumber(a))
}


func singleNumber(nums []int) int {
    t := 0
	for _,v := range(nums){
		t = t^v
	}
	return t
}

