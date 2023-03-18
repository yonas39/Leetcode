class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        S=s.lower() #convert to lowercase
        new_s =""   
        for char in S:
            #check if the number is alpha numeric--> alphabet or numbers only using inbuilt library isalnum()
            if char.isalnum(): 
                new_s+=char.lower()
                
        return new_s == new_s[::-1] #compare the string with its inverse after extra char is removed 
      
      
      
      
      
      
   
