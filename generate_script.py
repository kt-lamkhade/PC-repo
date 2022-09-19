from asyncore import write
import os
import json
import sys


map  = {
    'region': os.environ['AWS_REGION'],
    "stagingAreaSubnetId": os.environ['SUBNET_ID'],
    "edrClass": os.environ['EDR_CLASS']
}
with open('tmpfile.json', 'w') as outfile:
    json.dump(map, outfile)


map2 = {
    "sg_id": os.environ['SG_ID']
}
with open('tmpsgfile.json', 'w') as outfile:
    json.dump(map2, outfile) 
