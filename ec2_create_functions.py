
import boto3
import sys
import time
#NAME = input("Please provide server name: ")
#INSTANCE_TYPE = input("Please provide instance type. e.g: t2.micro : ")
ec2 = boto3.resource("ec2", region_name=AWS_REGION)
ec2_client = boto3.client("ec2", region_name=AWS_REGION)
s3_client = boto3.client("s3", region_name=AWS_REGION)
def create_instance():
    
    New_instances = ec2_client.run_instances(
                                        ImageId="ami-0d91a7c2ab81726af",
                                        MinCount=1,
                                        MaxCount=1,
                                        InstanceType= INSTANCE_TYPE,
                                        KeyName="ec2-keypair",
                                        TagSpecifications=[
                                            {
                                                'ResourceType': "instance",
                                                'Tags': [
                                                    {
                                                        'Key': 'Name',
                                                        'Value': NAME
                                                    }
                                                    ]
                                            }
                                        ],
                                        NetworkInterfaces=[
                                            {
                                                "DeviceIndex": 0,
                                                "AssociatePublicIpAddress": True
                                                
                                            }
                                            ]
                                        )
    return New_instances

def bucket_create(bucket_name):
    New_bucket = s3_client.create_bucket(Bucket=bucket_name)
    return New_bucket
    
    
      
def details():
    New_instances = create_instance()
    ec2_Name = New_instances['Instances'][0]['Tags']
    ec2_id = New_instances['Instances'][0]['InstanceId']
    ec2_zone = New_instances['Instances'][0]['Placement']
    ec2_private_ip = New_instances['Instances'][0]['PrivateIpAddress']
    print("Instance Created:\n")
    print("\nEC2 Instances ID : ", ec2_id, "\nInstance Tag Name : ", ec2_Name[0]['Value'], "\nAvailability Zone : ", ec2_zone['AvailabilityZone'], "\n Private IP : ", ec2_private_ip, "\n")
    
    bucket_create(bucket_name=New_instances['Instances'][0]['InstanceId'])

details()
