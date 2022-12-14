class Solution {
    public double calculateTax(int[][] brackets, int income) {
        int tax = 0;
        int last = 0;
        for (int[] b : brackets) {
            if (b[0] <= income) {
                tax += (b[0] - last) * b[1];
                last = b[0];
            } else {
                tax += (income - last) * b[1];
                break;
            }
        }

        return (double) tax / 100;
    }
}