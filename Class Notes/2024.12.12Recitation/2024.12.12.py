#all methods constant except displayEmployees
#based on urgent queue
from DoublyLinkedList import *
from ChainingHashTableMap import *
class Company:

    def __init__(self):
        self.map = ChainingHashTableMap() #key value pairs of employees and departments


    def __len__(self):
        return len(self.map)

    def addEmployee(self, employee_name, dept_name):
        '''Hires new employee with assigned department'''
        self.map[employee_name] = dept_name

    def fire(self):
        '''Fires last employee added, return name of fired employee'''
        ...

    def fireFromPriorityDept(self):
        '''Fires last employee added to priority department'''

    def displayEmployees(self):
        '''Displays list of all company employees'''