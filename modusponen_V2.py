import truthtable
import collections

presentVariables = ["P", "Q"]

global Table
Table = truthtable.TableGenerator(presentVariables)

#sentence 1
def R1(coord):
	for n in Table:
		n["R1"] = n[coord]

def R2():
	for n in Table:
		n["R2"] = not n["P"] or n["Q"]

def entailment():
	for n in Table:
		if (n["R1"] and n["R2"] is True):
			if (n["P"] and n["Q"] is True):
				print "Entails"
		return


R1("P")
R2()
entailment()
