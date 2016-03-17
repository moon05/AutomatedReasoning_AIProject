import walkSAT

walkSAT.presentVariables.append("P")
walkSAT.presentVariables.append("Q")

clauses = list()
clauses.append(["or","not","P","Q"])

print clauses


print walkSAT.WalkSAT(clauses, .45, 40)

print walkSAT.tempTable
