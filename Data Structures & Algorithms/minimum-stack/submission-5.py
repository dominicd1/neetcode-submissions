class MinStack:


    def __init__(self):
        self.topstack = -1
        self.stack = []
        self.minstack = []
        self.minstack_top = -1

        

    def push(self, val: int) -> None:

        self.stack.append(val)
        self.topstack += 1
        if (len(self.minstack) > 0):
            if (val <= self.minstack[self.minstack_top]):
                self.minstack.append(val)
                self.minstack_top += 1
        else:
            self.minstack.append(val)
            self.minstack_top += 1

        # print(self.minstack)
        # print(self.minstack_top)
       
        

    def pop(self) -> None:
        if (self.minstack[self.minstack_top] == self.stack[self.topstack]):
            self.minstack.pop(self.minstack_top)
            self.minstack_top -= 1

        self.stack.pop(self.topstack)
        self.topstack -= 1

       
        

    def top(self) -> int:
        return self.stack[self.topstack]
        

    def getMin(self) -> int:
        return self.minstack[self.minstack_top]
        
        
