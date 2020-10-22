import argparse
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time, sys, os, subprocess
from datetime import date
import datetime
import uuid
from google.cloud import spanner
from google.api_core.exceptions import ClientError
from google.oauth2 import service_account
from google.cloud import bigquery
from google.api_core import exceptions
import logging
import calendar



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



#Adding Logger
#handler = logging.FileHandler('/logs/hddlake/integration/ETL_SPANNER/SellableUnit/ETL_SellableUnit_StockItem_Data_' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log', mode='w')
handler = logging.FileHandler(r'C:\Users\achoud3\PyFiles\Project\SellableUnit1\ETL_SellableUnit_SearsHierarchy_Data_' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log', mode='w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
handler.setFormatter(formatter)




logger.addHandler(handler)

output_handler = logging.StreamHandler(sys.stdout)
output_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)d] - %(message)s')
output_handler.setFormatter(formatter)

logger.addHandler(output_handler)



#Initialization Part
#key_path = '/appl/hddlake/shc-enterprise-data-lake/integration/ETL_SPANNER/common/key/shc-enterprise-data-lake-fdeadb45bc59.json'
key_path = r'C:\Users\achoud3\Py Files\Json Keys\shc-enterprise-data-lake-dev-2dbbaaacf689.json'

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
instance_id='edl-spanner-dev'
database_id='shc-edl-etl-integration'

today = date.today()
odate = today.strftime("%Y-%m-%d")

SP_CLIENT_CONN = spanner.Client(credentials=credentials,project=credentials.project_id)
SP_INSTANCE_CONN = SP_CLIENT_CONN.instance(instance_id)
SP_DATABASE_CONN = SP_INSTANCE_CONN.database(database_id)

BQ_CLIENT_CONN = bigquery.Client(credentials=credentials,project=credentials.project_id)






#---date YYYYMMDD to standard formart
def YYYYMMDD_SD(date_str):

    tmp=datetime.datetime.strptime(date_str, '%Y%m%d').date()
    sFormat=str(tmp.strftime('%Y-%m-%d'))
    return sFormat



def dateCheck(value):
    #print("DT type :{} : {} : {}".format((value is None),(value=='None'),value))
    if value is None or value.strip() =='' or value=='None' or value=='null' or value=='Null':
        value='1900-01-01'
    else:
        value=str(value)
    #print("DT value :",value)
    return value



def stringCheck(value):
    #print("Str type :{} : {} : {} : {}".format((value is None),(value=='None'),(str(value).strip() ==''),value))
    if value is None or str(value).strip() =='' or value=='None' or value=='null' or value=='Null':
        value=-1
    else:
        value=str(value)
    #print("Str value :",value)
    return value





def utc_time_Check(value):
    #print("Time type :{} : {} ".format((value is None),(value=='None'),value))
    if value is None or value=='None' or value=='null':
        value=null
    else:
        value=str(value)
    #print("Time value :",value)
    return value




def numCheck(value):
    #print("Num type :{} : {} ".format(type(value),value))
    if value is None or value =='' or value=='None':
        value=-1
    #print("Num value :",value)
    return value




def boolCheck(value):
    #print("Bool type :{} : {} ".format(type(value),value))
    if value is None or value =='' or value=='None':
        value=False
    #print("Bool value :",value)
    return value


#Julian date conversion

def date_julian7_conv(date_str):
    
    tmp = str(date_str)
    dFormat='9999-12-31'
    if tmp =='' or tmp ==' ':
        return dFormat
    else:
        try:
            tmp=tmp.zfill(7)
            d1=int(tmp[-3:])
            y1=int(tmp[:4])
        except ValueError:
            return dFormat
    if tmp =='0000000':
        return dFormat
    elif d1 > 366:
        return dFormat
    else:
        month = 1
        try:
            while d1 - calendar.monthrange(y1,month)[1] > 0 and month <= 12:
                d1 = d1 - calendar.monthrange(y1,month)[1]
                month = month + 1
        except:
            return dFormat
        month=str(month).zfill(2)
        d1=str(d1).zfill(2)
        sFormat="'"+str(str(y1)+'-'+month+'-'+d1)+"'"
    return  sFormat







if __name__ == '__main__':
    parser = argparse.ArgumentParser(
           description=__doc__,
           formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
           'odate', help='',default='YYYY-MM-DD')
    parser.add_argument(
           'UpdateORNot', help='',default='False')
    args = parser.parse_args()   
