package main

import "fmt"

func isPalindrome(x int) bool {
	if x<0 {
		return false
	}else{
		x2 := x
		res := 0
		for i:=0;i<=100000;i++{ //for实现的while(true)
			a := x%10 //个位
			res = res*10 +a
			x = int(x/10) //整除
			if(x==0){
				break
			}
		}
		return x2==res
	}
}

func main() {
	fmt.Println(isPalindrome(15451))
}
