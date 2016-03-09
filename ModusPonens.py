import sys
import os

path = os.getcwd()

#####################################################################
def reader(filename):

	foo = open(filename,"r")
	content = foo.read()
	linebreaks_stripped = content.replace('\n',"")
	# print linebreaks_stripped
	return linebreaks_stripped

def parser(content):
	semiSplitter = content.split(";")
	return semiSplitter

arg1 = sys.argv[1]
#####################################################################

#this is to store the variables with their True/False values one decided
variables = {} #this is called a dictionary, similar to hashtable in java

#enum class, python doesn't really have one
def enum(**enums):
	return type('Enum', (), enums)


# def modelCheck(dictionary):

# 	if (type(dictionary)!=dict):
# 		break
# 	if (dictionary.)

def ListReverse(List):
	
	temp = List
	temp = temp[::-1]
	return temp


#assigning values to those sentences similar to "A" or "not A"
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
			return dictionary
		elif ((length == 2) and dictionary.keys()[0] == "not"):
			var = dictionary.keys()[1]
			dictionary[var] = False
			variables[var] = False
			return dictionary


#this will be for IMPLIES and IFF
def ModelChecker(dictionary):

	if (type(dictionary) != dict):
		print "This is not a dictionary"
		print "Please enter correct type of variable"
		return
	
	temp = dictionary.keys()
	length = len(temp)
	
	if (length > 2):
		
#Connectives
BinaryConnective = enum(AND = 1, OR = 2, IMPLIES = 3, IFF = 4)
UnaryConnective = enum(NOT = 5)
