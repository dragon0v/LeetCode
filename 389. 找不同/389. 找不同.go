package main

import "fmt"

func main() {
    fmt.Println(findTheDifference("a","as"))
}
func findTheDifference(s string, t string) byte {
    l := [26]int{}
    for i := 0; i < len(s); i++ {
        l[s[i]-'a'] ++
    }
    for i := 0; i < len(t); i++ {
        l[t[i]-'a'] --
        if l[t[i]-'a']==-1 {
            return t[i]
        }
    }
    return 0
}

