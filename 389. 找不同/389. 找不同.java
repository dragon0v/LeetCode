



class Solution {
    public char findTheDifference(String s, String t) {
        int[] l = new int[26];
        for (int i = 0; i < s.length(); i++) {
            l[(byte)s.charAt(i)-(byte)'a'] ++;
        }
        for (int i = 0; i < t.length(); i++) {
            l[(byte)t.charAt(i)-(byte)'a'] --;
            if(l[(byte)t.charAt(i)-(byte)'a']==-1){
                return t.charAt(i);
            }

        }
        return 'a';
    }
}
