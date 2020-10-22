
from google.cloud import bigquery
from google.api_core.exceptions import ClientError
from google.oauth2 import service_account
from google.api_core import exceptions
import pandas as pd
import multiprocessing



def trigger_function():
    
    key_path= r"C:\Users\achoud3\Documents\Project_Data_Engineering\Key_path\shc-enterprise-data-lake-dev-2dbbaaacf689.json"
    
    credentials = service_account.Credentials.from_service_account_file(
                key_path,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
    project_id='shc-enterprise-data-lake-dev'
    BQ_CLIENT =bigquery.Client(credentials= credentials,project=project_id)


    #table = 'PlaceVendor_Vend_Locn_Data'
    query_job = BQ_CLIENT.query("""SELECT
    * FROM `shc-enterprise-data-lake-dev.PreIntegration.PlaceVendor_Vend_Locn_Data` 
     order by Occ_Id desc limit 10""")

    results = query_job.result()
 
#    for i in results:
#        print(i)
    print("Total rows available: ", results.total_rows)

    records=[]
    for r in query_job:
        each_df_columns = [x for x in r.keys()]
        records.append([x for x in r.values()])
        
    if len(records) > 0:
        Vendor_Vendor_df = pd.DataFrame(data=records, columns=each_df_columns)
    else:
        Vendor_Vendor_df = pd.DataFrame()
        
    #print(Vendor_Vendor_df)
    #print(Vendor_Vendor_df)
    threshhold=3
    splitted_df = [Vendor_Vendor_df.loc[i:i+threshhold-1,:] for i in range(0, \
				   Vendor_Vendor_df.shape[0],threshhold)]
    #print(splitted_df)
    no_of_process=2
    threshhold2 = no_of_process
    final_list = [[i,i+threshhold2-1] for i in range(0,len(splitted_df),threshhold2)]
    print(final_list)
    #(0,1),(2,3)
    for item in final_list:
        print(item)
        for each_member_df in splitted_df[item[0]:item[1] + 1]:
            processes = []
            processes.append(multiprocessing.Process
                             (target=create_spanner_connection_SurveyResponseText
                              , args=(each_member_df,odate,)) )
			# completed_member_number += 1
            print(processes)
            # Run processes
            for p in processes:
                p.start()
            # Exit the completed processes
        for p in processes:
            p.join() 
if __name__ == '__main__':
    
    trigger_function()
    
    
    
    
