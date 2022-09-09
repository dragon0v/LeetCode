class Solution {
    public int minOperations(String[] logs) {
        int level=0;
        for(String log:logs){
            if ("../".equals(log)) level=Math.max(level-1,0);
            else if (!"./".equals(log)) level--;
        }
        return level;
    }
}