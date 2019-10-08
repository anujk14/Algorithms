# Problem:
# Given an array consisting of both negative and positive numbers, find out the largest contigious sum possible from the array.
# Contiguous refers to those elements which are are right next to each other(touching borders)
# The constraint is that there WILL AT LEAST BE ONE POSITIVE NUMBER in the array


def find_largest_contiguous_sum(arr):
	current_max_sum = 0
	final_max_sum = 0
	start = 0
	end = 0
	s = 0
	for i in range(0, len(arr)):
		current_max_sum += arr[i]
		if current_max_sum < 0:
			current_max_sum = 0	
			s = i + 1
		elif final_max_sum < current_max_sum:
			final_max_sum = current_max_sum
			start = s
			end = i
	print("start is %d" %(start))
	print("end is %d" %(end))		
		
	return final_max_sum

def main():
    num = int(input("Enter number of elements in the array\n"))
    print("Enter %d numbers:" %(num))

    arr = []

    for i in range(0, num):
        arr.append(int(input()))

    sum = find_largest_contiguous_sum(arr)

    print("The largest contiguous sum is %d" %(sum))

if __name__ == "__main__":
    main()
