import matplotlib.pyplot as plt
import seaborn as sns


#  Bar Chart → Time Spent per Task
def plot_tasks_bar(df):
    sns.barplot(data = df, x = 'activity_name', y = 'total_time')
    plt.show()

# Pie Chart → Focus vs Break 
def plot_focus_pie(df):
    focus_break_data = df.groupby('type')['total_time'].sum()
    plt.pie(focus_break_data.values,labels=focus_break_data.index, autopct='%1.1f%%' )
    plt.show()

# Bar Chart → Active Hours
def plot_hourly_bar(h_summary):
    plt.bar(h_summary.index, h_summary.values)
    plt.show()