class Solution {
public:
    bool isPalindrome(int x) {
        long long original = x;
        long long reversed = 0;
        
        if(x>=0 && x<=9){
            return true;
        }

        else if(x<0){
            return false;
        }

        while(x>0){
            int lastdigi = x%10;
            reversed = (reversed * 10) + lastdigi;
            x/=10;                       

        }

        if(reversed == original){
            return true;
        }
        else{return false;}
    }
};