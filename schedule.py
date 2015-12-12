import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calendar = [] #days
        self.average_sleep = 0

    def add_day(self):
        if not self.calendar or datetime.datetime.today().day != self.calendar[:-1].date.day:
            self.calendar.append(Day())
        pass

    def add_task(self, task):
        curr_day = self.calendar[-1]
        curr_day.tasks.append(task)
        if task.name is 'sleep':
            self.average_sleep = average_sleep(self)
        curr_day.productivity = day_productivity(curr_day)

    def curr_day(self):
        return self.calendar[-1]

class Task:
    def __init__(self, name, time, productivity):
        name = str(name).lower()
        if name is 'sleeping':
            name = 'sleep'
        self.name = name;
        self.time = time;
        self.productivity = productivity;

class Day:
    def __init__(self):
        self.date = datetime.datetime.today()
        self.tasks = [] #tasks
        self.productivity = 0

def average_sleep(user):
    all_sleep = [day.task.time for day in user.calendar if (day.task.name == 'sleep')]
    avg_sleep = sum(all_sleep) / len(all_sleep)
    return average_sleep

def day_productivity(day):
    all_tasks = [task.productivity for task in day.tasks]
    if all_tasks:
        return round(sum(all_tasks) / len(all_tasks), 2)

