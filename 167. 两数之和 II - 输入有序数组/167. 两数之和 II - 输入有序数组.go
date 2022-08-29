package main

import "fmt"

func main() {
    fmt.Println(twoSum([]int{1,2,3,4,5,6},3))
}

func twoSum(numbers []int, target int) []int {
    i,j := 0,len(numbers)-1
    k := 0
    for ;i<j; {
        k = numbers[i] + numbers[j]
        if k==target {
            return []int{i+1,j+1}
        }else if k < target{
            i += 1
        }else{
            j -= 1
        }
    }
    return []int{i,j}
}