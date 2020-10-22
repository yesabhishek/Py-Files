
def hello_decorator(func): 
	def inner1(): 
		print("Hello, this is before function execution") 
		func() 
        nt("This is after function execution") 
		
	return inner1 


### defining a function, to be called inside wrapper 
##def function_to_be_used(): 
##	print("This is inside the function !!") 
##
##
### passing 'function_to_be_used' inside the 
### decorator to control its behavior 
##function_to_be_used = hello_decorator(function_to_be_used) 
##
##
### calling the function 
##function_to_be_used() 
##
##fields_dict = {'VendorID':"'12'",'VendorName':"'1234'"
##,'SpStatus':"'I'" ,'SpModelName':"'Vendor'",'SpSourceName':"'Vendor'"}
##print(fields_dict)
##
##Insert_Vendor_query="INSERT Vendor ( " + ",".join([str(x) for x in fields_dict.keys()]) + ") Values(" + ",".join([str(x) for x in fields_dict.values()])  + ")"
##        
##print(Insert_Vendor_query)
#import time
#from datetime import date
#import datetime
#def insert_string(data):
#    if data == None:
#        data = "NULL"
#    elif data.find("\\") != -1 and  data.find("'") != -1:
#        data = str(data.replace("\\","\\\\"))
#        data = "'" + str(data.replace("'","\\'")) + "'"
#    elif data.find("'") != -1 :
#        data = "'" + str(data.replace("'","\\'")) + "'"
#    elif data.find("\\") != -1 :
#        data = "'" + str(data.replace("\\","\\\\")) + "'"
#    else:
#        data = "'" + data + "'"
#    return data
#
#def insert_Vendor_Vendor_df(odate):
#   
#    ts = (datetime.datetime.now() - datetime.timedelta(hours=12, minutes=30)).strftime("%H:%M:%S")
#    odate_EDLUpdatedTimestamp = "'" + str(odate) + " " + str(ts) + "'"
#    odate_EDLCreatedTimestamp = odate_EDLUpdatedTimestamp
#    
#    print(odate_EDLUpdatedTimestamp)
#    print(odate_EDLCreatedTimestamp)
#    
#    Insert_Vendor_query = ""
#        
#    fields_dict = {'VendorID':insert_string(['VendorID']),'VendorName':insert_string(['VendorName']),'EDLCreatedTimestamp':odate_EDLCreatedTimestamp ,'EDLUpdatedTimestamp':odate_EDLUpdatedTimestamp,'SpStatus':"'I'" ,'SpModelName':"'Vendor'",'SpSourceName':"'Vendor'"}
#    Insert_Vendor_query="INSERT Vendor ( " + ",".join([str(x) for x in fields_dict.keys()]) + ") Values(" + ",".join([str(x) for x in fields_dict.values()])  + ")"
#        
#    print(Insert_Vendor_query)
#    print(fields_dict)
#
#insert_Vendor_Vendor_df(20200119)
#
#
#
#
#    
#




#def insert_integer(data):
#    if data == None:
#        data = "NULL"
#    else:
#        data = str(data)
#    return data
#
#insert_insert()    