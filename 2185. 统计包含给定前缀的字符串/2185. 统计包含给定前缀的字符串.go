func prefixCount(words []string, pref string) int {
	ans := 0
	for _, word := range words {
		if strings.HasPrefix(word, pref) {
			ans++
		}
	}
	return ans
}
