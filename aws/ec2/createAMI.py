'''

Description:
The Script creates AMI and snapshots of the Instances having the followings tags:
   -->ibm_imi_managed = Yes

And tags newly created Amis and snapshots with the following tags:
   -->ibm_imi_managed = Yes
   -->Purpose = Backup Solution for Patching Activity

'''
import boto3
import datetime
import time
ec2_client = boto3.client('ec2')

#Function to create AMI of the instance
def amiCreate(instID):
	desc="AMI created from "+str(instID)
	response = ec2_client.create_image(
	Description=desc,
	InstanceId=instID,
	Name=desc,
	NoReboot=True)
	return(response['ImageId'])

#Function to create the tags for the newly created AMI
def addTagsAMI(amiID,instID):
	name="AMI created from "+str(instID)
	response = ec2_client.create_tags(
	Resources=[amiID],
	Tags=[
        {
            'Key': 'Name',
            'Value': name
        },
        {
            'Key': 'ibm_imi_managed',
            'Value': 'Yes'
        },
	{
            'Key': 'Purpose',
            'Value': 'Backup Solution for Patching Activity'
        },

    ]
)

#Function to create the tags for the newly created snapshots from the AMI
def addTagsnap(amiID,snaplist):
	name="Snapshot created as apart of AMI Creation : "+str(amiID)
	response = ec2_client.create_tags(
	Resources=snaplist,
	Tags=[
        {
            'Key': 'Name',
            'Value': name
        },
        {
            'Key': 'ibm_imi_managed',
            'Value': 'Yes'
        },
	{
            'Key': 'Purpose',
            'Value': 'Backup Solution for Patching Activity'
        },

    ]
)



def lambda_handler(event, context):
	amilist=[]
	reservations = ec2_client.describe_instances(Filters=[
        {
            'Name': 'tag:ibm_imi_managed',
            'Values': [
                'Yes',
            ]
        },
    ]).get('Reservations',[])
	instances = sum([[i for i in r['Instances']]for r in reservations], [])
	instancesCount = len(instances)
	print ("Number of Instances Present: "+str(instancesCount))
	for instance in instances:
		instID=instance['InstanceId']
		amiID=amiCreate(instID)
		amilist.append(amiID)
		addTagsAMI(amiID,instID)
	
	print("Number of AMI's created: "+str(len(amilist)))
	print("AMI List : "+str(amilist))
	#The function is put on 20 seconds sleep 
	time.sleep(20)
	for var in amilist:
		print ("AMI ID : " +str(var))
		snaplist=[]
		valdesc="*"+str(var)+"*"
		snapresult=ec2_client.describe_snapshots(
    		Filters=[
       		 {
          	  'Name': 'description',
          	  'Values': [
              	   valdesc,
           		 ]
        		},
   		 ],)
		for i in range(len(snapresult['Snapshots'])):
			snaplist.append(snapresult['Snapshots'][i]['SnapshotId'])
		print("Snapshot List :"+str(snaplist))
		addTagsnap(var,snaplist)

