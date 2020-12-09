"""Custom stack implemention in python"""
class Stack:

    """Constructor to initialize stack."""
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    """Function to add an element to stack."""  
    def push(self, x):
        if self.isFull():
            print("Stack OverFlow!! Calling exit()...")  
            exit(1)

        print("Inserting", x, "into the stack...")
        self.top = self.top + 1
        self.arr[self.top] = x

    """Function to delete an element from the stack."""
    def pop(self):
        #check for stack underflow
        if self.isEmpty():
            print("Stack UnderFlow!! Calling exit()...")
            exit(1)

        print("Removing", self.peek(), "from the stack")

        #decrease the stack by 1 and (optionally) return the popped element
        top = self.arr[self.top]
        self.top = self.top - 1
        return top

    """Function to return the top element on to the stack"""
    def peek(self):
        if self.isEmpty:
            exit(1)
        return self.arr[self.top]  
            
    """Function to return the size top of the stack."""
    def size(self):
        return self.top + 1

    """Function to check if the stack is empty or not."""
    def isEmpty(self):
        return self.size() == 0

    """Function that check if the stack is full or not."""
    def isFull(self):
        return self.size() == self.capacity


if __name__ == "__main__":
    
    stack = Stack(3)

    stack.push(1)  #Inserting 1 into the stack
    stack.push(2)  #Inserting 2 into the stack

    stack.pop()   #Remove 2 from the stack
    stack.pop()   #Remove 1 from the stack  

    stack.push(3)   #Inserting 3 into the stack 

    print("Top Element is ", stack.peek())
    print("Stack size is ", stack.size())

    stack.pop()    #Remove 3 from the stack    

    #check if stack is empty
    if stack.isEmpty():
        print("Stack Is Empty")
    else:
        print("Stack Is Not Empty")                          
