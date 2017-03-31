import csv
import time
from AVL import AVLTreeCountry
from AVL import AVLTreeData

csv.register_dialect('AED', delimiter=';') #registers a new dialect, separated with ";", instead of the default ","



def inputInt(string):
    while True:
        try:
            num = int(input(string))
        except ValueError:
            print("Error... Please try again...")
            continue
        else:
            return num

def inputFloat(string):
    while True:
        try:
            num = float(input(string))
        except ValueError:
            print("Error... Please try again...")
            continue
        else:
            return num


def checkBool(check):
    if check:
        print("Done...\n")
    else:
        print("Error...\n")

#loads the csv to the AVL tree
def load():
	arvorePais=AVLTreeCountry()
	startingYear=1960
	with open('dados.csv','r') as file:
		reader = csv.reader(file ,dialect = 'AED')
		stopFirst=0
		for row in reader:
			if stopFirst==0:
				stopFirst=1
			else:
				years=AVLTreeData()
				for i in range(len(row)):
					if row[i] != '' and i!=0 and i!=1:
						years.insertYears(startingYear+(i-2),row[i])
				arvorePais.insertCountry(row[0],row[1],years)
	file.close()
	return arvorePais

#loads the csv to an auxiliar dictionary
def loadToDict():
	dicioPais={}
	with open('dados.csv','r') as file:
		reader = csv.reader(file,dialect = 'AED')
		for row in reader:
			dicioPais[row[0]]=row[1]
	return dicioPais

#Searches the tree by tag with help from the dictionary
#the function uses the dictionary to get the name that corresponds to the tag
def tagSearch(tag, arvorePais ,dicioPais):
	if tag in dicioPais:
		node=arvorePais.countrySearch(dicioPais.get(tag))
		print(node)
	else:
		print("Error: Tag does not exist!")


#prints all the data of a country (year: XXXX data: XXXX)
def dataOfCountry(arvorePais):
	country=str(input("Insert Country: "))
	node=arvorePais.countrySearch(country)
	node.getYears().display()

#Prints all the Data of all the countries of a given year
def valuesOfYear(arvorePais):
	year=inputInt("Insert year: ")
	arvorePais.searchYears(year)

#Prints data of a country of a given year
def searchSpecific(arvorePais):
	country=str(input("Insert Country: "))
	year=inputInt("Insert year: ")
	node = arvorePais.countrySearch(country)
	if node !=False:
		if node.getYears().yearSearch(year) != None:
			print(node.getYears().yearSearch(year).getData(),"%")
	else:
		print("404 - Country not found!")

#Prints all the information of the tree (countries, years and respective data)
def printAll(arvorePais):
	arvorePais.displayAll()

#Prints the years and values of a country between the limit provided
def valuesInRange(arvorePais):
	country = str(input("Insert Country: "))
	min=inputFloat("Minimum value: ")
	max=inputFloat("Minimum value: ")
	node=arvorePais.countrySearch(country)
	if node != None:
		node.getYears().getValuesInRange(min,max)


#finds a year and changes its year
def editYear(arvorePais):
	country = str(input("Insert Country: "))
	year=inputInt("Choose year: ")
	newYear=inputInt("Insert New year: ")
	node = arvorePais.countrySearch(country)
	if node != False:
		if node.getYears().yearSearch(year) != None:
			oldValue=node.getYears().yearSearch(year).getData()
			node.getYears().delete(year)
			node.getYears().insertYears(newYear,oldValue)
		else:
			print("404 - Year not found!")
	else:
		print("country not found")

#finds a year and changes its value
def editData(arvorePais):
	country = str(input("Insert Country: "))
	year = inputInt("Choose year: ")
	newData = inputInt("Insert New data: ")
	node = arvorePais.countrySearch(country)
	if node!=False:
		if node.getYears().yearSearch(year) != None:
			node.getYears().yearSearch(year).setData(newData)
		else:
			print("404 - Year not found!")
	else:
		print("country not found")

#deltes a country
def deleteCountry(arvorePais):
	country = str(input("Insert Country to delete: "))
	arvorePais.delete(country)

#Deletes a year
def deleteYear(arvorePais):
	country=str(input("Insert Country to delete: "))
	year=inputInt("Insert year to delete: ")
	node = arvorePais.countrySearch(country)
	if node!=False:
		if node.getYears().yearSearch(year) != None:
			node.getYears().delete(year)
	else:
		print("404 - country not found!")

#adds a year and data to a country
def addYears(arvorePais):
	country = str(input("Insert Country to add: "))
	node=arvorePais.countrySearch(country)
	year=inputInt("Insert new year: ")
	data=inputFloat("Insert respective data:  ")
	if node!=False:
		node.getYears().insertYears(year,data)
	else:
		print("404 - Country not found!")

#Adds a country to the tree
def addCountry(arvorePais):
	country=str(input("Insert Country to add: "))
	tag=str(input("Insert the tag of the country: "))
	arvorePais.insertCountry(country, tag, None)

#prints all the countries and their tags
def printCountries(arvorePais):
	arvorePais.displayCountry()


#Adds nYears years to a certain country and times the process
def benchmarkingAddYears(arvorePais):
    nYears = inputInt("\nNumber of years to add:\n>")
    start = time.time()
    yearsTree = arvorePais.countrySearch("Portugal").getYears()
    for i in range(nYears):
        yearsTree.insertYears(i, i)
    end = time.time()
    print('Done in ' + str(end - start),'seconds...')
	#deltes the added values
    benchmarkingSearchYears(yearsTree, nYears)

def benchmarkingSearchYears(yearsTree, nYears):
	start = time.time()
	for i in range(nYears):
		yearsTree.yearSearch(i)

	end = time.time()
	print('[Searched] - Done in ' + str(end - start) + ' seconds...')
	benchmarkingRemoveYears(yearsTree, nYears)

#Removes nYears years and times the process
def benchmarkingRemoveYears(yearsTree, nYears):
    start = time.time()
    for i in range(nYears):
        yearsTree.delete(i)

    end = time.time()
    print('[REMOVE] - Done in ' + str(end - start) + ' seconds...')

#Adds nCountries countries to the tree and times the process
def benchmarkingAddCountries(arvorePais):
    nCountries = inputInt("\nNumber of countries to add:\n>")
    start = time.time()
    for i in range(nCountries):
        arvorePais.insertCountry(str(i), str(i),None)
    end = time.time()
    print('Added all the countries in ' + str(end - start) + ' seconds...')
	#removes the added countries
    benchmarkingSearchCountries(arvorePais, nCountries)


def benchmarkingSearchCountries(arvorePais, nCountries):
    start = time.time()
    for i in range(nCountries):
        arvorePais.countrySearch(str(i))
    end = time.time()
    print('Searched all the countries in ' + str(end - start) + ' seconds...')
    benchmarkingRemoveCountries(arvorePais, nCountries)

#Removes nCountries countries and times the process
def benchmarkingRemoveCountries(arvorePais, nCountries):
    start = time.time()
    for i in range(nCountries):
        arvorePais.delete(str(i))
    end = time.time()
    print('Removed all the countries in ' + str(end - start) + ' seconds...')