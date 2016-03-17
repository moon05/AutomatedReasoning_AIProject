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

def prettyPrint(table):
	for n in table:
		print n
		print
		

BinaryConnective = enum(AND = 1, OR = 2, IMPLIES = 3, IFF = 4)
UnaryConnective = enum(NOT = 5)


