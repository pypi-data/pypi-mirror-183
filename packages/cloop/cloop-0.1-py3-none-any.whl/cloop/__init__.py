# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 07:58:18 2022

@author: user
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import os
import pickle

import time
from datetime import datetime

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import numpy as np
import json
import rapidb
import cloopui as ui
import subprocess
from multiprocessing import Process



_history = pd.DataFrame(np.zeros([0,1])).rename(columns={0:"time"})
_sv = {}
_ui_activated = False
_data = {}



def get_DF(table_name):
    db = rapidb.sqlite()
    df = db.get_DataFrame(table_name)
    df['date_time'] = pd.to_datetime(df['date_time'])
    db.conn.close()
    return df



def is_ui_activated():
    return globals()["_ui_activated"]



def get_ui_slider(obj_name,default_value=0):
    if globals()["_ui_activated"]:
        if(obj_name in globals()["_data"]):
            return globals()["_data"][obj_name]
        else:
            print(f"{obj_name} not found in UI, returning default")
            return default_value
    else:
        return default_value

def get_ui_select(obj_name,default_value=""):
    return get_ui_slider(obj_name,default_value)
    


def get_ui_button(obj_name,default_value=False):
    if globals()["_ui_activated"]:
        if(obj_name in globals()["_data"]):
            return globals()["_data"][obj_name] 
        else:
            print(f"{obj_name} not found in UI, returning default")
            return default_value
    else:
        return default_value

    


def save_value(var_name,value):
    globals()["_sv"][var_name] = value



def start_webserver():
    webserver.app.run(host="0.0.0.0",debug=True)



def start_loop(activation=True,
         ui=None,
         min_time=10,
         keep=500):
        
    
    if activation:
        
        
    
        # Connect to database
        db = rapidb.sqlite()
        
        
        # Extract all existing variables and imported modules
        import __main__    
        for key in dir(__main__):
            if (key[:2] != "__") & \
               (key not in ["get_ui_value","save_value","loop"]):
                exec( f"{key} = __main__.{key}" )
                exec( f"global {key}" )
    
    
        # Get frames
        from inspect import currentframe, getouterframes
        frameinfo = getouterframes(currentframe())
        
        # Get executed script
        import sys
        file = sys.argv[0].lower()
        folder = file.split("/")[-1].split("\\")[-1].split(".py")[0]
        if( os.path.isdir(folder) == False ): # Create folder
            os.mkdir(folder)
            # Create last ui time
            file = open(folder+"/lastuitime.txt","w")
            file.write("0")
            file.close()
        
        # Create webpage
        if (ui is not None):
            ui.webpage(folder)
            
        
        # Extract script
        lineno = 1
        for fi in frameinfo:
            if(file == fi.filename):
                print("found",fi.lineno)
                lineno = int(fi.lineno)
                
        script = open(sys.argv[0]).read().splitlines()

        
        # Verify presence of loop
        pos = -1
        for i in range(len(script)):
            if(len(script[i])>=10):
                if((script[i][0] != " ")&(script[i][:10].replace(" ","").replace(".","").\
                       replace("cl","").replace("cloop","") == "start_loop")):
                    pos = i
                    
                    # Find last row of this command
                    found_final = True
                    while(found_final):
                        sline = script[pos].replace(" ","")
                        if(sline[-1]==")"):
                            found_final = False
                        else:
                            pos += 1
                
        script = script[pos+1:]
        
        script = "\n".join(script)
        
        
        # WHILE LOOP ==========================================================
        while(1):
            
            ts = time.time()
            
            
            # Check if UI is activated
            print("")
            try: 
                lastuitime = float(open(folder+"/lastuitime.txt").read())
                if np.abs(ts-lastuitime) < (min_time*5):
                    globals()["_ui_activated"] = True
                    print(str(datetime.now())[:19] + " - UI activated")                    
                    # Load data
                    globals()["_data"] = pickle.load( open(folder+"/input_data.pkl","rb") )
                    # Replace bool
                    for key in globals()["_data"]:
                        if globals()["_data"][key] == "false":
                            globals()["_data"][key] = False
                        elif globals()["_data"][key] == "true":
                            globals()["_data"][key] = True
                else:
                    globals()["_ui_activated"] = False
                    globals()["_data"] = {}
                    print(str(datetime.now())[:19] + " - UI not found")
            except:
                0
            
            
            # Execute loop script
            globals()["_sv"] = {}
            exec(script)
            
            # Insert data to db
            temp_dict = globals()["_sv"].copy()
            temp_dict.update(globals()["_data"])
            db.insert_row(folder,temp_dict)
            
            
            # Insert data to history
            new_index = np.max(globals()["_history"].index) + 1
            if pd.isnull(new_index):
                new_index = 0
            
            # Insert time
            globals()["_history"].loc[new_index] = None
            globals()["_history"].loc[new_index,"time"] = \
                datetime.fromtimestamp(ts)
            
            # Insert data for each key
            columns = list(globals()["_history"].columns)
            for key in globals()["_sv"].keys():
                # Create DataFrame column if not existing
                if(key not in columns):
                    globals()["_history"][key] = None
                globals()["_history"].loc[new_index,key] = globals()["_sv"][key]
            
            # Remove first row
            globals()["_history"] = globals()["_history"].iloc[-keep:]
            
            # Create json and save data
            datasave = {}
            columns = list(globals()["_history"].columns)
            for c in columns:
                if c != "time":
                    datasave[c] = list(globals()["_history"][c])
                else:
                    datasave[c] = list(globals()["_history"][c].astype(str))
                    
            datasave = "data = " + json.dumps(datasave).replace("NaN","null")
            file = open(folder+"/data.js","w")
            file.write(datasave)
            file.close()
            
            file = open(folder+"/dataid.js","w")
            file.write("dataid = " + str(np.random.randint(1,99999999)))
            file.close()
            
            # Wait remaining time
            rm = min_time - (time.time() - ts)
            if(rm > 0):
                time.sleep(rm)
            

