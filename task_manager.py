#Phase 1: Importation and Opening.
import datetime
date = datetime.datetime.today()
u = open('user.txt', 'r')



#Phase 2: Identification.
#Here i will ask the user to input their username and password then store them as name adn password.
name = input("Please enter your Username: ")
password = input("Please enter your Password: ")
#I make the user variable a combination of name and password to match the actaul line in the txt file.
user = name + ", " + password
#I make a boolean validU and set it as False for later.
validU = False #validU stands for valid user.



#Phase 3: Functions.
#Here i will be defining all my functions for this task.
def admin_menu():#I define the admin_menu function with no parameter.
#This function is the menu for the admin.
#This function displays the menu for the admin and allows them to navigate to the menu option they select.

    option = input("Please select one of the following options:\nr - register user\na - " +
                       "add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\n" +
                       "s - statistics\ne - exit\nselection: ")

    if option == "r": #If option r is selected the admin will be allowed to register a new user.
            
        reg_user() #I call the reg_user function.

    elif option == "a": #This option will add a new task and can be done by all users.
                
        add_task() #I call the add_task function.

    elif option == "va": #This option will display all tasks in the tasks.txt file.

        view_all() #I call the view_all function

    elif option == "vm": #This option will show the tasks for the user logged in and allow them to edit and/or mark as completed.

        view_mine()#I call the view_mine function

    elif option == "gr":

        generate_report()#I call the generate_report function

    elif option == "s": #The admin will be aloowed to check the statistics of files.
            
        statistics()#I call the statistics function.

    elif option == "e": #This option exits the program.

        print("Program has ended.") #Let the user know the program has ended.


def user_menu():#I define the function user_menu with no parameter.
#This function is the menu for the user that isn't admin.
#This function displays the menu to the user and allows them to navigate to the option they want.

    option = input("Please select one of the following options:\nr - register user\na - " +
                "add task\nva - view all tasks\nvm - view my tasks\ne - exit\nselection: ")#This is the menu for non admin users.

    if option == "r": #Only admins can register new users so this option doesn't have any further steps.
                
        print("Only admin may register a new user.") #Let the user know that only admins can register new users.

    elif option == "a": #This is basically the same as the above options for admin>
                
        add_task()

    elif option == "va": 

        view_all()

    elif option == "vm":

        view_mine()

    elif option == "e":

        print("Program has ended.")


def reg_user():#I define the reg_user function with no parameters.
#This function will be called when the user wants to register a new user.
#This function is responsible for registering a new user.
    
    u = open('user.txt', 'r')#I open the user file in read mode.
    newUser = input("Please enter the new username: ") #I ask the user to enter the new username.

    userCheck = False #I make userCheck False for my while loop that should only loop if userCheck is true.
    
    if newUser in u.read(): #If the new user is in the user file.

        userCheck = True

        while userCheck == True: #I use a while loop so that if the next entry is invalid it will loop again.

            u = open('user.txt', 'r') #I open the user file in read mode.
            #I print an error message to explain to the user that you can't register two of the same user.
            print("You have entered a username that already exists. You cannot register the same user twice. PLease try again.")
            newUser = input("Please enter the new username: ")#I ask again for the users new username.

            #These if and else statements is for the sake of restarting or ending the loop.
            if newUser in u.read(): #Restarts loop.

                userCheck = True

            else: #Ends loop

                userCheck = False

            u.close() #I close the user file.
    
    newPassword = input("Please enter the new password: ")
    confirm = input("Please confirm the new password: ") #The new pasword and must be the same as the confirmed password for it to be saved.
    
    while newPassword != confirm: #When the new and confirmed password are not the same the user will be asked to retry.
        
        print("You have entered two different passwords. Please enter the new password and then confirm it.")
        newPassword = input("Please enter the new password: ")
        confirm = input("Please confirm the new password: ")
                
    if newPassword == confirm: #When the passwords are the same it will be written in the txt file along with the username.
        
        output = newUser + ", " + confirm #I combine the new username and password in the correct format.
        u = open('user.txt', 'a') #open the text file in append mode so that i add to the existing text.
        u.write("\n" + output) #I put "\n" so that the new username and password will be written on a new line.
        u.close() #close the file when complete.
        print("New user has been registered.") #To let the user know that they have succesfully registered a new user.
        u.close()


