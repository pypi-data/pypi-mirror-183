## packages standard :
import time
import json
import random
from enum import Enum

## packages add-ons :
import damv1env as env
import damv1time7 as time7
import damv1manipulation as mpl

## Reference use "pyairtable" ***
## https://pyairtable.readthedocs.io/en/latest/getting-started.html
from pyairtable import Api, Base, Table
from pyairtable.formulas import match, FIND, FIELD, EQUAL, STR_VALUE, OR, AND, escape_quotes

## Rererence use "airtable python wrapper" ***
## https://airtable-python-wrapper.readthedocs.io/_/downloads/en/latest/pdf/
import airtable as airtable


class const_type(Enum):
    log = 'Log-pod'
    restart = 'Restart-pod'

class const_sincelast(Enum):
    h1 = '1h'
    h12 = '12h'
    h24 = '24h'
    
class const_process(Enum):
    end = 0
    start = 1

class const_status(Enum):
    ToDo = 'To do'
    InProgress = 'In progress'
    Done = 'Done'


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
                time.sleep(1)
        print(time7.currentTime7(),'      ', '.'*83)
        print(time7.currentTime7(),'      All Done ( 仕上がり )')
        print(time7.currentTime7(),'\n'*2)


    def convert_airtableDict_to_dictionary(self,airtable):
        lst_data = []
        try:
            if airtable:
                for page in airtable:
                    dict_row = {}
                    dict_row['id'] = page['id']
                    for key in page.keys():
                        if 'dict' in str(type(page[key])):
                            for record in page[key]:
                                dict_row[record] = page[key][record]
                    lst_data.append(dict_row)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_data

    def view_dictionary(self,lst_dict):
        try:
            if lst_dict:
                print('-'*35)
                for row in lst_dict:
                    for record in row:
                        print(record,':',row[record])
                    print('-'*35)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)

    # into utils Class
    def escape_dict(self,_page, _key, _esc=''):
        oput = None
        try: oput = str(_page[_key]).strip()
        except: oput = _esc
        return oput



class sandbox():

    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    ## USED PYAIRTABLE
    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

    def pyairtable_delete_all_rows(self):
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

    def pyairtable_create_batchrow(self):
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
    def pyairtable_loadAll_by_OR_condition(self, _pattern):
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
    # out = f.pyairtable__loadAll_by_rawformula(raw_example)
    # print(out)
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def pyairtable__loadAll_by_rawformula(self, _raw):
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

### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### SCHEMA TABLE PROJECTS    
# 'name'                          # single line text
# 'title'                         # single line text
# 'type'                          # single select | Log-pod, Restart-pod
# 'ns'                            # single line text | description: namespace
# 'target contains'               # long text | values: [dictionary]
# 'patterns'                      # long text | values: [dictionary]
# 'Enable'                        # checkbox
# 'status'                        # single select | To do, In Progress, Done
# 'cip'                           # number (integer:2) | description: Counter in Progress
# 'start date'                    # date
# 'end date'                      # date
# 'detected'                      # single line text | values: [dictionary]
# 'report'                        # single line text | values: [dictionary]
# 'exec method'                   # single select | One-to-one, One-to-many
# 'last of log 1'                 # single line text | description the current time live last of log
# 'last of log 2'                 # single line text | description the current time live last of log
# 'last of log 3'                 # single line text | description the current time live last of log
### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    ## USED PYAIRTABLE
    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    def pyairtable_loadAll_by_enable_ColParams(self, _enable=True):
        data = []
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            query = match({"enable": _enable})
            airtable = table.all(formula=query,fields=['name', 'title', 'type', 'ns', 'target contains', 'patterns', 'Enable', 'exec method'])
            if airtable: data = airtable
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return data

    def pyairtable_getFirstLstDict_by_name_and_enable(self, _table, _name, _Enable, _fields):
        lst_data = []
        try:
            query = match({'name': _name, "Enable": bool(_Enable)})
            airtable = _table.first(formula=query,fields=_fields)
            dict_airtable = []; dict_airtable.append(airtable)
            lst_data = utils().convert_airtableDict_to_dictionary(dict_airtable)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_data

    def pyairtable_update_StartEnd_process(self, _id, _name, _Enable, _stepProcess):
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            lst_data = f.pyairtable_getFirstLstDict_by_name_and_enable(table, _name,_Enable,['name','type','cip'])
            if len(lst_data)!=0:
                id = str(utils().escape_dict(lst_data[0],'id')).strip()
                cipInt = int(utils().escape_dict(lst_data[0],'cip','0'))
                field_date = None
                if id == str(_id).strip():
                    match _stepProcess:
                        case const_process.start.value: 
                            cipInt = cipInt + 1
                            field_date = 'start date'
                        case const_process.end.value: 
                            if cipInt>0: cipInt = cipInt - 1
                            field_date = 'end date'
                    if cipInt == 0:
                        table.update(id,{'status':const_status.Done.value, field_date:time7.currentTime7(), 'cip':cipInt})
                    else:
                        table.update(id,{'status':const_status.InProgress.value, field_date:time7.currentTime7(), 'cip': cipInt})
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)

    def pyairtable_append_detected_and_report_process(self, _id, _name, _Enable, _sumDetected, _urlShareable):
        try:
            table = Table(env.sandbox_airtable.api_key.value, env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value)
            lst_data = f.pyairtable_getFirstLstDict_by_name_and_enable(table, _name,_Enable,['name','detected','report'])
            if len(lst_data)!=0:
                id = str(utils().escape_dict(lst_data[0],'id')).strip()
                lst_detected = []; lst_detected = json.loads(utils().escape_dict(lst_data[0],'detected','[]'))
                if len(lst_detected)>=3:lst_detected.clear()
                lst_detected.append(_sumDetected)
                lst_report = []; lst_report = json.loads(utils().escape_dict(lst_data[0],'report','[]'))
                if len(lst_report)>=3:lst_report.clear()
                lst_report.append(_urlShareable)
                if id == str(_id).strip():
                    table.update(id,{'detected':escape_quotes(json.dumps(lst_detected)), 'report':escape_quotes(json.dumps(lst_report))})
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)

### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    ## USED AIRTABLE PYTHON WRAPPER
    ## * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    def airtablepywrapper_loadAll_data(self):
        lst_output = []
        try:
            rTable = airtable.Airtable(env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value,env.sandbox_airtable.api_key.value)
            lst_output = rTable.get_all()
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output
    
    def airtablepywrapper_parameter_filters(self):
        try:
            rTable = airtable.Airtable(env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value,env.sandbox_airtable.api_key.value)
            for page in rTable.get_iter(view='GridView_All',sort='ns'):
                for record in page:
                    value = record['fields']['name']
                    print(value)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
    
    def airtablepywrapper_loadAll_by_View(self):
        lst_output = []
        try:
            rTable = airtable.Airtable(env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value,env.sandbox_airtable.api_key.value)
            lst_output = rTable.get_all(view='GridView_Process', sort='name')
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output

    def airtablepywrapper_search(self):
        lst_output = []
        try:
            rTable = airtable.Airtable(env.sandbox_airtable.base_id.value, env.sandbox_airtable.table_name.value,env.sandbox_airtable.api_key.value)
            lst_output = rTable.search('name','WF-3')
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_output


class testing():
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    ## uncomments this bellow for testing only ( テスティング ) !
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    def excute():
        f = sandbox()
        u = utils()
        ## used PYAIRTABLE
        ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # f.pyairtable_delete_all_rows()
        # f.pyairtable_create_batchrow()
        ## skenario 1
        print(time7.currentTime7(),'(1) - Airtable Load All by Enable ( ローディング )')
        data=f.pyairtable_loadAll_by_enable_ColParams(True)
        lst_data = u.convert_airtableDict_to_dictionary(data)
        u.view_dictionary(lst_data)
        # print(json.dumps(lst_data))
        if len(lst_data)!=0:
            print(time7.currentTime7(),'      [ Data is available ] 入手可能')
            for idx, r in  enumerate(lst_data):
                r_id = u.escape_dict(r,'id')
                r_name = u.escape_dict(r,'name')
                r_title = u.escape_dict(r,'title')
                r_type = u.escape_dict(r,'type')
                r_ns = u.escape_dict(r,'ns')
                r_targets = u.escape_dict(r,'target contains')
                r_patterns = u.escape_dict(r,'patterns')
                r_Enable = u.escape_dict(r,'Enable')
                r_excmethod = u.escape_dict(r,'exec method')
                number = idx + 1
                lst_patterns = json.loads(r_patterns)
                lst_targets = json.loads(r_targets)
                sumDetected = str(random.randint(1, 50))
                urlShareable = "https://sandbox.evernote.com/shard/s1/sh/dd93c15c-33dc-4c56-9836-f36a0cb95631/8ea7d65a0f5835dfcf7c62f3ce5dee60"
                if const_type.log.value in r_type:
                    f.pyairtable_update_StartEnd_process(r_id, r_name, r_Enable, const_process.start.value)
                    u.simulation(number, r_title, r_ns, const_sincelast.h24.value, lst_patterns, lst_targets)
                    f.pyairtable_append_detected_and_report_process(r_id, r_name, r_Enable, sumDetected,urlShareable)
                    f.pyairtable_update_StartEnd_process(r_id, r_name, r_Enable, const_process.end.value)
        else:
            print(time7.currentTime7(),'      [ Data is unavailable ] 入手不可能')

        ## used AIRTABLE-PYTHON-WRAPPER
        ## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        ## skenario 1
        # datas = f.airtablepywrapper_loadAll_data()
        # print(datas)
        ## skenario 2
        # f.airtablepywrapper_parameter_filters()
        ## skenario 3
        # datas = f.airtablepywrapper_loadAll_by_View()
        # print(datas)
        ## skenario 4
        # datas = f.airtablepywrapper_search()
        # print(datas)

# test = testing()
# test.excute()