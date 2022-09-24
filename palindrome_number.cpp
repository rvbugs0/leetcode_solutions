class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        {
            return false;
        }
        int copyX = x;
        long reversedInteger =0;
        
        while(x>0)
        {
            reversedInteger = reversedInteger*10+ x%10;
            x=x/10;
        }
        if(reversedInteger==copyX)
        {
            return true;
        }
        return false;
        
    }
};