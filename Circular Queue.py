import os,sys

array = ["","","","","","","","","",""] #array of set size 10
x = 0 #back pointer
y = 0 #front pointer

def view(): #prints the entire array
	print(array)

def add():
	global x,y
	while (x <= 9): # proceeds to add only if the pointer isnt at the end of the array, so no values are added if the list is full
		addValue = input("Enter the value to add to the list: ")
		array[x] = addValue # changes the pointer empty space to the inputed value
		x += 1 # the pointer moves up to the next empty space
		break
	else:
		print("The list is full") # if the pointer is at the end of the array then the list is full and nothing gets added
		x = 0

def remove():
	global x,y
	if y > 9:
		y = 0
	while (x != y): # only proceeds to remove if the front pointer isnt at the same position as the back pointer
		print("Your value has been removed")
		array[y] = "" # the value behind the pointer, which is the last index in the array with a value in it, is removed/ replaced with ""
		y += 1 # the pointer goes back to the empty space that has just been created
		break
	else:
		print("There is nothing in the list to remove") # if the pointer is at the first index in the array then the list is empty and nothing gets removed


def quit():
	sys.exit()

def main():
	while True:
		print("1. View\n2. Add\n3. Remove\n4. Quit")
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
