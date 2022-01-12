from datetime import datetime
import time
from plyer import notification

habits = []

class Habit:
    def __init__(self, name, reminder_day, reminder_time, note):
        self.name = name
        self.reminder_day = reminder_day
        self.reminder_time = reminder_time
        self.note = note

    @classmethod
    def get_user_input(self):
        try:
            name = input('Enter habit name: ')
            reminder_day = str(input('Enter day of reminder: ')).lower()
            reminder_time_input = str(input('Enter reminder time (hh:mm): '))
            reminder_time = datetime.strptime(reminder_time_input, "%H:%M")
            print(type(reminder_time))
            reminder_time = reminder_time.strftime("%H:%M")
            print(type(reminder_time))

            note = input('Any extra notes? : ')
            return self(name, reminder_day, reminder_time, note)
        except:
            print('Invalid input')


    def append_habits_list(self):
        if self.reminder_day == 'monday':
            habit={}
            habit[self.name] = self.reminder_time
            habits.append(habit)
            print("Habits list:", habits)

    def print_habit(self):
        print('New Habit Stored: ', self.name)
        print("Reminder days: ", self.reminder_day, "\nReminder time: ", self.reminder_time, "\nNotes: ", self.note)


if __name__ == '__main__':
    h = Habit.get_user_input()
    h.print_habit()
    h.append_habits_list()
