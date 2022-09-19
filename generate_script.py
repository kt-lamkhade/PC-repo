from asyncore import write
import os
import json

map  = {
    'region': os.environ['AWS_REGION'],
    "stagingAreaSubnetId": os.environ['SUBNET_ID'],
    "edrClass": os.environ['EDR_CLASS'],
    "replicationServerSGIds": os.environ['SG_ID'].split(',')
}
with open('tmpfile.json', 'w') as outfile:
    json.dump(map, outfile)