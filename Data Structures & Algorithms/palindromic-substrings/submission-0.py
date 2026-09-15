class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s) #number of characters
        count=n #initialise (each individual character is def a palindrome)
        #compute all substrings 
        for i in range(0,n,1):
            for j in range(i+1,n,1):
                sub=s[i:j+1] #extract the substring 
                reverse=sub[::-1] #reverse the substring 
                if(sub==reverse):
                    count+=1
        return count
        