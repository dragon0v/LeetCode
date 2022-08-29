package main

import "fmt"

func isPowerOfTwo(n int) bool {
	if(n<=0){
		return false
	}
	for i := 0; i < 1<<31; i++ {
		if(n==1){
			return true
		}
		if(n%10 == 1 || n%10 == 3 || n%10 == 5 || n%10 == 7 || n%10 == 9){
			return false
		}
		n = n/2
	}
	return false
}

func main(){
	fmt.Println(isPowerOfTwo(11))
	// fmt.Println(1<<31)
}