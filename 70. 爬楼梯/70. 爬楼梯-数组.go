package main

import "fmt"

func main() {
	fmt.Println(climbStairs(45))
}



func climbStairs(n int) int {
    res := make([]int, 46)
    // 答案是前两个的和
    if n == 1{
        return 1
    }
    if n == 2{
        return  2
    }
    for i := 2; i < 46; i++ {
        res[i] = res[i-1] + res[i-2]
    }
    // 楼梯数从1开始
    return res[n-1]
}


// 通过找规律发现答案是前两个之和