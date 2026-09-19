class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we will maintain hashmap for each string 
        mp1=dict()
        mp2=dict() #two hashmaps to maintain frequency 
        
        #traversing string s
        for char in s:
            if(char in mp1):
                mp1[char]+=1 #increase the freq
            else:
                mp1[char]=1 #first time we saw
        #traversing string t
        for char in t:
            if(char in mp2):
                mp2[char]+=1 #increase the freq
            else:
                mp2[char]=1
        #compare both the hashmaps 
        if(mp1==mp2):
            return True
        return False