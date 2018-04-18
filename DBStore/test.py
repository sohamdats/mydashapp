import os
from datetime import datetime
from pymongo import MongoClient

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'logfile')
    f = open(file_path,'a')
    f.write('its working: {}'.format(datetime.now()))
    
    db = MongoClient().test
    f.write("object created") 
    data ={'time':str(datetime.now())}
    db.testingcon.insert_one(data)
    f.write("document inserted")
    
    f.close()
    
main()
