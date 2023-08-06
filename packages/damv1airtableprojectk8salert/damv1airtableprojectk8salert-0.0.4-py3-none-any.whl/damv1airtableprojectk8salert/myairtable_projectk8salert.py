import damv1env as env
import damv1time7 as time7
import damv1manipulation as mpl
from pyairtable import Api, Base, Table
from pyairtable.formulas import match

class sandbox():
    def airtable_delete_all_rows(self):
        print(time7.currentTime7(),'      Deleting all rows data ( すべて消す ):')
        boolexecute = False
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            data = table.all()
            if data:
                for row in data:
                    print(time7.currentTime7(),'        Deleted id (', row['id'],')')
                    table.delete(row['id'])
            else:
                print(time7.currentTime7(),'      Data is empty, abort delete')
            boolexecute = True
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    
        return boolexecute


    def airtable_create_batchrow(self):
        boolexecute = False
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            table.batch_create(\
                    [
                        {'name':'WF-1', 'title':'[ALERT] Logs service', 'ns':'sit', 'target contains':"{'distributorship','dashboard', 'business'}",'patterns':"{'Error 7 ---','Error 8 ---','Error 9 ---'}", 'Enable': True, 'status':'To do'},
                        {'name':'WF-2', 'title':'[ALERT] Logs service', 'ns':'uat', 'target contains':"{'distributorship','dashboard', 'business'}",'patterns':"{'Error 7 ---','Error 8 ---','Error 9 ---'}", 'Enable': True, 'status':'To do'},
                        {'name':'WF-3', 'title':'[ALERT] Restarts tracked', 'ns':'sit', 'target contains':"{''}",'patterns':"{'Restart'}", 'status':'To do'},
                        {'name':'WF-4', 'title':'[ALERT] Restarts tracked', 'ns':'uat', 'target contains':"{''}",'patterns':"{'Restart'}", 'status':'To do'},
                    ]
                )
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    
        return boolexecute





# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ## uncomments this bellow for testing only ( テスティング ) !
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# f = sandbox()
# def excute():
#     f.airtable_delete_all_rows()
#     f.airtable_create_batchrow()

# excute()