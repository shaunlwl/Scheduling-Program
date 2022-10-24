import class_functions as cf
import datetime as dt

def main():    
    calendar_start_date = "2022-01-01"
    calendar_end_date = "2032-12-31"
    list_of_employees = []
    list_of_jobs = []
    calendar_resource_dict = {} #This data structure will store the daily resource available by date as key
    job_id = 1000 #initialises first job id to 1000
    
    while True: #Purpose of this while loop is to keep the programme running after the first selection is fully completed (i.e Option 1 or 2 or 3 or 4 is fully completed)
        user_option = input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees or Update Job(s) ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicator(s) ""\n""")
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
                user_option_1 = input("Do you want to upload 1: Employee database or 2: Job database? Please input 1 or 2 ""\n""")
                try:
                    if user_option_1 not in ["1", "2"]:
                        raise ValueError
                    else:
                        if user_option_1 == "1": 
                            try:
                                with open("employee.csv", "r", encoding="utf-8") as file:
                                    employee_attritbutes = []
                                    employee_data = []
                                    for line in file:
                                        employee_data.append(line.strip().split(","))
                                    employee_attritbutes = employee_data.pop(0)
                                    if len(employee_attritbutes) != 7: #checks that the .csv file has seven columns for instantiation of employee class type
                                        print("ERROR: Data from .csv file does not match expected input of seven employee attributes, please try again""\n""")
                                        continue
                                    else:
                                        for items in employee_data: # this creates the employee objects and assumes that the .csv file has the same columns in the right order (refer to employee class __init__ ordering)
                                            list_of_employees.append(cf.employee(items[0], items[1], items[2],items[3], items[4], items[5], items[6]))

                                        cf.createCalendarRange(calendar_start_date, calendar_end_date, calendar_resource_dict, list_of_employees) #Scheduling app only works from year 2022 thru 2032
                                        print(calendar_resource_dict)
                                        break
                            except IOError:
                                print("ERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical employee attributes are in correct form ""\n""Pls try again""\n""")
                                continue   

                        elif user_option_1 == "2": 
                            try:
                                with open("job.csv", "r", encoding="utf-8") as file:
                                    job_attributes = []
                                    job_data = []
                                    for line in file:
                                        job_data.append(line.strip().split(","))
                                    job_attributes = job_data.pop(0)
                                    if len(job_attributes) != 7:
                                        print("ERROR: Data from .csv file does not match expected input of seven job attributes, please try again""\n""")
                                        continue
                                    else:                                        
                                        for items in job_data: # this creates the job objects and assumes that the .csv file has the same columns in the right order (refer to job class __init__ ordering)
                                            list_of_jobs.append(cf.job(items[0], items[1], items[2],items[3], items[4], items[5], items[6]))
                                        
                                        break                                      
                            except IOError:
                                print("ERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical/Date type job attributes are in correct form ""\n""Pls try again""\n""")
                                continue                                

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
                
                    
                    

            


        elif user_option == "2": #Add/Remove Employee(s)/Update Job/Task
            user_option_2 = input("Do you want to:""\n""1 : Add an Employee to Database ""\n""2 : Remove an Employee from Database ""\n""3 : Update existing Job details""\n""")
            if user_option_2 not in ["1", "2", "3"]:
                print("ERROR: You have entered an invalid selection, Please try again")
                continue

            else:
                
                if user_option_2 == "1":
                    employee_input_cleaned = False
                    while True:
                        employee_details = input("Please provide the following details, separated by commas: Employee ID, First Name, Last Name, Hourly Rate, Total Hours Per Day, Competency, Craft, Employee Start Date in yyyy-mm-dd""\n""").strip().split(",")
                        if len(employee_details) != 8:
                            print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
                            user_option_reselect = input("Do you want to re-input? Y/N""\n""").lower()
                            while True:
                                if user_option_reselect in ["y", "n"]:
                                    break
                                else:
                                    user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N").lower()
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
                                        user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N").lower()
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
                                        user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N").lower()
                                        continue
                                if user_option_reselect == "y":
                                    continue
                                else:
                                    break
                            else:
                                try:
                                    employee_details[7] = dt.datetime.strptime(employee_details[7],'%Y-%m-%d')
                                    if employee_details[7] > dt.datetime.strptime(calendar_end_date,'%Y-%m-%d'):
                                        print("Employee is planned to start past Resource Application workable date of 31st December 2032, Employee will not be added to Database in this scenario")
                                        
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
                                            user_option_reselect = input("ERROR: You have entered an invalid selection, Do you want to re-input employee details? Y/N").lower()
                                            continue
                                    if user_option_reselect == "y":
                                        continue
                                    else:
                                        break
                    if employee_input_cleaned == True:
                        cf.employee.addEmployee(employee_details[0],employee_details[1],employee_details[2],employee_details[3],employee_details[4],employee_details[5],employee_details[6],employee_details[7], list_of_employees, calendar_resource_dict, calendar_end_date)                   
                        print(calendar_resource_dict)



                elif user_option_2 == "2": #Remove Employee
                    pass



                else: #Update Scheduled Job details
                    pass
            

        elif user_option == "3": #Schedule a Job
            user_job_details = input("Please input Job Name, Start Date in yyyy-mm-dd, Due Date in yyyy-mm-dd, Resources Required, Total cost, Craft Required""\n""").strip().split(",")
            if len(user_job_details) != 6:
                print("ERROR: You have entered an invalid amount of inputs, Please try again""\n""")
            else:
                for i in range(len(user_job_details)):
                    user_job_details[i] = user_job_details[i].strip()
                try:
                    user_job_details[3] = float(user_job_details[3])
                    user_job_details[4] = float(user_job_details[4])
                except ValueError:
                    print("ERROR: You have entered an invalid format for Resources or Total Cost, Please try again")
                else:
                    try:
                        user_job_details[1] = dt.datetime.strptime(user_job_details[1],'%Y-%m-%d')
                        user_job_details[2] = dt.datetime.strptime(user_job_details[2],'%Y-%m-%d')
                    
                    except ValueError:
                        print("ERROR: You have entered an invalid date format, Please try again""\n""")
                    else:
                     
                        check_results = cf.scheduleJobCheck(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict)
                        if check_results == True:
                            cf.scheduleJob(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], user_job_details[5], calendar_resource_dict, job_id, list_of_jobs)
                            job_id += 1

        elif user_option == "4": #Calculate Key Performance Indicators
            print(list_of_jobs)


        while True: 
            user_option_continuation = input("Do you want to proceed with another action? Y/N ""\n""").lower()
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