import os

array = ["", "", "", "", "", "", "", "", "", ""]  # array of set size of 10
x = 0  # the pointer for the array is x, set at the begining 0


def view():
	print(array)  # prints entire array


def add():
	global x
	while (
	  x <= 9
	):  # proceeds to add only if the pointer isnt at the end of the array, so no values are added if the list is full
		addValue = input("Enter the value to add to the list: ")
		array[x] = addValue  # changes the pointer empty space to the inputed value
		x += 1  # the pointer moves up to the next empty space
		break
	else:
		print(
		 "The list is full"
		)  # if the pointer is at the end of the array then the list is full and nothing gets added


def remove():
	global x
	while (
	  x >=
	  1):  # only proceeds to remove if the pointer isnt at the end of the array
		print("Your value has been removed")
		array[
		 x -
		 1] = ""  # the value behind the pointer, which is the last index in the array with a value in it, is removed/ replaced with ""
		x -= 1  # the pointer goes back to the empty space that has just been created
		break
	else:
		print(
		 "There is nothing in the list to remove"
		)  # if the pointer is at the first index in the array then the list is empty and nothing gets removed


def quit():
	exit


def main():
	while True:
		print("1. View")
		print("2. Add")
		print("3. Remove")
		print("4. Quit")
		choice = int(input("\n"))
		os.system("clear")
		if choice == 1:
			view()
		elif choice == 2:
			add()
		elif choice == 3:
			remove()
		elif choice == 4:
			quit()


main()
