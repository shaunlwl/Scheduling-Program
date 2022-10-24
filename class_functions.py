import datetime as dt


def createCalendarRange(start_date, end_date, calendar_resource_dict, list_of_employees):
    '''This function initialises the date range (using a dictionary) for which our scheduling application works'''
    sd = dt.datetime.strptime(start_date, '%Y-%m-%d')
    ed = dt.datetime.strptime(end_date, '%Y-%m-%d')
    delta = ed - sd
    for i in range(delta.days+1):
        for employee in list_of_employees:
            if sd + dt.timedelta(days=i) not in calendar_resource_dict:
                calendar_resource_dict[sd + dt.timedelta(days=i)] = [{employee.getEmpId(): employee.getTotalHoursPerDay(), "Craft" : employee.getCraft()}]
            else:
                calendar_resource_dict[sd + dt.timedelta(days=i)].append({employee.getEmpId():employee.getTotalHoursPerDay(), "Craft" : employee.getCraft()})


def scheduleJob(job_name, start_date, due_date, resources, total_cost, craft ,calendar_resource_dict, current_job_id, list_of_jobs):
    '''This function only runs when there are sufficient resources within the time period of start date and due date and user confirms schedule (i.e scheduleJobCheck returns True)'''
    job_id = "#" + str(current_job_id)
    list_of_jobs.append(job(job_id, job_name, start_date, due_date, resources, total_cost, craft))
    job_start_date = start_date
    while start_date <= due_date  and resources !=0:
        for employee in calendar_resource_dict[start_date]:
            if list(employee.values())[0] == 0:
                continue
            if list(employee.values())[0] != 0 and resources >= list(employee.values())[0] and list(employee.values())[1].lower() == craft.lower(): #[0] is the index for the employee attribute of TotalHoursPerDay and [1] is the index for employee attribute Craft
                resources = resources - list(employee.values())[0]
                if start_date not in list(list_of_jobs[-1].employees.keys()): #if the start date is not a key in the job.employee attribute, save the start date as key
                    list_of_jobs[-1].employees[start_date] = [{list(employee.keys())[0]: list(employee.values())[0]}] #the job.employees attribute will look like this: {2022-01-02: [{emp_id: TotalHoursPerDay}]}
                else:
                    list_of_jobs[-1].employees[start_date].append({list(employee.keys())[0]: list(employee.values())[0]})
                
                employee[list(employee.keys())[0]]= 0

                if resources == 0:
                    break
                

            elif list(employee.values())[0] != 0 and resources < list(employee.values())[0] and list(employee.values())[1].lower() == craft.lower():
                employee[list(employee.keys())[0]]= list(employee.values())[0] - resources
                if start_date not in list(list_of_jobs[-1].employees.keys()):
                    list_of_jobs[-1].employees[start_date] = [{list(employee.keys())[0]: resources}]
                else:
                    list_of_jobs[-1].employees[start_date].append({list(employee.keys())[0]: resources})
                
                resources = resources- resources
                
                if resources == 0:
                    break
            
            else:
                continue
        start_date += dt.timedelta(days=1)
    
    print("SUCCESS! Job {} has been scheduled with ID {} and Start date: {}".format(job_name, job_id, job_start_date.date()))
    print("Here are the employee(s) (by ID) and Work Hours allocated to the Job (i.e {Emp Id : Work hours allocated}):")
    for dates in list_of_jobs[-1].employees:
        print("Date: {} --> {}".format(dates.date(),list(list_of_jobs[-1].employees[dates])))

    #Check that job has been scheduled properly)
    print(calendar_resource_dict)
    print(list_of_jobs[-1].job_id,list_of_jobs[-1].job_name, list_of_jobs[-1].resources)
    #Remove code above once application is ready

def scheduleJobCheck(job_name, start_date, due_date, resources, total_cost, craft, calendar_resource_dict):
    total_available_hours_within_period = 0
    
    current_date = start_date

        
    while current_date < due_date + dt.timedelta(days=1):
        for employee in calendar_resource_dict[current_date]:
            if list(employee.values())[1].lower() == craft.lower():
                total_available_hours_within_period += list(employee.values())[0]
            else:
                continue
        current_date += dt.timedelta(days=1)

    if total_available_hours_within_period >= resources:
        while True:
            user_input = input("Job can be scheduled, do you want to proceed? Y/N""\n""").lower()
            if user_input in ["y", "n"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, Please try again""\n""")
        if user_input == "y":
            return True
                
        else:
            return None
    else:
        print("Job cannot be scheduled due to unavailable resources")
        return False


def recommendSchedule(resources, start_date, due_date, calendar_resource_dict):
    while resources != 0:
        for employee in calendar_resource_dict[start_date]:
            pass
        
    



class job:
    
    def __init__(self, job_id, job_name, start_date, due_date, resources, total_cost, craft):
        
        self.job_id = job_id #does not have to be in numerical format, can be string digits
        self.job_name = job_name
        try:
            self.start_date = start_date
            self.due_date = due_date
            self.resources = float(resources)
            self.total_cost = float(total_cost)
            self.employees = {}
        except ValueError:
            print("ERROR: Job attribute(s) that are expected to be numerical or date format are not in the correct form, please change to numerical/date form""\n""")
            raise IOError
        self.craft = craft
       
             
        
   
class employee:
    
    def __init__(self, emp_id, first_name, last_name, hourly_rate, total_hours_per_day, competency, craft):
        
        self._emp_id = emp_id #does not have to be in numerical format, can be string digits
        self._first_name = first_name
        self._last_name = last_name
        try:
            self._hourly_rate = float(hourly_rate)
            self._total_hours_per_day = float(total_hours_per_day)
            self._competency = float(competency)
        except ValueError:
            print("ERROR: Employee attribute(s) that are expected to be numerical are not in the correct form, please change to numerical form""\n""")
            raise IOError
        self._craft = craft

    def getEmpId(self):
        return self._emp_id

    def setEmpId(self,emp_id):
        self._emp_id = emp_id

    def getFirstName(self):
        return self._first_name

    def setFirstName(self,first_name):
        self._first_name = first_name
    
    def getLastName(self):
        return self._last_name

    def setLastName(self,last_name):
        self._last_name = last_name

    def getHourlyRate(self):
        return self._hourly_rate

    def setHourlyRate(self,hourly_rate):
        self._hourly_rate = hourly_rate

    def getTotalHoursPerDay(self):
        return self._total_hours_per_day

    def setTotalHoursPerDay(self,total_hours_per_day):
        self._total_hours_per_day = total_hours_per_day

    def getCompetency(self):
        return self._competency
    
    def getCraft(self):
        return self._craft

    def setCompetency(self,competency):
        self._competency = competency

    def ComputeAvgCompetency(list_of_employees):
        total_competency =  0
        for employees in list_of_employees:
            total_competency += employees.getCompetency()
        return total_competency/len(list_of_employees)

    def CurrentEmployeeCount(list_of_employees):
        return len(list_of_employees)      

            


    

        

    

