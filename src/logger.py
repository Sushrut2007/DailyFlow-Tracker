import datetime as datetime
import os
import pandas as pd

"""
1. Obtain current date
2. store each data in the csv file
3. create csv file if not exist

"""
def log_activity(activity_name, start_time, end_time, type):
    
    # create a dataframe row 
    row = pd.DataFrame({
        'activity_name' : [activity_name], 
        'start_time' : [start_time],
        'end_time' : [end_time],
        'type' : [type]
    })
    
    # obtain today's date to store 
    try: 
        current_date = datetime.date.today()
    except Exception as e:
        print(f"Error getting current date! Using next date of previous entry instead! ")

    
    # create / open file 
    try :
        # get current file folder name (src)
        current_file_dir = os.path.dirname(__file__)
        # get main folder of current folder (Flow Mapper)
        project_root = os.path.dirname(current_file_dir)
        # obtain the path of the data folder
        data_folder = os.path.join(project_root, 'data')
        
        # create data folder if it doesn't exists (future expansion)
        
        
        file_path = os.path.join(data_folder, 'activity_log.csv')
        
        # check if above file exists, if not create it
        if not os.path.exists(file_path):
            # create empty file and insert the first row
            
            row.to_csv(file_path, index=False)
        else:
            row.to_csv(file_path, mode = 'a', index=False, header = False)  # only includes the values of row
            
    except Exception as e:
        print(f"File related issue {e} ")


# eg calling in main.py
log_activity('eat', '10:30', '10:45', 'break')  
   
