# Problem:
# A string is passed as input which contains the following bracket characters: '(', '{', '[', ')', '}', ']'
# Print whether the string is balanced or not
# A balanced string is one, where the open and closed brackets are placed in such a way that all opening brackets have a corresponding closing bracket
# Eg: "({})" is balanced while "({}" is not balanced since '(' does not have a corresponding closing bracket
import array_stack


def main():
    # Use a stack in order to check the bracket balance
    brackets = array_stack.ArrayStack()
    input_string = input("Enter a string consisiting of only brackets, whose balance is to be checked\n")

    for bracket in input_string:
        # Check balance of the input string


if __name__ == "__main__":
    main()
