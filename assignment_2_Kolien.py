#open the csv file
politicians = open("politicians.csv")

#make a multidimensional list and set indext to 0
newlist = []
index = 0

#strip the csv and make it a multidimensional list
for info in politicians:
	infosplit = info.strip().split(",")
	newlist.append(infosplit)
	firstname = infosplit[0]
	lastname = infosplit[1]
	year = infosplit[2]
	party = infosplit[3]
	print(str(index) + " " + firstname + " " + lastname + " was born in " + year + " and a member of the " + party + " party.")
	index = index + 1

#close the csv file
politicians.close()

#print how many rows there are in the list
print("There are " + str(index) + " politicians in the list.")

#make a while loop to to get back everytime to the questions
while True:
	#ask what they want to do
	print("What do you want to do?")
	print("To remove a person, type a")
	print("To add a person, type b")
	print("To save the database, type c")
	print("To quit the program, type d")
	answer = input("Type here your answer: ")

	#remove a person from the list by using the indexnumber and .pop
	if answer == "a" or answer == "A":
		removeperson = input("Who do you want to remove? Type the indexnumber: ")
		newlist.pop(int(removeperson))
		print("You have deleted " + newlist[int(removeperson)][0] + " " + newlist[int(removeperson)][1])

	#add a person to the list by asking the variables and adding them to newlist by using .append
	elif answer == "b" or answer == "B":
		addfirstname = input("What is the first name? ")
		addlastname = input("What is the last name? ")
		addyear = input("Which year is he or she born? ")
		addparty = input("For which party is he or she working? ")
		newrow = [addfirstname, addlastname, addyear, addparty]
		newlist.append(newrow)

	#save the list to list to the newpoliticians csv file and quit the program.
	elif answer == "c" or answer == "C":
		index = 0
		politicians = open("politicians.csv", "w")
		for information in newlist:
			infojoin = ",".join(information) + "\n"
			politicians.write(infojoin)
			index = index + 1
		print("It is saved to politicians.csv")
		politicians.close()

	#exit the program
	elif answer == "d" or answer == "D":
		print("Goodbye")
		exit()

	#if someone typed another letter, exit the program
	else:
		exit()