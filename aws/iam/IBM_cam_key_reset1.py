
#Python programe to recreate cam user access key

import boto3
filename="/tmp/Iam_Cam.csv"
csv_file = open(filename,'a+')
csv_file.write("%s,%s,%s\n"%('AccountNumber','accesskey','secretkey'))

for i in range(27,57):
	pro_name="prod"+str(i) 
	print "Account Number :" + str(i)
	session = boto3.Session(profile_name=pro_name)
	owner=session.client('sts').get_caller_identity()['Account']

	iam_client = session.client('iam')

#Getting the access key

	response = iam_client.list_access_keys(UserName='cam')
    	access_key=(response['AccessKeyMetadata'][0]['AccessKeyId'])


# Deleting the access key

	iam_client.delete_access_key(UserName='cam',AccessKeyId=access_key)

#Creating the accesskey

	response = iam_client.create_access_key(UserName='cam')

	newaccesskey = response['AccessKey']['AccessKeyId']
	newsecretkey = response['AccessKey']['SecretAccessKey']
	csv_file.write("%s,%s,%s\n"%(owner,newaccesskey,newsecretkey))
