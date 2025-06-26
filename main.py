from src import logger, analyzer, visualizer
from time import sleep


def main():

    print("=" * 60)
    print("🕒 WELCOME TO FLOW MAPPER 🕒")
    print("=" * 60)
    print()
    
    print("📊 Your Personal Activity Tracking & Analysis Tool")
    print()
    
    print("Features Available:")
    print("┌─────────────────────────────────────────────────────┐")
    print("│ 📝 LOGGING MODULE                                   │")
    print("│   • Log daily activities with timestamps           │")
    print("│   • Categorize as 'focus' or 'break' activities    │")
    print("│   • Auto-save to CSV for data persistence          │")
    print("└─────────────────────────────────────────────────────┘")
    print()
    
    print("┌─────────────────────────────────────────────────────┐")
    print("│ 📈 ANALYSIS MODULE                                  │")
    print("│   • Total time spent per task                      │")
    print("│   • Task frequency counts                          │")
    print("│   • Focus vs Break time breakdown                  │")
    print("│   • Top 3 most time-consuming tasks               │")
    print("│   • Most active hour identification               │")
    print("└─────────────────────────────────────────────────────┘")
    print()
    
    print("┌─────────────────────────────────────────────────────┐")
    print("│ 📊 VISUALIZATION MODULE                             │")
    print("│   • Bar charts for task time distribution         │")
    print("│   • Pie charts for focus/break analysis           │")
    print("│   • Hourly activity patterns                      │")
    print("└─────────────────────────────────────────────────────┘")
    print()
    
    print("🚀 Ready to track your productivity flow!")
    print("💡 Start by logging your activities or analyze existing data")

    while True : 
        # read existing data

        today_df = analyzer.convert_times()
        
        sleep(2)
        print('\n'+"=" * 60)
        
        
        activities = [' 1. Log Your Day ', ' 2. Total Time Spent Per Task', ' 3. Task frequency counts ', ' 4. Focus vs Break time breakdown ', ' 5. Top 3 most time-consuming tasks', ' 6. Most active hour identification', ' 7. Bar charts for task time distribution ', ' 8. Pie charts for focus/break analysis',' 9. Hourly activity patterns' ]
        print('')
        for i in activities : # print the available services
            print(f"{i}", end = " ")
            
        choice = int(input("\n\nEnter Your choice : ")) # get user choice
        
        if choice not in list(range(1, 10)):
            print("Invalid Input! Please try again!")
            break
        
        elif choice == 1:
            task = input("Enter activity name : ").strip()
            start_time = input("Enter start time (24H format Eg : 12:55) ")
            end_time = input("Enter end time (24H format Eg : 12:55) ")
            type = input("Enter the type of the activity  (focus/break): ").lower()
            
            if type not in ['focus', 'break']:
                print('Invalid input! Please try again!')
                break
            
            elif ':' not in start_time or ':' not in end_time:
                print('Invalid input! Please try again!')
                break
            
            # call the function 
            logger.log_activity(task, start_time, end_time, type)
            
        
        # total time taken per task
        elif choice == 2:
            tasks = analyzer.total_time_per_task()
            print(tasks)
        
        # total number of unique tasks (dont consider duplicate)
        elif choice == 3:
            task_count = analyzer.task_counts()
            print(task_count)
        
        # focus vs break breakdown
        elif choice == 4:
            tasks_by_tags = analyzer.group_by_tags()
            print(tasks_by_tags)
            
        # Top 3 most time-consuming tasks
        elif choice == 5:
            top_three_tasks = analyzer.top_three_tasks()
            print(top_three_tasks)
           
        # Most active hour identification
        elif choice == 6:
            most_active, max_time, hour_summary = analyzer.most_active_hour()
            print(most_active)
            print(max_time)
        
        #  Bar charts for task time distribution
        elif choice == 7:
            visualizer.plot_tasks_bar(today_df)
            
        #Pie charts for focus/break analysis
        elif choice == 8:
            visualizer.plot_focus_pie(today_df)
        
        # Hourly activity patterns
        elif choice == 9:
            most_active, max_time, hour_summary = analyzer.most_active_hour()
            visualizer.plot_hourly_bar( hour_summary)
        
        elif choice == 10:
            print("Have a great day!")

if __name__ == "__main__":
    main()


