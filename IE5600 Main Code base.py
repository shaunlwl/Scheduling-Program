import class_functions as cf
import datetime as dt

def main():    
    list_of_employees = []
    list_of_jobs = []
    calendar_resource_dict = {} #This data structure will store the daily resource available
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
                user_option_reselect = input("ERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
                if user_option_reselect == "Y":
                    user_option= input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
                    try:
                        if user_option not in ["1", "2", "3", "4"]:
                            raise ValueError
                        else:                            
                            break
                    except ValueError:
                        pass
                elif user_option_reselect == "N":
                    break
                else:
                    pass




        if user_option == "1": #Upload Employee/Job Database from .csv file format only
            while True:
                user_option_1 = input("Do you want to upload 1: Employee database or 2: Job database? Please input 1 or 2 ""\n""")
                try:
                    if user_option_1 not in ["1", "2"]:
                        raise ValueError
                    else:
                        if user_option_1 == "1": 
                            try:
                                with open("test.csv", "r", encoding="utf-8") as file:
                                    employee_attritbutes = []
                                    employee_data = []
                                    for line in file:
                                        employee_data.append(line.strip().split(","))
                                    employee_attritbutes = employee_data.pop(0)
                                    if len(employee_attritbutes) != 6: #checks that the .csv file has six columns for instantiation of employee class type
                                        print("ERROR: Data from .csv file does not match expected input of six employee attributes, please try again""\n""")
                                        continue
                                    else:
                                        for items in employee_data: # this creates the employee objects and assumes that the .csv file has the same columns in the right order (refer to employee class __init__ ordering)
                                            list_of_employees.append(cf.employee(items[0], items[1], items[2],items[3], items[4], items[5]))

                                        cf.createCalendarRange("2022-01-01", "2026-12-31", calendar_resource_dict, list_of_employees) #Scheduling app only works from year 2022 thru 2026

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
                                    if len(job_attributes) != 6:
                                        print("ERROR: Data from .csv file does not match expected input of six job attributes, please try again""\n""")
                                        continue
                                    else:                                        
                                        for items in job_data: # this creates the job objects and assumes that the .csv file has the same columns in the right order (refer to job class __init__ ordering)
                                            list_of_jobs.append(cf.job(items[0], items[1], items[2],items[3], items[4], items[5]))
                                        
                                        break                                      
                            except IOError:
                                print("ERROR: Please make sure that:""\n""1).csv file is in the same directory as .py file ""\n""2).csv file is named correctly ""\n""3)Numerical/Date type job attributes are in correct form ""\n""Pls try again""\n""")
                                continue                                

                except ValueError:
                    while True:
                        user_option_reselect = input("ERROR: You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
                        if user_option_reselect == "Y":
                            break
                        elif user_option_reselect == "N":
                            break
                        else:
                            pass
                if user_option_reselect == "Y":
                    continue
                elif user_option_reselect == "N":        
                    break
                
                    
                    

            


        elif user_option == "2": #Add/Remove Employee(s)/Update Job/Task
            pass
            

        elif user_option == "3": #Schedule a Job
            user_job_details = input("Please input Job Name, Start Date in yyyy-mm-dd, Due Date in yyyy-mm-dd, Resources required, Total cost""\n""").strip().split(",")
            if len(user_job_details) != 5:
                print("ERROR: You have entered an invalid amount of arguments, Please try again""\n""")
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
                        print("You have entered an invalid date format, Please try again""\n""")
                    else:

                        print(user_job_details)
                        check_results = cf.scheduleJobCheck(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], calendar_resource_dict)
                        if check_results == True:
                            cf.scheduleJob(user_job_details[0],user_job_details[1],user_job_details[2],user_job_details[3],user_job_details[4], calendar_resource_dict, job_id, list_of_jobs)
                            job_id += job_id

        elif user_option == "4": #Calculate Key Performance Indicators
            pass


        while True: 
            user_option_continuation = input("Do you want to proceed with another action? Y/N ""\n""")
            if user_option_continuation in ["N", "Y"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, please try again""\n""")
                continue
        if user_option_continuation == "Y":
            continue
        else: #breaks out of the most outer while loop and the programme stops
            break

if __name__ == "__main__":
    main()