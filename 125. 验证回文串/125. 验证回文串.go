package main

import "fmt"

func toLower(c byte) (r byte) {
	if c >= 'A' && c <= 'Z' {
		r = c + 'a' - 'A'
	} else {
		r = c
	}
	return
}
func process(s string) (ret string) {
	for _, c := range s {
		if (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
			ret += string(c)
		}
	}
	fmt.Println(ret)
	return
}
func isPalindrome(s string) bool {
	if s == "" {
		return true
	}
	s = process(s)
	for i := 0; i < len(s)/2; i++ {
		fmt.Println(toLower(s[i]), toLower(s[len(s)-i-1]))
		if toLower(s[i]) != toLower(s[len(s)-i-1]) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("j:kJ"))
}
