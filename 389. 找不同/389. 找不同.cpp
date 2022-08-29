#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <time.h>
using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        int l[26];
        for (int i = 0; i < s.length(); i++)
        {
            l[s[i]-'a'] ++;
        }
        for (int i = 0; i < t.length(); i++)
        {
            l[t[i]-'a'] --;
            if(l[t[i]-'a'] == -1){
                return t[i];
            }
        }
        return 'a';
    }
};

int main(int argc, const char** argv) {
    Solution s;
    printf("%c",s.findTheDifference("a","ar"));
    return 0;
}





