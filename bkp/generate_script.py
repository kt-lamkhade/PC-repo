#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This program generates temporary credentials to be used for agent installation
"""

import json
import sys
import logging
from os import environ

import boto3
from botocore.exceptions import ClientError

# Logger for helper module
logger = logging.getLogger("AWS-EDRS")
logger.setLevel(logging.DEBUG)

arguments = sys.argv

def get_session(profile, role_arn, session_name):
    """
    Function assumes a role and creates a session for SDK operations
    Args:
        profile         (str)   :   AWS Profile to be used
        role_arn        (str)   :   Assume Role's ARN
        session_name    (str)   :   A name for the session
    """
    try:
        session = boto3.session.Session(profile_name=profile)
        
        stsClient = session.client("sts")
        assumed_role = stsClient.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name
        )
    except NameError as err:
        logger.error(err)
        sys.exit(1)
    except ClientError as err:
        logger.error(err)
        sys.exit(1)

    tempCredentials = {
        "aws_access_key_id": assumed_role["Credentials"]["AccessKeyId"],
        "aws_secret_access_key": assumed_role["Credentials"]["SecretAccessKey"],
        "aws_session_token": assumed_role["Credentials"]["SessionToken"]
    }
    
    return tempCredentials

def generate_script(**kwargs):
    """
    Updates the agent installation script with AWS Credentials
    """
    with open('_agent_config.sh') as config_script:
        agent_script = config_script.read()
    
    agent_script = agent_script.replace('EDR_ACCESS_KEY_ID', credentials.get('aws_access_key_id'))
    agent_script = agent_script.replace('EDR_SECRET_ACCESS_KEY', credentials.get('aws_secret_access_key'))
    agent_script = agent_script.replace('EDR_SESSION_TOKEN', credentials.get('aws_session_token'))
    agent_script = agent_script.replace('DRS_ENDPOINT', dr_region_config.get('drsEndpoint'))
    agent_script = agent_script.replace('S3_ENDPOINT', dr_region_config.get('s3Endpoint'))
    agent_script = agent_script.replace('DR_REGION', dr_region_config.get('drRegion'))

    file_name = f"{fqdn}.sh"

    with open(file_name, 'w') as script_file:
        updated_script = script_file.write(agent_script)


if __name__ == '__main__':
    fqdn = arguments[1]   

    # Get host details forthe given FQDN
    logger.info("Reading host details file")
    with open('hostData.json') as hosts_file:
        host_data = json.loads(hosts_file.read())
        
    # print(f'HostData: {host_data}')
    assume_role_arn = host_data[fqdn]['Assume_Role_ARN']

    # Get Region mapping and Endpoint details
    with open('regionConfig.json') as reg_config:
       region_config = json.loads(reg_config.read())
    region = host_data[fqdn]['Region']
    dr_region_config = region_config.get(region)

    # Get temporary credentials
    logger.info("Initialize boto3 session")
    credentials = get_session(
        profile='itmp-tudeploy',
        role_arn=assume_role_arn,
        session_name='aws-edrs-temp-creds'
    )

    # Create agent_config from _agent_config.sh with updated session creds
    generate_script(
        credentials=credentials,
        host_data=host_data,
        dr_region_config=dr_region_config,
        fqdn=fqdn
        )