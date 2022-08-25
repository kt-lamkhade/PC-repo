#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program automates the creation of AWS EDR Replication Configuration
based on an input JSON file
"""

import json
import os
import sys
import logging

import boto3
from botocore.exceptions import ClientError

from logger import CustomFormatter

# Logger for helper module
logger = logging.getLogger("AWS-EDRS")
logger.setLevel(logging.DEBUG)

# Create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(CustomFormatter())
logger.addHandler(console_handler)

arguments = sys.argv


def init_edr_service():
    """
    Initialize the DR Service for an account for first time
    """    
    client = session.client('drs')
    init_response = client.initialize_service()
    logger.info(init_response)


def create_replication_template():
    """
    Create a Replication Template which will be used for instance
    replcation from source to DR region
    """

    client = session.client('drs')
    response = client.create_replication_configuration_template(
        associateDefaultSecurityGroup=True,
        bandwidthThrottling=0,
        createPublicIP=False,
        dataPlaneRouting='PRIVATE_IP',
        defaultLargeStagingDiskType='ST1',
        ebsEncryption=config.get('ebsEncryption'),
        # ebsEncryptionKeyArn=config.get('ebsEncryptionKeyArn'),
        pitPolicy=config.get('pitPolicy'),
        replicationServerInstanceType='t2.micro',
        replicationServersSecurityGroupsIDs=config.get('replicationServerSGIds'),
        stagingAreaSubnetId=config.get('stagingAreaSubnetId'),
        stagingAreaTags={
            'Name': 'drs-poc-staging'
        },
        tags={
            'Name': 'drs-poc'
        },
        useDedicatedReplicationServer=False
    )

    logger.info("Created replication template...")
    logger.info(response)
    
def test_module():
    """
    Temporary function to test random feaures
    """
    logger.info("Creating S3 session client")
    try:
        s3_client = session.resource('s3')
        for each_bu in s3_client.buckets.all():
            print(each_bu.name)

        logger.info("Completed Client creation")
    except ClientError as err:
        logger.error(err)
        logger.warning("Check if the libraries are installed")


def get_session(profile, role_arn, region, session_name):
    session = boto3.Session(profile_name=profile)
    s3_client = session.resource('s3')
    for each_bu in s3_client.buckets.all():
        print(each_bu.name)
    """
    Function assumes a role and creates a session for SDK operations
    Args:
        profile         (str)   :   AWS Profile to be used
        role_arn        (str)   :   Assume Role's ARN
        region          (str)   :   Region in whcih session is required
        session_name    (str)   :   A name for the session
    """
    """try:"""


"""
        sts_client = session.client('sts')
        logger.info("stsClient: - ", sts_client)

        sts_response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name
        )
        logger.info("sts_response: - ", sts_response)
    except NameError as err:
        logger.error(err)
        sys.exit(1)
    except ClientError as err:
        logger.error(err)
        sys.exit(1)
    session = boto3.session.Session(
        aws_access_key_id=sts_response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=sts_response["Credentials"]["SecretAccessKey"],
        aws_session_token=sts_response["Credentials"]["SessionToken"],
        region_name=region
    )
    return session
"""

if __name__ == '__main__':
    logger.info("Reading input file")
    with open('sample_input.json') as input_file:
        config = json.load(input_file)    
    assume_role_arn = config.get('assumeRoleArn')
    logger.info("Initialize boto3 session")
    session = get_session(
        profile='aws_credentials',
        role_arn=assume_role_arn,
        region=config.get('region'),
        session_name='aws-drs-session'
    )

    logging.info(f"Call {arguments[1]} action")
    fire.Fire(
        {
            'init': init_edr_service,
            'create': create_replication_template,
            'update': update_replication_config,
            'delete': delete_replication_config,
            'test': test_module
        }
    )