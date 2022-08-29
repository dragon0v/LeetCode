package main

import "fmt"

func main() {
	fmt.Println(removeDuplicates("abbaca"))
}

func removeDuplicates(S string) string {
	mystack := make([]rune, 0, 20000)
	for i, c := range S {
		// TODO
		fmt.Println(i, mystack)
	}
	res := ""
	return res
}
