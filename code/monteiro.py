import csv
from operator import itemgetter 	#testing this

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","

def loadCsvToArray():
	#loads the csv file into an array of arrays, 1
	with open('dados.csv','r') as file: 			#opens the csv file
		reader = csv.reader(file, dialect='AED')	
		countries = stackCountries()
		iterator = 0
		for row in reader:							#iterates the file
			years = stackYears()					#iterates the row and gets the stuff that matters

			for i in range(2, len(row)):

				if row[i] != '':
					years.push(tuple([int(i + 1958), float(row[i])]))
			years.invert(stackYears())
			countries.push(CountryNode(row[0], row[1] , years))
			if iterator == 0:
				countries.pop()
			iterator = 1
	
	file.close()									#closes the file since we don't need it open anymore
	return countries								#returns the stack

class stackCountries:
	def __init__(self):
		self.items = []		#each item == CountryNode() 

	def is_empty(self):		#prof
		return self.items == []
	
	def push(self, item):	#prof
		self.items.insert(0, item)

	def pop(self):			#prof
		return self.items.pop(0)

	def peek(self):			#prof
		return self.items[0]

	def size(self):			#prof
		return len(self.items)

	def invert(self, stackF): 			#stackF = Final (inverted)
		if self.size() > 0:				#if stack is not empty
			stackF.push(self.pop())		#ads to the aux stack the first elem of self
			return self.invert(stackF)	#calls the function itself
		else:
			self.items = stackF.items

	def concatenate(self, stack):
		for i in range(0, stack.size()):
			self.push(stack.pop())

	def search(self, keyWord, op):	#working
		stackAux = stackCountries()
		for i in range(0, self.size()):
			if keyWord == self.peek().cName or keyWord == self.peek().cCode:
				#do something
				if op == 1:		#add values

					break

				elif op == 2:	#edit values

					break

				elif op == 3:	#remove one values

					break

				elif op == 4:	#remove all years
					self.years = None
					break

				elif op == 5:	#delete country
					deletedVal = self.pop()
					break

				else:
					break

			else:
				stackAux.push(self.pop())
		self.concatenate(stackAux)

class CountryNode:
	def __init__(self, cName = None, cCode = None, years = None):
		self.cName = cName 		#str -> e.g. 'Portugal'
		self.cCode = cCode 		#str -> e.g. 'PRT'
		self.years = years 		#class -> stackYears()

	def getCountryName(self):	#self explanatory
		return self.cName

	def getCountryCode(self):	#self explanatory
		return self.cCode

	def getYears(self):			#set explanatory
		return self.years

	def setCountryName(self, cName):	#self explanatory
		self.cName = cName

	def setCountryCode(self, cCode):	#self explanatory
		self.cCode = cCode

	def setYears(self, years):			#self explanatory
		self.years = years

	def displayInfo(self):
		print(cName + '\t' + cCode)
		for i in range(0, years.size()):
			years.displayInfo()

class stackYears:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

	def invert(self, stackF): 			#stackF = Final (inverted)
		if self.size() > 0:				#if stack is not empty
			stackF.push(self.pop())		#ads to the aux stack the first elem of self
			return self.invert(stackF)	#calls the function itself
		else:
			self.items = stackF.items

	def concatenate(self, stack):
		for i in range(0, stack.size()):
			self.push(stack.pop())

	def displayInfo(self, stackAux):
		for i in range(0, self.size()):
			print(str(self.items[0][0]) + '\t' + str(self.items[0][1]) + '%')
			stackAux.push(self.pop())


if __name__ == '__main__':
	stack = loadCsvToArray()
	stack.invert(stackCountries())
	# print(stack.peek().cName)
	# print(stack.peek().cCode)
	# print(stack.peek().years.peek())
	
	stack.search('PRT', 1)
	print('\n')

	#print(stack.peek().cName)
	#print(stack.peek().cCode)
	#print(stack.peek().years.peek())
	print(stack.peek().years.displayInfo(stackYears()))