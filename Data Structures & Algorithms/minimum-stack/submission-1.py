class MinStack:
    #top element of the min stack keeps track of minimum element

    def __init__(self):
        self.stack=[] #normal stack
        self.minstack=[] #stack to keep track of the minimum element
        

    def push(self, val: int) -> None:
        self.stack.append(val) #pushing element onto normal stack 
        if(len(self.minstack)==0 or val<=self.minstack[-1]):
            #either minstack os empty or the current value is smaller than the top element of minstack 
            self.minstack.append(val) #New minimum
        

    def pop(self) -> None:
        if(self.stack[-1]==self.minstack[-1]):
            #if we are removing the min element, we need to remove it from min stack also 
            self.minstack.pop()
        self.stack.pop() #if not min element just remove from normal
        

    def top(self) -> int:
        return self.stack[-1] #top element on stack 
        

    def getMin(self) -> int:
        return self.minstack[-1] #top element of minstaack is the minimum element
        
