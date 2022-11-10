import class_functions as cf
import datetime as dt
import csv

def main():    
    calendar_start_date = "2022-12-31" # Tool can schedule jobs from 31st Dec 2022 onwards only
    calendar_end_date = "2042-12-31" #Tool will not be able to schedule any jobs past this date
    list_of_employees = [] #Does not take into account new additions or removal, to look up the relevant employee list for those
    list_of_new_employees = [] #Holds all new hires scheduled to join in the Tool
    list_of_leaving_employees = []  #Holds all planned attrition in the Tool
    list_of_jobs = [] #Holds all scheduled jobs accepted by the Tool
    calendar_resource_dict = {} #This data structure will store the daily resource available by date as key
    job_id = 1000 #initialises first job id to 1000
    job_database_initialised_count = 0 #To prevent job database from initialising twice
    file_generation_count = 0 #Used to create different named .csv files for data persistence


    print("-" * 95)
    print("\nFLEXI-INTELLIGENT RESOURCE AND SCHEDULING TOOL (FIRST) ** BETWEEN {} AND {} **\n".format(calendar_start_date, calendar_end_date))
    print("-" * 95)


    while True: #Purpose of this while loop is to keep the programme running after the first selection is fully completed (i.e Option 1 or 2 or 3 or 4 is fully completed)
        
        #INPUT DATA VALIDATION
        user_option = input("\nPlease input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees or Delete Scheduled Job ""\n"" 3 : Schedule a Job ""\n"" 4 : Downloading data to .csv files / Cost summary \nInput (1), (2), (3) or (4): ")
        try:
            if user_option not in ["1", "2", "3", "4"]:
                raise ValueError
            else:
                pass
        except ValueError:
            while True:
                user_option_reselect = input("\nERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
                if user_option_reselect == "y":
                    user_option= input("\nPlease input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees or Delete Scheduled Job ""\n"" 3 : Schedule a Job ""\n"" 4 : Downloading data to .csv files / Cost summary \nInput (1), (2), (3) or (4): ")
                    try:
                        if user_option not in ["1", "2", "3", "4"]:
                            raise ValueError
                        else:                            
                            break
                    except ValueError:
                        pass
                elif user_option_reselect == "n":
                    break
                else:
                    pass

        #END OF INPUT DATA VALIDATION


        #OPTION 1 SELECTED
        if user_option == "1": #Upload Employee/Job Database from .csv file format only (Note: Option 1-1 must always be run first to initialise the Resource Calendar (calendar data structure))
            while True:
                user_option_1 = input("\nWhich database do you want to upload - \n1 : Employee database \n2 : Job database \nInput (1) or (2): ")
                
                #INPUT DATA VALIDATION
                try:
                    if user_option_1 not in ["1", "2"]:
                        raise ValueError
                    else:
                        if user_option_1 == "1": 
                            #CREATE FILE OBJECT AND READ .CSV FILE
                            try:
                                with open("employee.csv", "r", encoding="utf-8") as file:
                                    employee_attributes = []
                                    employee_data = []
                                    for line in file:
                                        employee_data.append(line.strip().split(","))
                                    employee_attributes = employee_data.pop(0)
                                    
                                    
                                    if len(employee_attributes) != 7: #checks that the .csv file has seven columns for instantiation of employee class type
                                        print("\nERROR: Data from .csv file does not match expected input of seven employee attributes, please try again""\n""")
                                        continue
                                    else:
                                        for items in employee_data: # this creates the employee objects and assumes that the .csv file has the same columns in the right order (refer to employee class __init__ ordering)
                                            list_of_employees.append(cf.employee(items[0], items[1], items[2],items[3], items[4], items[5], items[6]))

                                        #CALLING createCalendarRange() FUNCTION TO INITIALISE CALENDAR DATA STRUCTURE
                                        cf.createCalendarRange(calendar_start_date, calendar_end_date, calendar_resource_dict, list_of_employees) #Resource Tool only works based on the Date range of calendar_start date to calendar_end_date
                                        
                                        break
                            except IOError:
                                print("\nERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical employee attributes are in correct form ""\n""Pls try again""\n""")
                                continue   

                        
                        
                        
                        elif user_option_1 == "2": 
                            
                            if job_database_initialised_count == 0: #Only allows the job.csv file to be loaded once
                                
                                
                                #CREATE FILE OBJECT AND READ .CSV FILE
                                try:
                                    with open("job.csv", "r", encoding="utf-8") as file:
                                        job_attributes = []
                                        job_data = []
                                        for line in file:
                                            job_data.append(line.strip().split(","))
                                        job_attributes = job_data.pop(0)
                                        
                                        
                                        if len(job_attributes) != 6:
                                            print("\nERROR: Data from .csv file does not match expected input of six job attributes, please try again""\n""")
                                            continue
                                        else:   

                                            if calendar_resource_dict == {}:
                                                print("\n** Please initialise Resource Tool with Employees as a first step before adding scheduled jobs **""\n""")
                                                break
                                            
                                            for items in job_data: # this creates the job objects and assumes that the .csv file has the same columns in the right order (refer to job class __init__ ordering)
                                                
                                                #Try-Except block not needed as data in .csv is assumed to be recorded accurately

                                                items[1] = dt.datetime.strptime(items[1], '%d/%m/%Y')
                                                items[2] = dt.datetime.strptime(items[2], '%d/%m/%Y')
                                                items[3] = float(items[3])
                                                items[4] = float(items[4])
                                                if items[1] < dt.datetime.strptime(calendar_start_date,'%Y-%m-%d'):
                                                    print("Scheduled job starts before Job Scheduling Tool start date of {}, please try again""\n""".format(calendar_start_date))
                                                    break
                                                
                                                
                                                #SCHEDULE JOBS IN THE .CSV FILE INTO THE RESOURCE TOOL
                                                cf.scheduleJob(items[0], items[1], items[2],items[3], items[4], items[5], calendar_resource_dict, job_id, list_of_jobs)
                                                job_id += 1 #Creates incremental numeric Job ID

                                            job_database_initialised_count = 1 #So that the job database will not be initialised twice   
                                            
                                            break                                      


                                except IOError:
                                    print("\nERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical/Date type job attributes are in correct form ""\n""Pls try again""\n""")
                                    continue                                

                            else:
                                print("\nERROR: Job Database have already been initialised""\n""") 
                                break

                except ValueError:
                    while True:
                        user_option_reselect = input("\nERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
                        if user_option_reselect == "y":
                            break
                        elif user_option_reselect == "n":
                            break
                        else:
                            pass
                if user_option_reselect == "y":
                    continue
                elif user_option_reselect == "n":        
                    break
                
                    
                    

            



        #OPTION 2 SELECTED
        elif user_option == "2": #Add/Remove Employee(s)/Delete Scheduled Job
            user_option_2 = input("\nDo you want to:""\n""1 : Add an employee to database ""\n""2 : Remove an employee from database ""\n""3 : Delete a Scheduled Job \nInput (1), (2) or (3): ")
            if user_option_2 not in ["1", "2", "3"]:
                print("\nERROR: You have entered an invalid selection, Please try again")
                

            else:
                
                if user_option_2 == "1": #Add Employee

                    if calendar_resource_dict == {}:
                        print("\n** Please initialise the Resource Tool first **\n")

                    else:
                        employee_input_cleaned = False
                        while True:
                            employee_details = input("\nPlease provide the following details (separated by commas) - \nEmployee ID, \nFirst Name, \nLast Name, \nHourly Rate, \nTotal Hours Per Day, \nCompetency, \nCraft, \nEmployee Start Date (yyyy-mm-dd) \nInput: ").strip().split(",")
                            if len(employee_details) != 8:
                                print("\nERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                                user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                                while True:
                                    if user_option_reselect in ["y", "n"]:
                                        break
                                    else:
                                        user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break

                            else:
                                for i in range(len(employee_details)):
                                    employee_details[i] = employee_details[i].strip()

                                #DATA VALIDITY CHECKS
                                if employee_details[6].lower() not in ["metals", "machinery", "instrument/electrical"]:
                                    print("\nERROR: You have entered an invalid employee craft, Please ensure that crafts are one of these: Metals, Machinery or Instrument/Electrical")
                                    user_option_reselect= input("\nDo you want to re-input? Y/N""\n""").lower()
                                    while True:
                                        if user_option_reselect in ["y", "n"]:
                                            break
                                        else:
                                            user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                            continue
                                    if user_option_reselect == "y":
                                        continue
                                    else:
                                        break
                                try:
                                    employee_details[0] = int(employee_details[0]) #Employee ID variation is allowable due to possible difference in employee type (such as contractor vs full-time), however, has to be integer form
                                    employee_details[3] = float(employee_details[3])
                                    employee_details[4] = float(employee_details[4])
                                    employee_details[5] = float(employee_details[5])
                                    if employee_details[3] < 0 or employee_details[4] < 0 or employee_details[5] < 0:
                                        print("\nERROR: Employee details for Hourly Rate, Total Hours Per Day and Competency are expected to be more than 0, Please try again\n")
                                        break
                                    if employee_details[4] > 12:
                                        print("\nERROR: Employee's Total Hours Per Day cannot be more than 12 Hours\n")
                                        break
                                except ValueError:
                                    print("\nERROR: Please check inputs for Employee ID, Hourly Rate, Total Hours Per Day and Competency and ensure that those are inputted as numerical digits, Please try again""\n""")
                                    user_option_reselect= input("\nDo you want to re-input employee details? Y/N""\n""").lower()
                                    while True:
                                        if user_option_reselect in ["y", "n"]:
                                            break
                                        else:
                                            user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                            continue
                                    if user_option_reselect == "y":
                                        continue
                                    else:
                                        break
                                else:
                                    try:
                                        employee_details[7] = dt.datetime.strptime(employee_details[7],'%Y-%m-%d')
                                        if employee_details[7] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d'): #Checks if employee is only joining past tool working date range
                                            print("\nEmployee is planned to start past Resource Tool workable date of {}, Employee will not be added to database in this scenario".format(calendar_end_date))
                                            
                                        else:
                                            if employee_details[7] < dt.datetime.strptime(calendar_start_date,'%Y-%m-%d'):
                                                employee_details[7] = dt.datetime.strptime(calendar_start_date,'%Y-%m-%d')
                                            employee_input_cleaned = True
                                        break
                                    except ValueError:
                                        print("\nERROR: You have entered an invalid date format for Employee Start Date, Please try again""\n""")
                                        user_option_reselect= input("\nDo you want to re-input employee details? Y/N""\n""").lower()
                                        while True:
                                            if user_option_reselect in ["y", "n"]:
                                                break
                                            else:
                                                user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                                continue
                                        if user_option_reselect == "y":
                                            continue
                                        else:
                                            break

                                #END OF DATA VALIDITY CHECKS

                        #IF ALL DATA IS VALID, CREATE EMPLOYEE OBJECT BY CALLING addEmployee() FUNCTION
                        if employee_input_cleaned == True:
                            employee_already_exist = False
                            for employees in list_of_employees:
                                if employee_details[0] == employees.getEmpId():
                                    print("\nEmployee with ID: {} already exist in database\n".format(employee_details[0]))
                                    employee_already_exist = True
                            if employee_already_exist == False:
                                cf.employee.addEmployee(employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5],employee_details[6],employee_details[7], list_of_new_employees, calendar_resource_dict, calendar_end_date)                   
                            



                elif user_option_2 == "2": # Remove Employee
                    while True:
                        employee_details = input("\nPlease key in the following (separated by commas) - \nEmployee ID \nLast Day of Work (yyyy-mm-dd) \nInput: ").strip().split(",")
                        
                        #DATA VALIDITY CHECKS
                        if len(employee_details) != 2:
                            print("\nERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            
                            user_option_reselect = input("\nDo you want to re-input? Y/N""\n""").lower()
                            while True:
                                if user_option_reselect in ["y", "n"]:
                                    break
                                else:
                                    user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                    continue
                            if user_option_reselect == "y":
                                continue
                            else:
                                break
                        
                        else:
                            for i in range(len(employee_details)):
                                employee_details[i] = employee_details[i].strip()    
                            employee_end_before_calendar_end = True

                            try:
                                
                                employee_details[1] = dt.datetime.strptime(employee_details[1],'%Y-%m-%d')
                                if employee_details[1] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d'): #Check if employee is only leaving past tool working date range
                                    print("\nEmployee's Last Day of Work is past Resource Tool workable date of {}, Employee will not be removed from database in this scenario".format(calendar_end_date))
                                    employee_end_before_calendar_end = False

                                if employee_details[1] < dt.datetime.strptime(calendar_start_date,'%Y-%m-%d'):
                                    employee_details[1] = dt.datetime.strptime(calendar_start_date,'%Y-%m-%d')
                            except ValueError:
                                print("\nERROR: You have entered an invalid date format for Last Day of Work, Please try again""\n""")
                                
                                user_option_reselect= input("\nDo you want to re-input employee details? Y/N""\n""").lower()
                                while True:
                                    if user_option_reselect in ["y", "n"]:
                                        break
                                    else:
                                        user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break   
                            else:        
                                try:
                                    employee_details[0] = int(employee_details[0])
                                except ValueError:
                                    print("\nERROR: Please check input for Employee ID, expected input are numerical digits, Please try again""\n""")
                                    
                                    user_option_reselect= input("\nDo you want to re-input employee details? Y/N""\n""").lower()
                                    while True:
                                        if user_option_reselect in ["y", "n"]:
                                            break
                                        else:
                                            user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                            continue
                                    if user_option_reselect == "y":
                                        continue
                                    else:
                                        break   
                                else:
                                    employee_exist_in_database = False
                                    
                                    for employee in list_of_employees:
                                        if employee_details[0] == employee.getEmpId():
                                            employee_exist_in_database = True
                                            removed_employee_craft = employee.getCraft()
                                            
                                            break
                                        else:
                                            continue

                        #END OF DATA VALIDITY CHECKS            

                                    #IF ALL DATA IS VALID AND CONDITIONS ARE MET, DELETE EMPLOYEE OBJECT BY CALLING removeEmployee() FUNCTION                                            
                                    if employee_exist_in_database == True and employee_end_before_calendar_end == True:
                                        confirm_deletion = input("\nDo you confirm removal of employee from database with Employee ID: " + str(employee_details[0]) + "? Y/N""\n""").lower()
                                        while True:
                                            if confirm_deletion in ["y", "n"]:
                                                break
                                            else:
                                                confirm_deletion = input("\nERROR: You have entered an invalid selection, Do you confirm removal of employee from database? Y/N""\n""").lower()
                                                continue
                                        if confirm_deletion == "y":
                                            cf.employee.removeEmployee(employee_details[0],employee_details[1], removed_employee_craft, list_of_leaving_employees, calendar_resource_dict, calendar_end_date, list_of_jobs)
                                            
                                            break

                                            
                                        else:
                                            print("\nDeletion not confirmed, no action taken by Resource Tool\n")
                                            break




                                    elif employee_exist_in_database == False:
                                        print("\nERROR: Employee ID does not exist in current database, Please try again""\n""")
                                        user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                                        while True:
                                            if user_option_reselect in ["y", "n"]:
                                                break
                                            else:
                                                user_option_reselect = input("\nERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                                continue
                                        if user_option_reselect == "y":
                                            continue
                                        else:
                                            break




                else: # Delete Scheduled Job
                    if calendar_resource_dict == {}:
                        print("\n** Please initialise the Resource Tool first **\n")
                    else:
                        user_input = input("\nPlease provide ID (e.g. #1010) of Job to be deleted:""\n""").strip()
                        job_exist = False
                        index = 0
                        if len(list_of_jobs) != 0:
                            for jobs in list_of_jobs: #Check if Job exists in database
                                if user_input == jobs.job_id:
                                    job_exist = True
                                    break
                                index +=1

                        if job_exist == True:
                            while True:
                                user_input_1 = input("\nJob identified in database. Do you confirm Job deletion? Y/N""\n""").lower()
                                
                                if user_input_1 == "y":

                                    for dates in list_of_jobs[index].employees:
                                        for employees in list_of_jobs[index].employees[dates]: #{emp_id : total hours allocated}
                                            for resource in calendar_resource_dict[dates]:
                                                if list(resource.keys())[0] == list(employees.keys())[0]:
                                                    resource[list(resource.keys())[0]] = list(resource.values())[0] + list(employees.values())[0]
                                    del list_of_jobs[index]
                                    print("\nJob has been successfully deleted\n")
                                    
                                    break

                                elif user_input_1 == "n":
                                    print("\nNo action taken by Resource Tool\n")
                                    break

                                else:
                                    print("\nERROR: You have entered an invalid input, Please try again""\n""")
                                    continue


                        else:
                            print("\nJob does not exist in database""\n""")
                





        #OPTION 3 SELECTED
        elif user_option == "3": #Schedule a Job
            if calendar_resource_dict == {}:
                print("\n** Please initialise the Resource Tool with Employees before scheduling any jobs **\n")
            else:
                user_job_details = input("\nPlease input the following (separated by commas) - \nJob Name, \nStart Date (yyyy-mm-dd), \nDue Date (yyyy-mm-dd), \nResources Required (man-hours), \nTotal cost (dollars), \nCraft Required (Metals, Machinery or Instrument/Electrical) \nInput: ").strip().split(",")
                
                #DATA VALIDITY CHECKS
                if len(user_job_details) != 6:
                    print("\nERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                else:
                    for i in range(len(user_job_details)):
                        user_job_details[i] = user_job_details[i].strip()
                    try:
                        user_job_details[3] = float(user_job_details[3])
                        user_job_details[4] = float(user_job_details[4])
                        if user_job_details[3] < 0 or user_job_details[4] < 0:
                            print("\nERROR: Resources Required and Total Cost of the job cannot be less than 0, Please try again\n")
                            raise ValueError
                    except ValueError:
                        print("\nERROR: You have entered an invalid format for Resources or Total Cost, Please try again""\n""")
                    else:
                        try:
                            date_range_error = False
                            user_job_details[1] = dt.datetime.strptime(user_job_details[1],'%Y-%m-%d')
                            user_job_details[2] = dt.datetime.strptime(user_job_details[2],'%Y-%m-%d')
                            if user_job_details[1] < dt.datetime.strptime(calendar_start_date,'%Y-%m-%d') or user_job_details[2] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d') :
                                print("\nERROR: Please schedule a job only within the Resource Tool Working Date Range of {} to {}\n".format(calendar_start_date, calendar_end_date))
                                date_range_error= True
                                raise ValueError
                        except ValueError:
                            if date_range_error == True :
                                pass
                            else:
                                print("\nERROR: You have entered an invalid date format, Please try again""\n""")
                        else:
                            user_job_details[5] = user_job_details[5].lower()
                            if user_job_details[5] not in ["metals", "machinery", "instrument/electrical"]:
                                print(print("\nERROR: You have entered an invalid employee craft, Please ensure that crafts are one of these: Metals, Machinery or Instrument/Electrical\n"))
                            
                #END OF DATA VALIDITY CHECKS            
                            
                            
                            
                            #CALLS scheduleJobCheck() FUNCTION TO SEE IF SCHEDULE IS AVAILABLE, IF NOT AVAILABLE, recommendSchedule() FUNCTION WILL BE CALLED IF USER AGREES 
                            else:
                                check_results, start_date, due_date = cf.scheduleJobCheck(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict, dt.datetime.strptime(calendar_start_date, '%Y-%m-%d'), dt.datetime.strptime(calendar_end_date, '%Y-%m-%d'))
                                
                                
                                #JOB IS SCHEDULED IF USER APPROVES OF SCHEDULED DATE(S)
                                if check_results == True:
                                    cf.scheduleJob(user_job_details[0],start_date, due_date,user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict, job_id, list_of_jobs)
                                    job_id += 1





        #OPTION 4 SELECTED
        elif user_option == "4": #Data Persistence to Files as well as Cost summary
            while True:
                user_input = input("\nPlease input a selection between 1 and 4:""\n"" 1 : Find all job details based on a specific date or by Date Range ""\n"" 2 : Find job details based on Job ID ""\n"" 3 : Total Cost spent on Jobs based on a specific date or by Date Range ""\n"" 4 : Employee List for a specified date (takes into account New Hires and Attritions) \nInput (1), (2), (3) or (4): ")
                if user_input not in ["1", "2", "3", "4"]:
                    while True:
                        user_input = input("\nERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
                        if user_input in ["y", "n"]:
                            break
                        else:
                            continue

                    if user_input == "y":
                        continue
                    else:
                        break                                

                               
                else:
                    if user_input == "1": #Find all job details based on a specific Date or by Date Range
                        date_input = input("\nPlease input start date followed by end date in this format: yyyy-mm-dd, yyyy-mm-dd \n(note: For a single specific date, put both dates as the same) \nInput: ").strip().split(",")
                        if len(date_input) != 2:
                            print("\nERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            break
                        else:    
                            for i in range(len(date_input)):
                                date_input[i] = date_input[i].strip()
                            try:
                                start_date_option_4 = dt.datetime.strptime(date_input[0], '%Y-%m-%d')
                                end_date_option_4 = dt.datetime.strptime(date_input[1], '%Y-%m-%d')
                            except ValueError:
                                print("\nERROR: You have entered an invalid date format/type, Please ensure that it is in yyyy-mm-dd and try again""\n""")
                                break

                            else:
                                list_of_jobs_on_selected_dates = []

                                if start_date_option_4 == end_date_option_4:
                                    for jobs in list_of_jobs:
                                        for dates in jobs.employees:
                                            if dates == start_date_option_4:
                                                list_of_jobs_on_selected_dates.append(jobs)

                                    if len(list_of_jobs_on_selected_dates) != 0:
                                        print("\nThese are the job(s) scheduled to happen on {}\n".format(start_date_option_4.date()))
                                        for items in list_of_jobs_on_selected_dates:
                                            print("\n{}: {} is scheduled with {} employee(s), {{Employee ID: Work Hours}} --> {}\n".format(items.job_id, items.job_name, len(items.employees[start_date_option_4]),items.employees[start_date_option_4] ))

                                        while True:
                                            user_input = input("\nDo you want to save Job details to .csv file? Y/N\n").lower() #Data persistence to .csv
                                            if user_input == "y":

                                                with open("file_output{}.csv".format(file_generation_count), "w", newline="") as f: #with open automatically closes the file once block is fully completed
                                                    fieldnames = ["Date", "Job ID", "Job Name", "Number of Employees", "Craft"]
                                                    writer = csv.DictWriter(f, fieldnames= fieldnames)
                                                    writer.writeheader()
                                                    for items in list_of_jobs_on_selected_dates:
                                                        writer.writerow({"Date": start_date_option_4.date(), "Job ID": items.job_id, "Job Name":items.job_name , "Number of Employees": len(items.employees[start_date_option_4]), "Craft": items.craft})
                                                
                                                print("\nFile successfully saved to folder\n")
                                                
                                                file_generation_count +=1
                                                break

                                            elif user_input =="n":
                                                break

                                            else:
                                                print("\nERROR: You have entered an invalid input, Please try again\n")
                                                continue

                                        break    

                                    else:
                                        print("\nNo job scheduled on this date: {}\n".format(start_date_option_4.date()))
                                        break

                                    

                                elif end_date_option_4 > start_date_option_4:#find the jobs that applies to that date range
                                    sd = start_date_option_4
                                    ed = end_date_option_4
                                    while sd <= ed:
                                        for jobs in list_of_jobs:
                                            for dates in jobs.employees:
                                                if dates == sd:
                                                    list_of_jobs_on_selected_dates.append(jobs)

                                        sd += dt.timedelta(days=1)

                                    list_of_jobs_on_selected_dates = list(set(list_of_jobs_on_selected_dates))

                                    
                                    if len(list_of_jobs_on_selected_dates) != 0:
                                        print("\nThese are the job(s) scheduled to happen from {} to {}\n".format(start_date_option_4.date(), end_date_option_4.date()))
                                        sd =start_date_option_4

                                        while sd <= end_date_option_4:
                                            for items in list_of_jobs_on_selected_dates:
                                                for dates in items.employees:
                                                    if dates == sd:
                                                        print("\n{}: {} is scheduled with {} employee(s) on {}, {{Employee ID: Work Hours}} --> {}\n".format(items.job_id, items.job_name, len(items.employees[dates]), dates.date(),items.employees[dates] )) 

                                            sd += dt.timedelta(days=1)

                                        while True:
                                            user_input = input("\nDo you want to save Job details to .csv file? Y/N\n").lower() #Data persistence to .csv
                                            if user_input == "y":
                                                
                                                with open("file_output{}.csv".format(file_generation_count), "w", newline="") as f:
                                                    fieldnames = ["Date", "Job ID", "Job Name", "Number of Employees", "Craft"]
                                                    writer = csv.DictWriter(f, fieldnames= fieldnames)
                                                    writer.writeheader()
                                                
                                                
                                                    sd = start_date_option_4
                                                    while sd <= end_date_option_4:



                                                        for items in list_of_jobs_on_selected_dates:
                                                            for dates in items.employees:
                                                                if dates == sd:
                                                                    writer.writerow({"Date": sd.date(), "Job ID": items.job_id, "Job Name":items.job_name , "Number of Employees": len(items.employees[sd]), "Craft": items.craft})
                                                    
                                                        sd += dt.timedelta(days=1)
                                                
                                                print("\nFile successfully saved to folder\n")
                                                file_generation_count +=1
                                                
                                                break

                                            elif user_input == "n":
                                                break

                                            else:
                                                print("\nERROR: You have entered an invalid input, Please try again\n")
                                                continue
                                        
                                        break
                                    
                                    else:
                                        print("\nNo job scheduled for this date range: {} to {}\n".format(start_date_option_4.date(), end_date_option_4.date()))
                                    
                                        break

                                else:
                                    print("\nERROR: You have input end date to be earlier than start date, Please try again\n")
                                    break



                    if user_input == "2":  #Find job details based on Job ID
                        job_exist = False
                        id_input = input("\nPlease input Job ID:").strip()

                        for jobs in list_of_jobs:
                            
                            if id_input == jobs.job_id:
                                print("\nJob details are as follows: Job ID: {} , Job Name: {}, Resources Required: {}, Total Cost SGD$: {}, Craft: {}\n".format(jobs.job_id, jobs.job_name, jobs.resources, jobs.total_cost, jobs.craft))
                                print("\nThese are the dates and employees and their hours working on the job:")
                                for dates in jobs.employees:
                                    print(dates.date(), " --> ",jobs.employees[dates])   
                                job_exist = True 
                                
                                break
                            
                            else:
                                
                                continue                   
                        

                        if job_exist == False:
                            print("\nJob ID: {} does not exist in database\n".format(id_input))
                            break


                        break

                    if user_input == "3": #Total Cost spent on Jobs for a specified Date Range
                        
                        print("\n** NOTE: Cost is only considered incurred/captured past the Scheduled Job Completion date in the system (i.e Cost incurred only on last day of job) **\n")
                        date_input = input("\nPlease input start date followed by end date in this format: yyyy-mm-dd, yyyy-mm-dd \n(note: For a single specific date, put both dates as the same) \nInput: ").strip().split(",")
                        
                        if len(date_input) != 2:
                            
                            print("\nERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            
                            break
                        
                        else:    
                            for i in range(len(date_input)):
                                date_input[i] = date_input[i].strip()
                            try:
                                start_date_option_4 = dt.datetime.strptime(date_input[0], '%Y-%m-%d')
                                end_date_option_4 = dt.datetime.strptime(date_input[1], '%Y-%m-%d')
                            except ValueError:
                                print("\nERROR: You have entered an invalid date format/type, Please ensure that it is in yyyy-mm-dd and try again""\n""")
                                break

                            else:
                                list_of_jobs_completed_on_selected_dates = []

                                if start_date_option_4 == end_date_option_4:
                                    for jobs in list_of_jobs:
                                        if jobs.scheduled_end_date == start_date_option_4:
                                            list_of_jobs_completed_on_selected_dates.append({jobs.job_id: jobs.total_cost})

                                    if len(list_of_jobs_completed_on_selected_dates) != 0:
                                        total_cost = 0
                                        print("\nThese are the job(s) completed on this date: {}, with their respective Total Cost(SGD)\n".format(start_date_option_4.date()))
                                        for items in list_of_jobs_completed_on_selected_dates:
                                            print(items)
                                            total_cost += list(items.values())[0]

                                        print("Total Cost = SGD${}".format(total_cost))
                                        
                                        while True:
                                            user_input = input("\nDo you want to save these cost details to .csv file? Y/N\n").lower() #Data persistence to .csv
                                            if user_input == "y":

                                                with open("file_output{}.csv".format(file_generation_count), "w", newline="") as f:
                                                    fieldnames = ["Date", "Job ID", "Total Cost"]
                                                    writer = csv.DictWriter(f, fieldnames= fieldnames)
                                                    writer.writeheader()
                                                    for items in list_of_jobs_completed_on_selected_dates:
                                                        writer.writerow({"Date": start_date_option_4.date(), "Job ID": list(items.keys())[0], "Total Cost":list(items.values())[0]})
                                                
                                                print("\nFile successfully saved to folder\n")
                                                file_generation_count +=1
                                                break

                                            elif user_input =="n":
                                                break

                                            else:
                                                print("\nERROR: You have entered an invalid input, Please try again\n")
                                                continue
                                        break

                                    else:
                                        print("\nNo cost incurred on this particular date: {}\n".format(start_date_option_4.date()))
                                        
                                        break

                                elif end_date_option_4 > start_date_option_4:
                                    
                                    sd = start_date_option_4
                                    ed = end_date_option_4
                                    
                                    while sd <= ed:
                                        for jobs in list_of_jobs:
                                            if jobs.scheduled_end_date == sd:
                                                list_of_jobs_completed_on_selected_dates.append({"Completed Date": "{}".format(jobs.scheduled_end_date.date()), jobs.job_id: jobs.total_cost })

                                        sd += dt.timedelta(days=1)

                                    
                                    if len(list_of_jobs_completed_on_selected_dates) != 0:
                                        total_cost = 0
                                        print("\nThese are the job(s) completed for this date range: {} to {}, with their respective Total Cost(SGD)\n".format(start_date_option_4.date(), end_date_option_4.date()))
                                        for items in list_of_jobs_completed_on_selected_dates:
                                            print(items)
                                            total_cost += list(items.values())[1]

                                        print("Total Cost = SGD${}".format(total_cost))
                                        
                                        while True:
                                            user_input = input("\nDo you want to save these cost details to .csv file? Y/N\n").lower() #Data persistence to .csv
                                            if user_input == "y":

                                                with open("file_output{}.csv".format(file_generation_count), "w", newline="") as f:
                                                    fieldnames = ["Completed Date", "Job ID", "Total Cost"]
                                                    writer = csv.DictWriter(f, fieldnames= fieldnames)
                                                    writer.writeheader()
                                                    for items in list_of_jobs_completed_on_selected_dates:
                                                        writer.writerow({"Completed Date": list(items.values())[0], "Job ID": list(items.keys())[1], "Total Cost":list(items.values())[1]})
                                                
                                                print("\nFile successfully saved to folder\n")
                                                file_generation_count +=1
                                                break

                                            elif user_input =="n":
                                                break

                                            else:
                                                print("\nERROR: You have entered an invalid input, Please try again\n")
                                                continue
                                        break

                                    else:
                                        print("\nNo cost incurred on this particular date: {}\n".format(start_date_option_4.date()))
                                        
                                        break


                                
                                else:
                                    print("\nERROR: You have input end date to be earlier than start date, Please try again\n")
                                    break  
                        
                        





                    if user_input == "4": #Employee List for a specified date (takes into account New Additions and Attritions)
                        date_input = input("\nPlease input date in this format: yyyy-mm-dd\nInput: ").strip()
                        
                        try:
                            date_option_4 = dt.datetime.strptime(date_input, '%Y-%m-%d')
                            
                        except ValueError:
                            print("\nERROR: You have entered an invalid date format/type, Please ensure that it is in yyyy-mm-dd and try again""\n""")
                            
                            break

                        else: 
                            
                            list_of_current_employees = cf.employee.CurrentEmployeeList(list_of_employees, list_of_new_employees, list_of_leaving_employees, date_option_4)
                            if len(list_of_current_employees) != 0:
                                print("\nThis is the list of employees on this date: {}".format(date_option_4.date()))
                                for employees in list_of_current_employees:
                                    print({employees.getEmpId(): employees.getFirstName() + " " + employees.getLastName(), "Craft": employees.getCraft()})
                                
                                while True:
                                            user_input = input("\nDo you want to save employee details to .csv file? Y/N\n").lower() #Data persistence to .csv
                                            if user_input == "y":

                                                with open("file_output{}.csv".format(file_generation_count), "w", newline="") as f:
                                                    fieldnames = ["Emp_id", "First Name", "Last Name", "Craft"]
                                                    writer = csv.DictWriter(f, fieldnames= fieldnames)
                                                    writer.writeheader()
                                                    for employees in list_of_current_employees:
                                                        writer.writerow({"Emp_id":employees.getEmpId() , "First Name":employees.getFirstName() , "Last Name":employees.getLastName(), "Craft":employees.getCraft()})
                                                
                                                print("\nFile successfully saved to folder\n")
                                                file_generation_count +=1
                                                break

                                            elif user_input =="n":
                                                break

                                            else:
                                                print("\nERROR: You have entered an invalid input, Please try again\n")
                                                continue

                                break


                            else:
                                print("\nThere are no remaining employees at this date: {}".format(date_option_4.date()))
                                break
                    
                    
                    
                    










        while True: 
            user_option_continuation = input("\nDo you want to proceed with another action? Y/N ""\n""").lower()
            if user_option_continuation in ["n", "y"]:
                break
            else:
                print("\nERROR: You have entered an invalid selection, please try again""\n""")
                continue
        if user_option_continuation == "y":
            continue
        else: #breaks out of the most outer while loop and the programme stops
            break

if __name__ == "__main__":
    main()
