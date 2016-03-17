import truthtable
import collections
import walkSAT

presentVariables = ["Mythical", "Immortal", "Mammal", "Mortal", "Horned", "Magical"]

for n in presentVariables:
	walkSAT.presentVariables.append(n)

clauses = list()

clauses.append(["IMPLIES", "Mythical", "Immortal"])
clauses.append(["IMPLIES","NOT","Horned","NOT","OR","Immortal","Mammal", ])
clauses.append(["IMPLIES","Horned", "Magical"])

print walkSAT.WalkSAT(clauses, .45, 5)
