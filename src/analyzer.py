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
    
    # obtain current date for further daily insights
    today = pd.Timestamp(datetime.date.today())
    global today_df
    # create only TODAY's dataframe
    today_df = df[df['date'] == today].copy()
    
    return df, today_df

#---------------------------------

# convert start and end time to proper datatypes (date time)
def convert_times():
    # call the read_data() function
    df, today_df = read_data()
    
    convert = lambda x : pd.to_datetime(today_df['date'].astype(str) + ' ' + today_df[x].astype(str))

    today_df['start_time'] =  convert('start_time')
    today_df['end_time'] =  convert('end_time')

    # total_time column
    today_df['total_time'] = (today_df['end_time'] - today_df['start_time']).dt.total_seconds() / 60
    return today_df

# total time per task
def total_time_per_task():
    global today_df
    
    if today_df.shape[0] == 0:
        return "No activities for today were inserted !"
    
    
    # groupby task and calculate real total time
    tasks = today_df.groupby('activity_name')['total_time'].sum()
    return tasks



# total number of times  a task was done in a day
def task_counts():
    if today_df.shape[0] == 0:
        return "No activities for today were inserted !"
    
    task_count = today_df['activity_name'].value_counts()
    return task_count



# group the activities by the tags (break / focus) for that day
def group_by_tags():
    if today_df.shape[0] == 0:
        return "No activities for today were inserted !"
    
    tasks_by_tags = today_df.groupby('type').agg(
        {
            'activity_name' : 'count', # how many unique activities were done
            'total_time' : 'sum', # absolute total time spent overall
        }
    )
    # rename the activity name column, because it will contain count of unique tasks, not names
    renamed_tags = tasks_by_tags.rename(columns = {'activity_name' : 'activity_count'})
    return renamed_tags


# top 3 tasks by total time taken
def top_three_tasks():
    return today_df.sort_values(by = 'total_time', ascending=False)[['activity_name', 'total_time']].head(3)



# find the most active hour 
def most_active_hour():
    today_df['hour'] = today_df['start_time'].dt.hour

    hour_summary = today_df.groupby('hour')['total_time'].sum()
    
    # find the most active hour
    most_active = hour_summary.idxmax() # find the max hour (index value)
    max_time = hour_summary.max() 
    
    return most_active, max_time, hour_summary

