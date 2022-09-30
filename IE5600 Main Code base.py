
def main():    
    while True:
        user_option = input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
        try:
            if user_option not in ["1", "2", "3", "4"]:
                raise ValueError
            else:
                user_option = int(user_option)
        except ValueError:
            while True:
                user_option_reselect = input("You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
                if user_option_reselect == "Y":
                    user_option= input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database [From .CSV only] ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
                    try:
                        if user_option not in ["1", "2", "3", "4"]:
                            raise ValueError
                        else:
                            user_option = int(user_option)
                            break
                    except ValueError:
                        pass
                elif user_option_reselect == "N":
                    break
                else:
                    pass




        if user_option == 1: #Upload Employee/Job Database from .csv file format only
            while True:
                user_option_1 = input("Do you want to upload 1: Employee database or 2: Job database? Please input 1 or 2 ""\n""")
                try:
                    if user_option_1 not in ["1", "2"]:
                        raise ValueError
                    else:
                        if user_option_1 == "1":
                            with open("test.csv", "r", encoding="utf-8") as file:
                                employee_data = []
                                for line in file:
                                    employee_data.append(line.replace("\n", ",").split(","))
                                no_of_attributes = len(employee_data[0]) - 1 #-1 due to additional white space from split(",")
                                print(employee_data)
                                print(no_of_attributes)    

                                break
                        elif user_option_1 == "2":
                            with open("job.csv", "r", encoding="utf-8") as file:
                                job_data = []
                                for line in file:
                                    job_data.append(line.replace("\n", ",").split(","))
                                no_of_job_attributes = len(job_data[0]) - 1 #-1 due to additional white space from split(",")
                                print(job_data)
                                print(no_of_job_attributes) 
                            
                                break

                except ValueError:
                    while True:
                        user_option_reselect = input("You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
                        if user_option_reselect == "Y":
                            break
                        elif user_option_reselect == "N":
                            break
                        else:
                            pass
                break
                
                    
                    

            


        elif user_option == 2: #Add/Remove Employee(s)
            pass


        elif user_option == 3: #Schedule a Job
            pass



        else: #Calculate Key Performance Indicators
            pass


        while True: #purpose of this while loop is to keep the programme running after the first selection is fully completed (i.e Option 1 or 2 or 3 or 4 is fully completed)
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
