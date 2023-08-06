import damv1env as env
import damv1time7 as time7
import damv1manipulation as mpl
from pyairtable import Api, Base, Table
from pyairtable.formulas import match, FIND, FIELD, EQUAL, STR_VALUE, OR, AND, escape_quotes

import time
import json


class utils():
    def simulation(self,_number,_nameof_msg_rpt, _namespace, _sincelast, _lst_patterns, _lst_target=[]):
        print(time7.currentTime7(),'      [ Begin simulation - {0} ] シミュレーション'.format(_number))
        print(time7.currentTime7(),'        Arguments (パラメタ値):')
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
        print(time7.currentTime7(),'      All Done ( 仕上がり )')
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
                        {'name':'WF-1', 'title': escape_quotes('[ALERT] Logs service'), 'type':'Log-pod', 'ns':'sit', 'target contains':escape_quotes('["dashboardsvc", "distributorshippromotionquery", "inventory", "pricecmd", "shopeeintegrationcmd", "userquery", "warehousequery"]'),'patterns':escape_quotes('["Error 7 ---","Error 8 ---","Error 9 ---"]'), 'Enable': True, 'status':'To do','detected':'[]','report':escape_quotes('[]')},
                        {'name':'WF-2', 'title': escape_quotes('[ALERT] Logs service'), 'type':'Log-pod','ns':'uat', 'target contains':escape_quotes('["dashboardsvc", "distributorshippromotionquery", "inventory", "pricecmd", "shopeeintegrationcmd", "userquery", "warehousequery"]'),'patterns':escape_quotes('["Error 7 ---","Error 8 ---","Error 9 ---"]'), 'Enable': True, 'status':'To do','detected':'[]','report':escape_quotes('[]')},
                        {'name':'WF-3', 'title': escape_quotes('[ALERT] Restarts tracked'), 'type':'Restart-pod','ns':'sit', 'target contains':'[]','patterns':'["Restart"]', 'status':'To do','detected':'[]','report':'[]'},
                        {'name':'WF-4', 'title': escape_quotes('[ALERT] Restarts tracked'), 'type':'Restart-pod','ns':'uat', 'target contains':'[]','patterns':'["Restart"]', 'status':'To do','detected':'[]','report':'[]'},
                    ]
                )
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)    
        return boolexecute

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Example : [ get data by formula match with condition OR ]
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # out = f.airtable_loadAll_by_OR_condition({'status': 'Done','Enable': True})
    # print(out)
    def airtable_loadAll_by_OR_condition(self, _pattern):
        # Notes : If match_any=True, expressions are grouped with OR()
        lst_output =[]
        try:
            if len(_pattern)!=0:
                table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
                query = match(_pattern,match_any=True)
                r = table.all(formula=query)
                if r: lst_output = r
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Example : [ get data by raw formula ]
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # raw_example = None
    # # skenario 1
    # raw_example = "FIND('Done', {Status})"
    # # skenario 2
    # raw_example =  "AND(NOT(OR({status}='Done', {Status}='To do')),{ns}='sit')"
    # # skenario 3
    # raw_status_todo = EQUAL(STR_VALUE('To do'),FIELD('status'))
    # raw_status_done = EQUAL(STR_VALUE('Done'),FIELD('status'))
    # raw_example = OR(raw_status_todo,raw_status_done)
    # # skenario 4
    # raw_example = EQUAL(STR_VALUE('To do'),FIELD('status'))
    # # skenario 5
    # raw_example = FIND(STR_VALUE('inventory'),FIELD('target contains'))
    # out = f.airtable__loadAll_by_rawformula(raw_example)
    # print(out)
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def airtable__loadAll_by_rawformula(self, _raw):
        # Reference https://pyairtable.readthedocs.io/en/latest/api.html
        lst_output = []
        try:
            if _raw.strip()!= '':
                table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
                r = table.all(formula=_raw)
                if r: lst_output = r 
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output

    def airtable_loadAll_by_enable(self, _enable=True):
        print(time7.currentTime7(),'(1) - Airtable Load All by Enable ( ローディング )')
        lst_output = []
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            query = match({"enable": True})
            r = table.all(formula=query)
            if r:
                print(time7.currentTime7(),'      [ Data is available ] 入手可能')
                lst_output=r
            else:
                print(time7.currentTime7(),'      [ Data is unavailable ] 入手不可能')
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output

    def airtable_normalize_datafrom_loadAll_origin(self, _lst_data):
        dict_rows = []
        try:
            for data in _lst_data:
                normalize_dict_row = {}
                row_id = data['id']
                fdName = utils().airtable_escape_fields(data,'name','')                         # single line text
                fdTitle = utils().airtable_escape_fields(data,'title','')                       # single line text
                fdType = utils().airtable_escape_fields(data,'type','')                         # single select | Log-pod, Restart-pod
                fdNs = utils().airtable_escape_fields(data,'ns','')                             # single line text | description: namespace
                fdTargets = utils().airtable_escape_fields(data,'target contains','')           # long text | values: [dictionary]
                fdPatterns = utils().airtable_escape_fields(data,'patterns','')                 # long text | values: [dictionary]
                fdEnable = utils().airtable_escape_fields(data,'Enable','')                     # checkbox
                fdStatus = utils().airtable_escape_fields(data,'status','')                     # single select | To do, In Progress, Done
                fdCip = utils().airtable_escape_fields(data,'cip','')                           # number (integer:2) | description: Counter in Progress
                fdStartDt = utils().airtable_escape_fields(data,'start date','')                # date
                fdEndDt = utils().airtable_escape_fields(data,'end date','')                    # date
                fdDetected = utils().airtable_escape_fields(data,'detected','')                 # single line text | values: [dictionary]
                fdReport = utils().airtable_escape_fields(data,'report','')                     # single line text | values: [dictionary]
                fdMethod = utils().airtable_escape_fields(data,'exec method','')                # single select | One-to-one, One-to-many
                fdTimeLiveLastLog1 = utils().airtable_escape_fields(data,'last of log 1','')    # single line text | description the current time live last of log
                fdTimeLiveLastLog2 = utils().airtable_escape_fields(data,'last of log 2','')    # single line text | description the current time live last of log
                fdTimeLiveLastLog3 = utils().airtable_escape_fields(data,'last of log 3','')    # single line text | description the current time live last of log

                normalize_dict_row = {  'id': row_id, \
                                        'name':fdName, 'title':fdTitle, 'type':fdType, 'ns':fdNs, 'target contains':fdTargets, \
                                        'patterns':fdPatterns, 'Enable':fdEnable, 'status':fdStatus, 'cip':fdCip, \
                                        'start date':fdStartDt, 'end date':fdEndDt, 'detected':fdDetected, 'report':fdReport, 'exec method':fdMethod, \
                                        'log live 1':fdTimeLiveLastLog1, 'log live 2':fdTimeLiveLastLog2, 'log live 3':fdTimeLiveLastLog3                
                                    }
                dict_rows.append(normalize_dict_row)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return dict_rows

    def airtable_update_startprocess(self, _id, _name, _Enable):
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            formula = match({"name": _name, "Enable": _Enable})
            r = table.first(formula=formula)
            if r['id']==_id.strip():
                cip = int(utils().airtable_escape_fields(r,'cip','0'))
                cip = int(cip) + 1
                table.update(r['id'],{'status':'In progress','start date':time7.currentTime7(), 'cip':cip})
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)

    def airtable_update_endprocess(self, _id, _name, _Enable):
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            formula = match({"name": _name, "Enable": _Enable})
            r = table.first(formula=formula)
            if r['id']==_id.strip():
                cip = int(utils().airtable_escape_fields(r,'cip','0'))
                cip = int(cip) - 1
                if cip == 0:
                    table.update(r['id'],{'status':'Done','end date':time7.currentTime7(),'cip':cip})
                else:
                    table.update(r['id'],{'end date':time7.currentTime7(),'cip':cip})
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## uncomments this bellow for testing only ( テスティング ) !
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
f = sandbox()
u = utils()
def excute():
    transdata = []
    f.airtable_delete_all_rows()
    f.airtable_create_batchrow()
    datas=f.airtable_loadAll_by_enable(True)
    transdata = f.airtable_normalize_datafrom_loadAll_origin(datas)


    if len(transdata)!=0:
        number = 0
        print(time7.currentTime7(),'(2) - Execution ( エグゼキュート )')
        for row in transdata:
            number += 1
            # SIMULATION
            id = row['id']
            name = row['name']
            typeprocess = row['type']
            rowEnable = row['Enable']

            title = row['title']
            namespace = row['ns']
            sincelast = '24h'
            lst_patterns = json.loads(row['patterns'])
            target_podstr = json.loads(row['target contains'])
            if typeprocess.strip() == 'Log-pod':
                # check Exec method
                f.airtable_update_startprocess(id, name, rowEnable)
                utils().simulation(number, title, namespace,sincelast,lst_patterns,target_podstr)
                f.airtable_update_endprocess(id,name,rowEnable)

excute()