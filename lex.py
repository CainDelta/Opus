import json
import pandas as pd
import os
import collections

os.getcwd()
names = pd.read_csv(r'C:\Users\ThinkPad\Desktop\alpha\Blackbird\Chelete\LexStep\columnnames.csv')
names.to_dict(orient='dict')
your_dict = dict(zip(names['LEXSTEP-LEGACY'], names['LEXSTEP-NEST']))


with open('testing.json') as f:
  data = json.load(f)

data.keys()
data['filter'].keys()
data['filter']

def getNewkey(k):
    if (your_dict.get(k)):
        return (your_dict.get(k))
    else:
        return k

##declare empty filter
filter = {}
## loop through keys in filter then append to dict, its duplicating on purpose to remove [] brackets
new_dict={}
dict_list = []
for k,v in data['filter'].items():

    new_key = getNewkey(k)
    value = v
    new_dict[new_key] = v
    dict_list.append(new_dict)


filter['filter'] = dict_list[0]
filter['filter']

new_data = data
new_data['filter'] = filter['filter']
new_data
