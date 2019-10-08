class ArrayStack:
    def __init__(self):
        self.node_array = []

    def push(self, node):
        self.node_array.append(node)

    def pop(self):
        # Implement a method that replicates how pop works on a stack
        if self.size() > 0:
            return self.node_array.pop()
        else:
            return None

    def size(self):
        # Prints the size of a stack (i.e., the number of items in a stack)
        return len(self.node_array)

    def is_empty(self):
        # Checks if the stack is currently empty
        return self.size() == 0

    def display(self):
        print("\n")
        for node in range(self.size() - 1, -1, -1):
            print(self.node_array[node])
        print("\n")
