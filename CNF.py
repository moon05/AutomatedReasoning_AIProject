

def valueConverter(tableROW, clause, variableList):

	tempClause = clause
	print tempClause
	
	
	if ( len(tempClause) == 1 and type(tempClause[0]) == bool ):
		print "In bool"
		a = tempClause[0]
		print a
		print "about to return"
		print a
		return a

	elif ( len(tempClause) == 1 and type(tempClause[0] != bool) ):

		var = clause.pop()
		if (var in variableList):
			print tableROW[var]
			tempClause.append(tableROW[var])
			return valueConverter(tableROW, tempClause, variableList)


	elif ( len(tempClause) >=2 ):
		
		# print "In Double"

		varB = None
		varA = None
		op = None
		varB = tempClause.pop()
		if (tempClause[-1] is "NOT"):
			# print "In NOT"
			op = tempClause.pop()
			tempClause.append(not tableROW[varB])
			# print "Printing from double NOT"
			print tempClause
			return valueConverter(tableROW, tempClause, variableList)
		else:
			# print "Didnt go into NOT"
			varA = tempClause.pop()
			op = tempClause.pop()

		if (op is "OR" and varA in variableList and varB in variableList):
			tempClause.append(tableROW[varA] or tableROW[varB])
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "OR" and varA in variableList and type(varB)==bool ):
			tempClause.append(tableROW[varA] or varB)
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "AND" and varA in variableList and varB in variableList):
			tempClause.append(tableROW[varA] and tableROW[varB])
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "AND" and varA in variableList and type(varB)==bool ):
			tempClause.append(tableROW[varA] and varB)
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "IMPLIES" and varA in variableList and varB in variableList):
			tempClause.append(not tableROW[varA] or tableROW[varB])
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "IMPLIES" and varA in variableList and type(varB)==bool ):
			tempClause.append(not tableROW[varA] or varB)
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "IFF" and varA in variableList and varB in variableList):
			j = not tableROW[varA] or tableROW[varB]
			k = tableROW[varA] or not tableROW[varB]
			tempClause.append(j and k)
			return valueConverter(tableROW, tempClause, variableList)

		elif (op is "IFF" and varA in variableList and type(varB)==bool ):
			j = not tableROW[varA] or varB
			k = tableROW[varA] or not varB
			tempClause.append(j and k)
			return valueConverter(tableROW, tempClause, variableList)



