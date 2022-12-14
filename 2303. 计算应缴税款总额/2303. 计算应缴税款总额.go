func calculateTax(brackets [][]int, income int) float64 {
	tax, last := 0, 0
	for _, b := range brackets {
		if b[0] <= income {
			tax += (b[0] - last) * b[1]
			last = b[0]
		} else {
			tax += (income - last) * b[1]
			break
		}
	}

	return float64(tax) / 100
}
