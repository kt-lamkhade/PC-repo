import boto3
import json
import os
import sys
import logging

import fire
from botocore.exceptions import ClientError

from logger import CustomFormatter
def create_backend_config(credentials):
    print(credentials)
    """credentials.update({
        'region_name': 'eu-east-1'
    })
    secrets_client = boto3.client(**credentials)
    logging.info('Getting terraform backend config file')
    session = boto3.session.Session(profile_name="aws_credentials")
    print("##############", session)
    s3_client = session.resource('s3')
    for each_bu in s3_client.buckets.all():
        print(each_bu.name)
"""

def assume_infra_role():
    print("Inside assume_infra_role")
    infra_assume_role = 'arn:aws:iam::719446341377:role/my_sts'
    session = boto3.Session(profile_name='aws_credentials')
    sts_client = session.client('sts')
    sts_response = sts_client.assume_role(
        RoleArn=infra_assume_role,
        RoleSessionName='AWSDaytwoAutomation'
    )

    session = boto3.session.Session( 
        'aws_access_key_id': sts_response['Credentials']['AccessKeyId'],
        'aws_secret_access_key': sts_response['Credentials']['SecretAccessKey'],
        'aws_session_token': sts_response['Credentials']['SessionToken']
    )
    return session

if __name__ == '__main__':
    credentials = assume_infra_role()
    create_backend_config(credentials)

"""
sts_client = boto3.client('sts')

assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::719446341377:role/AssumeRoleSession1",
    RoleSessionName="AssumeRoleSession1"
)

credentials=assumed_role_object['Credentials']

s3_resource=boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)

for bucket in s3_resource.buckets.all():
    print(bucket.name)
    """