from subprocess import Popen
import os
import time
import sys
import math
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>---F--U--N--C--T--I--O--N--S--->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def PrintSlow(thing, slep=None):
	for char in thing:
		time.sleep(.05)
		sys.stdout.write(char)
		sys.stdout.flush()
	if slep != None:
		time.sleep(slep)
#Function to print things out slow throughout the game so that it seems that they are being typed real time
#the "sys.stdout.write()" is there so it works in a terminal because of the buffer with the print function
#the "sys.stdout.flush()" is there so that sys.stdout.write()'s parameters don't appear on the error list

def ShowMap():
	with open("MAPS/GAME1/"+CurrentRoom+".txt", "r") as DaRoom:
		for line in DaRoom:
			print(line, end = "")
		print("\n")
#Depending on where you are in the game
#the function gives you the corresponding map
#which also tells you where you are in the game.a
#-----------------------------------------------------------#It's too long it needs shortening
def ShowInventory():
	with open("Inventory.txt", "r") as invtest:
		for line in invtest:
			print(line, end="")
		print("\n")

#Displays the players inventory
#-----------------------------------------------------------
def InventoryCheck(Item):
	if Item in Inventory:
		return True
	else:
		return False
#another simple funcion that checks if an item is currently in the player's inventory
#---------------------------------------------------------------------------------------
def textreplace(IString):
	magic_number = (58 - len(IString)) // 2
	if len(IString) % 2 == 0:
		return "|" + (magic_number * " ") + IString + (magic_number * " ") + "|"
	else:
		return "|" + (magic_number * " ") + IString + (magic_number * " ") + " " + "|"
#Function to add another item in the inventory...it will remain that way unless the inventory is blanked again.
#----------------------------------------------------------------------------------------------------------------

def Inventoryadd(Item):
	global timesran
	numba = str(timesran-7) + "." #for the number before the item in the Inventory
	with open("Inventory.txt", "r") as invtest:
					thefile = invtest.readlines()

	thefile.insert(timesran, textreplace(numba + Item) + "\n")

	with open("Inventory.txt", "w") as invtest:
		thefile = "".join(thefile)
		invtest.write(thefile)

	timesran += 1
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---F--U--N--C--T--I--O--N--S---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#--------------------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>---G--A--M--E___I--N--I--T--I--A--L--I--Z--A--T--I--O--N--->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#|---LEVELS---|
GAME1 = True
GAME2 = False
GAME3 = False
#|---LEVELS---|

#!@$%^&*-------------------------The beginning----------------------*&^%$@!#
PrintSlow("HINT: -At any time you can use 'look around' (to look around)\n")
#=========================================================================================
#|---The Room changing system---|
CurrentRoom = "Room1"
Room1 = True
Room2 = False
Room3 = False
Room4 = False
#|---The Room changing system---|
#=========================================================================================
#|---Inventory Items---|
ExitKey = ["Basement Key", "Hmm a not-so shiny key...this should play a part in helping me get out of here....where ever the hell this is"]
Crowbar = ["Crowbar", "Always handy to have one of these when there's a door that needs unjamming...it may even be useful after that"]
MAP = ["Basement Map", "A large peice of paper seems to have the layout of the floor that I'm on printed on to it"]
#|---Inventory Items---|
#=========================================================================================
#|---Firsttime Bools for unique output when you enter somewhere for the first time---|
timesran = 8 #----------------------------------------------------variable for which line to write the item to---
room1firsttime = True
room2firsttime = True
room3firsttime = True
room4firsttime = True
#|---Firsttime Bools for unique output when you enter somewhere for the first time---|
#=========================================================================================
Inventory = [] #the inventory

#|---Global options that are used commonly---|
Mapopt = ["showmethemap", "showmap", "map"]
TheDoor = ["opendoor", "openthedoor", "door", "openwoodendoor"]
gtfo = ["leavetheroom", "exit", "leave", "leaveroom", "gtfo", "goback", "leavetheroom"]
ShowingInventory = ["showinventory", "inventory", "items", "showitems", "displayitems", "displayinventory"]
#|---Global options that are used commonly---|


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---G--A--M--E___I--N--I--T--I--A--L--I--Z--A--T--I--O--N---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<






