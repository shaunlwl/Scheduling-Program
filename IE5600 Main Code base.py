import class_functions as cf
import datetime as dt

def main():    
    calendar_start_date = "2022-12-31" # Application starts working from 31st Dec 2022 onwards only
    calendar_end_date = "2042-12-31"
    list_of_employees = [] #Dos not take into account new additions or removal, to look up the relevant employee list for those
    list_of_new_employees = []
    list_of_leaving_employees = []
    list_of_jobs = []
    calendar_resource_dict = {} #This data structure will store the daily resource available by date as key
    job_id = 1000 #initialises first job id to 1000
    job_database_initialised_count = 0 #To prevent job database from initialising twice

    print("\nRESOURCE MANAGEMENT AND JOB SCHEDULING TOOL ** BETWEEN {} AND {} **".format(calendar_start_date, calendar_end_date))

    while True: #Purpose of this while loop is to keep the programme running after the first selection is fully completed (i.e Option 1 or 2 or 3 or 4 is fully completed)
        
        user_option = input("\nPlease input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees or Delete Scheduled Job ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicator(s) \nInput (1), (2), (3) or (4): ")
        try:
            if user_option not in ["1", "2", "3", "4"]:
                raise ValueError
            else:
                pass
        except ValueError:
            while True:
                user_option_reselect = input("ERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
                if user_option_reselect == "y":
                    user_option= input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
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




        if user_option == "1": #Upload Employee/Job Database from .csv file format only (Note: Option 1 must always be run first to initialise the Resource Calendar)
            while True:
                user_option_1 = input("Which database do you want to upload - \n1 : Employee database \n2 : Job database \nInput (1) or (2): ")
                try:
                    if user_option_1 not in ["1", "2"]:
                        raise ValueError
                    else:
                        if user_option_1 == "1": 
                            try:
                                with open("employee.csv", "r", encoding="utf-8") as file:
                                    employee_attributes = []
                                    employee_data = []
                                    for line in file:
                                        employee_data.append(line.strip().split(","))
                                    employee_attributes = employee_data.pop(0)
                                    if len(employee_attributes) != 7: #checks that the .csv file has seven columns for instantiation of employee class type
                                        print("ERROR: Data from .csv file does not match expected input of seven employee attributes, please try again""\n""")
                                        continue
                                    else:
                                        for items in employee_data: # this creates the employee objects and assumes that the .csv file has the same columns in the right order (refer to employee class __init__ ordering)
                                            list_of_employees.append(cf.employee(items[0], items[1], items[2],items[3], items[4], items[5], items[6]))

                                        cf.createCalendarRange(calendar_start_date, calendar_end_date, calendar_resource_dict, list_of_employees) #Scheduling app only works from year 2022 thru 2032
                                        
                                        break
                            except IOError:
                                print("ERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical employee attributes are in correct form ""\n""Pls try again""\n""")
                                continue   

                        elif user_option_1 == "2": 
                            
                            if job_database_initialised_count == 0:
                                try:
                                    with open("job.csv", "r", encoding="utf-8") as file:
                                        job_attributes = []
                                        job_data = []
                                        for line in file:
                                            job_data.append(line.strip().split(","))
                                        job_attributes = job_data.pop(0)
                                        
                                        
                                        if len(job_attributes) != 6:
                                            print("ERROR: Data from .csv file does not match expected input of six job attributes, please try again""\n""")
                                            continue
                                        else:                                        
                                            if calendar_resource_dict == {}:
                                                print("ERROR: Please initialise Resource Calendar as a first step before adding scheduled jobs by adding employee database""\n""")
                                                continue
                                            
                                            for items in job_data: # this creates the job objects and assumes that the .csv file has the same columns in the right order (refer to job class __init__ ordering)
                                                
                                                items[1] = dt.datetime.strptime(items[1], '%d/%m/%Y')
                                                items[2] = dt.datetime.strptime(items[2], '%d/%m/%Y')
                                                items[3] = float(items[3])
                                                items[4] = float(items[4])
                                                if items[1] < dt.datetime.strptime(calendar_start_date,'%Y-%m-%d'):
                                                    print("Scheduled job starts before Job Scheduling Tool start date of {}, please try again""\n""".format(calendar_start_date))
                                                    break
                                                cf.scheduleJob(items[0], items[1], items[2],items[3], items[4], items[5], calendar_resource_dict, job_id, list_of_jobs)
                                                job_id += 1
                                            job_database_initialised_count = 1 #So that the job database will not be initialised twice   
                                            
                                            break                                      


                                except IOError:
                                    print("ERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical/Date type job attributes are in correct form ""\n""Pls try again""\n""")
                                    continue                                

                            else:
                                print("ERROR: You have already initialised the Job Database""\n""") 
                                break

                except ValueError:
                    while True:
                        user_option_reselect = input("ERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
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
                
                    
                    

            


        elif user_option == "2": #Add/Remove Employee(s)/Delete Scheduled Job
            user_option_2 = input("Do you want to:""\n""1 : Add an employee to database ""\n""2 : Remove an employee from database ""\n""3 : Delete a Scheduled Job \nInput (1), (2) or (3): ")
            if user_option_2 not in ["1", "2", "3"]:
                print("ERROR: You have entered an invalid selection, Please try again")
                

            else:
                
                if user_option_2 == "1": #Add Employee
                    employee_input_cleaned = False
                    while True:
                        employee_details = input("Please provide the following details (separated by commas) - \nEmployee ID, \nFirst Name, \nLast Name, \nHourly Rate, \nTotal Hours Per Day, \nCompetency, \nCraft, \nEmployee Start Date (yyyy-mm-dd) \nInput: ").strip().split(",")
                        if len(employee_details) != 8:
                            print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                            while True:
                                if user_option_reselect in ["y", "n"]:
                                    break
                                else:
                                    user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                    continue
                            if user_option_reselect == "y":
                                continue
                            else:
                                break

                        else:
                            for i in range(len(employee_details)):
                                employee_details[i] = employee_details[i].strip()

                            if employee_details[6].lower() not in ["metals", "machinery", "instrument/electrical"]:
                                print("ERROR: You have entered an invalid employee craft, Please ensure that crafts are one of these: Metals, Machinery or Instrument/Electrical")
                                user_option_reselect= input("Do you want to re-input? Y/N""\n""").lower()
                                while True:
                                    if user_option_reselect in ["y", "n"]:
                                        break
                                    else:
                                        user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break
                            try:
                                employee_details[0] = int(employee_details[0])
                                employee_details[3] = float(employee_details[3])
                                employee_details[4] = float(employee_details[4])
                                employee_details[5] = float(employee_details[5])
                            except ValueError:
                                print("ERROR: Please check inputs for Employee Id, Hourly Rate, Total hours Per Day and Competency and ensure that those are inputted as numerical digits, Please try again""\n""")
                                user_option_reselect= input("Do you want to re-input employee details? Y/N""\n""").lower()
                                while True:
                                    if user_option_reselect in ["y", "n"]:
                                        break
                                    else:
                                        user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break
                            else:
                                try:
                                    employee_details[7] = dt.datetime.strptime(employee_details[7],'%Y-%m-%d')
                                    if employee_details[7] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d'):
                                        print("Employee is planned to start past Resource Application workable date of {}, Employee will not be added to Database in this scenario".format(calendar_end_date))
                                        
                                    else:
                                        employee_input_cleaned = True
                                    break
                                except ValueError:
                                    print("ERROR: You have entered an invalid date format for Employee Start Date, Please try again""\n""")
                                    user_option_reselect= input("Do you want to re-input employee details? Y/N""\n""").lower()
                                    while True:
                                        if user_option_reselect in ["y", "n"]:
                                            break
                                        else:
                                            user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                            continue
                                    if user_option_reselect == "y":
                                        continue
                                    else:
                                        break
                    if employee_input_cleaned == True:
                        cf.employee.addEmployee(employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5],employee_details[6],employee_details[7], list_of_new_employees, calendar_resource_dict, calendar_end_date)                   
                        



                elif user_option_2 == "2": # Remove Employee
                    while True:
                        employee_details = input("Please key in the following (separated by commas) - \nEmployee ID \nLast Day of Work (yyyy-mm-dd) \nInput: ").strip().split(",")
                        if len(employee_details) != 2:
                            print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            
                            user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                            while True:
                                if user_option_reselect in ["y", "n"]:
                                    break
                                else:
                                    user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
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
                                if employee_details[1] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d'):
                                    print("Employee's Last Day of Work is past Resource Application workable date of {}, Employee will not be removed from Database in this scenario".format(calendar_end_date))
                                    employee_end_before_calendar_end = False
                            except ValueError:
                                print("ERROR: You have entered an invalid date format for Last Day of Work, Please try again""\n""")
                                
                                user_option_reselect= input("Do you want to re-input employee details? Y/N""\n""").lower()
                                while True:
                                    if user_option_reselect in ["y", "n"]:
                                        break
                                    else:
                                        user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break   
                            else:        
                                try:
                                    employee_details[0] = int(employee_details[0])
                                except ValueError:
                                    print("ERROR: Please check input for Employee ID, expected input are numerical digits, Please try again""\n""")
                                    
                                    user_option_reselect= input("Do you want to re-input employee details? Y/N""\n""").lower()
                                    while True:
                                        if user_option_reselect in ["y", "n"]:
                                            break
                                        else:
                                            user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
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
                                    if employee_exist_in_database == True and employee_end_before_calendar_end == True:
                                        confirm_deletion = input("Do you confirm removal of employee from database with Employee ID: " + str(employee_details[0]) + "? Y/N""\n""").lower()
                                        while True:
                                            if confirm_deletion in ["y", "n"]:
                                                break
                                            else:
                                                confirm_deletion = input("ERROR: You have entered an invalid selection, Do you confirm removal of employee from database? Y/N""\n""").lower()
                                                continue
                                        if confirm_deletion == "y":
                                            cf.employee.removeEmployee(employee_details[0],employee_details[1], removed_employee_craft, list_of_leaving_employees, calendar_resource_dict, calendar_end_date, list_of_jobs)
                                            break

                                            
                                        else:
                                            print("Deletion not confirmed, no action taken by system")
                                            break




                                    elif employee_exist_in_database == False:
                                        print("ERROR: Employee ID does not exist in current database, Please try again""\n""")
                                        user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                                        while True:
                                            if user_option_reselect in ["y", "n"]:
                                                break
                                            else:
                                                user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N""\n""").lower()
                                                continue
                                        if user_option_reselect == "y":
                                            continue
                                        else:
                                            break




                else: # Delete Scheduled Job
                    
                    user_input = input("Please provide Job ID of Job to be deleted:""\n""").strip()
                    job_exist = False
                    index = 0
                    if len(list_of_jobs) != 0:
                        for jobs in list_of_jobs: #Check if Job exists in databse
                            if user_input == jobs.job_id:
                                job_exist = True
                                break
                            index +=1

                    if job_exist == True:
                        while True:
                            user_input_1 = input("Job identified in database. Do you confirm Job deletion? Y/N""\n""").lower()
                            
                            if user_input_1 == "y":

                                for dates in list_of_jobs[index].employees:
                                    for employees in list_of_jobs[index].employees[dates]: #{emp_id : total hours allocated}
                                        for resource in calendar_resource_dict[dates]:
                                            if list(resource.keys())[0] == list(employees.keys())[0]:
                                                resource[list(resource.keys())[0]] = list(resource.values())[0] + list(employees.values())[0]
                                print("Job has been successfully deleted")
                                
                                break

                            elif user_input_1 == "n":
                                print("No action taken by system")
                                break

                            else:
                                print("ERROR: You have entered an invalid input, Please try again""\n""")
                                continue


                    else:
                        print("Job does not exist in database""\n""")
            



        elif user_option == "3": #Schedule a Job
            user_job_details = input("Please input the following (separated by commas) - \nJob Name, \nStart Date (yyyy-mm-dd), \nDue Date (yyyy-mm-dd), \nResources Required (man-hours), \nTotal cost (dollars), \nCraft Required (Metals, Machinery or Instrument/Electrical) \nInput: ").strip().split(",")
            if len(user_job_details) != 6:
                print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
            else:
                for i in range(len(user_job_details)):
                    user_job_details[i] = user_job_details[i].strip()
                try:
                    user_job_details[3] = float(user_job_details[3])
                    user_job_details[4] = float(user_job_details[4])
                except ValueError:
                    print("ERROR: You have entered an invalid format for Resources or Total Cost, Please try again""\n""")
                else:
                    try:
                        user_job_details[1] = dt.datetime.strptime(user_job_details[1],'%Y-%m-%d')
                        user_job_details[2] = dt.datetime.strptime(user_job_details[2],'%Y-%m-%d')
                    
                    except ValueError:
                        print("ERROR: You have entered an invalid date format, Please try again""\n""")
                    else:
                     
                        check_results, start_date, due_date = cf.scheduleJobCheck(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict)
                        if check_results == True:
                            cf.scheduleJob(user_job_details[0],start_date, due_date,user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict, job_id, list_of_jobs)
                            job_id += 1






        elif user_option == "4": #Calculate Key Performance Indicators
            while True:
                user_input = input("Please input a selection between 1 and 4:""\n"" 1 : Find all job details based on a specific Date or by Date Range ""\n"" 2 : Find job details based on Job ID ""\n"" 3 : Total Cost spent on Jobs for a specified Date Range ""\n"" 4 : Total Employee count by Craft for a specified Date (takes into account New Additions and Attritions) \nInput (1), (2), (3) or (4): ")
                if user_input not in ["1", "2", "3", "4"]:
                    while True:
                        user_input = input("ERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""").lower()
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
                        date_input = input("Please input start date followed by end date in this format: yyyy-mm-dd, yyyy-mm-dd \n(note: For a single specific date, put both dates as the same) \nInput: ").strip().split(",")
                        if len(date_input) != 2:
                            print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            break
                        else:    
                            for i in range(len(date_input)):
                                date_input[i] = date_input[i].strip()
                            try:
                                start_date_option_4 = dt.datetime.strptime(date_input[0], '%Y-%m-%d')
                                end_date_option_4 = dt.datetime.strptime(date_input[1], '%Y-%m-%d')
                            except ValueError:
                                print("ERROR: You have entered an invalid date format/type, Please ensure that it is in yyyy-mm-dd and try again""\n""")
                            else:
                                if start_date_option_4 == end_date_option_4:
                                    pass #find any jobs that is happening on a specific date (use list of job employee attribute)
                                else:
                                    pass #find the jobs that applies to that date range



                    if user_input == "2":  #Find job details based on Job ID
                        job_exist = False
                        id_input = input("Please input Job ID""\n""").strip()
                        for jobs in list_of_jobs:
                            if id_input == jobs.job_id:
                                print("Job details are as follows: {} , {}, {}, {}, {} ".format(jobs.job_id, jobs.job_name, jobs.resources, jobs.total_cost, jobs.craft))
                                print("These are the dates and employees and their hours working on the job:")
                                print(jobs.employees)   
                                job_exist = True 
                                break
                            else:
                                continue                   
                        if job_exist == False:
                            print("Job ID does not exist in current database")

                    if user_input == "3": #Total Cost spent on Jobs for a specified Date Range
                        break


                    if user_input == "4": #Total Employee count by Craft for a specified Date (takes into account New Additions and Attritions)
                        break

                    
                    
                    
                    break










        while True: 
            user_option_continuation = input("\nDo you want to proceed with another action? Y/N ""\n""").lower()
            if user_option_continuation in ["n", "y"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, please try again""\n""")
                continue
        if user_option_continuation == "y":
            continue
        else: #breaks out of the most outer while loop and the programme stops
            break

if __name__ == "__main__":
    main()
