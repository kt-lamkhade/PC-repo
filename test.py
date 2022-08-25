import boto3

session = boto3.session.Session(profile_name=admin1)
s3_client = session.resource('s3')
for each_bu in s3_client.buckets.all():
    print(each_bu.name)

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