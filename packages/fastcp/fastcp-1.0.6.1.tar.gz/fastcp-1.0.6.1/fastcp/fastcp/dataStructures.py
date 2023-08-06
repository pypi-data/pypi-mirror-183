from queue import *

global _val; 
_val = 10**100;

def info():
    """
    Contents of this Package:
        - minHeap
        - maxHeap
        - queue
        - PriorityQueue
        - SimpleQueue
        - Stack (O(1) Insertion and Deletion)
        ** along with all functions in : https://docs.python.org/3/library/queue.html
    """

class maxHeap:
    """
        Max Heap: returns the maximum value available in the heap 
                  when ever get() method is called.
        Methods:
            - get() - returns the maximum value available in the heap (carefull)
            - put(value) - inserts the value into the heap
            - size() - returns the size of the heap
            - empty() - returns True if the heap is empty else False
            - full() - returns True if the heap is full else False
            ** get() can return an error if the heap is empty!
        Complexity: O(log N)
    
    """
    def __init__(self):
        self.heap = PriorityQueue();
    
    def get(self) -> any:
        """
        Returns the Maximum value available in the heap
        ** returns Error if the heap is empty **

        Raises:
            Exception: HeapEmpty

        Returns:
            any: Returns the Maximum value available in the heap
        """
        if self.heap.empty():
            raise Exception("Heap is empty!")
        return _val - self.heap.get();

    def put(self, value) -> None:
        """
        Args:
            value (any): Inserts data into Min Heap
            Returns: None
        """
        self.heap.put(_val - value);

    def empty(self) -> bool:
        """
        returns True if the Heap is Empty else False
        
        Returns:
            bool: True/False
        """
        return self.heap.empty();
    
    def full(self) -> bool:
        """
        returns True if the Heap is Full else False
        
        Returns:
            bool: True/False
        """
        return self.heap.full();

    def size(self) -> int:
        """
        returns the size of the Heap
        
        Returns:
            int: the size of the Heap
        """
        return self.heap.qsize();


class minHeap:
    """
        Min Heap: returns the minimum value available in the heap 
                  when ever get() method is called.
        Methods:
            - get() - returns the minimum value available in the heap (carefull)
            - put(value) - inserts the value into the heap
            - size() - returns the size of the heap
            - empty() - returns True if the heap is empty else False
            - full() - returns True if the heap is full else False
            ** get() can return an error if the heap is empty!
        Complexity: O(log N)
    """
    def __init__(self) -> any:
        self.heap = PriorityQueue();
    
    def get(self) -> any:
        """
        Returns the minimum value available in the heap
        ** returns Error if the heap is empty **

        Raises:
            Exception: HeapEmpty

        Returns:
            any: Returns the minimum value available in the heap
        """
        if self.heap.empty():
            raise Exception("Heap is empty!")
        return self.heap.get();

    def put(self, value) -> None:
        """
        Args:
            value (any): Inserts data into Min Heap
            Returns: None
        """
        self.heap.put(value);
    
    def empty(self) -> bool:
        """
        returns True if the Heap is Empty else False
        
        Returns:
            bool: True/False
        """
        return self.heap.empty();
    
    def full(self) -> bool:
        """
        returns True if the Heap is Full else False
        
        Returns:
            bool: True/False
        """
        return self.heap.full();

    def size(self) -> int:
        """
        returns the size of the Heap
        
        Returns:
            int: the size of the Heap
        """
        return self.heap.qsize();
    
class Stack:
    """
    Stack follows the Principle of 'Last In First Out'
    
    Methods:
        - push(value)
        - pop()
        - size()
    **Every method works in O(1) Complexity**
    
    """
    
    def __init__(self):
        self.stack = []; self.top = -1;
        
    def push(self, value) -> None:
        """
        Insert value into Stack

        Args:
            value (any): value to insert into the stack
        """
        self.stack.append(value); self.top += 1;
    
    def pop(self) -> any:
        """
        Returns the top most element in stack
        ** Returns None if Stack is empty**

        Returns:
            any: Top most element in Stack
        """
        if self.top == -1: return None;
        return self.stack.pop(); self.top -= 1;
    
    def size(self) -> int:
        """Returns the Size of Stacks

        Returns:
            int: size of Stack
        """
        return self.top + 1;
    