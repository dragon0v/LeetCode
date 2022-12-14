class Solution {
    public double calculateTax(int[][] brackets, int income) {
        int tax = 0;
        int last = 0;
        for (int i = 0; i < brackets.length; i++) {
            if (brackets[i][0] <= income) {
                tax += (brackets[i][0] - last) * brackets[i][1];
                last = brackets[i][0];
            } else {
                tax += (income - last) * brackets[i][1];
                break;
            }
        }

        return (double) tax / 100;
    }
}