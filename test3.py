import boto3
import datetime
import time
import os
import json
import random

class RDSSnapShots:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        config_file = script_dir + '/config.json'
        #print(script_dir)
        if not os.path.isfile(config_file):
            print(config_file + " does not exist")
            exit(1)
        else:
            config_data = open(config_file).read()
            config_json = json.loads(config_data)
            self.AWS_REGION = config_json['AWS_REGION']
            self.ACCESS_KEY_ID = config_json['ACCESS_KEY_ID']
            self.SECRET_ACCESS_KEY_ID = config_json['SECRET_ACCESS_KEY_ID']
            self.ACCOUNT_ID = config_json['ACCOUNT_ID']
            self.INSTANCES = config_json['INSTANCES']
            print(self.INSTANCES)
        self.session = boto3.Session(aws_access_key_id=self.ACCESS_KEY_ID,aws_secret_access_key=self.SECRET_ACCESS_KEY_ID,region_name=self.AWS_REGION)
        self.rds = self.session.client('rds')

    def rds_list(self):
        rds_instances = self.rds.describe_db_instances()['DBInstances']
        return rds_instances


    def create_snapshots(self, rds_instances):
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        rds_snapshot = "{0}-{1}-{2}".format("mysnapshot", rds_instances, timestamp)
        snap = self.rds.create_db_snapshot(DBSnapshotIdentifier=rds_snapshot, DBInstanceIdentifier=rds_instances)
        time.sleep(2)  # wait 2 seconds before status request
        current_status = None
        print("SNAPSHOT CREATING OF: ",rds_instances)
        while True:
            current_status = self.rds.describe_db_snapshots(DBSnapshotIdentifier=rds_snapshot)['DBSnapshots'][0]['Status']
            if current_status == 'available' :
                print("SNAPSHOT CREATED OF: ",rds_instances)
                print("======================================================")
                break
            elif current_status == 'failed':
                print("SNAPSHOT FAILED OF: ",rds_instances)
                print("======================================================")
                break




def main():
    x=RDSSnapShots()
    #print(x.INSTANCES)
    for i in x.INSTANCES:
        x.create_snapshots(i)



if __name__ == "__main__":
    main()