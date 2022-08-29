package main

import "fmt"

func main() {
    fmt.Println(clumsy(9))
}
func clumsy(N int) (ans int) {
    stk := []int{N}
    N--

    index := 0 // 用于控制乘、除、加、减
    for N > 0 {
        switch index % 4 {
        case 0:
            stk[len(stk)-1] *= N
        case 1:
            stk[len(stk)-1] /= N
        case 2:
            stk = append(stk, N)
        default:
            stk = append(stk, -N)
        }
        N--
        index++
    }

    // 累加栈中数字
    for _, v := range stk {
        ans += v
    }
    return
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/clumsy-factorial/solution/ben-jie-cheng-by-leetcode-solution-deh2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。