#!/usr/bin/env python
import pandas as pd
from datetime import datetime
import json
from tkinter import *
from tkinter.ttk import *
from lilmodmod.module import *


pd.set_option("display.max_colwidth", 10000) # ! Important !

check_config()

m = pd.DataFrame()

with open('config.json','r') as f:
    file = json.load(f)

for i in file['groups']:
    disease_group = MDSS_DiseaseGroup(diseases=i['diseases'],
                        case_settings=i['settings']['Case Status'],
                        investigation_settings=i['settings']['Investigation Status'])
    df = prompt_user_for_path(disease_group)
    for disease in disease_group.diseases:
        m[disease] = df[disease]


n = transpose_add_YTD(m)
k = n.set_index(['Disease'])
k = k.loc[k['Time'] < datetime.fromisoformat(datetime.today().isoformat()[:7] + '-01')]
k.reset_index(inplace=True)
k.set_index(['Disease','Month'], inplace=True)
k['Month Median'] = k.groupby(['Disease','Month'])['Count'].median().reset_index().set_index(['Disease','Month'])['Count']
k.to_csv('test.csv')
