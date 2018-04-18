from pymongo import MongoClient
from datetime import datetime
import os 

class mongoGuest:
    def __init__(self):
        self.collection = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)['test']['t']
        
    def find_cpu_percentage(self,con):
        cpu_usage = con["cpu_usage"]
        system_usage = con["system_cpu_usage"]
        precpu_usage= con["pre_cpu_usage"]
        presystem_usage = con["presystem_usage"]
        online_cpus = con["online_cpus"]
        cpu_delta = (cpu_usage - precpu_usage)
        system_delta = (system_usage - presystem_usage)
        
        if cpu_delta >0.0 and system_delta > 0.0:
            return (cpu_delta/system_delta) * online_cpus *100.0
        else:
            return 0.0

    def changeHMS(self,time):
        return time.strftime("%H:%M:%S")

    def get_cpu_usage(self,cont_name,percent=False):
        time = 1
        timestamps = []
        X = []
        Y = []
        for doc in self.collection.find():
            timestamps.append(doc["time"])
        timestamps.sort()
        for ts_obj in timestamps:
            doc = self.collection.find({'time':ts_obj})[0]
            for con in doc['stats']:
                if con['name'] == cont_name:
                    if percent==True:
                        Y.append(self.find_cpu_percentage(con))
                    else:
                        Y.append(con["cpu_usage"])
            X.append(self.changeHMS(ts_obj))
            #X.append(time)
            time+=1

        return (X,Y)

    def get_memory_usage(self,cont_name):
        time = 1
        timestamps = []
        X = []
        Y = []
        for doc in self.collection.find():
            timestamps.append(doc["time"])
        timestamps.sort()
        for ts_obj in timestamps:
            doc = self.collection.find({'time':ts_obj})[0]
            for con in doc['stats']:
                if con['name'] == cont_name:
                    Y.append(con['memory_usage'])
            X.append(self.changeHMS(ts_obj))
            #X.append(time)
            time+=1
        return (X,Y)
    
    '''
    def get_cpu_usage(self,cont_id,percent=False):
        time = 1
        X = []
        Y = []
        
        for doc in self.collection.find():
            for con in doc['stats']:
                if con['name'] == cont_id:
                    if percent==True:
                        Y.append(self.find_cpu_percentage(con))
                    else:
                        Y.append(con["cpu_usage"])
                    X.append(time)
                    time+=1
    
        return (X,Y)
    

    def get_memory_usage(self,cont_id):
        time = 1
        X = []
        Y = []
        for doc in self.collection.find():
            for con in doc['stats']:
                if con['name'] == cont_id:
                    Y.append(con['memory_usage'])
                    X.append(time)
                    time += 1

        return (X,Y)
                    
    '''    