#------------------------PURELY FOR TESTING SINCE I CAN'T STAND GOING THROUGH THE ENTIRE GAME JUST TO GET TO A CERTAIN POINT.
#--------------------------------THIS WILL SERVE AS A PASSWORD TO BYPASS A CERTAIN PORTION OF THE GAME TO TEST FEATURES------.
catchphrase = input("")
if catchphrase == "GAME2":
	GAME2 = True
	GAME1 = False
else:
	PrintSlow("hmm...")
#----------------------------------------------------------------------------------------------------------------------------
while GAME1 == True:
#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---W-H-I-L-E---G-A-M-E-1--==--T-R-U-E---_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------------R-O-O-M--1-----------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Room1:
		room1opts = ["lookaround", "openthedoor", "openthebox"]  #Different actions that can be fulfilled in room 1
		WoodenBox = ["openthebox", "openbox", "openwoodenbox", "openthewoodenbox"]

		PrintSlow("What to do next I wonder...\n")
		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")
		if  Action == "lookaround":
			if room1firsttime:
				PrintSlow("The only thing I can Barely see is an old wooden door...I think...OH and there's what appears to be a wooden box next to me...\n")
			else:
				PrintSlow("The only thing I can Barely see is the old wooden door I just came through...this place really looks like a boring dungeon...\n")

		elif Action in Mapopt and InventoryCheck(MAP[0]) == True:
			ShowMap()

		elif Action in WoodenBox:
			PrintSlow("There's a note that reads: 'Good  luck.'....how uplifting..\n")
		elif Action in ShowingInventory:
			ShowInventory()

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(MAP[0]) == True:
				print("\n")
				print(MAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) ==  True:
				print("\n")
				print(ExitKey[1])

		elif Action in TheDoor:
			Room2 = True
			CurrentRoom = "ROOM2"
			room1firsttime = False
			Room1 = False
		else:
			PrintSlow("Nah...")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------------R-O-O-M--2-----------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Room2:
		room2opts = ["lookaround", "opendoor1", "opendoor2", "opendoor3", "lookinthefireplace"]
		Door1 = ["opendoor1", "openthefirstdoor", "openfirstdoor", ]
		Door2 = ["opendoor2", "opentheseconddoor", "openseconddoor", ]
		Door3 = ["opendoor3", "openthethirddoor", "openthirddoor", ]
		Fireplace = ["lookinthefireplace", "inspectfireplace", "lookatfireplace", "fireplace", "searchfireplace"]



		if room2firsttime == False:
			PrintSlow("Ok, what's the next move?\n")
			Action = input("")

		if room2firsttime:
			PrintSlow("ok...looks like I'm in the second room...\n")
			Action = input("")
			room2firsttime = False

		Action = Action.lower()
		Action = Action.replace(" ", "")
		if Action == "lookaround":
			PrintSlow("Well there seem to be 3 doors here...The one I came from I'll call door 1, another lies ahead of me..I'll call that Door 2. There is also one to my right..I'll call that door 3...There is a fireplace to my left and a light above me illuminates the room..\n")

		elif Action in Door1 :
			Room1 = True
			CurrentRoom = "ROOM1"
			Room2 = False

		elif Action in Mapopt and InventoryCheck(MAP[0]) == True:
			ShowMap()

		elif Action in ShowingInventory:
			ShowInventory()

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(MAP[0]) == True:
				print("\n")
				print(MAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) == True:
				print("\n")
				print(ExitKey[1])

		elif Action in Door2:
			Room3 = True
			CurrentRoom = "ROOM3"
			Room2 = False

		elif Action in Door3:
			if InventoryCheck(Crowbar[0]) == True:
				Room4 = True
				CurrentRoom = "ROOM4"
				Room2 = False
			else:
				PrintSlow("Oh shit the door seems locked...But it doesn't seem unbreakable...though I can't get through without any tools...or maybe a key...looks like I'll have to explore further\n")

		elif Action in Fireplace:
			if InventoryCheck(ExitKey[0]) == False:
				PrintSlow("There is no fire...and there seems to be nothing of import-... Oh look a key!, I'll have that\n")
				Inventory.append(ExitKey[0])
				Inventoryadd(ExitKey[0])

			else:
				PrintSlow("There is no fire...and there seems to be nothing of importance...\n")

		else:
			PrintSlow("WRONG ANSWER\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------------R-O-O-M--3-----------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Room3:
		room3opts = ["lookaround", "crowbar", "leaveroom"]
		Floortile = ["floortile", "inspectfloortile", "lookunderfloortile","lookunderthefloortile", "tile", "inspectfloor", "liftfloortile", "liftthefloortile"]
		Thecrowbar = ["takecrowbar", "takethecrowbar", "crowbar", "getcrowbar", "gocrowbargo"]


		if room3firsttime == False:
			PrintSlow("hmm what's next?.. \n")
			Action = input("")
		if room3firsttime:
			PrintSlow("*Coughs* ugh aand here I am in the third room... \n")
			Action = input("")
			room3firsttime = False

		Action = Action.lower()
		Action = Action.replace(" ", "")


		if Action == "lookaround":
			if InventoryCheck(Crowbar[0]) == False and InventoryCheck(MAP[0]) == True:
				PrintSlow("A baron room...a crowbar on the floor and not much else other than a pretty uneven floor...\n")
			elif InventoryCheck(Crowbar[0]) == True and InventoryCheck(MAP[0]) == False:
				PrintSlow("A baron room...not much else other than a pretty uneven floor...one of the tiles seems quite unstable...\n")
			elif InventoryCheck(Crowbar[0]) == True and InventoryCheck(MAP[0]) == True:
				PrintSlow("A pretty baron room...These walls look ancient and quite filthy...\n")
			else:
				PrintSlow("A baron room...a crowbar on the floor and not much else other than a pretty uneven floor...one of the tiles seems quite unstable...\n")

		elif Action in Mapopt and InventoryCheck(MAP[0]) == True:
			ShowMap()

		elif Action in Floortile and MAP[0] not in Inventory:
			PrintSlow("AHA a MAP!!...wait why would someone hide a map deliberatelly under a stone slab?..let's have a look..\n")
			Inventory.append(MAP[0])
			Inventoryadd(MAP[0])
			ShowMap()

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(MAP[0]) == True:
				print("\n")
				print(MAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) == True:
				print("\n")
				print(ExitKey[1])

		elif Action in ShowingInventory:
			ShowInventory()

		elif Action in Thecrowbar and InventoryCheck(Crowbar[0]) == False:
			Inventory.append(Crowbar[0])
			Inventoryadd(Crowbar[0])
			PrintSlow("OK I've got the crowbar...good thinking...")

		elif Action in gtfo:
			Room2 = True
			CurrentRoom = "ROOM2"
			Room3 = False
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------------R-O-O-M--4-----------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Room4:
		room4opts = ["lookaround"]
		TheExitDoor = ["opendoor", "openthedoor", "door", "openwoodendoor"]
		Backdoor = ["leave", "back", "leavebehind", "goback", ""]

		if room4firsttime == False:
			PrintSlow("I wonder what My brain will come up with next... \n")
			Action = input("")
		if room4firsttime:
			PrintSlow("Looks like this is room 4! \n")
			Action = input("")
			room4firsttime = False
		Action = Action.lower()
		Action = Action.replace(" ", "")
		if Action == "lookaround":
			PrintSlow("hmm not much in this room but there seems to be a door...I can see light coming from behind it!..\n")

		elif Action in Mapopt and InventoryCheck(MAP[0]) ==True:
			ShowMap()

		elif Action in ShowingInventory:
			ShowInventory()

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(MAP[0]) == True:
				print("\n")
				print(MAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) == True:
				print("\n")
				print(ExitKey[1])

		elif Action in TheDoor:
			if InventoryCheck(ExitKey[0]) == True:
				PrintSlow("YES It's opened!....looks like stairs leading to another floor..")
				GAME2 = True
				GAME1 = False #THIS IS WHERE THE GAME EXITZ (actually it extis two lines below)
				break
			else:
				PrintSlow("It's fucking locked...unlike the last door This one will definitely need a key for me to get through so I better get looking.\n")
		elif Action in Backdoor:
			Room2 = True
			CurrentRoom = "ROOM2"
			Room4 = False
		else:
			PrintSlow("eh..nO.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stairs = True
CurrentRoom = "stairs"
Corridor1 = False
Lounge = False
Dining_Room = False
Kitchen = False
Bed_Room = False
#^^Rooms that activate and de-activate based on their Boolean values^^
SecondMAP = ["A map for the current floor", "What appears to be a map for the second floor"]
#^^Items for the second part of the game^^
Bottomofstairs = True
#^^just there to check if you're at the bottom of the stairs to give you unique output.^^
firststairs = 0
#if firststairs == 0 it means that you've entered for the first time giving you a unique output(story orientated).
#if firststairs == 1 it means that you've gone up the stiars for the first time giving you a different unique output(story orientated).
#if firststairs == 2 it means that you've gone up and down so it doesn't play the unique first time messages as it did before.
firstcorridor = True
firstkitchen = True
firstlounge = True
firstbedroom = True
firstdiningroom = True
#----
firstwindow = True
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#-!-!-!-!-!-!-!-1-!-!-!-1-!-!-1-!-!-!-!-!-!-!-!-!-Functions for the output of unique text for the first time you enter rooms!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!
def TheStairDilema(justnow, at_the_bottom):
	if justnow == 1 or justnow == 2:
		if at_the_bottom:
			PrintSlow("I should stop lingering down here and get upstairs..\n")
		else:
			PrintSlow("hmm back at the stairs leading down to the basement..at least I think it's the basement\n")
	if justnow == 0:
		PrintSlow("huh...there seems to be a light up there just getting through the cracks o the door...Why can't I remember where I was before I woke up here...UGH..\n")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def firsttimeDilema(time):
#---------------ROOMS (which give special output on first entry)-------------
	if Kitchen:
		if time:
			PrintSlow("I guess this is the Kitchen..")
		else:
			PrintSlow("Ok..The kitchen..")
	elif Corridor1:
		if time:
			PrintSlow("I wonder where I am..hmm..it's a little dark in here..")
		else:
			PrintSlow("*Stands and thinks...*")
	elif Lounge:
		if time:
			PrintSlow("")
		else:
			PrintSlow("*Currently in the Lounge*")
	elif Bed_Room:
		if time:
			PrintSlow("aHA the bedroom....if only I wasn't alone...")
		else:
			PrintSlow("*Currently in the bedroom*")
#---------------ROOMS (which give special output on first entry)-------------

#-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!


while GAME2:
#|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|
#|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_---W-H-I-L-E---G-A-M-E-2--==--T-R-U-E---_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-|
#|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|

	KitchenDoor = ["enterkitchen", "openkitchendoor", "kitchendoor", "openthekitchendoor"]
	Corridor1Door = ["entercorridor1", "opencorridor1door", "corridor1door"]
	LoungeDoor = ["enterlounge", "openloungedoor", "loungedoor", "opentheloungedoor"]
	Bed_RoomDoor = ["enterbedroom", "openbedroomdoor", "bedroomdoor", "openthebedroomdoor"]
	Dining_RoomDoor = ["enterdiningroom", "opendiningroomdoor", "diningroomdoor", "openthediningroomdoor"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------------S-T-A-I-R-S----------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

	while stairs:
		upstairs = ["goupstairs", "goupthestairs", "stairs", "usestairs", "usethestairs"]
		downstairs = ["godownstairs", "godownthestairs", "stairs", "usestairs", "usethestairs"]

		VanishingDoor = False #Condition for unique output when the user tries to turn back.

		TheStairDilema(firststairs, Bottomofstairs)
		firststairs = 1

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			PrintSlow("Ahh..yes...stairs... yet another  door lies at the top \n")

		elif Action in upstairs and Bottomofstairs:
			PrintSlow("Ok I'm at the door...\n")
			Bottomofstairs = False

		elif Action in downstairs and Bottomofstairs == False:
			PrintSlow("ok..")
			Bottomofstairs = True

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(MAP[0]) == True:
				print("\n")
				print(SecondMAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) == True:
				print("\n")
				print(ExitKey[1])

		elif Action in ShowingInventory:
			ShowInventory()

		elif Action in gtfo and Bottomofstairs:
			if VanishingDoor == False:
				PrintSlow("OMG the door has Vanished!!...I don't like this one bit....I have to press on.\n")
				VanishingDoor = True
			elif VanishingDoor:
				PrintSlow("I told you it's gone...I can't walk through walls.")


		elif Action in TheDoor and Bottomofstairs == False:
			if firststairs == 2:
				PrintSlow("aaand through the door we go\n")
				Corridor1 = True
				Stairs = False
			elif firststairs == 1:
				PrintSlow("*Creek..* huh this all seems so ordinary..it still doesn't answer the question as to why or where I am though\n")
				firststaris = 2
				Corridor1 = True
				Stairs = False
				break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#--------------------------------------------C-O-R-R-I-D-O-R--1------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Corridor1:
		takingmap = ["takemap", "takethemap", "getmap", "getthemap"]

		firsttimeDilema(firstcorridor)
		firstcorridor = False

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			if InventoryCheck(SecondMAP) == False:
				PrintSlow("Huh...another map against this wall....this is very weird....\n")
			else:
				PrintSlow("A fairly sized corridor..A massive painting of what seems to be......Your mom...I feel like it's important..\n")

		elif Action in Mapopt and InventoryCheck(SecondMAP[0]):
			ShowMap()

		elif "examine" in Action:
			if "map" in Action and InventoryCheck(SecondMAP[0]) == True:
				print("\n")
				print(SecondMAP[1])
			elif "crowbar" in Action and InventoryCheck(Crowbar[0]) == True:
				print("\n")
				print(Crowbar[1])
			elif "key" in Action and InventoryCheck(ExitKey[0]) == True:
				print("\n")
				print(ExitKey[1])


		elif Action in takingmap and InventoryCheck(SecondMAP[0]) == False:
			Inventory.append(SecondMAP[0])
			PrintSlow("Hmmm good idea..let's see what we have here..\n")
			ShowMap()

		elif Action in ShowingInventory:
			ShowInventory()

		#---Door Actions which never get old..obviously---
		elif Action in Bed_RoomDoor:
			Bed_Room = True
			CurrentRoom = "Bed_Room"
			Corridor1 = False
		elif Action in KitchenDoor:
			Kitchen = True
			CurrentRoom = "Kitchen"
			Corridor1 = False
		elif Action == "go back":
			stairs = True
			CurrentRoom = "stiars"
			Corridor1 = False
			break
		#---Door Actions which never get old..obviously---
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-----------------------------------------T-H-E--K-I-T-C-H-E--N------------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Kitchen:
		KitchenWindow = ["inspectwindow", "inspectthewindow", "lookinthewindow", "lookinwindow", "window", "lookatwindow"]
		KitchenCounter = ["inspectcounter", "lookatcounter", "counter", "kitchencounter", "gotocounter"]
		Cuboards = ["inspectcuboards", "inspectthecuboards", "gotocuboards", "gotothecuboards", "cuboards", "lookinthecuboards", "lookincuboards"]
		kitchenchairs = ["inspectchairs", "inspectthechairs", "chiars", "gotochairs", "gotothechairs"]

		KitchenDilema(firstkitchen)
		firstkitchen = False

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			PrintSlow("a kitchen counter is in the center of the room..some cuboards and cuttlery allong with a few chairs and a...window!!\n")
		if Action in KitchenWindow:
			if firsttimeDilema(firstwindow):
				PrintSlow("what?!....what is that out there?!....I've got to go and take a look myself..but there's no chance I'll be getting through this window..I'm going to have to find my way out")
			else:
				PrintSlow("huh..it's still there...")
		if Action in KitchenCounter:
			pass

		#----------Object Reaction Actions-------#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#---------------------------------------T-H-E--D-I-N-I-N-G--R-O-O-M--------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Dining_Room:

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			PrintSlow("")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#---------------------------------------------T-H-E--L-O-U-N-G-E-----------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Lounge:

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			PrintSlow("")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#------------------------------------------T-H-E--B-E-D--R-O-O-M-----------------------------------------#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
	while Bed_Room:

		Action = input("")
		Action = Action.lower()
		Action = Action.replace(" ", "")

		if Action == "lookaround":
			PrintSlow("")
