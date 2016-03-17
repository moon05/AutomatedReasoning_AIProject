import truthtable
import CNF

presentVariables = ["Amy", "Bob", "Cal"]

global Table
Table = truthtable.TableGenerator(presentVariables)

def R1():
	for n in Table:
		if (n["Amy"] is True and n["Cal"] is True):
			n["Cal&Amy"] = True
		else:
			n["Cal&Amy"] = False

def R2():
	for n in Table:
		if (n["Cal"] is False):
			n["CalLiar"] = True
		else:
			n["CalLiar"] = False

def R3():
	for n in Table:
		if (n["Bob"] is True or n["Amy"] is False):
			n["BobTAmyF"] = True
		else:
			n["BobTAmyF"] = False

def KB():
	for n in Table:
		if ( n["Cal&Amy"] and n["CalLiar"] and n["BobTAmyF"] is True ):
			n["KB"] = True
		else:
			n["KB"] = False

def Amy():
	for n in Table:
		if (n["KB"] is True):
			if (n["Amy"] is False):
				print "Amy is a Liar"
				return

	print "Amy is a truthteller"
	return

def Bob():
	for n in Table:
		if (n["KB"] is True):
			if (n["Bob"] is False):
				print "Bob is a Liar"
				return

	print "Bob is a truthteller"
	return

def Cal():
	for n in Table:
		if (n["KB"] is True):
			if (n["Cal"] is False):
				print "Cal is a Liar"
				return

	print "Cal is a truthteller"
	return

R1()
R2()
R3()
KB()

Amy()
Bob()
Cal()
