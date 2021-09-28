import paho.mqtt.client as mqtt
import time
import schedule
import json

host="127.0.0.1"
port=1883
oneMinData=fiveMinData=thirtyMinData=[]
Statistics={"oneMinAvg":None,"fiveMinAvg":None,"thirtyMinAvg":None}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection successful")
        client.subscribe("demoproject/values")
    elif rc==1:
        print("Connection refused - incorrect protocol version")
    elif rc==2:
        print("Connection refused - invalid client identifier")
    elif rc==3:
        print("Connection refused - server unavailable ")
    elif rc==4:
        print("Connection refused - bad username or password")
    elif rc==5:
        print(" Connection refused - not authorised")            
    else:
        print("Connection Unsuccessfull")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Task 2:  (Recieved) "+msg.payload.decode('utf-8', 'ignore')+" on "+msg.topic+" ")
    oneMinData.append(int(msg.payload))
    fiveMinData.append(int(msg.payload))
    thirtyMinData.append(int(msg.payload))



# Calculating 1 minute Average
def OneMinAverage():
    try:
        average=0
        for i in oneMinData:
            average+=i
        average=average/len(oneMinData)
        average=round(average,2)
        del oneMinData[:]
        Statistics["oneMinAvg"]=average;
        SendMessage("demoproject/statistics",Statistics)
    except:
        pass
# Calculating 5 minute Average
def FiveMinAverage():
    try:
        average=0
        for i in fiveMinData:
            average+=i
        average=average/len(fiveMinData)
        average=round(average,2)
        del fiveMinData[:]
        Statistics["fiveMinAvg"]=average;
        SendMessage("demoproject/statistics",Statistics)
    except:
        pass
# Calculating 30 minute Average 
def ThirtyMinAverage():
    try:
        average=0
        for i in thirtyMinData:
            average+=i
        average=average/len(thirtyMinData)
        average=round(average,2)
        del thirtyMinData[:]
        Statistics["thirtyMinAvg"]=average;
        SendMessage("demoproject/statistics",Statistics)
    except:
        pass
# Publish Message
def SendMessage(topic,data):
    data=json.dumps(data) # Coverting dict to json string
    client.publish(topic,data,0,False)
    print("Task 2: (Publish) "+json.dumps(data)+" on "+topic)

client = mqtt.Client()
# Callbacks
client.on_connect = on_connect
client.on_message = on_message
#Mqtt Connection
client.connect(host, port, 60)


# Event Scheduling
schedule.every().minutes.do(OneMinAverage)
schedule.every(5).minutes.do(FiveMinAverage)
schedule.every(30).minutes.do(ThirtyMinAverage)

while True:
    schedule.run_pending()
    client.loop()
    time.sleep(1)


