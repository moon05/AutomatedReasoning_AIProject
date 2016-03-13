import sys
import os
import itertools
import collections

# this is the global dictionary to store all the variables
# with their True/False values (if available)

variables = {}
sentenceSolved = list()

# custom enum funtion

def enum(**enums):
	return type('Enum', (), enums)


# custom list reversing function

def ListReverse(List):
	
	temp = List
	temp = temp[::-1]
	return temp


# A list with the variables will be the input
# The TruthTable for n variables will be generated
# The table's values will be matched with respective variables
# A list with 2^n dictionarties will be returned

def TableGenerator(ListVar):

	List_of_Variables = ListVar
	length_vars = len(List_of_Variables)
	values = [True, False]
	truth_table = list(itertools.product(values,repeat=length_vars))
	table_list = list()
	
	for n in truth_table:
		d = dict()
		for i in range(length_vars):
			d[List_of_Variables[i]] = n[i]
		table_list.append(d)
	
	return table_list
		

# This function assigns True/False to a variable depending on
# the sentence.


def TruthFinder(dictionary):

	if (type(dictionary) != dict):
		print "This is not a dictionary"
		print "Please enter correct type of variable"
		return

	temp = dictionary.keys()
	length = len(temp)
	
	if (length < 3):
		global variables
		if (length == 1):
			var = dictionary.keys()[0]
			dictionary[var] = True
			variables[var] = True
			sentenceSolved.append(True)
			return dictionary
		elif ((length == 2) and dictionary.keys()[0] == "not"):
			var = dictionary.keys()[1]
			dictionary[var] = False
			variables[var] = False
			sentenceSolved.append(True)
			return dictionary



def Simplifier(ORDdict):

	if (type(ORDdict) != collections.OrderedDict):
		print "This is not a ordered dictionary"
		print "Please enter correct type of variable"
		return
	ORDdict2 = ORDdict
	length = len(ORDdict2)

	glob_key_list = list(ORDdict2)
	if (length >= 3):
		list_keys = list(ORDdict2)
		S_Var_tuple =  ORDdict2.popitem()
		Operator = ORDdict2.popitem()
		F_Var_tuple = ORDdict2.popitem()
		length_keys = len(list_keys)
		temp_a, temp_b = None
		if variables.has_key(length_keys):
			temp_b = variables[length_keys]
		if variables.has_key(length_keys-2):
			temp_a = variables[length_keys-2]
		if BinaryConnective.OR in Operator: #OR
			answer = temp_a or temp_b
			ORDdict2[answer] = answer
		if  BinaryConnective.AND in Operator: #AND
			answer = temp_a and temp_b
			ORDdict2[answer] = answer

	if ( len(ORDdict2) == 1 ):
		return list(ORDdict2)

	if ( len(ORDdict2) != 1 ):
		Simplifier(ORDdict2)



def CNFConverter(ORDdict):

	if (type(ORDdict) != collections.OrderedDict):
		print "This is not a ordered dictionary"
		print "Please enter correct type of variable"
		return
	# temp = dictionarty.keys()
	length = len(ORDdict)
	dict_to_list = list(ORDdict)
	print ORDdict

	if ( length==3 and (BinaryConnective.IMPLIES in ORDdict) ):
		temp = list()
		temp.append(UnaryConnective.NOT)
		temp.append(dict_to_list[0])
		temp.append(BinaryConnective.OR)
		temp.append(dict_to_list[2])

		return temp

	elif( length==3 and (BinaryConnective.IFF in ORDdict) ):
		temp1 = list()
		temp2 = list()

		temp1.append(UnaryConnective.NOT)
		temp1.append(dict_to_list[0])
		temp1.append(BinaryConnective.OR)
		temp1.append(dict_to_list[2])

		temp2.append(dict_to_list[0])
		temp2.append(BinaryConnective.OR)
		temp2.append(UnaryConnective.NOT)
		temp2.append(dict_to_list[2])

		return (temp1,temp2)
		#type == tuple


		


BinaryConnective = enum(AND = 1, OR = 2, IMPLIES = 3, IFF = 4)
UnaryConnective = enum(NOT = 5)



# P
# P => Q
# =| Q
