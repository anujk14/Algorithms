# Problem:
# Given an array, find al the leaders in the array. 
# An element is leader if it is greater than all the elements to its right side.
# And the rightmost element is always a leader.

def find_leaders(arr):
	leaders_array = list()
	max_element = arr[len(arr) - 1]
	leaders_array.append(max_element)
	for num in reversed(arr):
		if num > max_element:
			max_element = num
			leaders_array.append(num)

	return leaders_array		

def main():
	num_array = list()
	num = int(input("Enter number of elements in the array\n"))

	print("Enter %d numbers:" %(num))

	for i in range(0, num):
		num_array.append(int(input()))

	leaders_array = find_leaders(num_array)

	print("The leaders of the array are: ")
	print(', '.join(str(x) for x in leaders_array))

if __name__ == "__main__":
	main()
