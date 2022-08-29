package main

import "fmt"

func main() {

}

func compressString(S string) string {
	if len(S) <= 2 {
		return S
	}
	last := byte(S[0])
	count := 1
	res := ""
	for _, cc := range S[1:] {
		c := byte(cc)
		if c == last {
			count++
		} else {
			res += string(last) + fmt.Sprint(count)
			last = c
			count = 1
		}
	}
	res += string(last) + fmt.Sprint(count)
	if len(res) >= len(S) {
		return S
	}
	return res
}

// 感受：类型转换，rune和byte
// int转string不可以用string(int)->返回\u0001，要用fmt.Sprint(int)
