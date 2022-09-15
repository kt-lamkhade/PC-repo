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
    client = session_call.client('drs')
    init_response = client.initialize_service()
    logger.info(init_response)
 


def create_replication_template():
    """
    Create a Replication Template which will be used for instance
    replcation from source to DR region
    """
    client = session_call.client('drs')
    response = client.create_replication_configuration_template(
        associateDefaultSecurityGroup=True,
        bandwidthThrottling=0,
        createPublicIP=False,
        dataPlaneRouting='PRIVATE_IP',
        defaultLargeStagingDiskType='ST1',
        ebsEncryption=config.get('ebsEncryption'),
        replicationServerInstanceType='t2.micro',
        replicationServersSecurityGroupsIDs=config_sg.get('replicationServerSGIds'),
        stagingAreaSubnetId=config_env.get('stagingAreaSubnetId'),
        stagingAreaTags={
            'Name': 'drs-poc-staging'
        },
        tags={
            'Name': 'drs-poc'
        },
        pitPolicy=config.get('pitPolicy'),
        useDedicatedReplicationServer=False
        )
    logger.info(response)

def get_replication_config():
    """
    Get the existing replication configurations
    """
    ##PLACE_HOLDER#


def update_replication_config():
    """
    Update and existing replication config
    """
    ##PLACE_HOLDER##


def delete_replication_config():
    """
    Delete and existing replication configuration
    
    client = session_call.client('drs')
    responce = client.delete_replication_configuration_template(
        
    )
    logger.info(responce)
    ##PLACE_HOLDER##
    """
def test_module():
    """logger.info(configVar.get('subneyId'))
    
    Temporary function to test random feaures
    
    
    try:
        s3_client = session_call.resource('s3')
        for each_bu in s3_client.buckets.all():
            print(each_bu.name)

        logger.info("Completed Client creation")
    except ClientError as err:
        logger.error(err)
        logger.warning("Check if the libraries are installed")
    """
def get_session(profile, region, session_name):
    try:
        session = boto3.session.Session(
            profile_name=profile,
            region_name=region
            )
    except NameError as err:
        logger.error(err)
        sys.exit(1)
    except ClientError as err:
        logger.error(err)
        sys.exit(1)

    return session



if __name__ == '__main__': 
    logger.info("Initialize boto3 session")
    with open('sample_input.json') as input_file:
        config = json.load(input_file)  
    with open('tmpfile.json') as input_env_file:
        config_env = json.load(input_env_file)
    with open('tmpsgfile.json') as input_sg:
        config_sg = json.load(input_sg)
        
    session_call = get_session(
        profile='aws_credentials',
        region=config_env.get('region'),
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
   