# 🕒 Flow Mapper

A Python tool for tracking and analyzing your daily activities with visual insights.

## 🚀 Quick Start

### Install Dependencies
```bash
pip install pandas matplotlib seaborn
```

### Run Application
```bash
python main.py
```

## 📋 Features

**Track Activities**: Log tasks with timestamps and categorize as focus/break  
**Analyze Patterns**: View time spent, task frequency, and productivity breakdown  
**Visualize Data**: Generate charts for better insights  

## 🎯 Usage

The app provides a simple menu with 9 options:

1. **Log Your Day** - Add new activities
2. **Total Time Spent Per Task** - See time breakdown
3. **Task Frequency Counts** - How often you do each task
4. **Focus vs Break Breakdown** - Work-rest balance analysis
5. **Top 3 Time-Consuming Tasks** - Your biggest time investments
6. **Most Active Hour** - Peak productivity time
7. **Bar Charts** - Visual time distribution
8. **Pie Charts** - Focus vs break visualization
9. **Hourly Patterns** - Activity trends by hour

## 📊 Sample Output

### Time Analysis
```
activity_name
coding      120.0
meetings     45.0
lunch        30.0
Name: total_time, dtype: float64
```

### Focus vs Break
```
         activity_name  total_time
type                            
break                2        45.0
focus                3       165.0
```

### Most Active Hour
```
Most active hour: 14
Max time in that hour: 75.0 minutes
```

## 📁 Project Structure
```
Flow Mapper/
├── main.py              # Main application
├── data/
│   └── activity_log.csv # Your data (auto-created)
└── src/
    ├── logger.py        # Activity logging
    ├── analyzer.py      # Data analysis
    └── visualizer.py    # Charts & graphs
```

## 💡 Tips

- Use 24-hour format for times (e.g., 14:30)
- Activities are automatically saved to CSV
- Charts open in separate windows
- Data persists between sessions

## 🛠️ Built With

Python • Pandas • Matplotlib • Seaborn

---

**Start tracking your productivity today! ⭐**

**********************************************
### Note : If You have any trouble setting up the folder structure, 
## please feel free to create an issue!
