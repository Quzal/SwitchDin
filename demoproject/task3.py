import paho.mqtt.client as mqtt
from tabulate import tabulate
import json
# The callback for when the client receives a CONNACK response from the server.
host="127.0.0.1"
port=1883
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection successful")
        client.subscribe("demoproject/statistics")
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

# Printing  Pretty Tabular Layout in Console
def prettyTabularLayout(stats):
    print(tabulate({
    "1 Minute Average":[stats["oneMinAvg"]],
    "5 Minute Average ":[stats["fiveMinAvg"]], 
    "30 Minute Average":[stats["thirtyMinAvg"]]
    },headers="keys",tablefmt="pretty"))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    data=json.loads(msg.payload) # Converting json string to dict
    prettyTabularLayout(data)
    


    
client = mqtt.Client()
# Callbacks
client.on_connect = on_connect
client.on_message = on_message
#MQTT Connection
client.connect(host, port, 60)

client.loop_forever()