def add_task():#I define the add_task function with no parameters.
#This function will be called if the user wishes to add a task to the tasks file.
#This function is responsible for adding the new task to the tasks file.

    taskFor = input("Please enter the username of the person the task is assigned to: ") #Who the task is for.
    taskTitle = input("Please enter the title of the task: ") #Title of the task.
    taskDescrp = input("Please enter a description of the task: ") #Task description.
    dueDate = input("Please enter the due date of the task: ") #due date for the task.
    t = open('tasks.txt', 'a') #Open the text file in append mode to add to the existing text.
    t.write("\n" + taskFor + ", " + taskTitle + ", " + taskDescrp +
            ", " + str(date.day) + " " + str(date.strftime("%b")) + " " +
            str(date.year) + ", " + dueDate + ", "
            + "No") #Written in the same format as the other tasks and automatically no for not complete.
    t.close() #close file when complete.
    print("New task has been added.") #To let the user know that they have successfully added a new task.
    

def view_all():#I define the view_all function with no parameters
#This function will be called when the user selects to view all tasks.
#This function displays all the tasks in the task file.

    t = open('tasks.txt', 'r') #Open tasks.txt in read mode.
    tasks = t.read()#storing the lines of the file in tasks.
    tasks = tasks.replace('\n', '\n\n')#replacing the next lines with two instead so its user friendly.
    tasks = tasks.replace(',', '\n') #replacing the , with \n so that the displayed information is easy to read.
    print(tasks) #Print the tasks for all users.
    t.close() #close file when complete.


