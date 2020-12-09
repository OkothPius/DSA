	
# Stack implementation using deque class in Python
 
from collections import deque
 
if __name__ == '__main__':
 
    stack = deque()
 
    print("Inserting 'A' into the stack...")
    stack.append('A')
 
    print("Inserting 'B' into the stack...")
    stack.append('B')
 
    print("Inserting 'C' into the stack...")
    stack.append('C')
 
    print("Inserting 'D' into the stack...")
    stack.append('D')
 
    print("Top element is", stack[-1])        # Prints the top of the stack('D')
 
    print("Removing", stack.pop(), "from the stack")        # removing the top ('D')
    print("Removing", stack.pop(), "from the stack")        # removing the next top ('C')
 
    # Returns the number of elements present in the stack
    print("Stack size is", len(stack))
 
    print("Removing", stack.pop(), "from the stack")        # removing the top ('B')
    print("Removing", stack.pop(), "from the stack")        # removing the next top ('A')
 
    # check if stack is empty
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")