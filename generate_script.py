from asyncore import write
import os
import json

    edrClass = config_env.get('edrClass')
    if edrClass == "EDRCLASS1":
        pitPolicy = config.get('pitPolicy1')
    else:
        pitPolicy = config.get('pitPolicy2')
    ec2_client = session_call.client('ec2')
    filters = [{'Name':'tag:Name', 'Values':['staging-area*']}]

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



map  = {
    'region': os.environ['AWS_REGION'],
    "stagingAreaSubnetId": os.environ['SUBNET_ID'],
    "edrClass": os.environ['EDR_CLASS'],
    "replicationServerSGIds": os.environ['SG_ID'].split(',')
}
with open('tmpfile.json', 'w') as outfile:
    json.dump(map, outfile)