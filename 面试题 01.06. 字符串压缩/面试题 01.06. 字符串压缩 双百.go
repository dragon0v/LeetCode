package main

import "strconv"

func main() {

}

func compressString(S string) string {

	// str := []byte("0123456789")
	count := len(S)
	if count <= 2 {
		return S
	}
	pre := S[0]
	preCount := 1
	newS := make([]byte, 0)
	for i := 1; i < count; i++ {
		if S[i] != pre {
			newS = append(newS, pre)
			newS = append(newS, []byte(strconv.Itoa(preCount))...)
			pre = S[i]
			preCount = 1
		} else {
			preCount++
		}
	}
	newS = append(newS, pre)
	newS = append(newS, []byte(strconv.Itoa(preCount))...)
	if len(newS) >= count {
		return S
	}

	return string(newS)

}

// 作者：kingeasternsun
// 链接：https://leetcode-cn.com/problems/compress-string-lcci/solution/0ms-31mb-by-kingeasternsun/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// 这个是可以学习的版本，和我的思路一样，只是注意了细节就简化了很多
