import csv
User_option= input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
try:
    if User_option not in ["1", "2", "3", "4"]:
        raise ValueError
    else:
        User_option = int(User_option)
except ValueError:
    while True:
        User_option_reselect = input("You have entered an invalid selection, do you want to re-select? Y/N ""\n""")
        if User_option_reselect == "Y":
            User_option= input("Please input a selection between 1 and 4:""\n"" 1 : Upload Employee/Job Database ""\n"" 2 : Add/Remove Employees ""\n"" 3 : Schedule a Job ""\n"" 4 : Calculate Key Performance Indicators ""\n""")
            try:
                if User_option not in ["1", "2", "3", "4"]:
                    raise ValueError
                else:
                    User_option = int(User_option)
                    break
            except ValueError:
                pass
        elif User_option_reselect == "N":
            break
        else:
            pass

if User_option == 1: #Upload Employee/Job Database
    file =  open('data.csv', 'r')
    reader = csv.reader(file)


elif User_option == 2: #Add/Remove Employee(s)
    pass


elif User_option == 3: #Schedule a Job
    pass



else: #Calculate Key Performance Indicators
    pass
