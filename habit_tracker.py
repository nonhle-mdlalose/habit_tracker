from datetime import datetime
import time
import os
import logging

#global variables
dt = datetime.today()
monday = []
tuesday = []
wednesday = [{"name": "code","day":"wednesday", "time":"13:57","notes":"extra tings" },{"name": "code","day":"wednesday", "time":"13:37","notes":"extra tings" }, {"name": "code","day":"wednesday", "time":"13:27","notes":"extra tings" }]
thursday = []
friday = []
saturday = []
sunday = []
habit = {}
categories = {'hobby': {}, 'gratitude': {}, 'health': {}, 'fitness': {}, 'other': {}}

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class Habit:
    def __init__(self,category, name, reminder_day, reminder_time, note):
        self.category = category
        self.name = name
        self.reminder_day = reminder_day
        self.reminder_time = reminder_time
        self.note = note

    @classmethod
    def get_user_input(self):
        #we set status to yes so a user can be prompted to add multiple habits at the same time
        status = 'yes'
        try:
            while status == 'yes'.lower():
                category = input('Enter category name (hobby, gratitude, health, fitness or other): ')
                name = input('Enter habit name: ')
                reminder_day = str(input('Enter day of reminder: ')).lower()
                reminder_time_input = str(input('Enter reminder time (hh:mm): '))
                reminder_time = datetime.strptime(reminder_time_input, "%H:%M")
                reminder_time = reminder_time.strftime("%H:%M")
                note = input('Any extra notes? : ')
                #Append habit to list based on day and to dict based on category
                habit = {"category": category, "name": name, "day": reminder_day, "time": reminder_time, "notes": note}
                append_habits_list(day=reminder_day, habit=habit)
                append_category_dict(category=category, habit=habit)
                
                #Ask user if they want to input another habit
                status = input('Would you like to enter another habit? Yes or No: ')
            else:
                print("Habit added!")
        except Exception as e:
            print('Invalid input')
            print(e)

    def print_habit(self):
        print('New Habit Stored: ', self.name)
        print("Reminder day: ", self.reminder_day, "\nReminder time: ", self.reminder_time, "\nNotes: ", self.note)



#This function  appends the appropriate list
def append_habits_list(day, habit):
    try:
        if day == 'monday':
            monday.append(habit)
        elif day == 'tuesday':
            tuesday.append(habit)
        elif day == 'wednesday':
            wednesday.append(habit)
        elif day == 'thursday':
            thursday.append(habit)
        elif day == 'friday':
            friday.append(habit)
        elif day == 'saturday':
            saturday.append(habit)
        elif day == 'sunday':
            sunday.append(habit)
    except:
        #This exception is not working
        print("Invalid day, habit not added to database")

def append_category_dict(category, habit):
    try:
        if category == "hobby".lower():
            categories['hobby'] = habit
        elif category == "gratitude".lower():
            categories['gratitude'] = habit
        elif category == "health".lower():
            categories['health'] = habit
        elif category == "fitness".lower():
            categories['fitness'] = habit
        else:
            categories['other'] = habit
    except Exception as e:
        print(e)

#checks the day list so that we can create notifications based on time
def check_reminders_for_day():
    try:
        day = dt.strftime("%A").lower()
        if day == 'monday':
            if len(monday) > 0:
                return monday
        elif day == 'tuesday':
            if len(tuesday) >0:
                return tuesday
        elif day == 'wednesday':
            if len(wednesday) > 0:
                return wednesday
        elif day == 'thursday':
            if len(thursday) > 0:
                return thursday
        elif day == 'friday':
            if len(friday) > 0:
                return friday
        elif day == 'saturday':
            if len(saturday) > 0:
                return saturday
        elif day == 'sunday':
            if len(sunday) > 0:
                return sunday
    except Exception as e:
        print(e)

def create_notification():
    try:
        time_now= dt.strftime("%H:%M").lower()
        list_item = check_reminders_for_day()
        for i in list_item:
            if time_now in i.values():
                message = "Hey there! Here is your reminder to {} for: \n{} at {} \n\n{}".format(i['name'].title(), i['day'].title(), i['time'], i['notes'].title())
                os.system(f"""
                          osascript -e 'display notification "{message}" with title "{i["name"].title()}"'
                          """)
            else:
                continue
    except Exception as e:
        print(e)

def all_habits():
    all_habits_joined = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    print(
        "Habits in the database: \n"
        "Monday: \n", all_habits_joined[0],
        "\nTuesday: \n", all_habits_joined[1],
        "\nWednesday: \n", all_habits_joined[2],
        "\nThursday: \n ", all_habits_joined[3],
        "\nFriday: \n", all_habits_joined[4],
        "\nSaturday: \n", all_habits_joined[5],
        "\nSunday\n",all_habits_joined[6],
    )

def user_commands():
    print("Hey there! Welcome to the habit tracking application. Input a command to get started\n"
          "#add : to add a new habit\n#viewhabits : to view all the habits stored in the database\n"
          "#help : to see list of commands.")
    command = input("Enter command : ")
    try:

        if command == "#help".lower():
            print("To add a new habit: #add")
        elif command == "#add".lower():
            h = Habit.get_user_input()
        elif command == "#viewhabits":
            all_habits()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    # user_commands()
    # time.sleep(15)
    h = Habit.get_user_input()
    print(categories)
    # check_reminders_for_day()
    # create_notification()
    # all_habits()
