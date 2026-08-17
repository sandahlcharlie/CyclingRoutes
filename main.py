import os
import routeFilter

# Intro to program asking for input
print("Welcome to the gpx Cycling Route Summary")
print("This program will summarize cycling data in gpx format and give you a summary of your trips")
homeLat = input("Input home latitude: ")
homeLon = input("Input home longitude: ")
inputFolder = input("Please input the folder with you gpx data: ")
outputFolder = "output"
if not os.path.exists(outputFolder):
    os.mkdirs(outputFolder)


# Choice Menu
print("What would you like to do?")
print("1.) ")

# Error checking for user choice 
while True:
    menuInput = input("Enter the number for the menu item you choose: ")
    try:
        if 1 <= menuInput <= 3:
            break
    else:
        print("Please choose a number between 1 and 3.")
    except ValueError:
        print("Please enter a number.")

# Activate the user choice
match menuInput:
    case 1:
        routeFilter(inputFolder, homeLat, homeLon)
