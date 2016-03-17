import truthtable
import collections

presentVariables = ["Mythical", "Immortal", "Mammal", "Mortal", "Horned", "Magical"]

global Table
Table = truthtable.TableGenerator(presentVariables)

#sentence 1
def isImmortal():
	for n in Table:
		if (n["Mythical"] is True):
			n["=>Immortal"] = True
			n["=>Mammal"] = True
			n["=>Mortal"] = False

def isMammal():
	for n in Table:
		if (n["Mythical"] is False):
			n["=>Mammal"] = True
			n["=>Mortal"] = True
			n["=>Immortal"] = False

def isHorned():
	for n in Table:
		if (n["=>Immortal"] is True or n["=>Mammal"] is True):
			n["=>Horned"] = True
		else:
			n["=>Horned"] = False

def isMagical():
	for n in Table:
		if (n["=>Horned"] is True):
			n["=>Magical"] = True
		else:
			n["=>Magical"] = False

def KB():
	for n in Table:
		if ( n["=>Immortal"] and n["=>Mammal"] and n["=>Mortal"] and n["=>Horned"] and n["=>Magical"] is True ):
			n["KB"] = True
		else:
			n["KB"] = False

def entailmentA():
	i = 0
	for n in Table:
		if ( n["KB"] is True ):
			if ( n["Mythical"] is False ):
				print "We can't prove"
				return

	print "We have proved (a)"
	print "The unicorn is Mythical"
	return

def entailmentB():

	for n in Table:
		if ( n["KB"] is True ):
			if ( n["Magical"] == False ):
				print "We can't prove"
				return

	print "We have proved (b)"
	print "The unicorn is Magical"

	return

def entailmentC():

	for n in Table:
		if ( n["KB"] is True ):
			if ( n["Horned"] is False ):
				print "We can't prove"
				return

	print "We have proved (c)"
	print "The unicorn is Horned"
	return



isImmortal()
isMammal()
isHorned()
isMagical()
KB()

entailmentA()
entailmentB()
entailmentC()
