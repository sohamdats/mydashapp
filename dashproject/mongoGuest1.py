from pymongo import MongoClient


class mongoGuest:
    def __init__(self):
        self.db = MongoClient().test

        
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
            
        
    def get_cpu_usage(self,cont_id,percent=False):
        time = 1
        X = []
        Y = []
        for doc in self.db.timestamp.find():
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
        for doc in self.db.timestamp.find():
            for con in doc['stats']:
                if con['name'] == cont_id:
                    Y.append(con['memory_usage'])
                    X.append(time)
                    time += 1

        return (X,Y)
                    
        
