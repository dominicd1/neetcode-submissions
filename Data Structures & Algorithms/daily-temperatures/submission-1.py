class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #initialize stack and output arrays

        #the stack keeps track of the next warmest day, and a pointer to it's index is on top
        stack = []
        output = [0] * (len(temperatures))
        
        #start from the right side of temperature list, so we can see ahead from the future

        i = len(temperatures)-1
        for x in range (len(temperatures)):
            count = 0

        #the first index will always have no days warmer than it, so set it to zero
        #if the stack is empty, there is no warmer days ahead, therefore the output is zero
            if (x == 0 or len(stack) == 0):
                output[i] = 0  
            
        #if the temperature in the stack is less than the current temperature, pop it off and continue until the temperature in the stack is greater than current

            while (len(stack) > 0) and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
        #empty stack means no days ahead that are warmer
            if not stack:
                output[i] = 0
        
        #otherwise, calculate the difference between the next warmer day and the current day
            else:
                output[i] = stack[-1] - i
                    
            #then, push onto the stack the current temperature
            stack.append(i)
            
            i-=1
        
        return output
            
            
            

           


            

        