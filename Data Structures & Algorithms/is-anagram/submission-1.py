class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s=dict() #to maintain frequency of characters in s
        map_t=dict() #to mainatin frequencey of characters in t
        for letter in s:
            if( letter in map_s):
                map_s[letter]+=1
            else:
                map_s[letter]=1
        for letter in t:
            if( letter in map_t):
                map_t[letter]+=1
            else:
                map_t[letter]=1
        if(map_s==map_t):
            return True
        return False
        
        