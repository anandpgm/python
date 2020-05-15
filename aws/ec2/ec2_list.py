# Print Instance id and volume id
import boto3
from pprint import pprint
aws_msg_con = boto3.session.Session(profile_name='default')
aws_con_ec2 = aws_msg_con.client(service_name='ec2', region_name='us-west-2')
response = aws_con_ec2.describe_instances()
print("Using client method")
for items in response['Reservations']:
    for instances in items['Instances']:
        #pprint(instances['InstanceId'])
        for disk in instances['BlockDeviceMappings']:
            print(instances['InstanceId'], disk['Ebs']['VolumeId'])

print("Using resources")
aws_con_ec2_ser = aws_msg_con.resource(service_name='ec2', region_name="us-west-2")
response = aws_con_ec2_ser.instances.all()
for items in response:
    #print(dir(items))
    print(items.id)
for disks in aws_con_ec2_ser.volumes.all():
        print(disks.volume_id)
# instance_iterator=aws_con_ec2_ser.Instances.all()
# print(dir(instance_iterator))
