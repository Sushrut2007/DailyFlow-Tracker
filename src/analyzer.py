import numpy as np
import pandas as pd
import glob

# read the data
def read_data():
    # dynamic file searching approach
    f_name = glob.glob('**/data/activity_log.csv', recursive = True)[0]
    try :
        df = pd.read_csv(f_name)
        
    # Raise exception if there is no data / file     
    except FileNotFoundError as e:
        print("File/data does not exists! Please add some data and try again.")
        return None
    
    return df



#df = read_data()    
#print(df.head())