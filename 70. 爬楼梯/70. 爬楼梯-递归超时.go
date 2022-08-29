package main

import "fmt"

func main() {
	fmt.Println(climbStairs(45))
}


// 递归实现，在n=44超时了，本地运行都跑了9秒
func climbStairs(n int) int {
    // 答案是前两个的和
    if n == 1{
        return 1
    }
    if n == 2{
        return  2
    }
    return climbStairs(n-1) + climbStairs(n-2)
}


// 通过找规律发现答案是前两个之和