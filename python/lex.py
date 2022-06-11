import json
import pandas as pd
import sys
import csv
from sqlalchemy import create_engine

##### TODO
#MAKE FUNCTION
# CONNECT DATABASE
# IF ELSE DICT -- RECURSIVE
# filter none dicts from func
# connect mysql
# make function applicable to dataframe column
# WRAP UP


##GETS KEY IF EXISTS
def getNewkey(k):
    if (your_dict.get(k)):
        return (your_dict.get(k))
    else:
        return k


def renameKeys(key):

    ##declare empty filter
    filter = {}
    ## loop through keys in filter then append to dict, its duplicating on purpose to remove [] brackets
    new_dict={}
    dict_list = []
    for k,v in key.items():

        new_key = getNewkey(k)
        value = v
        new_dict[new_key] = v
        dict_list.append(new_dict)
    #filter[key] = dict_list[0]
    #print(dict_list[0])
    try:
        return dict_list[0]
    except Exception as e:
        return {}

##final function takes json column and returns new json with converted names
def convertJSON(filter_col):

    #convert string to json
    data = json.loads(filter_col)

    replacement = {}
    for key in data.keys():
        if (key == 'columnState'):
            replacement[key] = data[key]
        elif isinstance(data[key],dict):
            replacement[key] = renameKeys(data[key])
            #print('dict')
        elif isinstance(data[key],list):
            #print(data[key])
            if (len(data[key])>0):
                x=data[key]
                sort = [{'colId': getNewkey(x[0]['colId']), 'sort': x[0]['sort']}]
                replacement[key] = sort
            else:
                replacement[key] = data[key]

        else:
            replacement[key] = data[key]
            #print('not dict')
    rep = json.dumps(replacement)
    return rep


if __name__ == '__main__':

    ###load csv , both data dictionary and data
    #names= pd.read_csv(r'C:\Users\ThinkPad\Desktop\alpha\Blackbird\Chelete\LexStep\columnnames.csv')
    names_loc = sys.argv[1]
    names = pd.read_csv(names_loc)
    names.to_dict(orient='dict')
    your_dict = dict(zip(names['LEXSTEP-LEGACY'], names['LEXSTEP-NEST']))
    applied_filters.head()

    #pd.read_csv(r"C:\Users\ThinkPad\Downloads\data-integration\applied_filters.txt",sep=';')
    ##read applied_filters
    filters = sys.argv[2]
    applied_filters = pd.read_csv(filters)
    #print(applied_filters.head())
    applied_filters['applied_filters'] = applied_filters['filter'].apply(lambda x : convertJSON(x) if '{' in x else x ) ##apply function
    applied_filters.to_csv('applied_filters_fixed.csv',index=False,quote=False)

    sqlcon = create_engine('mysql://root:unlimited@localhost/lexstep')
    #
    applied_filters = pd.read_sql('select * from applied_filters',sqlcon)
    # applied_filters['applied_filters'] = applied_filters['filter'].apply(lambda x : convertJSON(x) if '{' in x else x )
    applied_filters= pd.read_csv('applied_filters.csv',sep=';')
    applied_filters['applied_filters'] = applied_filters['filter'].apply(lambda x : convertJSON(x) if '{' in x else x ) ##apply function
    applied_filters.to_csv('applied_filters_fixed.csv',index=False, sep=';', quoting=csv.QUOTE_NONE)

    applied_filters.to_json('applied_filters.json',orient='records')
    ap = pd.read_csv('applied_filters_fixed.csv',sep=';')

    convertJSON(applied_filters['filter'][44])

x = [{'colId': 'jobType', 'sort': 'desc'}]
