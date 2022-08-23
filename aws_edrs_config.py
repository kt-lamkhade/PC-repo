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

    init_edr_service()
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


create_replication_template()

