package main

import "fmt"

func main() {
	fmt.Println(canConstruct("aab","abcba"))
}

func canConstruct(ransomNote string, magazine string) bool {
    a := [26] int {}
	for _,c := range(magazine){
		a[c-'a'] ++
	}
	for _,c := range(ransomNote){
		a[c-'a'] --
		if a[c-'a']<0{
			return false
		}
	}
    return true
}