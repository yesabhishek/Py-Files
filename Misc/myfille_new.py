# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:42:06 2020

@author: achoud3
"""

#Prod
[DEFAULT]
json_key_path = r"C:\Users\achoud3\Documents\Project_Data_Engineering\Key_path\shc-enterprise-data-lake-dev-2dbbaaacf689.json"

#dev
#[DEFAULT]
#json_key_path =/appl/hdlakeqa/shc-enterprise-data-lake-dev/integration/ETL_SPANNER/common/key/shc-enterprise-data-lake-dev-2dbbaaacf689.json

[Spanner]
#dev
#spanner_instance_name = edlspanner
#spanner_database_name = edl-integration

#prod
spanner_instance_name = edl-spanner-prod
spanner_database_name = shc-edl-etl-integration

date_query = select cast(cast(EDLCreatedTimestamp as timestamp)as date) as EDLCreatedDate from SurveyQuestion where cast(cast(EDLCreatedTimestamp as timestamp)as date) = '$o_date' or cast(cast(EDLUpdatedTimestamp as timestamp)as date)= '$o_date' group by 1

spanner_query =  select SurveyQuestionID, SurveyID, QuestionSortOrder, QuestionText, QuestionComments, AnswerDataType,  SUBSTR(cast(QuestionActiveDate as String), 1,19)  as QuestionActiveDate, QuestionInactiveDate, EDLCreatedTimestamp, EDLUpdatedTimestamp from SurveyQuestion where cast(cast(EDLCreatedTimestamp as timestamp)as date) in ($dates)

#Prod
csv_file_path = r"C:\Users\achoud3\Documents\Project_Data_Engineering\Survey_SurveyQuestion.csv"

# Dev
#csv_file_path = /appl/hdlakeqa/shc-enterprise-data-lake-dev/integration/ETL_SPANNER/Survey/Datafiles/Survey_SurveyQuestion.csv

bq_temp_delete_query =  delete FROM IntegrationTemp.Survey_SurveyQuestion where  1=1

bq_delete_query = delete FROM Customer.SurveyQuestion a where  exists ( select 1 from IntegrationTemp.Survey_SurveyQuestion b where a.SurveyQuestionID  = b.SurveyQuestionID )

bq_insert_from_temp_query = insert into Customer.SurveyQuestion select * from IntegrationTemp.Survey_SurveyQuestion

performance_flag = True
uuid_column = SurveyQuestionID




[Bigquery]
bq_location = US
bq_dataset = Customer
bq_table = SurveyQuestion
bq_dataset_tmp = IntegrationTemp
bq_table_temp = Survey_SurveyQuestion
bq_pk_column = SurveyQuestionID
job_name = Sp-Bq-Survey-SurveyQuestion




def spanner_to_bq_main(spanner_query, bq_location, date_query, csv_file_path, bq_dataset, bq_table, bq_dataset_tmp , bq_table_temp ,bq_pk_column , bq_temp_delete_query , bq_delete_query , bq_insert_from_temp_query,performance_flag,uuid_column):
        """
                This function will trigger the data movement from spanner to bq
                by creating the csv file in unix path
                Then bq will load data from that csv file.
                Arguments
                ---------
                1.
                2.
        """
        dates_string = get_dates_from_spanner(date_query)
        spanner_to_csv(spanner_query, dates_string, csv_file_path,performance_flag,uuid_column)
        print("CSV file created at path : " + str(csv_file_path))
        print( "Loading csv data into " + "Bq Dataset:" + str(bq_dataset) + " Bq Table:" + str(bq_table) )
        # sys.exit()
        delete_temp_bq(bq_location, bq_temp_delete_query)
        csv_to_bq(csv_file_path, bq_location , bq_dataset_tmp, bq_table_temp)
        delete_exist_bq(bq_location, bq_delete_query)
        insert_bq_tmp_to_bq_integration(bq_location, bq_insert_from_temp_query)


def csv_to_bq(csv_file_path, bq_location , bq_dataset, bq_table):
        """
                This function will trigger the data movement from csv to bq.
                Arguments
                ---------
                1. source_table
                2. target_table
        """
        global BQ_DATABASE_CONN
        filename = csv_file_path
        dataset_id = bq_dataset
        table_id = bq_table

        command = 'bq load --quote "" --format=csv --field_delimiter="|" ' + bq_dataset + "." + bq_table + ' ' + csv_file_path # the shell command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        #Launch the shell command:
        output, error = process.communicate()
        # print(output.decode('utf-8'), error.decode('utf-8'))
        # print(len(error.decode('utf-8')))
        if len(error.decode('utf-8')) != 0 and error.decode('utf-8').find("Waiting on bqjob_") == -1:
                print("Error occured during execution of below command \n Command: {} \n {}".format(command, error.decode('utf-8')))
                raise Exception
        else:
                print(output.decode('utf-8'))
                print("Loaded rows into {}:{}.".format(dataset_id, table_id))



        # proc = subprocess.Popen(["bq show --schema "  + str(bq_dataset) + "." + str(bq_table)], stdout=subprocess.PIPE, shell=True)
        # print("bq show --schema "  + str(bq_dataset) + "." + str(bq_table))
        # (out, err) = proc.communicate()
        # # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # # In future if outuput of this command changes, below logic needs to be changed.
        # out = out.decode('utf-8')
        # #print(out)
        # #print([str(x[1:] + "}") for x in out.replace("]","").replace("\n","").split("}")[:-1] ])
        # final_bq_schema_list = [ast.literal_eval(str(x[1:] + "}")) for x in out.replace("]","").replace("\n","").split("}")[:-1] ]
        # # bq_column_names = [x['name'] for x in final_bq_schema_list]
        # # validate each column in spanner config section is present in bq table
        # # spanner_column_list = [str(x).strip() for x in str(spanner_columns).split(",")]
        # # for item in spanner_column_list:
        # #        if item not in bq_column_names:
        # #                print("Spanner Column : " + str(item) + " not present in Bq Dataset:" + str(bq_dataset) + " Bq Table:" + str(bq_table) )
        # #                sys.exit()
        # #print(final_bq_schema_list)
        # dataset_ref = BQ_DATABASE_CONN.dataset(dataset_id)
        # table_ref = dataset_ref.table(table_id)
        # job_config = bigquery.LoadJobConfig()
        # job_config.source_format = bigquery.SourceFormat.CSV
        # job_config.skip_leading_rows = 0
        # job_config.autodetect = True



        # schema_list=[]
        # schema_main = []

        # for x in final_bq_schema_list:
        #         if 'mode' in x.keys():
        #                 schema_main.append(bigquery.SchemaField(x['name'], x['type'], x['mode']))
        #         else:
        #                 schema_main.append(bigquery.SchemaField(x['name'],x['type']))

        # #print(schema_main)

        # job_config.schema = schema_main

        # #job_config.schema = [bigquery.SchemaField(x['name'], x['type']) for x in final_bq_schema_list]
        # #job_config.schema = [
        #                 # bigquery.SchemaField("PartyRoleAssignmentID","STRING","REQUIRED"),
        #                 # bigquery.SchemaField("PartyID","STRING","REQUIRED"),
        #                 # bigquery.SchemaField("PartyRoleTypeCode","STRING","REQUIRED"),
        #                 # bigquery.SchemaField("StatusCode","STRING"),
        #                 # bigquery.SchemaField("EffectiveDate","DATE"),
        #                 # bigquery.SchemaField("ExpirationDate","DATE"),
        #                 # bigquery.SchemaField("EDLCreatedTimestamp","TIMESTAMP","REQUIRED"),
        #                 # bigquery.SchemaField("EDLUpdatedTimestamp","TIMESTAMP","REQUIRED")
        #          #]
        # print("Schema : ",job_config.schema)
        # #sys.exit()
        # with open(filename, "rb") as source_file:
        #         print("source_file : ",source_file)
        #         job = BQ_DATABASE_CONN.load_table_from_file(source_file, table_ref, job_config=job_config)

        # job.result()  # Waits for table load to complete.

        # print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))
