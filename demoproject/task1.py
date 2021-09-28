import paho.mqtt.client as mqtt
import time
import random

host="127.0.0.1"
port=1883
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection successful")
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


# The callback for mqtt logs
def on_log(client,userdata,level,buf):
    # Uncomment to enable logs
    # print("Task1 : (logs) "+buf) 
    pass

# Method to generate random numbers    
def randomNumber(min,max):
    number=random.randint(min,max)
    return number

# Send Message Method
def sendMessage(topic,message):
    client.publish(topic,message,0,False)
    print("Task1: (Publish) "+str(message)+" on "+topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_log=on_log
# MQTT connection
client.connect(host, port, 60)

client.loop_start()
while True:
    sendMessage("demoproject/values",randomNumber(1,100))
    time.sleep(randomNumber(1,30))
