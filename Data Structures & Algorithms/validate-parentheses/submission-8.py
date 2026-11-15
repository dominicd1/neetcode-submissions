class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = True
        for c in s:
            if(c =='(' or c =='[' or c =='{'):
                stack.append(c)

            elif (c ==')' or c ==']' or c =='}'):
                if (len(stack) <= 0):
                    return False

                s_index = len(stack)-1
                
                match c:
                    case ')':
                        if (stack[s_index] != '('):
                            return False
                            
                    case ']':
                        if (stack[s_index] != '['):
                            return False
                    case '}':
                        if (stack[s_index] != '{'):
                            return False

                stack.pop(s_index)

            

            print (c)
            print (stack)
        
        if not stack:
            return True
        else:
            return False
                
            

