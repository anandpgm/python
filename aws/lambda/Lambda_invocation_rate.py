# This will give the all lambda invocation rate for the last one day (us-west-2)
import boto3
from datetime import datetime, timedelta
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
        try:
                    response = cloudwatch.get_metric_statistics(
                    Namespace='AWS/Lambda',
                    Dimensions=[
                        {
                            'Name': 'FunctionName',
                            'Value': functions['FunctionName']
                        }

                    ],
                    MetricName='Invocations',
                    StartTime=datetime.now() - timedelta(days=1),
                    EndTime=datetime.now(),
                    Period=seconds_in_one_day,
                    Statistics=[
                        'Sum'
                    ],
                    Unit='Count'
                )

                    print(cnt, functions['FunctionName'], response['Datapoints'][0]['Sum'])
        except Exception as e:
                    print(cnt, functions['FunctionName'], '0')