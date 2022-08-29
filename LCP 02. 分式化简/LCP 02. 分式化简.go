package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	fmt.Println(fraction(a))
}

func fraction(cont []int) []int {
	a := 0
	b := 1
	for i := len(cont) - 1; i >= 0; i-- {
		a += b * cont[i]
		a, b = b, a
	}

	g := gcd(a, b)
	// 最后一次不用反转，所以这里是b,a
	res := []int{b / g, a / g}
	return res
}
func gcd(a int, b int) int {
	r := 1
	if a > b {
		a, b = b, a
	}
	for i := 2; i < a; i++ {
		if a%i == 0 && b%i == 0 {
			r = i
		}
	}
	return r
}
