#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb
Department.drop_table()
Department.create_table()
#creating instances
#payroll = Department("Payroll", "Building A, 5th Floor")
#print(payroll) #print before save will return the row with id as None

#payroll.save()
#print(payroll)# print after save will assign object id attribute
 
#use create class method to combine instance and saving
payroll = Department.create("Payroll", "Building A, 5th Floor")

hr = Department.create("Human Resources", "Building C, East Wing")

#updating a table row
hr.name = 'HR'
hr.location = "Building F, 10th floor"
hr.update()

#deleting a table row
payroll.delete()



ipdb.set_trace()
