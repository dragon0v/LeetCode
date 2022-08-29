package main

func main() {

}
func isMonotonic(A []int) bool {
	if len(A) == 1 {
		return true
	}
	f := "="
	for i := 0; i < len(A)-1; i++ {

		if A[i] > A[i+1] {
			if f == "<" {
				return false
			}
			f = ">"
		}
		if A[i] < A[i+1] {
			if f == ">" {
				return false
			}
			f = "<"
		}
	}
	return true
}
