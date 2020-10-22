#!/usr/bin/env python

import click
import concurrent.futures
import time, sys, os, subprocess
import configparser
import ast
import decimal
import datetime
import uuid
from google.cloud import spanner
from google.oauth2 import service_account
from google.cloud import bigquery
#import sys
#sys.exit()


SPANNER_INSTANCE_CONN = None
SPANNER_DATABASE_CONN = None
BQ_DATABASE_CONN = None
#config_path = '/appl/hdlakeqa/shc-enterprise-data-lake-dev/integration/ETL_SPANNER/Survey/Config/'
config_path = '/appl/hddlake/shc-enterprise-data-lake/integration/ETL_SPANNER/Survey/Config/'


CONTEXT_SETTINGS = dict(help_option_names=['/h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--bq_spanner/--spanner_bq', default=None, help='Inititiate functions for spanner to bq or bq to spanner dataflow')
@click.argument('config_file_path')
@click.argument('o_date')

def main(config_file_path, o_date, bq_spanner):
        '''
                This script will trigger the data movement from spanner to bq or bq to spanner.\n
                Examples- \n
                --------- \n
                1. python bq_spanner_bq_load.py config_file_path o_date --spanner_bq\n
                python bq_spanner_bq_load.py "\/home/auto/hdlakeqa/ashish/spanner/config_bq_spanner.ini"  --bq_spanner\n
                2. python bq_spanner_bq_load.py config_file_path o_date --bq_spanner\n
                python bq_spanner_bq_load.py "\/home/auto/hdlakeqa/ashish/spanner/config_spanner_bq.ini"  --spanner_bq
                Note:Please specify o_date in yyyy-mm-dd
        '''
        o_date=YYYYMMDD_SD(o_date)
        config_file_path = os.path.join(config_path, config_file_path)
        config = configparser.ConfigParser()
        print(config_file_path)
        if os.path.exists(config_file_path):
                config.read(config_file_path)
        else:
                print("Config file path : " + str(config_file_path) + " doesn't exists")
                sys.exit()

        if bq_spanner == None:
                print("Please provide --bq_spanner or --spanner_bq data movement option")
                sys.exit()
        try:
                json_key_path = config['DEFAULT']['json_key_path']
                spanner_instance_name = config['Spanner']['spanner_instance_name']
                spanner_database_name = config['Spanner']['spanner_database_name']
                create_bq_spanner_connection(json_key_path, spanner_instance_name, spanner_database_name)
                print("Connection established successfully to Spanner and Bq")
        except Exception as e:
                print("Connection Error : " + str(e))
        if bq_spanner:
                print("Executing BQ to Spanner dataflow.")
                bq_query = config['Bigquery']['bq_query']
                bq_query = bq_query.replace('$o_date', str(o_date))
                bq_location = config['Bigquery']['bq_location']
                bq_lookup_table = config['Bigquery']['bq_lookup_table']
                spanner_table = config['Spanner']['spanner_table']
                spanner_columns = config['Spanner']['spanner_columns']
                if bq_lookup_table.strip().lower() == 'false':
                        create_table_query = config['Spanner']['create_table_query']
                        create_database(config['Spanner']['spanner_table'], create_table_query)
                bq_to_spanner_main(bq_query, bq_location, spanner_table, spanner_columns)
        else:
                print("Executing Spanner to BQ dataflow.")
                spanner_query = config['Spanner']['spanner_query']
                date_query = config['Spanner']['date_query']
                bq_temp_delete_query = config['Spanner']['bq_temp_delete_query']
                bq_delete_query = config['Spanner']['bq_delete_query']
                bq_insert_from_temp_query = config['Spanner']['bq_insert_from_temp_query']
                date_query = date_query.replace('$o_date', str(o_date))
                csv_file_path = config['Spanner']['csv_file_path']
                performance_flag = config['Spanner']['performance_flag']
                uuid_column = config['Spanner']['uuid_column']
                bq_dataset = config['Bigquery']['bq_dataset']
                bq_dataset_tmp = config['Bigquery']['bq_dataset_tmp']
                bq_table = config['Bigquery']['bq_table']
                bq_table_temp = config['Bigquery']['bq_table_temp']
                bq_pk_column = config['Bigquery']['bq_pk_column']
                bq_location = config['Bigquery']['bq_location']
                bq_job_name = config['Bigquery']['job_name']
                bq_location = config['Bigquery']['bq_location']
                try:
                        spanner_to_bq_main(spanner_query, bq_location, date_query, csv_file_path, bq_dataset, bq_table, bq_dataset_tmp , bq_table_temp ,bq_pk_column, bq_temp_delete_query , bq_delete_query , bq_insert_from_temp_query,performance_flag,uuid_column)
                        command = "sh  /appl/hddlake/shc-enterprise-data-lake/scripts/source_audit_integration.sh " + o_date +" "+ bq_job_name +" "+ str(0)
                        process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        output, error = process.communicate()
                except Exception as e:
                        print(e)
                        command = "sh /appl/hddlake/shc-enterprise-data-lake/scripts/source_audit_integration.sh " + o_date +" "+ bq_job_name +" "+ str(1)
                        process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                        output, error = process.communicate()
                        raise Exception


def create_bq_spanner_connection(json_key_path, spanner_instance_name, spanner_database_name):
        """
                This function will create spanner database connection.
                Arguments
                ---------
                1.
                2.
        """
        key_path = str(json_key_path)
        credentials = service_account.Credentials.from_service_account_file(
                key_path,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

        #-----Initialization Part
        global SPANNER_DATABASE_CONN
        SPANNER_DATABASE_CONN = spanner.Client(credentials=credentials, project=credentials.project_id).\
                                        instance(str(spanner_instance_name)).database(str(spanner_database_name))
        global BQ_DATABASE_CONN
        BQ_DATABASE_CONN = bigquery.Client(credentials=credentials, project=credentials.project_id)

# [START spanner_create_database]

def create_database(spanner_table, create_table_query):

        """Creates a database and tables for sample data."""
        global SPANNER_DATABASE_CONN
        print("Dropping Table")
        with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                results = snapshot.execute_sql("SELECT t.table_name FROM information_schema.tables AS t WHERE t.table_catalog = \"\" AND t.table_schema = \"\" AND t.table_name = \"" + str(spanner_table) + "\"")
        # check_table = SPANNER_DATABASE_CONN.execute_sql()
        if len(list(results)) != 0:
                operation = SPANNER_DATABASE_CONN.update_ddl(["drop TABLE " + str(spanner_table)])
                operation.result()
                print("Table Dropped")
        print("Creating Table")
        operation = SPANNER_DATABASE_CONN.update_ddl([create_table_query])



        print('Waiting for operation to complete...')

        operation.result()
        print("Table Created")

        # [END spanner_create_database]



def bq_to_spanner_main(bq_query, bq_location, spanner_table, spanner_columns):
        """
                This function will trigger the data movement from bq to spanner
                Arguments
                ---------
                1.
                2.
        """
        #-----Fetching from BQ
        global BQ_DATABASE_CONN
        global SPANNER_DATABASE_CONN

        query = (bq_query)
        print("Job Started : ", datetime.datetime.now())
        #query_job = BQ_DATABASE_CONN.query(
        #    query,
        #    location=bq_location,
        #)
        proc = subprocess.Popen(["bq query --use_legacy_sql=false " + '"' + str(query) + '"'], stdout=subprocess.PIPE,
                            shell=True)
        (out, err) = proc.communicate()
        # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # In future if outuput of this command changes, below logic needs to be changed.
        out = out.decode('utf-8')
        # error = err.decode('utf-8')
        print(out)

        if out.find("Number of affected rows:") != -1 or out.find("Error") == -1:
            pass
        else:
            raise Exception
        print("Fetching from BQ Completed : ", datetime.datetime.now())
        spanner_column_list = [str(x).strip() for x in str(spanner_columns).split(",")]
        records=[]
        i=0
        c=1
        for r in query_job:
                #print(c,r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
                each_record = []
                prim_col=str(uuid.uuid4())
                each_record.append(prim_col)
        #each_record.append(c)
                #print(r)
                for each_value in r:

                        if isinstance(each_value, decimal.Decimal):
                #               print(each_value)
 #                         print(float(each_value))
                                each_record.append(float(each_value))
                        else:
                                each_record.append(each_value)
                records.append(each_record)
                c+=1
                i=i+1
                threshold_value = (20000 // (len(r) + 1))
                if i%threshold_value==0:
                        # print("Range is ....",i)
                        with SPANNER_DATABASE_CONN.batch() as batch:
                                batch.insert(table=spanner_table, columns=spanner_column_list, values=records)
                        records=[]
                        print("Completed for rows :" + str(c))
                        i=0
        if i!=0:
                print("loading remaining data....")
                with SPANNER_DATABASE_CONN.batch() as batch:
                        batch.insert(table=spanner_table, columns=spanner_column_list, values=records)
                records=[]
        print('Inserted data.')


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


def get_dates_from_spanner(date_query):
        global SPANNER_DATABASE_CONN
        print(date_query)
        dates_list = []
        with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                results = snapshot.execute_sql(date_query)
                for row in list(results):
                        dates_list.append("'" + row[0].strftime('%Y-%m-%d') + "'")
        if len(dates_list) == 0:
                print("Skipping Spanner to BQ load process as odate data is not present in Spanner")
                sys.exit()
        else:
                return ",".join(dates_list)


def delete_from_bq(bq_dataset, bq_location, bq_table, dates_string):
        bq_delete_query = "delete FROM `" + str(bq_dataset) + "." + str(bq_table) + "` where     cast(EDLCreatedTimestamp as Date) in (" + str(dates_string) + ")"
        print(bq_delete_query)
        #sys.exit()
        global BQ_DATABASE_CONN
        global SPANNER_DATABASE_CONN

        query = (bq_delete_query)
        print("Job for Data deletion from BQ integration table Completed  for today's odate Started : ", datetime.datetime.now())
        #query_job = BQ_DATABASE_CONN.query(
        #    query,
        #    location=bq_location,
        #)
        proc = subprocess.Popen(["bq query --use_legacy_sql=false " + '"' + str(query) + '"'], stdout=subprocess.PIPE,
                            shell=True)
        (out, err) = proc.communicate()
        # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # In future if outuput of this command changes, below logic needs to be changed.
        out = out.decode('utf-8')
        # error = err.decode('utf-8')
        print(out)

        if out.find("Number of affected rows:") != -1 or out.find("Error") == -1:
            pass
        else:
            raise Exception
        print("Data deletion from BQ integration table Completed  for today's odate: ", datetime.datetime.now())
        #sys.exit()


def spanner_to_csv(spanner_query, dates_string, csv_file_path,performance_flag,uuid_column):
        """
                This function will trigger the data movement from spanner to csv file in unix path
                Arguments
                ---------
                1. source_table
                2. target_table
        """
        global SPANNER_DATABASE_CONN
        spanner_query = spanner_query.replace('$dates', dates_string)
        if performance_flag == 'True':
                spanner_query = spanner_query.replace('$dates', dates_string)
                spanner_count_query = "select count(*) from (" + spanner_query + ")"
                print(spanner_count_query)
                with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                        results = snapshot.execute_sql(spanner_count_query)
                        row = list(results)[0]
                if row[0] > 600000:
                        #fast load
                        print("Loading data into csv file in splits as number of rows is : "  + str(row[0]))
                        print("uuid column:" + uuid_column)
                        uuid_list = ['4','1','9','8','0','f','e','7','b','2','d','3','c','a','5','6']
                        with open(csv_file_path,'w') as fd:
                                for each_uuid in uuid_list:
                                        spanner_query_each_uuid = spanner_query + " and substr(" + uuid_column  + ",1,1) = '" + each_uuid + "'"
                                        print(spanner_query_each_uuid)
                                        with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                                                results = snapshot.execute_sql(spanner_query_each_uuid)
                                                for row in list(results):
                                                        file_string = ""
                                                        for x in range(0,len(row)):
                                                                if x == len(row)-1:
                                                                        if row[x] == None:
                                                                                file_string = file_string + ""
                                                                        elif row[x] == "":
                                                                                file_string = file_string + " "  + "|"
                                                                        else:
                                                                                file_string = file_string + str(row[x])
                                                                else:
                                                                        if row[x] == None:
                                                                                file_string = file_string + "" + "|"
                                                                        elif row[x] == "":
                                                                                file_string = file_string + " "  + "|"
                                                                        else:
                                                                                file_string = file_string + str(row[x]) + "|"
                                                        file_string += "\n"
                                                        # file_string = "|".join([str(x) for x in row]) + "\n"
                                                        # file_string = file_string.replace("None","")
                                                        # print(file_string)
                                                        fd.write(file_string)
                else:
                        with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                                results = snapshot.execute_sql(spanner_query)
                                with open(csv_file_path,'w') as fd:
                                        file_string = ""
                                        for row in list(results):
                                                file_string = ""
                                                for x in range(0,len(row)):
                                                        if x == len(row)-1:
                                                                if row[x] == None:
                                                                        file_string = file_string + ""
                                                                elif row[x] == "":
                                                                        file_string = file_string + " "
                                                                else:
                                                                        file_string = file_string + str(row[x])
                                                        else:
                                                                if row[x] == None:
                                                                        file_string = file_string + "" + "|"
                                                                elif row[x] == "":
                                                                        file_string = file_string + " "  + "|"
                                                                else:
                                                                        file_string = file_string + str(row[x]) + "|"
                                                file_string += "\n"

                                                # file_string = "|".join([str(x) for x in row]) + "\n"
                                                # file_string = file_string.replace("None","")
                                                # print(file_string)
                                                fd.write(file_string)
        else:
                with SPANNER_DATABASE_CONN.snapshot() as snapshot:
                        results = snapshot.execute_sql(spanner_query)
                        with open(csv_file_path,'w') as fd:
                                file_string = ""
                                for row in list(results):
                                        file_string = ""
                                        for x in range(0,len(row)):
                                                if x == len(row)-1:
                                                        if row[x] == None:
                                                                file_string = file_string + ""
                                                        elif row[x] == "":
                                                                file_string = file_string + " "  + "|"
                                                        else:
                                                                file_string = file_string + str(row[x])
                                                else:
                                                        if row[x] == None:
                                                                file_string = file_string + "" + "|"
                                                        elif row[x] == "":
                                                                file_string = file_string + " "  + "|"
                                                        else:
                                                                file_string = file_string + str(row[x]) + "|"
                                        file_string += "\n"

                                        # file_string = "|".join([str(x) for x in row]) + "\n"
                                        # file_string = file_string.replace("None","")
                                        # print(file_string)
                                        fd.write(file_string)
                # sys.exit()
        # snapshot = SPANNER_DATABASE_CONN.batch_snapshot()
        # partitions = snapshot.generate_read_batches(
        #        table=spanner_table,
        #        columns=spanner_column_list,
        #        keyset=spanner.KeySet(all_=True)
        # )

        # start = time.time()

        # def process(snapshot, partition):
        #        print('Started processing partition.')
        #        row_ct = 0
        #        for row in snapshot.process_read_batch(partition):
        #                with open(csv_file_path,'a') as fd:
        #                        write_string_csv = "|".join([str(x) for x in row]) + "\n"
        #                        fd.write(write_string_csv)
        #        #              print(u'Id: {}, Value: {}'.format(*row))
        #                        row_ct += 1
        #        return time.time(), row_ct


        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #        futures = [executor.submit(process, snapshot, p) for p in partitions]

        #        for future in concurrent.futures.as_completed(futures, timeout=3600):
        #                finish, row_ct = future.result()
        #                elapsed = finish - start
        #                print(u'Completed {} rows in {} seconds'.format(row_ct, elapsed))

        # snapshot.close()


def delete_temp_bq(bq_location, bq_temp_delete_query):
        global BQ_DATABASE_CONN
        query = (bq_temp_delete_query)
        print(query)
        print("Job for deletion of BQ IntegrationTemp table Started : ", datetime.datetime.now())
        #query_job = BQ_DATABASE_CONN.query(
        #    query,
        #    location=bq_location,
        #)
        proc = subprocess.Popen(["bq query --use_legacy_sql=false " + '"' + str(query) + '"'], stdout=subprocess.PIPE,
                            shell=True)
        (out, err) = proc.communicate()
        # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # In future if outuput of this command changes, below logic needs to be changed.
        out = out.decode('utf-8')
        # error = err.decode('utf-8')
        print(out)

        if out.find("Number of affected rows:") != -1 or out.find("Error") == -1:
            pass
        else:
            raise Exception
        print("Deletion from BQ IntegrationTemp table Completed : ", datetime.datetime.now())


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



def delete_exist_bq(bq_location, bq_delete_query):
        global BQ_DATABASE_CONN
        query = (bq_delete_query)
        print(query)
        print("Job for deletion of BQ Integration table from temp table Started : ", datetime.datetime.now())
        #query_job = BQ_DATABASE_CONN.query(
        #    query,
        #    location=bq_location,
        #)
        proc = subprocess.Popen(["bq query --use_legacy_sql=false " + '"' + str(query) + '"'], stdout=subprocess.PIPE,
                            shell=True)
        (out, err) = proc.communicate()
        # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # In future if outuput of this command changes, below logic needs to be changed.
        out = out.decode('utf-8')
        # error = err.decode('utf-8')
        print(out)

        if out.find("Number of affected rows:") != -1 or out.find("Error") == -1:
            pass
        else:
            raise Exception
        print("Data deletion from BQ Integration table Completed : ", datetime.datetime.now())
        time.sleep(180)
        #sys.exit()



def insert_bq_tmp_to_bq_integration(bq_location,bq_insert_from_temp_query):
        global BQ_DATABASE_CONN
        query = (bq_insert_from_temp_query)
        print(query)
        print("Job for Insertion from BQ IntegrationTemp to Integration table Started : ", datetime.datetime.now())
        #query_job = BQ_DATABASE_CONN.query(
        #    query,
        #    location=bq_location,
        #)
        proc = subprocess.Popen(["bq query --use_legacy_sql=false " + '"' + str(query) + '"'], stdout=subprocess.PIPE,
                            shell=True)
        (out, err) = proc.communicate()
        # This is to handle bq show --schema output and convert to a list having each element as dictionary type
        # In future if outuput of this command changes, below logic needs to be changed.
        out = out.decode('utf-8')
        # error = err.decode('utf-8')
        print(out)

        if out.find("Number of affected rows:") != -1 or out.find("Error") == -1:
            pass
        else:
            raise Exception
        print("Insertion from BQ IntegrationTemp to Integration Completed : ", datetime.datetime.now())
        #sys.exit()



#---date YYYYMMDD to standard formart
def YYYYMMDD_SD(date_str):

                tmp=datetime.datetime.strptime(date_str, '%Y%m%d').date()
                sFormat=str(tmp.strftime('%Y-%m-%d'))
                return sFormat


if __name__ == '__main__':
        main()


