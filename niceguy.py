#!/usr/bin/env python3
from nicegui import ui
import pandas as pd
from datetime import *
import json
from tkinter import *
from tkinter.ttk import *
from src.epi_helper.lilmodmod.module import *

with open('config.json','r') as f:
    config = json.load(f)
    
groups = [MDSS_DiseaseGroup(diseases=i['diseases'],
                        case_settings=i['settings']['Case Status'],
                        investigation_settings=i['settings']['Investigation Status']) 
                        for i in config['groups']
                        ]

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle()).props('flat color=white icon=menu')
    with ui.tabs() as tabs:
        ui.tab('Settings')
        ui.tab('B')
        ui.tab('C')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='Settings').classes('w-full'):
    with ui.tab_panel(''):
        ui.label('Content of B')
        ui.button('Choose file', on_click="good job", icon='Button')
    with ui.tab_panel('Settings'):
        ui.label('Settings')
        #ui.element()
        for diseases, case_settings, investigation_settings in zip(groups[2].diseases, groups[2].case_settings, groups[2].investigation_settings):
            ui.expansion(str(diseases))



    with ui.tab_panel('C'):
        ui.label('Content of C')
ui.run(native=True, window_size=(720, 500), fullscreen=False)
