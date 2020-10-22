# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:47:07 2020

@author: achoud3
"""

import datetime  
CurrentDate=datetime.date.today()


Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
Previous_Date_Formatted = Previous_Date.strftime ('%Y%m%d') 
print ('Previous Date: ' + str(Previous_Date_Formatted))

#print(CurrentDate.strftime('Join My Birthday party on %A, %d-%B-%Y')) 



