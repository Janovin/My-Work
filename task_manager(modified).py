'''
Response to first review: 
-- Please see line 281 for where the user can edit the status of the task.
-- I find no issue with the generate reports function. Perhaps use the 'tasks' and 'users' text files I have now added to the Dropbox folder
'''
#Import libraries
import datetime
today = datetime.datetime.now().date()

#Define functions
def reg_user():
        for i in range(2):     # Added loop to try again if user exists
            user_name = input("New username: ")
            pass_word = input("New password: ")
            pass_word_conf = input("Confirm your new password: ")
            if user_name in usernames:
                print("This username already exists, please choose another username.")
            elif pass_word in passwords:    # Made this an elif cause it would still log user if user was taken
                print("This password already exists.")
            elif pass_word != pass_word_conf:
                print("Your passwords do not match. Please try again")
            else:
                users = open("user.txt", "a")
                users.write(f"\n{user_name}, {pass_word}")
                users.close()
                break

def add_task():
    global number_of_tasks
    global number_of_my_tasks
    number_of_tasks += 1
    with open("tasks.txt", "a") as tasks:
            user = input("Enter the username of the person responsible for completing the task: ")
            if user == username:
                number_of_my_tasks += 1
            task = input("Title of the task: ")
            description = input("Description of task: ")
            due_date = input("Due date of task e.g. '2023-05-16' : ")
            completion = input("Is the task completed? 'Yes' or 'No': ")
            date_assigned = today
            tasks.write(f"\n{user}, {task}, {description}, {date_assigned}, {due_date}, {completion}")
            tasks.close()

def view_all():
    with open("tasks.txt", "r") as tasks:
            for lines in tasks:
                temp = lines.strip().split(", ")
                if len(temp) > 1:
                    user_list = temp[0]
                    tasks_list = temp[1]
                    description_list = temp[2]
                    due_date_list = temp[3]
                    date_assigned_list = temp[4]
                    completion_list = temp[5]
                    
                    print(f'''
                    ___________________________________________________________________
                    Task:                               {tasks_list}
                    Assigned to:                        {user_list}
                    Dates assigned:                     {date_assigned_list}
                    Due Date:                           {due_date_list}
                    Description:                        {description_list}
                    Completed:                          {completion_list}
                    ___________________________________________________________________''')

def view_mine():
    with open("tasks.txt", "r") as tasks:
        for task_number, lines in enumerate(tasks, 1):
                temp = lines.strip().split(", ")
                if temp[0] == username:
                    user_list = temp[0]
                    tasks_list = temp[1]
                    description_list = temp[2]
                    date_assigned_list = temp[3]
                    due_date_list = temp[4]
                    completion_list = temp[5]

                    print(f'''
                    ___________________________________________________________________
                    Task {task_number}:                 {tasks_list}
                    Assigned to:                        {user_list}
                    Dates assigned:                     {date_assigned_list}
                    Due Date:                           {due_date_list}
                    Description:                        {description_list}
                    Completed:                          {completion_list}
                    ___________________________________________________________________''')  


def generate_reports():
    global number_of_tasks
    global number_of_my_tasks

    num_completed_tasks = 0
    num_incomplete_tasks = 0
    overdue_tasks = 0
    num_users = 0
    task_count = {}

    with open('tasks.txt', 'r') as tasks:
        for line in tasks:
            if ", Yes" in line:
                num_completed_tasks += 1
            elif ", No" in line:
                num_incomplete_tasks += 1

            specific_task = line.strip().split(', ')
            if len(specific_task) >= 6 and specific_task[5] == 'No':
                due_date_1 = datetime.datetime.strptime(specific_task[4], '%Y-%m-%d').date()
                if due_date_1 < today:
                     overdue_tasks += 1
            
            elements = line.strip().split(', ')
            if len(elements) > 0:
                word = elements[0]
                task_count[word] = task_count.get(word, 0) + 1
                
            percentage_incomplete = (num_incomplete_tasks/number_of_tasks)*100
            percentage_overdue = (overdue_tasks/number_of_tasks)*100
        
        
    with open('task_overview.txt', 'w') as tasks_overview:
        tasks_overview.write(f"Total number of tasks: {number_of_tasks}\n")
        tasks_overview.write(f"Completed tasks: {num_completed_tasks}\n")
        tasks_overview.write(f"Incomplete tasks: {num_incomplete_tasks}\n")
        tasks_overview.write(f"Number of incomplete overdue tasks: {overdue_tasks}\n")
        tasks_overview.write(f"Percentage of tasks incomplete: {percentage_incomplete}%\n")
        tasks_overview.write(f"Percentage of overdue tasks: {percentage_overdue}%\n")

    # Start with the user_overview.txt
    
    with open("user.txt", "r") as users:
            for line in users:
                if len(line.strip().split(", ")) > 0:
                    num_users += 1

    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"Total number of users: {num_users}\n")
        user_overview.write(f"Total number of tasks: {number_of_tasks}\n")

    with open("user.txt", "r") as users:
        for line in users:
            user = line.strip().split(", ")[0]  #Contains username
            with open("user_overview.txt", "a") as user_overview:
                users_tasks = 0
                users_complete = 0
                users_incomplete = 0
                users_overdue = 0
                with open("tasks.txt", "r") as tasks:
                    for line in tasks:
                        temp = line.strip().split(", ")
                        if (temp[0] == user):
                            users_tasks += 1
                            if (temp[5] == "Yes"):
                                users_complete += 1
                            else:
                                users_incomplete += 1
                                due_date_1 = datetime.datetime.strptime(specific_task[4], '%Y-%m-%d').date()
                                if due_date_1 < today:
                                    users_overdue += 1
                
                if users_tasks != 0:
                    percentage_assigned = users_tasks/number_of_tasks * 100
                    percentage_completed = users_complete/users_tasks * 100
                    percentage_incompleted = users_incomplete/users_tasks * 100
                    percentage_overdue_incomplete = users_overdue/users_tasks * 100
                else:
                    percentage_assigned = 0
                    percentage_completed = 0
                    percentage_incompleted = 0
                    percentage_overdue_incomplete = 0

                user_overview.write(f"\nThe number of tasks assigned to {user}: {users_tasks}\n")
                user_overview.write(f"Percentage of tasks assigned to {user}: {percentage_assigned}%\n")
                user_overview.write(f"Percentage of {user}'s complete tasks: {percentage_completed}%\n")
                user_overview.write(f"Percentage of {user}'s incomplete tasks: {percentage_incompleted}%\n")
                user_overview.write(f"Percentage of {user}'s overdue incomplete tasks: {percentage_overdue_incomplete}%\n\n")



