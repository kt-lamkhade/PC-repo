import boto3

session = boto3.session.Session()
s3 = session.resource('s3')
for bucket in s3.buckets.all():
  print(bucket.name)

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