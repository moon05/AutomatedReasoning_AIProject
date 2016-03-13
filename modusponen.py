import truthtable
import collections

#inserting first sentence
truthtable.TruthFinder({"P":None})

#inserting second sentence
Sentence2 = collections.OrderedDict(([("P",None),(truthtable.BinaryConnective.IMPLIES,None),("Q",None)]))

ConvertedSentence2 = truthtable.CNFConverter(Sentence2)
print ConvertedSentence2

table = truthtable.TableGenerator(["P","Q"])
print table



def solver(table,senteceAsList):
	table = table
	print senteceAsList

	if (len(senteceAsList) == 3):
		currA = truthtable.variables[senteceAsList[0]]
		currB = True

		if (senteceAsList[1] == truthtable.BinaryConnective.OR):
			for n in table:
				if ( n[senteceAsList[0]] == currA and n[senteceAsList[2]] == currB ):
					return currA or currB

	if (len(senteceAsList) == 4):
		currA = None
		currB = None
		if (senteceAsList[0] == truthtable.UnaryConnective.NOT):
			currA = not truthtable.variables[senteceAsList[1]]
			currB = True

			if (senteceAsList[2] == truthtable.BinaryConnective.OR):
				for n in table:
					if( n[senteceAsList[1]] == currA and n[senteceAsList[3]] == currB):
						return currA or currB
		elif (senteceAsList[2] == truthtable.UnaryConnective.NOT):
			currA = truthtable.variables[senteceAsList[0]]
			currB = not truthtable.variables[senteceAsList[3]]

			if (senteceAsList[2] == truthtable.BinaryConnective.OR):
				for n in table:
					if( n[senteceAsList[1]] == currA and n[senteceAsList[3]] == currB):
						return currA or currB





print truthtable.variables

print solver(table, ConvertedSentence2)

