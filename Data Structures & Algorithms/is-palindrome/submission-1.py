class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        print (j)
        for x in range(len(s)):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            elif not s[j].isalnum() and s[i].isalnum():
                j -= 1
            else:
                i += 1
                j -= 1

        return True
            
                

        