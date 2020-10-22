'''import argparse
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time, sys, os, subprocess'''
from datetime import date
import datetime
#import uuid
from google.cloud import spanner
#from google.api_core.exceptions import ClientError
from google.oauth2 import service_account

from google.cloud import bigquery
#from google.api_core import exceptions
import logging
#from datetime import calendar


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Adding Logger
handler = logging.FileHandler('/logs/hdlakeqa/integration/ETL_SPANNER/SellableUnit/ETL_SellableUnit_StockItem_Data_' + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.log', mode='w')
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
key_path = '/appl/hdlakeqa/shc-enterprise-data-lake-dev/integration/ETL_SPANNER/common/key/shc-enterprise-data-lake-fdeadb45bc59.json'
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



def stringCheck(value):
    #print("Str type :{} : {} : {} : {}".format((value is None),(value=='None'),(str(value).strip() ==''),value))
    if value is None or str(value).strip() =='' or value=='None' or value=='null' or value=='Null':
        value=-1
    else:
        value=str(value)
    #print("Str value :",value)
    return value





if __name__ == '__main__':
#    parser = argparse.ArgumentParser(
#           description=__doc__,
#           formatter_class=argparse.RawDescriptionHelpFormatter)
#    parser.add_argument(
#           'odate', help='',default='YYYY-MM-DD')
#    parser.add_argument(
#           'UpdateORNot', help='',default='False')
#    args = parser.parse_args()   
    odate=20190928
    
    query="""SELECT MerchandiseHierarchyFunctionID FROM SellableUnit.MerchandiseHierarchyFunction
    WHERE MerchandiseHierarchyFunctionName = 'Sears'"""
    query_job = BQ_CLIENT_CONN.query(
        query,
#        location="US",
    )
    FunctionID = [str(x[0]) for x in query_job]
    MerchandiseHierarchyFunctionID = FunctionID[0]
    
    MerchandiseHierarchyFunctionID =stringCheck(MerchandiseHierarchyFunctionID)
    
    
