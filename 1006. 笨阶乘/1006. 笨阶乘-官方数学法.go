func clumsy(N int) (ans int) {
    switch {
    case N == 1:
        return 1
    case N == 2:
        return 2
    case N == 3:
        return 6
    case N == 4:
        return 7

    case N%4 == 0:
        return N + 1
    case N%4 <= 2:
        return N + 2
    default:
        return N - 1
    }
}

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/clumsy-factorial/solution/ben-jie-cheng-by-leetcode-solution-deh2/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。