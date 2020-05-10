# List all lambda function using the pagination
import boto3
from datetime import datetime, timedelta
lambda_client = boto3.client('lambda')
paginator = lambda_client.get_paginator('list_functions')
cnt = 1
page_iterator = paginator.paginate()
for items in page_iterator:
    for functions in items['Functions']:
        print(cnt, functions['FunctionName'])
