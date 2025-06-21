import numpy as np
import pandas as pd
import glob
import datetime as datetime

# read the data
def read_data():
    # dynamic file searching approach
    f_name = glob.glob('**/data/activity_log.csv', recursive = True)[0]
    try :
        df = pd.read_csv(f_name, parse_dates = [0])
        
    # Raise exception if there is no data / file     
    except FileNotFoundError as e:
        print("File/data does not exists! Please add some data and try again.")
        return None
    
    return df

df = read_data()    
print(df.head())
#---------------------------------

# convert start and end time to proper datatypes (date time)
def convert_times():
    convert = lambda x : pd.to_datetime(df['date'].astype(str) + ' ' + df[x].astype(str))

    df['start_time'] =  convert('start_time')
    df['end_time'] =  convert('end_time')

convert_times()

# total time per task
def total_time_per_task():
    df['total_time'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60
    
    # groupby task and calculate real total time
    temp = df.groupby('activity_name')['total_time'].sum()
    return temp

# temp = total_time_per_task()


