##game to increase productivity!
import time
from datetime import datetime
import json

#function to print characters in output string based on seconds
cps = 0
  
def print_slow(str):
    for char in str:
        print(char, end='', flush=True)
        time.sleep(cps)
    print()  

# Global variables
tasks = {}
total_xp = 0
past_time = 0 # Default value for past_time
#function to create tasks
def task_create(task_name , gain_xp , loss_xp ):
    if task_name in tasks:
        print_slow("task already exists ")
        print_slow("try creating another task please")
    else:
        tasks[task_name]={"gain_xp":gain_xp , "loss_xp":loss_xp}
        print_slow(f"The {task_name} was created succesfully")
        print_slow(f"complete {task_name} and gain {gain_xp} xp")
        print_slow(f"failure to finish task at time will result in loss of {loss_xp} xp")

#function to delete tasks
def task_delete(task_name):
    if task_name in tasks:
        print_slow("Are you sure you wanna remove this task?")
        clear_response = input(print_slow("Enter yes or no") )
        clear_response = clear_response.lower()
    else:
        print_slow("Task doesn't exist, therefore it can't be removed silly!")


    if clear_response == "yes":
        del tasks[task_name]  # Remove the task
        print_slow(f"{task_name} has been removed successfully!")
    else:
         print_slow(f"{task_name} was not removed, maybe a BUG or you didn't type yes properly? ")
         print_slow("Or you wanted to not remove it after second thought and chose no")

#function to view tasks
def view_tasks():
     if tasks:
        for task, details in tasks.items():
            print_slow(f"{task}: Gain {details['gain_xp']} XP | Loss {details['loss_xp']} XP")
     else:
        print_slow("No tasks available.")
#saving progress of game
def save_progress():
    data = {
        "total_xp": total_xp,  # User's XP
        "tasks": tasks,  # Dictionary of tasks
        "past_time": past_time.isoformat()  # Save past_time as a string in ISO format
    }
    with open("xp_progress.json", "w") as file:
        json.dump(data, file, indent=4)  # Saves in a readable format

#loading progress of game
def load_progress():
    global total_xp, tasks , past_time  # Ensure these variables can be modified
    try:
        with open("xp_progress.json", "r") as file:
            data = json.load(file)
            total_xp = data.get("total_xp", 0)  # Default to 0 if missing
            tasks = data.get("tasks", {})  # Default to empty dict if missing
            past_time_str = data.get("past_time", 0)

            if past_time_str:
                past_time = datetime.fromisoformat(past_time_str)  # Convert string back to datetime
            else:
                past_time = 0
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ No saved progress found or file is corrupted.")

# Function to reset the tasks in the JSON file
def reset_tasks():
    data = {
        "total_xp": total_xp,  # Keep the current XP
        "tasks": {},  # Reset the tasks dictionary to an empty one
        "last_played": datetime.now().isoformat()  # Update the last played time
    }

    # Save the empty tasks dictionary in the JSON file
    with open("xp_progress.json", "w") as file:
        json.dump(data, file, indent=4)

    print_slow("Tasks have been reset! All tasks are deleted.")

'''
# Get current time and compare it with past time
current_time = 0
current_time = datetime.now().time()
past_time = 0
'''
'''def time_manipulate(current_time):
  if (current_time - past_time).days  >= 1:
    print_slow("it's been more than 1 day since you have opened this script")
    print_slow("do you wanna clear all previous tasks? ")
    time_response=input(print_slow("Enter yes or no") )
  else:
    print_slow("error")
  if time_response == "yes":
    print_slow("resetting tasks.......")
    reset_tasks() '''  



# Updated time manipulation function
def time_manipulate():
    global past_time
    current_time = datetime.now()  # Use datetime to include both date and time

    # Check if past_time is set and calculate the difference
    if past_time:
        time_difference = current_time - past_time
        if time_difference.days >= 1:  # If it's been more than 1 day
            print_slow("It's been more than 1 day since you last opened this script.")
            print_slow("Do you want to clear all previous tasks?")
            time_response = input("Enter yes or no: ")
            time_response= time_response.lower()
            if time_response == "yes" or "y":
                print_slow("Resetting tasks...")
                reset_tasks()
            else:
                print_slow("Tasks will remain unchanged.")
        else:
            print_slow("It's been less than 1 day since your last session.")
    else:
        print_slow("No previous playtime found, this is your first time playing.")

    # After checking, update past_time
    past_time = current_time


# function to evaluate and make user gain xp upon task completion
def task_complete(task_name):
    global total_xp  # Declare global total_xp
    if task_name in tasks:
        task = tasks[task_name]  # Get the task dictionary
        print_slow(f"Task: {task_name}")
        print_slow(f"✅ XP Gained: {task['gain_xp']}")
        total_xp+=task['gain_xp']
    else:
        print_slow("Task not found!")

#function to evaluate and  make user loss xp upon failure of task completion on time
def task_failure(task_name):
    global total_xp  # Declare global total_xp
    if task_name in tasks:
        task = tasks[task_name]  # Get the task dictionary
        print_slow(f"Task: {task_name}")
        print_slow(f" XP lost: {task['loss_xp']}")
        total_xp-=task['loss_xp']
    else:
        print_slow("Task not found!")



# Main menu
def main():
    load_progress()  # Load progress on startup
    time_manipulate() #checks time on startup
    print("DO YOU WANT TO ACTIVATE OUTPUT SPEED?")
    print("WARNING: THIS MIGHT MAKE THE SCRIPT RIDICULOUSLY SLOW-")
    print("ENTER Y FOR YES AND N FOR NO")
    while True:
     output_speed=input()
     output_speed=output_speed.lower()
     if output_speed == "y" or "yes" :
        print("select the desired text speed.... ")
        print("Recommended value (from 0.01 to 0.2) anymore or less will make it useless")
        cps = input()
        print_slow(cps)
        break
     elif output_speed == "n" or "no":
        print("The script will run on default speed...")
        break
     else:

      print("give a valid input!! like yes or no!")

    while True:
        print_slow("\n🔹 Productivity Game Menu 🔹")
        print_slow("Enter 1 to Create a Task")
        print_slow("Enter 2 to Delete a task")
        print_slow("Enter 3 to View Tasks")
        print_slow("Enter 4 to Complete a Task")
        print_slow("Enter 5 if you failed a Task")
        print_slow("Enter 6 to Save Progress")
        print_slow("Enter 7 to Exit Game")

       
       
        choice = input().strip()

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_name = task_name.lower()
            gain_xp = int(input("Enter XP gain for this task: "))
            while not isinstance(gain_xp, int) or gain_xp <= 0:
               try:
                    gain_xp = int(input("The XP gained must be a positive Natural number (positive integer): "))
               except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            loss_xp = int(input("Enter xp loss for this task"))
            
            while not isinstance(loss_xp,int) or loss_xp <=0:
               try:
                    loss_xp = input("The xp loss must be given a positive integer: ")
               except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            task_create(task_name, gain_xp, loss_xp)

        elif choice == "2":
            task_name = input("Enter the task name you failed: ")
            task_name = task_name.lower()
            task_delete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            task_name = input("Enter the task name to complete: ")
            task_name = task_name.lower()
            task_complete(task_name)
        elif choice == "5":
            task_name = input ("Enter the task name you failed: ")
            task_failure(task_name)
        elif choice == "6":
            save_progress()
        elif choice == "7":
             save_progress()  # Save before exit
             print_slow("Exiting... Your progress is saved! ")
             break
        else:
            print_slow(" Invalid choice! Please enter a number between 1 and 6.")

# Run the program
main()