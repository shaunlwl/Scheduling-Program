from datetime import datetime

employee_table = {'emp_id':[], 'first_name':[], "last_name": [], "hourly_rate" : [], "total_hours_per_day" : [], 'competency':[] }
job_table = {'job_id':[], 'start_date':[], 'due_date':[], 'resources':[]}

class job:
    
    def __init__(self, job_id, job_name, start_date, due_date, resources, total_cost):
        
        self.job_id = job_id
        self.job_name = job_name
        self.start_date = start_date
        self.due_date = due_date
        self.resources = resources
        self.total_cost = total_cost
        
        if self.job_id not in job_table:
            job_table['job_id'].append(self.job_id)
            job_table['start_date'].append(self.start_date)
            job_table['due_date'].append(self.due_date)
            job_table['resources'].append(self.resources)
            
    
    def max_duration(self):
        
        self.start_date = datetime.strptime(self.start_date, "%Y/%m/%d %H:%M")
        self.due_date = datetime.strptime(self.due_date, "%Y/%m/%d %H:%M")
        
        delta = self.due_date - self.start_date
        
        return int(delta.total_seconds()/3600)
    
    def remove(self):
        
        if self.job_id in job_table['job_id']:
            index = job_table['job_id'].index(self.job_id)
            job_table['job_id'].pop(index)
            job_table['start_date'].pop(index)
            job_table['due_date'].pop(index)
            job_table['resources'].pop(index)
            
        else:
            return print('Record is not found!')
        
        
   
class employee:
    
    def __init__(self, emp_id, first_name, last_name, hourly_rate, total_hours_per_day, competency):
        
        self._emp_id = emp_id
        self._first_name = first_name
        self._last_name = last_name
        self._hourly_rate = float(hourly_rate)
        self._total_hours_per_day = float(total_hours_per_day)
        self._competency = float(competency)
        
        if self._emp_id not in employee_table:
            employee_table['emp_id'].append(self._emp_id)
            employee_table['first_name'].append(self._first_name)
            employee_table['last_name'].append(self._last_name)
            employee_table['hourly_rate'].append(self._hourly_rate)
            employee_table["total_hours_per_day"].append(self._total_hours_per_day)            
            employee_table['competency'].append(self._competency)
            
    def remove(self):
        
        if self.emp_id in employee_table['emp_id']:
            index = employee_table['emp_id'].index(self.emp_id)
            employee_table['emp_id'].pop(index)
            employee_table['name'].pop(index)
            employee_table['competency'].pop(index)
            
        else:
            return print('Record is not found!')
        
        

    

      
    
# start = '2022/8/20 18:00'
# end = '2022/12/10 8:20'
# resources = 50

# task1 = job(5, start, end, resources)
# task2 = job(50, start, end, resources)