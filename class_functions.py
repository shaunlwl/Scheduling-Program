import datetime as dt


def createCalendarRange(start_date, end_date, calendar_resource_dict, list_of_employees):
    '''This function initialises the date range for which our scheduling application works'''
    sd = dt.datetime.strptime(start_date, '%Y-%m-%d')
    ed = dt.datetime.strptime(end_date, '%Y-%m-%d')
    delta = ed - sd
    for i in range(delta.days+1):
        calendar_resource_dict[sd + dt.timedelta(days=i)] = list_of_employees
    


def scheduleJob(job_name, start_date, due_date, resources, total_cost, calendar_resource_dict, current_job_id):
    '''This function only runs when there is sufficient available resource within the time period of start date and due date, after function scheduleJobCheck is carried out'''
    pass


def scheduleJobCheck(job_name, start_date, due_date, resources, total_cost, calendar_resource_dict):
    total_available_hours_within_period = 0
    
    current_date = start_date

        
    while current_date < due_date + dt.timedelta(days=1):
        for employee in calendar_resource_dict[current_date]:
            total_available_hours_within_period += employee.getTotalHoursPerDay()
        current_date += dt.timedelta(days=1)

    if total_available_hours_within_period >= resources:
        while True:
            user_input = input("Job can be scheduled, do you want to proceed? Y/N""\n""")
            if user_input in ["Y", "N"]:
                break
            else:
                print("ERROR: You have entered an invalid selection, Please try again""\n""")
        if user_input == "Y":
            return True
                
        else:
            return False
    else:
        print("Job cannot be scheduled due to unavailable resources")
        return False







class job:
    
    def __init__(self, job_id, job_name, start_date, due_date, resources, total_cost):
        
        self.job_id = job_id #does not have to be in numerical format, can be string digits
        self.job_name = job_name
        try:
            self.start_date = start_date
            self.due_date = due_date
            self.resources = float(resources)
            self.total_cost = float(total_cost)
            self.employees = []
        except ValueError:
            print("ERROR: Job attribute(s) that are expected to be numerical or date format are not in the correct form, please change to numerical/date form""\n""")
            raise IOError
       
    
    def max_duration(self):
        
        self.start_date = dt.datetime.strptime(self.start_date, "%Y/%m/%d %H:%M")
        self.due_date = dt.datetime.strptime(self.due_date, "%Y/%m/%d %H:%M")
        
        delta = self.due_date - self.start_date
        
        return int(delta.total_seconds()/3600)

    
    # def remove(self):
        
    #     if self.job_id in job_table['job_id']:
    #         index = job_table['job_id'].index(self.job_id)
    #         job_table['job_id'].pop(index)
    #         job_table['start_date'].pop(index)
    #         job_table['due_date'].pop(index)
    #         job_table['resources'].pop(index)
            
    #     else:
    #         return print('Record is not found!')
        
        
   
class employee:
    
    def __init__(self, emp_id, first_name, last_name, hourly_rate, total_hours_per_day, competency):
        
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

    def setCompetency(self,competency):
        self._competency = competency

    def ComputeAvgCompetency(list_of_employees):
        total_competency =  0
        for employees in list_of_employees:
            total_competency += employees.getCompetency()
        return total_competency/len(list_of_employees)

    def CurrentEmployeeCount(list_of_employees):
        return len(list_of_employees)      

            
    # def removeEmployee(self):
        
    #     if self._emp_id in employee_table['emp_id']:
    #         index = employee_table['emp_id'].index(self._emp_id)
    #         del_emp_id = employee_table['emp_id'].pop(index)
    #         del_first_name = employee_table['first_name'].pop(index)
    #         del_last_name = employee_table['last_name'].pop(index)
    #         del employee_table['hourly_rate'][index] #do not use pop here as there is no need to return the deleted value
    #         del employee_table['total_hours_per_day'][index]
    #         del employee_table['competency'][index]
    #         return print("Successfully removed " + del_emp_id + " " + del_first_name + " " + del_last_name + " from database.")

    #     else:
    #         return print('ERROR: No such employee record found!')
        

    

        

    

