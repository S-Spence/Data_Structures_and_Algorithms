"""
Problem: Implement the class queue using stacks. The queue methods you need to implement are enqueue, dequeue, peek, and empty.
        - Enqueue adds to end
        - Dequeue removes front front
        - Peek returns value at the start of the queue
        - Empty returns a boolean of whether or not the queue is empty
        Leetcode (Easy): https://leetcode.com/problems/implement-queue-using-stacks/

Step 1: Constraints
        Do the queue methods need to perform at the same space and time complexity of a real queue? ->  No, but they should be as 
        performant as possible. 

Step 2: Tests
        Implement a class questions do not need test cases.

Step 3: Solution

Step 4: Code
"""

class Queue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.length = 0


    def enqueue(self, data):
        """Add one element to the stack. O(1) space and time"""
        self.stack_1.append(data)
        self.length += 1
        
    def dequeue(self):
        """Dequeue on element from the queue. O(n) time if we pop every value. O(n) space."""
        """ 
        Fill the second stack with elements popped from the first stack to reverse the order. Only add elements if
        the second stack is empty. 
        """
        if len(self.stack_2) == 0: 
            while len(self.stack_1) > 0:
                popped = self.stack_1.pop()
                self.stack_2.append(popped)
        # The second stack represents the order of the queue, pop to dequeue
        self.length -= 1
        if len(self.stack_2) > 0:
            return self.stack_2.pop()
    
    def empty(self):
        """Empty the queue. O(1) space and time."""
        self.stack_1 = []
        self.stack_2 = []
        self.length = 0

    def peek(self):
        """Peek the last element of the queue. O(n) space"""
        """ 
        Fill the second stack with elements popped from the first stack to reverse the order. Only add elements if
        the second stack is empty. 
        """
        if len(self.stack_2) == 0:
            while len(self.stack_1) > 0:
                popped = self.stack_1.pop()
                self.stack_2.append(popped)
        # The second stack represents the order of the queue, pop the dequeue
        if len(self.stack_2) > 0:
            return self.stack_2[-1]
        else:
            return self.stack_2

    def is_empty(self) -> bool:
        """Empty the queue. O(1) space and time."""
        if self.length == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    queue = Queue()
    
    for i in range(5):
        queue.enqueue(i+1)
    print(f"Peek Queue: {queue.peek()}")
    print(f"Queue empty? {queue.is_empty()}")
    # Dequeue
    for i in range(queue.length):
        print(queue.dequeue(), end=" ")

    print("")
    print(f"Queue empty? {queue.is_empty()}")
