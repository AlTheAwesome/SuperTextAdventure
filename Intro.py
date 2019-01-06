import sys
import time
def PrintSlow(thing):
	for char in thing:
		time.sleep(.05)
		sys.stdout.write(char)
		sys.stdout.flush()

PrintSlow("Axel: ARRGHHH...that really hurt!\n")
PrintSlow("Zach: is that what I think it was?...(*Explosion in the background*)\n")
PrintSlow("Axel: Were going to have to hurry..or else there won't be much left of me by the time we arrive...I'm going to pull over, get out the machine \"CC\" gave us\n")
PrintSlow("Zach: You're gonna be fine...just concentrate and try to remember as much as you can while you're in there...it's gonna be ok\n")
PrintSlow("Axel: I think it's starting...quick Hurry!\n")
PrintSlow("Zach: Good luck...\n")
with open("DNA.txt", "r") as fancy:
    print(fancy.read())
