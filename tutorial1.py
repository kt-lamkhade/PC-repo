import boto3
aws_resource= boto3.resource("s3")
bucket=aws_resource.Bucket("kirantechnologytest")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'ap-east-1'
    },
)
