#Welcome statement
print("Welcome to this program")

#Ask for first name, make the name with a capital and wihtout space around it
#and print a welcome statement with the firstname.
firstname = input("What is your first name?")
firstname = firstname.title().strip()
print("Welcome " + firstname + ", welcome to my program")

#making a variable for my lastname
mylastname = "Pleijsant"

#ask for their lastname and make the first letter a capital letter and without space
lastname = input("What is your last name?")
lastname = lastname.title().strip()

#testing if it is family from me
if lastname == mylastname:
    print ("We are family " + firstname + " " + lastname + "!")
else: 
    print ("Welcome " + firstname + " " + lastname + ", we are not family but you are still welcome!")

#import current year and make it a integer
from datetime import date
currentyear = date.today().year
currentyear = int(currentyear)

#asking for their year of birth and make it a integer
yearofbirth = input("What is the year you are born in?")
yearofbirth = int(yearofbirth)

#calculating their age
age = currentyear - yearofbirth

#is the user older than 18? If not, they get a warning and exit the program.
import warnings
if age >= 18:
    print("You are 18+, welcome!")
else:
    warnings.warn("WARNING! You are under 18. This website is for 18+goodbye!")
    exit()

#POITNING SYSTEM
#Give 10 points for being female
gender = input("What is your gender? f for female, m for male, x for gender neutral")

if gender == "f" or "F":
    count = 10
elif gender == "x" or "X":
	count = 5
else:
	count = 0

#counting characters in firstname and lastname and adding up to the variable count
count = len(firstname) + count
count = len(lastname) + count

#adding age to the couting
count = count + age

#Giving points for their hometown
hometown = input("In which city do you live?")
hometown = hometown.title().strip()

if hometown == "Utrecht" or "Utreg":
	print("That is a cool city!")
	count = count + 40
elif hometown == "Baarn":
	print("Nice place to live in.")
	count = count + 20
elif hometown == "Groningen":
	print("Is it cold in the north?")
	count = count +10
elif hometown == "Rotterdam":
	print("That is a big city")
	count = count + 5
else:
	print("MOVE!")
	count = count - 5

#Asking for their favorite social media and give points for it.
social_media = input("What is your favorite social media?")
social_media = social_media.title().strip()

if social_media == "Facebook":
	print("Like")
	count = count + 12
elif social_media == "Instagram":
	print("Heart")
	count = count + 16
elif social_media == "Twitter":
	print("Retweet")
	count = count + 3
elif social_media == "Whatsapp":
	print("Star")
	count = count + 19
elif social_media == "LinkedIn":
	print("Interesting")
	count = count + 21
else:
	print("Is that social?")
	count = count - 3

#make the variable count a string and print the total points
count = str(count)
print("You got " + count + " points")
print ("Thanks for signing up! Goodbye!")
exit()