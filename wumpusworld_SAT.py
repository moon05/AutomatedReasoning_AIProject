import truthtable
import walkSAT
import CNF

variables = ["B11", "B21", "P11", "P12", "P21", "P22", "P31"]

for n in variables:
	walkSAT.presentVariables.append(n)

clauses = list()

clauses.append(["NOT", "P11"])
clauses.append(["IFF","B11","OR","P12","P21"])
clauses.append(["IFF","B21","OR","P11","OR","P22","P31"])
clauses.append(["NOT", "B11"])
clauses.append(["B21"])

print walkSAT.WalkSAT(clauses, .45, 100)









