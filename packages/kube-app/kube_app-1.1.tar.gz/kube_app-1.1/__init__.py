"""
General functions for kube.
"""
import requests
import pandas as pd

__all__ = ['pushData', 'getSchema','getData']

def initializeApp(client_config):
    """
    client_config = 
    {
        "api_key":"<alpha_numeric string from kube portal>",
        "secret_key":"<alpha_numeric string from kube portal>"
    }
    """
    if client_config=='abc':
        return True
    else:
        return False

# (Kube Connectivity functions) 
# Functions to connect with source databases using only connection strings.
def pgsql_data(conn_str,schema_name,table_name):
    return True

def mssql_data(conn_str,schema_name,table_name):
    return True

def mongo_data(conn_str,collection_name):
    return True

def excel_data(file_path,sheet_name):
    if file_path==None:
        return False
    if sheet_name==None:
        return False
    df = pd.read_excel(file_path,sheet_name=sheet_name)
    if df==None | len(df)==0:
        return False
    return df

def csv_data(file_path):
    if file_path==None:
        return False
    df = pd.read_csv(file_path)
    if df==None | len(df)==0:
        return False
    return df
# End Here

def pushData(client,source_data,table,overwrite=True):
    """
    compulsory arguments ->
    source_data is pandas dataframe returned from (Kube connectivity functions), 
    table = <sales,sales_order,ar,hierarchy,customer,product,target>
    ------------------------------------------------------------------
    overwrite -> optional argument -> True/False
    """
    error_message = ''
    if client==True:
        if source_data==None:
            error_message = 'source_data as compulsory argument is not provided'
            return error_message
        if table==None:
            error_message = 'table name as a compulsory argument is not provided'
            return error_message
        else:
            return True
    else:
        return False

def getSchema():
    """
    compulsory argument ->
    ------------------------------------------------------------------

    optional argument ->
    table = <sales,sales_order,ar,hierarchy,customer,product,target>
    ------------------------------------------------------------------
    """
    return True

def getData():
    """
    """
    return True