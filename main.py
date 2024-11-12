import time
import plyer
from datetime import datetime

print("Current time is: ", datetime.now().strftime("%H:%M"))

def get_valid_time():
    while True:
        time_input = input("When do you want to be reminded? (Houre:MM) ")
        try:
            return datetime.strptime(time_input, "%H:%M").time()
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

def main():
    reminders = []

    while True:
        print("---------------------------------------------")
        print("\n1. Add reminder")
        print("2. View reminders")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            reminder = input("What do you want to be reminded of? ")
            reminder_time = get_valid_time()
            reminders.append((reminder, reminder_time))
            print("Reminder added successfully!")

        elif choice == '2':
            if reminders:
                print("\nCurrent reminders:")
                for i, (reminder, reminder_time) in enumerate(reminders, 1):
                    print(f"{i}. {reminder} at {reminder_time.strftime('%H:%M')}")
            else:
                print("No reminders set.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")
            

    print("Checking reminders...")
    while reminders:
        current_time = datetime.now().time()
        for reminder, reminder_time in reminders[:]:
            if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
                plyer.notification.notify(
                    title="Reminder",
                    message=reminder,
                    app_icon = r"D:\python projects\reminder\reminder.ico",
                    app_name = "Reminder By ZAN",
                    timeout=10
                )
                reminders.remove((reminder, reminder_time))
        time.sleep(30)  

if __name__ == "__main__":
    main()
