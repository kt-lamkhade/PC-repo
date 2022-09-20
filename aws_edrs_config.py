#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program automates the creation of AWS EDR Replication Configuration
based on an input JSON file
"""

import json
import os
from readline import append_history_file
import sys
import logging
from urllib import response
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
    edrClass = config_env.get('edrClass')
    if edrClass == "EDRCLASS1":
        pitPolicy = config.get('pitPolicy1')
    else:
        pitPolicy = config.get('pitPolicy2')

    client = session_call.client('drs')
    response = client.create_replication_configuration_template(
        associateDefaultSecurityGroup=True,
        bandwidthThrottling=0,
        createPublicIP=False,
        dataPlaneRouting='PRIVATE_IP',
        defaultLargeStagingDiskType='ST1',
        ebsEncryption=config.get('ebsEncryption'),
        replicationServerInstanceType='t2.micro',
        replicationServersSecurityGroupsIDs=config_env.get('replicationServerSGIds'),
        stagingAreaSubnetId=config_env.get('stagingAreaSubnetId'),
        stagingAreaTags={
            'Name': 'drs-poc-staging'
        },
        tags={
            'Name': 'drs-poc'
        },
        pitPolicy=pitPolicy,
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

    for i in rep_template['items']:
        rct_Id = i["replicationConfigurationTemplateID"]
    logger.info(rct_Id)
  
    client = session_call.client('drs')
    response = client.update_replication_configuration_template(
    associateDefaultSecurityGroup=True,
    bandwidthThrottling=0,
    createPublicIP=False,
    dataPlaneRouting='PRIVATE_IP',
    defaultLargeStagingDiskType='GP2',
    ebsEncryption=config.get('ebsEncryption'),
    pitPolicy=config.get('pitPolicy'),
    replicationConfigurationTemplateID=rct_Id,
    replicationServerInstanceType='t2.micro',
    replicationServersSecurityGroupsIDs=config_env.get('replicationServerSGIds'),
    stagingAreaSubnetId=config_env.get('stagingAreaSubnetId'),
    stagingAreaTags={
        'Name': 'drs-poc-staging'
    },
    useDedicatedReplicationServer=False
)


def delete_replication_config():
    """
    Delete and existing replication configuration
    """
    for i in rep_template['items']:
        rct_Id = i["replicationConfigurationTemplateID"]
        
    client = session_call.client('drs')
    response = client.delete_replication_configuration_template(
    replicationConfigurationTemplateID=rct_Id
    )
    logger.info(response)

 
def test_module():
        client = session_call.client('drs')
        response = client.describe_replication_configuration_templates()
        logger.info(response)   
    
"""
    logger.info(configVar.get('subneyId'))
    Temporary function to test random feaures
    
    edrClass = config_env.get('edrClass')
    if edrClass == "EDRCLASS1":
        pitPolicy = config.get('pitPolicy1')
    else:
        pitPolicy = config.get('pitPolicy2')
    ec2_client = session_call.client('ec2')
    filters = [{'Name':'tag:Name', 'Values':['stajing*']}]

    print("VPC ID:-")
    for vpc in ec2_client.describe_vpcs(Filters=filters)['Vpcs']:
        print(vpc['VpcId'])

    print("Subnet:-")
    sn_all = ec2_client.describe_subnets(Filters=filters)
    for sn in sn_all['Subnets'] :
        if sn['VpcId'] == "vpc-0ec4fd6ab42babd17":
            print(sn['SubnetId'])

    print("Security Group:-")
    sg_all = ec2_client.describe_security_groups(Filters=filters)
    sgID = []
    for sg in sg_all['SecurityGroups']:
        if sg['VpcId'] == "vpc-0ec4fd6ab42babd17":
            sgID.append(sg['GroupId'])
    
    print(sgID)
    """

    
def get_session(profile, region, session_name):
    try:
        session = boto3.session.Session(profile_name=profile)
        stsClient = session.client("sts")
        assumed_role = stsClient.assume_role(
            RoleArn="arn:aws:iam::719446341377:role/drsRole",
            RoleSessionName=session_name
        )
    except NameError as err:
        logger.error(err)
        sys.exit(1)
    except ClientError as err:
        logger.error(err)
        sys.exit(1)

    access_keys = boto3.session.Session(
        aws_access_key_id=assumed_role["Credentials"]["AccessKeyId"],
        aws_secret_access_key=assumed_role["Credentials"]["SecretAccessKey"],
        aws_session_token=assumed_role["Credentials"]["SessionToken"],
            region_name=region
    )

    return access_keys



if __name__ == '__main__': 
    logger.info("Initialize boto3 session")
    with open('sample_input.json') as input_file:
        config = json.load(input_file)  
    with open('tmpfile.json') as input_env_file:
        config_env = json.load(input_env_file)
    with open('replication_template.json') as rep_template_file:
        rep_template = json.load(rep_template_file)
        
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
   