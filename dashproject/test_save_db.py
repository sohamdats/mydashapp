from pymongo import MongoClient
import random
db = MongoClient().test

def get_random_time():
    hour = str(random.randint(0,24))
    minute = str(random.randint(0,60))
    second = str(random.randint(0,60))
    return hour +":" + minute+":"+second
def get_random_number():
    return random.randint(0,100)

def check_time(time):
    time = time.split(":")
    hour = int(time[0])
    minute= int(time[1])
    second= int(time[2])
    #print(hour,minute,second)
    return (hour,minute,second)

def main():
    random_time=[]
    
    for _ in range(1000):
        random_time.append(get_random_time())
    random_time = sorted(random_time,key=check_time)
    
    for i in range(1000):
        data = {}
        data['time']=random_time[i]
        data['value']=get_random_number()
        db.timestampdata.insert_one(data)
     
    #print(random_time[0:50])
if __name__ =='__main__':
    main()
