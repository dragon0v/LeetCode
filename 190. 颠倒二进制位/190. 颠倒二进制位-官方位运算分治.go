package main

import "fmt"

func main() {
    fmt.Println()
}

const (
    m1 = 0x55555555 // 01010101010101010101010101010101
    m2 = 0x33333333 // 00110011001100110011001100110011
    m4 = 0x0f0f0f0f // 00001111000011110000111100001111
    m8 = 0x00ff00ff // 00000000111111110000000011111111
)

func reverseBits(n uint32) uint32 {
    n = n>>1&m1 | n&m1<<1
    n = n>>2&m2 | n&m2<<2
    n = n>>4&m4 | n&m4<<4
    n = n>>8&m8 | n&m8<<8
    return n>>16 | n<<16
}
// 若要翻转一个二进制串，可以将其均分成左右两部分，
// 对每部分递归执行翻转操作，然后将左半部分拼在右半部分的后面，即完成了翻转。

// 由于左右两部分的计算方式是相似的，利用位掩码和位移运算，我们可以自底向上地完成这一分治流程。

// 对于递归的最底层，我们需要交换所有奇偶位：

// 取出所有奇数位和偶数位；
// 将奇数位移到偶数位上，偶数位移到奇数位上。
// 类似地，对于倒数第二层，每两位分一组，按组号取出所有奇数组和偶数组，
// 然后将奇数组移到偶数组上，偶数组移到奇数组上。以此类推。

// 时间空间O1

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode-solu-yhxz/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。