class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_stack = []
        top = -1
        operand_stack = []
        on = 0

        for s in tokens:
            if (s.isalnum() or (s[0] == '-' and len(s) > 1)):
                operand_stack.append(int(s))
                top += 1
            
                
            
            else:
                match s:
                    case '+':
                        operand_stack.append(operand_stack[top] + operand_stack[top-1])
                    case '*':
                        operand_stack.append(operand_stack[top] * operand_stack[top-1])
                    case '-':
                        operand_stack.append(operand_stack[top-1] - operand_stack[top])
                    case '/':
                        operand_stack.append(int(operand_stack[top-1] / operand_stack[top]))
                        
                operand_stack.pop(top)
                operand_stack.pop(top-1)
                top -= 1

            # print(s)
            # print(operand_stack)
            

        return operand_stack[0]