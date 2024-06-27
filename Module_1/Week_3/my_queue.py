class Myqueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.count = 0
        self.queue = []
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False
    def is_full(self):
        if self.count == self.capacity:
            return True
        else:
            return False
    def dequeue(self):
        if self.count == 0:
            raise RuntimeError("Queue underflow")
        else:
            element = self.queue[0]
            del self.queue[0]
            self.count -= 1
            return element
    def enqueue(self,value):
        if self.count == self.capacity:
            raise RuntimeError("Queue overfloww")
        else:
            self.queue.insert(len(self.queue),value)
            self.count += 1
    def front(self):
        return self.queue[0]
    def get_queue(self):
        return self.queue
    
if __name__ == '__main__':
    queue = Myqueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.get_queue())
    print(queue.is_full())
    print(queue.front())
    print(queue.dequeue())
    print(queue.front())
    print(queue.dequeue())
    print(queue.is_empty())