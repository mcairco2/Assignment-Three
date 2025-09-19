# Import the Node class you created in node.py
from node import Node
print("DEBUG: Using Node Class from:", Node)

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None #first in line
        self.rear = None #last in line
    def enqueue(self, value):
        #adds a new customer to the end of the queue
        new_node = Node(value)
        if self.rear is None:
            #queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        #removes and returns the next customer in line
        if self.front is None:
            return None
        node = self.front
        self.front = node.next
        if self.front is None: #queue became empty
            self.rear = None
        node.next = None
        return node.value
    def peek(self):
        #returns the next customer without removing them
        return None if self.front is None else self.front.value
    def is_empty(self):
        return self.front is None
    def print_queue(self):
        #displays all customers currently waiting
        if self.front is None:
            print("(no waiting customers)")
            return
        cur = self.front
        while cur:
            print(f"- {cur.value}")
            cur = cur.next


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped = queue.dequeue()
            if helped is None:
                print(f"No customers to help.")
            else:
                print(f"Helped: {helped}")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            nxt = queue.peek()
            if nxt is None:
                print("Next customer: (none)")
            else: 
                print(f"Next customer: {nxt}")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

#Design Memo Response
#   - A stack is the correct choice for undo/redo because it enforces LIFO ordering. 
#   
#   - User edits are naturally reversed in the opposite order from which they were made:
#   the most recent edit should be the first to be undone. Using one stack to record performed actions
#   and another to store undone actions supports both undo and redo workflows: popping an action from
#   the undo stack and pushing it onto the redo stack reverses hte user's most recent action, and reapplying
#   that action pops it from redo back onto undo.
#
#   - A queue is better suited for the help desk ebcause it enforces FIFO ordering. Tickets must be handled 
#   in the order they arrive to preserve fairness; the earliest-arriving customer should be served first. A 
#   queue with 'enqueue' adding to the rear and 'dequeue' removing from the front naturally model that real
#   world line behavior.
#
#   - Difference from Python lists:
#       My implementations use linked nodes rather than Python lists. Linked structures provide a 0(1) time
#       for push/pop at the head (stack) and 0(1) enqueue/dequeue when maintaining both front and rear (queue).
#       Python's list is backed by a dynamic array, which gives 0(1) amortized append and pop from the end but 0(n)
#       operations for insertions/removals at the front. Also, lists expose random access by index, which is 
#       unnecessary for a pure stack/queue abstraction and can encourage usage patterns that violate the intended
#       access order. The linked implementations make the intended access patterns explicit, simple, and efficient 
#       for head/rear operations.
#