class Solution:
    def isPalindrome(self, s: str) -> bool:
        #python shortcut method will not work with special characters
        words=[]
        for char in s:
            if(char.isalnum()==True):
                words.append(char.lower()) #only add characters
        #check whether it is a palindrome 
        string="".join(words)
        print(string)
        reverse=string[::-1]
        if(string==reverse):
            return True
        return False
         
        