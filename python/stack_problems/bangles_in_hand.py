# Problem:
# Simulation of wearing, removing, counting and printing colours of bangles on a hand
import array_stack


def main():
    # We perform bangle wearing and removing operations on this hand
    hand = array_stack.ArrayStack()

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


if __name__ == "__main__":
    main()
