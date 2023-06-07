#=====importing libraries===========

# Import date class from datetime module

from datetime import date

#**************************************************Declaring functions********************************************************

#function for registering new user==========================================================================================

def reg_user():
    if user_name == "admin":
            check = 0
            user_check = 0         
            user_file = open("user.txt", "r")
            data = user_file.read()
            data = data.replace(",", "")
            data = data.replace("\n", " ")
            user_pass_list = data.split()
            while True:
                new_username = input("Enter user name for the new user:  ").lower()
                user_check = 0
                for index_count in range(len(user_pass_list)):
                    if new_username == user_pass_list[index_count]:
                        user_check += 1
                        user_pass_list[index_count]
                    index_count +=2
                if user_check == 0:
                    break
                else:
                    print("User name already exists. Please choose another name.")
            user_file.close()            
            while check == 0:          # check is 1 only when password matches with confirm password.
                new_password = input("Enter password for new username. Password is case sensitive: ")
                confirm_password = input("Confirm the password. Password is case sensitive: ")
                if new_password == confirm_password: 
                    user_file = open("user.txt", "a")                
                    user_file.write(f"\n{new_username.lower()}, {new_password}")
                    print('\x1b[7;32;47m')
                    print(f"You have successfully registered {new_username}")
                    print('\x1b[0m')
                    check +=1
                    user_file.close()           
                else:
                    print('\x1b[1;31;47m')
                    print("\nPassword and confirm password do not match. ")
                    print('\x1b[0m')                  
    else:
        print('\x1b[1;31;47m') # prints in red
        print("Only admin can register. Please select other options from the menu. \n")
        print('\x1b[0m')

#function for adding tasks=============================================================================================

