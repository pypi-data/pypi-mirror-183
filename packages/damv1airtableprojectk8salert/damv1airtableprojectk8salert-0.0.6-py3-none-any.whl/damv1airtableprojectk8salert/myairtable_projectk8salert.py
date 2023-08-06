import damv1env as env
import damv1time7 as time7
import damv1manipulation as mpl
from pyairtable import Api, Base, Table
from pyairtable.formulas import match

import time


class utils():
    def simulation(self,_nameof_msg_rpt, _namespace, _sincelast, _lst_patterns, _lst_target=[]):
        print(time7.currentTime7(),'    [ Begin simulation ]')
        print(time7.currentTime7(),'      Arguments :')
        print(time7.currentTime7(),'         - name of message :', _nameof_msg_rpt)
        print(time7.currentTime7(),'         - namespace :', _namespace)
        print(time7.currentTime7(),'         - sincelast :', _sincelast)
        print(time7.currentTime7(),'         - patterns :', _lst_patterns)
        print(time7.currentTime7(),'         - targets :', _lst_target)
        print(time7.currentTime7(),'      ', '.'*83)

        if len(_lst_target)!=0:
            for x in _lst_target:
                print(time7.currentTime7(),'       In Progress step (',x,')')
                time.sleep(3)
        print(time7.currentTime7(),'      ', '.'*83)
        print(time7.currentTime7(),'      All Done')
        print(time7.currentTime7(),'\n'*2)

    def airtable_escape_fields(self, _data, _colname, _strNull=None):
        try:output = _data["fields"][_colname]
        except:output = _strNull
        return output        

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


    def airtable_loadAll_by_enable(self, _enable=True):
        print(time7.currentTime7(),'(1) - Airtable Load All by Enable ( ローディング )')
        lst_output = []
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            query = match({"enable": True})
            r = table.all(formula=query)
            if r:
                print(time7.currentTime7(),'     [ Data is available ] 入手可能')
                lst_output=r
            else:
                print(time7.currentTime7(),'     [ Data is unavailable ] 入手不可能')
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output

    def airtable_normalize_datafrom_loadAll_origin(self, _lst_data):
        normalize_dict_row = {}
        try:
            for data in _lst_data:
                fdName = u.airtable_escape_fields(data,'name','')
                fdTitle = u.airtable_escape_fields(data,'title','')
                fdType = u.airtable_escape_fields(data,'type','')
                fdNs = u.airtable_escape_fields(data,'ns','')
                fdTargets = u.airtable_escape_fields(data,'target contains','')     # dictionary values
                fdPatterns = u.airtable_escape_fields(data,'patterns','')           # dictionary values
                fdEnable = u.airtable_escape_fields(data,'Enable','')
                fdStatus = u.airtable_escape_fields(data,'status','')
                fdStartDt = u.airtable_escape_fields(data,'start date','')
                fdEndDt = u.airtable_escape_fields(data,'end date','')
                fdDetected = u.airtable_escape_fields(data,'detected','')           # dictionary values
                fdReport = u.airtable_escape_fields(data,'report','')               # dictionary values
                fdMethod = u.airtable_escape_fields(data,'exec method','')
                fdCip = u.airtable_escape_fields(data,'cip','')
                fdLogLive1 = u.airtable_escape_fields(data,'log live 1','')
                fdLogLive2 = u.airtable_escape_fields(data,'log live 2','')
                fdLogLive3 = u.airtable_escape_fields(data,'log live 3','')

                normalize_dict_row = {  'name':fdName, 'title':fdTitle, 'type':fdType, 'ns':fdNs, 'target contains':fdTargets, \
                                        'patterns':fdPatterns, 'Enable':fdEnable, 'status':fdStatus, 'start date':fdStartDt, \
                                        'end date':fdEndDt, 'detected':fdDetected, 'report':fdReport, 'exec method':fdMethod, \
                                        'cip':fdCip, 'log live 1':fdLogLive1, 'log live 2':fdLogLive2, 'log live 3':fdLogLive3                 
                                    }
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return normalize_dict_row

# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ## uncomments this bellow for testing only ( テスティング ) !
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# f = sandbox()
# u = utils()
# def excute():
#     # f.airtable_delete_all_rows()
#     # f.airtable_create_batchrow()
#     datas=f.airtable_loadAll_by_enable(True)
#     transdata = f.airtable_normalize_datafrom_loadAll_origin(datas)
#     print(time7.currentTime7(),transdata)


#     # # SIMULATION
#     # lst_patterns=[]
#     # lst_patterns.append('502 Bad Gateway')
#     # lst_patterns.append('Error while validating pooled Jedis object')
#     # lst_patterns.append('Error 7 ---')
#     # target_podstr = []
#     # target_podstr = ['dashboardsvc', 'distributorshippromotionquery','inventory','pricecmd', 'shopeeintegrationcmd','userquery','warehousequery']

#     # u.simulation('Test title', 'test','24h',lst_patterns,target_podstr)
# excute()