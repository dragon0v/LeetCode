package main

import "fmt"

func main() {
	fmt.Println(subtractProductAndSum(1234))

}
func subtractProductAndSum(n int) int {
	sum := 0
	mul := 1
	for n > 0 {
		r := n % 10
		n = n / 10
		sum += r
		mul *= r
	}
	return mul - sum
}
