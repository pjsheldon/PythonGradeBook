'''--------By: PJ Sheldon---------
	--------Date: 8/2/20---------
	hwk4.py programming assignment 4
	SEC-290 Wilmington University'''


# Menu 1 thru 4 for the while loop
menu = """
1: Exit
2: List score so far 
3: Add a score
4: Display the highest and lowest scores
"""

# The initial list 
num = [85.3, 85.2, 21.99]

done = False # While loop variable.

while not done: # While loop is always true by making the variable false and saying not always makes the loop true
	print("Scoring Engine") # program title
	print() # spacing
	print(menu)
	selection = input("please make a selection between 1 and 4: ") # input for menu
	print()

	if selection == "1": # the exit selection
		done = True # variable is oppistie of while loop statement making the while loop false and claosing it
		print('Good bye!')
		print('Thanks for Playing!')  # exit messaging.

	elif selection == "2": # list the scores highest to lowest.
		print("List scores so far: ") # title for section
		print()

		num.sort(reverse=True, key=float) # sort mathod in reverse with key of flost function

		for i in range(len(num)): # uses the index function for as many entries as needed. 
			print('      {:.2f}'.format(num[i])) # formating for the float and sort method to be displayed 
			print()
			
	elif selection == "3": # Slection 3 user input
		numinput = float(input('Please enter a score between 0 and 100: ')) # input question is also a float number
		
		if float(numinput) >= 0.0 and float(numinput) <= 100.0: # float between statement to for secure software
			num.append(numinput)
			num.sort(reverse=True, key=float) # make sure the new entry is sorted in the list properly
			print()
			print('Added {:.2f} to the list'.format(numinput)) # information to verify added to the list to user.
			print()
		else:
			print()
			print('Please Pick a number that is between 0.0 and 100.0') # make sure the correct information is entered
			print()

	elif selection == "4": # last section for hist number and lowest number
		print("Display the highest and lowest scores-") # title of section
		print()

		print('The highest number is: {:.2f}, the lowest number is: {:.2f}'.format(num[0], num[-1])) # formatted for decimals and used index numbers to show the and last in the list.
		print()

	else:
		print("Please select 1, 2, or 3") # if the wrong menu number is entered.