package main

import "fmt"

func main() {
    fmt.Println()
}

func reverseBits(n uint32) (rev uint32) {
    for i := 0; i < 32 && n > 0; i++ {
        // 逐位颠倒，n&1取n最低位，左移31-i，表示把该位放到它对应的位置上
        rev |= n & 1 << (31 - i)
        // n右移1位，保证最低位为要枚举的比特位
        n >>= 1
    }
    return
}

// 有提前终止所以复杂度Ologn

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode-solu-yhxz/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。