def view_mine():#I define the view_mine function with no parameters.
#This function will be called when the user selects to view their tasks.
#This function will view the tasks for the user and will allow the user to edit it or mark as complete.

    username = user.split(', ')[0] #This is that the only the username is read and not both username and password.
    with open('tasks.txt', 'r') as t: #open tasks file in read mode.
        print("\n")#I add a blank line so that things are presented in an easy to read fashion.
        correspNum = 0 #I start a corresponding number count for the task IDs.
        for line in t: #I start a loop to read through the lines in the tasks file.

            correspNum += 1#Each time a line is read the counter increases.

            if line.startswith(user): #This is so we only get the line that belongs to the specific user.

                print("Task ID: " + str(correspNum) + "\n" + line.replace(', ', '\n')) #print the line with ' replaced by \n so that its easy to read.

        #I now ask the user what they would like to do next.    
        optionNum = int(input("\nEnter the Task ID of the task you would like to select or enter '-1' to return to menu: "))

        if optionNum == -1 and user == "admin": #If the user wants to go back to menu and its the admin they will be returned to that menu.

                admin_menu()#I call the admin menu function.

        elif optionNum == -1 and user != "admin": #If the user is not admin they will be taken to the user menu.

                user_menu()#I call the user menu function.

        elif optionNum <= (correspNum):#if the option is less than the correspNum then it is a valid choice.

            with open('tasks.txt', 'r') as t:#I open the tasks file in read mode.

                count = 0 #I start the count at 0.
                    
                for line in t: #I read through the lines in the tasks file.

                    count += 1 #I increase the count by 1.

                    if count == optionNum:#This loop basically loops until the right task is found.
                                                
                        selectedTask = line.split(', ')#I store the line as a list in the variable selectedTask.
                        print("\nYou have selected: " + str(selectedTask)) #I show the user what task they have selected.
                        option = input("\nWould you like to mark as complete or edit the task?\n" +
                                        "Simply enter 'mark' or 'edit': ") #I ask the user what they would like to do.
                
                        if option == 'mark':#If they choose to mark the task as complete.
                            
                            selectedTask[-1] = 'Yes\n' #I change the last item( [-1] ) to yes. this indicates its complete.
                            selectedTask = ", ".join(selectedTask) #I use .join() to convert the list to string.
                            
                            t = open('tasks.txt', 'r') #I open the tasks file in read mode.
                            lines = t.readlines() #I store the lines from the tasks file in the lines variable.
                            lines[optionNum - 1] = selectedTask #I add selectedTask to the line it belongs in.
                            t.close() #I close the tasks file.
                            t = open('tasks.txt', 'w') #I opne the tasks file in write mode.
                            t.writelines(lines) #I write lines in the tasks file.
                            t.close() #I close the tasks file.
                            print("\nThe selected task has been marked as complete.") #I tell the user the action has been completed.
                            
                        elif option == 'edit': #If they choose to edit the task.

                            if selectedTask[-1] == 'No' or selectedTask[-1] == 'No\n':#This is so that already complete tasks can't be edited.

                                userChange = input("\nIf you would like to enter a new user for this task enter the new username.\n" +
                                                   "If you would like to keep the same user, enter 'same': ")#I ask the user if they would change the assignment.

                                if userChange == "same":#If same then the user won't change.

                                    dueDChange = input("\nIf you would like to change the due date of this task enter the new due date.\n" +
                                                       "If you would like to keep the same due date, enter 'same': ")#I ask the user if they would like to chnage the due date.

                                    if dueDChange == "same": #If same nothing will change.
                                        
                                        #This is so the user is taken back to the menu.
                                        if user == "admin":

                                            admin_menu()

                                        elif user != "admin":

                                            user_menu()

                                    elif dueDChange != "same":#If not same then the due date will be changed to the input.

                                        selectedTaskDEdit = selectTask #This is to edit the selected task.
                                        selectedTaskDEdit[4] = dueDChange #change the due date in the list to the input.
                                        selectedDEditTask = ", ".join(selectedTaskDEdit)#Make the list into a string
                                        t = open('tasks.txt', 'r')#I open the tasks file in read mode.
                                        lines = t.readlines() #I add all the lines to the lines variable.
                                        lines[optionNum - 1] = selectedTaskDEdit #I add the new due date.
                                        t.close()#close the tasks file.
                                        t = open('tasks.txt', 'w') #open the tasks file in write mode.
                                        t.writelines(lines)#write lines into the tasks file.
                                        t.close()#close the tasks file.
                                        print("\nThe change has been made.")#I let the user know the chnages have been made.
                                        

                                elif userChange != "same":#This is basically the same as the due dates change.

                                    selectedTaskUEdit = selectedTask
                                    selectedTaskUEdit[0] = userChange
                                    selectedTaskUEdit = ", ".join(selectedTaskUEdit)
                                    t = open('tasks.txt', 'r')
                                    lines = t.readlines()
                                    lines[optionNum - 1] = selectedTaskUEdit
                                    t.close()
                                    t = open('tasks.txt', 'w')
                                    t.writelines(lines)
                                    t.close()
                                    print("\nThe change has been made.")
                                    dueDChange = input("\nIf you would like to change the due date of this task enter the new due date.\n" +
                                                       "If you would like to keep the same due date, enter 'same': ")

                                    if dueDChange == "same":

                                        if user == "admin":

                                            admin_menu()

                                        elif user != "admin":

                                            user_menu()

                                    elif dueDChange != "same":

                                        selectedTaskDEdit = selectedTask
                                        selectedTaskDEdit[4] = dueDChange
                                        selectedTaskDEdit = ", ".join(selectedTaskDEdit)
                                        t = open('tasks.txt', 'r')
                                        lines = t.readlines()
                                        lines[optionNum - 1] = selectedTaskDEdit
                                        t.close()
                                        t = open('tasks.txt', 'w')
                                        t.writelines(lines)
                                        t.close()
                                        print("\nThe change have been made.")

                                        if user == "admin":

                                            admin_menu()

                                        elif user != "admin":

                                            user_menu()

                            else:#If the task is already completed.

                                print("This task has already been completed and therefore cannot be editted.")

                                if user == "admin":

                                    admin_menu()

                                elif user != "admin":

                                    user_menu()

        else: #If the optionNum isn't valid.

            print("You have not selected a valid option. Please try again.")
            view_mine()


