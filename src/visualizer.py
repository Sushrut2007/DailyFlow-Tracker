import matplotlib.pyplot as plt
import seaborn as sns


#  Bar Chart → Time Spent per Task
def plot_tasks_bar(df):
    sns.barplot(data = df, x = 'activity_name', y = 'total_time')
    

# Pie Chart → Focus vs Break 
def plot_focus_pie(df):
    plt.pie(y = 'total_time', labels = df['type'])
    

# Bar Chart → Active Hours
def plot_hourly_bar(h_summary):
    plt.bar(h_summary.index, h_summary.values)