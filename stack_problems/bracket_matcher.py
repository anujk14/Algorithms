# Problem:
# A string is passed as input which contains the following bracket characters: '(', '{', '[', ')', '}', ']'
# Print whether the string is balanced or not
# A balanced string is one, where the open and closed brackets are placed in such a way that all opening brackets have a corresponding closing bracket
# Eg: "({})" is balanced while "({}" is not balanced since '(' does not have a corresponding closing bracket
import array_stack

def check_matching_brackets(opening_bracket, closing_bracket):
	if opening_bracket == "(" and closing_bracket == ")":
		return True
	elif opening_bracket == "{" and closing_bracket == "}":
		return True
	elif opening_bracket == "[" and closing_bracket == "]":
		return True
	else:
		return False
				
def main():
    # Use a stack in order to check the bracket balance
	brackets = array_stack.ArrayStack()
	input_string = input("Enter a string consisiting of only brackets, whose balance is to be checked\n")

	opening_bracket_list = ["{", "(", "["]
	closing_bracket_list = ["}", ")", "]"]

	print(len(input_string))

	for bracket in input_string:
		# Check balance of the input string
		if bracket in opening_bracket_list:
			brackets.push(bracket)
		elif bracket in closing_bracket_list:
			if brackets.is_empty():
				print("imbalanced")
				return
			elif check_matching_brackets(brackets.pop(), bracket) == False:
				print("imbalanced")
				return		
  	
	if brackets.is_empty() == True:
		print("balanced")
	else:
		print("imbalanced")	
        	
if __name__ == "__main__":
    main()