#Create empty lists
usernames = []
passwords = []
user_list = []
tasks_list = []
description_list = []
date_assigned_list = []
due_date_list = []
completion_list = []

#Create global variables
username = ""
password = ""
number_of_tasks = 0
number_of_my_tasks = 0


def main():

    global username
    global password
    global number_of_tasks
    global number_of_my_tasks

#------Login section---------------------------------------------------------------------------------------------
    with open("user.txt", "r") as users:
        for lines in users:
            temp = lines.strip().split(", ")
            usernames.append(temp[0])
            passwords.append(temp[1])

    username = input("Username: ")
    password = input("Password: ")

#-----Login details validation------------------------------------------------------------------------------------

    while True:
        if username not in usernames or password != passwords[usernames.index(username)]:
            print("Incorrect username or password.")
            username = input("Username: ")
            password = input("Password: ")
        else:
            break

# Count the total number of tasks and how many are assigned to the user

    with open("tasks.txt", "r") as tasks:
        for line in tasks:
            temp = line.strip().split(", ")
            if len(temp) > 1:
                number_of_tasks += 1
                if temp[0] == username:
                    number_of_my_tasks += 1



#-------------Task manager for non-admin users -------------------------------------------------------------------
    while True:
        if username != "admin":
            menu = input('''Select one of the following Options below:
                a - Adding a task
                va - View all tasks
                vm - view my task
                e - Exit
                : ''').lower()
    
    #---------Task manager for admin------------------------------------------------------------------------------
        else:
            menu = input('''Select one of the following Options below:
                r - Register a user
                s - Statistics
                a - Adding a task
                va - View all tasks
                vm - View my tasks
                gr - Generate reports
                e - Exit
                : ''').lower() 

    #-------------------------Registering new user ----------------------------------------------------------------
        if menu == 'r' and username == 'admin':
            reg_user()

    #--------------------------Allowing admin to view "statistics"-------------------------------------------------
        elif menu == 's' and username == 'admin':
            generate_reports()
            print(f"\n*********************************************************************************\n")
            with open("task_overview.txt", "r") as tasks:
                for lines in tasks:
                    print(lines)

            print(f"*********************************************************************************\n")
            with open("user_overview.txt", "r") as users:
                for lines in users:
                    print(lines)
        
    #--------------------------Adding new task---------------------------------------------------------------------
        elif menu == 'a':
            add_task()

    #--------------------------View all tasks----------------------------------------------------------------------
        elif menu == 'va':
            view_all()

    #--------------------------View my tasks------------------------------------------------------------------
        elif menu == 'vm':  
            view_mine()
            while True:
                choice = input("Enter the number of the task you would like to edit\nOR\nEnter '-1' to return to menu\n:")
                if choice == '-1':
                    break
                else:
                    task_number = choice
                    choice2 = input("Has the task been completed? 'Yes' or 'No':")
                    if choice2.lower() == "yes":
                        with open("tasks.txt", "r") as tasks:
                            lines = tasks.readlines()
                        if (int(task_number)) <= len(lines):
                            line = lines[(int(task_number)) - 1]
                            modified_line = line.replace("No", "Yes")
                            lines[(int(task_number)) - 1] = modified_line
                            with open("tasks.txt", 'w') as tasks:
                                tasks.writelines(lines)
                        break


                    else:
                        choice3 = input("1. Edit username\n2. Edit due date\n:")
                        if choice3 == '1':
                            new_username = input("Enter new username for task: ")
                            new_username = f"{new_username}, "
                            with open('tasks.txt', 'r') as tasks:
                                lines = tasks.readlines()
                                if 1 <= int(task_number) <= len(lines):
                                    lines[int(task_number) - 1] = new_username + lines[int(task_number) - 1].split(' ', 1)[1]
                                    with open('tasks.txt', 'w') as tasks:
                                        tasks.writelines(lines)
                        else:
                            new_duedate = input("Enter new due date e.g. '2023-05-16': ")
                            new_duedate = f"{new_duedate}"
                            with open('tasks.txt', 'r') as tasks:
                                lines = tasks.readlines()
                            if int(task_number) <= len(lines):
                                line = lines[int(task_number) - 1].strip().split(', ')
                                if len(line) >= 5:
                                    line[4] = new_duedate
                                    lines[int(task_number) - 1] = ', '.join(line) + '\n'
                            with open('tasks.txt', 'w') as tasks:
                                tasks.writelines(lines)
                            break
    
    #-------------------------Generate Reports--------------------------------------------------------------------
        elif menu == 'gr' and username == 'admin':
            generate_reports()

    #--------------------------Other task manager options----------------------------------------------------------
        elif menu == 'e':
            print('Goodbye!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

if __name__ == "__main__":
    main()