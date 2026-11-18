class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_stack = []
        top = -1
        operand_stack = []
        on = 0

        for s in tokens:

            #if its alphanumeric, add to stack after converting to int
            if (s.isalnum() or (s[0] == '-' and len(s) > 1)):
                operand_stack.append(int(s))
                top += 1
            
                
            else:
            
            #if the character is an operator, perform the operation on the top two elements in the stack
            #append the result to the stack to be used for further operations later
                match s:
                    case '+':
                        operand_stack.append(operand_stack[top] + operand_stack[top-1])
                    case '*':
                        operand_stack.append(operand_stack[top] * operand_stack[top-1])
                    case '-':
                        operand_stack.append(operand_stack[top-1] - operand_stack[top])
                    case '/':
                        operand_stack.append(int(operand_stack[top-1] / operand_stack[top]))

            # pop the original top two from the stack (the numbers the operation was performed on )
            #decrease the stack pointer
                        
                operand_stack.pop(top)
                operand_stack.pop(top-1)
                top -= 1

           
            

        return operand_stack[0]