from datetime import datetime

employee_table = {'emp_id':[], 'name':[], 'competency':[]}
job_table = {'job_id':[], 'start_date':[], 'due_date':[], 'resources':[]}

class job:
    
    def __init__(self, job_id, start_date, due_date, resources):
        
        self.job_id = job_id
        self.start_date = start_date
        self.due_date = due_date
        self.resources = resources
        
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
    
    def __init__(self, emp_id, name, competency):
        
        self.emp_id = emp_id
        self.name = name
        self.competency = int(competency)
        
        if self.emp_id not in employee_table:
            employee_table['emp_id'].append(self.emp_id)
            employee_table['name'].append(self.name)
            employee_table['competency'].append(self.competency)
            
    def remove(self):
        
        if self.emp_id in employee_table['emp_id']:
            index = employee_table['emp_id'].index(self.emp_id)
            employee_table['emp_id'].pop(index)
            employee_table['name'].pop(index)
            employee_table['competency'].pop(index)
            
        else:
            return print('Record is not found!')
        
        

    

      
    
start = '2022/8/20 18:00'
end = '2022/12/10 8:20'
resources = 50

task1 = job(5, start, end, resources)
task2 = job(50, start, end, resources)