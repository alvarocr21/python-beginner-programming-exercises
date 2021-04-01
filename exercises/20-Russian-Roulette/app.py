import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    chamber = spin_chamber()
    resultado=""
    if bullet_position==chamber:
        resultado = "You are dead!"
    else:
        resultado ="Keep playing!"
    return resultado



print(fire_gun())