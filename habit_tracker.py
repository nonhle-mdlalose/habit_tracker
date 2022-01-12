from datetime import datetime
import time
from plyer import notification
import os

#global variables
monday = []
tuesday = []
wednesday = [{"name": "code","day":"wednesday", "time":"13:57","notes":"extra tings" },{"name": "code","day":"wednesday", "time":"13:37","notes":"extra tings" }, {"name": "code","day":"wednesday", "time":"13:27","notes":"extra tings" }]
thursday = []
friday = []
saturday = []
sunday = []
habit = {}
dt = datetime.today()


class Habit:
    def __init__(self, name, reminder_day, reminder_time, note):
        self.name = name
        self.reminder_day = reminder_day
        self.reminder_time = reminder_time
        self.note = note

    @classmethod
    def get_user_input(self):
        status = 'yes'
        try:
            while status == 'yes'.lower():
                name = input('Enter habit name: ')
                reminder_day = str(input('Enter day of reminder: ')).lower()
                reminder_time_input = str(input('Enter reminder time (hh:mm): '))
                reminder_time = datetime.strptime(reminder_time_input, "%H:%M")
                reminder_time = reminder_time.strftime("%H:%M")
                note = input('Any extra notes? : ')
                status = input('Would you like to enter another habit? Yes or No: ')
            else:
                print("Habit added!")
            return self(name, reminder_day, reminder_time, note)
        except:
            print('Invalid input')

    #passes the class instance to be appended to appropriate list
    def pass_habit_to_list(self):
        day = self.reminder_day
        habit = {"name":self.name, "day":self.reminder_day, "time":self.reminder_time, "notes":self.note}
        append_habits_list(day, habit)


    def print_habit(self):
        print('New Habit Stored: ', self.name)
        print("Reminder day: ", self.reminder_day, "\nReminder time: ", self.reminder_time, "\nNotes: ", self.note)


#prompt user if they want to add another habit
def user_prompt():
    status = input('Would you like to enter another habit? Yes or No: ')
    return status

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


def check_time():
    try:

        time_now= dt.strftime("%H:%M").lower()
        list_item = check_reminders_for_day()
        for i in list_item:
            if '13:57' in i.values():
                print(i)
                os.system(f"""
                          osascript -e 'display notification "{i["notes"]}" with title "{i["name"]}"'
                          """)
                print("worked")
            else:
                continue
    except Exception as e:
        print(e)




if __name__ == '__main__':
    # time.sleep(15)
    # h = Habit.get_user_input()
    # h.print_habit()
    # h.pass_habit_to_list()
    # print(monday)
    # check_reminders_for_day()
    # create_notification()
    check_time()
