public class palindrome {
    public boolean isPalindrome(int x) {
        int copy=x;
        int s,rev=0;
     if(x<=-1)
         return(false);
        else
            while(x !=0 )
            {
                s=x%10;
        rev=rev*10+s;
        x=x/10;
            }
        if(copy == rev)
        return(true);
        else
            return(false);
    }
}
