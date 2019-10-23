'''


Description:
The Script deletes AMI and snapshots of the Instances having the followings tags:
   -->ibm_imi_managed = Yes
   -->Purpose = Backup Solution for Patching Activity

'''

import boto3
import datetime
import time
ec2_client = boto3.client('ec2')

#Function to delete the AMI
def amiDelete(amiID):
	
	response = ec2_client.deregister_image(
        ImageId=amiID)
	
#Function to delete the Snapshot
def snapshotDelete(snapID):

	response = ec2_client.delete_snapshot(
	SnapshotId=snapID)
	

def lambda_handler(event, context):
	amilist=[]
	amiresult = ec2_client.describe_images(
    		Filters=[
       		 {
          	  'Name': 'tag:ibm_imi_managed',
          	  'Values': [
              	   'Yes',
           		 ]
        		},
		{
          	  'Name': 'tag:Purpose',
          	  'Values': [
              	   'Backup Solution for Patching Activity',
           		 ]
        		}
   		 ])
    
	for i in range(len(amiresult['Images'])):
		amilist.append(amiresult['Images'][i]['ImageId'])
	print("Number of AMI's present: "+str(len(amilist)))
	print("AMI List : "+str(amilist))
	for amiID in amilist:
		amiDelete(amiID)
	#The function is put on 20 seconds sleep
	time.sleep(20)
	
	snaplist=[]
	snapresult=ec2_client.describe_snapshots(
    	Filters=[
       		 {
          	  'Name': 'tag:ibm_imi_managed',
          	  'Values': [
              	   'Yes',
           		 ]
        		},
		{
          	  'Name': 'tag:Purpose',
          	  'Values': [
              	   'Backup Solution for Patching Activity',
           		 ]
        		}
   		 ])
	for j in range(len(snapresult['Snapshots'])):
			snaplist.append(snapresult['Snapshots'][j]['SnapshotId'])
	print("Number of Snapshot's Present: "+str(len(snaplist)))
	print("Snapshot List : "+str(snaplist))
	for snapID in snaplist:
		snapshotDelete(snapID)
