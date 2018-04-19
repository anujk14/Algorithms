# Problem:
# Simulation of wearing, removing, counting and printing colours of bangles on a hand

class Stack:
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

    def isEmpty(self):
        # Checks if the stack is currently empty
        return self.size == 0

    def display(self):
        print("\n")
        for node in range(self.size() - 1, -1, -1):
            print(self.bangles[node])
        print("\n")


def main():
    # We perform bangle wearing and removing operations on this hand
    hand = Stack()

    iterations = int(input("Enter the number of operations you want to perform\n"))
    for num in range(0, iterations):
        print("Enter the operation you want to perform:\n")
        operation = int(input("1) Wear a bangle\n2) Remove a bangle\n3) Count the number of bangles currently on your hand\n"))

        if operation == 1:
            # Wear a bangle
            color_input = input("Enter colour\n")
            hand.push(color_input)
            hand.display()
        elif operation == 2:
            # Remove a bangle
            print(hand.pop())
            hand.display()
        elif operation == 3:
            # Count number of bangles
            print(hand.size())
            hand.display()
        else:
            print("Whoops! Not sure what you meant there. Bye bye!")
            exit(0)


main()
