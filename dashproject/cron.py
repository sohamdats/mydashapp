from datetime import datetime,timedelta
from pymongo import MongoClient
import docker
from time import sleep

class dockerGuest:
    def __init__(self):
        self.client = docker.APIClient(base_url = 'unix://var/run/docker.sock')

    def container_list(self):
        return self.client.containers()

    def get_stats(self):
        stat_list = []
        container_list = self.container_list()
        if len(container_list) == 0:
            return None
        
        for container in container_list:
            _id = container['Id']
            _dict = self.client.stats(container=_id,stream=False)
            stat_dict = {}
            stat_dict["_id"] = _id
            stat_dict["name"] = _dict["name"][1:]
            stat_dict["cpu_usage"] = _dict["cpu_stats"]["cpu_usage"]["total_usage"]
            stat_dict["memory_usage"] = _dict["memory_stats"]["usage"]
            stat_list.append(stat_dict)
        return stat_list

class Stat:
    def __init__(self):
        self.docker = dockerGuest()
        self.client = MongoClient()
        self.db = self.client.test

    @staticmethod
    def get_time():
        t = datetime.now() + timedelta(hours=5,minutes=30)
        return t.strftime("%H:%M:%S")
    
    def data_to_save(self):
        stats = self.docker.get_stats()
        if stats == None:
            return None
        global_stat_dict ={}
        global_stat_dict["time"]=Stat.get_time()
        global_stat_dict["stats"] = stats
        return global_stat_dict

    
    def save_to_db(self):        
        data = self.data_to_save()        
        if data != None:
            self.db.timestamp.insert_one(data)

    def make_space_db(self):
        self.db.timestamp.delete_one({'_id':db.timestamp.find()[0]['_id']})

    def is_db_full(self):
        if self.db.timestamp.find({}).count() == 60:
            return True
        return False

def get_scheduled_job():
    stat = Stat()
    if stat.is_db_full():
        stat.make_space_db()
    stat.save_to_db()
        
if __name__ == '__main__':
    get_scheduled_job()
        
'''
def main():
    docker = docker.APIClient(base_url='unix://var/run/docker.sock') 
    client = MongoClient()
    db = client.test
        
    
    for i in range(7):
        docker.create_container('my-gcc-app',detach=True)

    docker.run_containers()



    for stat in docker.generate_stats():
        global_stat_dict={}     #document in mongodb
        global_stat_dict["time"]=get_time()

        stat_list = []

        for stat_container in stat:
            stat_dict = {}

            _id = stat_container["id"]
            name=stat_container["name"]
            cpu_usage= stat_container["cpu_stats"]["cpu_usage"]["total_usage"]
            memory_usage=stat_container["memory_stats"]["usage"]
            
            stat_dict["id"]=_id
            stat_dict["name"]=name
            stat_dict["cpu_usage"]=cpu_usage
            stat_dict["memory_usage"]=memory_usage

            stat_list.append(stat_dict)
            

        global_stat_dict["stat_list"] = stat_list
        db.test_table.insert_one(global_stat_dict)  #storing each document in test_table collection  
        pprint(global_stat_dict,width=1)    
    

if __name__ == '__main__':
    main()
'''
