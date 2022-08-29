package main

func main() {

}

func countSegments(s string) int {
	if len(s) == 0 {
		return 0
	}
	curr := 0  //当前单词的长度
	count := 0 //单词数
	for _, c := range s {
		if c != ' ' {
			curr++
		} else {
			if curr != 0 {
				count++
			}
			curr = 0
		}
	}
	if curr != 0 {
		count++
	}
	return count
}
