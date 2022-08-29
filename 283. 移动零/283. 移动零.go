package main

import "fmt"

func main() {
    // fmt.Println()
}

func moveZeroes(nums []int)  {
    cnt := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[cnt] = nums[i]
            cnt += 1
        }
    }
    for j := 0; j < len(nums)-cnt; j++ {
        nums[j] = 0
    }


}