def add_task():
    from datetime import date
    task_file = open("tasks.txt", "a")
    user_name = input("Enter username of the person whom the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    task_duedate = input("Enter the due date of the task in the format: dd name of month YYYY: " )
    today = date.today()
    date_today =  today.strftime("%d %B %Y")
    task_file.write(f"\n{user_name.lower()}, {task_title}, {task_description}, {date_today}, {task_duedate}, No") # ensures username is stored in lower case.
    task_file.close()
    print('\x1b[5;30;42m')  # prints in green
    print("You have successfully added task")
    print('\x1b[0m')  # stop printing  in green


#function for viewing all tasks==================================================================================================
def view_all():
    task_file = open("tasks.txt", "r")
    task_data = task_file.read()
    task_data = task_data.replace("\n", ", ")
    task_data_list = task_data.split(",")
    total_data =  (len(task_data_list)) 
    total_user = total_data / 6    # each user has 6 entries for them 
    total_user = int(total_user)
    index_count = 0
    for count in range (0, total_user):
            print('\x1b[1;34;47m')  # prints in blue on white background      
            print(f"\nTask:   \t\t{task_data_list[index_count+1]}\nAssigned to:    \t{task_data_list[index_count]}\nTask description:       {task_data_list[index_count+2]}")
            print(f"Date assigned:  \t{task_data_list[index_count+3]}\nDue date:\t\t{task_data_list[index_count+4]}\nTask completed: \t{task_data_list[index_count+5]}")
            index_count += 6  
            print('\x1b[0m')    # stops printing in blue
    task_file.close()

#function for viewing my tasks==================================================================================================
def view_mine():
    task_file = open("tasks.txt", "r")
    task_data = task_file.read()
    task_data = task_data.replace("\n", ", ")
    task_data_list = task_data.split(", ")
    total_data =  (len(task_data_list)) 
    total_user = total_data / 6
    total_user = int(total_user)
    print('\x1b[1;34;47m')       # prints in blue on white 
    print(u'\u2015' * 150)       # draws horizontal line
    index_count = 0   
    for count in range (0, total_user):          
        if task_data_list[index_count] == user_name:      
            print(f"\nTask No. {count +1}:   \t\t{task_data_list[index_count+1]}\nAssigned to:    \t{task_data_list[index_count]}\nTask description:       {task_data_list[index_count+2]}")
            print(f"Date assigned:  \t{task_data_list[index_count+3]}\nDue date:\t\t{task_data_list[index_count+4]}\nTask completed: \t{task_data_list[index_count+5]}")
        index_count += 6 
    print(u'\u2015' * 150)   # draws horizontal line  
    print('\x1b[0m')# stop printing in blue
    while True:
        choice = int(input("Please enter the task number you want to edit or enter -1 to return to the main menu: "))  
        if choice == -1:
            task_file.close()
            break
        else:
            completion_index = (6 * choice) - 1
            edit_choice = input('''Please select one of the following options below:   
y - mark the task as complete
e - edit a task
: ''').lower()
            if edit_choice == "y":
                task_data_list[completion_index] = "Yes"
                edited_task_file = open("tasks.txt", "w")
                c = 0
                for line_count in range (0, total_user):
                    edited_task_file.write(f"{task_data_list[c]}, {task_data_list[c + 1]}, {task_data_list[c + 2]}, {task_data_list[c + 3]}, {task_data_list[c + 4]}, {task_data_list[c + 5]}\n")
                    c += 6  
                edited_task_file.close()
            elif edit_choice == "e":
                if task_data_list[completion_index] == "Yes":
                    print("Task has been completed so cannot be edited")
                else:
                    what_to_edit = input('''Please select one of the following options below:   
u - edit username
d - edit completion date:
ud - edit both 
: ''').lower()
                    if what_to_edit == "u":
                        edited_user_name = input("Please enter the new user name for the task: ")
                        user_name_index = (choice - 1) * 6 
                        task_data_list[user_name_index] = edited_user_name
                        edited_task_file = open("tasks.txt", "w")
                        c = 0
                        for line_count in range (0, total_user):
                            edited_task_file.write(f"{task_data_list[c]}, {task_data_list[c + 1]}, {task_data_list[c + 2]}, {task_data_list[c + 3]}, {task_data_list[c + 4]}, {task_data_list[c + 5]}\n")
                            c += 6  
                        edited_task_file.close()
                    elif what_to_edit == "d":
                        edited_date = input("Please enter the new date for completion in dd first three letters of month YYYY format : ")
                        date_index = (choice - 1) * 6 + 4                      
                        task_data_list[date_index] = edited_date
                        edited_task_file = open("tasks.txt", "w")
                        c = 0
                        for line_count in range (0, total_user):
                            edited_task_file.write(f"{task_data_list[c]}, {task_data_list[c + 1]}, {task_data_list[c + 2]}, {task_data_list[c + 3]}, {task_data_list[c + 4]}, {task_data_list[c + 5]}\n")
                            c += 6  
                        edited_task_file.close()
                    elif what_to_edit == "ud":
                        edited_user_name = input("Please enter the new user name for the task: ")
                        user_name_index = (choice - 1) * 6
                        task_data_list[user_name_index] = edited_user_name
                        edited_date = input("Please enter the new date for completion in dd first three letters of month YYYY format : ")
                        date_index = (choice - 1) * 6 + 4                      
                        task_data_list[date_index] = edited_date                        
                        edited_task_file = open("tasks.txt", "w")
                        c = 0
                        for line_count in range (0, total_user):
                            edited_task_file.write(f"{task_data_list[c]}, {task_data_list[c + 1]}, {task_data_list[c + 2]}, {task_data_list[c + 3]}, {task_data_list[c + 4]}, {task_data_list[c + 5]}\n")
                            c += 6  
                        edited_task_file.close()   

#function for generating reports:
def gen_report():
    #codes for creating 'task_overview.txt'
    print('\x1b[1;34;47m')       # prints in blue on white 
    print(u'\u2015' * 150)       # draws horizontal line
    from datetime import datetime
    today = datetime.today()
    date_today =  today.strftime("%d %B %Y")                
    task_file = open("tasks.txt", "r")
    task_data = task_file.read()
    task_data = task_data.replace("\n", ", ")
    task_data_list = task_data.split(", ")
    total_data =  (len(task_data_list)) 
    tasks_num = total_data / 6
    tasks_num = int(tasks_num)
    task_file.close()
    index_count = 0  
    com_task_count = 0
    due_task_count = 0      
    date_format = "%d %B %Y" 
    for count in range (0, tasks_num):          
        if task_data_list[index_count + 5] == "Yes":
            com_task_count += 1
        if task_data_list[index_count + 5] == "No":
            due_date = task_data_list[index_count + 4]
            obj_due_date = datetime.strptime(due_date, date_format)                
            if today > obj_due_date :
                due_task_count += 1 
        index_count +=6           
    inc_task_count = tasks_num - com_task_count
    per_comp_task = (inc_task_count / tasks_num) * 100
    per_due_task = (due_task_count/tasks_num) * 100
    file_tasks_report = open("task_overview.txt", "w+" )
    file_tasks_report.write(f"\nTotal number of tasks are:                                {tasks_num}") 
    file_tasks_report.write(f"\nTotal number of completed tasks are:                      {com_task_count}")
    file_tasks_report.write(f"\nTotal number of incomplete tasks are:                     {inc_task_count}")
    file_tasks_report.write(f"\nTotal number of tasks that are incomplete and overdue :   {due_task_count}")       
    file_tasks_report.write(f"\nThe percentage of tasks that are incomplete:              {per_comp_task}%")
    file_tasks_report.write(f"\nThe percentage of tasks that are incomplete and overdue:  {per_due_task}%")
    file_tasks_report.close()
    file_tasks_report = open("task_overview.txt", "r+" )
    report = file_tasks_report.read()
    print(report)
    print(u'\u2015' * 150)       # draws horizontal line
    file_tasks_report.close()
        
    #========codes for creating 'user_overview.txt'
    print(u'\u2015' * 150)                       
    user_file = open("user.txt", "r")
    data = user_file.read()
    data = data.replace(",", "")
    data = data.replace("\n", " ")
    user_pass_list = data.split()
    user_num = len(user_pass_list) / 2
    file_user_report = open("user_overview.txt", "w+")
    file_user_report.write(f"Total number of users are:      {int(user_num)}")
    file_user_report.write(f"\nTotal number of tasks are:      {tasks_num}\n") 
    username_list = []
    for i in range(0, len(user_pass_list)):
        if i % 2 == 0:
            username_list.append(user_pass_list[i])
    task_index = 0
    user_index = 0
    for username in username_list:
        task_total = 0
        task_index = 0
        comp_task = 0
        overdue_task_count = 0
        for counter_2 in range (0, tasks_num):                
            if task_data_list[task_index] == username:
                task_total += 1
                if task_data_list[task_index + 5] == "Yes":
                    comp_task += 1
                elif task_data_list[task_index + 5] == "No":
                    date_due = task_data_list[task_index + 4]
                    obj_date_due = datetime.strptime(date_due, date_format)                
                    if today > obj_date_due :
                        overdue_task_count += 1
            task_index +=6               
        incom_task = task_total - comp_task
        perc_total_task = (task_total / tasks_num) * 100            
        if task_total > 0:
            perc_comp_task = (comp_task / task_total) * 100
        else:
            perc_comp_task = 0           
        perc_task_to_comp = 100 - perc_comp_task
        if incom_task > 0:
            perc_overdue_task = (overdue_task_count/incom_task) * 100
        else:
            perc_overdue_task = 0            
        file_user_report.write(f"\nReport for:   {username}")
        file_user_report.write(f"\nTotal number of tasks assigned  :                                                     {task_total}")
        file_user_report.write(f"\nThe percentage of the total number of tasks assigned:                                 {perc_total_task}%") 
        file_user_report.write(f"\nThe percentage of the tasks assigned that have been completed:                        {perc_comp_task}%") 
        file_user_report.write(f"\nThe percentage of the tasks assigned that must still be completed:                    {perc_task_to_comp}%") 
        file_user_report.write(f"\nThe percentage of the tasks assigned that must still be completed and are overdue:    {perc_overdue_task}%\n")
    user_file.close()
    file_user_report.close()
    file_user_report = open("user_overview.txt", "r+", encoding='utf-8')
    user_report = file_user_report.read()
    print(f"\n{user_report}")        
    file_user_report.close() 
    print('\x1b[0m')
        
#function for displaying statistics: ==================================================================================================
def dis_statistics():
    user_file = open("user.txt", "r")
    data = user_file.read()
    data = data.replace(",", "")
    data = data.replace("\n", " ")
    user_pass_list = data.split()
    user_num = len(user_pass_list) / 2 
    print('\x1b[1;34;47m')       # prints in blue
    print(f"Total number of users are:      {int(user_num)}")
    user_file.close()
    task_file = open("tasks.txt", "r")
    task_data = task_file.read()
    task_data = task_data.replace("\n", ", ")
    task_data_list = task_data.split(", ")
    total_data =  (len(task_data_list)) 
    tasks_num = total_data / 6
    tasks_num = int(tasks_num)
    task_file.close()   
    print(f"\nTotal number of tasks are:      {tasks_num}")
    print('\x1b[0m')
    
#============================Login Section=====================================================================================================

user_file = open("user.txt", "r")
data = user_file.read()
data = data.replace(",", "")
data = data.replace("\n", " ")
user_pass_list = data.split()
check = 0              # check is 1 when both username and password are correct
while check == 0:
    valid_username = 0    
    user_name = input("Enter user name: ").lower()  # all the username are stored in lower case in the user file.
    user_password = input("Enter password. Password is case sensitive: ")
    print("\n")
    for index_count in range (0, len(user_pass_list)):     
        if user_name == user_pass_list[index_count] and user_password == user_pass_list[index_count + 1]:
            check += 1                                         
        index_count += 2
    for name in user_pass_list:
        if name == user_name:
            valid_username = 1         
    if check == 1:
        print('\x1b[5;30;42m')   # prints in green
        print ("You have successfully login")
        print('\x1b[0m')         # stops printing in green
    elif valid_username == 1:     
        print('\x1b[1;31;47m' + "You have entered wrong password. Please enter username and password again.")  # prints in red
        print('\x1b[0m')         # stops printing in red     
    else:
        print('\x1b[1;31;47m' + "The user name you have entered does not exist. Please enter username and password again.\n")
        print('\x1b[0m')        # stops printing in red.
              
user_file.close()

# presenting menu to the user and making sure input is lower case

while True:    
    print('\x1b[1;37;44m')      # prints menu on a white background in blue font.
    if user_name == "admin":
        menu = input('''Please select one of the following options below:   
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds  - dispaly statistics
gr - generate reports
e - Exit
: ''').lower()         
    else:        
        menu = input('''Select one of the following Options below:    
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()     
    print('\x1b[0m')

    #===========codes for calling function- reg_user for registering new user        
    if menu == 'r':
        reg_user()
         
    #=========== codes for calling function- add_task for adding tasks.      
    elif menu == 'a':  
        add_task()        
           
    #=========== codes for calling function- view_all for  displaying the tasks of all the employees
    elif menu == 'va': 
        view_all()       

    #=========== This part of program displays the tasks of the user who has logged in                       
    elif menu == 'vm':
        view_mine()

    #============ This block of codes calls function to generate reports 
    elif menu == 'gr':
        gen_report()
        
             
    #============ This block of codes calls function to dispaly the statistics of all the tasks
    elif menu == 'ds':
        dis_statistics() 

    #============ This block of codes exits the menu      
    elif menu == 'e':   
        print('Goodbye!!!')
        exit()

    #=========== This block of codes asks the user to choose right option from the menu
    else:
        print("You have made a wrong choice, Please Try again")

tasks_file = open("tasks.txt", "r")
data_tasks_lines = tasks_file.readlines()
tasks_num = 0        
for lines in data_tasks_lines: 
    tasks_num += 1
print(tasks_num)
tasks_file.close       

    

            


        
    