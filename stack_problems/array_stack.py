class ArrayStack:
    def __init__(self):
        self.bangles = []

    def push(self, bangle_colour="red"):
        self.bangles.append(bangle_colour)

    def pop(self):
        # Implement a method that replicates how pop works on a stack
        if self.size() > 0:
            return self.bangles.pop()
        else:
            return None

    def size(self):
        # Prints the size of a stack (i.e., the number of items in a stack)
        return len(self.bangles)

    def is_empty(self):
        # Checks if the stack is currently empty
        return self.size == 0

    def display(self):
        print("\n")
        for node in range(self.size() - 1, -1, -1):
            print(self.bangles[node])
        print("\n")
