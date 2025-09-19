# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None #reference to the top node
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node.next
        node.next = None
        return node.value
    def peek(self):
        return None if self.top is None else self.top.value
    def is_empty(self):
        return self.top is None
    def print_stack(self):
        if self.top is None:
            print("(empty)")
            return
        cur = self.top
        while cur:
            print(f"- {cur.value}")
            cur = cur.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack() #resets redo stack

            print(f"Action performed: {action}")
        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            val = undo_stack.pop()
            if val is None: 
                print("No actions to undo.")
            else: 
                redo_stack.push(val)
                print(f"Undid action: {val}")
            

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            val = redo_stack.pop()
            if val is None:
                print("No actions to redo.")
            else:
                undo_stack.push(val)
                print(f"Redid action: {val}")


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()