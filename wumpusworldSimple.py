import truthtable
import collections
import itertools

presentVariables = ["B11", "B21", "P11", "P12", "P21", "P22", "P31"]

global Table
Table = truthtable.TableGenerator(presentVariables)

#Sentence 1
def R1(coord):
	for n in Table:
		n["R1"] = not n[coord]

#Sentence 2
def R2():
	for n in Table:
		lhs = n["B11"]
		rhs = n["P12"] or n["P21"]
		LC = not lhs or rhs
		RC = lhs or not rhs
		result = LC and RC
		n["R2"] = result

#Sentence 3
def R3():
	for n in Table:
		lhs = n["B21"]
		rhs = n["P11"] or n["P22"] or n["P31"]
		LC = not lhs or rhs
		RC = lhs or not rhs
		result = LC and RC
		n["R3"] = result

#Sentence 4
def R4(coord):
	for n in Table:
		n["R4"] = not n[coord]

#Sentence 5
def R5(coord):
	for n in Table:
		n["R5"] = n[coord]

R1("P11")
R2()
R3()
R4("B11")
R5("B21")

#truthtable.prettyPrint(Table)
