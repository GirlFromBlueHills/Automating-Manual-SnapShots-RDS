#RDS Automation - Manual Snapshot Creation

Manual snaphots are very important in RDS since it will remain available even when you delete your instance. But taking a manual snapshot may be tedious especially if you have a large number of instances. You have to go individually on each instance and go to create snapshots. I have tried to automate this process with python. Kindly note that this is just a basic code and you can do or add a lot with this code.


Requirements:
1. Python 3.6 - boto
2. AWS Account - user access and secret access credentials

Installation:
1. Kindly install the packages involved by checking the snap.py file
	example:	pip install datetime
2. Change the config.json file and add your aws account details. 
3. Under the INSTANCES in config.json file, add the instance name which you have specified

Run:
1. run the snap.py file
	python snap.py
