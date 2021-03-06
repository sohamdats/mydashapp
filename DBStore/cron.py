from crontab import CronTab
import os


class CTab:
    def __init__(self,username=None):
        self.cron = CronTab(user=username)

    def print_job(self,comment=None):
        '''
            Args:
              comment:To print a specific job
        '''
        if comment:
            print('The Job is...')
            for job in self.cron:
                if job.comment == comment:
                    print(job)
        else:
            print('All the jobs are..')
            for job in self.cron:
                print(job)

    def add_job(self,command,interval,comment=None):
        '''
           Args:
                command: command that the job will execute,
                interval: every minute,
                comment: a comment for the job(Optional 
                         but recommended)
        '''
        job = self.cron.new(command=command,comment=comment)
        job.minute.every(interval)
        self.cron.write()
        print('Job added successfully...')
    
    def remove_job(self,comment=None):
        '''
           Args:
               comment: To remove specific job
        '''
        if comment:
            for job in self.cron:
                if job.comment == comment:
                    self.cron.remove(job)
                    print("Job removed...")
        else:
             self.cron.remove_all()
             print('All jobs removed..')
        self.cron.write()

    
        
if __name__ == '__main__':
    import sys
    cron = CTab('sohdatta')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'test.py')
    command = 'python ' + file_path
    comment = 'Storing container stats in mongodb'
    if len(sys.argv) > 1 and sys.argv[1] == 'remove':
        cron.remove_job()
    else:
        cron.add_job(command,1,comment)
    
