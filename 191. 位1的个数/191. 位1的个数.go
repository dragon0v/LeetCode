package main

import "fmt"

func main() {
    fmt.Println(hammingWeight(11))
}

func hammingWeight(num uint32) int {
    cnt := 0
    for i := 0; i < 32; i++ {
        if num & 1 == 1 {
            cnt += 1
        }
        num = num >> 1
    }
    return cnt
}