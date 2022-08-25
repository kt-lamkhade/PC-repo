import boto3
role_info = {
    'RoleArn': 'arn:aws:iam::719446341377:role/aws-service-role/drs.amazonaws.com/AWSServiceRoleForElasticDisasterRecovery',
    'RoleSessionName': 'AWSServiceRoleForElasticDisasterRecovery'
}

client = boto3.client('sts')
credentials = client.assume_role(**role_info)

session = boto3.session.Session(
    aws_access_key_id=credentials['Credentials']['AccessKeyId'],
    aws_secret_access_key=credentials['Credentials']['SecretAccessKey'],
    aws_session_token=credentials['Credentials']['SessionToken']
)