def generate_report():#I define the generate_report function with no parameters.
#This function will be called when the user selects to generate report.
#This function call the task and user overview functions to generate reports and write them in text files.

    to = task_overview()#I call the task_overview function.
    uo = user_overview()#I call the user_overview function.
    statistics = f"\nNumber of users - {uo}\nNumber of tasks - {to}\n" #I store this string in statistics so when statistcs is called and therefore this function,
                                                                       #It prints the statistics. 
    return statistics #I return the statistics variable.


def task_overview():#I define the task_overview function with no parameters.
#This function will be called when the user chooses to generate reports.
#This function generates reports of the tasks and writes it into a text file.

    to = open('task_overview.txt', 'w')#I open the tasks_overview file in write mode.
    t = open('tasks.txt', 'r') #Open the tasks file in read mode.
    
    tasks = [] #I make an empty list and store it in the tasks variable.
    
    for line in t: #I loop through the lines in the tasks file.

        line = line.split(', ')#I make the lines into a list.
        tasks += line #I add the line list to the tasks list.
        
    t.close() #I close the tasks file.
    
    t = open('tasks.txt', 'r') #I opne the tasks file in read mode.
    
    numTasks = len(t.readlines())#I check the length of the tasks file to see how many tasks there are.
    
    completed = tasks.count('Yes\n')#I count the amount of yes's to check how many complete tasks there are.
    
    uncompleted = tasks.count('No\n')#I count the amount of no's to check how many incomplete tasks there are.
    
    t.close()#I close the tasks file.

    t = open('tasks.txt', 'r')#I open the tasks in read mode.
    
    dueDates = []#I make an empty list in the dueDates variable.
    today = datetime.datetime.today()#I store todays date and time in the today variable.
    
    for line in t:#I read through the lines in the tasks file.

        if 'No\n' in line:#For the lines that contain no (Incomplete tasks).

            line = line.split(', ')#I add the line in list form to the line variable.
            dueDates += line[4:5]#I slice the list so that only the due dates are stored in the dueDates variable.

    overdueCount = 0 #I start the overdueCount at 0.
    
    for line in dueDates:#I loop through the lines in dueDates.

        if datetime.datetime.strptime(line, "%d %B %Y") < today:#If the due date is greater than the current date.

            overdueCount += 1#I increase the count by 1.

    t.close()#I close the tasks file.
    
    percentUncomplete = round((uncompleted * 100) / numTasks, 2) #I work out the percent of tasks that are complete.
    percentOverdue = round((overdueCount * 100) / numTasks, 2)#I work out the percent that aren't complete and overdue.

    #I write all the reports in the task_overview file.
    to.write(f"Total number of tasks: {numTasks}\n") 
    to.write(f"Total number of completed tasks: {completed}\n")
    to.write(f"Total number of uncompleted tasks: {uncompleted}\n")
    to.write(f"Total number of overdue uncompleted tasks: {overdueCount}\n")
    to.write(f"Percentage of tasks that are incomplete: {percentUncomplete}%\n")
    to.write(f"Percentage of tasks that are overdue: {percentOverdue}%\n")
    
    to.close()#I close the task_overview file.
    return numTasks #I return the numTasks variable.


