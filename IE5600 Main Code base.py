import class_functions as cf

def main(): #Purpose of this while loop is to keep the programme running after the first selection is fully completed (i.e Option 1 or 2 or 3 or 4 is fully completed)   
    list_of_employees = []
    list_of_jobs = []
    while True:
        user_option = input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
        try:
            if user_option not in ["1", "2", "3", "4"]:
                raise ValueError
            else:
                pass
        except ValueError:
            while True:
                user_option_reselect = input("You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
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
                        if user_option_1 == "1": #this assumes that "test".csv file is in same directory as current .py file and is named correctly
                            try:
                                with open("test.csv", "r", encoding="utf-8") as file:
                                    employee_attritbutes = []
                                    employee_data = []
                                    for line in file:
                                        employee_data.append(line.strip().split(","))
                                    employee_attritbutes = employee_data.pop(0)
                                    for items in employee_data: # this assumes that the .csv file has the same columns in the right order always (refer to employee class __init__ ordering)
                                        list_of_employees.append(cf.employee(items[0], items[1], items[2],items[3], items[4], items[5]))
                                    break
                            except IOError:
                                print("ERROR: Please make sure that 1).csv file is in the same directory as .py file and 2) .csv file is named correctly ""\n""Pls try again")
                                continue   

                        elif user_option_1 == "2": #this assumes that "job".csv file is in same directory as current .py file and is named correctly
                            try:
                                with open("job.csv", "r", encoding="utf-8") as file:
                                    job_attributes = []
                                    job_data = []
                                    for line in file:
                                        job_data.append(line.strip().split(","))
                                    job_attributes = job_data.pop(0)
                                    no_of_job_attributes = len(job_attributes)
                                    print(job_data)
                                    print(no_of_job_attributes)
                                    break 
                            except IOError:
                                print("ERROR: Please make sure that 1).csv file is in the same directory as .py file and 2) .csv file is named correctly ""\n""Pls try again")
                                continue                                

                except ValueError:
                    while True:
                        user_option_reselect = input("You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
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
            pass



        elif user_option == "4": #Calculate Key Performance Indicators
            pass


        while True: 
            user_option_continuation = input("Do you want to proceed with another action? Y/N ""\n""")
            if user_option_continuation in ["N", "Y"]:
                break
            else:
                print("You have entered an invalid selection, please try again")
                continue
        if user_option_continuation == "Y":
            continue
        else: #breaks out of the most outer while loop and the programme stops
            break

if __name__ == "__main__":
    main()