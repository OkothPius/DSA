package DSA;

public class Stack {
    static class MyStack {
        private int[] arr;
        private int top;
        private int capacity;

        //constructor to initialize stack
        MyStack(int size) {
            this.arr = new int[size];
            this.capacity = size;
            this.top = -1;
        }

        /**Method to add an element onto the stack*/
        private void push(int x) {
            if (isFull()) {
                StdOut.println("Overflow\nProgram Terminated\n");
                System.exit(1);
            }
            StdOut.println("Inserting " + x);
            arr[++top] = x;
        }

        /**Method to delete top element from a stack*/
        private void pop() {
            //check for stack underflow
            if (isEmpty()) {
                StdOut.println("Underflow\nProgram Terminated\n");
                System.exit(1);
            }
            StdOut.println("Removing " + peek());
            //decrease the stack size by 1 and (optionally) return the popped element
            top--;
        }

        /**Method to return the top element in a stack*/
        private int peek() {
            if (!isEmpty())
                return arr[top];
            else
                System.exit(1);

            return -1;
        }

        /**Method to return the size of the stack*/
        private int size() {
            return top + 1;
        }

        /**Method to check if the stack is empty or not*/
        private boolean isEmpty() {
            return top == -1;   // or return size() == 0
        }

        /**Method to check if the stack is full or not*/
        private boolean isFull() {
            return top == capacity -1;   // or return size() == capacity
        }

        /**Main Method*/
        public static void main(String[] args) {
            MyStack myStack = new MyStack(3);
            myStack.push(1);   //Inserting 1 into the stack
            myStack.push(2);   //Inserting 2 into the stack

            myStack.pop();        //Removing the top 2
            myStack.pop();        //Removing the top 1

            myStack.push(3);  //Inserting 3 into the stack

            StdOut.println("Top element is: " + myStack.peek());
            StdOut.println("Stack size is: " + myStack.size());

            myStack.pop();      //Removing the top 3

            //check if stack is empty
            if (myStack.isEmpty())
                StdOut.println("Stack Is Empty");
            else
                StdOut.println("Stack Is Not Empty");
        }

    }
}


