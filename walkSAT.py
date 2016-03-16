import truthtable
import random

presentVariables = []
len_Vars = len(presentVariables)

def flip(truthRow,Var):
	
	Row = truthRow
	if (Row[Var] == True):
		Row[Var] = False
	elif (Row[Var] == False):
		Row[Var] = True

	return Row

def satisfies(clause, Row):

	s = None
	
	if (len(clause)==3):
		s = Row[clause[0]] or Row[clause[2]]
	elif (len(clause)==4 and clause[0] == "not"):
		s = not Row[clause[1]] or Row[clause[3]]
	elif (len(clause)==4 and clause[2] == "not"):
		s = Row[clause[0]] or not Row[clause[3]]
	elif (len(clause)==5 and clause[0] == "not" and clause[3]=="not"):
		s = not Row[clause[0]] or not Row[clause[4]]

	return s

def numSatisfied(clauseList, Row):

	number = 0

	for n in clauseList:
		k = satisfies(n,Row)
		if (k is True):
			number = number + 1

	return number

def varMaxesSAT(clauseList, VARS, Row):

	var = VARS[0]
	clauseSatisfied = 0

	for n in VARS:

		tempVar = n
		if ( numSatisfied(clauseList,flip(tempVar)) > clauseSatisfied ):
			var = tempVar
			clauseSatisfied = numSatisfied(clauseSatisfied,flip(tempVar))

	return var


def WalkSAT(clauses, probability, maxflips):

	for i in range(maxflips):
		try:
		tempTable = truthtable.TableGenerator[presentvariables]
		len_of_table = tempTable

		
		model = tempTable[0]
		for i in range(0):
			
			s = list()
			for n in clauses:

				sat = satisfies(n, model)
				s.append()

			if (False not in s):
				return model

			if (random.uniform(0,1) >= probability):
				temp_model = model
				index_var_to_change = random.randint(0,len_Vars-1)
				temp_list_model = list(model)
				var_to_change = temp_list_model[index_var_to_change]
				model = flip(temp_model, var_to_change)

			else:

				varFlip = varMaxesSAT(clauses, presentVariables, model)
				model = flip(model, varFlip)

		return "Failure"

		except IndexError:
			return "Failure"
