# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 00:31:36 2020

@author: achoud3
"""

import pandas as pd

person={
	"Name":["Abhishek",'Choudhury','AlphaCobra','RDX'],
	"Roll_no":[2,1,164101776,'achoud3'],
	"Email":["abhi.rock.the.world97@gmail.com",'choudhuryabhishek76@gmail.com','abhishek.choudhury@searshc.com'],
    "Hobby":["yes",'yes','no','yes']
	}
#print(person['Email'])



df = pd.DataFrame({ key:pd.Series(value) for key, value in person.items() })

#dict_df =pd.DataFrame([ pd.Series(value) for value in person ])

#print(df['Email'])
#print("----------------------------------------------------------------------------\n")
#print(df)
#print('............................................................................\n')
#
#print(df.Email)
#print('............................................................................\n')
#print(df.count())
#print('............................................................................\n')
#print(df.info())
#
#print('............................................................................\n')
#
#print(df[['Name','Email']])

#print('............................................................................\n')
#
#print(df.iloc[0]) #For printing out the rows by giving out the specific row number 
#print('............................................................................\n')
#print(df.iloc[0,1],[2])     #rows and colums

print(df['Hobby'].value_counts())



