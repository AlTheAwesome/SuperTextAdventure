import sys
import time
import os

def PrintSlow(thing, slep=None):
	for char in thing:
		time.sleep(.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	sys.stdout.write("\n")
	if slep != None:
		time.sleep(slep)

def Loading(): #---------------------Loading Hourglass animation---------------------#
	os.system("clear")
	for i in range(2):
		x = open("Assets/HourGlass.txt", "r")
		for i in range(7):
			for i in range(15):
				print(x.readline(), end="")
			x.readline()
			time.sleep(0.7)
			os.system("clear")
		x.close()

def Transition(): #---------------------DNA Transition animation---------------------#
	with open("DNA.txt", "r") as fancy:
		for i in range(2):
			for line in fancy:
				print(line, end="")
				time.sleep(0.05)
			fancy.seek(0)
		time.sleep(3)
	print("___________________")
    
#-----------------------------------------------------------So-It-Begins-----------------------------------------------------------#

Loading() 

PrintSlow("SOMEWHERE IN SECTOR 44, EARTH, 2099\n", 2)

PrintSlow("Axel: ARRGHHH...that really hurt!", 0.6)
PrintSlow("Zach: is that what I think it was?...(*Explosion in the background*)", 0.3)
PrintSlow("Axel: We're going to have to hurry..or else there won't be much left of me by the time we arrive.. I can barely drive...I'm going to pull over, take out the machine HQ gave us", .7)
PrintSlow("Zach: You're gonna be fine...just concentrate and try to remember as much as you can while you're in there...it's gonna be ok", .3)
PrintSlow("Axel: I think it's starting...quick Hurry!", .3)
PrintSlow("Zach: Don't forget the rules. They'll be in your pocket..Good luck partner.", 1)
PrintSlow("Axel: Ouch!", .2)
os.system("clear")

Transition()

PrintSlow("Axel: uGHhh...STOP IT!", 0.8)
PrintSlow("Axel: WHO'S DOING THAT?!...YOUR TORCH IS GIVING ME A HEADACHE...AND I ALREADY HAVE ONE", 1)
PrintSlow("Someone: Maybe you weren't aware you were trespassing on private property mr....", 0.8)
PrintSlow("Axel: Axel...and NO I wasn't aware I was trespassing...allow me to get off your property", 0.4)
PrintSlow("Someone: I'm afraid it's not going to be that easy...and that was a retorical question...this is not a place you end up accidentally son....Get your ass up.", 0.5)
PrintSlow("Axel: look, just let me go and I'll be on my way...*Wherever that is..*", 1)
PrintSlow("Someone: looks like I'm gonna have to use this after all...", 0.2)
PrintSlow("Axel: NO!", 0.5)
PrintSlow("Someone: Too late.", 1)


Loading()

PrintSlow("...", 1)
PrintSlow("ouch that really hurt...", .5)
PrintSlow("I have to get out of here...")

exec(open("./Main.py").read())

