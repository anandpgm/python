#List of each lambda concurrency limit
import boto3
lambda_client = boto3.client('lambda')
cloudwatch = boto3.client('cloudwatch')
paginator = lambda_client.get_paginator('list_functions')
cnt = 0
page_iterator = paginator.paginate()
seconds_in_one_day = 86400  # used for granularity
for items in page_iterator:
    for functions in items['Functions']:
        #print(cnt, functions['FunctionName'])
        cnt = cnt+1
        response = lambda_client.get_function_concurrency(FunctionName=functions['FunctionName'])
        try:
                    print(cnt, functions['FunctionName'], response['ReservedConcurrentExecutions'] )
        except Exception as e:
                    print(cnt,  functions['FunctionName'], "0" )