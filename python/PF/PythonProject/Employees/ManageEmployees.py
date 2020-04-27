'''
Created on Jan 27, 2017

@author: kautilya.save

'''
from Flights.ManageFlights  import add #from packagename import modulename
add(101)

from Flights import ManageFlights #from packagename import modulename
ManageFlights.add(10)

import Flights.ManageFlights #import packagename.modulename
Flights.ManageFlights.add(10)

import Flights.Manage
import Employees.Manage
Flights.Manage.add(22)
Employees.Manage.add(43)

from Flights import Manage as FManage 
from Employees import Manage as EManage
FManage.add(3454) 
EManage.add(4542) 


from Flights.Manage import add as add123
from Employees.Manage import add as add212
add123(35334)
add212(342313)


Flights.Manage.sub(34, 24)

Employees.Manage.sub(23,12)


from Flights.Manage import sub as sub123

sub123(23,32)
