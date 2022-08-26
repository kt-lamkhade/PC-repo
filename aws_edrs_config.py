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
import fire

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
    logger.info("start##########################")    
    client = session.client('drs')
    init_response = client.initialize_service()
    logger.info(init_response)
    logger.info("End##########################")


def create_replication_template():
    """
    Create a Replication Template which will be used for instance
    replcation from source to DR region
    """
    logger.info("Creating replication template......................")
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

    logger.info("Created replication template............")
    logger.info(response)

def get_replication_config():
    """
    Get the existing replication configurations
    """
    ##PLACE_HOLDER##


def update_replication_config():
    """
    Update and existing replication config
    """
    ##PLACE_HOLDER##


def delete_replication_config():
    """
    Delete and existing replication configuration
    """
    ##PLACE_HOLDER##
    
def test_module():
    logger.info("Creating S3 session client")
    """
    Temporary function to test random feaures
    """
    
    try:
        s3_client = session_call.resource('s3')
        for each_bu in s3_client.buckets.all():
            print(each_bu.name)

        logger.info("Completed Client creation")
    except ClientError as err:
        logger.error(err)
        logger.warning("Check if the libraries are installed")

def get_session(profile, region, session_name):
    try:
        session = boto3.session.Session(profile_name=profile)
        stsClient = session.client("sts")
    except NameError as err:
        logger.error(err)
        sys.exit(1)
    except ClientError as err:
        logger.error(err)
        sys.exit(1)
    """
    session_return = boto3.session.Session(
        aws_access_key_id=session["Credentials"]["AccessKeyId"],
        aws_secret_access_key=session["Credentials"]["SecretAccessKey"],
        aws_session_token=session["Credentials"]["SessionToken"]
    )"""

    logger.info("_____________", "${session}","_____________", "${region}","_____________", "${session_name}")
    return session



if __name__ == '__main__':  
    logger.info("Initialize boto3 session")
    session_call = get_session(
        profile='aws_credentials',
        region='us-east-1',
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