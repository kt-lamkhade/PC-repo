#!/usr/bin/env bash

# DO NOT RENAME THE SCRIPT
# This script is a template which has place holders for AWS Credentials

set -e

AGENT_SCRIPT=/home/itmpjenk/aws-replication-installer-init.py

# Run Agent Installer
sudo /home/itmpjenk/aws-replication-installer-init.py \
    --region DR_REGION \
    --aws-access-key-id EDR_ACCESS_KEY_ID \
    --aws-secret-access-key EDR_SECRET_ACCESS_KEY \
    --aws-session-token EDR_SESSION_TOKEN \
    --endpoint DRS_ENDPOINT \
    --s3-endpoint S3_ENDPOINT \
    --no-prompt &&

# Remove script after agent installation
[ -f $AGENT_SCRIPT ] && rm $AGENT_SCRIPT