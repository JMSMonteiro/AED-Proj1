#@source: https://github.com/recluze/python-avl-tree/blob/master/simple_avl.py
outputdebug = False 

def debug(msg):
    if outputdebug:
        print (msg)

#Node of the country AVL
class countryNode():
    def __init__(self, country, tag, years):
        self.country = country
        self.tag = tag
        self.years = years
        self.left = None 
        self.right = None 

    #Returns the name of the current country
    def getCountry(self):
        return self.country

    #Returns the tag of the current country
    def getTag(self):
        return self.tag

    #Returns the node's AVL of years
    def getYears(self):
        return self.years

    #Sets the year tree to a provided tree
    #@param years - AVL tree
    def setYears(self,years):
        self.years=years

    #Returns the left child of the node
    def getLeft(self):
        return self.left

    #Returns the right child of the node
    def getRight(self):
        return self.right

#AVL Tree class
class AVLTreeCountry():
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        self.height = 0
        return (self.height)

    #inserts a new Country
    #@param country - String: name of the country
    #@param tag - String: tag of the country
    #@param years - AVLTreeYears: Tree with all the years and data
    def insertCountry(self, country, tag, years):
        tree = self.node

        newnode = countryNode(country, tag, years)

        if tree == None:
            self.node = newnode
            self.node.left = AVLTreeCountry()
            self.node.right = AVLTreeCountry()
            debug("Inserted key [" + str(country) + "]")

        elif country < tree.getCountry():
            self.node.left.insertCountry(country, tag, years)

        elif country > tree.getCountry():
            self.node.right.insertCountry(country, tag, years)

        else:
            debug("Key [" + str(country) + "] already in tree.")

        self.rebalance()

    #prints all of the tree and sub-trees
    def displayAll(self):
        if (self.node != None):
            print("\nCountry: ", self.node.getCountry())
            self.node.getYears().display()
            if self.node.left != None:
                self.node.left.displayAll()
            if self.node.left != None:
                self.node.right.displayAll()

    #prints all the countries' name and tag
    def displayCountry(self):
        if(self.node != None):
            print ("\nCountry:",self.node.getCountry(),"- Tag:",self.node.getTag())
            if self.node.left != None:
                self.node.left.displayCountry()
            if self.node.left != None:
                self.node.right.displayCountry()

    #Returns the node correspondent to a given name
    #(searches for the country and returns the name when found, if not found returns False)
    def countrySearch(self, country):
        tree = self.node

        if tree:
            if tree.getCountry() == country:
                return tree

            elif country < tree.getCountry():
                return self.node.left.countrySearch(country)

            elif country > tree.getCountry():
                return self.node.right.countrySearch(country)
        else:
            return False

    #Searches for a year and it's value in all of the countries
    #prints results
    def searchYears(self, year):
        tree = self.node
        if tree != None:
            if tree.getYears().yearSearch(year):
                print("Country:",tree.getCountry(), "Data:", tree.getYears().yearSearch(year).getData())
            if tree.getLeft() != None:
                tree.getLeft().searchYears(year)
            if tree.getRight() != None:
                tree.getRight().searchYears(year)

    #Rebalances the tree when something is removed or added
    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.country) + ' right')
        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug('Rotating ' + str(self.node.country) + ' left')
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    #Removes a country from the tree
    def delete(self, country):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None:
            if self.node.country == country:
                debug("Deleting ... " + str(country))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        debug("Found replacement for " + str(country) + " -> " + str(replacement.country))
                        self.node.country = replacement.country

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.country)

                self.rebalance()
                return
            elif country < self.node.country:
                self.node.left.delete(country)
            elif country > self.node.country:
                self.node.right.delete(country)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.country))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.node == None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.country)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist




#-------------------------------------------------------------------------------------XXXXXXXX----------------------------------------------------------------------------------------------------------------#


#Node of the year AVL
class yearNode:
    def __init__(self, year = None, data = None):
        self.year = year
        self.data = data
        self.left = None
        self.right = None

    #Retrns the year of the current node
    def getYear(self):
        return self.year

    #Returns the Data of the current node(year)
    def getData(self):
        return self.data

    #Returns the right child of the node
    def getRight(self):
        return self.right

    #Returns the left child of the node
    def getLeft(self):
        return self.left

    #Sets the value of the current year
    #@param data - Float: percentage correspondent to the year
    def setData(self, data):
        self.data = data

    #Sets the year of the current node to a new Year
    #@param year - int: new year
    def setYear(self, year):
        self.year=year



class AVLTreeData():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0)

    def display(self):
        if(self.node != None):
            print ("Year:",self.node.getYear(),"- Data:",self.node.getData())
            if self.node.left != None:
                self.node.left.display()
            if self.node.left != None:
                self.node.right.display()


    #Inserts a new year(node) in the AVL tree
    #@param year - int: year to be added
    #@param data - float: percentage correspondent to the year
    def insertYears(self, year, data):
        tree = self.node
        
        newnode = yearNode(year, data)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTreeData() 
            self.node.right = AVLTreeData()
            debug("Inserted key [" + str(year) + "]")
        
        elif year < tree.year: 
            self.node.left.insertYears(year, data)
            
        elif year > tree.year: 
            self.node.right.insertYears(year, data)
        
        else: 
            debug("Key [" + str(year) + "] already in tree.")
            
        self.rebalance()

    #Searches for a given year in the tree
    #param year - int: year to be searched for
    def yearSearch(self,year):
        tree=self.node
        if tree:
            if tree.getYear() == year:
                return tree

            elif year < tree.getYear():
                return self.node.left.yearSearch(year)

            elif year > tree.getYear():
                return self.node.right.yearSearch(year)

    #Prints all the years which values are in a provided range
    #@param min - float: minimum percentage
    #@param mac - float: maximum percentage
    def getValuesInRange(self,min,max):
        tree=self.node
        if tree:
            if float(tree.getData())>=min and float(tree.getData())<=max:
                print("Year:",tree.getYear(),"Data:",tree.getData())
            if tree.getLeft()!= None:
                tree.getLeft().getValuesInRange(min,max)
            if tree.getRight() != None:
                tree.getRight().getValuesInRange(min,max)

    #Rebalances the tree when a node is added or deleted
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.year) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.year) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 

    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    #Deletes a year from the tree
    #@param year - int: year to be deleted
    def delete(self, year):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.year == year: 
                debug("Deleting ... " + str(year))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(year) + " -> " + str(replacement.year))  
                        self.node.year = replacement.year 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.year)
                    
                self.rebalance()
                return  
            elif year < self.node.year: 
                self.node.left.delete(year)  
            elif year > self.node.year: 
                self.node.year.delete(year)
                        
            self.rebalance()
        else: 
            return 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.year))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.year)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 


