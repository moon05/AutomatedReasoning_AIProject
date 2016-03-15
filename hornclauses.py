import truthtable
import collections

presentVariables = ["Mythical", "Immortal", "Mortal", "Horned", "Magical"]

global Table
Table = truthtable.TableGenerator(presentVariables)

#sentence 1
def isImmortal():
	for n in Table:
		if (n["Mythical"] is True):
			n["isImmortal"] = True
			n["isMammal"] = False

def isMammal():
	for n in Table:
		if (n["Mythical"] is False):
			n["isMammal"] = True
			n["isImmortal"] = False

def isHorned():
	for n in Table:
		if (n["isImmortal"] is True or n["isMammal"] is True):
			n["isHorned"] = True
		else:
			n["isHorned"] = False

def isMagical():
	for n in Table:
		if (n["isHorned"] is True):
			n["isMagical"] = True
		else:
			n["isMagical"] = False

def entailmentA():
	i = 0
	for n in Table:
		if (n["isMagical"] is True):
			if (n["isHorned"] is True):
				if (n["Mythical"] is False):
					print "Doesn't entail"
					print "We can't prove it"
					return
		print i
		i = i + 1
		print "Has entailed so far"
	return

def entailmentB():
	i = 0
	for n in Table:
		if (n["Mythical"] is True):
			if (n["Immortal"] is True and n["Mortal"] is False):
				if (n["Horned"] is False):
					print n
					print "Doesn't entail"
					print "Mythical !> Immortal !> Horned !> Magical"
					print "We can't prove it"
					return
		if (n["Mythical"] is False):
			if (n["Immortal"] is False and n["Mortal"] is True):
				if (n["Horned"] is False):
					print n
					print "Doesn't entail"
					print "Mythical !> Mortal !> Horned !> Magical"
					print "We can't prove it"
					return					

		print i
		i = i + 1
		print "Has entailed so far"
	return


isImmortal()
isMammal()
isHorned()
isMagical()

entailmentA()
entailmentB()
