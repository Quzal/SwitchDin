# SwitchDin | Demo Project | Python Data Developer
## Table of contents
* [Running MQTT Broker](#mqtt-broker)
* [Running Programs](#running)

## Running MQTT Broker
In order to run Mqtt Broker change the mosquitto.conf to one provided with this repo<br>
Run the following command
```
sudo docker run -it -p 1883:1883 --restart always -v /home/ubuntu/SwitchDin/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
````
## Running Programs
Create a Virtual Environment and Install the packages mentioned in the SwitchDin/demoproject/requirement.txt 
#### Run Task 1 
Change the directory to demoproject
```
cd SwitchDin/demoproject
````
Then run the script to start task1
```
python3 task1.py
````
#### Run Task 2
While keeping in the same directory i.e SwitchDin/demoproject<br>
Run the command
```
python3 task2.py
```
### Run Task 3
In the same directory run the command
```
python3 task3.py
```


