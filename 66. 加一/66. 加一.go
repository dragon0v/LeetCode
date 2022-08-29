package main

import "fmt"
// 作为go语言学习，按照python版翻译得来
func plusOne(digits []int) []int {
    jinwei := 1
    n := len(digits)
    for i := n-1; i >= 0; i-- {
        if jinwei!=1 {
            break
        }
        digits[i] ++
        if digits[i] == 10 {
            jinwei = 1
            digits[i] = 0
        }else{
            return digits
        }
    }
    return append([]int{1},digits...)
}

func main()  {
    digits := []int{9,9}
    fmt.Println(plusOne(digits))
}