#    odate=20190928
    
    query="""SELECT MerchandiseHierarchyFunctionID FROM SellableUnit.MerchandiseHierarchyFunction
    WHERE MerchandiseHierarchyFunctionName = 'Sears'"""
    query_job = BQ_CLIENT_CONN.query(
        query,
#        location="US",
    )
    FunctionID = [str(x[0]) for x in query_job]
    MerchandiseHierarchyFunctionID = FunctionID[0]
    
    MerchandiseHierarchyFunctionID =stringCheck(MerchandiseHierarchyFunctionID)
    
    query="""
    
    
    Select Max(MHLevelId_Class) As MHLevelId_Class, Max(MHLevelId_SubLine) As MHLevelId_SubLine,  
    Max(MHLevelId_Line) As MHLevelId_Line, Max(MHLevelId_Division) As MHLevelId_Division, Max(MHLevelId_Business) As MHLevelId_Business
    From
    (SELECT MerchandiseHierarchyLevelID as MHLevelId_Class, '' As  MHLevelId_SubLine,  '' As  MHLevelId_Line,  '' As  MHLevelId_Division,  '' As  MHLevelId_Business
    FROM SellableUnit.MerchandiseHierarchyLevel
    WHERE MerchandiseHierarchyLevelName = 'Class' And MerchandiseHierarchyFunctionID = '%s'
    UNION ALL
    SELECT '' as MHLevelId_Class, MerchandiseHierarchyLevelID As  MHLevelId_SubLine,  '' As  MHLevelId_Line,  '' As  MHLevelId_Division,  '' As  MHLevelId_Business
    FROM SellableUnit.MerchandiseHierarchyLevel
    WHERE MerchandiseHierarchyLevelName = 'SubLine' And MerchandiseHierarchyFunctionID = '%s'
    UNION ALL
    SELECT '' as MHLevelId_Class, '' As  MHLevelId_SubLine,  MerchandiseHierarchyLevelID As  MHLevelId_Line,  '' As  MHLevelId_Division,  '' As  MHLevelId_Business
    FROM SellableUnit.MerchandiseHierarchyLevel
    WHERE MerchandiseHierarchyLevelName = 'Line' And MerchandiseHierarchyFunctionID = '%s'
    UNION ALL
    SELECT '' as MHLevelId_Class, '' As  MHLevelId_SubLine,  '' As  MHLevelId_Line,  MerchandiseHierarchyLevelID As  MHLevelId_Division,  '' As  MHLevelId_Business
    FROM SellableUnit.MerchandiseHierarchyLevel
    WHERE MerchandiseHierarchyLevelName = 'Division' And MerchandiseHierarchyFunctionID = '%s'
    UNION ALL
    SELECT '' as MHLevelId_Class, '' As  MHLevelId_SubLine,  '' As  MHLevelId_Line,  '' As  MHLevelId_Division,  MerchandiseHierarchyLevelID As  MHLevelId_Business
    FROM SellableUnit.MerchandiseHierarchyLevel
    WHERE MerchandiseHierarchyLevelName = 'Business' And MerchandiseHierarchyFunctionID = '%s'
    
    )C


    
    """ %(MerchandiseHierarchyFunctionID, MerchandiseHierarchyFunctionID,MerchandiseHierarchyFunctionID,
    MerchandiseHierarchyFunctionID,MerchandiseHierarchyFunctionID)
    
    query_job = BQ_CLIENT_CONN.query(
        query,
#        location="US",
    )
#    LevelID=list(query_job)
    
    LevelID = [x for x in query_job]
    for x in LevelID:   

        MerchandiseHierarchyLevelID_Class =str(x[0]) 
        MerchandiseHierarchyLevelID_SubLine = str(x[1]) 
        MerchandiseHierarchyLevelID_Line = str(x[2]) 
        MerchandiseHierarchyLevelID_Division = str(x[3]) 
        MerchandiseHierarchyLevelID_Business = str(x[4]) 
    
    MerchandiseHierarchyLevelID_Class =stringCheck(MerchandiseHierarchyLevelID_Class)
    MerchandiseHierarchyLevelID_SubLine = stringCheck(MerchandiseHierarchyLevelID_SubLine)
    MerchandiseHierarchyLevelID_Line = stringCheck(MerchandiseHierarchyLevelID_Line)
    MerchandiseHierarchyLevelID_Division = stringCheck(MerchandiseHierarchyLevelID_Division)
    MerchandiseHierarchyLevelID_Business = stringCheck(MerchandiseHierarchyLevelID_Business)


