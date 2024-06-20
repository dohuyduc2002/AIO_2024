class MyStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = []
        self.count = 0
    def is_empty(self):
        if self.stack == []:
            return True
    def is_full(self):
        if self.count == self.capacity:
            return True
        else:
            return False
    def pop(self):
        if self.count == 0:
            raise RuntimeError("Stack underfloww")
        else:
            last_item = self.stack[-1]
            del self.stack[-1]
            self.count -= 1
            return last_item
    def push(self,value):
        if self.count == self.capacity:
            raise RuntimeError("Stack overflow")
        self.stack.append(value)
        self.count += 1
    def top(self):
        return self.stack[-1]
    def get_stack(self):
        return self.stack
    
if __name__ == '__main__':
    stack = MyStack(5)
    stack.push(1)
    stack.push(2)
    print(stack.get_stack())
    print(stack.is_full())
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.is_empty())
        