def user_overview():
#This function will be called when the generate reports option is selected.
#This function will generate reports for the users.

    uo = open('user_overview.txt', 'w')#I open the user_overview file in the write mode.
    
    u = open('user.txt', 'r') #Open the user file in read mode.
    
    numUsers = len(u.readlines())#I readlines in the user file and check the length to see how many users there are.
    
    u.close()#I close the user file.
    
    t = open('tasks.txt', 'r')#I open the tasks file in read mode.
    
    numTasks = len(t.readlines()) #I readlines in the tasks file and check the length to see how many tasks there are.
    
    t.close()#I close the tasks file.
    
    uo.write(f"Total number of users: {numUsers}\n")#I write the amount of users in the user._overview file.
    uo.write(f"Total number of tasks: {numTasks}\n")#I do the same for tasks
    
    u = open('user.txt', 'r') #I open the user file in read mode.
    
    dueDates = [] #I make an empty list and store it in the dueDates variable.
    today = datetime.datetime.today() #I store the current date in the today module.
    
    for line in u:#I loop through in lines in the user file.

        userTasks = []#I make an empty list and store it in the userTasks variable.
        count = 0 #I start the count at 0.
        user = line.split(', ')[0] #I split the line and store the 0 index item in the variable user.
        uo.write("\n" + line.split(', ')[0] + ":\n\n") #I write the user in the user_overview file as a header.
        
        with open('tasks.txt', 'r') as t:#I open the tasks file in read mode as t.

            for line in t:#I loop through lines in the tasks file.
                    
                if line.startswith(user):#I indentify the tasks for the user.
                                
                    count += 1 #I increase the ocunt by 1.
                    lines = line.split(', ') #I make the task into a list and store it in the lines variable.
                    userTasks += lines #I store the lines list in the userTasks list.
                    
                    if 'No\n' in line: #If the task is not complete.

                        line = line.split(', ') #I make the task into a list.
                        dueDates += line[4:5] #I slice the list and store the due dates in the dueDates variable.

                overdueCount = 0 #I start the overdueCount at 0.
                
                for line in dueDates:#I loop through the items in the dueDates list.

                    if datetime.datetime.strptime(line, "%d %B %Y") < today: #If the due date is greater than the current date.

                        overdueCount += 1 #I increase the overdueCount by 1.

            #I do my calculations for percentages.
            #I write all the reports in the user_overview file.
            uo.write(f"Amount of tasks assigned - {count}\n")
            
            perTasksAssigned = round((count * 100) / numTasks, 2)#I round the calculation to two so its easy to read.
            uo.write(f"Percentage of tasks assigned - {perTasksAssigned}%\n")
            
            userCompleted = userTasks.count('Yes\n')
            percCompleted = round((userCompleted *100) / count, 2)
            uo.write(f"Completed tasks - {percCompleted}%\n")
            
            perUncompleted = round(((count - userCompleted) * 100) / count, 2)
            uo.write(f"Incomplete tasks - {perUncompleted}%\n")
            
            percentOverdue = round((overdueCount * 100) / count, 2)
            uo.write(f"Percentage of incomplete tasks past thier due dates - {percentOverdue}%\n")
                    
    u.close()#I close the user file.

    return numUsers #I return the numUsers variable.
    

def statistics(): #I define the statistics function with no parameters.
#This function will be called when the admin selects the statistics option in the menu.
#This function simply print the number of users and tasks in an easy to read fashion.

    print(generate_report())#I call the generate report function and print the return.



#Phase 4: While Loop.
#If the users username and password are valid it will change the validU to true.
if user in u.read(): #This if statement means that if the user is found in user.txt.

    validU = True

#While validU is False they will be asked to enter a valid username or password until a valid username is entered.
while validU == False:
    
    u = open('user.txt', 'r')
    print("You have not entered a valid username or password!")
    name = input("Please enter a valid Username: ")
    password = input("Please enter a valid Password: ")
    user = name + ", " + password
    
    if user in u.read(): #If they enter a valid username and password then validU will become True and they'll move to the next part of the program.
        
        validU = True
        
    else:
        
        validU = False #validU will remain false basically until the username and password is in the list of valid users.



#Phase 5.1: Admin Menu.
#If the validU is true then the user will be able to proceed to the menu.
if validU == True:
    
    user = user.split(', ')[0]#I split the username from the password to identify the username becuase different users get different menus.
    
    if user == "admin": #If the user is admin they will get a specific menu.

        admin_menu()


            
#Phase 5.2: User Menu.
#The options in this phase are the same as the admins options but without a few.
    else:#This if for users without ther username admin.

        user_menu()

#=================================================================END OF CODE====================================================================================
