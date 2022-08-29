package main

func main() {

}

func findLucky(arr []int) int {
	freq := [502]int{}
	for i := 0; i < len(arr); i++ {
		freq[arr[i]]++
	}
	for i := 501; i > 0; i-- {
		if freq[i] == i {
			return i
		}
	}
	return -1

}
