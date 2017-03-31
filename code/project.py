import stacks as stacks
import doubleLinkedLists as dll
import AVL_Func as AVL


def inputInt(string):
    while True:
        try:
            num = int(input(string))
        except ValueError:
            print("Error... Please try again...")
            continue
        else:
            return num


def loadStructures():  # loads the structures to be used in the program
    DoubleLinkedLists = dll.loadCsv()
    stack = stacks.loadStrut()# chage this for the load
    stack.invert(stacks.stackCountries())
    countriesAVL = AVL.load() # chage this for the load
    tagDic= AVL.loadToDict()

    return [stack, DoubleLinkedLists, countriesAVL, tagDic]	#countriesAVL + tagDic == sopas


def menuDataStrut():
    while True:
        print("\nWhich one of the following data structure you want want to use?")
        print("1 - Stack of Stacks")
        print("2 - DoubleLinkedList of DoubleLinkedLists")
        print("3 - AVL tree of AVL trees")
        print("0 - Quit")
        structPicked = inputInt("> ")
        if structPicked == 0 or structPicked == 1 or structPicked == 2 or structPicked == 3:
            break
        else:
            print("Option not available... Try Again...\n")

    return structPicked


def menu(countriesStack, countriesList, countriesAVL, structPicked, tagDic):
    while True:
        print("\n---------------------------------------------------\nMENU")
        print("1  - Search all the years with available information of one country;")
        print("2  - Search all the countries information of one year;")
        print("3  - Search one year information of one country;")
        print("4  - Search all the years of all the countries;")
        print("5  - Search a range of percentages of one country;")
        print("6  - Edit year of a country;")
        print("7  - Edit year's respective percentage of a country;")
        print("8  - Remove one country;")
        print("9  - Remove one year of one country;")
        print("10 - Add one country;")
        print("11 - Add one pair [Year, Percentage] to a country;")
        print("12 - BENCHMARKING - Add, search and remove 'x' years;")
        print("13 - BENCHMARKING - Add, search and remove 'x' countries;")
        print("0  - Quit")
        choice = inputInt("> ")

        # delete the "continues"
        if choice == 1:
            if structPicked == 1:
                countriesStack.search('', 0)
            elif structPicked == 2:
                dll.allYearsFromCountry(countriesList)
            elif structPicked == 3:
                AVL.dataOfCountry(countriesAVL)

        elif choice == 2:
            if structPicked == 1:
                countriesStack.displayInfoForYear()
            elif structPicked == 2:
                dll.allCountryFromYear(countriesList)
            elif structPicked == 3:
                AVL.valuesOfYear(countriesAVL)


        elif choice == 3:
            if structPicked == 1:
                countriesStack.search('', 7)
            elif structPicked == 2:
                dll.oneYearFromOneCountry(countriesList)
            elif structPicked == 3:
                AVL.searchSpecific(countriesAVL)

        elif choice == 4:
            if structPicked == 1:
                countriesStack.displayInfo()
            elif structPicked == 2:
                dll.allYearsFromAllCountries(countriesList)
            elif structPicked == 3:
                AVL.printAll(countriesAVL)

        elif choice == 5:
            if structPicked == 1:
                countriesStack.search('', 8)
            elif structPicked == 2:
                dll.RangeOfDataOfOneCountry(countriesList)
            elif structPicked == 3:
                AVL.valuesInRange(countriesAVL)

        elif choice == 6:
            if structPicked == 1:
                countriesStack.search('', 6)
            elif structPicked == 2:
                dll.editYearOfACountry(countriesList)
            elif structPicked == 3:
                AVL.editYear(countriesAVL)
                countriesAVL.rebalance()

        elif choice == 7:
            if structPicked == 1:
                countriesStack.search('', 2)
            elif structPicked == 2:
                dll.editValueOfAYear(countriesList)
            elif structPicked == 3:
                AVL.editData(countriesAVL)

        elif choice == 8:
            if structPicked == 1:
                countriesStack.search('', 5)
            elif structPicked == 2:
                dll.removeCountry(countriesList)
            elif structPicked == 3:
                AVL.deleteCountry(countriesAVL)

        elif choice == 9:
            if structPicked == 1:
                countriesStack.search('', 3)
            elif structPicked == 2:
                dll.removeYearFromCountry(countriesList)
            elif structPicked == 3:
                AVL.deleteYear(countriesAVL)

        elif choice == 10:
            if structPicked == 1:
                countriesStack.addCountry()
            elif structPicked == 2:
                dll.addCountry(countriesList)
            elif structPicked == 3:
                AVL.addCountry(countriesAVL)

        elif choice == 11:
            if structPicked == 1:
                countriesStack.search('', 1)
            elif structPicked == 2:
                dll.addYearToCountry(countriesList)
            elif structPicked == 3:
                AVL.addYears(countriesAVL)

        elif choice == 12:
            if structPicked == 1:
                stacks.benchmarkingAddYearsStart(countriesStack)
                stacks.benchmarkingAddYearsEnd(countriesStack)
            elif structPicked == 2:
                dll.benchmarkingAddYearsStart(countriesList)
                dll.benchmarkingAddYearsEnd(countriesList)
            elif structPicked == 3:
                AVL.benchmarkingAddYears(countriesAVL)
        elif choice == 13:
            if structPicked == 1:
                stacks.benchmarkingAddCountries(countriesStack)
            elif structPicked == 2:
                dll.benchmarkingAddCountries(countriesList)
            elif structPicked == 3:
                AVL.benchmarkingAddCountries(countriesAVL)

        elif choice == 0:
            break

        else:
            print("Option not available... Try Again...\n")


def main():
    countriesStack, countriesList, countriesAVL, tagDic = loadStructures()

    while True:
        structPicked = menuDataStrut()
        if structPicked == 0:
            break
        menu(countriesStack, countriesList, countriesAVL, structPicked, tagDic)


if __name__ == '__main__':
	main()