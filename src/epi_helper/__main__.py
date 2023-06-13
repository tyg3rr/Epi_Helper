#!/usr/bin/env python
import pandas as pd
from datetime import datetime
import json
from tkinter import *
from tkinter.ttk import *
from src.epi_helper.lilmodmod.module import *


pd.set_option("display.max_colwidth", 10000) # ! Important !

check_config()

m = pd.DataFrame()

with open('config.json','r') as f:
    file = json.load(f)

for i in file['groups']:
    dg = MDSS_DiseaseGroup(diseases=i['diseases'],
                        case_settings=i['settings']['Case Status'],
                        investigation_settings=i['settings']['Investigation Status'])
    df = prompt_user_for_path(dg)
    for disease in dg.diseases:
        m[disease] = df[disease]



m.to_csv('dataset.csv')
