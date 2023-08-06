# import kube as k
# client = k.initializeApp('abc')
# print(k.pushData(client,None,None))
def getData(conn_str,table_name='sales'):
    return conn_str+table_name

print(getData('mongo --->',table_name='ar'))