import truthtable
import collections
import CNF

presentVariables = ["P", "Q"]

global Table
Table = truthtable.TableGenerator(presentVariables)

#sentence 1
def R1(coord):
	for n in Table:
		n["=>R1"] = n[coord]

def R2():
	for n in Table:
		n["=>R2"] = CNF.valueConverter(n, ["NOT","OR","P","Q"], presentVariables)
def KB():
	for n in Table:
		if ( n["=>R1"] and n["=>R2"] is True ):
			n["KB"] = True
		else:
			n["KB"] = False



def entailment():
	for n in Table:
		if (n["KB"] is True):
			if (n["Q"] is False):
				print "Doesn't Entail"
				return
	
	print "Entails"
	return


R1("P")
R2()
KB()
entailment()
