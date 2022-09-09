func minOperations(logs []string) int {
	level := 0
	for _, log := range logs {
		if log=="../" && level>0{
			level--
		}else if log!="./" && log!="../"{
			level++
		}
	}
	return level
}