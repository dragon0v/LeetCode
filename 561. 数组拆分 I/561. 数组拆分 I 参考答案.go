package main

import (
	"fmt"
	"sort"
)

func main() {
	a := []int{1, 2, 3, 4, 5, 3, 2, 1}
	fmt.Println(arrayPairSum(a))
}

func arrayPairSum(nums []int) (ans int) {
	sort.Ints(nums)
	for i := 0; i < len(nums); i += 2 {
		ans += nums[i]
	}
	return
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/array-partition-i/solution/shu-zu-chai-fen-i-by-leetcode-solution-9m9y/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
