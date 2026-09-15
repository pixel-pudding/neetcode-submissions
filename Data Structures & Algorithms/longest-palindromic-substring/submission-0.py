class Solution:
    def longestPalindrome(self, s: str) -> str:
    #find all palindromic substrings and check whether they have the longest length 
        length=0 #length of palindromic substring 
        maxsub=s[0] #max palindromic length substring
        maxlength=0 #max length
        n=len(s)
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                sub=s[i:j+1] #extract the substring 
                reverse=sub[::-1] #reverse the substring 
                if(sub==reverse):
                    #the substring is a palindrome 
                    length=len(sub) #get the length of the palidromic substr
                    if(length>maxlength):
                        maxlength=length #if it has the max length
                        maxsub=sub #update
                        
        return maxsub