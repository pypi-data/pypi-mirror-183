import damv1env as env
import damv1time7 as time7
import damv1manipulation as mpl
from pyairtable import Api, Base, Table
from pyairtable.formulas import match

class sandbox():
    def airtable_delete_all_rows(self):
        boolexecute = False
        try:
            table = Table(env.sandbox_airtable.api_key, env.sandbox_airtable.base_id, env.sandbox_airtable.table_name)
            data = table.all()
            for row in data:
                table.delete(row['id'])
            boolexecute = True
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    
        return boolexecute


    def airtable_create_batchrow(self):
        boolexecute = False
        try:
            table = Table(env.sandbox_airtable.api_key, env.sandbox_airtable.base_id, env.sandbox_airtable.table_name)
            table.batch_create(\
                    [
                        {'name':'WF-1', 'title':'[ALERT] Logs service', 'namespace':'sit', 'targets contain':"{'distributorship','dashboard', 'business'}",'patterns':"{'Error 7 ---','Error 8 ---','Error 9 ---'}", 'status':'To do'},
                        {'name':'WF-2', 'title':'[ALERT] Logs service', 'namespace':'uat', 'targets contain':"{'distributorship','dashboard', 'business'}",'patterns':"{'Error 7 ---','Error 8 ---','Error 9 ---'}", 'status':'To do'},
                        {'name':'WF-3', 'title':'[ALERT] Restarts tracked', 'namespace':'sit', 'targets contain':"{''}",'patterns':"{'Restart'}", 'status':'To do'},
                        {'name':'WF-4', 'title':'[ALERT] Restarts tracked', 'namespace':'uat', 'targets contain':"{''}",'patterns':"{'Restart'}", 'status':'To do'}
                    ]
                )
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    
        return boolexecute

